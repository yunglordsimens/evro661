import React, { useState } from 'react'
import { eventConfig } from '../../data/event'

export default function TicketsButton() {
  const [flash, setFlash] = useState(false)

  const handleHover = () => { setFlash(true); setTimeout(() => setFlash(false), 300) }

  return (
    <a
      href={eventConfig.ticketsUrl}
      target="_blank"
      rel="noopener noreferrer"
      onMouseEnter={handleHover}
      className={`font-grunge text-2xl md:text-4xl text-white border-2 border-white/40 px-16 py-5 rounded-lg transition-all duration-200 hover:border-white hover:scale-105 inline-block text-center ${
        flash ? 'bg-white text-black' : 'bg-transparent'
      }`}
    >
      КВИТКИ
    </a>
  )
}
