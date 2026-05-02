# Implementation Plan — евро661
> DeepSeek architectural brief | 2026-05-02

---

## Project Structure (Vite)

```
evro661/
├── public/
│   ├── artists-data/          ← move from repo root after setup
│   │   └── {slug}/photo-1.jpg, video.mp4, bio.md
│   ├── textures/
│   │   ├── barn-door-wood.jpg
│   │   └── sheep-logo.png     ← евро+овечки PNG
│   └── fallbacks/
│       ├── placeholder-artist.jpg
│       └── default-video.mp4  ← footbolchik.mp4
├── src/
│   ├── components/
│   │   ├── layout/
│   │   │   └── Navbar.jsx             # logo + socials
│   │   ├── doors/
│   │   │   ├── BarnDoors.jsx          # Three.js wrapper
│   │   │   └── DoorScene.jsx          # scene logic
│   │   ├── event/
│   │   │   ├── EventHeader.jsx        # large logo + scroll shrink
│   │   │   ├── EventInfo.jsx          # date + location + mini-map
│   │   │   ├── EventDescription.jsx   # what is the event
│   │   │   ├── MapSection.jsx         # full map → Google Maps
│   │   │   └── TicketsButton.jsx
│   │   ├── lineup/
│   │   │   ├── LineupGrid.jsx         # 23 artists
│   │   │   ├── ArtistCard.jsx         # paper strip style
│   │   │   ├── ArtistSidebar.jsx      # photo left / video right
│   │   │   └── LineupBackground.jsx   # video bg switcher
│   │   ├── game/
│   │   │   ├── FootballGame.jsx       # canvas wrapper
│   │   │   ├── GameCanvas.jsx         # physics loop
│   │   │   └── GameToggle.jsx         # bottom-left button
│   │   ├── audio/
│   │   │   ├── AudioContext.jsx       # global audio state
│   │   │   ├── AudioPlayer.jsx        # auto-switch player
│   │   │   └── AudioToggle.jsx        # mute/unmute button
│   │   └── fundraiser/
│   │       └── FundraiserPoster.jsx   # 3D tilt card (AppFundraiser)
│   ├── pages/
│   │   ├── LandingPage.jsx            # barn doors
│   │   └── EventPage.jsx              # after doors open
│   ├── hooks/
│   │   ├── useScrollAnimation.js      # logo shrink
│   │   ├── useMapVisibility.js        # map icon hide
│   │   ├── useAudioManager.js         # track switching
│   │   └── useGameState.js            # game overlay
│   ├── data/
│   │   └── lineup/                    # already exists
│   ├── App.jsx
│   └── main.jsx
├── package.json
├── vite.config.js
└── tailwind.config.js
```

---

## Page Flow

```
/ (LandingPage)
  └── BarnDoors Three.js scene
      └── Click → doors open animation + sound
          └── navigate to /event

/event (EventPage) — single scrollable page:
  [full screen]  FootballGame (canvas, activated by bottom-left button)
  [scroll]       Large евро+овечки logo → shrinks top-left as you scroll
  [scroll]       EventInfo: date, location, mini-map click → scroll to map
  [scroll]       EventDescription
  [scroll]       LineupGrid (23 artists, paper strip cards)
                   ↳ click artist → photo sidebar left, video sidebar right
                   ↳ auto-switches audio player to artist track
  [scroll]       Big TICKETS button
  [scroll]       MapSection (full map, icon top-right disappears when here)

Fixed overlays (always visible):
  bottom-right   FundraiserPoster (3D tilt)
  bottom-left    AudioToggle + GameToggle buttons
  top-right      Map icon (hides when map section is in view)
  anywhere       AudioPlayer mini-bar (closeable)
```

---

## Gutting Appmain.jsx

Keep from the original:
- Three.js renderer setup
- Wooden chamber + two doors geometry
- Shader-based warm light through door gap
- `Dive In` click handler → door opening animation
- Web Audio API sub-bass sound
- Bloom post-processing
- White flash transition

**Delete entirely:**
- All portfolio sections (about, projects, contact)
- Inner navigation
- Any content that isn't the door entrance

Export only: `<BarnDoors onEnter={fn} />`

---

## Audio System

```jsx
// AudioContext.jsx — global provider
const { playTrack, togglePlay, isPlaying } = useAudio()

// In LineupGrid — when artist clicked:
onArtistClick(artist.trackSrc)  // → AudioContext.playTrack()

// AudioPlayer shows as mini-bar (closeable):
// [▶ ████░░░░ ✕]   fixed bottom-right

// AudioToggle (bottom-left, next to game button):
// mutes/unmutes entire site audio
```

Audio switches automatically when a new artist is clicked. Player can be minimized or closed. Sound toggle controls all site audio globally (lineup videos + player).

---

## Game Integration

```
Game is always mounted but only renders when active.

Bottom-left button → toggleGame()
  inactive: canvas hidden, ball resets
  active:   canvas fixed inset-0 z-30, physics running, click to kick

Game toggle and sound toggle sit side by side bottom-left.
```

---

## Artist Data Wiring

After running `rename-artists.sh` and moving `artists-data/` to `public/`:

```js
// artists.js fields used by components:
{
  slug: 'angst',
  name: 'ANGST',
  img: '/artists-data/angst/photo-1.jpg',   // served from public/
  vid: '/artists-data/angst/video.mov',
  bio: '/artists-data/angst/bio.md',         // fetched on demand
  track: '/artists-data/angst/track.mp3',    // if exists
}
```

Missing materials → fallback:
- No photo → `/fallbacks/placeholder-artist.jpg`
- No video → sidebar just shows photo only
- No bio → show artist name only
- No track → no audio switch on click

---

## Map Section

- Mini-map: Google Maps embed iframe, always visible in EventInfo
- Click mini-map → smooth scroll to `#map-section`
- Full map section: larger iframe + "Open in Google Maps" link
- Map icon top-right: disappears via `IntersectionObserver` when `#map-section` enters viewport

```js
// useMapVisibility.js
const observer = new IntersectionObserver(([entry]) => {
  setShowMapIcon(!entry.isIntersecting)
}, { threshold: 0.1 })
observer.observe(document.getElementById('map-section'))
```

---

## Logo Scroll Animation

```js
// useScrollAnimation.js
scroll 0 → 1vh:     logo centered, full size, scale(1)
scroll 1vh → 2vh:   logo transitions top-left, shrinks
scroll > 2vh:       logo fixed top-left, scale(0.3), opacity 0.7
```

---

## 6-Day Build Order

| Day | Date | What to build |
|-----|------|---------------|
| **1** | May 2 | `npm create vite`, project structure, Navbar, BarnDoors (gut Appmain.jsx), basic routing |
| **2** | May 3 | EventPage skeleton, EventHeader + scroll animation, EventInfo + mini-map, MapSection |
| **3** | May 4 | LineupGrid, ArtistCard (paper strip), ArtistSidebar (photo+video), LineupBackground, artist data wiring |
| **4** | May 5 | AudioContext + AudioPlayer + AudioToggle, game toggle integration, fallback handling |
| **5** | May 6 | FundraiserPoster wired in, TicketsButton, map icon logic, mobile fixes, compress videos |
| **6** | May 7 | Deploy to Vercel, domain, final test on phone, fix any broken layouts |
| **7** | May 8 | Event. Monitor errors. Hotfix if needed. |

---

## Init Commands (run these first)

```bash
npm create vite@latest evro661 -- --template react
cd evro661
npm install react-router-dom three @react-three/fiber
npm install -D tailwindcss @tailwindcss/vite autoprefixer
npx tailwindcss init -p
```

Then copy existing components into `src/components/` and start gutting.

---

*Plan by DeepSeek R1 via multi-AI-collab MCP | 2026-05-02*
