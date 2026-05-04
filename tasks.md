Я подготовлю для тебя **полный файл-инструкцию для Claude в формате Markdown**. Ты сможешь просто скопировать его и отправить своему помощнику, чтобы он по пунктам всё исправил в твоём `index.html`.

В инструкции будет:
- Объяснение контекста (что уже сделано, что нужно).
- Список задач с подробными шагами и примерами кода (что искать, на что заменять, куда вставлять).
- Ответы на твои вопросы про шрифты, цветокор и стики-элементы.

Ты сможешь дать этот файл Claude и сказать: «Вот моя страница index.html, пройди по этому списку и внеси все правки по очереди».

Если что-то останется непонятным, всегда можно уточнить у меня. Держи инструкцию 👇

---

```markdown
# Инструкция по доработке index.html для проекта "Двери в сарай"

## Общая информация
Этот файл содержит HTML/CSS/JS для одностраничного сайта с 3D-дверью и "внутренним ивентом" (сараем).  
Уже частично применены патчи, но нужны дополнительные правки.  
**Языковые переключатели оставляем только английский активным, остальные (UKR, CZE) отключены (disabled). Менять это не надо.**

Твоя задача – последовательно выполнить все пункты ниже, редактируя файл `index.html`.

---

## 1. Удаление кнопок навигации по блокам (Block 1, Block 2 и т.д.)
*Если таких кнопок уже нет в коде – пропусти этот пункт.*

**Что искать:**  
- HTML-элементы с классом `block-divider` или `block-arrow`.  
- В скрипте функцию `initBlockArrows()` (начинается с `// ── Block-arrow scroll-to-block`).

**Действия:**  
1. Удалить все `<div class="block-divider">...</div>` (обычно два таких блока).  
2. Удалить CSS-правила, начинающиеся с `.block-divider` и `.block-arrow`.  
3. Удалить весь скрипт, обёрнутый в `(function initBlockArrows() { ... })();`.

Если ничего из этого не найдено – значит уже удалено, переходи к следующему пункту.

---

## 2. Растянуть карту на всю ширину и подписать "Location"
Сейчас карта Google Maps ограничена по ширине `max-width: 680px`. Нужно убрать ограничение и добавить подпись.

**Шаги:**  
1. В секции `<style>` найди правило `.map-wrap iframe`. Удали строку `width: min(680px, 90vw);` и замени на `width: 100%;`. Высота пусть будет `height: 350px;`.  
2. В HTML найди `<div id="map-section">`. Сразу после `<h3>Strahov Stadium</h3>` перед блоком с картой добавь:
   ```html
   <p style="text-align:center; color:#ccc; font-size:0.9rem; margin-top:-10px; margin-bottom:20px;">📍 Location — Strahov Stadium, Prague</p>
   ```
3. Замени заголовок `<h3>Strahov Stadium</h3>` на:
   ```html
   <h3 style="font-size:1.2rem;">Strahov Stadium, Prague</h3>
   ```

Теперь карта будет на всю ширину секции, и подпись "Location" отобразится.

---

## 3. Sticky-логотип evro661 на всех страницах
Маленькое лого evro661 должно быть фиксировано в левом верхнем углу **на всех страницах** (и на дверях, и внутри сарая). Сейчас оно есть только внутри сарая.

**Как сделать:**
1. Внутри `<body>` сразу после открывающего тега добавь новый фиксированный блок:
   ```html
   <div id="sticky-logo" title="Back to entrance" style="position:fixed; top:20px; left:20px; z-index:1000; cursor:pointer;">
     <img src="" alt="EVRO661" id="sticky-logo-img" style="height:44px; width:auto; filter: drop-shadow(0 2px 8px rgba(0,0,0,0.6));">
   </div>
   ```
2. Найди в JS функцию `syncLogoSources()`. Сразу после неё добавь код, который копирует src для нового логотипа:
   ```javascript
   const stickyImg = document.getElementById('sticky-logo-img');
   if (stickyImg) {
     const heroSmall = document.querySelector('nav .logo img');
     if (heroSmall) stickyImg.src = heroSmall.src;
   }
   ```
3. Чтобы клик по логотипу возвращал на главную (если пользователь внутри сарая), добавь обработчик. Найди уже существующий обработчик для `#inner-logo-wrap`, скопируй его логику и привяжи к `#sticky-logo`. Можно просто продублировать тот же код, заменив селектор:
   ```javascript
   const stickyLogoDiv = document.getElementById('sticky-logo');
   if (stickyLogoDiv) {
     stickyLogoDiv.addEventListener('click', () => {
       // сюда вставить тот же код возврата, что и для #inner-logo-wrap
     });
   }
   ```
   (Логику возврата скопируй из уже существующей, она начинается с `if (innerLogoWrap) ...`).

Теперь логотип всегда будет в углу, независимо от того, открыты двери или нет.

---

## 4. Перевод сайта на английский
Замени все украинские/русские тексты на английские.

**Тексты для замены:**
- В секции `hero-scroll-content` внутри `<div class="content-text">`:
  ```
  Было: Двохденний благодійний івент на стадіоні Страгов (Прага). 8–9 травня 2026 — два дні безперервного рейву...
  Стало: A two‑day charity event at Strahov Stadium (Prague). May 8–9, 2026 — two days of non‑stop rave, experimental music and visual art by 6000ovecek & EVRO661. All proceeds go to the production of FPV drones for Ukraine.
  ```
- Кнопка: `<span class="paper-text font-grunge">Зайти</span>` → `Enter`.
- В JavaScript-коде (функция `renderPanels`) замени:
  - `'фото скоро'` → `'photos soon'`
  - `'видео будут позже'` → `'videos coming soon'`
  - `'фотки будут позже'` (если есть) → `'photos coming soon'`
  - `'Здесь будет био...'` – удали или замени на `'Bio coming soon'`.

---

## 5. Кнопка "Enter" поверх логотипа (на главной странице)
Сейчас кнопка находится под картинкой с овечками. Нужно, чтобы она была **поверх картинки**, по центру.

**Как сделать:**
1. Найди в `hero-center` заголовок `<h1 class="main-title">...<img...></h1>` и следующий за ним `<div class="btn-wrapper" id="enter-btn">...`.
2. Оберни их в общий контейнер:
   ```html
   <div style="position: relative; display: inline-block;">
     <h1 class="main-title" style="margin:0;"> ... (логотип) </h1>
     <div class="btn-wrapper paper-strip" id="enter-btn" style="position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%); margin: 0; width: auto;">
       <button class="enter-btn">
         <div class="paper-bg torn-edges"></div>
         <span class="paper-text font-grunge">Enter</span>
       </button>
     </div>
   </div>
   ```
3. Убедись, что у `h1.main-title` удалены лишние отступы (margin-bottom: 0;). Если был `margin-bottom: 40px;`, замени на `0`.

Теперь кнопка будет аккуратно наложена на картинку.

---

## 6. Донат-постер: точное соответствие React-компоненту
Сейчас донат-постер визуально отличается от компонента `AppDONATE.jsx`. Нужно привести HTML и CSS в соответствие.

**Замени текущий блок** (начиная с `<a id="donate-poster" ...>` и до закрывающего `</a>`) на:
```html
<a id="donate-poster" href="https://donio.cz/drony-solidarity-ctyri?utm_source=ig&utm_medium=social&utm_content=link_in_bio&fbclid=PAZnRzaARkOVJleHRuA2FlbQIxMQBzcnRjBmFwcF9pZA8xMjQwMjQ1NzQyODc0MTQAAac9JGrGySz9-WOv5QHxkTdHhGLoHlc_Wdyamg6nwUgc9gVl4fbKN8cFmwbGpw_aem_SmnPEwNws18n2qD_E0_AiQ" target="_blank" rel="noopener" title="Donate for Ukraine" aria-label="Donate">
  <div class="donate-inner" id="donate-inner">
    <div class="donate-noise"></div>
    <div class="donate-flag-bg"></div>
    <div class="donate-block donate-block-1"><span>Fundraiser</span></div>
    <div class="donate-block donate-block-2"><span>For</span></div>
    <div class="donate-block donate-block-3"><span>Ukraine</span></div>
    <div class="donate-cta"><span>Donate</span></div>
  </div>
</a>
```

**В CSS замени (или добавь) следующие правила** (полностью скопируй блок ниже и вставь в секцию `<style>`, удалив старые правила для donate-*):
```css
/* Полный блок стилей донат-постера (соответствует React) */
#donate-poster {
  position: fixed;
  bottom: 22px;
  right: 22px;
  width: 200px;
  height: 200px;
  z-index: 40;
  cursor: pointer;
  text-decoration: none;
  transform-style: preserve-3d;
}
.donate-inner {
  width: 100%; height: 100%;
  position: relative;
  display: flex;
  flex-direction: column;
  overflow: hidden;
  border: 6px solid #000;
  box-shadow: 6px 8px 0 rgba(0,0,0,0.8);
  transition: transform 0.5s ease-out, border-color 0.5s;
}
#donate-poster:hover .donate-inner {
  border-color: transparent;
  transition: transform 0.1s ease-out, border-color 0.5s;
}
.donate-flag-bg {
  position: absolute;
  inset: 0;
  background: linear-gradient(to bottom, #0057B7 50%, #FFDD00 50%);
  background-size: 100% 200%;
  background-position: 0 0;
  opacity: 0;
  transition: opacity 0.5s ease, background-position 0.5s ease;
  z-index: 0;
}
#donate-poster:hover .donate-flag-bg {
  opacity: 1;
  background-position: 0 -100%;
}
.donate-noise {
  position: absolute;
  inset: 0;
  background-image: url("data:image/svg+xml,%3Csvg viewBox='0 0 200 200' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.85' numOctaves='3' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23n)'/%3E%3C/svg%3E");
  opacity: 0.05;
  z-index: 2;
  pointer-events: none;
  mix-blend-mode: overlay;
}
.donate-block {
  flex: 1;
  display: flex;
  align-items: center;
  justify-content: center;
  position: relative;
  z-index: 1;
  transition: background-color 0.5s;
}
.donate-block-1, .donate-block-3 { background: #000; }
.donate-block-2 { background: #fff; }
#donate-poster:hover .donate-block-1,
#donate-poster:hover .donate-block-2,
#donate-poster:hover .donate-block-3 {
  background: transparent;
}
.donate-block span {
  font-family: 'Anton', sans-serif;
  line-height: 1;
  text-transform: uppercase;
  display: block;
  width: 100%;
  text-align: center;
  transition: transform 0.5s ease-out, color 0.5s;
}
.donate-block-1 span,
.donate-block-3 span {
  color: #fff;
  font-size: clamp(1.7rem, 9.5vw, 2.4rem);
  letter-spacing: -0.005em;
}
.donate-block-3 span { letter-spacing: 0.08em; }
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
}
.donate-cta {
  position: absolute;
  inset: 0;
  z-index: 3;
  display: flex;
  align-items: center;
  justify-content: center;
  opacity: 0;
  transition: opacity 0.5s 0.1s;
  pointer-events: none;
}
#donate-poster:hover .donate-cta { opacity: 1; }
.donate-cta span {
  background: #000;
  color: #fff;
  font-family: 'Anton', sans-serif;
  font-size: clamp(1.6rem, 7vw, 2.1rem);
  letter-spacing: 0.18em;
  text-transform: uppercase;
  padding: 10px 22px;
  border: 2px solid rgba(255,255,255,0.18);
  backdrop-filter: blur(4px);
  transform: translateY(16px);
  transition: transform 0.5s ease-out;
  box-shadow: 0 0 30px rgba(0,0,0,0.5);
}
#donate-poster:hover .donate-cta span { transform: translateY(0); }
```

JS-код для 3D-наклона оставь без изменений (он уже есть).

---

## 7. Иконка Instagram evro661 на дверях (вертикально, как в сарае)
На главной странице (hero-секция) нужно добавить вертикальную панель с иконкой Instagram, аналогичную той, что внутри сарая (`#event-social`), но только с одной ссылкой.

**Куда вставить:**  
Найди закрывающий тег `</nav>` самого верхнего меню в `hero-screen` (сразу после `div lang-switch`). Сразу после него добавь:

```html
<!-- Вертикальная иконка Instagram на дверях -->
<nav class="ev-social-door" aria-label="Instagram" style="position:fixed; left:20px; top:50%; transform:translateY(-50%); z-index:28;">
  <a class="ev-social-link" href="https://www.instagram.com/evro_661/" target="_blank" rel="noopener" aria-label="evro_661 on Instagram">
    <svg viewBox="0 0 24 24" style="width:17px; height:17px; fill:currentColor;"><path d="M12 0C8.74 0 8.333.015 7.053.072..."/></svg>
    <span>@evro_661</span>
  </a>
</nav>
```
(Можно скопировать полный svg из существующей ссылки в `#event-social`.)

Дополнительно в CSS добавь стили для `.ev-social-link` (если их ещё нет), они уже есть для `#event-social .ev-social-link`. Просто убедись, что они применяются глобально.

---

## 8. Кнопка звука на дверях (mute/unmute)
На дверях должна быть такая же кнопка управления звуком, как внутри сарая (`#bottom-left-ctrl`).

**Добавь HTML:**  
Внутри `hero-screen`, перед закрывающим `</section>`, вставь:
```html
<div class="door-audio-ctrl" style="position:fixed; bottom:24px; left:24px; z-index:40;">
  <button class="ctrl-btn" id="btn-sound-door" title="Toggle sound" aria-label="Toggle sound">🔇</button>
</div>
```

**Модифицируй JS:**  
Найди функцию `initSoundToggle()` (в самом конце скрипта). Внутри неё после получения `btn` добавь поддержку второго id:
```javascript
const btnDoor = document.getElementById('btn-sound-door');
// Добавь обработчик для btnDoor аналогично btn:
if (btnDoor) {
  let mutedDoor = true;
  btnDoor.addEventListener('click', () => {
    mutedDoor = !mutedDoor;
    const vid = document.getElementById('lineup-video-bg');
    if (vid) vid.muted = mutedDoor;
    btnDoor.textContent = mutedDoor ? '🔇' : '🔊';
  });
}
```
Либо просто замени в существующем коде `'btn-sound'` на `'btn-sound-door'` для дверей, а для сарая оставь `'btn-sound'`.

---

## 9. Sticky переключатель языков внутри сарая
Он уже находится в `<nav id="inner-nav">`, который становится видимым при скролле. Это работает. **Ничего менять не надо.** Если в будущем захочешь сделать его отдельно, можно вынести, но пока оставь.

---

## 10. Инстаграм 6000ovecek
Эта ссылка должна быть **только внутри сарая** – уже есть в `#event-social`. Ничего не меняем.

---

## 11. Дополнительные вопросы: шрифты и цветокор

### Шрифт в панковском стиле
Можешь использовать **Google Font "Permanent Marker"** – он отлично подходит для "панковского" настроения. Подключается простым добавлением в `<head>` ссылки:
```html
<link href="https://fonts.googleapis.com/css2?family=Permanent+Marker&display=swap" rel="stylesheet">
```
Затем применяем к нужным элементам (например, к названиям артистов или заголовкам) через `font-family: 'Permanent Marker', cursive;`. Можно заменить им шрифт для кнопок и заголовков, оставив `Cinzel` для лайнапа.

Если нужен более агрессивный, попробуй **"Metal Mania"** или **"Creepster"**, но они хуже читаются.

### Цветокор на дверях
Проблема: фон плохо сочетается с текстом. Решения:
- Изменить цвет заголовка `h1.main-title` на более контрастный, например, `#ffffff` с чёткой тенью.
- Добавить полупрозрачный тёмный фон непосредственно под текст с помощью `background: rgba(0,0,0,0.4); padding: 10px 20px; border-radius: 4px;`.
- Изменить цвет свечения (voidLight) или уменьшить интенсивность.

**Рекомендация:** добавь в CSS для `.hero-center`:
```css
.hero-center h1.main-title,
.hero-center .btn-wrapper {
  background: rgba(0,0,0,0.5);
  backdrop-filter: blur(5px);
  display: inline-block;
  padding: 15px 30px;
  border-radius: 8px;
}
```
Это сделает текст читаемым на любом фоне.

---

## Заключение
Пройди по всем пунктам по порядку. Если какой-то элемент уже отсутствует или выглядит иначе, пропускай его и переходи к следующему.

После выполнения всех правок страница должна выглядеть и работать так, как задумано. Удачи!
```

Ты можешь скопировать этот Markdown-текст и отправить его своему помощнику. Если что-то нужно уточнить или добавить, дай знать – я дополню.
