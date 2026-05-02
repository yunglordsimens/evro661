import React, { useState, useCallback, useRef } from 'react'
import { eventConfig } from '../data/event'
import { useScrollAnimation } from '../hooks/useScrollAnimation'
import { useMapVisibility } from '../hooks/useMapVisibility'
import { useGameState } from '../hooks/useGameState'
import { useAudio } from '../components/audio/AudioContext'
import EventHeader from '../components/event/EventHeader'
import EventInfo from '../components/event/EventInfo'
import EventDescription from '../components/event/EventDescription'
import LineupGrid from '../components/lineup/LineupGrid'
import TicketsButton from '../components/event/TicketsButton'
import MapSection from '../components/event/MapSection'
import FundraiserPoster from '../components/fundraiser/FundraiserPoster'
import AudioToggle from '../components/audio/AudioToggle'
import GameToggle from '../components/game/GameToggle'
import AudioPlayer from '../components/audio/AudioPlayer'
import GameCanvas from '../components/game/GameCanvas'

export default function EventPage() {
  const [bgVideo, setBgVideo] = useState(eventConfig.defaultVideo)
  const { scrollY } = useScrollAnimation()
  const { mapVisible, mapRef } = useMapVisibility()
  const { gameActive, toggleGame } = useGameState()
  const { playTrack } = useAudio()

  const handleArtistClick = useCallback((artist) => {
    if (artist.vid) setBgVideo(`/artists-data/${artist.slug}/video.mp4`)
    else setBgVideo(eventConfig.defaultVideo)
    playTrack(artist)
  }, [playTrack])

  return (
    <div className="relative min-h-screen bg-black text-white">
      {/* Fixed background video */}
      <video
        key={bgVideo}
        className="fixed inset-0 z-0 w-full h-full object-cover opacity-30 pointer-events-none"
        src={bgVideo}
        autoPlay loop muted playsInline
      />

      {/* Game overlay */}
      {gameActive && (
        <div className="fixed inset-0 z-50">
          <GameCanvas onClose={toggleGame} />
        </div>
      )}

      {/* Scrollable content */}
      <div className="relative z-10">
        <EventHeader scrollY={scrollY} />

        <section className="pt-40 px-4 md:px-8 max-w-7xl mx-auto">
          <EventInfo />
        </section>

        <section className="mt-20 px-4 md:px-8 max-w-7xl mx-auto">
          <EventDescription />
        </section>

        <section className="mt-20 px-4 md:px-8">
          <LineupGrid onArtistClick={handleArtistClick} />
        </section>

        <section className="mt-20 flex justify-center pb-10">
          <TicketsButton />
        </section>

        <section id="map-section" ref={mapRef}>
          <MapSection />
        </section>
      </div>

      {/* Fixed overlays */}
      <div className="fixed bottom-4 right-4 z-40">
        <FundraiserPoster />
      </div>

      <div className="fixed bottom-4 left-4 z-50 flex gap-3">
        <AudioToggle />
        <GameToggle active={gameActive} onToggle={toggleGame} />
      </div>

      {!mapVisible && (
        <button
          className="fixed top-20 right-4 z-30 w-10 h-10 bg-white/10 backdrop-blur rounded-full flex items-center justify-center hover:bg-white/20 transition-all"
          onClick={() => document.getElementById('map-section').scrollIntoView({ behavior: 'smooth' })}
          title="Go to map"
        >
          📍
        </button>
      )}

      <AudioPlayer />
    </div>
  )
}
