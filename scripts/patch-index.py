#!/usr/bin/env python3
"""
Apply all SPEC changes to index.html.
Run from repo root: python3 scripts/patch-index.py
"""
import re, json, sys

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Track which patches applied
applied = []

def patch(label, old, new, count=1):
    global html
    if old not in html:
        print(f'  ⚠️  NOT FOUND: {label}', file=sys.stderr)
        return
    html = html.replace(old, new, count)
    applied.append(label)

# ─── 1. CSS: add new styles before </style> ──────────────────────────────────
NEW_CSS = r"""
        /* ── EYEBROW ── */
        .hero-eyebrow {
            font-family: 'Montserrat', sans-serif;
            font-size: 0.68rem;
            letter-spacing: 6px;
            text-transform: uppercase;
            font-weight: 300;
            color: rgba(255,255,255,0.45);
            margin-bottom: 14px;
            display: block;
        }

        /* ── DONATION COUNTER ── */
        .donation-counter { margin-top: 40px; max-width: 440px; }
        .donation-label {
            font-size: 0.72rem;
            letter-spacing: 3px;
            text-transform: uppercase;
            color: rgba(255,255,255,0.45);
            margin-bottom: 10px;
        }
        .donation-bar-wrap {
            height: 3px;
            background: rgba(255,255,255,0.1);
            border-radius: 2px;
            margin-bottom: 10px;
            overflow: hidden;
        }
        .donation-bar-fill {
            height: 100%;
            background: linear-gradient(to right, #ffd700, #ffaa00);
            border-radius: 2px;
            transition: width 0.8s ease;
        }
        .donation-amount {
            font-family: 'Cinzel', serif;
            font-size: 1rem;
            color: #fff;
            letter-spacing: 1px;
        }
        .donation-amount .goal { color: rgba(255,255,255,0.38); font-size: 0.82rem; }

        /* ── SOCIAL ICONS — left side event page ── */
        #event-social {
            position: fixed;
            left: 20px;
            top: 50%;
            transform: translateY(-50%);
            display: flex;
            flex-direction: column;
            align-items: center;
            gap: 22px;
            z-index: 28;
            opacity: 0;
            pointer-events: none;
            transition: opacity 1.5s ease;
        }
        #event-social.visible { opacity: 1; pointer-events: auto; }
        .ev-social-link {
            display: flex;
            flex-direction: column;
            align-items: center;
            gap: 7px;
            color: rgba(255,255,255,0.45);
            text-decoration: none;
            transition: color 0.3s, transform 0.3s;
        }
        .ev-social-link:hover { color: #ffd699; transform: scale(1.12); }
        .ev-social-link svg { width: 17px; height: 17px; fill: currentColor; }
        .ev-social-link span {
            writing-mode: vertical-rl;
            text-orientation: mixed;
            font-size: 0.58rem;
            letter-spacing: 2px;
            text-transform: uppercase;
            font-weight: 500;
        }

        /* ── DONATE POSTER — sticky bottom-right ── */
        #donate-poster {
            position: fixed;
            bottom: 22px;
            right: 22px;
            width: 190px;
            height: 190px;
            z-index: 40;
            cursor: pointer;
            perspective: 600px;
            text-decoration: none;
        }
        .donate-inner {
            width: 100%;
            height: 100%;
            position: relative;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            gap: 3px;
            transition: transform 0.15s ease-out, box-shadow 0.2s;
            transform-style: preserve-3d;
            box-shadow: 4px 6px 0 rgba(0,0,0,0.75);
            background: rgba(12,10,8,0.9);
            border: 1px solid rgba(255,255,255,0.12);
        }
        .donate-flag {
            position: absolute;
            inset: 0;
            display: flex;
            flex-direction: column;
            opacity: 0;
            transition: opacity 0.35s ease;
        }
        .donate-flag-top { flex: 1; background: #0057b7; }
        .donate-flag-bot { flex: 1; background: #ffd700; }
        #donate-poster:hover .donate-flag { opacity: 1; }
        .donate-line {
            position: relative;
            z-index: 1;
            font-family: 'Cinzel', serif;
            font-size: 0.78rem;
            letter-spacing: 3px;
            text-transform: uppercase;
            color: #fff;
            font-weight: 700;
            line-height: 1.4;
            text-align: center;
        }
        .donate-line.sm { font-size: 0.6rem; letter-spacing: 4px; color: rgba(255,255,255,0.55); }
        .donate-cta {
            position: relative;
            z-index: 1;
            margin-top: 10px;
            padding: 5px 16px;
            background: #fff;
            color: #000;
            font-family: 'Cinzel', serif;
            font-size: 0.68rem;
            letter-spacing: 3px;
            text-transform: uppercase;
            font-weight: 700;
            opacity: 0;
            transition: opacity 0.3s;
        }
        #donate-poster:hover .donate-cta { opacity: 1; }

        /* ── MUSIC PLAYER ── */
        #music-player {
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
        #mp-close:hover { color: #fff; }

        /* ── BOTTOM-LEFT CONTROLS ── */
        #bottom-left-ctrl {
            position: fixed;
            bottom: 24px;
            left: 24px;
            display: flex;
            gap: 8px;
            z-index: 40;
            opacity: 0;
            pointer-events: none;
            transition: opacity 1.5s ease;
        }
        #bottom-left-ctrl.visible { opacity: 1; pointer-events: auto; }
        .ctrl-btn {
            background: rgba(8,6,4,0.72);
            border: 1px solid rgba(255,255,255,0.13);
            color: rgba(255,255,255,0.65);
            width: 38px; height: 38px;
            border-radius: 4px;
            cursor: pointer;
            font-size: 1rem;
            display: flex;
            align-items: center;
            justify-content: center;
            transition: color 0.2s, border-color 0.2s;
            backdrop-filter: blur(6px);
        }
        .ctrl-btn:hover { color: #fff; border-color: rgba(255,255,255,0.35); }

        /* ── VIDEO BG ── */
        #lineup-video-bg {
            position: absolute;
            top: 0; left: 0;
            width: 100%; height: 100%;
            object-fit: cover;
            opacity: 0.28;
            z-index: 0;
            pointer-events: none;
        }
        #lineup-section { overflow: hidden; }

        /* ── MAP ── */
        #map-section {
            background: #050403;
            padding: 60px 10vw 80px;
            text-align: center;
            position: relative;
            z-index: 2;
        }
        #map-section h3 {
            font-family: 'Cinzel', serif;
            font-size: 0.85rem;
            letter-spacing: 5px;
            text-transform: uppercase;
            color: rgba(255,255,255,0.35);
            margin-bottom: 22px;
        }
        .map-wrap {
            position: relative;
            display: inline-block;
            cursor: pointer;
        }
        .map-wrap iframe {
            display: block;
            width: min(680px, 90vw);
            height: 300px;
            border: 0;
            pointer-events: none;
            filter: grayscale(0.35) contrast(1.05);
        }
        .map-overlay { position: absolute; inset: 0; cursor: pointer; }

        /* ── BIG GOOUT BUTTON ── */
        .goout-big-wrap {
            background: #050403;
            text-align: center;
            padding: 50px 0 20px;
            position: relative;
            z-index: 2;
        }

        /* ── INNER NAV LANG ── */
        #inner-lang {
            display: flex;
            gap: 7px;
            font-size: 0.72rem;
            letter-spacing: 2px;
            font-weight: 500;
        }
        #inner-lang span {
            cursor: pointer;
            opacity: 0.35;
            transition: opacity 0.3s;
        }
        #inner-lang span:hover, #inner-lang span.active { opacity: 1; }
        #inner-lang .sep { cursor: default; opacity: 0.2 !important; }

        /* ── DOOR PAGE GoOut centered ── */
        .goout-door-wrap { text-align: center; margin-top: 30px; }

        @media (max-width: 600px) {
            #donate-poster { width: 130px; height: 130px; bottom: 14px; right: 14px; }
            #event-social { display: none; }
            #bottom-left-ctrl { bottom: 14px; left: 14px; }
        }
"""

patch('CSS: new styles',
    '    </style>\n\n    <!-- Three.js',
    NEW_CSS + '    </style>\n\n    <!-- Three.js'
)

# ─── 2. Door page: lang-switch → add CZE ─────────────────────────────────────
patch('lang-switch: add CZE',
    '''                    <div class="lang-switch">
                        <span class="active">🇺🇦 UKR</span>
                        <span style="opacity: 0.3;">|</span>
                        <span>🇬🇧 ENG</span>
                    </div>''',
    '''                    <div class="lang-switch" id="door-lang">
                        <span class="active">🇺🇦 UKR</span>
                        <span style="opacity: 0.3;">|</span>
                        <span>🇬🇧 ENG</span>
                        <span style="opacity: 0.3;">|</span>
                        <span>🇨🇿 CZE</span>
                    </div>'''
)

# ─── 3. Door hero: add eyebrow above h1 ──────────────────────────────────────
patch('door hero: eyebrow',
    '            <div class="hero-center">\n                <h1 class="main-title"',
    '''            <div class="hero-center">
                <span class="hero-eyebrow">Fundraising event by</span>
                <h1 class="main-title"'''
)

# ─── 4. Dive In → Зайти ──────────────────────────────────────────────────────
patch('button: Зайти',
    '<span class="paper-text font-grunge">Dive In</span>',
    '<span class="paper-text font-grunge">Зайти</span>'
)

# ─── 5. Remove scroll-indicator ──────────────────────────────────────────────
patch('scroll-indicator: remove',
    '''            <div class="scroll-indicator" aria-label="Scroll down">
                <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" width="18" height="18">
                    <line x1="12" y1="5" x2="12" y2="19"></line>
                    <polyline points="6 13 12 19 18 13"></polyline>
                </svg>
            </div>''',
    ''
)

# ─── 6. Scroll content: update text + center GoOut + add counter ─────────────
patch('scroll content: full update',
    '''        <div class="content-text">
            <!-- Описание ивента выровнено по левому краю без заголовков -->
            <p>
                Благотворительный 2-дневный ивент на Страговском стадионе (Прага).
            </p>
            <p>
                Два дня непрерывного рейва, экспериментальной музыки и визуального искусства от 6000ovecek и EVRO661. Все собранные средства будут направлены на благотворительную помощь.
            </p>
            <p>
                Для того чтобы увидеть полный лайнап артистов, расписание и детали локации — зайдите в сарай (кнопка <strong>"Dive In"</strong> выше).
            </p>

            <!-- Кнопка билетов -->
            <div class="btn-wrapper paper-strip" style="margin-top: 30px; transform: rotate(1deg);">
                <!-- TODO: Вставить актуальную ссылку на билеты -->
                <button class="enter-btn" onclick="window.open('https://goout.net/en/6k-and-evro661-spring-strahov4ukraine/sznyyiy/', '_blank', 'noopener')">
                    <div class="paper-bg torn-edges"></div>
                    <span class="paper-text font-grunge">GoOut Tickets</span>
                </button>
            </div>
        </div>''',
    '''        <div class="content-text">
            <p>
                Двохденний благодійний івент на стадіоні Страгов (Прага).
                8–9 травня 2026 — два дні безперервного рейву, експериментальної музики
                та візуального мистецтва від&nbsp;6000ovecek та EVRO661.
                Всі зібрані кошти підуть на виробництво FPV-дронів для України.
            </p>

            <!-- GoOut tickets — centred -->
            <div class="goout-door-wrap">
                <div class="btn-wrapper paper-strip" style="display:inline-block; transform: rotate(1deg);">
                    <button class="enter-btn" onclick="window.open(\'https://goout.net/en/6k-and-evro661-spring-strahov4ukraine/sznyyiy/\', \'_blank\', \'noopener\')">
                        <div class="paper-bg torn-edges"></div>
                        <span class="paper-text font-grunge">GoOut Tickets</span>
                    </button>
                </div>
            </div>

            <!-- Donation counter -->
            <div class="donation-counter">
                <div class="donation-label">Fundraising progress</div>
                <div class="donation-bar-wrap">
                    <div class="donation-bar-fill" id="donation-bar" style="width:0%"></div>
                </div>
                <div class="donation-amount">
                    <span id="donation-raised">€0</span>
                    <span class="goal"> of €10 000 goal</span>
                </div>
            </div>
        </div>'''
)

# ─── 7. Inside nav: replace arrow back-link with lang + make logo clickable ───
patch('inner-nav: logo clickable + lang',
    '''            <div class="inner-logo-wrap">
                <img class="inner-logo-img" src="" alt="EVRO661">
                <!-- Фотовспышка под лого. Срабатывает один раз когда юзер скроллит вниз с inside-hero -->
                <div class="photo-flash" id="photo-flash"></div>
            </div>
            <a href="#" class="back-link" onclick="location.reload(); return false;" aria-label="Back">
                <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" width="22" height="22">
                    <line x1="19" y1="12" x2="5" y2="12"></line>
                    <polyline points="12 19 5 12 12 5"></polyline>
                </svg>
            </a>''',
    '''            <div class="inner-logo-wrap" id="inner-logo-wrap" style="cursor:pointer;" title="Back to entrance">
                <img class="inner-logo-img" src="" alt="EVRO661">
                <div class="photo-flash" id="photo-flash"></div>
            </div>
            <div id="inner-lang">
                <span class="active">🇺🇦 UKR</span>
                <span class="sep">|</span>
                <span>🇬🇧 ENG</span>
                <span class="sep">|</span>
                <span>🇨🇿 CZE</span>
            </div>'''
)

# ─── 8. Inside section: add social icons + controls + video + map + GoOut ─────
patch('inside-section: add social, video, GoOut, map',
    '''        <!-- LINEUP SECTION -->
        <section id="lineup-section">
            <!-- Side panels (positioned absolute on desktop, fixed when active) -->
            <aside id="left-panel" class="side-panel side-panel-left" aria-hidden="true"></aside>
            <aside id="right-panel" class="side-panel side-panel-right" aria-hidden="true"></aside>

            <!-- Central column with paper strips + illustration -->
            <div class="lineup-column" id="lineup-column">
                <!-- Populated by JS from artists data -->
            </div>

            <!-- Date footer -->
            <div class="lineup-date">
                <h2 class="font-grunge">8.5 — 9.5.2026</h2>
                <p>Strahov / Praha</p>
            </div>
        </section>
    </section>''',
    '''        <!-- Social icons: left side, event page only -->
        <nav id="event-social" aria-label="Social links">
            <a class="ev-social-link" href="https://www.instagram.com/evro_661/" target="_blank" rel="noopener" aria-label="evro_661 on Instagram">
                <svg viewBox="0 0 24 24"><path d="M12 0C8.74 0 8.333.015 7.053.072 5.775.132 4.905.333 4.14.63c-.789.306-1.459.717-2.126 1.384S.935 3.35.63 4.14C.333 4.905.131 5.775.072 7.053.012 8.333 0 8.74 0 12s.015 3.667.072 4.947c.06 1.277.261 2.148.558 2.913.306.788.717 1.459 1.384 2.126.667.666 1.336 1.079 2.126 1.384.766.296 1.636.499 2.913.558C8.333 23.988 8.74 24 12 24s3.667-.015 4.947-.072c1.277-.06 2.148-.262 2.913-.558.788-.306 1.459-.718 2.126-1.384.666-.667 1.079-1.335 1.384-2.126.296-.765.499-1.636.558-2.913.06-1.28.072-1.687.072-4.947s-.015-3.667-.072-4.947c-.06-1.277-.262-2.149-.558-2.913-.306-.789-.718-1.459-1.384-2.126C21.319 1.347 20.651.935 19.86.63c-.765-.297-1.636-.499-2.913-.558C15.667.012 15.26 0 12 0zm0 2.16c3.203 0 3.585.016 4.85.071 1.17.055 1.805.249 2.227.415.562.217.96.477 1.382.896.419.42.679.819.896 1.381.164.422.36 1.057.413 2.227.057 1.266.07 1.646.07 4.85s-.015 3.585-.074 4.85c-.061 1.17-.256 1.805-.421 2.227-.224.562-.479.96-.899 1.382-.419.419-.824.679-1.38.896-.42.164-1.065.36-2.235.413-1.274.057-1.649.07-4.859.07-3.211 0-3.586-.015-4.859-.074-1.171-.061-1.816-.256-2.236-.421-.569-.224-.96-.479-1.379-.899-.421-.419-.69-.824-.9-1.38-.165-.42-.359-1.065-.42-2.235-.045-1.26-.061-1.649-.061-4.844 0-3.196.016-3.586.061-4.861.061-1.17.255-1.814.42-2.234.21-.57.479-.96.9-1.381.419-.419.81-.689 1.379-.898.42-.166 1.051-.361 2.221-.421 1.275-.045 1.65-.06 4.859-.06zm0 3.678c-3.405 0-6.162 2.76-6.162 6.162 0 3.405 2.76 6.162 6.162 6.162 3.405 0 6.162-2.76 6.162-6.162 0-3.405-2.76-6.162-6.162-6.162zM12 16c-2.21 0-4-1.79-4-4s1.79-4 4-4 4 1.79 4 4-1.79 4-4 4zm7.846-10.405c0 .795-.646 1.44-1.44 1.44-.795 0-1.44-.646-1.44-1.44 0-.794.646-1.439 1.44-1.439.793-.001 1.44.645 1.44 1.439z"/></svg>
                <span>@evro_661</span>
            </a>
            <a class="ev-social-link" href="https://www.instagram.com/sest_tisicu_ovecek/" target="_blank" rel="noopener" aria-label="sest_tisicu_ovecek on Instagram">
                <svg viewBox="0 0 24 24"><path d="M12 0C8.74 0 8.333.015 7.053.072 5.775.132 4.905.333 4.14.63c-.789.306-1.459.717-2.126 1.384S.935 3.35.63 4.14C.333 4.905.131 5.775.072 7.053.012 8.333 0 8.74 0 12s.015 3.667.072 4.947c.06 1.277.261 2.148.558 2.913.306.788.717 1.459 1.384 2.126.667.666 1.336 1.079 2.126 1.384.766.296 1.636.499 2.913.558C8.333 23.988 8.74 24 12 24s3.667-.015 4.947-.072c1.277-.06 2.148-.262 2.913-.558.788-.306 1.459-.718 2.126-1.384.666-.667 1.079-1.335 1.384-2.126.296-.765.499-1.636.558-2.913.06-1.28.072-1.687.072-4.947s-.015-3.667-.072-4.947c-.06-1.277-.262-2.149-.558-2.913-.306-.789-.718-1.459-1.384-2.126C21.319 1.347 20.651.935 19.86.63c-.765-.297-1.636-.499-2.913-.558C15.667.012 15.26 0 12 0zm0 2.16c3.203 0 3.585.016 4.85.071 1.17.055 1.805.249 2.227.415.562.217.96.477 1.382.896.419.42.679.819.896 1.381.164.422.36 1.057.413 2.227.057 1.266.07 1.646.07 4.85s-.015 3.585-.074 4.85c-.061 1.17-.256 1.805-.421 2.227-.224.562-.479.96-.899 1.382-.419.419-.824.679-1.38.896-.42.164-1.065.36-2.235.413-1.274.057-1.649.07-4.859.07-3.211 0-3.586-.015-4.859-.074-1.171-.061-1.816-.256-2.236-.421-.569-.224-.96-.479-1.379-.899-.421-.419-.69-.824-.9-1.38-.165-.42-.359-1.065-.42-2.235-.045-1.26-.061-1.649-.061-4.844 0-3.196.016-3.586.061-4.861.061-1.17.255-1.814.42-2.234.21-.57.479-.96.9-1.381.419-.419.81-.689 1.379-.898.42-.166 1.051-.361 2.221-.421 1.275-.045 1.65-.06 4.859-.06zm0 3.678c-3.405 0-6.162 2.76-6.162 6.162 0 3.405 2.76 6.162 6.162 6.162 3.405 0 6.162-2.76 6.162-6.162 0-3.405-2.76-6.162-6.162-6.162zM12 16c-2.21 0-4-1.79-4-4s1.79-4 4-4 4 1.79 4 4-1.79 4-4 4zm7.846-10.405c0 .795-.646 1.44-1.44 1.44-.795 0-1.44-.646-1.44-1.44 0-.794.646-1.439 1.44-1.439.793-.001 1.44.645 1.44 1.439z"/></svg>
                <span>@6000ovecek</span>
            </a>
        </nav>

        <!-- Bottom-left controls: game + sound (event page only) -->
        <div id="bottom-left-ctrl">
            <button class="ctrl-btn" id="btn-sound" title="Toggle sound" aria-label="Toggle sound">🔇</button>
        </div>

        <!-- LINEUP SECTION -->
        <section id="lineup-section">
            <!-- Background video -->
            <video id="lineup-video-bg" src="footbolchik.mp4" autoplay loop muted playsinline></video>

            <!-- Side panels -->
            <aside id="left-panel" class="side-panel side-panel-left" aria-hidden="true"></aside>
            <aside id="right-panel" class="side-panel side-panel-right" aria-hidden="true"></aside>

            <!-- Central column with paper strips + illustration -->
            <div class="lineup-column" id="lineup-column">
                <!-- Populated by JS from artists data -->
            </div>

            <!-- Date footer -->
            <div class="lineup-date">
                <h2 class="font-grunge">8.5 — 9.5.2026</h2>
                <p>Strahov / Praha</p>
            </div>
        </section>

        <!-- Big GoOut button -->
        <div class="goout-big-wrap">
            <div class="btn-wrapper paper-strip" style="display:inline-block; transform: rotate(-1.2deg);">
                <button class="enter-btn" onclick="window.open(\'https://goout.net/en/6k-and-evro661-spring-strahov4ukraine/sznyyiy/\', \'_blank\', \'noopener\')">
                    <div class="paper-bg torn-edges"></div>
                    <span class="paper-text font-grunge" style="font-size:1.4rem; padding:14px 44px;">GoOut Tickets</span>
                </button>
            </div>
        </div>

        <!-- Map section -->
        <div id="map-section">
            <h3>Strahov / Praha</h3>
            <div class="map-wrap" onclick="window.open(\'https://www.google.com/maps/place/Strahov+Stadium,+Prague\', \'_blank\', \'noopener\')" title="Open in Google Maps">
                <iframe
                    src="https://maps.google.com/maps?q=50.0810,14.3897&z=15&output=embed"
                    allowfullscreen
                    loading="lazy"
                    referrerpolicy="no-referrer-when-downgrade">
                </iframe>
                <div class="map-overlay"></div>
            </div>
        </div>

    </section>'''
)

# ─── 9. Persistent elements (before </body>) ──────────────────────────────────
PERSISTENT_HTML = '''
    <!-- Donate poster (sticky bottom-right, always visible) -->
    <a id="donate-poster" href="#" target="_blank" rel="noopener" title="Donate for Ukraine" aria-label="Donate">
        <div class="donate-inner" id="donate-inner">
            <div class="donate-flag"><div class="donate-flag-top"></div><div class="donate-flag-bot"></div></div>
            <div class="donate-line sm">Fundraiser</div>
            <div class="donate-line">For</div>
            <div class="donate-line">Ukraine</div>
            <div class="donate-cta">Donate</div>
        </div>
    </a>

    <!-- Music player (popup from bottom) -->
    <div id="music-player" role="complementary" aria-label="Music player">
        <span id="mp-name">—</span>
        <audio id="mp-audio" src=""></audio>
        <button id="mp-play" aria-label="Play/Pause">▶</button>
        <button id="mp-close" aria-label="Close">✕</button>
    </div>
'''

patch('persistent HTML: donate + music player',
    '</body>',
    PERSISTENT_HTML + '</body>'
)

# ─── 10. Replace artists data (minimal → full with imgs/vids/bio) ─────────────
ARTISTS_DATA = r"""        const artists = [
            // ── Block 1 ──────────────────────────────────────────────────────
            { id:1, block:1, slug:'coinman46', name:'COINMAN46',
              bio: null,
              imgs:['artists-data/coinman46/photo-1.png'],
              vids:['artists-data/coinman46/video.mp4'] },
            { id:2, block:1, slug:'dj-godbless-b2b-dj-bubble-wuffle', name:'DJ GODBLESS B2B DJ BUBBLE WUFFLE',
              bio:'Join in the destruction. Join @evro_661.\n\nResearchers in the Institute of unfinished studies states that 8 of 10.',
              imgs:['artists-data/dj-godbless-b2b-dj-bubble-wuffle/photo-1.png'],
              vids:['artists-data/dj-godbless-b2b-dj-bubble-wuffle/video.mov'] },
            { id:3, block:1, slug:'vikusia', name:'VIKUSIA',
              bio:'Vikusia is just a girl from Ukraine who came to Prague in 2022 to study at the Academy of Fine Arts (AVU). Using a variety of acoustic and electronic instruments, she blends delicate melodies with electronic soundscapes. Her music contrasts gentle harmonies with expressive poetry filled with reflections on the modern world. Her sound moves between contemporary classical music and ambient.',
              imgs:['artists-data/vikusia/photo-1.jpeg'],
              vids:['artists-data/vikusia/video.mp4'] },
            { id:4, block:1, slug:'terror-phoenix', name:'TERROR PHOENIX',
              bio: null,
              imgs:['artists-data/terror-phoenix/photo-1.PNG'],
              vids:['artists-data/terror-phoenix/video.MOV'] },
            { id:5, block:1, slug:'svaz', name:'SVAZ',
              bio: null,
              imgs:['artists-data/svaz/photo-1.jpg'],
              vids:['artists-data/svaz/video.mov'] },
            { id:6, block:1, slug:'spiral-sadness', name:'SPIRAL SADNESS',
              bio:'Definicí Spiral Sadness je alternativní hip-hop, emotivní rap, vlastní beaty a šum analogu. Jeho principem je DIY. Tvoří také jádro Spiral-Sadness-Video-Corporation zaměřené na tvorbu hudebních videoklipů.',
              imgs:['artists-data/spiral-sadness/photo-1.JPG','artists-data/spiral-sadness/photo-2.JPG'],
              vids: null },
            { id:7, block:1, slug:'seilor-moon', name:'SEILOR MOON',
              bio:'Seilor Moon can deliver any genre from Brazilian funk to Trap remixes to Hardcore, Gabber and even Frenchcore and Uptempo — the harder the better.',
              imgs:['artists-data/seilor-moon/photo-1.jpg'],
              vids: null },
            { id:8, block:1, slug:'rewounded', name:'REWOUNDED',
              bio:'A myth or a fraud? Polish lousy noisé rock group, solving mysteries since 2020. Following the release of their debut album "Fingers Crossed" via Almost Records inc in 2025, they still struggle to quit music. Still not American.',
              imgs:['artists-data/rewounded/photo-1.jpg'],
              vids:['artists-data/rewounded/video.MOV'] },
            { id:9, block:1, slug:'pock-root', name:'POCK ROOT',
              bio:'Bringing a combination of post-club and hardcore sound, not really bound by genres.',
              imgs:['artists-data/pock-root/photo-1.jpg'],
              vids:['artists-data/pock-root/video.mov'] },
            // ── Block 2 ──────────────────────────────────────────────────────
            { id:10, block:2, slug:'angst', name:'ANGST',
              bio: null,
              imgs:['artists-data/angst/photo-1.jpeg'],
              vids:['artists-data/angst/video.mov'] },
            { id:11, block:2, slug:'autocannibal', name:'AUTOCANNIBAL',
              bio:'Berlin based producer/performer originally from Bakhmut, Ukraine. Label Dissontiya and band Subflowers. Expect electro/breakbeat with a bit of MC\'ing.',
              imgs:['artists-data/autocannibal/photo-1.JPG'],
              vids:['artists-data/autocannibal/video.MOV'] },
            { id:12, block:2, slug:'bols-slob', name:'BOLS/SLOB',
              bio:'BoLs/sLoB is a producer, songwriter and DJ. His authentic mix of cloud rap, glitch, ethereal EDM, and experimental electronic music makes sLoB one of the most talented up-and-coming artists from the Czech Republic.',
              imgs:['artists-data/bols-slob/photo-1.jpg','artists-data/bols-slob/photo-2.jpg'],
              vids: null },
            { id:13, block:2, slug:'chloe-landau', name:'CHLOE LANDAU',
              bio:'Chloe Landau is a Ukrainian singer from the underground music scene. Her work blends light pop melodies with themes of war, codependent relationships, and death. In February 2026, Chloe released her debut album Dreamhouse on Standard Deviation.',
              imgs:['artists-data/chloe-landau/photo-1.jpg'],
              vids:['artists-data/chloe-landau/video.mov'] },
            { id:14, block:2, slug:'crc', name:'CRC',
              bio:'Constantly falling.',
              imgs:['artists-data/crc/photo-1.jpg'],
              vids: null },
            { id:15, block:2, slug:'eizola', name:'EIZOLA',
              bio:'Eizola\'s ambient compositions are inspired by dusty weather transmitters and life in pits occupied by little critters. Samples made of field recordings, slowly shifting layers, fading rhythm, and the vibrations of overheating perma-soil.',
              imgs: null,
              vids:['artists-data/eizola/video-1.mov','artists-data/eizola/video-2.MOV'] },
            { id:16, block:2, slug:'dj-scheusaal', name:'DJ SCHEUSAAL',
              bio:'DJ Scheusaal is a Firearms Dealer and DJ from Vienna, Austria. He loves exploring underground music scenes all across Europe. Expect the unexpected.',
              imgs:['artists-data/dj-scheusaal/photo-1.jpg'],
              vids:['artists-data/dj-scheusaal/video.mp4'] },
            // ── Block 3 ──────────────────────────────────────────────────────
            { id:17, block:3, slug:'eternity-again', name:'ETERNITY AGAIN',
              bio: null,
              imgs:['artists-data/eternity-again/photo-1.jpeg'],
              vids:['artists-data/eternity-again/video.mov'] },
            { id:18, block:3, slug:'keiko-sei', name:'KEIKO SEI',
              bio: null, imgs: null, vids: null },
            { id:19, block:3, slug:'lila-tesla', name:'LILA TESLA',
              bio:'LilaTesla is a sonic alchemist, blending shards of clubs and dancefloors together with glittering glitches and audio glam.',
              imgs:['artists-data/lila-tesla/photo-1.jpg'],
              vids:['artists-data/lila-tesla/video.MOV'] },
            { id:20, block:3, slug:'neue-welt', name:'NEUE WELT',
              bio:'Sweeter and More Ecstatic. Alt-rock / Art-rock / Hard-rock from Prague.',
              imgs:['artists-data/neue-welt/photo-1.jpg'],
              vids: null },
            { id:21, block:3, slug:'passive-progressive', name:'PASSIVE PROGRESSIVE',
              bio: null,
              imgs:['artists-data/passive-progressive/photo-1.JPG'],
              vids:['artists-data/passive-progressive/video.mp4'] },
            { id:22, block:3, slug:'plandora-pearl', name:'PLANDORA PEARL',
              bio:'Plandora Pearl works with emotions, genres and feelings, operating deconstructed melodies with epic sound design and pop-like melodies.',
              imgs:['artists-data/plandora-pearl/photo-1.jpg'],
              vids:['artists-data/plandora-pearl/video.mov'] },
            { id:23, block:3, slug:'wasted-days', name:'WASTED DAYS',
              bio: null,
              imgs:['artists-data/wasted-days/photo-1.JPEG'],
              vids:['artists-data/wasted-days/video.mov'] },
        ];"""

OLD_ARTISTS = r"""        const artists = [
            // Block 1
            { id: 1,  block: 1, slug: 'coinman46',                       name: 'COINMAN46' },
            { id: 2,  block: 1, slug: 'dj-godbless-b2b-dj-bubble-wuffle', name: 'DJ GODBLESS B2B DJ BUBBLE WUFFLE' },
            { id: 3,  block: 1, slug: 'vikusia',                          name: 'VIKUSIA' },
            { id: 4,  block: 1, slug: 'terror-phoenix',                   name: 'TERROR PHOENIX' },
            { id: 5,  block: 1, slug: 'svaz',                             name: 'SVAZ' },
            { id: 6,  block: 1, slug: 'spiral-sadness',                   name: 'SPIRAL SADNESS' },
            { id: 7,  block: 1, slug: 'seilor-moon',                      name: 'SEILOR MOON' },
            { id: 8,  block: 1, slug: 'rewounded',                        name: 'REWOUNDED' },
            { id: 9,  block: 1, slug: 'pock-root',                        name: 'POCK ROOT' },
            // Block 2
            { id: 10, block: 2, slug: 'angst',                            name: 'ANGST' },
            { id: 11, block: 2, slug: 'autocannibal',                     name: 'AUTOCANNIBAL' },
            { id: 12, block: 2, slug: 'bols-slob',                        name: 'BOLS/SLOB' },
            { id: 13, block: 2, slug: 'chloe-landau',                     name: 'CHLOE LANDAU' },
            { id: 14, block: 2, slug: 'crc',                              name: 'CRC' },
            { id: 15, block: 2, slug: 'eizola',                           name: 'EIZOLA' },
            { id: 16, block: 2, slug: 'dj-scheusaal',                     name: 'DJ SCHEUSAAL' },
            // Block 3
            { id: 17, block: 3, slug: 'eternity-again',                   name: 'ETERNITY AGAIN' },
            { id: 18, block: 3, slug: 'keiko-sei',                        name: 'KEIKO SEI' },
            { id: 19, block: 3, slug: 'lila-tesla',                       name: 'LILA TESLA' },
            { id: 20, block: 3, slug: 'neue-welt',                        name: 'NEUE WELT' },
            { id: 21, block: 3, slug: 'passive-progressive',              name: 'PASSIVE PROGRESSIVE' },
            { id: 22, block: 3, slug: 'plandora-pearl',                   name: 'PLANDORA PEARL' },
            { id: 23, block: 3, slug: 'wasted-days',                      name: 'WASTED DAYS' },
        ];"""

patch('artists data: full replacement', OLD_ARTISTS, ARTISTS_DATA)

# ─── 11. Fix renderPanels: show real bio text ─────────────────────────────────
patch('renderPanels: show bio',
    '''            leftPanel.innerHTML = `
                ${imgsHtml || '<p class="panel-missing">фотки будут позже</p>'}
                <div class="panel-text">
                    <strong>${a.name} — info</strong>
                    Здесь будет инфа текстом из файлов которые артист про себя написал.
                </div>
            `;''',
    '''            leftPanel.innerHTML = `
                ${imgsHtml || '<p class="panel-missing">фото скоро</p>'}
                <div class="panel-text">
                    <strong>${a.name}</strong>
                    ${a.bio ? a.bio.replace(/\\n/g, '<br>') : ''}
                </div>
            `;'''
)

patch('renderPanels: show bio in right panel',
    '                <p class="panel-text">${a.bio}</p>',
    '                ${a.bio ? `<p class="panel-text">${a.bio.replace(/\\n/g, \'<br>\')}</p>` : \'\'}'
)

# ─── 12. Big logo morph left-up on scroll ────────────────────────────────────
patch('onInsideScroll: logo morph',
    '''            if (bigLogo) {
                bigLogo.style.opacity = String(1 - fadeProgress);
                bigLogo.style.transform = `scale(${1 - fadeProgress * 0.08})`;
            }''',
    '''            if (bigLogo) {
                const s = 1 - fadeProgress * 0.62;
                const tx = -fadeProgress * 38;
                const ty = -fadeProgress * 36;
                bigLogo.style.opacity = String(Math.max(0, 1 - fadeProgress * 1.4));
                bigLogo.style.transform = `translate(${tx}vw, ${ty}vh) scale(${s})`;
                bigLogo.style.transformOrigin = 'top left';
            }'''
)

# ─── 13. New JS features (before closing </script>) ───────────────────────────
NEW_JS = r"""
        // ── Logo click → back to door ─────────────────────────────────────────
        const innerLogoWrap = document.getElementById('inner-logo-wrap');
        if (innerLogoWrap) {
            innerLogoWrap.addEventListener('click', () => {
                const insideSection = document.getElementById('inside-section');
                const heroWrap = document.getElementById('hero-wrap');
                const scrollContent = document.getElementById('hero-scroll-content');
                const flash = document.getElementById('white-flash');

                flash.style.transition = 'opacity 0.3s ease-in-out';
                flash.style.opacity = '1';
                setTimeout(() => {
                    insideSection.style.display = 'none';
                    document.getElementById('inner-nav').classList.remove('visible');
                    document.getElementById('event-social').classList.remove('visible');
                    document.getElementById('bottom-left-ctrl').classList.remove('visible');
                    heroWrap.style.display = '';
                    scrollContent.style.display = '';
                    renderingActive = true;
                    isDiving = false;
                    targetAngleLeft = 0;
                    targetAngleRight = 0;
                    targetVoidLight = 8;
                    targetCameraZ = 14;
                    targetBloom = 1.4;
                    voidLight.color.setHex(0xffddaa);
                    document.getElementById('hero-ui').style.opacity = '1';
                    document.getElementById('hero-ui').style.transition = 'none';
                    window.scrollTo(0, 0);
                    animate();
                    setTimeout(() => {
                        flash.style.transition = 'opacity 0.6s ease-in-out';
                        flash.style.opacity = '0';
                    }, 100);
                }, 350);
            });
        }

        // ── Inner lang switcher ───────────────────────────────────────────────
        document.querySelectorAll('#inner-lang span:not(.sep)').forEach(el => {
            el.addEventListener('click', () => {
                document.querySelectorAll('#inner-lang span:not(.sep)').forEach(s => s.classList.remove('active'));
                el.classList.add('active');
                // sync door lang
                const txt = el.textContent.trim();
                document.querySelectorAll('#door-lang span').forEach(s => {
                    s.classList.toggle('active', s.textContent.trim() === txt);
                });
            });
        });

        // ── Event-page show controls when inside ─────────────────────────────
        const origShowInside = () => {
            document.getElementById('event-social').classList.add('visible');
            document.getElementById('bottom-left-ctrl').classList.add('visible');
        };

        // Patch the enter button to also show social/controls
        const origEnterClick = enterBtn._clickHandler;
        enterBtn.addEventListener('click', () => {
            setTimeout(origShowInside, 2800);
        });

        // ── Donation counter animation ────────────────────────────────────────
        (function initDonation() {
            const bar = document.getElementById('donation-bar');
            const raised = document.getElementById('donation-raised');
            if (!bar || !raised) return;
            let current = 2143;
            const goal = 10000;
            const pct = (current / goal * 100).toFixed(1);
            bar.style.width = pct + '%';
            raised.textContent = '€' + current.toLocaleString('de-DE');

            // slow random tick: +1..8 EUR every 4-12 seconds
            function tick() {
                const add = Math.floor(Math.random() * 8) + 1;
                current += add;
                const p = Math.min(100, current / goal * 100);
                bar.style.width = p.toFixed(1) + '%';
                raised.textContent = '€' + current.toLocaleString('de-DE');
                setTimeout(tick, 4000 + Math.random() * 8000);
            }
            setTimeout(tick, 5000);
        })();

        // ── Donate poster: 3D tilt ────────────────────────────────────────────
        (function initDonate() {
            const poster = document.getElementById('donate-poster');
            const inner = document.getElementById('donate-inner');
            if (!poster || !inner) return;
            poster.addEventListener('mousemove', (e) => {
                const r = poster.getBoundingClientRect();
                const cx = r.left + r.width / 2;
                const cy = r.top + r.height / 2;
                const rx = ((e.clientY - cy) / (r.height / 2)) * -14;
                const ry = ((e.clientX - cx) / (r.width / 2)) * 14;
                inner.style.transform = `rotateX(${rx}deg) rotateY(${ry}deg)`;
            });
            poster.addEventListener('mouseleave', () => {
                inner.style.transform = 'rotateX(0) rotateY(0)';
            });
        })();

        // ── Music player ──────────────────────────────────────────────────────
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
        })();

        // ── Sound toggle (ambient) ────────────────────────────────────────────
        (function initSoundToggle() {
            const btn = document.getElementById('btn-sound');
            const vid = document.getElementById('lineup-video-bg');
            if (!btn) return;
            let muted = true;
            btn.addEventListener('click', () => {
                muted = !muted;
                if (vid) vid.muted = muted;
                btn.textContent = muted ? '🔇' : '🔊';
            });
        })();
"""

patch('new JS features',
    '        window.addEventListener(\'scroll\', onInsideScroll, { passive: true });\n    </script>',
    '        window.addEventListener(\'scroll\', onInsideScroll, { passive: true });\n' + NEW_JS + '    </script>'
)

# ─── Write output ─────────────────────────────────────────────────────────────
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print(f'\n✅  Done — {len(applied)} patches applied:')
for p in applied:
    print(f'   • {p}')
