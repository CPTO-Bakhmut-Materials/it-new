# Plan: 4 IT lessons (mdBook, Ukrainian)

Detailed lesson plans: [plans/](plans/). Process step by step: [WORKFLOW.md](WORKFLOW.md).

## Decisions

| Topic | Decision |
|---|---|
| Language | Ukrainian (book text, program interfaces, GIF captions, tests) |
| Audience | Adults and college students. Very easy to follow, nothing deep |
| Software | Open-source only. The AI part uses the free Duck.ai web service, no sign-up |
| Format | mdBook |
| Fonts | Fixel Text / Fixel Display (MacPaw, designed in Ukraine, OFL) for text, headings, GIF captions and pictures; JetBrains Mono (OFL) for code. Bundled in `src/assets/fonts`, so the book works offline. Typographic apostrophe ’ in Ukrainian words |
| Lesson length | 35 min. The test is separate and not counted in that time |
| Student flow | Every lesson starts with an introduction: read the theory → watch the GIFs → take the test → (only if they want to) do the extra task |
| Theory | Two levels: short theory on the lesson page (what the 35 min and the test are built on), and a separate optional page **«Детальніше»** per lesson with more text, diagrams, charts, real examples and links to credible sources. Not covered by the test |
| Practical tasks | None in class. Each lesson ends with an extra task marked «Необов'язково» (not required; graded if the student submits it by email to cpto.bakhmut.925@gmail.com, subject: surname, name, group, lesson topic) |
| Media | GIFs (10–25 s, one action each, 960 px, 0.4–1.8 MB) recorded from the real programs, with click highlights and Ukrainian captions; MP4 for longer sequences. Private details (folder paths with the user name) are blurred |
| Tests | 10 questions per lesson, as a Google Form created by an Apps Script. One field «Прізвище та ім'я» plus «Група»; no email collection |
| No system changes | Ukrainian locale built inside the project; every program runs with a settings folder inside the project |
| Annotation tooling | Keep our own pipeline (scripted recording on a virtual X11 screen + annotations drawn afterwards from the event log). Wayscriber (live on-screen drawing for Wayland) was considered and not adopted: highlights would be baked in, no blur or caption bar, not repeatable, needs a Wayland session; ~1–2 days to switch for little gain. Good fit for live teaching and hand-made one-off clips in future projects |

## Lessons

| # | Field | Program | Content | Clips | Timing (35 min) |
|---|---|---|---|---|---|
| 1 | [Комп'ютерна графіка](plans/lesson-1-graphics.md) | Krita | Raster vs vector, formats; canvas, brush and colour, eraser and undo, layers, shapes, fill, text (with font size); open a photo, crop, resize, brightness (HSV/HSL filter); export JPG vs save layered drawing as .kra | 14 GIFs + 1 screenshot ✅ | theory 10, walkthrough 25 |
| 2 | [Текстові документи](plans/lesson-2-writer.md) | LibreOffice Writer | Paste and select text, font/size/bold/italic, heading styles + Navigator, alignment, lists, photo, table, spellcheck, save ODT/DOCX, export PDF; built around a simple CV | 10 GIFs + 1 screenshot ✅ | theory 10, walkthrough 25 |
| 3 | [Інтернет і безпека](plans/lesson-3-internet.md) | Firefox + uBlock Origin | Search operators, tabs, bookmarks, private window, domain and padlock check, phishing email, password manager, uBlock install / counter / per-site off | 8 GIFs + 1 MP4 + 2 pictures ✅ | theory 10, walkthrough 25 |
| 4 | [Основи програмування та ШІ](plans/lesson-4-programming-ai.md) | Geany (Python) + Duck.ai | First program, `input()`, calculator, `if`, read and fix an error; good requests to the AI, explain, find a bug, extend code and test it, everyday use; rules: check facts, no personal data, academic honesty | 11 GIFs + 3 pictures ✅ | theory 5, programming 15, AI 12, rules 3 |

Order: safety (lesson 3) comes before AI (lesson 4), so personal-data and source-checking rules are already known.

Topics of the «Детальніше» page per lesson (full lists in the lesson plans):

| # | «Детальніше» page |
|---|---|
| 1 ✅ | <ul><li>what a pixel stores, RGB numbers, HEX codes, 8 bits per channel</li><li>RGB vs CMYK (light vs ink)</li><li>DPI and print size, with a formula and a table</li><li>compression: JPG quality vs file size (measured chart), repeated saving</li><li>which format to choose (measured chart: photo vs drawing in PNG/JPG/WebP)</li><li>SVG, with the file's real source</li><li>graphics tablet and pressure</li><li>where to get images legally (Creative Commons)</li></ul> |
| 2 ✅ | <ul><li>text editor vs word processor (real .txt vs the formatted CV)</li><li>what is inside ODT/DOCX/PDF: measured size chart, ODT = ZIP diagram, fonts embedded in PDF</li><li>Enter vs Shift+Enter, Ctrl+Enter</li><li>serif vs sans-serif, sizes in points</li><li>page format, orientation, margins</li><li>automatic table of contents (real result)</li><li>compatibility with MS Office</li><li>more hotkeys</li></ul> |
| 3 ✅ | <ul><li>DNS (real IP lookup)</li><li>what https encrypts</li><li>what to do after entering data on a phishing site (table)</li><li>password guessing time chart (computed, assumption stated)</li><li>how 2FA codes work (real TOTP codes)</li><li>how uBlock works + measurement: 36 vs 1 domains on the same page</li><li>cookies</li><li>public Wi-Fi and updates</li></ul> |
| 4 ✅ | <ul><li>Hello World in 5 languages (compiled and run)</li><li>interpreter vs compiler</li><li>Python speed, measured</li><li>variable names with real Python errors</li><li>how LLMs write: next word, two real different answers, a real «no such function» answer</li><li>open-source AI on your own computer</li><li>what happens to chat data</li><li>installing Python on Windows today</li></ul> |

### Lesson 3: ad blocker section (uBlock Origin, open source)

- **Why:**
  - safety: fake "Download" buttons, fake virus warnings, and ads that lead to malware
  - privacy: trackers that follow you from site to site
  - speed and less traffic: pages load faster
  - less distraction
- **How it works:**
  - «Головне», one sentence: uBlock compares what a page loads against filter lists of known ad and tracker addresses and blocks the matches.
  - «Детальніше» page, with a simple diagram: a page asks the browser to load many parts (text, pictures, ads, trackers). uBlock checks each address against filter lists, which volunteers keep up to date. Blocked parts are never downloaded, and empty spaces left on the page are hidden.
- **Clips:**
  1. Install from addons.mozilla.org
  2. Pin the icon to the toolbar
  3. The same news site before and after, plus the counter of blocked items
  4. Turn blocking off for one site and back on
- **Rules:**
  - install only from the official add-ons store
  - beware of fake "ad blockers"
  - some sites ask you to turn off the blocker, so decide for yourself whether you trust that site

Phishing examples use only a made-up bank («ТвійБанк») and made-up domains.

## Lesson page structure

Every lesson starts with the same short introduction (a highlighted note block), then the sections follow in the order students work through them.

0. **Як працювати з уроком** (introduction, same in every lesson):
   > 1. Прочитайте теорію. Сторінку «Детальніше» відкривайте, якщо цікаво.
   > 2. Перегляньте анімації: кожна показує одну дію крок за кроком.
   > 3. Пройдіть тест (10 запитань). На початку вкажіть прізвище, ім'я та групу.
   > 4. За бажанням виконайте додаткове завдання. Воно необов'язкове, але якщо ви його надішлете, воно буде оцінене.
1. **Мета уроку:** 2–3 sentences
2. **Що знадобиться:** the program and the sample files to download
3. **Теорія:** short, at most one screen plus pictures. This is what the 35 min and the test are built on. It ends with a dashed box «Хочете знати більше?» (marked «Необов’язково»): a link to the «Детальніше» page and a list of its topics
4. **Покроково:** each step is short text plus a GIF; students watch them in order
5. **Підсумок:** 3–5 bullet points
6. **Тест:** link to or embed of the Google Form, done outside the 35 min
7. **Додаткове завдання (необов'язково):** only if the student wants to; graded if submitted; how to submit it

### The «Детальніше» page (`src/lesson-N-*/more.md`)

- A separate page under its lesson in the book menu; optional; not in the test. Starts with a note saying so and a link back to the lesson
- Numbered sections, each: plain text → a diagram, chart or real example → a short conclusion → **«Джерела»** line with links
- Every example and number is real: made from the lesson's own files and measured by a script (`recording/more_lN.py`), so the page can be regenerated
- Charts: one message per chart, a measured-values table next to it, colours checked for colour-blind readers
- Sources, in order of preference: the official manual of the program in Ukrainian (e.g. docs.krita.org/uk_UA), Ukrainian Wikipedia, official standards and vendors (W3C, JPEG committee, Google, Mozilla MDN, Creative Commons); English sources are marked «(англ.)». Every link is checked to open before publishing

## Recording the GIFs

- Xvfb virtual screen at 1280×800 plus openbox, so the user's Wayland desktop is not touched
- Programs run with `LANG=uk_UA.UTF-8`, so the menus are in Ukrainian. The locale is built into the project (`localedef` → `recording/locale/`, used through `LOCPATH`)
- Every program uses a profile in `recording/profiles/`; the user's own settings are never touched
- One Python scenario per clip (`recording/scenarios/<ID>.py`, helper `recording/lib/rec.py`) drives xdotool; `ffmpeg x11grab` records with the cursor visible and wallclock timestamps, so every logged action lines up with the video exactly
- Clips of one lesson run as a chain (each starts where the previous ended); the first clip restarts the program from its golden profile (`recording/profiles/<app>.golden`), so results never depend on earlier experiments
- Afterwards `recording/annotate.py` (Pillow) draws from the event log: a halo around the cursor (red while dragging), a red ripple on every click, red boxes around targets, key badges («Ctrl + Z»), blur over private areas, and a caption bar under the screen (Fixel Display; long captions shrink to fit)
- `gifski` makes the GIFs (960 px, < 2 MB); `ffmpeg` makes the MP4s; each clip is checked on a contact sheet (`recording/check.sh`)
- Captions can be changed without re-recording: the raw video and event log are kept in `recording/raw/`
- Annotated screenshots (numbered areas) come from `recording/shot.py`; theory pictures are generated by a script per lesson (`recording/theory_l1.py`)
- Web and AI clips change from run to run: each is recorded several times and the clearest take is kept; AI answers are read in full
- Every clip can be recorded again

## Tests

- 10 single-choice questions per lesson (4 options each), 1 point each, auto-graded, answer order shuffled
- Questions come only from the lesson page (theory and clips), never from the «Детальніше» page
- `tests/lesson-N.json` holds the questions; `tests/build.py` generates from it:
  - `tests/lesson-N.gs`: an Apps Script that creates the Google Form:
    - quiz mode is on
    - emails are not collected and sign-in is not required
    - «Прізвище та ім'я» and «Група» are required and not graded
  - `tests/lesson-N-key.md`: the answer key for the teacher; it is not part of the book
- Short guide on how to run the script: `tests/README.md` (a GIF can be added after the first real run)

## Typography

- **Fixel Text** (body), **Fixel Display** (headings), by MacPaw, designed in Ukraine, SIL OFL 1.1; full Ukrainian set (ґ, є, і, ї, ʼ/’, «»)
- **JetBrains Mono** (code), SIL OFL 1.1, full Cyrillic
- Fonts are bundled as WOFF2 in `src/assets/fonts/` with their licences (~0.8 MB); no internet needed
- Reading settings in `theme/lessons.css`: ~17 px text, line height 1.6, ~70 characters per line, automatic hyphenation (page language is `uk`)
- Ukrainian words use the typographic apostrophe ’ in the book (not in code and not in test questions)
- The same Fixel font is used for GIF captions and theory pictures

## Layout

```
PLAN.md, WORKFLOW.md, plans/  planning documents
book.toml                     mdBook settings (language uk)
theme/lessons.css             fonts, reading typography, note/clip/details styles
src/SUMMARY.md, intro.md
src/assets/fonts/             Fixel + JetBrains Mono (WOFF2) and licences
src/lesson-1-graphics/        index.md (lesson), more.md («Детальніше»), media/, media/more/, files/
src/lesson-2-writer/
src/lesson-3-internet/
src/lesson-4-programming-ai/
recording/                    not part of the book:
  env.sh, xstart.sh, app.sh     virtual screen, local locale, program launcher
  locale/, fonts/               local uk_UA locale, Fixel for captions
  profiles/<app>, <app>.golden  program settings (live copy and clean copy)
  scenarios/<ID>.py, lib/rec.py clip scenarios and helper
  run.sh, annotate.py, check.sh record + annotate, contact sheets
  shot.py, theory_l1.py         screenshots with numbers, theory pictures
  more_l1.py                    pictures, charts and measured numbers for «Детальніше»
  raw/                          raw videos and event logs
tests/                        lesson-N.json, build.py, lesson-N.gs, lesson-N-key.md, README.md
book/                         built site (mdbook build)
```

## Work order and status

| Stage | Status |
|---|---|
| Plan and lesson plans | ✅ done |
| 1. Environment: packages, local locale, program profiles | ✅ done (Krita golden profile in `recording/profiles/krita.golden`) |
| 2. Trial clip in Krita, style approved ✋ | 🔄 lesson 1 recorded in full (14 GIFs), waiting for review |
| Lesson 2 | 🔄 recorded (10 GIFs), page + «Детальніше» (8 sections) + test written; waiting for review |
| Lesson 3 | 🔄 recorded (8 GIFs + 1 MP4), page + «Детальніше» (8 sections) + test written; waiting for review |
| Lesson 4 | 🔄 recorded (11 GIFs), page + «Детальніше» (8 sections) + test written; waiting for review |
| 3. Lesson texts (one lesson reviewed first) ✋ | 🔄 lesson 1 written, plus its «Детальніше» page (8 sections, 11 pictures and 2 charts + 1 SVG, 33 checked source links, 0.56 MB); waiting for review |
| 4. Recordings, each checked | ✅ all 4 lessons |
| 5. Tests; the user runs one script to confirm it works ✋ | ✅ lesson 1 form created and linked (https://forms.gle/vdyZskWxerL8CF118 — opens without sign-in, name and group fields present); lesson 2 form linked (https://forms.gle/kYD2HWuUmeF2L41A9); lesson 3 form linked (https://forms.gle/ZqwCKrL6dhkWkSnaA); lesson 4 form linked (https://forms.gle/Xk2GWm2skzH81b519). All 4 tests done ✅ |
| 6. `mdbook build`, final read-through ✋ | 🔄 book builds; intro + all 4 lessons with «Детальніше» pages done; final read-through by the user pending |

✋ = the user approves before work continues.

## Open questions

1. ~~Windows screenshot of the Python installer~~ — resolved: the old installer is deprecated; the lesson now points to the Python install manager, which needs no PATH step.
2. ~~How students submit the extra tasks~~ — resolved: by email to cpto.bakhmut.925@gmail.com, subject «Прізвище Ім’я, група, тема уроку»; the file as an attachment. Written into every lesson and the intro.
3. Lesson 3: "what to do if you entered your data on a phishing site" is practical for adults. Keep it on the «Детальніше» page, or move it to the lesson page?

## Notes from recording lesson 1

- Krita's file dialogs show the full folder path (with the user name), so it is blurred in the clips. Two labels there («Look in», «Files of type») stay in English because Qt's own translations are not installed; students on Windows see the native dialog anyway.
- Every recording run of a lesson starts from the golden profile, so clips do not depend on earlier experiments.
- Krita 6 text tool: the default text is small; the clip shows changing «Розмір шрифту» in «Властивості тексту» (panel closed again afterwards, off camera).
- Krita remembers dialog positions; scenarios read the real window position (`win_geom`) instead of assuming it.
- Krita autosave is switched off in the golden profile (`AutoSaveInterval=0`), so autosave files never appear in file dialogs.
- Sample photo: «Carpathians in Ukraine», Roman Zacharij, public domain (Wikimedia Commons), credited on the page.
- Placeholders still on the lesson page: the test link and how to submit the extra task.
- «Детальніше» page: all numbers (JPG sizes, format comparison, print sizes) are measured from the lesson photo; re-running the script refreshes pictures and prints the numbers to copy into the tables. Krita's Ukrainian manual lives at `docs.krita.org/uk_UA/` (not `/uk/`).
- Commands: `recording/run.sh L1-02 … L1-15` records and annotates (~5 min for lesson 1); `recording/check.sh L1-05` makes a contact sheet; `python3 recording/more_l1.py` regenerates the «Детальніше» pictures and charts; `python3 tests/build.py 1` rebuilds the test; `mdbook build` builds the book into `book/`.

## Notes from recording lesson 2

- LibreOffice runs with a project-local profile (`recording/profiles/libreoffice`, golden copy `.golden`): Writer zoom 120 %, autosave/recovery off, LibreOffice's own (Ukrainian) file dialogs.
- Ukrainian spellcheck: Arch has no system package, so the official LibreOffice dictionary (MPL 1.1, from github.com/LibreOffice/dictionaries) is packed as `recording/extras/dict-uk.oxt` and installed into the project profile only.
- Typing Cyrillic with xdotool on Xvfb garbles letters below ~100 ms per key; `type_()` now defaults to 120 ms. Text is pasted through a small clipboard helper (`clipboard()`).
- The sample photo is a generated silhouette (no real person), saved at 300 dpi so Writer inserts it at a sensible size.
- Blur over file dialogs now starts at the click or key press that opens the dialog (fix applied to lessons 1 and 2; no path is visible in any frame).
- A crashing scenario now always stops its recorder (`atexit` cleanup in `lib/rec.py`).
- Commands: `recording/run.sh L2-02 … L2-11` (~5 min); `python3 recording/theory_l2.py`; `python3 recording/more_l2.py`; `python3 tests/build.py 2`.

## Notes from recording lesson 3

- Firefox runs with a project-local profile (`recording/profiles/firefox`, golden copy `.golden`; prefs in `ff/user.js`): Ukrainian UI, no first-run pages, no search suggestions or trending queries in the address bar, no account/sync prompts, no quit confirmation, no session-restore bar, reader view off, geolocation and speech prompts off, page zoom 1.2.
- uBlock Origin is installed during clip L3-09 from addons.mozilla.org, so every recording run starts without it.
- Ad content on real sites is random: every take is reviewed. One "without uBlock" screenshot showed a dating ad and was retaken; the final takes show only household goods, clothing and saplings.
- News sites were avoided (war content on the front page); sinoptik.ua (weather) is used for the ad-blocking demo.
- The password demo uses a local practice page served by `recording/serve.py`; the form posts to the local server, so no password appears in the address bar.
- Phishing examples use only made-up banks («ТвійБанк», «КвіткаБанк») and made-up domains; real state domains appear only as the genuine example.
- L3-06 is an MP4 (Diia's homepage has an animated background; the GIF was 9.4 MB, the MP4 0.8 MB). The page uses `<video autoplay loop muted playsinline>`.
- Commands: `recording/run.sh L3-02 L3-03 L3-04 L3-05 L3-06 L3-08 L3-09 L3-10 L3-11` (~7 min, needs internet), then `python3 recording/annotate.py L3-06 src/lesson-3-internet/media --mp4`; `python3 recording/theory_l3.py`; `python3 recording/more_l3.py`; `python3 tests/build.py 3`.

## Notes from recording lesson 4

- Geany runs with a project-local profile (`recording/profiles/geany`, golden `.golden`): editor font JetBrains Mono NL 16 (NL = no ligatures, so `>=` shows as typed; the book's CSS also turns ligatures off in code), no sidebar or message window, autocomplete off, programs run in xterm («Виконання програми») placed under the code.
- Programs are saved in `/tmp/kurs/programs`, so Python's error messages show a short path without the user name (no blur needed).
- Code with indentation is pasted, not typed, so Geany's auto-indent cannot double the spaces.
- Duck.ai: the first question shows a consent card («Продовжити») that the big input box can hide — L4-08 asks a short question first. A «PDF» promo card is closed before L4-10. Answers do not auto-scroll; `wait_stable()` scrolls and waits until the chat stops changing.
- Long AI waits are cut from the GIFs (`cut_start()`/`cut_end()` in scenarios, a «(очікування пропущено)» note in the clip).
- Every AI answer was read in full: all correct on both recording runs (explanation, both bugs found, working zero-division check, short polite message).
- GIF encoder now uses `--motion-quality 100 --lossy-quality 100`: lossy motion left faint "ghosts" of closed dialogs. All lessons were re-encoded from their raw recordings.
- Commands: `recording/run.sh L4-02 L4-03 L4-04 L4-05 L4-06 L4-07` (Geany), then `recording/run.sh L4-08 L4-10 L4-12 L4-11 L4-13` (AI; order matters — L4-12 continues the L4-10 chat; needs internet); `python3 recording/theory_l4.py`; `python3 recording/more_l4.py`; `python3 tests/build.py 4`.
