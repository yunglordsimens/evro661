import React, { useRef, useEffect, useCallback, useState } from 'react'

const GRAVITY = 0.4
const FRICTION = 0.98
const BOUNCE = 0.7
const MAX_BALLS = 12
const WASTED_SCORE = 12

function makeBall(x, y) {
  return {
    x, y,
    vx: (Math.random() - 0.5) * 8,
    vy: -12,
    radius: 25,
    rotation: 0,
    trail: [],
    color: `hsl(${Math.random() * 360},70%,55%)`,
  }
}

function makeParticle(x, y) {
  return {
    x, y,
    vx: (Math.random() - 0.5) * 6,
    vy: (Math.random() - 0.5) * 6 - 3,
    life: 1,
    size: Math.random() * 4 + 2,
    color: `hsl(${Math.random() * 360},80%,60%)`,
  }
}

function drawJagged(ctx, x, y, radius, rotation, color) {
  const spikes = 8
  ctx.save()
  ctx.translate(x, y)
  ctx.rotate(rotation)
  ctx.beginPath()
  for (let i = 0; i < spikes * 2; i++) {
    const r = i % 2 === 0 ? radius : radius * 0.5
    const angle = (i * Math.PI) / spikes - Math.PI / 2
    i === 0 ? ctx.moveTo(Math.cos(angle)*r, Math.sin(angle)*r)
             : ctx.lineTo(Math.cos(angle)*r, Math.sin(angle)*r)
  }
  ctx.closePath()
  ctx.fillStyle = color
  ctx.fill()
  ctx.strokeStyle = 'rgba(255,255,255,0.3)'
  ctx.lineWidth = 2
  ctx.stroke()
  ctx.restore()
}

export default function GameCanvas({ onClose }) {
  const canvasRef = useRef(null)
  const stateRef = useRef({ balls: [], particles: [], score: 0, wasted: false, wastedAt: 0, animId: null })
  const [score, setScore] = useState(0)
  const [wasted, setWasted] = useState(false)

  const loop = useCallback(() => {
    const canvas = canvasRef.current
    if (!canvas) return
    const ctx = canvas.getContext('2d')
    const s = stateRef.current

    ctx.clearRect(0, 0, canvas.width, canvas.height)

    s.balls.forEach(ball => {
      ball.vy += GRAVITY
      ball.vx *= FRICTION
      ball.x += ball.vx
      ball.y += ball.vy
      ball.rotation += ball.vx * 0.05
      ball.trail.push({ x: ball.x, y: ball.y })
      if (ball.trail.length > 15) ball.trail.shift()

      // trail
      ctx.beginPath()
      ball.trail.forEach((t, i) => i === 0 ? ctx.moveTo(t.x, t.y) : ctx.lineTo(t.x, t.y))
      ctx.strokeStyle = 'rgba(255,255,255,0.15)'
      ctx.lineWidth = 2
      ctx.stroke()

      // walls
      if (ball.x + ball.radius > canvas.width) {
        ball.x = canvas.width - ball.radius; ball.vx *= -BOUNCE
        for (let i = 0; i < 5; i++) s.particles.push(makeParticle(ball.x, ball.y))
      }
      if (ball.x - ball.radius < 0) {
        ball.x = ball.radius; ball.vx *= -BOUNCE
        for (let i = 0; i < 5; i++) s.particles.push(makeParticle(ball.x, ball.y))
      }
      if (ball.y + ball.radius > canvas.height) {
        ball.y = canvas.height - ball.radius; ball.vy *= -BOUNCE
        for (let i = 0; i < 8; i++) s.particles.push(makeParticle(ball.x, ball.y))
      }
      if (ball.y - ball.radius < 0) { ball.y = ball.radius; ball.vy *= -BOUNCE }

      drawJagged(ctx, ball.x, ball.y, ball.radius, ball.rotation, ball.color)
    })

    s.particles = s.particles.filter(p => {
      p.x += p.vx; p.y += p.vy; p.vy += 0.1; p.life -= 0.025
      if (p.life <= 0) return false
      ctx.beginPath()
      ctx.arc(p.x, p.y, p.size * p.life, 0, Math.PI * 2)
      ctx.fillStyle = p.color
      ctx.globalAlpha = p.life
      ctx.fill()
      ctx.globalAlpha = 1
      return true
    })

    if (s.score >= WASTED_SCORE && !s.wasted) {
      s.wasted = true; s.wastedAt = Date.now(); setWasted(true)
    }
    if (s.wasted && Date.now() - s.wastedAt > 2500) {
      s.balls = []; s.particles = []; s.score = 0; s.wasted = false
      setWasted(false); setScore(0); onClose?.()
      return
    }

    s.animId = requestAnimationFrame(loop)
  }, [onClose])

  const handleClick = useCallback(e => {
    const canvas = canvasRef.current
    if (!canvas || stateRef.current.wasted) return
    const rect = canvas.getBoundingClientRect()
    stateRef.current.balls.push(makeBall(e.clientX - rect.left, e.clientY - rect.top))
    stateRef.current.score += 1
    setScore(stateRef.current.score)
  }, [])

  useEffect(() => {
    const canvas = canvasRef.current
    if (!canvas) return
    const resize = () => { canvas.width = canvas.offsetWidth; canvas.height = canvas.offsetHeight }
    resize()
    window.addEventListener('resize', resize)
    stateRef.current.animId = requestAnimationFrame(loop)
    const onKey = e => { if (e.key === 'Escape') onClose?.() }
    window.addEventListener('keydown', onKey)
    return () => {
      window.removeEventListener('resize', resize)
      window.removeEventListener('keydown', onKey)
      if (stateRef.current.animId) cancelAnimationFrame(stateRef.current.animId)
    }
  }, [loop, onClose])

  return (
    <div className="relative w-full h-full">
      <canvas ref={canvasRef} onClick={handleClick} className="w-full h-full cursor-crosshair" />

      <div className="absolute top-4 left-1/2 -translate-x-1/2 font-grunge text-2xl text-white pointer-events-none">
        score: {score}
      </div>

      {wasted && (
        <div className="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 font-grunge text-7xl md:text-9xl text-red-500 pointer-events-none animate-pulse"
             style={{ textShadow: '3px 3px 0 #000' }}>
          WASTED
        </div>
      )}

      <button
        onClick={onClose}
        className="absolute top-4 right-4 w-10 h-10 bg-black/60 backdrop-blur-md border border-white/20 rounded-full flex items-center justify-center text-white hover:bg-white/10 transition-all"
        aria-label="Close game"
      >
        ✕
      </button>
    </div>
  )
}
