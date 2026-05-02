import { useInView } from 'react-intersection-observer'

export function useMapVisibility() {
  const { ref: mapRef, inView: mapVisible } = useInView({ threshold: 0.1 })
  return { mapVisible, mapRef }
}
