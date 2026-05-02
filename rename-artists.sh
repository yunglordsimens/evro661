#!/usr/bin/env bash
# rename-artists.sh — run from repo root: bash rename-artists.sh
# Uses git mv so renames are tracked in history.

set -e
BASE="Downloads/Artist materials"

rename_folder() {
  local from="$BASE/$1"
  local to="$BASE/$2"
  if [ -d "$from" ] && [ ! -d "$to" ]; then
    git mv "$from" "$to"
    echo "  folder: $1 → $2"
  fi
}

rename_file() {
  local artist="$1"
  local from="$BASE/$artist/$2"
  local to="$BASE/$artist/$3"
  if [ -f "$from" ] && [ "$from" != "$to" ]; then
    git mv "$from" "$to"
    echo "  file:   $2 → $3"
  fi
}

echo "── Renaming folders ──────────────────────────────────"
rename_folder "Angst"                             "angst"
rename_folder "Autocannibal"                      "autocannibal"
rename_folder "Bols-slob"                         "bols-slob"
rename_folder "CRC"                               "crc"
rename_folder "Chloe Landau"                      "chloe-landau"
rename_folder "Coinman46"                         "coinman46"
rename_folder "DJ SCHEUSAAL"                      "dj-scheusaal"
rename_folder "DJ godbless b2b DJ bubble wuffle"  "dj-godbless-b2b-dj-bubble-wuffle"
rename_folder "Eizola "                           "eizola"
rename_folder "Eternity Again"                    "eternity-again"
rename_folder "Lila tesla"                          "lila-tesla"
rename_folder "Neue Welt"                         "neue-welt"
rename_folder "Passive progressive "              "passive-progressive"
rename_folder "Plandora Pearl"                     "plandora-pearl"
rename_folder "Rewounded"                         "rewounded"
rename_folder "Seilor moon"                       "seilor-moon"
rename_folder "Spiral sadness"                    "spiral-sadness"
rename_folder "Svaz"                              "svaz"
rename_folder "Terror phoenix "                   "terror-phoenix"
rename_folder "Vikusia"                           "vikusia"
rename_folder "Wasted Days"                       "wasted-days"
rename_folder "pock.root"                         "pock-root"

echo ""
echo "── Renaming files ────────────────────────────────────"

# angst
rename_file "angst" "L1003355.jpeg"                                              "photo.jpg"
rename_file "angst" "3ed946b3315c4618beecae145cf09636.mov"                       "video.mov"

# autocannibal
rename_file "autocannibal" "Autocannibal bio.md"                                 "bio.md"
rename_file "autocannibal" "IMG_6054.JPG"                                        "photo.jpg"
rename_file "autocannibal" "IMG_6055.JPG"                                        "photo-2.jpg"
rename_file "autocannibal" "trim.676FCF6C-0BF7-4352-BDD2-D6E14F430E00.MOV"      "video.mov"

# bols-slob — bio.md already correct

# crc
rename_file "crc" "5422853170410492237.jpg"                                      "photo.jpg"

# chloe-landau
rename_file "chloe-landau" "2026_UKR_MARCH_ANYA_ALYA_LORIASHVILI_01.jpg"        "photo.jpg"
rename_file "chloe-landau" "ScreenRecording_04-24-2026 00-14-14_1.mov"           "video.mov"

# goinman  (folder was Coinman46)
rename_file "coinman46" "cccc.png"                                                 "photo.png"
rename_file "coinman46" "Screenshot 2026-04-26 at 12.33.06.png"                   "photo-2.png"
rename_file "coinman46" "promo.mp4"                                                "video.mp4"

# dj-scheusaal
rename_file "dj-scheusaal" "PHOTO-2026-04-25-16-02-52.jpg"                      "photo.jpg"
rename_file "dj-scheusaal" "VIDEO-2026-04-25-16-03-34.mp4"                      "video.mp4"

# dj-godbless-b2b-dj-bubble-wuffle
rename_file "dj-godbless-b2b-dj-bubble-wuffle" "алваи.png"                      "photo.png"
rename_file "dj-godbless-b2b-dj-bubble-wuffle" "vedoe.mov"                      "video.mov"

# eizola
rename_file "eizola" "IMG_6415cistirna_vertical.mov"                             "video-vertical.mov"
rename_file "eizola" "IMG_9818cistirna_horizontal.MOV"                           "video-horizontal.mov"

# eternity-again
rename_file "eternity-again" "img_23.jpeg"                                       "photo.jpg"
rename_file "eternity-again" "IMG_8679.jpeg"                                     "photo-2.jpg"
rename_file "eternity-again" "video-output-8A7F0281-8216-4FAC-9734-5D843361F2E4-1.mov" "video.mov"

# lilatesla
rename_file "lila-tesla" "Vše je zde.md"                                          "bio.md"

# neue-welt
rename_file "neue-welt" "nw-32.jpg"                                              "photo.jpg"
rename_file "neue-welt" "Neue Welt stage plán  (1).pdf"                          "stage-plan.pdf"

# passive-progressive
rename_file "passive-progressive" "IMG_6058.JPG"                                 "photo.jpg"
rename_file "passive-progressive" "pp video.mp4"                                 "video.mp4"

# plandona-pearl  (folder was Plandora Pearl)
rename_file "plandora-pearl" "6C62D8D2-A303-42B6-9899-8749DD8734A6.jpg"         "photo.jpg"
rename_file "plandora-pearl" "7af76d2d027a40e58cebea9fa21337f5.mov"             "video.mov"
rename_file "plandora-pearl" "Bio.md"                                            "bio.md"

# rewounded
rename_file "rewounded" "rewounded.jpg"                                          "photo.jpg"
rename_file "rewounded" "f40bfb9c36bf48a5a36fdec477b44d72.MOV"                  "video.mov"
rename_file "rewounded" "Bio.md"                                                 "bio.md"

# seilor-moon
rename_file "seilor-moon" "CB9283A3-507A-4297-9FB9-F6B1F6DD8597.jpg"            "photo.jpg"
rename_file "seilor-moon" "Bio.md"                                               "bio.md"

# spiral-sadness
rename_file "spiral-sadness" "Spiral bio.md"                                     "bio.md"
rename_file "spiral-sadness" "IMG_6053.JPG"                                      "photo.jpg"
rename_file "spiral-sadness" "IMG_6062.JPG"                                      "photo-2.jpg"
rename_file "spiral-sadness" "skenování0311.jpg"                                 "photo-3.jpg"
rename_file "spiral-sadness" "IMG_6060.JPG"                                      "photo-4.jpg"
rename_file "spiral-sadness" "IMG_6061.JPG"                                      "photo-5.jpg"

# svaz
rename_file "svaz" "svaz blurred.jpg"                                            "photo.jpg"
rename_file "svaz" "IMG_5161.mov"                                                "video.mov"

# terror-phoenix
rename_file "terror-phoenix" "IMG_6057.PNG"                                      "photo.png"
rename_file "terror-phoenix" "trim.676FCF6C-0BF7-4352-BDD2-D6E14F430E00.MOV"   "video.mov"

# vikusia
rename_file "vikusia" "img0221.jpeg"                                             "photo.jpg"
rename_file "vikusia" "2026-04-24 00.28.49.mp4"                                 "video.mp4"

# wasted-days
rename_file "wasted-days" "0B8137FA-F404-4290-94E6-2E68FAB7B40A.JPEG"          "photo.jpg"
rename_file "wasted-days" "ScreenRecording_04-26-2026 00-14-56_1.mov"           "video.mov"

# pock-root
rename_file "pock-root" "E2C305D1-2754-4AA7-9AA4-B76541B1F50B.jpg"             "photo.jpg"
rename_file "pock-root" "1359bcd2cb254de99dd71f6ee4ee1753.mov"                  "video.mov"

echo ""
echo "Done. Review with: git status"
echo "Then commit: git add -A && git commit -m 'Rename artist folders and files to consistent slugs'"
echo ""
echo "NOTE: KEIKO SEI has no folder — create: Downloads/Artist materials/keiko-sei/"
