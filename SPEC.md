# evro661 × 6000ovecek — задание для Claude Code

> Лежит как `SPEC.md` в корне репо. Это финальное ТЗ на сборку лендинга.

---

## 0. Что уже лежит в репо

Разрозненные куски, которые надо собрать в один сайт:

| Файл | Что это |
|---|---|
| `Appmain.jsx` | Двери сарая + переход на event page. Three.js + inline `<style>`. **Заглушки:** `THE VOID`, `Works/Studio/Contact` — заменить. |
| `AppLineup.jsx` | Лайнап с боковыми панелями. **Имена кривые** (`GOINMAN`, `PLANDONA`, `LILATESLA`) — игнорировать, брать из `artists.js`. |
| `AppFundraiser.jsx` | Постер «Fundraiser For Ukraine» с 3D-tilt, hover-флагом и DONATE. Использовать как sticky badge в углу. |
| `Appfootball.jsx` | Игра с мячом. **HTML, не JSX** — портировать в React. Заменить нарисованный мяч на `ball.png`. |
| `artists.js` | **Источник правды** для имён артистов. |
| `artists-data/` | Папки с реальными ассетами после ручного переименования. **Содержимое неизвестно — проанализировать**. |
| `footbolchik.mp4` | Фоновое видео для event page. |
| `logo-ovecki-evro.png` | Большой рукописный логотип. |
| `logoevro661.png` | Маленький лого evro661 (зелёный). |
| `characters.png` | Иллюстрация для лайнапа. |
| `ball.png` | Мяч для игры. |
| `index.html` (если есть от Claude) | Self-contained прототип со всем уже состыкованным — живой пример. |

---

## 1. Первая задача: проанализировать `artists-data/` и переписать `artists.js`

В `artists.js` сейчас захардкожены пути типа `artists-data/{slug}/photo-1.jpg` — но **реальное содержимое папок неизвестно**: у кого-то 1 фотка, у кого-то 3, форматы разные (jpg/png), видео может быть `.mov`, `.mp4` или отсутствовать, у кого-то bio есть, у кого-то нет.

**Действие:**

1. Написать скрипт `scripts/build-artists-data.mjs` который:
   - Проходит по `artists-data/`, для каждой папки-артиста собирает что реально есть
   - Распознаёт фотки по расширениям (`jpg|jpeg|png|webp`), сортирует по имени
   - Распознаёт видео (`mov|mp4|webm`), сортирует по имени
   - Читает `bio.md` если есть, кладёт содержимое в `bio`
2. Сгенерировать новый `src/data/artists.js` с массивами `imgs: [...]` и `vids: [...]` (как в `AppLineup.jsx`-моке, не singular как в текущем `artists.js`)
3. Если у артиста нет фоток — `imgs: []`, нет видео — `vids: []`, нет био — `bio: null`
4. **TODO-репорт** в конце скрипта: список slugs у которых чего-то не хватает

**Структура итогового `artists.js`:**

```js
export const artists = [
  {
    id: 1,
    block: 1,
    slug: 'coinman46',
    name: 'COINMAN46',
    bio: 'текст из bio.md или null',
    imgs: [
      '/artists-data/coinman46/photo-1.png',
      '/artists-data/coinman46/photo-2.jpg',
    ],
    vids: ['/artists-data/coinman46/video.mp4'],
    track: null, // SoundCloud iframe URL — TBD позже
  },
  // ... 22 more
];
```

**⚠️ Большие файлы:**
- Видео > 20MB — TODO «нужна компрессия»
- Фото > 3MB — то же самое
- Команды для компрессии в `scripts/optimize-media.sh` (ffmpeg для видео, sharp/imagemagick для фото)

---

## 2. Структура итогового приложения

Стек: **Vite + React + Tailwind** (как в твоём portfolio repo, чтобы DX совпадал).

```
src/
  App.jsx                  ← роутинг: door / event (один useState)
  data/
    artists.js             ← сгенерированный из артефактов
  components/
    DoorPage.jsx           ← из Appmain.jsx, c доработками
    EventPage.jsx          ← композит всего что после дверей
    Lineup.jsx             ← из AppLineup.jsx
    DonatePoster.jsx       ← из AppFundraiser.jsx, sticky версия
    GameOverlay.jsx        ← из Appfootball.jsx, портированный в React
    MusicPlayer.jsx        ← новый, простой
    MapSection.jsx         ← новый, Google Maps embed
    DonationCounter.jsx    ← новый, прогресс-бар
    GlobalNav.jsx          ← persistent: лого + lang switcher
    EventSocials.jsx       ← вертикальный столбик ig-иконок (только event page)
    EventControls.jsx      ← bottom-left: game toggle + sound toggle
  hooks/
    usePageTransition.js   ← логика door → event перехода
public/
  logo-ovecki-evro.png
  logoevro661.png
  characters.png
  ball.png
  footbolchik.mp4
  artists-data/
    {slug}/...
scripts/
  build-artists-data.mjs   ← одноразовый: пересобирает src/data/artists.js
  optimize-media.sh        ← по необходимости
```

### Routing
React Router НЕ нужен. SPA с двумя состояниями (door/event) через один `useState` в `App.jsx`. Клик «Зайти» / клик на маленький лого в шапке — переключают.

---

## 3. DOOR PAGE — `DoorPage.jsx`

Базируется на `Appmain.jsx`. Изменения:

### Hero (по центру)

```
[FUNDRAISING EVENT BY]              ← мелкий tracking-wide eyebrow
[ logo-ovecki-evro.png — большой ]  ← mix-blend-mode: screen
[ описание ивента 1-2 строки ]
[ Зайти ]                            ← paper-strip кнопка ПО ЦЕНТРУ
```

**Eyebrow:** `FUNDRAISING EVENT BY` (ENG) / `БЛАГОДІЙНА ПОДІЯ` (UKR) / `BENEFIČNÍ AKCE` (CZE)

**Описание (примерно):**
> Двухдневный благотворительный концерт солидарности с Украиной. 8–9 мая 2026, Прага. Все средства идут на производство FPV-дронов.

### Что убрать

- ❌ `Scroll to explore` внизу — убрать
- ❌ Стрелка top-right — убрать (её роль играет клик на лого)
- ❌ `Works / Studio / Contact` — заменить на lang switcher (он persistent)
- ❌ Логотип-текст `THE VOID` — заменить на `<img src="/logoevro661.png">`

### Scroll content под дверями

Если юзер не клик «Зайти», а скроллит — показать:

1. Полное описание ивента (даты, локация, цель, организаторы с @-ссылками)
2. **GoOut Tickets** кнопка **по центру** (paper-strip): `https://goout.net/en/6k-and-evro661-spring-strahov4ukraine/sznyyiy/`
3. **Donation counter:** прогресс-бар + текст. Хардкод `€2,143 / €10,000` пока (TODO: backend).

### Стены сарая
В `Appmain.jsx` уже правильные: `BoxGeometry(10, 10, 1)` для боков. **Не трогать**.

---

## 4. EVENT PAGE — `EventPage.jsx`

После открытия дверей. Композит из:

### 4.1. Inside hero (первый экран после входа)
- `logo-ovecki-evro.png` на весь viewport, по центру
- Под ним стрелка вниз (одна простая SVG)
- При скролле — большое лого **уходит влево-вверх и уменьшается** до маленькой версии в районе persistent nav (через `transform: translate() scale()` по scroll progress 0→1)
- В момент когда большое лого начинает уходить — **под `logoevro661.png` в шапке срабатывает фотовспышка** (один раз).

**CSS вспышки** (если ещё не написан, можно взять из моего прототипа):
```css
@keyframes photoFlash {
  0%   { opacity: 0;    transform: translate(-50%,-50%) scale(0.3);  filter: blur(0); }
  8%   { opacity: 1;    transform: translate(-50%,-50%) scale(1.4);  filter: blur(0); }
  18%  { opacity: 0.9;  transform: translate(-50%,-50%) scale(1.6);  filter: blur(1px); }
  45%  { opacity: 0.35; transform: translate(-50%,-50%) scale(2.2);  filter: blur(4px); }
  100% { opacity: 0;    transform: translate(-50%,-50%) scale(2.8);  filter: blur(8px); }
}
```
Триггер один раз на `scroll > 25%`, сбрасывается если scroll back to top.

### 4.2. Лайнап (`Lineup.jsx`)
Из `AppLineup.jsx`. Изменения:
- **Имена** — из `artists.js` (`GOINMAN` → `COINMAN46`, `PLANDONA` → `PLANDORA PEARL`, `LILATESLA` → `LILA TESLA`, и т.д.)
- **Boundaries** между блоками 1/2/3 — визуальные паузы (бОльший gap, либо тонкий divider)
- **Иллюстрация в центре** — `characters.png` после блока 1 (после ~9 артистов), `mix-blend-mode: screen`
- Side panels работают как в моке: hover → preview, click → lock, click outside → unlock
- Если у артиста `imgs.length === 0` — left panel показывает «фотки скоро будут», аналогично для видео и био
- Mobile (< 900px) — side panels скрыть, био показывать tooltip-ом под полоской

### 4.3. Background video
`footbolchik.mp4` — `<video autoplay loop muted playsinline>` за лайнапом, `opacity: 0.4`.

### 4.4. Music player (`MusicPlayer.jsx`)
- Появляется снизу при клике на артиста (если у него есть `track`)
- Простейший: имя артиста, ▶/⏸, ✕ (close), `<audio>` или iframe SoundCloud
- Закрывается крестиком, при клике на следующего артиста переключается
- Поле `track` в `artists.js` пока null — TODO коммент

### 4.5. Bottom-left controls (`EventControls.jsx`)
- ⚽ кнопка → toggle игры (overlay on/off)
- 🔇/🔊 → toggle ambient sound сайта (можно завязать на текущий music player)

### 4.6. Game (`GameOverlay.jsx`)
Портировать `Appfootball.jsx` (HTML) → React компонент. Изменения:
- Вместо `punkCircle()` рисования — `<img src="/ball.png">` через `ctx.drawImage()` (preload image, потом drawImage с rotation/translation)
- Toggle через ⚽ кнопку из EventControls
- Сохранить логику `pointer-events: none` на canvas + window listeners на kick — это умно сделано

### 4.7. Под лайнапом
- **Большая GoOut Tickets кнопка** по центру (paper-strip, заметная)
- **Map section** — Google Maps iframe со Страговским стадионом
  - Координаты: `50.0810, 14.3897`
  - Клик на карту → открыть `https://maps.google.com/?q=Strahov+Stadium+Praha` в новой вкладке
  - Иконка карты в шапке (если будет) — прячется когда юзер на map section (Intersection Observer)

---

## 5. Persistent UI (на обеих страницах)

### `GlobalNav.jsx`
```
[ logo top-left ]                        [ 🇺🇦 / 🇬🇧 / 🇨🇿 top-right ]
```

- Логотип `logoevro661.png` — на event page click → возврат на DoorPage. На door page click → noop (или scroll to top).
- **Lang switcher** — 3 языка: украинский, английский, чешский. Подсветка активного. Реальная локализация через `react-i18next` (или просто `useState` для preview, чтобы не блокироваться).

### `<DonatePoster />` (sticky bottom-right)
Из `AppFundraiser.jsx`. Sticky, не модал. Размер ~280×280px (в оригинале full-screen, нужно уменьшить через wrapper). Wrapper это `<a href={DONATE_URL}>` (ссылка пока placeholder).

### `<EventSocials />` (только event page, top-left под лого)
Вертикально, иконка слева + подпись справа от иконки:
```
[ig icon]  evro661 instagram
[ig icon]  ovecek instagram
```
- `evro_661` → `https://www.instagram.com/evro_661/`
- `sest_tisicu_ovecek` → `https://www.instagram.com/sest_tisicu_ovecek/`
- ❌ **SoundCloud — убрать совсем со всех страниц**
- (опционально третья) `resistancesupportclub` → `https://www.instagram.com/resistancesupportclub/`

---

## 6. Favicon

Сгенерировать из `logoevro661.png`:
- `favicon.ico` (16×16, 32×32)
- `favicon-32x32.png`
- `favicon-16x16.png`
- `apple-touch-icon.png` (180×180)
- `android-chrome-192x192.png`
- `android-chrome-512x512.png`

Подключение в `index.html`:
```html
<link rel="icon" type="image/png" sizes="32x32" href="/favicon-32x32.png">
<link rel="icon" type="image/png" sizes="16x16" href="/favicon-16x16.png">
<link rel="apple-touch-icon" sizes="180x180" href="/apple-touch-icon.png">
```

Для генерации — `sharp` (npm) или онлайн `realfavicongenerator.net`.

---

## 7. Шрифты и стили (общие)

Глобально, в `index.html` или CSS `@import`:
- `Rock Salt` (рукописные полоски)
- `Cinzel` (заголовки)
- `Montserrat` (body)
- `Anton` (donate poster)

SVG `torn-edges-filter` — глобальный, в корневом компоненте, чтобы все полоски использовали:
```html
<svg width="0" height="0" style="position:absolute">
  <defs>
    <filter id="torn-edges-filter" x="-2%" y="-5%" width="104%" height="110%">
      <feTurbulence type="fractalNoise" baseFrequency="0.04 0.1" numOctaves="3" result="noise" />
      <feDisplacementMap in="SourceGraphic" in2="noise" scale="3" xChannelSelector="R" yChannelSelector="G" />
    </filter>
  </defs>
</svg>
```

---

## 8. Ссылки (источник правды)

| Что | Куда |
|---|---|
| Tickets | https://goout.net/en/6k-and-evro661-spring-strahov4ukraine/sznyyiy/ |
| Instagram evro661 | https://www.instagram.com/evro_661/ |
| Instagram 6000 ovecek | https://www.instagram.com/sest_tisicu_ovecek/ |
| Instagram resistance | https://www.instagram.com/resistancesupportclub/ |
| Donate (TBD) | placeholder, потом реальная платформа |
| Map | https://maps.google.com/?q=Strahov+Stadium+Praha |

---

## 9. Порядок работы для Claude Code

1. **Анализ `artists-data/`** — написать `scripts/build-artists-data.mjs`, запустить, сгенерировать `src/data/artists.js` + report missing materials в консоль
2. **Положить ассеты** в `public/` (логотипы, characters, ball, footbolchik, artists-data)
3. **Сгенерировать favicon**, подключить в `index.html`
4. **Накатить шрифты + torn-edges SVG** глобально в `App.jsx`
5. **Собрать `DoorPage`** из `Appmain.jsx` со всеми правками
6. **Собрать persistent layer** (GlobalNav, DonatePoster)
7. **Собрать `EventPage`** + Lineup + side panels
8. **Music player + Game + EventControls** (последний слой)
9. **Map section + Donation counter**
10. **Полировать переход** door → event (white flash, photo flash, лого-морф)
11. **Тестировать на мобиле** — все sticky-элементы (donate poster, controls) не должны перекрывать контент

---

## 10. Что уже работает (не переписывать с нуля)

В `Appmain.jsx`:
- Three.js сцена дверей (текстуры, свет, bloom, анимация открытия)
- Двери-сарай с диагональными досками
- White flash transition

В `AppLineup.jsx`:
- Side panel логика (hover/click, фон-фотка, видео muted/unmuted)
- Random tilt полосок
- torn-edges SVG filter

В `AppFundraiser.jsx`:
- 3D mouse tilt
- Ukraine flag hover transition
- DONATE button reveal

В `Appfootball.jsx`:
- Физика мяча (gravity, friction, bounciness)
- Глобальные window listeners (clever: pointer-events: none на canvas)
- Particles + grunge effects

Эти части переноси как есть, оборачивая в React-компонент с `useEffect` для инициализации Three.js / canvas. **Не пытайся переписать физику или 3D с нуля — это работает.**
