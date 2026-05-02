import React, { useState, useEffect } from 'react'
import { useNavigate } from 'react-router-dom'
import BarnDoors from '../components/doors/BarnDoors'
import Navbar from '../components/layout/Navbar'

export default function LandingPage() {
  const navigate = useNavigate()
  const [flash, setFlash] = useState(false)

  const handleEnter = () => {
    setFlash(true)
    setTimeout(() => navigate('/event'), 600)
  }

  return (
    <div className="relative w-full h-screen bg-black overflow-hidden">
      <Navbar />
      <BarnDoors onEnter={handleEnter} />
      <div
        className="fixed inset-0 z-50 bg-white pointer-events-none transition-opacity duration-500"
        style={{ opacity: flash ? 1 : 0 }}
      />
    </div>
  )
}
