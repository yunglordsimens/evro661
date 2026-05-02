import { useState, useCallback } from 'react'

export function useGameState() {
  const [gameActive, setGameActive] = useState(false)
  const toggleGame = useCallback(() => setGameActive(prev => !prev), [])
  return { gameActive, toggleGame }
}
