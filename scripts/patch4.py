#!/usr/bin/env python3
"""Patch #4:
- remove SoundCloud icon from door page header
- shrink door-lang to match inner-lang size
- football: remove score counter and WASTED message
- ball.png fallback: simple solid black circle (no vector punk drawing)
- 'Strahov / Praha' → 'Strahov Stadium'
- donate poster: bigger text + drop-shadow on FOR hover (closer to React mock)
- block navigation arrows in lineup (click → scroll to next block top)
- multi-language bio support: bio can be {uk,en,cz} object; switcher updates panel
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
        changes.append(f'❌ {label}')

# ── 1. Remove SoundCloud icon from door page ──────────────────────────────────
patch(
    '''                        <a href="#" target="_blank" rel="noopener" aria-label="SoundCloud" title="SoundCloud (добавь ссылку когда будет)">
                            <svg viewBox="0 0 24 24">
                                <path d="M1.175 12.225c-.051 0-.094.046-.101.1l-.233 2.154.233 2.105c.007.058.05.104.101.104.05 0 .09-.46.099-.104l.27-2.105-.27-2.154c0-.057-.045-.1-.099-.1m-.899.828c-.06 0-.091.037-.104.094L0 14.479l.165 1.308c0 .055.045.094.09.094s.089-.045.104-.104l.21-1.319-.21-1.235c0-.062-.045-.094-.09-.094m1.83-1.229c-.061 0-.12.045-.12.104l-.21 2.563.225 2.458c0 .06.045.12.119.12.061 0 .105-.061.121-.12l.254-2.474-.254-2.548c-.016-.06-.061-.12-.121-.12m.945-.089c-.075 0-.135.06-.15.135l-.193 2.64.21 2.544c.016.077.075.138.15.138.074 0 .135-.061.15-.15l.24-2.532-.24-2.642c0-.074-.061-.135-.135-.135l-.012.002zm1.155.36c-.005-.09-.075-.149-.159-.149-.09 0-.158.06-.164.149l-.217 2.43.2 2.563c0 .09.075.157.159.157.074 0 .148-.068.148-.158l.227-2.563-.227-2.444zm.809-1.709c-.101 0-.18.09-.18.181l-.21 3.957.187 2.563c0 .09.08.164.18.164.094 0 .174-.09.18-.18l.209-2.563-.209-3.972c-.007-.104-.088-.18-.18-.18m.959-.914c-.105 0-.195.09-.203.194l-.18 4.872.165 2.548c0 .12.09.209.195.209.104 0 .194-.089.21-.209l.193-2.548-.192-4.872c-.016-.12-.105-.194-.21-.194m.989-.449c-.121 0-.22.104-.226.225l-.165 5.275.165 2.52c0 .119.105.225.225.225.121 0 .211-.105.225-.225l.182-2.52-.18-5.275c0-.121-.105-.225-.225-.225m1.245.045c-.001-.135-.105-.24-.239-.24-.119 0-.24.105-.24.24l-.149 5.441.149 2.503c0 .135.105.24.24.24.119 0 .24-.105.24-.24l.164-2.503-.165-5.456zm.749-1.784c-.149 0-.27.119-.27.27l-.18 7.142.165 2.473c0 .15.119.271.27.271.149 0 .27-.121.285-.271l.18-2.473-.18-7.142c-.016-.149-.135-.27-.285-.27m1.005-.345c-.165 0-.299.135-.299.3l-.146 7.476.146 2.443c0 .166.134.301.3.301.165 0 .299-.135.299-.301l.18-2.443-.18-7.476c-.014-.165-.149-.3-.3-.3m1.214.39c-.181 0-.33.149-.33.329l-.135 7.057.135 2.413c0 .18.149.329.33.329s.329-.149.329-.329l.15-2.413-.15-7.057c0-.18-.149-.329-.329-.329m.93-2.067a.36.36 0 00-.36.36l-.165 9.124.165 2.398a.36.36 0 00.36.359c.196 0 .345-.164.359-.359l.18-2.398-.18-9.125c-.014-.193-.18-.359-.359-.359m1.23-.105c-.045-.029-.105-.045-.165-.045a.357.357 0 00-.21.06.39.39 0 00-.165.314l-.029.166-.121 8.954s0 .03.121 2.443v.029a.39.39 0 00.105.255c.061.06.149.105.255.105.09 0 .18-.045.24-.121.075-.061.119-.149.119-.255l.014-.241.135-2.203-.149-9.139a.387.387 0 00-.149-.314m11.16 7.11s-.51 0-.93.135c-.51-2.595-2.83-4.522-5.609-4.522-1.05 0-2.04.279-2.88.755-.314.18-.404.359-.404.629v9.244c0 .299.225.524.495.555h9.328c2.052-.045 3.694-1.71 3.694-3.793 0-2.117-1.711-3.793-3.793-3.793z"/>
                            </svg>
                        </a>
                    </div>''',
    '''                    </div>''',
    'Removed SoundCloud icon from door page'
)

# ── 2. Shrink door-lang CSS to match inner-lang ───────────────────────────────
patch(
    '''        .lang-switch {
            display: flex;
            gap: 10px;
            font-size: 0.9rem;
            letter-spacing: 2px;
            font-weight: 500;
        }

        .lang-switch span {
            cursor: pointer;
            opacity: 0.5;
            transition: opacity 0.3s;
        }

        .lang-switch span:hover, .lang-switch span.active {
            opacity: 1;
        }''',
    '''        .lang-switch {
            display: flex;
            gap: 7px;
            font-size: 0.72rem;
            letter-spacing: 2px;
            font-weight: 500;
        }
        .lang-switch span {
            cursor: pointer;
            opacity: 0.35;
            transition: opacity 0.3s;
        }
        .lang-switch span:hover, .lang-switch span.active { opacity: 1; }
        .lang-switch span[style*="opacity: 0.3"] { cursor: default; opacity: 0.2 !important; }''',
    'door-lang sized like inner-lang'
)

# ── 3. Football: remove score counter + WASTED message DOM elements ───────────
patch(
    '''        <!-- Football game elements -->
        <canvas id="football-canvas"></canvas>
        <div id="fb-game-score"><span id="fb-score-num">0</span></div>
        <div id="fb-game-msg">WASTED!</div>''',
    '''        <!-- Football game elements (no score, no game-over message) -->
        <canvas id="football-canvas"></canvas>''',
    'Removed score + WASTED HTML'
)

# Remove score/msg references in JS — strip lines that touch scoreEl / msgEl
OLD_JS = '''        // ── Football game ─────────────────────────────────────────────────────
        (function initFootballGame() {
            const canvas = document.getElementById('football-canvas');
            const scoreEl = document.getElementById('fb-game-score');
            const msgEl = document.getElementById('fb-game-msg');
            const btn = document.getElementById('btn-football');
            if (!canvas || !btn) return;'''
NEW_JS = '''        // ── Football game ─────────────────────────────────────────────────────
        (function initFootballGame() {
            const canvas = document.getElementById('football-canvas');
            const btn = document.getElementById('btn-football');
            if (!canvas || !btn) return;'''
patch(OLD_JS, NEW_JS, 'Removed score/msg refs from game JS init')

# Replace all the score/msg manipulation blocks
patch(
    '''                if (ball.y + ball.radius > height) {
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
                }''',
    '''                if (ball.y + ball.radius > height) {
                    ball.y = height - ball.radius;
                    ball.vy *= -fBounce; ball.vx *= 0.8; ball.angV *= 0.8;
                }''',
    'Removed game-over logic from physics'
)

patch(
    '''            function kick(clientX, clientY, ev) {
                const dx = clientX - ball.x, dy = clientY - ball.y;
                if (Math.sqrt(dx*dx + dy*dy) < ball.radius * 2.5) {
                    if (ev && ev.cancelable) ev.preventDefault();
                    if (isGameOver) { isGameOver = false; score = 0; msgEl.style.opacity = 0; }
                    score++;
                    scoreEl.querySelector('#fb-score-num').textContent = score;
                    const nd = dx / ball.radius;''',
    '''            function kick(clientX, clientY, ev) {
                const dx = clientX - ball.x, dy = clientY - ball.y;
                if (Math.sqrt(dx*dx + dy*dy) < ball.radius * 2.5) {
                    if (ev && ev.cancelable) ev.preventDefault();
                    const nd = dx / ball.radius;''',
    'Removed score increment in kick()'
)

patch(
    '''            function startGame() {
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
            }''',
    '''            function startGame() {
                active = true;
                canvas.classList.add('active');
                resize(); initBall();
                cancelAnimationFrame(raf);
                gameLoop();
                btn.textContent = '❌';
            }

            function stopGame() {
                active = false;
                canvas.classList.remove('active');
                cancelAnimationFrame(raf);
                btn.textContent = '⚽';
            }''',
    'Removed score from start/stop'
)

# Remove now-unused state vars
patch(
    '            let active = false;\n            let score = 0, isGameOver = false;',
    '            let active = false;',
    'Removed score/isGameOver state'
)

# ── 4. Ball.png fallback: simple solid black circle (replace vector punk) ─────
patch(
    '''            function drawVectorBall() {
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
            }''',
    '''            function drawFallbackBall() {
                // Simple solid circle while ball.png loads or if it's missing
                ctx.fillStyle = '#111';
                ctx.beginPath();
                ctx.arc(0, 0, ball.radius, 0, Math.PI * 2);
                ctx.fill();
            }''',
    'Ball fallback: simple solid black circle'
)

patch(
    '''                if (ballImgLoaded) {
                    const r = ball.radius;
                    ctx.drawImage(ballImg, -r, -r, r * 2, r * 2);
                } else {
                    drawVectorBall();
                }''',
    '''                if (ballImgLoaded) {
                    const r = ball.radius;
                    ctx.drawImage(ballImg, -r, -r, r * 2, r * 2);
                } else {
                    drawFallbackBall();
                }''',
    'Use drawFallbackBall instead of drawVectorBall'
)

# ── 5. 'Strahov / Praha' → 'Strahov Stadium' ──────────────────────────────────
patch(
    '<p>Strahov / Praha</p>',
    '<p>Strahov Stadium, Prague</p>',
    "Lineup date footer → 'Strahov Stadium, Prague'"
)
patch(
    '<h3>Strahov / Praha</h3>',
    '<h3>Strahov Stadium</h3>',
    "Map heading → 'Strahov Stadium'"
)

# ── 6. Donate poster: bigger text + drop-shadow on FOR hover ──────────────────
patch(
    '''        /* FUNDRAISER / UKRAINE — long word, tight fit */
        .donate-block-1 span,
        .donate-block-3 span {
            color: #fff;
            font-size: clamp(1.5rem, 8.5vw, 1.95rem);
            letter-spacing: -0.01em;
        }
        /* FOR — short word, much bigger */
        .donate-block-2 span {
            color: #000;
            font-size: clamp(2.8rem, 14vw, 3.6rem);
            letter-spacing: 0.02em;
        }
        #donate-poster:hover .donate-block-1 span,
        #donate-poster:hover .donate-block-3 span { color: #fff; transform: scale(1.05); }
        #donate-poster:hover .donate-block-2 span { color: #fff; transform: scale(1.08); }''',
    '''        /* FUNDRAISER / UKRAINE — match React proportions on small poster */
        .donate-block-1 span,
        .donate-block-3 span {
            color: #fff;
            font-size: clamp(1.7rem, 9.5vw, 2.4rem);
            letter-spacing: -0.005em;
        }
        .donate-block-3 span { letter-spacing: 0.08em; }
        /* FOR — short word, much bigger */
        .donate-block-2 span {
            color: #000;
            font-size: clamp(3.3rem, 16vw, 4.4rem);
            letter-spacing: 0.02em;
        }
        #donate-poster:hover .donate-block-1 span,
        #donate-poster:hover .donate-block-3 span {
            color: #fff;
            transform: scale(1.05);
            text-shadow: 0 2px 8px rgba(0,0,0,0.4);
        }
        #donate-poster:hover .donate-block-2 span {
            color: #fff;
            transform: scale(1.10);
            text-shadow: 0 5px 15px rgba(0,0,0,0.5);
        }''',
    'Donate poster: bigger text + FOR drop-shadow on hover'
)

# ── 7. Block navigation arrows in lineup ──────────────────────────────────────
# Find the lineup builder and inject block dividers + click handlers
patch(
    '''        // ---- Сборка лайн-апа ----
        function buildLineup() {
            const col = document.getElementById('lineup-column');
            if (!col) return;

            const insertIllustrationAfter = 9; // после Block 1 (по аналогии с jsx-моком)

            artists.forEach((a, idx) => {
                const wrap = document.createElement('div');
                wrap.className = 'strip-wrap';
                wrap.dataset.artistId = a.id;
                wrap.dataset.bio = a.bio;''',
    '''        // ---- Сборка лайн-апа ----
        function buildLineup() {
            const col = document.getElementById('lineup-column');
            if (!col) return;

            const insertIllustrationAfter = 9; // после Block 1 (по аналогии с jsx-моком)
            let prevBlock = null;

            artists.forEach((a, idx) => {
                // Block divider (with arrow) before first artist of a new block (except block 1)
                if (prevBlock !== null && a.block !== prevBlock) {
                    const div = document.createElement('div');
                    div.className = 'block-divider';
                    div.dataset.targetBlock = a.block;
                    div.innerHTML = `<button class="block-arrow" type="button" aria-label="Go to Block ${a.block}">
                        <span class="arrow-label">Block ${a.block}</span>
                        <span class="arrow-icon">↓</span>
                    </button>`;
                    col.appendChild(div);
                }
                prevBlock = a.block;

                const wrap = document.createElement('div');
                wrap.className = 'strip-wrap';
                wrap.dataset.artistId = a.id;
                wrap.dataset.block = a.block;
                wrap.dataset.bio = typeof a.bio === 'string' ? a.bio : (a.bio && (a.bio[currentLang] || a.bio.en || a.bio.uk) || '');''',
    'Lineup: inject block dividers with arrows'
)

# Insert block-divider CSS + arrow click handler. Inject CSS before .scroll-indicator
patch(
    '        .scroll-indicator {',
    '''        .block-divider {
            width: 100%;
            display: flex;
            justify-content: center;
            padding: 28px 0 14px;
            position: relative;
        }
        .block-arrow {
            background: rgba(8,6,4,0.65);
            border: 1px solid rgba(255,255,255,0.2);
            color: rgba(255,255,255,0.75);
            padding: 10px 22px;
            font-family: 'Cinzel', serif;
            font-size: 0.78rem;
            letter-spacing: 3px;
            text-transform: uppercase;
            cursor: pointer;
            display: flex;
            align-items: center;
            gap: 14px;
            border-radius: 2px;
            transition: color 0.25s, border-color 0.25s, background 0.25s, transform 0.25s;
            backdrop-filter: blur(6px);
        }
        .block-arrow:hover {
            color: #fff;
            border-color: rgba(255,255,255,0.5);
            background: rgba(8,6,4,0.85);
            transform: translateY(2px);
        }
        .block-arrow .arrow-icon { font-size: 1rem; line-height: 1; }

        .scroll-indicator {''',
    'Block divider CSS'
)

# Add arrow click handler at end of buildLineup or in init — append after buildLineup
patch(
    '''        document.getElementById('lineup-column').addEventListener('click', (e) => {
                const wrap = e.target.closest('.strip-wrap');
                if (wrap) openPlayer();
            });
        })();''',
    '''        document.getElementById('lineup-column').addEventListener('click', (e) => {
                const wrap = e.target.closest('.strip-wrap');
                if (wrap) openPlayer();
            });
        })();

        // ── Block-arrow scroll-to-block ───────────────────────────────────────
        (function initBlockArrows() {
            const col = document.getElementById('lineup-column');
            if (!col) return;
            col.addEventListener('click', (e) => {
                const arrow = e.target.closest('.block-arrow');
                if (!arrow) return;
                const divider = arrow.closest('.block-divider');
                if (!divider) return;
                // Find the FIRST .strip-wrap of the target block (i.e. the one immediately after this divider)
                const targetBlock = divider.dataset.targetBlock;
                const firstStrip = divider.nextElementSibling;
                if (!firstStrip) return;
                // Scroll so the strip's top sits at the very top of the viewport
                const y = firstStrip.getBoundingClientRect().top + window.scrollY - 8;
                window.scrollTo({ top: y, behavior: 'smooth' });
            });
        })();''',
    'Block arrow click handler'
)

# ── 8. Multi-language bio + lang switcher actually swaps ──────────────────────
# Inject `currentLang` global + sync between door-lang & inner-lang BEFORE buildLineup
patch(
    '        // ---- Сборка лайн-апа ----',
    '''        // ── Language state (UK default) ───────────────────────────────────────
        let currentLang = 'uk';
        function getBio(a) {
            if (!a.bio) return '';
            if (typeof a.bio === 'string') return a.bio;
            return a.bio[currentLang] || a.bio.en || a.bio.uk || a.bio.cz || '';
        }
        function setLang(lang) {
            currentLang = lang;
            // Sync both lang switchers' active state
            const sel = `[data-lang="${lang}"]`;
            document.querySelectorAll('#door-lang span, #inner-lang span:not(.sep)').forEach(el => {
                el.classList.toggle('active', el.dataset.lang === lang);
            });
            // Update strip-wrap dataset bios + any open panel
            document.querySelectorAll('.strip-wrap').forEach(wrap => {
                const id = +wrap.dataset.artistId;
                const a = artists.find(x => x.id === id);
                if (a) wrap.dataset.bio = getBio(a);
            });
            // If side panel is open, refresh its content
            window.dispatchEvent(new CustomEvent('langchange'));
        }
        window.setLang = setLang;

        // ---- Сборка лайн-апа ----''',
    'Multi-lang state + setLang()'
)

# Add data-lang to door-lang spans
patch(
    '''                    <div class="lang-switch" id="door-lang">
                        <span class="active">🇺🇦 UKR</span>
                        <span style="opacity: 0.3;">|</span>
                        <span>🇬🇧 ENG</span>
                        <span style="opacity: 0.3;">|</span>
                        <span>🇨🇿 CZE</span>
                    </div>''',
    '''                    <div class="lang-switch" id="door-lang">
                        <span class="active" data-lang="uk">🇺🇦 UKR</span>
                        <span style="opacity: 0.3;">|</span>
                        <span data-lang="en">🇬🇧 ENG</span>
                        <span style="opacity: 0.3;">|</span>
                        <span data-lang="cz">🇨🇿 CZE</span>
                    </div>''',
    'door-lang data-lang attrs'
)

patch(
    '''            <div id="inner-lang">
                <span class="active">🇺🇦 UKR</span>
                <span class="sep">|</span>
                <span>🇬🇧 ENG</span>
                <span class="sep">|</span>
                <span>🇨🇿 CZE</span>
            </div>''',
    '''            <div id="inner-lang">
                <span class="active" data-lang="uk">🇺🇦 UKR</span>
                <span class="sep">|</span>
                <span data-lang="en">🇬🇧 ENG</span>
                <span class="sep">|</span>
                <span data-lang="cz">🇨🇿 CZE</span>
            </div>''',
    'inner-lang data-lang attrs'
)

# Wire up click handlers — replace the existing dummy lang-switch listener
patch(
    '''        document.querySelectorAll('.lang-switch span').forEach(el => {''',
    '''        document.querySelectorAll('#door-lang span[data-lang], #inner-lang span[data-lang]').forEach(el => {''',
    'Lang switcher click selector → both switchers'
)

# Tweak the inline handler to call setLang
patch(
    '''        document.querySelectorAll('#door-lang span[data-lang], #inner-lang span[data-lang]').forEach(el => {
            el.addEventListener('click', (e) => {
                document.querySelectorAll('.lang-switch span').forEach(span => span.classList.remove('active'));''',
    '''        document.querySelectorAll('#door-lang span[data-lang], #inner-lang span[data-lang]').forEach(el => {
            el.addEventListener('click', (e) => {
                const lang = el.dataset.lang;
                if (window.setLang) { window.setLang(lang); return; }
                document.querySelectorAll('.lang-switch span').forEach(span => span.classList.remove('active'));''',
    'Wire lang click → setLang()'
)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

for c in changes:
    print(c)
print(f'\nTotal: {len(html)} bytes')
