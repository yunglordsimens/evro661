import React, { useState, useMemo } from 'react'
import { lineupData } from '../../data/lineup/index'
import ArtistCard from './ArtistCard'
import ArtistSidebar from './ArtistSidebar'

export default function LineupGrid({ onArtistClick }) {
  const [selectedArtist, setSelectedArtist] = useState(null)

  // Group flat array into renderable chunks: { type:'block', block:N, artists:[] } or { type:'illustration', img }
  const groups = useMemo(() => {
    const result = []
    let currentBlock = null

    lineupData.forEach(item => {
      if (item.type === 'illustration') {
        currentBlock = null
        result.push({ type: 'illustration', id: item.id, img: item.img })
      } else if (item.type === 'artist') {
        if (!currentBlock || currentBlock.block !== item.block) {
          currentBlock = { type: 'block', block: item.block, artists: [] }
          result.push(currentBlock)
        }
        currentBlock.artists.push(item)
      }
    })

    return result
  }, [])

  const handleClick = (artist) => {
    setSelectedArtist(artist)
    onArtistClick?.(artist)
  }

  return (
    <section className="py-16 px-4">
      <h2 className="font-grunge text-4xl md:text-6xl text-white text-center mb-16 tracking-wider">
        ЛАЙНАП
      </h2>

      <div className="max-w-6xl mx-auto space-y-16">
        {groups.map((group, i) =>
          group.type === 'illustration' ? (
            <div key={group.id} className="flex justify-center py-4">
              <img src={group.img} alt="divider" className="max-w-full h-auto opacity-60 rounded-lg" loading="lazy" />
            </div>
          ) : (
            <div key={`block-${group.block}-${i}`}>
              <p className="text-white/30 text-xs uppercase tracking-[0.3em] mb-6 font-grunge">
                block {group.block}
              </p>
              <div className="grid grid-cols-2 sm:grid-cols-3 md:grid-cols-4 lg:grid-cols-5 gap-3">
                {group.artists.map(artist => (
                  <ArtistCard key={artist.id} artist={artist} onClick={handleClick} />
                ))}
              </div>
            </div>
          )
        )}
      </div>

      <ArtistSidebar artist={selectedArtist} onClose={() => setSelectedArtist(null)} />
    </section>
  )
}
