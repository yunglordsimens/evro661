#!/usr/bin/env python3
"""Patch #2: donate URL, music player → SoundCloud, football game, neue-welt bio"""

import sys, re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

changes = []

# ── 1. Donate URL ──────────────────────────────────────────────────────────────
OLD1 = '<a id="donate-poster" href="#" target="_blank" rel="noopener" title="Donate for Ukraine" aria-label="Donate">'
NEW1 = '<a id="donate-poster" href="https://donio.cz/drony-solidarity-ctyri?utm_source=ig&utm_medium=social&utm_content=link_in_bio&fbclid=PAZnRzaARkOVJleHRuA2FlbQIxMQBzcnRjBmFwcF9pZA8xMjQwMjQ1NzQyODc0MTQAAac9JGrGySz9-WOv5QHxkTdHhGLoHlc_Wdyamg6nwUgc9gVl4fbKN8cFmwbGpw_aem_SmnPEwNws18n2qD_E0_AiQ" target="_blank" rel="noopener" title="Donate for Ukraine" aria-label="Donate">'
if OLD1 in html:
    html = html.replace(OLD1, NEW1, 1)
    changes.append('✅ Donate URL updated')
else:
    changes.append('❌ Donate URL: pattern not found')

# ── 2. Music player CSS: make it taller for SoundCloud widget ──────────────────
OLD2 = '''        #music-player {
            position: fixed;
            bottom: -76px;
            left: 50%;
            transform: translateX(-50%);
            background: rgba(8,6,4,0.95);
            border: 1px solid rgba(255,255,255,0.1);
            border-bottom: none;
            padding: 12px 24px;
            display: flex;
            align-items: center;
            gap: 16px;
            z-index: 42;
            transition: bottom 0.4s cubic-bezier(0.22,1,0.36,1);
            min-width: 280px;
            backdrop-filter: blur(12px);
        }
        #music-player.open { bottom: 0; }
        #mp-name {
            font-family: 'Rock Salt', cursive;
            font-size: 0.68rem;
            color: #fff;
            letter-spacing: 1px;
            flex: 1;
            white-space: nowrap;
            overflow: hidden;
            text-overflow: ellipsis;
            max-width: 160px;
        }
        #mp-play {
            background: none;
            border: 1px solid rgba(255,255,255,0.25);
            color: #fff;
            width: 32px; height: 32px;
            border-radius: 50%;
            cursor: pointer;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 0.85rem;
            transition: border-color 0.2s, background 0.2s;
            flex-shrink: 0;
        }
        #mp-play:hover { border-color: #fff; background: rgba(255,255,255,0.08); }
        #mp-close {
            background: none;
            border: none;
            color: rgba(255,255,255,0.35);
            cursor: pointer;
            font-size: 1rem;
            line-height: 1;
            padding: 2px;
            transition: color 0.2s;
            flex-shrink: 0;
        }
        #mp-close:hover { color: #fff; }'''
NEW2 = '''        #music-player {
            position: fixed;
            bottom: -220px;
            left: 50%;
            transform: translateX(-50%);
            background: rgba(8,6,4,0.97);
            border: 1px solid rgba(255,255,255,0.12);
            border-bottom: none;
            padding: 10px 16px 0;
            display: flex;
            flex-direction: column;
            gap: 8px;
            z-index: 42;
            transition: bottom 0.4s cubic-bezier(0.22,1,0.36,1);
            width: min(420px, 92vw);
            backdrop-filter: blur(12px);
        }
        #music-player.open { bottom: 0; }
        #mp-header {
            display: flex;
            align-items: center;
            justify-content: space-between;
            padding-bottom: 6px;
        }
        #mp-name {
            font-family: 'Rock Salt', cursive;
            font-size: 0.6rem;
            color: rgba(255,255,255,0.55);
            letter-spacing: 1px;
            white-space: nowrap;
            overflow: hidden;
            text-overflow: ellipsis;
        }
        #mp-close {
            background: none;
            border: none;
            color: rgba(255,255,255,0.35);
            cursor: pointer;
            font-size: 1rem;
            line-height: 1;
            padding: 2px 0 2px 8px;
            transition: color 0.2s;
            flex-shrink: 0;
        }
        #mp-close:hover { color: #fff; }
        #mp-sc-iframe {
            display: block;
            border: none;
            width: 100%;
            height: 166px;
        }'''
if OLD2 in html:
    html = html.replace(OLD2, NEW2, 1)
    changes.append('✅ Music player CSS updated for SoundCloud')
else:
    changes.append('❌ Music player CSS: pattern not found')

# ── 3. Add football canvas CSS right before #bottom-left-ctrl ─────────────────
OLD3 = '        /* ── BOTTOM-LEFT CONTROLS ── */\n        #bottom-left-ctrl {'
NEW3 = '''        /* ── FOOTBALL GAME ── */
        #football-canvas {
            position: fixed;
            top: 0; left: 0;
            width: 100%; height: 100%;
            z-index: 9998;
            pointer-events: none;
            display: none;
        }
        #football-canvas.active { display: block; }
        #fb-game-score {
            position: fixed;
            bottom: 70px;
            left: 50%;
            transform: translateX(-50%) rotate(-1deg);
            background: #111;
            color: #f2f2f2;
            padding: 6px 14px;
            font-family: 'Courier New', monospace;
            font-weight: bold;
            font-size: 0.9rem;
            border: 2px solid #333;
            box-shadow: 3px 3px 0 #666;
            pointer-events: none;
            white-space: nowrap;
            z-index: 9999;
            display: none;
        }
        #fb-game-score.active { display: block; }
        #fb-game-msg {
            position: fixed;
            bottom: 110px;
            left: 50%;
            transform: translateX(-50%) rotate(2deg);
            font-family: 'Courier New', monospace;
            font-size: 1.3rem;
            font-weight: 900;
            background: #fff;
            color: #111;
            padding: 4px 12px;
            border: 3px solid #111;
            box-shadow: 4px 4px 0 #111;
            opacity: 0;
            transition: opacity 0.1s;
            text-transform: uppercase;
            pointer-events: none;
            z-index: 9999;
        }

        /* ── BOTTOM-LEFT CONTROLS ── */
        #bottom-left-ctrl {'''
if OLD3 in html:
    html = html.replace(OLD3, NEW3, 1)
    changes.append('✅ Football canvas CSS added')
else:
    changes.append('❌ Football canvas CSS: pattern not found')

# ── 4. Add ⚽ button to #bottom-left-ctrl ─────────────────────────────────────
OLD4 = '        <div id="bottom-left-ctrl">\n            <button class="ctrl-btn" id="btn-sound" title="Toggle sound" aria-label="Toggle sound">🔇</button>\n        </div>'
NEW4 = '''        <div id="bottom-left-ctrl">
            <button class="ctrl-btn" id="btn-sound" title="Toggle sound" aria-label="Toggle sound">🔇</button>
            <button class="ctrl-btn" id="btn-football" title="Football game" aria-label="Football game">⚽</button>
        </div>
        <!-- Football game elements -->
        <canvas id="football-canvas"></canvas>
        <div id="fb-game-score"><span id="fb-score-num">0</span> &nbsp;|&nbsp; DON'T LET IT FALL</div>
        <div id="fb-game-msg">WASTED!</div>'''
if OLD4 in html:
    html = html.replace(OLD4, NEW4, 1)
    changes.append('✅ Football button + canvas HTML added')
else:
    changes.append('❌ Football button HTML: pattern not found')

# ── 5. Replace music player HTML ──────────────────────────────────────────────
OLD5 = '''    <!-- Music player (popup from bottom) -->
    <div id="music-player" role="complementary" aria-label="Music player">
        <span id="mp-name">—</span>
        <audio id="mp-audio" src=""></audio>
        <button id="mp-play" aria-label="Play/Pause">▶</button>
        <button id="mp-close" aria-label="Close">✕</button>
    </div>'''
NEW5 = '''    <!-- Music player (SoundCloud popup from bottom) -->
    <div id="music-player" role="complementary" aria-label="Music player">
        <div id="mp-header">
            <span id="mp-name">евро661 × 6000ovecek — Playlist</span>
            <button id="mp-close" aria-label="Close">✕</button>
        </div>
        <iframe id="mp-sc-iframe"
            src="https://w.soundcloud.com/player/?url=https%3A//on.soundcloud.com/STbBCaOqiw2rMiNOQF&color=%23ffffff&auto_play=false&hide_related=true&show_comments=false&show_user=true&show_reposts=false&show_teaser=false"
            allow="autoplay"></iframe>
    </div>'''
if OLD5 in html:
    html = html.replace(OLD5, NEW5, 1)
    changes.append('✅ Music player HTML → SoundCloud widget')
else:
    changes.append('❌ Music player HTML: pattern not found')

# ── 6. Replace music player JS ────────────────────────────────────────────────
OLD6 = '''        // ── Music player ──────────────────────────────────────────────────────
        (function initMusicPlayer() {
            const player = document.getElementById('music-player');
            const mpName = document.getElementById('mp-name');
            const mpAudio = document.getElementById('mp-audio');
            const mpPlay = document.getElementById('mp-play');
            const mpClose = document.getElementById('mp-close');
            if (!player) return;

            let isPlaying = false;

            function openPlayer(artistName, trackSrc) {
                mpName.textContent = artistName;
                // TODO: set real track src when available
                // mpAudio.src = trackSrc || '';
                player.classList.add('open');
            }

            function togglePlay() {
                if (mpAudio.src && mpAudio.src !== window.location.href) {
                    if (isPlaying) { mpAudio.pause(); mpPlay.textContent = '▶'; }
                    else { mpAudio.play().catch(() => {}); mpPlay.textContent = '⏸'; }
                    isPlaying = !isPlaying;
                } else {
                    mpPlay.textContent = isPlaying ? '▶' : '⏸';
                    isPlaying = !isPlaying;
                }
            }

            mpPlay.addEventListener('click', togglePlay);
            mpClose.addEventListener('click', () => {
                player.classList.remove('open');
                mpAudio.pause();
                isPlaying = false;
                mpPlay.textContent = '▶';
            });

            // Open player on strip click (hook into existing click handler)
            document.getElementById('lineup-column').addEventListener('click', (e) => {
                const wrap = e.target.closest('.strip-wrap');
                if (!wrap) return;
                const a = artists.find(x => x.id === +wrap.dataset.artistId);
                if (a) openPlayer(a.name, null /* TODO: a.track */);
            });
        })();'''
NEW6 = '''        // ── Music player (SoundCloud) ─────────────────────────────────────────
        (function initMusicPlayer() {
            const player = document.getElementById('music-player');
            const mpClose = document.getElementById('mp-close');
            if (!player) return;

            function openPlayer() {
                player.classList.add('open');
            }

            mpClose.addEventListener('click', () => player.classList.remove('open'));

            // Open player on strip click
            document.getElementById('lineup-column').addEventListener('click', (e) => {
                const wrap = e.target.closest('.strip-wrap');
                if (wrap) openPlayer();
            });
        })();

        // ── Football game ─────────────────────────────────────────────────────
        (function initFootballGame() {
            const canvas = document.getElementById('football-canvas');
            const scoreEl = document.getElementById('fb-game-score');
            const msgEl = document.getElementById('fb-game-msg');
            const btn = document.getElementById('btn-football');
            if (!canvas || !btn) return;

            const ctx = canvas.getContext('2d');
            let width, height, raf;
            let active = false;
            let score = 0, isGameOver = false;

            const gravity = 0.5, friction = 0.98, wBounce = 0.8, fBounce = 0.5;
            const ball = { x:0, y:0, vx:0, vy:0, radius:45, rotation:0, angV:0 };
            let particles = [];

            function resize() {
                width = canvas.width = window.innerWidth;
                height = canvas.height = window.innerHeight;
                ball.radius = Math.min(Math.min(width, height) * 0.08, 70);
                if (ball.radius < 35) ball.radius = 35;
            }

            function initBall() {
                ball.x = width / 2; ball.y = height * 0.3;
                ball.vx = (Math.random() - 0.5) * 6;
                ball.vy = -5;
                ball.angV = (Math.random() - 0.5) * 0.3;
            }

            function spawnParticles(x, y) {
                for (let i = 0; i < 12; i++) {
                    particles.push({
                        x, y,
                        vx: (Math.random() - 0.5) * 22,
                        vy: (Math.random() - 0.5) * 22,
                        life: 1,
                        size: Math.random() * 8 + 2,
                        color: Math.random() > 0.5 ? '#ccc' : '#111'
                    });
                }
            }

            function punkCircle(x, y, r, jitter) {
                ctx.beginPath();
                for (let i = 0; i <= Math.PI * 2; i += 0.4) {
                    const jx = x + Math.cos(i) * r + (Math.random() - 0.5) * jitter;
                    const jy = y + Math.sin(i) * r + (Math.random() - 0.5) * jitter;
                    i === 0 ? ctx.moveTo(jx, jy) : ctx.lineTo(jx, jy);
                }
                ctx.closePath();
                ctx.stroke();
            }

            function update() {
                ball.vy += gravity;
                ball.vx *= friction; ball.vy *= friction;
                ball.x += ball.vx; ball.y += ball.vy;
                ball.rotation += ball.angV;

                if (ball.x - ball.radius < 0) {
                    ball.x = ball.radius; ball.vx *= -wBounce;
                    ball.angV += ball.vy * 0.02;
                } else if (ball.x + ball.radius > width) {
                    ball.x = width - ball.radius; ball.vx *= -wBounce;
                    ball.angV -= ball.vy * 0.02;
                }
                if (ball.y - ball.radius < 0) {
                    ball.y = ball.radius; ball.vy *= -wBounce;
                }
                if (ball.y + ball.radius > height) {
                    ball.y = height - ball.radius;
                    ball.vy *= -fBounce; ball.vx *= 0.8; ball.angV *= 0.8;
                    if (!isGameOver && score > 0) {
                        isGameOver = true;
                        msgEl.style.opacity = 1;
                        document.body.style.transform = `translate(${(Math.random()-0.5)*14}px,${(Math.random()-0.5)*14}px)`;
                        setTimeout(() => { document.body.style.transform = ''; }, 50);
                        setTimeout(() => {
                            msgEl.style.opacity = 0;
                            score = 0; scoreEl.querySelector('#fb-score-num').textContent = score;
                            isGameOver = false;
                        }, 1500);
                    }
                }

                for (let i = particles.length - 1; i >= 0; i--) {
                    const p = particles[i];
                    p.x += p.vx; p.y += p.vy; p.life -= 0.04;
                    if (p.life <= 0) particles.splice(i, 1);
                }
            }

            function draw() {
                ctx.clearRect(0, 0, width, height);
                ctx.save();
                ctx.translate(ball.x, ball.y);
                ctx.rotate(ball.rotation);

                ctx.lineCap = 'square'; ctx.lineJoin = 'miter';
                ctx.strokeStyle = '#ccc'; ctx.lineWidth = 3;
                punkCircle(4, 4, ball.radius, 4);
                ctx.strokeStyle = '#111'; ctx.lineWidth = 6;
                punkCircle(0, 0, ball.radius, 3);

                // € symbol
                ctx.beginPath();
                for (let i = Math.PI * 0.25; i <= Math.PI * 1.75; i += 0.4) {
                    const jx = Math.cos(i) * (ball.radius * 0.5) + (Math.random()-0.5)*3;
                    const jy = Math.sin(i) * (ball.radius * 0.5) + (Math.random()-0.5)*3;
                    i === Math.PI * 0.25 ? ctx.moveTo(jx + ball.radius*0.1, jy) : ctx.lineTo(jx + ball.radius*0.1, jy);
                }
                ctx.stroke();
                ctx.beginPath();
                ctx.moveTo(-ball.radius*0.6, -ball.radius*0.1+(Math.random()-0.5)*2);
                ctx.lineTo( ball.radius*0.2, -ball.radius*0.1+(Math.random()-0.5)*2);
                ctx.moveTo(-ball.radius*0.6,  ball.radius*0.15+(Math.random()-0.5)*2);
                ctx.lineTo( ball.radius*0.1,  ball.radius*0.15+(Math.random()-0.5)*2);
                ctx.stroke();
                ctx.restore();

                ctx.lineWidth = 3;
                particles.forEach(p => {
                    ctx.strokeStyle = p.color; ctx.globalAlpha = p.life;
                    ctx.beginPath();
                    ctx.moveTo(p.x - p.size, p.y - p.size); ctx.lineTo(p.x + p.size, p.y + p.size);
                    ctx.moveTo(p.x + p.size, p.y - p.size); ctx.lineTo(p.x - p.size, p.y + p.size);
                    ctx.stroke();
                });
                ctx.globalAlpha = 1;
            }

            function gameLoop() {
                if (!active) return;
                update(); draw();
                raf = requestAnimationFrame(gameLoop);
            }

            function kick(clientX, clientY, ev) {
                const dx = clientX - ball.x, dy = clientY - ball.y;
                if (Math.sqrt(dx*dx + dy*dy) < ball.radius * 2.5) {
                    if (ev && ev.cancelable) ev.preventDefault();
                    if (isGameOver) { isGameOver = false; score = 0; msgEl.style.opacity = 0; }
                    score++;
                    scoreEl.querySelector('#fb-score-num').textContent = score;
                    const nd = dx / ball.radius;
                    ball.vy = -14 - Math.random()*4;
                    ball.vx = -nd * 10 + (Math.random()-0.5)*4;
                    ball.angV = nd * 0.8;
                    spawnParticles(clientX, clientY);
                    return true;
                }
                return false;
            }

            function startGame() {
                active = true;
                canvas.classList.add('active');
                scoreEl.classList.add('active');
                resize(); initBall(); score = 0; isGameOver = false;
                scoreEl.querySelector('#fb-score-num').textContent = 0;
                cancelAnimationFrame(raf);
                gameLoop();
                btn.textContent = '❌';
            }

            function stopGame() {
                active = false;
                canvas.classList.remove('active');
                scoreEl.classList.remove('active');
                cancelAnimationFrame(raf);
                btn.textContent = '⚽';
            }

            btn.addEventListener('click', () => active ? stopGame() : startGame());
            window.addEventListener('resize', () => { if (active) resize(); });
            window.addEventListener('mousedown', (e) => { if (active) kick(e.clientX, e.clientY, e); });
            window.addEventListener('touchstart', (e) => {
                if (!active) return;
                for (let i = 0; i < e.changedTouches.length; i++)
                    kick(e.changedTouches[i].clientX, e.changedTouches[i].clientY, e);
            }, { passive: false });
        })();'''
if OLD6 in html:
    html = html.replace(OLD6, NEW6, 1)
    changes.append('✅ Music player + Football game JS added')
else:
    changes.append('❌ Music player JS: pattern not found')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

for c in changes:
    print(c)
print(f'\nTotal: {len(html)} bytes')
