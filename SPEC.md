# evro661 × 6000ovecek — лендинг spec

> Этот документ — задание для Claude Code. Он описывает что нужно построить.
> Стек предполагается **Vite + React + Tailwind** (как в твоём portfolio repo).
> Текущий self-contained `index.html` лежит в репо как **рабочий референс** —
> вся логика дверей / лайнапа / вспышки уже там, можно копировать куски.

---

## 0. Контекст ивента

- **Что это:** одностраничный сайт (лендинг) для двухдневного благотворительного концерта / вечеринки солидарности
- **Даты и локация:** 8–9 мая 2026 года, Страгов, Прага
- **Цель:** сбор средств на производство FPV-дронов для Украины
- **Организаторы:** [@sest_tisicu_ovecek](https://www.instagram.com/sest_tisicu_ovecek/), [@evro_661](https://www.instagram.com/evro_661/), [@resistancesupportclub](https://www.instagram.com/resistancesupportclub/)

---

## 1. Структура — два экрана в SPA

1. **Door page** — двери сарая, hero с большим логотипом, краткое описание, кнопка «Зайти»
2. **Event page** — за дверями, лайнап + всё остальное

**Переход:** клик «Зайти» → анимация открытия дверей → white flash → event page.
**Возврат:** клик на маленький логотип `evro661` в шапке → обратно на door page.

---

## 2. Persistent UI (одинаково на обеих страницах)

| Позиция | Элемент | Когда показывать |
|---|---|---|
| top-left | clickable logo `logoevro661.png` | всегда |
| top-right | language switcher `🇺🇦 UKR ｜ 🇬🇧 ENG ｜ 🇨🇿 CZE` | всегда |
| bottom-right | Donate poster (sticky) | всегда |
| left side, под логотипом | соц-иконки instagram с подписями | **только event page** |
| bottom-left | кнопки game ⚽ + sound 🔇 | **только event page** |

### Соц-иконки на event page (вертикальный столбик слева)
```
[ig icon]  @evro_661           → https://www.instagram.com/evro_661/
[ig icon]  @sest_tisicu_ovecek → https://www.instagram.com/sest_tisicu_ovecek/
```
**Важно:** SoundCloud иконку убрать совсем.

### Lang switcher
- 3 языка: украинский, английский, чешский
- Подсветка активного, клик переключает (для preview можно просто визуально, без реального i18n; задел под `react-i18next` если потом надо)

### Donate poster (sticky bottom-right, всегда виден)
**Порт из твоего React-сниппета** (`Fundraiser / For / Ukraine`, 3D mouse tilt, hover → украинский флаг + DONATE button). Основные параметры:
- Размер: ~`280px × 280px` (компактнее чем в твоём оригинале — это ведь sticky badge, не главный элемент)
- 3D tilt по mouse position (твой код `handleMouseMove` готовый)
- Hover: фон становится украинским флагом, появляется DONATE кнопка
- Wrapper это `<a href={DONATE_URL}>` — пока placeholder, потом реальная ссылка на платформу

---

## 3. Door page

### Hero (центр экрана)
1. **Eyebrow:** «FUNDRAISING EVENT BY» (мелкий tracking, тонкий шрифт)
2. **Big logo:** `logo-ovecki-evro.png` (с `mix-blend-mode: screen` чтоб белый фон растворился над тёмной 3D-сценой)
3. **Description:** короткий текст-абстракт (1–2 предложения)
4. **Button:** «Зайти» (paper strip с `torn-edges` SVG-фильтром, **по центру**) — на месте старой «Dive In»

**Чего быть не должно** на door page:
- ❌ Стрелка «scroll to explore» внизу (убрать)
- ❌ Стрелка top-right (она была для перехода — теперь её роль играет клик на логотип)
- ❌ SoundCloud иконка

### Scroll content (если юзер скроллит вниз вместо клика на «Зайти»)
- Полное описание ивента (см. секцию 0)
- Кнопка **GoOut Tickets — по центру** → `https://goout.net/en/6k-and-evro661-spring-strahov4ukraine/sznyyiy/`
- **Donation counter:** прогресс-бар + текст вида `€2,143 of €10,000 goal`. Для preview — анимированный random tick. Позже подключить к backend.

---

## 4. Event page

### 4.1. Inside hero — большой логотип, морфит на скролле
- На входе занимает весь viewport, по центру
- При скролле **уходит влево-вверх и становится меньше**
- Конечное состояние: маленькая версия в районе top-left (можно ниже основного `evro661` лого, или как persistent header lineup-а)
- Один раз срабатывает **фотовспышка** под `evro661` (текущая реализация в `index.html` готовая, копировать)

### 4.2. Lineup
- Источник правды для имён: **`artists.js`** в репо
- ⚠️ В `Lineup.jsx` мок-имена местами кривые: `GOINMAN`, `PLANDONA`, `LILATESLA` — игнорировать, использовать `name` из `artists.js`
- 23 артиста, разбиты на 3 блока (поле `block: 1|2|3`)
- Имя на бумажной полоске с `torn-edges` SVG-фильтром, лёгкий random наклон
- Артисты подгружают свои ассеты из папок `artists-data/{slug}/`:
  - `imgs: ["photo-1.jpg", "photo-2.jpg", ...]` — **массив**, от 1 до N штук
  - `vids: ["video.mov"]` — массив, до 3 штук рендерится в side panel
  - `bio: contents of bio.md`
- В `artists.js` некоторые поля `null` — у этих артистов ассеты ещё не пришли. Нужно gracefully скипать (либо placeholder, либо просто не рендерить блок)

### 4.3. Side panels (когда артист активен)
- **Left panel:** все фотки артиста + блок текста с инфо
- **Right panel:** до 3 видео (autoplay muted, на hover — звук включается) + bio
- Activate: hover (preview) или click (lock); клик мимо = снять lock
- На мобиле side panels не лезут — fallback на inline tooltip под полоской

### 4.4. Central illustration
`characters.png` — после блока 1 (после ~9 артистов), по центру колонки, `mix-blend-mode: screen`

### 4.5. Background video
`footbolchik.mp4` (лежит в репо, ветка `original`) — фон секции лайнапа, `loop muted`, `opacity: 0.4`. Можно как `<video>` или CSS background.

### 4.6. Music player (всплывающий снизу, простейший)
- При клике на артиста в лайнапе появляется снизу
- Контент: имя артиста + ▶/⏸ + ✕ (close)
- Источник трека: добавить поле `track` в данные артиста (URL на mp3 или SoundCloud iframe). **Пока placeholder** — повесь `<audio src="">`, оставь TODO comment
- Можно закрыть кнопкой × — пока не вернётся при клике на следующего артиста

### 4.7. Bottom-left controls (только event page)
- **⚽ кнопка** — toggle игры (см. ниже)
- **🔇 / 🔊 кнопка** — toggle ambient sound сайта (можно либо beep loop, либо аудио из текущего трека)

### 4.8. Game ⚽
- Источник: твой `Punk Football Game` HTML (готовый код, в репо)
- **Замени:** custom-drawn euro-ball → `<img src="ball.png">` (либо drawImage на canvas)
- Toggle через кнопку bottom-left: при первом клике мяч «прикрепляется» в нижнем левом углу (idle state), второй клик/перетягивание = ввод в игру
- Или проще: кнопка просто переключает overlay on/off, как в её HTML
- Канвас `pointer-events: none` глобально, на window listener — если клик попал в радиус мяча, ловим (preventDefault) и пинаем; иначе клик проходит сквозь на сайт
- Score badge bottom-center

### 4.9. Под лайнапом
- **Большая кнопка GoOut Tickets** — по центру, заметная (не маленькая как в шапке)
- **Map section:** Google Maps embed Strahov stadium (~`50.0810, 14.3897`)
- Клик на карту = открывает реальный Google Maps в новой вкладке
- Когда юзер находится на map section — иконка карты (если она есть в шапке) прячется

---

## 5. Assets

Положи в `/public/` или `/src/assets/`:

| Файл | Назначение |
|---|---|
| `logo-ovecki-evro.png` | большой логотип (рукописный) |
| `logoevro661.png` | маленький лого evro661 (зелёный) |
| `characters.png` | иллюстрация персонажей в лайнапе |
| `ball.png` | мяч для игры |
| `footbolchik.mp4` | фоновое видео для event page |
| `artists-data/{slug}/photo-{n}.{jpg,png}` | фотки артистов |
| `artists-data/{slug}/video.{mov,mp4}` | видео артистов |
| `artists-data/{slug}/bio.md` | био артистов |

⚠️ В `artists.js` отмечено что у части артистов материалы ещё не пришли (`null`). Контактировать с **keiko-sei** — у неё ничего нет.

---

## 6. Технические заметки

- **3D сцена дверей:** копируй целиком из текущего `index.html`. Работает, протестировано. Three.js r128 + EffectComposer + UnrealBloomPass.
- **Стены сарая:** `BoxGeometry(10, 10, 1)` для боков, `BoxGeometry(30, 5, 1)` для верх/низ — без удлинённых линий
- **Шрифты:** `Rock Salt` (рукописные полоски), `Cinzel` (заголовки), `Montserrat` (body)
- **SVG filter `torn-edges-filter`:** копируй из текущего файла, нужен для всех бумажек
- **Photo flash под лого:** keyframes `@keyframes photoFlash` — резкий pop за 8% длительности, потом fade с blur. Триггер один раз на `scroll > 25%`, сбрасывается если scroll back to top.

---

## 7. Ссылки (источник правды)

| Что | Куда |
|---|---|
| Tickets | https://goout.net/en/6k-and-evro661-spring-strahov4ukraine/sznyyiy/ |
| Instagram evro661 | https://www.instagram.com/evro_661/ |
| Instagram 6000 ovecek | https://www.instagram.com/sest_tisicu_ovecek/ |
| Instagram resistance | https://www.instagram.com/resistancesupportclub/ |
| Donate | TBD (placeholder) |
| Map | Strahov stadium, Praha — embed Google Maps |

---

## 8. Что уже сделано (в текущем `index.html` в репо)

✅ 3D сцена дверей с открытием
✅ Big logo + small logo embedded
✅ White flash transition
✅ Photo flash под evro661 (на скролле)
✅ Lineup из 23 артистов с правильными именами из artists.js
✅ Side panels (hover/click, фотки + видео + bio)
✅ Characters illustration в центре лайнапа
✅ Кнопка GoOut с правильной ссылкой
✅ Instagram link на evro_661
✅ Стены сарая компактные (без удлинённых линий)
✅ Скролл-стрелочка вместо текста

## 9. Что осталось сделать

⏳ «Зайти» вместо «Dive In»
⏳ Persistent layer: глобальный logo + lang switcher (с CZE) + donate poster + соц-иконки слева на event page
⏳ Eyebrow «FUNDRAISING EVENT BY» + описание на door page
⏳ Donation counter
⏳ GoOut button по центру (сейчас слева)
⏳ Big logo морф left-up на скролле (сейчас просто fade out)
⏳ Music player widget
⏳ Game с ball.png
⏳ Map section
⏳ Background video footbolchik.mp4
⏳ Перекрёстные клики на лого для навигации между экранами
⏳ Sound toggle
