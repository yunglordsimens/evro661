import React, { useState } from 'react';
import { lineupData } from './src/data/lineup/index.js';
import { eventConfig } from './src/data/lineup/config.js';

export default function App() {
  const [hoveredId, setHoveredId] = useState(null);
  const [clickedId, setClickedId] = useState(null);
  const [isVideoHovered, setIsVideoHovered] = useState(false);

  const activeId = clickedId || hoveredId;
  const activeArtist = lineupData.find(item => item.id === activeId);
  
  const bgVideoSrc = (activeArtist && activeArtist.type === 'artist') 
    ? activeArtist.vid 
    : eventConfig.defaultVideo;

  const handleBgClick = () => {
    setClickedId(null);
  };

  return (
    <div 
      className="min-h-screen bg-black overflow-x-hidden font-sans selection:bg-white selection:text-black pb-20 relative"
      onClick={handleBgClick}
    >
      
      {/* ФОНОВОЕ ВИДЕО */}
      <div className="fixed inset-0 z-0 overflow-hidden pointer-events-none transition-opacity duration-500 ease-in-out">
        <video 
          key={bgVideoSrc}
          autoPlay 
          loop 
          muted 
          playsInline
          className="absolute inset-0 w-full h-full object-cover opacity-60 mix-blend-lighten"
          src={bgVideoSrc}
        />
        <div className="absolute inset-0 bg-black/50"></div>
        <div className="absolute inset-0 bg-[url('https://grainy-gradients.vercel.app/noise.svg')] opacity-30 mix-blend-overlay"></div>
      </div>

      {/* ШРИФТЫ И СТИЛИ */}
      <style dangerouslySetInnerHTML={{__html: `
        @import url('https://fonts.googleapis.com/css2?family=Rock+Salt&family=Caveat+Brush&display=swap');
        
        .font-grunge { font-family: 'Rock Salt', cursive; }
        
        .paper-strip { filter: drop-shadow(3px 4px 0px rgba(0,0,0,0.9)); }
        .torn-edges { filter: url(#torn-edges-filter); }

        .text-outline {
          text-shadow: 
            -2px -2px 0 #fff,  
             2px -2px 0 #fff,
            -2px  2px 0 #fff,
             2px  2px 0 #fff,
             0px  4px 0 #fff;
        }

        ::-webkit-scrollbar { width: 8px; }
        ::-webkit-scrollbar-track { background: #000; }
        ::-webkit-scrollbar-thumb { background: #333; }
      `}} />

      {/* ФИЛЬТР ДЛЯ БУМАГИ */}
      <svg width="0" height="0" className="absolute hidden">
        <defs>
          <filter id="torn-edges-filter" x="-2%" y="-5%" width="104%" height="110%">
            <feTurbulence type="fractalNoise" baseFrequency="0.04 0.1" numOctaves="3" result="noise" />
            <feDisplacementMap in="SourceGraphic" in2="noise" scale="3" xChannelSelector="R" yChannelSelector="G" />
          </filter>
        </defs>
      </svg>

      {/* САЙДБАРЫ */}
      {activeArtist && activeArtist.type === 'artist' && (
        <div className="fixed inset-0 z-0 pointer-events-none hidden lg:block">
          
          <div 
            className="absolute left-10 xl:left-20 top-1/2 -translate-y-1/2 flex flex-col gap-3 w-[250px] xl:w-[320px] transition-all duration-300 pointer-events-auto"
            onClick={(e) => e.stopPropagation()}
          >
            <img 
              src={activeArtist.img} 
              alt={activeArtist.name}
              className="w-full h-auto object-contain shadow-2xl" 
            />
            <div className="text-white/80 font-sans text-sm xl:text-base leading-snug">
              <p className="font-bold uppercase mb-1">{activeArtist.name} — INFO</p>
              <p>Здесь будет просто инфа текстом, которую они про себя сказали в файлах. Без лишнего форматирования.</p>
            </div>
          </div>

          <div 
            className="absolute right-10 xl:right-20 top-1/2 -translate-y-1/2 flex flex-col items-end gap-3 w-[250px] xl:w-[320px] transition-all duration-300 pointer-events-auto"
            onClick={(e) => e.stopPropagation()}
          >
            <video 
              src={activeArtist.vid}
              autoPlay 
              loop 
              muted={!isVideoHovered}
              playsInline
              onMouseEnter={() => setIsVideoHovered(true)}
              onMouseLeave={() => setIsVideoHovered(false)}
              className="w-full h-auto max-h-[50vh] object-contain shadow-2xl cursor-pointer"
            />
            <p className="text-white font-sans text-base xl:text-lg text-right w-full">
              {activeArtist.bio}
            </p>
          </div>
          
        </div>
      )}

      {/* ОСНОВНОЙ КОНТЕНТ */}
      <main className="container mx-auto px-4 pt-12 flex flex-col items-center relative z-10">
        
        <div className="flex flex-col items-center w-full max-w-[500px] relative">
          {lineupData.map((item, index) => {
            
            if (item.type === 'illustration') {
              return (
                <div key={item.id} className="w-48 h-48 md:w-64 md:h-64 my-6 relative z-0 flex justify-center pointer-events-none">
                   <img 
                      src={item.img} 
                      alt="Art" 
                      className="w-full h-full object-cover filter grayscale contrast-200 brightness-110 mix-blend-screen opacity-90"
                      style={{ clipPath: 'polygon(10% 0%, 100% 10%, 90% 100%, 0% 90%)' }} 
                   />
                </div>
              );
            }

            const rotation = (index % 2 === 0 ? 1 : -1) * (0.5 + Math.random() * 1.5);
            const isLocked = clickedId === item.id;

            return (
              <div 
                key={item.id} 
                className="relative group cursor-crosshair w-full flex justify-center z-10 my-2 md:my-3"
                onMouseEnter={() => setHoveredId(item.id)}
                onMouseLeave={() => setHoveredId(null)}
                onClick={(e) => {
                  e.stopPropagation();
                  setClickedId(isLocked ? null : item.id);
                }}
              >
                <div className="relative transition-transform duration-200 ease-out group-hover:scale-110 paper-strip flex justify-center">
                  <div 
                    className="relative inline-block"
                    style={{ transform: `rotate(${rotation}deg)` }}
                  >
                    <div className="absolute inset-0 bg-white torn-edges"></div>
                    <h2 className="relative z-10 font-grunge text-black text-lg md:text-2xl px-6 py-1 uppercase whitespace-nowrap text-center tracking-tighter">
                      {item.name}
                    </h2>
                  </div>
                </div>
              </div>
            );
          })}
        </div>

        <div className="mt-12 text-center transform -rotate-2 w-full max-w-[500px]">
          <h1 className="font-grunge text-4xl md:text-6xl text-black text-outline tracking-tighter">
            {eventConfig.dates}
          </h1>
        </div>

      </main>
    </div>
  );
}
