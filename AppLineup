import React, { useState } from 'react';

// Полный список
const lineupData = [
  // БЛОК 1
  { id: 1, type: 'artist', name: "GOINMAN", bio: "Мрачный бит, ломаные ритмы.", img: "https://images.unsplash.com/photo-1599839619722-39751411ea63?w=400&q=80", vid: "https://media.giphy.com/media/xT9IgzoKnwFNmISR8I/giphy.mp4" },
  { id: 2, type: 'artist', name: "DJ GODBLESS X DJ BUBBLE WUFFLE", bio: "B2B сет, который уничтожит танцпол.", img: "https://images.unsplash.com/photo-1605658661608-f4219cc0dcd9?w=400&q=80", vid: "https://media.giphy.com/media/l41YcWxh1455mUf3W/giphy.mp4" },
  { id: 3, type: 'artist', name: "VIKUSIA", bio: "Экспериментальный нойз.", img: "https://images.unsplash.com/photo-1514525253161-7a46d19cd819?w=400&q=80", vid: "https://media.giphy.com/media/26ufcVAp3AiLxruSs/giphy.mp4" },
  { id: 4, type: 'artist', name: "TERROR PHOENIX", bio: "Хардкор панк из подвалов.", img: "https://images.unsplash.com/photo-1526478806334-5fd488fceabc?w=400&q=80", vid: "https://media.giphy.com/media/3oEjI6SIIHBdRxXI40/giphy.mp4" },
  { id: 5, type: 'artist', name: "SVAZ", bio: "Локальная поддержка.", img: "https://images.unsplash.com/photo-1621360811013-c76831f1628c?w=400&q=80", vid: "https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExMTh1aG90YzgyNm9wNWNxMnZhZ2twaDBpM3RydG1sdTUzNHV5azZqYiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/3o7TKSjRrfIPjeiVyM/giphy.mp4" },
  { id: 6, type: 'artist', name: "SPIRAL SADNESS", bio: "Меланхолия и дисторшн.", img: "https://images.unsplash.com/photo-1508700115892-45ecd05ae2ad?w=400&q=80", vid: "https://media.giphy.com/media/xT9IgzoKnwFNmISR8I/giphy.mp4" },
  { id: 7, type: 'artist', name: "SEILOR MOON", bio: "Рейв энергия.", img: "https://images.unsplash.com/photo-1598387181032-a3103a2db5b3?w=400&q=80", vid: "https://media.giphy.com/media/l41YcWxh1455mUf3W/giphy.mp4" },
  { id: 8, type: 'artist', name: "REWOUNDED", bio: "Тяжелые синты.", img: "https://images.unsplash.com/photo-1542282811-943ef1a977f5?w=400&q=80", vid: "https://media.giphy.com/media/26ufcVAp3AiLxruSs/giphy.mp4" },
  { id: 9, type: 'artist', name: "POCK ROOT", bio: "Индустриальный скрежет.", img: "https://images.unsplash.com/photo-1510525009512-ad7fc13eefab?w=400&q=80", vid: "https://media.giphy.com/media/3oEjI6SIIHBdRxXI40/giphy.mp4" },
  
  // ЦЕНТРАЛЬНАЯ ИЛЛЮСТРАЦИЯ
  { id: 'illustration_1', type: 'illustration', img: "https://images.unsplash.com/photo-1501179691627-eeaa65ea017c?w=600&q=80" },

  // БЛОК 2
  { id: 10, type: 'artist', name: "ANGST", bio: "Чистая тревога.", img: "https://images.unsplash.com/photo-1546707012-c46675f12716?w=400&q=80", vid: "https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExMTh1aG90YzgyNm9wNWNxMnZhZ2twaDBpM3RydG1sdTUzNHV5azZqYiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/3o7TKSjRrfIPjeiVyM/giphy.mp4" },
  { id: 11, type: 'artist', name: "AUTOCANNIBAL", bio: "Саморазрушение.", img: "https://images.unsplash.com/photo-1599839619722-39751411ea63?w=400&q=80", vid: "https://media.giphy.com/media/xT9IgzoKnwFNmISR8I/giphy.mp4" },
  { id: 12, type: 'artist', name: "BOLS/SLOB", bio: "Грязный саунд.", img: "https://images.unsplash.com/photo-1605658661608-f4219cc0dcd9?w=400&q=80", vid: "https://media.giphy.com/media/l41YcWxh1455mUf3W/giphy.mp4" },
  { id: 13, type: 'artist', name: "CHLOE LANDAU", bio: "Дарквейв сет.", img: "https://images.unsplash.com/photo-1514525253161-7a46d19cd819?w=400&q=80", vid: "https://media.giphy.com/media/26ufcVAp3AiLxruSs/giphy.mp4" },
  { id: 14, type: 'artist', name: "CRC", bio: "Электро.", img: "https://images.unsplash.com/photo-1526478806334-5fd488fceabc?w=400&q=80", vid: "https://media.giphy.com/media/3oEjI6SIIHBdRxXI40/giphy.mp4" },
  { id: 15, type: 'artist', name: "EIZOLA", bio: "Техно.", img: "https://images.unsplash.com/photo-1621360811013-c76831f1628c?w=400&q=80", vid: "https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExMTh1aG90YzgyNm9wNWNxMnZhZ2twaDBpM3RydG1sdTUzNHV5azZqYiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/3o7TKSjRrfIPjeiVyM/giphy.mp4" },
  { id: 16, type: 'artist', name: "DJ SCHEUSAAL", bio: "Закрываем ночь.", img: "https://images.unsplash.com/photo-1508700115892-45ecd05ae2ad?w=400&q=80", vid: "https://media.giphy.com/media/xT9IgzoKnwFNmISR8I/giphy.mp4" },

  // БЛОК 3
  { id: 17, type: 'artist', name: "ETERNITY AGAIN", bio: "Пост-панк.", img: "https://images.unsplash.com/photo-1598387181032-a3103a2db5b3?w=400&q=80", vid: "https://media.giphy.com/media/l41YcWxh1455mUf3W/giphy.mp4" },
  { id: 18, type: 'artist', name: "KEIKO SEI", bio: "Вокал и синты.", img: "https://images.unsplash.com/photo-1542282811-943ef1a977f5?w=400&q=80", vid: "https://media.giphy.com/media/26ufcVAp3AiLxruSs/giphy.mp4" },
  { id: 19, type: 'artist', name: "LILATESLA", bio: "Шум.", img: "https://images.unsplash.com/photo-1510525009512-ad7fc13eefab?w=400&q=80", vid: "https://media.giphy.com/media/3oEjI6SIIHBdRxXI40/giphy.mp4" },
  { id: 20, type: 'artist', name: "NEUE WELT", bio: "EBM.", img: "https://images.unsplash.com/photo-1546707012-c46675f12716?w=400&q=80", vid: "https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExMTh1aG90YzgyNm9wNWNxMnZhZ2twaDBpM3RydG1sdTUzNHV5azZqYiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/3o7TKSjRrfIPjeiVyM/giphy.mp4" },
  { id: 21, type: 'artist', name: "PASSIVE PROGRESSIVE", bio: "IDM.", img: "https://images.unsplash.com/photo-1599839619722-39751411ea63?w=400&q=80", vid: "https://media.giphy.com/media/xT9IgzoKnwFNmISR8I/giphy.mp4" },
  { id: 22, type: 'artist', name: "PLANDONA PEARL", bio: "Брейкбит.", img: "https://images.unsplash.com/photo-1605658661608-f4219cc0dcd9?w=400&q=80", vid: "https://media.giphy.com/media/l41YcWxh1455mUf3W/giphy.mp4" },
  { id: 23, type: 'artist', name: "WASTED DAYS", bio: "Рассвет.", img: "https://images.unsplash.com/photo-1514525253161-7a46d19cd819?w=400&q=80", vid: "https://media.giphy.com/media/26ufcVAp3AiLxruSs/giphy.mp4" },
];

export default function App() {
  const [hoveredId, setHoveredId] = useState(null);
  const [clickedId, setClickedId] = useState(null); // Хранит ID зафиксированного кликом артиста
  const [isVideoHovered, setIsVideoHovered] = useState(false); // Состояние наведения на само видео для звука

  // Активным считается тот, на кого кликнули. Если не кликали — тот, на кого навели мышку
  const activeId = clickedId || hoveredId;
  const activeArtist = lineupData.find(item => item.id === activeId);
  
  // Если активен артист — ставим его видео на фон. Если нет — дефолтный футбол.
  const bgVideoSrc = (activeArtist && activeArtist.type === 'artist') 
    ? activeArtist.vid 
    : "https://media.giphy.com/media/3o7TKSvGqEAEoEMOcg/giphy.mp4";

  // Сброс фиксации при клике в пустое место
  const handleBgClick = () => {
    setClickedId(null);
  };

  return (
    <div 
      className="min-h-screen bg-black overflow-x-hidden font-sans selection:bg-white selection:text-black pb-20 relative"
      onClick={handleBgClick} // Клик по фону сбрасывает всё
    >
      
      {/* ФОНОВОЕ ВИДЕО */}
      <div className="fixed inset-0 z-0 overflow-hidden pointer-events-none transition-opacity duration-500 ease-in-out">
        {/* Ключ key заставляет React перезагрузить видео при смене источника */}
        <video 
          key={bgVideoSrc}
          autoPlay 
          loop 
          muted 
          playsInline
          className="absolute inset-0 w-full h-full object-cover opacity-60 mix-blend-lighten"
          src={bgVideoSrc}
        />
        {/* Затемнение фона, чтобы центральный текст всегда читался */}
        <div className="absolute inset-0 bg-black/50"></div>
        <div className="absolute inset-0 bg-[url('https://grainy-gradients.vercel.app/noise.svg')] opacity-30 mix-blend-overlay"></div>
      </div>

      {/* ШРИФТЫ И СТИЛИ */}
      <style dangerouslySetInnerHTML={{__html: `
        @import url('https://fonts.googleapis.com/css2?family=Rock+Salt&family=Caveat+Brush&display=swap');
        
        .font-grunge { font-family: 'Rock Salt', cursive; }
        
        /* Жесткая тень + SVG фильтр рваных краев для центрального списка */
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

      {/* САЙДБАРЫ (ПОЯВЛЯЮТСЯ ПРИ НАВЕДЕНИИ ИЛИ КЛИКЕ) */}
      {activeArtist && activeArtist.type === 'artist' && (
        <div className="fixed inset-0 z-0 pointer-events-none hidden lg:block">
          
          {/* ЛЕВАЯ СТОРОНА: Фотка + простой текст */}
          <div 
            className="absolute left-10 xl:left-20 top-1/2 -translate-y-1/2 flex flex-col gap-3 w-[250px] xl:w-[320px] transition-all duration-300 pointer-events-auto"
            onClick={(e) => e.stopPropagation()} // Чтобы клик по этому блоку не сбрасывал фиксацию
          >
            {/* Фотка без рамок */}
            <img 
              src={activeArtist.img} 
              alt={activeArtist.name}
              className="w-full h-auto object-contain shadow-2xl" 
            />
            {/* Текст тупо инфа */}
            <div className="text-white/80 font-sans text-sm xl:text-base leading-snug">
              <p className="font-bold uppercase mb-1">{activeArtist.name} — INFO</p>
              <p>Здесь будет просто инфа текстом, которую они про себя сказали в файлах. Без лишнего форматирования.</p>
            </div>
          </div>

          {/* ПРАВАЯ СТОРОНА: Видео как есть + Био */}
          <div 
            className="absolute right-10 xl:right-20 top-1/2 -translate-y-1/2 flex flex-col items-end gap-3 w-[250px] xl:w-[320px] transition-all duration-300 pointer-events-auto"
            onClick={(e) => e.stopPropagation()} // Чтобы клик по этому блоку не сбрасывал фиксацию
          >
            {/* Видео без рамок, включает звук при наведении! */}
            <video 
              src={activeArtist.vid}
              autoPlay 
              loop 
              muted={!isVideoHovered} // Если навели мышку - включаем звук
              playsInline
              onMouseEnter={() => setIsVideoHovered(true)}
              onMouseLeave={() => setIsVideoHovered(false)}
              className="w-full h-auto max-h-[50vh] object-contain shadow-2xl cursor-pointer"
            />
            {/* Биография артиста */}
            <p className="text-white font-sans text-base xl:text-lg text-right w-full">
              {activeArtist.bio}
            </p>
          </div>
          
        </div>
      )}

      {/* ОСНОВНОЙ КОНТЕНТ (ЦЕНТР) */}
      <main className="container mx-auto px-4 pt-12 flex flex-col items-center relative z-10">
        
        {/* Лайнап блок */}
        <div className="flex flex-col items-center w-full max-w-[500px] relative">
          {lineupData.map((item, index) => {
            
            // ЕСЛИ ЭТО ИЛЛЮСТРАЦИЯ (между блоками)
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

            // ЕСЛИ ЭТО АРТИСТ
            const rotation = (index % 2 === 0 ? 1 : -1) * (0.5 + Math.random() * 1.5);
            const isLocked = clickedId === item.id; // Проверяем, зафиксирован ли этот элемент

            return (
              <div 
                key={item.id} 
                className="relative group cursor-crosshair w-full flex justify-center z-10 my-2 md:my-3"
                onMouseEnter={() => setHoveredId(item.id)}
                onMouseLeave={() => setHoveredId(null)}
                onClick={(e) => {
                  e.stopPropagation(); // Не даем клику дойти до фона, чтобы он не сработал как сброс
                  setClickedId(isLocked ? null : item.id); // Фиксируем, либо снимаем фиксацию (если кликнуть повторно)
                }}
              >
                {/* ЦЕНТРАЛЬНАЯ БУМАЖКА */}
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

        {/* ДАТЫ ВНИЗУ */}
        <div className="mt-12 text-center transform -rotate-2 w-full max-w-[500px]">
          <h1 className="font-grunge text-4xl md:text-6xl text-black text-outline tracking-tighter">
            8.5-9.5.2026
          </h1>
        </div>

      </main>
    </div>
  );
}
