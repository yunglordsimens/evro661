#!/usr/bin/env python3
"""Patch #3:
- update keiko-sei artist data (now has bio + assets)
- remove 'DON'T LET IT FALL' text from football game
- football game uses ball.png with fallback to punk drawing
- SoundCloud lazy load (don't preload iframe on page open)
- auto render quality (detect low-end / mobile, disable bloom/shadows)
- minor mobile responsive tweaks
"""

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

changes = []

def patch(old, new, label):
    global html
    if old in html:
        html = html.replace(old, new, 1)
        changes.append(f'✅ {label}')
    else:
        changes.append(f'❌ {label} — pattern NOT FOUND')

# ── 1. keiko-sei data ─────────────────────────────────────────────────────────
patch(
    "{ id:18, block:3, slug:'keiko-sei', name:'KEIKO SEI',\n              bio: null, imgs: null, vids: null },",
    "{ id:18, block:3, slug:'keiko-sei', name:'KEIKO SEI',\n              bio:'Keiko Sei is a musical project by Daniel Rajmon and Tamara Spalajković. Their sound blends guitar loops and fractured harmonies of bedroom pop with introspective lyrics and flashes of euphoria. The band takes their name from the Japanese media theorist, whom they\\'ve never met but whose book \"Final Landscape\" left a mark on both. On favu label they recently released their second album \"Her Car\".',\n              imgs:['artists-data/keiko-sei/photo-1.png','artists-data/keiko-sei/photo-2.JPG'],\n              vids:['artists-data/keiko-sei/video.mp4'] },",
    'keiko-sei artist data populated'
)

# ── 2. Remove "DON'T LET IT FALL" text + simplify score ───────────────────────
patch(
    '''<div id="fb-game-score"><span id="fb-score-num">0</span> &nbsp;|&nbsp; DON'T LET IT FALL</div>''',
    '''<div id="fb-game-score"><span id="fb-score-num">0</span></div>''',
    "Removed 'DON'T LET IT FALL' text"
)

# ── 3. Football: load ball.png and use drawImage with fallback ────────────────
# Replace the entire draw() function to support image rendering
OLD_DRAW = '''            function draw() {
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
            }'''

NEW_DRAW = '''            // Try to load ball.png; if it fails, use vector punk-ball
            const ballImg = new Image();
            let ballImgLoaded = false;
            ballImg.onload = () => { ballImgLoaded = true; };
            ballImg.onerror = () => { ballImgLoaded = false; };
            ballImg.src = 'ball.png';

            function drawVectorBall() {
                ctx.lineCap = 'square'; ctx.lineJoin = 'miter';
                ctx.strokeStyle = '#ccc'; ctx.lineWidth = 3;
                punkCircle(4, 4, ball.radius, 4);
                ctx.strokeStyle = '#111'; ctx.lineWidth = 6;
                punkCircle(0, 0, ball.radius, 3);
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
            }

            function draw() {
                ctx.clearRect(0, 0, width, height);
                ctx.save();
                ctx.translate(ball.x, ball.y);
                ctx.rotate(ball.rotation);
                if (ballImgLoaded) {
                    const r = ball.radius;
                    ctx.drawImage(ballImg, -r, -r, r * 2, r * 2);
                } else {
                    drawVectorBall();
                }
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
            }'''

patch(OLD_DRAW, NEW_DRAW, 'Football: use ball.png with vector fallback')

# ── 4. SoundCloud lazy load: empty iframe src; populate on first open ─────────
patch(
    '''        <iframe id="mp-sc-iframe"
            src="https://w.soundcloud.com/player/?url=https%3A//on.soundcloud.com/STbBCaOqiw2rMiNOQF&color=%23ffffff&auto_play=false&hide_related=true&show_comments=false&show_user=true&show_reposts=false&show_teaser=false"
            allow="autoplay"></iframe>''',
    '''        <iframe id="mp-sc-iframe"
            data-src="https://w.soundcloud.com/player/?url=https%3A//on.soundcloud.com/STbBCaOqiw2rMiNOQF&color=%23ffffff&auto_play=false&hide_related=true&show_comments=false&show_user=true&show_reposts=false&show_teaser=false"
            loading="lazy"
            allow="autoplay"></iframe>''',
    'SoundCloud: iframe src deferred (data-src)'
)

# Update music player JS: set src on first open
patch(
    '''        // ── Music player (SoundCloud) ─────────────────────────────────────────
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
        })();''',
    '''        // ── Music player (SoundCloud, lazy) ───────────────────────────────────
        (function initMusicPlayer() {
            const player = document.getElementById('music-player');
            const mpClose = document.getElementById('mp-close');
            const iframe = document.getElementById('mp-sc-iframe');
            if (!player) return;
            let iframeLoaded = false;

            function openPlayer() {
                if (!iframeLoaded && iframe && iframe.dataset.src) {
                    iframe.src = iframe.dataset.src;
                    iframeLoaded = true;
                }
                player.classList.add('open');
            }

            mpClose.addEventListener('click', () => player.classList.remove('open'));

            document.getElementById('lineup-column').addEventListener('click', (e) => {
                const wrap = e.target.closest('.strip-wrap');
                if (wrap) openPlayer();
            });
        })();''',
    'Music player: lazy SoundCloud loading'
)

# ── 5. Auto render quality + mobile detection ─────────────────────────────────
patch(
    '''        const camera = new THREE.PerspectiveCamera(55, window.innerWidth / window.innerHeight, 0.1, 1000);
        camera.position.set(0, 0, 14);

        const renderer = new THREE.WebGLRenderer({ antialias: true, powerPreference: "high-performance" });
        renderer.setSize(window.innerWidth, window.innerHeight);
        renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2));
        renderer.shadowMap.enabled = true;
        renderer.shadowMap.type = THREE.PCFSoftShadowMap;
        renderer.toneMapping = THREE.ACESFilmicToneMapping;
        renderer.toneMappingExposure = 1.0;
        container.appendChild(renderer.domElement);

        // --- ПОСТОБРАБОТКА (Bloom) ---
        const renderScene = new THREE.RenderPass(scene, camera);
        const bloomPass = new THREE.UnrealBloomPass(new THREE.Vector2(window.innerWidth, window.innerHeight), 1.5, 0.4, 0.85);
        bloomPass.threshold = 0.2;
        bloomPass.strength = 1.4;
        bloomPass.radius = 0.6;

        const composer = new THREE.EffectComposer(renderer);
        composer.addPass(renderScene);
        composer.addPass(bloomPass);''',
    '''        const camera = new THREE.PerspectiveCamera(55, window.innerWidth / window.innerHeight, 0.1, 1000);
        camera.position.set(0, 0, 14);

        // ─ Auto render quality detection ─────────────────────────────────────
        // Goal: keep heat/fans down on weak machines, mobile, and battery savers
        const isMobile = /android|iphone|ipad|ipod|mobile/i.test(navigator.userAgent) || window.innerWidth < 820;
        const lowMemory = (navigator.deviceMemory && navigator.deviceMemory <= 4);
        const lowCores = (navigator.hardwareConcurrency && navigator.hardwareConcurrency <= 4);
        const reducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
        const lowEnd = isMobile || lowMemory || lowCores || reducedMotion;
        const QUALITY = lowEnd ? 'low' : 'high';
        window.__EVRO_QUALITY = QUALITY;

        const renderer = new THREE.WebGLRenderer({
            antialias: !lowEnd,
            powerPreference: lowEnd ? "low-power" : "high-performance",
            alpha: false
        });
        renderer.setSize(window.innerWidth, window.innerHeight);
        renderer.setPixelRatio(lowEnd ? 1 : Math.min(window.devicePixelRatio, 2));
        renderer.shadowMap.enabled = !lowEnd;
        if (!lowEnd) renderer.shadowMap.type = THREE.PCFSoftShadowMap;
        renderer.toneMapping = THREE.ACESFilmicToneMapping;
        renderer.toneMappingExposure = 1.0;
        container.appendChild(renderer.domElement);

        // --- ПОСТОБРАБОТКА (Bloom) — отключаем целиком на слабых ---
        const renderScene = new THREE.RenderPass(scene, camera);
        const bloomPass = new THREE.UnrealBloomPass(
            new THREE.Vector2(window.innerWidth, window.innerHeight),
            lowEnd ? 0.6 : 1.5,
            lowEnd ? 0.2 : 0.4,
            0.85
        );
        bloomPass.threshold = 0.2;
        bloomPass.strength = lowEnd ? 0.7 : 1.4;
        bloomPass.radius = lowEnd ? 0.3 : 0.6;

        const composer = new THREE.EffectComposer(renderer);
        composer.addPass(renderScene);
        if (!lowEnd) composer.addPass(bloomPass);''',
    'Auto render quality + low-end detection'
)

# ── 6. Throttle animation on low-end + cap framerate (~30fps when low) ────────
patch(
    '''        function animate() {
            if (!renderingActive) return;

            requestAnimationFrame(animate);
            const time = clock.getElapsedTime();''',
    '''        let __lastFrame = 0;
        const __frameStep = (window.__EVRO_QUALITY === 'low') ? 1000 / 30 : 0; // 30fps on low-end, vsync otherwise
        function animate(now) {
            if (!renderingActive) return;
            requestAnimationFrame(animate);
            if (__frameStep) {
                if (!now) now = performance.now();
                if (now - __lastFrame < __frameStep) return;
                __lastFrame = now;
            }
            const time = clock.getElapsedTime();''',
    'Animation: cap to 30fps on low-end devices'
)

# ── 7. Mobile responsive tweaks (donate poster + lineup column) ───────────────
patch(
    '            #donate-poster { width: 150px; height: 150px; bottom: 14px; right: 14px; }',
    '''            #donate-poster { width: 130px; height: 130px; bottom: 12px; right: 12px; }
            #music-player { width: 100vw; }
            #fundraising-bar { width: auto; flex: 1; min-width: 0; }
            #fundraising-bar .fb-label { font-size: 0.55rem; }
            #fb-game-score { bottom: 60px; font-size: 0.75rem; }''',
    'Mobile responsive: donate poster + music player + score'
)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

for c in changes:
    print(c)
print(f'\nTotal: {len(html)} bytes')
