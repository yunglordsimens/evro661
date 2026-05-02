import React, { useState, useCallback } from 'react'

export default function BarnDoors({ onEnter }) {
  const [opening, setOpening] = useState(false)

  const handleEnter = useCallback(() => {
    setOpening(true)
    setTimeout(() => onEnter?.(), 800)
  }, [onEnter])

  return (
    <div className="fixed inset-0 z-40">
      {/* Left door */}
      <div
        className="absolute top-0 left-0 h-full w-1/2 bg-black flex items-center justify-end pr-8 transition-transform duration-[800ms] ease-in-out"
        style={{ transform: opening ? 'translateX(-100%)' : 'translateX(0)' }}
      >
        <span className="font-grunge text-6xl md:text-8xl text-white select-none">ЄВРО</span>
      </div>

      {/* Right door */}
      <div
        className="absolute top-0 right-0 h-full w-1/2 bg-black flex items-center justify-start pl-8 transition-transform duration-[800ms] ease-in-out"
        style={{ transform: opening ? 'translateX(100%)' : 'translateX(0)' }}
      >
        <span className="font-grunge text-6xl md:text-8xl text-white select-none">661</span>
      </div>

      {/* Enter button — sits above both doors in the center */}
      {!opening && (
        <div className="absolute inset-0 flex items-center justify-center z-10">
          <button
            onClick={handleEnter}
            className="font-grunge text-2xl md:text-3xl text-white border-2 border-white/40 px-10 py-4 rounded-lg hover:bg-white/10 hover:scale-105 hover:border-white/70 transition-all duration-300"
          >
            УВІЙТИ
          </button>
        </div>
      )}
    </div>
  )
}
