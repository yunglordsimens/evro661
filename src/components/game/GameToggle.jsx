import React from 'react'

export default function GameToggle({ active, onToggle }) {
  return (
    <button
      onClick={onToggle}
      className={`bg-black/60 backdrop-blur-md w-10 h-10 rounded-full flex items-center justify-center text-lg hover:bg-white/10 transition-all duration-200 ${
        active ? 'ring-2 ring-white' : 'border border-white/20'
      }`}
      aria-label={active ? 'Close game' : 'Open game'}
    >
      ⚽
    </button>
  )
}
