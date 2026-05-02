import React, { useEffect } from 'react'

export default function ArtistSidebar({ artist, onClose }) {
  useEffect(() => {
    if (!artist) return
    const onKey = e => { if (e.key === 'Escape') onClose() }
    document.body.style.overflow = 'hidden'
    window.addEventListener('keydown', onKey)
    return () => { window.removeEventListener('keydown', onKey); document.body.style.overflow = '' }
  }, [artist, onClose])

  return (
    <>
      {/* Backdrop */}
      <div
        className={`fixed inset-0 bg-black/60 backdrop-blur-sm z-40 transition-opacity duration-300 ${artist ? 'opacity-100 pointer-events-auto' : 'opacity-0 pointer-events-none'}`}
        onClick={onClose}
      />

      {/* Panel */}
      <div
        className={`fixed top-0 right-0 h-full w-full md:w-1/2 bg-black/95 backdrop-blur-md border-l border-white/10 z-50 transition-transform duration-500 ease-in-out ${artist ? 'translate-x-0' : 'translate-x-full'}`}
      >
        {artist && (
          <div className="h-full overflow-y-auto">
            <button
              onClick={onClose}
              className="absolute top-4 right-4 w-10 h-10 bg-white/10 rounded-full flex items-center justify-center text-white hover:bg-white/20 transition-colors z-10 text-xl"
              aria-label="Close"
            >
              ✕
            </button>

            <div className="p-6 pt-16">
              {/* Photo */}
              {artist.img ? (
                <div className="w-full aspect-[4/5] rounded-lg overflow-hidden mb-6">
                  <img src={`/${artist.img}`} alt={artist.name} className="w-full h-full object-cover" />
                </div>
              ) : (
                <div className="w-full aspect-[4/5] bg-white/5 rounded-lg flex items-center justify-center mb-6">
                  <span className="font-grunge text-6xl text-white/20">
                    {artist.name.split(' ').map(w => w[0]).join('').toUpperCase().slice(0, 2)}
                  </span>
                </div>
              )}

              {/* Video */}
              {artist.vid && (
                <div className="w-full aspect-video rounded-lg overflow-hidden mb-6 bg-black">
                  <video src={`/${artist.vid}`} autoPlay muted loop playsInline className="w-full h-full object-cover" />
                </div>
              )}

              <h2 className="font-grunge text-3xl text-white mb-4">{artist.name}</h2>

              {artist.bio && (
                <p className="text-white/70 leading-relaxed text-sm">{artist.bio}</p>
              )}
            </div>
          </div>
        )}
      </div>
    </>
  )
}
