import React from 'react'
import { useAudio } from './AudioContext'

export default function AudioPlayer() {
  const { currentTrack, isPlaying, toggleMute, stopTrack } = useAudio()
  if (!currentTrack) return null

  return (
    <div className="fixed bottom-20 left-1/2 -translate-x-1/2 z-50 bg-black/80 backdrop-blur-md text-white border border-white/20 rounded-full px-6 py-3 flex items-center gap-4 shadow-2xl">
      <span className="text-sm font-medium truncate max-w-[150px]">{currentTrack.name}</span>

      <button
        onClick={toggleMute}
        className="w-8 h-8 flex items-center justify-center rounded-full hover:bg-white/10 transition-colors"
        aria-label={isPlaying ? 'Pause' : 'Play'}
      >
        {isPlaying ? (
          <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" className="w-5 h-5">
            <path fillRule="evenodd" d="M6.75 5.25a.75.75 0 01.75-.75H9a.75.75 0 01.75.75v13.5a.75.75 0 01-.75.75H7.5a.75.75 0 01-.75-.75V5.25zm7.5 0A.75.75 0 0115 4.5h1.5a.75.75 0 01.75.75v13.5a.75.75 0 01-.75.75H15a.75.75 0 01-.75-.75V5.25z" clipRule="evenodd"/>
          </svg>
        ) : (
          <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" className="w-5 h-5">
            <path fillRule="evenodd" d="M4.5 5.653c0-1.426 1.529-2.33 2.779-1.643l11.54 6.348c1.295.712 1.295 2.573 0 3.285L7.28 19.991c-1.25.687-2.779-.217-2.779-1.643V5.653z" clipRule="evenodd"/>
          </svg>
        )}
      </button>

      <button
        onClick={stopTrack}
        className="w-8 h-8 flex items-center justify-center rounded-full hover:bg-white/10 transition-colors"
        aria-label="Close player"
      >
        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" className="w-5 h-5">
          <path fillRule="evenodd" d="M5.47 5.47a.75.75 0 011.06 0L12 10.94l5.47-5.47a.75.75 0 111.06 1.06L13.06 12l5.47 5.47a.75.75 0 11-1.06 1.06L12 13.06l-5.47 5.47a.75.75 0 01-1.06-1.06L10.94 12 5.47 6.53a.75.75 0 010-1.06z" clipRule="evenodd"/>
        </svg>
      </button>
    </div>
  )
}
