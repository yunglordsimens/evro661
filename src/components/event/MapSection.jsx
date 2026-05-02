import React from 'react'
import { eventConfig } from '../../data/event'

export default function MapSection() {
  return (
    <div className="w-full py-16 px-4">
      <h2 className="font-grunge text-3xl md:text-5xl text-white text-center mb-4 tracking-wider">
        ЯК ДІСТАТИСЬ
      </h2>
      {eventConfig.address && eventConfig.address !== 'TBD' && (
        <p className="text-white/50 text-center mb-8 text-sm tracking-widest uppercase">
          {eventConfig.address}
        </p>
      )}
      <div className="w-full max-w-4xl mx-auto aspect-video rounded-xl overflow-hidden border border-white/10 bg-white/5 flex items-center justify-center">
        {/* Replace the src with the actual Google Maps embed URL when venue is confirmed */}
        <iframe
          title="Venue map"
          src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d81776.03841497698!2d30.4234!3d50.4501!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x40d4cf0000000001%3A0x1!2sKyiv%2C+Ukraine!5e0!3m2!1sen!2sua!4v1000000000000"
          width="100%"
          height="100%"
          style={{ border: 0, filter: 'invert(90%) hue-rotate(180deg)' }}
          allowFullScreen
          loading="lazy"
          referrerPolicy="no-referrer-when-downgrade"
        />
      </div>
    </div>
  )
}
