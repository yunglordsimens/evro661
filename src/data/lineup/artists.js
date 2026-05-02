// Artist data for евро661 — May 8-9, 2026
//
// img / vid point to post-rename paths under Downloads/Artist materials/{slug}/
// When you set up the Vite project, move these to public/artists/{slug}/ and
// update the paths to /artists/{slug}/photo.jpg
//
// MISSING: keiko-sei — no folder in Downloads yet

export const artists = [

  // ── Block 1 ─────────────────────────────────────────────────────────────────

  {
    id: 1,
    block: 1,
    type: 'artist',
    slug: 'goinman',                // folder was: Coinman46
    name: 'GOINMAN',
    bio: 'Мрачный бит, ломаные ритмы.',
    img: 'Downloads/Artist materials/goinman/photo.png',
    vid: 'Downloads/Artist materials/goinman/video.mp4',
  },
  {
    id: 2,
    block: 1,
    type: 'artist',
    slug: 'dj-godbless-b2b-dj-bubble-wuffle',
    name: 'DJ GODBLESS X DJ BUBBLE WUFFLE',
    bio: 'B2B сет, который уничтожит танцпол.',
    img: 'Downloads/Artist materials/dj-godbless-b2b-dj-bubble-wuffle/photo.png',
    vid: 'Downloads/Artist materials/dj-godbless-b2b-dj-bubble-wuffle/video.mov',
  },
  {
    id: 3,
    block: 1,
    type: 'artist',
    slug: 'vikusia',
    name: 'VIKUSIA',
    bio: 'Экспериментальный нойз.',
    img: 'Downloads/Artist materials/vikusia/photo.jpg',
    vid: 'Downloads/Artist materials/vikusia/video.mp4',
  },
  {
    id: 4,
    block: 1,
    type: 'artist',
    slug: 'terror-phoenix',
    name: 'TERROR PHOENIX',
    bio: 'Хардкор панк из подвалов.',
    img: 'Downloads/Artist materials/terror-phoenix/photo.png',
    vid: 'Downloads/Artist materials/terror-phoenix/video.mov',
  },
  {
    id: 5,
    block: 1,
    type: 'artist',
    slug: 'svaz',
    name: 'SVAZ',
    bio: 'Локальная поддержка.',
    img: 'Downloads/Artist materials/svaz/photo.jpg',
    vid: 'Downloads/Artist materials/svaz/video.mov',
  },
  {
    id: 6,
    block: 1,
    type: 'artist',
    slug: 'spiral-sadness',
    name: 'SPIRAL SADNESS',
    bio: 'Меланхолия и дисторшн.',
    img: 'Downloads/Artist materials/spiral-sadness/photo.jpg',
    vid: null,                      // no video in folder
  },
  {
    id: 7,
    block: 1,
    type: 'artist',
    slug: 'seilor-moon',
    name: 'SEILOR MOON',
    bio: 'Рейв энергия.',
    img: 'Downloads/Artist materials/seilor-moon/photo.jpg',
    vid: null,                      // no video in folder
  },
  {
    id: 8,
    block: 1,
    type: 'artist',
    slug: 'rewounded',
    name: 'REWOUNDED',
    bio: 'Тяжелые синты.',
    img: 'Downloads/Artist materials/rewounded/photo.jpg',
    vid: 'Downloads/Artist materials/rewounded/video.mov',
  },
  {
    id: 9,
    block: 1,
    type: 'artist',
    slug: 'pock-root',
    name: 'POCK ROOT',
    bio: 'Индустриальный скрежет.',
    img: 'Downloads/Artist materials/pock-root/photo.jpg',
    vid: 'Downloads/Artist materials/pock-root/video.mov',
  },

  // ── Block 2 ─────────────────────────────────────────────────────────────────

  {
    id: 10,
    block: 2,
    type: 'artist',
    slug: 'angst',
    name: 'ANGST',
    bio: 'Чистая тревога.',
    img: 'Downloads/Artist materials/angst/photo.jpg',
    vid: 'Downloads/Artist materials/angst/video.mov',
  },
  {
    id: 11,
    block: 2,
    type: 'artist',
    slug: 'autocannibal',
    name: 'AUTOCANNIBAL',
    bio: 'Саморазрушение.',
    img: 'Downloads/Artist materials/autocannibal/photo.jpg',
    vid: 'Downloads/Artist materials/autocannibal/video.mov',
  },
  {
    id: 12,
    block: 2,
    type: 'artist',
    slug: 'bols-slob',
    name: 'BOLS/SLOB',
    bio: 'Грязный саунд.',
    img: null,                      // no photo yet
    vid: null,                      // no video yet
  },
  {
    id: 13,
    block: 2,
    type: 'artist',
    slug: 'chloe-landau',
    name: 'CHLOE LANDAU',
    bio: 'Дарквейв сет.',
    img: 'Downloads/Artist materials/chloe-landau/photo.jpg',
    vid: 'Downloads/Artist materials/chloe-landau/video.mov',
  },
  {
    id: 14,
    block: 2,
    type: 'artist',
    slug: 'crc',
    name: 'CRC',
    bio: 'Электро.',
    img: 'Downloads/Artist materials/crc/photo.jpg',
    vid: null,                      // no video yet
  },
  {
    id: 15,
    block: 2,
    type: 'artist',
    slug: 'eizola',
    name: 'EIZOLA',
    bio: 'Техно.',
    img: null,                      // no photo — only videos
    vid: 'Downloads/Artist materials/eizola/video-vertical.mov',
  },
  {
    id: 16,
    block: 2,
    type: 'artist',
    slug: 'dj-scheusaal',
    name: 'DJ SCHEUSAAL',
    bio: 'Закрываем ночь.',
    img: 'Downloads/Artist materials/dj-scheusaal/photo.jpg',
    vid: 'Downloads/Artist materials/dj-scheusaal/video.mp4',
  },

  // ── Block 3 ─────────────────────────────────────────────────────────────────

  {
    id: 17,
    block: 3,
    type: 'artist',
    slug: 'eternity-again',
    name: 'ETERNITY AGAIN',
    bio: 'Пост-панк.',
    img: 'Downloads/Artist materials/eternity-again/photo.jpg',
    vid: 'Downloads/Artist materials/eternity-again/video.mov',
  },
  {
    id: 18,
    block: 3,
    type: 'artist',
    slug: 'keiko-sei',            // ⚠️ folder missing — needs to be created
    name: 'KEIKO SEI',
    bio: 'Вокал и синты.',
    img: null,
    vid: null,
  },
  {
    id: 19,
    block: 3,
    type: 'artist',
    slug: 'lilatesla',
    name: 'LILATESLA',
    bio: 'Шум.',
    img: null,                      // no photo in folder
    vid: null,                      // no video in folder
  },
  {
    id: 20,
    block: 3,
    type: 'artist',
    slug: 'neue-welt',
    name: 'NEUE WELT',
    bio: 'EBM.',
    img: 'Downloads/Artist materials/neue-welt/photo.jpg',
    vid: null,                      // no video yet
  },
  {
    id: 21,
    block: 3,
    type: 'artist',
    slug: 'passive-progressive',
    name: 'PASSIVE PROGRESSIVE',
    bio: 'IDM.',
    img: 'Downloads/Artist materials/passive-progressive/photo.jpg',
    vid: 'Downloads/Artist materials/passive-progressive/video.mp4',
  },
  {
    id: 22,
    block: 3,
    type: 'artist',
    slug: 'plandona-pearl',         // folder was: Plandora Pearl
    name: 'PLANDONA PEARL',
    bio: 'Брейкбит.',
    img: 'Downloads/Artist materials/plandona-pearl/photo.jpg',
    vid: 'Downloads/Artist materials/plandona-pearl/video.mov',
  },
  {
    id: 23,
    block: 3,
    type: 'artist',
    slug: 'wasted-days',
    name: 'WASTED DAYS',
    bio: 'Рассвет.',
    img: 'Downloads/Artist materials/wasted-days/photo.jpg',
    vid: 'Downloads/Artist materials/wasted-days/video.mov',
  },
]
