Вот следующий пакет задач для Claude Code. Скопируй его в чат и выполняй по пунктам.

---

## Пакет задач для Claude Code (в файле index-2.html)

### 1. Замена шрифта Punk Kid на HitMePunk-8 для кнопок GoOut Tickets
- Добавь `@font-face` для `HitMePunk-8.ttf` (лежит в корне/папке public).
- У всех элементов, где сейчас используется `'Punk Kid'`, замени на `'HitMePunk-8'`.  
  Кнопки `#goout-sticky .paper-text` и `.goout-big-wrap .paper-text`.

### 2. Увеличить размер всех текстов с HitMePunk
- Найди селекторы `.strip-text`, `.paper-text`, `.font-grunge` и увеличь `font-size` на 30% (если было 1.2rem, сделай 1.56rem; если 1.4rem → 1.82rem).  
- Где используется инлайн-стиль с font-size (например, в `goout-big-wrap`), тоже подкрути.

### 3. Заменить шрифт «Montserrat» на «Times New Roman» в определённых местах
- Замени `font-family: 'Montserrat', sans-serif` на `'Times New Roman', serif` для следующих селекторов:
  - `.hero-eyebrow`
  - `.content-text p`
  - `.donation-label`
  - `.donation-amount .goal`
  - `#fundraising-bar .fb-label`
  - `.lineup-date p`
  - Везде, где используется классами с `font-family: 'Montserrat'` (кроме основных `body`, `html` – их оставь).

### 4. Разбить на две строки дату и место под большим логотипом внутри сарая
- Найди элемент внутри `#inside-hero` с текстом `8.5 — 9.5.2026  |  Strahov Stadium, Prague`.
- Сделай его двумя `<p>`:
  ```html
  <p class="inside-date">8.5 — 9.5.2026</p>
  <p class="inside-location">Strahov Stadium, Prague</p>
  ```
- Добавь стили для `.inside-date` и `.inside-location` – оба центрированы, размер шрифта как текущий, но `inside-location` может быть чуть мельче.

### 5. Добавить плашку «SPOT» под переключателем языков
- На дверной странице (после `#door-lang`) добавь:
  ```html
  <div class="spot-badge">📍 <span>SPOT</span></div>
  ```
- На внутренней странице (после `#inner-lang`) добавь такой же блок, но с `onclick="scrollToMap()"` (или `id="spot-badge-inner"` и отдельный обработчик).
- Стили для `.spot-badge`:
  - Без рамок.
  - Крупный шрифт (например, 1.8rem), иконка 📍 и слово SPOT капсом.
  - Расположить горизонтально, центрировать под языками.

### 6. Мобильная адаптация (исправление переключателя языков и переносов)
- При ширине экрана ≤600px скрывай текстовый переключатель языков (спаны) и показывай выпадающий список `<select>` с теми же опциями (UKR, ENG, CZE). Расположи его слева.
- JS для создания select и привязки обработчика (или через `initMobileLangSelector`).
- Чтобы текст не вылезал за границы, добавь `word-break: break-word;` или `overflow-wrap: break-word;` для проблемных элементов (например, `.hero-eyebrow`, длинные названия артистов на мобильном).
- Убедись, что `.lineup-column` и `.strip-wrap` имеют `max-width: 100%` и `white-space: normal` на мобильных.

---

Эти задачи покрывают все твои пожелания. Выполни их по порядку в Claude Code, после каждого пункта проверяй результат. Если нужно, я могу уточнить любой шаг.
