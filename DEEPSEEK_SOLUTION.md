# DeepSeek Architecture Analysis — evro661

> Generated: 2026-05-02 | Event: May 8-9, 2026 (6 days away)

---

## Critical Context

**Time constraint: 6 days until event.** This is a **minimum viable product** sprint, not a clean-architecture exercise. Every recommendation below is sorted by impact-per-hour.

---

## 1. Project Structure (set up in ~1 hour)

```
evro661/
├── public/
│   ├── videos/
│   │   ├── footbolchik_compressed.mp4   ← compressed version
│   │   └── footbolchik_mobile.mp4       ← 720p mobile version
│   ├── images/
│   │   ├── logo.svg
│   │   ├── sheep.png
│   │   └── barn-doors.jpg
│   └── favicon.ico
├── src/
│   ├── components/
│   │   ├── layout/
│   │   │   ├── Header.jsx
│   │   │   ├── Footer.jsx
│   │   │   └── Navigation.jsx
│   │   ├── pages/
│   │   │   ├── HomePage.jsx          ← Appmain Three.js logic
│   │   │   ├── EventPage.jsx         ← master orchestrator
│   │   │   └── ArchivePage.jsx
│   │   ├── features/
│   │   │   ├── Fundraiser/
│   │   │   │   └── AppFundraiser.jsx
│   │   │   ├── Lineup/
│   │   │   │   ├── AppLineup.jsx
│   │   │   │   └── LineupData.js     ← extract artist data here
│   │   │   ├── Game/
│   │   │   │   ├── Appfootball.jsx
│   │   │   │   ├── GameEngine.js     ← canvas physics
│   │   │   │   └── Physics.js
│   │   │   └── ThreeScene/
│   │   │       ├── Chamber.jsx
│   │   │       ├── DoorAnimation.js
│   │   │       └── Shaders.js
│   │   └── shared/
│   │       ├── VideoBackground.jsx
│   │       ├── AudioToggle.jsx
│   │       └── LoadingSpinner.jsx
│   ├── hooks/
│   │   ├── useAudio.js
│   │   ├── useScrollAnimation.js
│   │   └── useMediaQuery.js
│   ├── styles/globals.css
│   ├── App.jsx
│   └── main.jsx
├── package.json
├── vite.config.js
├── tailwind.config.js
└── .gitignore
```

---

## 2. Build Tooling — Use Vite

```bash
npm create vite@latest evro661 -- --template react
npm install react-router-dom react-intersection-observer three
npm install -D tailwindcss @tailwindcss/vite
```

**Why Vite over CRA:** 10× faster HMR, better Three.js tree-shaking, native ESM.

```js
// vite.config.js
import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

export default defineConfig({
  plugins: [react()],
  build: {
    chunkSizeWarningLimit: 1000,
    rollupOptions: {
      output: {
        manualChunks: {
          three: ['three'],
          game: ['./src/components/features/Game/Appfootball.jsx']
        }
      }
    }
  }
})
```

---

## 3. Wiring the 4 Components Together

### App.jsx — Router

```jsx
import { BrowserRouter, Routes, Route } from 'react-router-dom'
import { Suspense, lazy } from 'react'
import LoadingSpinner from './components/shared/LoadingSpinner'

const HomePage  = lazy(() => import('./components/pages/HomePage'))
const EventPage = lazy(() => import('./components/pages/EventPage'))
const ArchivePage = lazy(() => import('./components/pages/ArchivePage'))

export default function App() {
  return (
    <BrowserRouter>
      <Suspense fallback={<LoadingSpinner />}>
        <Routes>
          <Route path="/"        element={<HomePage />} />
          <Route path="/event"   element={<EventPage />} />
          <Route path="/archive" element={<ArchivePage />} />
        </Routes>
      </Suspense>
    </BrowserRouter>
  )
}
```

### EventPage.jsx — Master Orchestrator

```jsx
import { useState, useEffect } from 'react'
import { useInView } from 'react-intersection-observer'
import AppFundraiser from '../features/Fundraiser/AppFundraiser'
import AppLineup     from '../features/Lineup/AppLineup'
import Appfootball   from '../features/Game/Appfootball'
import VideoBackground from '../shared/VideoBackground'
import AudioToggle   from '../shared/AudioToggle'

export default function EventPage() {
  const [showGame, setShowGame]     = useState(false)
  const [audioEnabled, setAudio]    = useState(false)
  const { ref: gameRef, inView }    = useInView({ threshold: 0.1, triggerOnce: true })

  useEffect(() => { if (inView) setShowGame(true) }, [inView])

  return (
    <div className="relative min-h-screen bg-black">
      <VideoBackground src="/videos/footbolchik_compressed.mp4" opacity={0.5} audioEnabled={audioEnabled} />
      <header className="fixed top-0 z-50 w-full">
        <AudioToggle enabled={audioEnabled} onToggle={setAudio} />
      </header>
      <section id="fundraiser"><AppFundraiser /></section>
      <section id="lineup"><AppLineup /></section>
      <section id="game" ref={gameRef}>
        {showGame && <Appfootball />}
      </section>
    </div>
  )
}
```

---

## 4. Top Priority Bug Fixes

### Fix 1 — Three.js Memory Leak (Appmain.jsx)

Every unmount without cleanup leaks GPU memory and eventually crashes the tab.

```jsx
useEffect(() => {
  const renderer = new THREE.WebGLRenderer({ antialias: true })
  const scene    = new THREE.Scene()
  let animId

  const animate = () => {
    animId = requestAnimationFrame(animate)
    // render logic
  }
  animate()

  return () => {
    cancelAnimationFrame(animId)
    renderer.dispose()
    scene.traverse(obj => {
      obj.geometry?.dispose()
      if (Array.isArray(obj.material)) obj.material.forEach(m => m.dispose())
      else obj.material?.dispose()
    })
    renderer.domElement.remove()
  }
}, [])
```

### Fix 2 — Canvas Game Frame Limiting (Appfootball.jsx)

Without a frame cap the game burns 100% GPU on a 144Hz display.

```js
const FPS = 60
const frameInterval = 1000 / FPS
let lastFrameTime = 0

function gameLoop(timestamp) {
  const delta = timestamp - lastFrameTime
  if (delta >= frameInterval) {
    update(delta)
    render()
    lastFrameTime = timestamp
  }
  if (gameRunning) requestAnimationFrame(gameLoop)
}
```

### Fix 3 — Video Background (VideoBackground.jsx)

Pause video when off-screen, respect connection speed.

```jsx
import { useRef, useEffect, useState } from 'react'

export default function VideoBackground({ src, opacity, audioEnabled }) {
  const videoRef = useRef(null)
  const [resolvedSrc, setSrc] = useState(src)

  useEffect(() => {
    const conn = navigator.connection || {}
    if (['slow-2g', '2g'].includes(conn.effectiveType)) {
      setSrc(src.replace('.mp4', '_mobile.mp4'))
    }
  }, [src])

  useEffect(() => {
    const video = videoRef.current
    if (!video) return
    const observer = new IntersectionObserver(
      ([e]) => e.isIntersecting ? video.play().catch(() => {}) : video.pause(),
      { threshold: 0.1 }
    )
    observer.observe(video)
    return () => observer.disconnect()
  }, [])

  return (
    <video
      ref={videoRef}
      src={resolvedSrc}
      muted={!audioEnabled}
      loop playsInline preload="metadata"
      className="fixed inset-0 w-full h-full object-cover -z-10"
      style={{ opacity }}
    />
  )
}
```

---

## 5. Video File — The 25MB Problem

The `footbolchik.mp4` committed to git must be removed from git history and served from a CDN.

### Step 1 — Compress Locally

```bash
# Requires ffmpeg
ffmpeg -i footbolchik.mp4 -c:v libx264 -crf 28 -preset fast \
  -c:a aac -b:a 64k -movflags +faststart \
  public/videos/footbolchik_compressed.mp4

# Mobile 720p version
ffmpeg -i footbolchik.mp4 -vf scale=-2:720 -c:v libx264 -crf 30 \
  public/videos/footbolchik_mobile.mp4
```

### Step 2 — Remove from Git & Add to .gitignore

```bash
git rm --cached footbolchik.mp4
echo "*.mp4" >> .gitignore
echo "!*.mp4  # tracked by LFS" >> .gitignore
```

### Step 3 — Use Git LFS or CDN

```bash
# Git LFS (quickest)
git lfs install
git lfs track "*.mp4"
git add .gitattributes

# OR upload to Cloudinary/Bunny.net and use env var:
# VITE_VIDEO_URL=https://cdn.example.com/footbolchik.mp4
```

---

## 6. Mobile UX Fixes

```jsx
// iOS audio context must be resumed on user gesture
const initAudio = () => {
  const Ctx = window.AudioContext || window.webkitAudioContext
  if (!Ctx) return
  const ctx = new Ctx()
  document.addEventListener('touchstart', () => {
    if (ctx.state === 'suspended') ctx.resume()
  }, { once: true })
}

// Three.js — disable shadows + lower resolution on mobile
const isMobile = window.innerWidth < 768
const renderer = new THREE.WebGLRenderer({
  antialias: !isMobile,
  powerPreference: isMobile ? 'low-power' : 'high-performance'
})
renderer.setPixelRatio(Math.min(window.devicePixelRatio, isMobile ? 1.5 : 2))
if (isMobile) renderer.shadowMap.enabled = false

// Three.js — responsive camera
const handleResize = () => {
  const w = window.innerWidth, h = window.innerHeight
  camera.aspect = w / h
  camera.updateProjectionMatrix()
  renderer.setSize(w, h)
  camera.position.z = w < 768 ? 8 : 5
}
window.addEventListener('resize', handleResize)

// Canvas game — reduce particles on mobile
const PARTICLE_COUNT = window.innerWidth < 768 ? 8 : 20
```

### Three.js Fallback for Old/Low-end Devices

```jsx
const [threeError, setThreeError] = useState(false)

{threeError ? (
  <div className="h-screen bg-gradient-to-b from-amber-900 to-black flex items-center justify-center">
    <img src="/images/barn-doors.jpg" alt="евро661" className="max-h-full" />
  </div>
) : (
  <Suspense fallback={<LoadingSpinner />}>
    <ThreeScene onError={() => setThreeError(true)} />
  </Suspense>
)}
```

---

## 7. Step-by-Step 6-Day Plan

| Day | Date  | Focus | Key Tasks |
|-----|-------|-------|-----------|
| 1 | May 2 | Foundation | Vite setup, folder structure, compress video, extract LineupData.js |
| 2 | May 3 | Core components | Refactor Appmain into HomePage with cleanup, build EventPage orchestrator |
| 3 | May 4 | Performance | Frame limiting, Three.js cleanup, IntersectionObserver lazy loads |
| 4 | May 5 | Integration | Wire all 4 components, audio toggle, touch events, cross-browser test |
| 5 | May 6 | Production | Env vars, code splitting, meta tags, 404 page, Lighthouse audit |
| 6 | May 7 | Deploy | Vercel/Netlify deploy, domain, CDN, final mobile device test |
| 7 | May 8 | Event day | Monitor errors, be ready for hotfixes |

---

## 8. High-Risk Items & Mitigation

| Risk | Mitigation |
|------|-----------|
| Three.js crashes on mobile | Test on real iPhone/Android by Day 3, have static image fallback ready |
| iOS blocks video autoplay | Always set `muted` attribute, use `playsInline` |
| iOS blocks audio context | Unlock on first `touchstart` gesture |
| Canvas game 60fps on low-end | Cap at 30fps on mobile, object pool particles |
| High traffic on event night | Put Cloudflare in front, cache static assets aggressively |

---

## 9. Quick Wins (do these first)

1. `npm create vite@latest` — get a real build system in 5 minutes
2. `ffmpeg` compress the video — 25MB → ~3MB immediately
3. Extract artist data from `AppLineup.jsx` into `LineupData.js` — makes the component readable and editable
4. Add Three.js cleanup `return () => { ... }` — stops the single biggest source of crashes
5. Add `<meta>` tags for Instagram/Telegram link previews — huge for event promotion

---

*Analysis by DeepSeek R1 via multi-AI-collab MCP | Assembled 2026-05-02*
