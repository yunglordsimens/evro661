import React, { createContext, useContext, useRef, useState, useCallback, useEffect } from 'react'

const AudioCtx = createContext(null)

export function AudioProvider({ children }) {
  const audioRef = useRef(new Audio())
  const [currentTrack, setCurrentTrack] = useState(null)
  const [isPlaying, setIsPlaying] = useState(false)
  const [isMuted, setIsMuted] = useState(false)

  useEffect(() => {
    const audio = audioRef.current
    return () => { audio.pause(); audio.src = '' }
  }, [])

  const stopTrack = useCallback(() => {
    const audio = audioRef.current
    audio.pause()
    audio.currentTime = 0
    setCurrentTrack(null)
    setIsPlaying(false)
  }, [])

  const playTrack = useCallback((artist) => {
    const audio = audioRef.current

    if (currentTrack?.id === artist.id) {
      if (audio.paused) { audio.play().catch(() => {}); setIsPlaying(true) }
      else { audio.pause(); setIsPlaying(false) }
      return
    }

    audio.pause()
    audio.currentTime = 0
    setCurrentTrack(artist)

    if (artist.vid) {
      audio.src = `/${artist.vid}`
      audio.loop = true
      audio.muted = isMuted
      audio.oncanplaythrough = () => {
        audio.play().catch(() => setIsPlaying(false))
        setIsPlaying(true)
      }
      audio.onerror = () => { console.warn(`Audio 404 for ${artist.name}`); stopTrack() }
    } else {
      setIsPlaying(false)
    }
  }, [currentTrack, isMuted, stopTrack])

  const toggleMute = useCallback(() => {
    setIsMuted(prev => {
      const next = !prev
      audioRef.current.muted = next
      return next
    })
  }, [])

  return (
    <AudioCtx.Provider value={{ currentTrack, isPlaying, isMuted, playTrack, toggleMute, stopTrack }}>
      {children}
    </AudioCtx.Provider>
  )
}

export function useAudio() {
  const ctx = useContext(AudioCtx)
  if (!ctx) throw new Error('useAudio must be inside AudioProvider')
  return ctx
}
