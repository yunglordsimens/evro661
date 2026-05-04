```markdown
# Analysis & Task List for index.html

## 1. Favicon
**Problem:** No favicon is set; user wants to use `public/logo evro.png` as favicon.  
**Solution:**  
- Add `<link rel="icon" type="image/png" href="public/logo evro.png">` (or convert to .ico) inside `<head>`.  
- Ensure the path is correct relative to the deployed site (if `public/` is not served, move the image to root and adjust href).

---

## 2. Sticky logo behaviour (evro661 logo)
**Problem:** “сейчас стики на все станицы evro661 надо убрать это ошибка”. Currently `#sticky-logo` appears on both the door page and the inside page? Needs investigation.  
**Current code behaviour:**  
- `#sticky-logo` is always in the DOM but hidden (`opacity:0; pointer-events:none`).  
- When user clicks “Enter” (dive), the JS adds class `visible` to `#sticky-logo` (after the doors open).  
- Clicking `#sticky-logo` triggers a “back to entrance” function that hides `#inside-section`, resets the 3D scene, and returns to the door page.  

**Issue:** User says sticky appears on all pages “evro661 надо убрать”. Could be that the logo is visible on the door page as well? Check the logic:  
```js
setTimeout(() => {
    const sLogo = document.getElementById('sticky-logo');
    if (sLogo) sLogo.classList.add('visible');
}, …)
```
This only runs inside the dive sequence, so it should only become visible on the inside page. But perhaps CSS initial state is wrong? The CSS has:
```css
#sticky-logo {
  position: fixed;
  ...
  opacity: 0;
  pointer-events: none;
  transition: opacity 0.6s ease;
}
#sticky-logo.visible { opacity: 1; pointer-events: auto; }
```
So it should be hidden by default. **Possible bug:** if the page is loaded with the inside section already open (e.g., via back navigation), the logo may not have `.visible`. That’s correct – it’s hidden.  
**Action:** Keep current logic; ensure no accidental early visibility. Remove any code that might prematurely add `.visible`.

---

## 3. Fonts integration
**User request:** Use the punk fonts from `public/` folder (especially **Hit Me Punk**). Other fonts (ttf) should just lie there for now. Apply **Hit Me Punk** (or **Punk Kid**) to:  
- Date & location text (“8.5 — 9.5.2026”, “Strahov Stadium, Prague”)  
- “GoOut Tickets” buttons on all pages.

**Steps:**
1. Add `@font-face` declarations for all provided ttf files, but initially only load one or two.
2. Apply `font-family: 'Hit Me Punk', cursive;` (or whatever the correct family name) to:
   - `.lineup-date h2, .lineup-date p` (inside section)
   - The date/location text under the big logo (inside-hero)
   - `.goout-big-wrap .paper-text` and `#goout-sticky .paper-text`
3. Keep other fonts ready for future use.

---

## 4. GoOut Tickets buttons – font
**Request:** Use “punk kid” font specifically for GoOut Tickets. If “Punk Kid” exists as a separate ttf, load it as a second family, otherwise use “Hit Me Punk”. Apply to:
- The “GoOut Tickets” button on the door page (`#goout-sticky`)
- The large “GoOut Tickets” button inside (`goout-big-wrap`)
- (Optional) any other ticket buttons.

---

## 5. Опечатка “<” near “📍 LOCATION — STRAHOV STADIUM”
**Report:** “Тут есть вот єта опечатка «<«”.  
**Inspection:** The HTML shows:
```html
<h3 style="font-size:1.2rem;">Strahov Stadium, Prague</h3>
<p style="…">📍 Location — Strahov Stadium, Prague</p>
```
No stray `<` character. Possibly a visual rendering quirk or a missing closing tag? If user insists, add a comment that no literal “<” was found, but we can re-check the encoding. Could be a misinterpretation of the `<p>` tag?  
**Action:** Verify the page in browser; if an extra “<” appears, it might be from an unescaped character. Ensure all text is clean. If needed, re-type the line.

---

## 6. Football ball image not loading (ball.png)
**Problem:** In the football game (`initFootballGame`), the code does `ballImg.src = 'ball.png';` and on error draws a grey circle. The ball image is in `public/ball.png`, but the path is wrong because the HTML is likely served from the root, so it should be `'public/ball.png'` or just `'ball.png'` if the server maps `public/` to root.  
**Solution:**  
- Move `ball.png` out of `public/` into the same directory as `index-2.html`, or adjust the path to `'public/ball.png'`.  
- Test that the image loads; if not, fix path.

---

## 7. Fundraising progress – “old station clock” style flip counter
**Request:** Style the donation counter like an old train-station split-flap display. It should be in the center of the door page (currently inside `.hero-scroll-content`). User may want to revert later, so keep changes modular.

**Implementation plan:**
- Create a flip-clock style container for the numbers (e.g., `€2,143`).
- Use CSS for the flip effect (or a small JS animation) – each digit is a card with top/bottom halves that flip on update.
- Keep the bar as a secondary indicator.
- Make it centered: `.donation-counter { margin: 40px auto; max-width: 440px; text-align: center; }` (already does).
- Add a new class `.flip-counter` with required styles.
- Provide a fallback class without flip animation for easy revert.

---

## 8. Mobile adaptation
**Current state:** Some media queries exist (`@media (max-width: 700px)`, `@media (max-width: 600px)`), but they are minimal. Need thorough responsive improvements:
- Ensure `.hero-logo-wrap` → logo image resizes and stays centered.
- `.lineup-column` strips adjust width/font-size.
- Side panels disappear on mobile (already done via `@media (max-width: 900px)`), verify behaviour.
- The big logo inside `#inside-hero` should scale down and remain centered.
- `.btn-wrapper` buttons should scale appropriately.
- The fundraising counter should stack vertically if needed.
- The map iframe should be 100% width.

**Action:** Expand the mobile media queries with rules for:
- Flexible widths, max-width on containers.
- Reduce font sizes where needed.
- Stack elements that are side-by-side.
- Adjust sticky elements (GoOut button, donate poster).

---

## 9. Sticky “📍 Map” link that scrolls to map section
**Request:** “добавить надо плашку сверху стики типо 📍 чтоб можно было кликнуть и перелистывается на низ старицы в то метто где карта”.  
**Implementation:**
- Inside `#inside-section`, add a fixed-position link/button at the top-right or top-left with an icon (📍) and maybe text “Map”.
- On click, smoothly scroll to `#map-section`.
- Style it with a paper-strip aesthetic or simple button.
- Ensure it is hidden unless the inside section is active (use same visibility logic as `#event-social`).

---

## 10. Remove bouncing scroll arrow
**Problem:** User said “убрать надо стрелочку которая качается нахуй”. There is a `.scroll-indicator` on the door page (inside hero) with a `bounce` animation.  
**Action:** Remove the entire `.scroll-indicator` element from the door page. The inside page also has `.inside-scroll-hint` (non-bouncing) – keep that for now, but if the user wants all hints gone, remove it too; default to just removing the door one.

---

## Summary of Changes to Make

| # | Task | Location | Priority |
|---|------|----------|----------|
| 1 | Add favicon | `<head>` | High |
| 2 | Verify sticky logo visibility logic; no changes likely needed | JS after dive | Low |
| 3 | Load punk fonts via @font-face, apply to date/location/buttons | CSS + HTML classes | High |
| 4 | Apply font “Punk Kid” to GoOut buttons | Buttons: `#goout-sticky`, `.goout-big-wrap` | High |
| 5 | Check for stray “<” character near Location text | Map section text | Medium |
| 6 | Fix ball.png path in football game | `initFootballGame()` | Medium |
| 7 | Style fundraising counter as flip-clock | `.donation-counter` | Medium (with toggle) |
| 8 | Improve mobile/tablet responsive styles | CSS media queries | High |
| 9 | Add sticky “📌 Map” button with scroll-to | Inside section (JS + HTML) | Medium |
| 10 | Remove bouncing scroll indicator on door page | `.scroll-indicator` | High |

---

**Next Steps for Claude Code:**
1. Read the current `index.html` file thoroughly.
2. For each task above, implement the changes directly in the HTML file (add/remove elements, adjust CSS, tweak JS).
3. Pay special attention to paths (fonts, images) – ensure they reference the correct relative or absolute paths.
4. Test mobile responsiveness using browser dev tools after changes.
5. Provide a summary of modifications when done.
```
