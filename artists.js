// Artist data for евро661 — May 8-9, 2026
// Source of truth for names: Downloads/Artist materials/ folder names
// Paths use post-rename structure: artists-data/{slug}/photo-1.jpg
// Run rename-artists.sh first to move and rename everything.
//
// ⚠️  MISSING MATERIALS (as of 2026-05-02):
//   No bio:   angst, coinman46, eternity-again, passive-progressive, svaz, terror-phoenix, wasted-days
//   No photo: bols-slob, eizola, lila-tesla, keiko-sei
//   No video: bols-slob, crc, lila-tesla, neue-welt, seilor-moon, spiral-sadness, keiko-sei
//   MISSING ENTIRELY: keiko-sei — contact artist ASAP

export const artists = [

  // ── Block 1 ─────────────────────────────────────────────────────────────────

  {
    id: 1, block: 1, type: 'artist',
    slug: 'coinman46',
    name: 'COINMAN46',
    bio: null,                    // ⚠️ missing
    img: 'artists-data/coinman46/photo-1.png',
    vid: 'artists-data/coinman46/video.mp4',
  },
  {
    id: 2, block: 1, type: 'artist',
    slug: 'dj-godbless-b2b-dj-bubble-wuffle',
    name: 'DJ GODBLESS B2B DJ BUBBLE WUFFLE',
    bio: 'artists-data/dj-godbless-b2b-dj-bubble-wuffle/bio.md',
    img: 'artists-data/dj-godbless-b2b-dj-bubble-wuffle/photo-1.png',
    vid: 'artists-data/dj-godbless-b2b-dj-bubble-wuffle/video.mov',
  },
  {
    id: 3, block: 1, type: 'artist',
    slug: 'vikusia',
    name: 'VIKUSIA',
    bio: 'artists-data/vikusia/bio.md',
    img: 'artists-data/vikusia/photo-1.jpg',
    vid: 'artists-data/vikusia/video.mp4',
  },
  {
    id: 4, block: 1, type: 'artist',
    slug: 'terror-phoenix',
    name: 'TERROR PHOENIX',
    bio: null,                    // ⚠️ missing
    img: 'artists-data/terror-phoenix/photo-1.png',
    vid: 'artists-data/terror-phoenix/video.mov',
  },
  {
    id: 5, block: 1, type: 'artist',
    slug: 'svaz',
    name: 'SVAZ',
    bio: null,                    // ⚠️ missing
    img: 'artists-data/svaz/photo-1.jpg',
    vid: 'artists-data/svaz/video.mov',   // ⚠️ 89MB — compress before deploy
  },
  {
    id: 6, block: 1, type: 'artist',
    slug: 'spiral-sadness',
    name: 'SPIRAL SADNESS',
    bio: 'artists-data/spiral-sadness/bio.md',
    img: 'artists-data/spiral-sadness/photo-1.jpg',
    vid: null,                    // ⚠️ missing
  },
  {
    id: 7, block: 1, type: 'artist',
    slug: 'seilor-moon',
    name: 'SEILOR MOON',
    bio: 'artists-data/seilor-moon/bio.md',
    img: 'artists-data/seilor-moon/photo-1.jpg',
    vid: null,                    // ⚠️ missing
  },
  {
    id: 8, block: 1, type: 'artist',
    slug: 'rewounded',
    name: 'REWOUNDED',
    bio: 'artists-data/rewounded/bio.md',
    img: 'artists-data/rewounded/photo-1.jpg',
    vid: 'artists-data/rewounded/video.mov',
  },
  {
    id: 9, block: 1, type: 'artist',
    slug: 'pock-root',
    name: 'POCK ROOT',
    bio: 'artists-data/pock-root/bio.md',
    img: 'artists-data/pock-root/photo-1.jpg',
    vid: 'artists-data/pock-root/video.mov',
  },

  // ── Block 2 ─────────────────────────────────────────────────────────────────

  {
    id: 10, block: 2, type: 'artist',
    slug: 'angst',
    name: 'ANGST',
    bio: null,                    // ⚠️ missing
    img: 'artists-data/angst/photo-1.jpg',
    vid: 'artists-data/angst/video.mov',
  },
  {
    id: 11, block: 2, type: 'artist',
    slug: 'autocannibal',
    name: 'AUTOCANNIBAL',
    bio: 'artists-data/autocannibal/bio.md',
    img: 'artists-data/autocannibal/photo-1.jpg',
    vid: 'artists-data/autocannibal/video.mov',
  },
  {
    id: 12, block: 2, type: 'artist',
    slug: 'bols-slob',
    name: 'BOLS/SLOB',
    bio: 'artists-data/bols-slob/bio.md',
    img: null,                    // ⚠️ missing
    vid: null,                    // ⚠️ missing
  },
  {
    id: 13, block: 2, type: 'artist',
    slug: 'chloe-landau',
    name: 'CHLOE LANDAU',
    bio: 'artists-data/chloe-landau/bio.md',  // ⚠️ convert from bio.pdf first
    img: 'artists-data/chloe-landau/photo-1.jpg', // ⚠️ 10MB — compress first
    vid: 'artists-data/chloe-landau/video.mov',
  },
  {
    id: 14, block: 2, type: 'artist',
    slug: 'crc',
    name: 'CRC',
    bio: 'artists-data/crc/bio.md',
    img: 'artists-data/crc/photo-1.jpg',
    vid: null,                    // ⚠️ missing
  },
  {
    id: 15, block: 2, type: 'artist',
    slug: 'eizola',
    name: 'EIZOLA',
    bio: 'artists-data/eizola/bio.md',
    img: null,                    // ⚠️ missing
    vid: 'artists-data/eizola/video.mov',   // vertical version (5.5MB)
  },
  {
    id: 16, block: 2, type: 'artist',
    slug: 'dj-scheusaal',
    name: 'DJ SCHEUSAAL',
    bio: 'artists-data/dj-scheusaal/bio.md',
    img: 'artists-data/dj-scheusaal/photo-1.jpg',
    vid: 'artists-data/dj-scheusaal/video.mp4',
  },

  // ── Block 3 ─────────────────────────────────────────────────────────────────

  {
    id: 17, block: 3, type: 'artist',
    slug: 'eternity-again',
    name: 'ETERNITY AGAIN',
    bio: null,                    // ⚠️ missing
    img: 'artists-data/eternity-again/photo-1.jpg',
    vid: 'artists-data/eternity-again/video.mov',
  },
  {
    id: 18, block: 3, type: 'artist',
    slug: 'keiko-sei',
    name: 'KEIKO SEI',
    bio: null,                    // ⚠️ ENTIRELY MISSING — contact artist
    img: null,
    vid: null,
  },
  {
    id: 19, block: 3, type: 'artist',
    slug: 'lila-tesla',
    name: 'LILA TESLA',
    bio: 'artists-data/lila-tesla/bio.md',
    img: null,                    // ⚠️ missing
    vid: null,                    // ⚠️ missing
  },
  {
    id: 20, block: 3, type: 'artist',
    slug: 'neue-welt',
    name: 'NEUE WELT',
    bio: 'artists-data/neue-welt/bio.md',
    img: 'artists-data/neue-welt/photo-1.jpg',
    vid: null,                    // ⚠️ missing
  },
  {
    id: 21, block: 3, type: 'artist',
    slug: 'passive-progressive',
    name: 'PASSIVE PROGRESSIVE',
    bio: null,                    // ⚠️ missing
    img: 'artists-data/passive-progressive/photo-1.jpg',
    vid: 'artists-data/passive-progressive/video.mp4',
  },
  {
    id: 22, block: 3, type: 'artist',
    slug: 'plandora-pearl',
    name: 'PLANDORA PEARL',
    bio: 'artists-data/plandora-pearl/bio.md',
    img: 'artists-data/plandora-pearl/photo-1.jpg',
    vid: 'artists-data/plandora-pearl/video.mov',
  },
  {
    id: 23, block: 3, type: 'artist',
    slug: 'wasted-days',
    name: 'WASTED DAYS',
    bio: null,                    // ⚠️ missing
    img: 'artists-data/wasted-days/photo-1.jpg',
    vid: 'artists-data/wasted-days/video.mov',
  },
]
