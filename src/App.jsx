import React, { Suspense, lazy } from 'react'
import { BrowserRouter, Routes, Route } from 'react-router-dom'
import { AudioProvider } from './components/audio/AudioContext'

const LandingPage = lazy(() => import('./pages/LandingPage'))
const EventPage   = lazy(() => import('./pages/EventPage'))

function Loader() {
  return (
    <div className="fixed inset-0 bg-black flex items-center justify-center">
      <span className="font-grunge text-white text-4xl animate-pulse">...</span>
    </div>
  )
}

export default function App() {
  return (
    <BrowserRouter>
      <AudioProvider>
        <Suspense fallback={<Loader />}>
          <Routes>
            <Route path="/"      element={<LandingPage />} />
            <Route path="/event" element={<EventPage />} />
          </Routes>
        </Suspense>
      </AudioProvider>
    </BrowserRouter>
  )
}
