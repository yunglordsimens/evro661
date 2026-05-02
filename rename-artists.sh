#!/usr/bin/env bash
# rename-artists.sh
# Run from repo root: bash rename-artists.sh
# Moves Downloads/Artist materials/ → artists-data/ at repo root
# Renames all folders to slugs, all files to photo-1/video-1 convention
# Uses git mv so everything stays in history.

set -e

OLD_BASE="Downloads/Artist materials"
NEW_BASE="artists-data"

# Step 1 — move each artist folder out of Downloads/ and rename to slug
move_artist() {
  local old_name="$1"
  local new_slug="$2"
  local from="$OLD_BASE/$old_name"
  local to="$NEW_BASE/$new_slug"
  if [ -d "$from" ]; then
    git mv "$from" "$to"
    echo "  moved: $old_name → artists-data/$new_slug"
  fi
}

echo "── Moving folders to artists-data/ ──────────────────────────────────────"
move_artist "Angst"                              "angst"
move_artist "Autocannibal"                       "autocannibal"
move_artist "Bols-slob"                          "bols-slob"
move_artist "CRC"                                "crc"
move_artist "Chloe Landau"                       "chloe-landau"
move_artist "Coinman46"                          "coinman46"
move_artist "DJ SCHEUSAAL"                       "dj-scheusaal"
move_artist "DJ godbless b2b DJ bubble wuffle"   "dj-godbless-b2b-dj-bubble-wuffle"
move_artist "Eizola "                            "eizola"
move_artist "Eternity Again"                     "eternity-again"
move_artist "Lila tesla"                         "lila-tesla"
move_artist "Neue Welt"                          "neue-welt"
move_artist "Passive progressive "               "passive-progressive"
move_artist "Plandora Pearl"                     "plandora-pearl"
move_artist "Rewounded"                          "rewounded"
move_artist "Seilor moon"                        "seilor-moon"
move_artist "Spiral sadness"                     "spiral-sadness"
move_artist "Svaz"                               "svaz"
move_artist "Terror phoenix "                    "terror-phoenix"
move_artist "Vikusia"                            "vikusia"
move_artist "Wasted Days"                        "wasted-days"
move_artist "pock.root"                          "pock-root"

# Step 2 — rename files inside each artist folder to clean convention
# Photos → photo-1.jpg, photo-2.jpg  (max 3 — delete extras manually first)
# Videos → video.mp4 / video.mov     (if two: video-1.mov, video-2.mov)
# Bio    → bio.md
# Docs   → keep descriptive name

B="artists-data"

rf() {
  local artist="$1" from="$2" to="$3"
  local full_from="$B/$artist/$from"
  local full_to="$B/$artist/$to"
  if [ -f "$full_from" ] && [ "$full_from" != "$full_to" ]; then
    git mv "$full_from" "$full_to"
    echo "  file: $from → $to"
  fi
}

echo ""
echo "── Renaming files ───────────────────────────────────────────────────────"

# angst
rf angst "L1003355.jpeg"                                                "photo-1.jpg"
rf angst "3ed946b3315c4618beecae145cf09636.mov"                         "video.mov"

# autocannibal  (2 photos — keep both as photo-1, photo-2)
rf autocannibal "Autocannibal bio.md"                                   "bio.md"
rf autocannibal "IMG_6054.JPG"                                          "photo-1.jpg"
rf autocannibal "IMG_6055.JPG"                                          "photo-2.jpg"
rf autocannibal "trim.676FCF6C-0BF7-4352-BDD2-D6E14F430E00.MOV"        "video.mov"

# bols-slob — bio.md already correct

# crc
rf crc "5422853170410492237.jpg"                                         "photo-1.jpg"

# chloe-landau
rf chloe-landau "2026_UKR_MARCH_ANYA_ALYA_LORIASHVILI_01.jpg"          "photo-1.jpg"
rf chloe-landau "ScreenRecording_04-24-2026 00-14-14_1.mov"             "video.mov"
rf chloe-landau "bio.pdf"                                               "bio.pdf"

# coinman46 — delete Screenshot manually, keep cccc.png as photo-1
rf coinman46 "cccc.png"                                                 "photo-1.png"
rf coinman46 "promo.mp4"                                                "video.mp4"
# NOTE: delete "Screenshot 2026-04-26 at 12.33.06.png" manually — it is useless

# dj-scheusaal
rf dj-scheusaal "PHOTO-2026-04-25-16-02-52.jpg"                        "photo-1.jpg"
rf dj-scheusaal "VIDEO-2026-04-25-16-03-34.mp4"                        "video.mp4"

# dj-godbless-b2b-dj-bubble-wuffle
rf dj-godbless-b2b-dj-bubble-wuffle "алваи.png"                        "photo-1.png"
rf dj-godbless-b2b-dj-bubble-wuffle "vedoe.mov"                        "video.mov"

# eizola — vertical video is the usable one (5.5MB), horizontal is 93MB
rf eizola "IMG_6415cistirna_vertical.mov"                               "video.mov"
rf eizola "IMG_9818cistirna_horizontal.MOV"                             "video-horizontal.mov"
# NOTE: video-horizontal.mov is 93MB — compress or delete

# eternity-again  (2 photos — keep both)
rf eternity-again "img_23.jpeg"                                         "photo-1.jpg"
rf eternity-again "IMG_8679.jpeg"                                       "photo-2.jpg"
rf eternity-again "video-output-8A7F0281-8216-4FAC-9734-5D843361F2E4-1.mov" "video.mov"

# lila-tesla
rf lila-tesla "Vše je zde.md"                                           "bio.md"

# neue-welt
rf neue-welt "nw-32.jpg"                                                "photo-1.jpg"
rf neue-welt "Neue Welt stage plán  (1).pdf"                            "stage-plan.pdf"

# passive-progressive
rf passive-progressive "IMG_6058.JPG"                                   "photo-1.jpg"
rf passive-progressive "pp video.mp4"                                   "video.mp4"

# plandora-pearl
rf plandora-pearl "6C62D8D2-A303-42B6-9899-8749DD8734A6.jpg"            "photo-1.jpg"
rf plandora-pearl "7af76d2d027a40e58cebea9fa21337f5.mov"                "video.mov"
rf plandora-pearl "Bio.md"                                              "bio.md"

# rewounded
rf rewounded "rewounded.jpg"                                            "photo-1.jpg"
rf rewounded "f40bfb9c36bf48a5a36fdec477b44d72.MOV"                    "video.mov"
rf rewounded "Bio.md"                                                   "bio.md"

# seilor-moon
rf seilor-moon "CB9283A3-507A-4297-9FB9-F6B1F6DD8597.jpg"              "photo-1.jpg"
rf seilor-moon "Bio.md"                                                 "bio.md"

# spiral-sadness — 5 photos: pick best 3, delete rest manually before running
rf spiral-sadness "Spiral bio.md"                                       "bio.md"
rf spiral-sadness "IMG_6053.JPG"                                        "photo-1.jpg"
rf spiral-sadness "IMG_6062.JPG"                                        "photo-2.jpg"
rf spiral-sadness "skenování0311.jpg"                                   "photo-3.jpg"
# NOTE: IMG_6060.JPG and IMG_6061.JPG are small (110-123KB) — delete manually

# svaz
rf svaz "svaz blurred.jpg"                                              "photo-1.jpg"
rf svaz "IMG_5161.mov"                                                  "video.mov"
# NOTE: video.mov is 89MB — compress with: ffmpeg -i video.mov -c:v libx264 -crf 28 video_compressed.mp4

# terror-phoenix
rf terror-phoenix "IMG_6057.PNG"                                        "photo-1.png"
rf terror-phoenix "trim.676FCF6C-0BF7-4352-BDD2-D6E14F430E00.MOV"      "video.mov"

# vikusia
rf vikusia "img0221.jpeg"                                               "photo-1.jpg"
rf vikusia "2026-04-24 00.28.49.mp4"                                    "video.mp4"

# wasted-days
rf wasted-days "0B8137FA-F404-4290-94E6-2E68FAB7B40A.JPEG"             "photo-1.jpg"
rf wasted-days "ScreenRecording_04-26-2026 00-14-56_1.mov"              "video.mov"

# pock-root
rf pock-root "E2C305D1-2754-4AA7-9AA4-B76541B1F50B.jpg"                "photo-1.jpg"
rf pock-root "1359bcd2cb254de99dd71f6ee4ee1753.mov"                    "video.mov"

echo ""
echo "Done. Review with: git status"
echo "Then: git add -A && git commit -m 'Move artist materials to artists-data/, normalize filenames'"
echo ""
echo "MANUAL ACTIONS STILL NEEDED:"
echo "  - Delete: artists-data/coinman46/Screenshot 2026-04-26 at 12.33.06.png"
echo "  - Delete: artists-data/spiral-sadness/IMG_6060.JPG"
echo "  - Delete: artists-data/spiral-sadness/IMG_6061.JPG"
echo "  - Compress: artists-data/svaz/video.mov (89MB)"
echo "  - Compress: artists-data/eizola/video-horizontal.mov (93MB) or delete"
echo "  - Compress: artists-data/chloe-landau/photo-1.jpg (10MB)"
echo "  - Convert: artists-data/chloe-landau/bio.pdf → bio.md"
echo "  - CREATE:  artists-data/keiko-sei/ — completely missing!"
echo "  - ADD BIO: angst, coinman46, eternity-again, passive-progressive,"
echo "             svaz, terror-phoenix, wasted-days"
