import React from 'react'
import { eventConfig } from '../../data/event'

export default function EventInfo() {
  const { date, venue } = eventConfig

  const scrollToMap = () =>
    document.getElementById('map-section')?.scrollIntoView({ behavior: 'smooth' })

  return (
    <div className="max-w-4xl mx-auto">
      <div className="grid grid-cols-1 md:grid-cols-3 gap-10">
        <div>
          <p className="text-white/40 text-xs font-grunge tracking-widest uppercase mb-2">Date</p>
          <p className="text-white text-2xl font-grunge">{date}</p>
        </div>
        <div>
          <p className="text-white/40 text-xs font-grunge tracking-widest uppercase mb-2">Venue</p>
          <p className="text-white text-2xl font-grunge">{venue || 'TBD'}</p>
        </div>
        <div>
          <p className="text-white/40 text-xs font-grunge tracking-widest uppercase mb-2">Location</p>
          <button
            onClick={scrollToMap}
            className="w-full aspect-video border border-white/20 flex flex-col items-center justify-center gap-2 hover:border-white/60 hover:bg-white/5 transition-all rounded group"
          >
            <span className="text-2xl group-hover:scale-125 transition-transform">📍</span>
            <span className="text-white/40 text-xs font-grunge group-hover:text-white/80 transition-colors">
              open map
            </span>
          </button>
        </div>
      </div>
    </div>
  )
}
