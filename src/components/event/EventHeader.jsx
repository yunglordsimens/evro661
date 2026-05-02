import React, { forwardRef, useMemo } from 'react'

const EventHeader = forwardRef(({ scrollY }, ref) => {
  const isSmall = scrollY > 80

  const style = useMemo(() => {
    if (!isSmall) return {}
    const p = Math.min((scrollY - 80) / 120, 1)
    return { transform: `scale(${1 - p * 0.6})`, transformOrigin: 'left top' }
  }, [scrollY, isSmall])

  return (
    <div
      ref={ref}
      className={`transition-all duration-300 ease-out z-20 ${
        isSmall
          ? 'fixed top-16 left-4'
          : 'fixed top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 text-center'
      }`}
      style={style}
    >
      <h1 className={`font-grunge text-white leading-tight transition-all duration-300 ${
        isSmall ? 'text-lg' : 'text-5xl md:text-8xl'
      }`}>
        євро661
      </h1>
      {!isSmall && (
        <p className="mt-4 text-white/50 text-sm font-grunge tracking-widest">
          May 8–9 · 2026
        </p>
      )}
    </div>
  )
})

EventHeader.displayName = 'EventHeader'
export default EventHeader
