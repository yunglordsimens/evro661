import React from 'react'

export default function ArtistCard({ artist, onClick }) {
  const initials = artist.name.split(' ').map(w => w[0]).join('').toUpperCase().slice(0, 2)

  return (
    <div
      className="paper-strip rounded-lg overflow-hidden cursor-pointer group hover:scale-[1.03] transition-transform duration-300"
      onClick={() => onClick(artist)}
    >
      {artist.img ? (
        <div className="aspect-square overflow-hidden">
          <img
            src={`/${artist.img}`}
            alt={artist.name}
            className="w-full h-full object-cover group-hover:scale-110 transition-transform duration-500"
            loading="lazy"
          />
        </div>
      ) : (
        <div className="aspect-square bg-white/5 flex items-center justify-center">
          <span className="font-grunge text-4xl text-white/30">{initials}</span>
        </div>
      )}
      <div className="p-3">
        <h3 className="font-grunge text-xs text-white truncate leading-tight">{artist.name}</h3>
      </div>
    </div>
  )
}
