# Artist Materials Audit — евро661
> DeepSeek analysis | 2026-05-02 | 6 days until event

---

## Status at a Glance

| | Count |
|---|---|
| Artists total | 23 |
| Complete (photo + video + bio) | 7 |
| Missing bio only | 7 |
| Missing video | 7 |
| Missing photo | 4 |
| **Missing everything** | **1 (KEIKO SEI — URGENT)** |

---

## Per-Artist Status

| Artist | Photo | Video | Bio | Notes |
|---|---|---|---|---|
| COINMAN46 | ✅ | ✅ | ❌ | Delete the 20KB screenshot — it's junk |
| DJ GODBLESS B2B DJ BUBBLE WUFFLE | ✅ | ✅ | ✅ | |
| VIKUSIA | ✅ | ✅ | ✅ | |
| TERROR PHOENIX | ✅ | ✅ | ❌ | |
| SVAZ | ✅ | ⚠️ 89MB | ❌ | Compress video before deploy |
| SPIRAL SADNESS | ✅ (5 photos) | ❌ | ✅ | Keep 3 best, delete 2 small ones (110KB, 123KB) |
| SEILOR MOON | ✅ | ❌ | ✅ | |
| REWOUNDED | ✅ | ✅ | ✅ | |
| POCK ROOT | ✅ | ✅ | ✅ | |
| ANGST | ✅ | ✅ | ❌ | |
| AUTOCANNIBAL | ✅ (2) | ✅ | ✅ | |
| BOLS/SLOB | ❌ | ❌ | ✅ | |
| CHLOE LANDAU | ⚠️ 10MB | ✅ | ⚠️ PDF | Compress photo; convert bio.pdf → bio.md |
| CRC | ✅ | ❌ | ✅ | |
| EIZOLA | ❌ | ✅ + ⚠️93MB | ✅ | Use vertical video (5.5MB); compress/delete horizontal (93MB) |
| DJ SCHEUSAAL | ✅ | ✅ | ✅ | |
| ETERNITY AGAIN | ✅ (2) | ✅ | ❌ | |
| **KEIKO SEI** | ❌ | ❌ | ❌ | **CONTACT ARTIST TODAY** |
| LILA TESLA | ❌ | ❌ | ✅ | |
| NEUE WELT | ✅ | ❌ | ✅ | |
| PASSIVE PROGRESSIVE | ✅ | ✅ | ❌ | |
| PLANDORA PEARL | ✅ | ✅ | ✅ | |
| WASTED DAYS | ✅ | ✅ | ❌ | |

---

## Multi-Photo Artists — What to Keep

| Artist | Photos | Recommendation |
|---|---|---|
| AUTOCANNIBAL | 2 × ~2MB | Keep both as photo-1 + photo-2 |
| COINMAN46 | 1.7MB png + 20KB screenshot | Delete the screenshot. Keep only cccc.png → photo-1 |
| ETERNITY AGAIN | 5.5MB + 4.8MB | Keep both as photo-1 + photo-2 |
| SPIRAL SADNESS | 5 photos (2.6MB, 2.1MB, 260KB, 123KB, 110KB) | Keep top 3 (2.6MB, 2.1MB, 260KB). Delete the 123KB and 110KB ones |

---

## File Size Problems

| File | Current | Target | Tool |
|---|---|---|---|
| chloe-landau/photo-1.jpg | **10MB** | ≤ 500KB | Squoosh.app or ImageOptim |
| eizola/video-horizontal.mov | **93MB** | delete or ≤ 15MB | HandBrake or `ffmpeg -crf 28` |
| svaz/video.mov | **89MB** | ≤ 15MB | HandBrake or `ffmpeg -crf 28` |

**ffmpeg one-liners:**
```bash
# svaz
ffmpeg -i artists-data/svaz/video.mov -c:v libx264 -crf 28 -preset fast -movflags +faststart artists-data/svaz/video.mp4

# eizola horizontal (or just delete it)
ffmpeg -i artists-data/eizola/video-horizontal.mov -c:v libx264 -crf 28 -preset fast -movflags +faststart artists-data/eizola/video-horizontal.mp4
```

---

## File Naming Convention (agreed)

```
artists-data/
  {slug}/
    photo-1.jpg      ← primary photo
    photo-2.jpg      ← optional second (only if genuinely different)
    photo-3.jpg      ← optional third (max)
    video.mp4        ← single video
    video-1.mov      ← if multiple videos
    video-2.mov
    bio.md           ← bio text in markdown
    stage-plan.pdf   ← extra docs (keep descriptive name)
```

---

## Top 5 Actions Right Now

| # | Action | Deadline |
|---|---|---|
| 1 | **Contact KEIKO SEI** — request photo, video, bio | Today |
| 2 | **Request bios** from 7 artists — angst, coinman46, eternity-again, passive-progressive, svaz, terror-phoenix, wasted-days | May 3 |
| 3 | **Compress** svaz video (89MB), eizola horizontal (93MB), chloe-landau photo (10MB) | May 3 |
| 4 | **Request missing photos** — bols-slob, eizola, lila-tesla | May 4 |
| 5 | **Request missing videos** — bols-slob, crc, lila-tesla, neue-welt, seilor-moon, spiral-sadness | May 4 |

**Hard deadline for all materials: May 5.** After that use placeholders — site must be tested May 6-7.

---

## Manual Cleanup Checklist

- [ ] Delete `artists-data/coinman46/Screenshot 2026-04-26 at 12.33.06.png`
- [ ] Delete `artists-data/spiral-sadness/IMG_6060.JPG` (110KB)
- [ ] Delete `artists-data/spiral-sadness/IMG_6061.JPG` (123KB)
- [ ] Convert `artists-data/chloe-landau/bio.pdf` → `bio.md` (copy text, save as md)
- [ ] Compress `artists-data/svaz/video.mov` (89MB)
- [ ] Compress `artists-data/eizola/video-horizontal.mov` (93MB) or delete
- [ ] Compress `artists-data/chloe-landau/photo-1.jpg` (10MB)
- [ ] Create folder `artists-data/keiko-sei/` and add materials
- [ ] Run `bash rename-artists.sh` to move + rename everything

---

*Report by DeepSeek R1 via multi-AI-collab MCP | 2026-05-02*
