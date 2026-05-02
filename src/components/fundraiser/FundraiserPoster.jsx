import React, { useRef, useEffect } from 'react'
import { eventConfig } from '../../data/event'

export default function FundraiserPoster() {
  const cardRef = useRef(null)

  useEffect(() => {
    const card = cardRef.current
    if (!card) return
    const onMove = e => {
      const rect = card.getBoundingClientRect()
      const cx = rect.left + rect.width / 2
      const cy = rect.top + rect.height / 2
      const rx = (e.clientY - cy) / 10
      const ry = (e.clientX - cx) / 10
      card.style.transform = `perspective(1000px) rotateX(${-rx}deg) rotateY(${ry}deg) scale(1.05)`
    }
    const onLeave = () => {
      card.style.transform = 'perspective(1000px) rotateX(0deg) rotateY(0deg) scale(1)'
    }
    card.addEventListener('mousemove', onMove)
    card.addEventListener('mouseleave', onLeave)
    return () => { card.removeEventListener('mousemove', onMove); card.removeEventListener('mouseleave', onLeave) }
  }, [])

  return (
    <div
      ref={cardRef}
      className="w-[200px] h-[270px] rounded-xl flex flex-col items-center justify-center cursor-pointer shadow-2xl border border-white/10 transition-transform duration-100"
      style={{ background: 'linear-gradient(135deg,#1a1a2e,#16213e,#0f3460)' }}
    >
      <div className="text-4xl mb-3">🐑</div>
      <h2 className="font-grunge text-lg text-white text-center mb-2 px-2">євро661</h2>
      <p className="text-xs text-white/60 text-center px-4 mb-4">підтримай захід</p>
      <a
        href={eventConfig.donateUrl}
        target="_blank"
        rel="noopener noreferrer"
        className="px-4 py-2 bg-white/10 border border-white/30 rounded text-white text-xs hover:bg-white/20 transition-colors"
      >
        ЗАДОНАТИТИ
      </a>
    </div>
  )
}
