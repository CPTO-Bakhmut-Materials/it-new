# Урок 3. Інтернет і безпека (Firefox + uBlock Origin)

**Time:** 35 min — theory 10, step-by-step walkthrough 25 (test is separate, not counted)
**Goal:** the student searches efficiently, reads a web address correctly, spots phishing, uses strong passwords and blocks ads.
**Sample files:** `files/login-demo.html` (a local practice login form, for the password manager), `files/phishing-email.png` (a made-up email from a fictional bank «ТвійБанк»)

Phishing examples use only made-up brands and domains (e.g. `tviybank.ua` vs `tviybank-ua.secure-check.com`).

## Theory

### On the lesson page (split between the parts)

- **Web address (URL):** annotated picture of `https://` + domain + path; **the domain is the part right before the first single `/`**
- **Padlock:** the connection is encrypted, but that does not mean the site is honest
- **Phishing:** signs to look for:
  - urgency («рахунок заблоковано!»)
  - a strange sender or link
  - requests for a password, card number or code from an SMS
  - spelling mistakes
- **Passwords:**
  - long beats complex (passphrase of 3–4 words)
  - a different password for every site
  - a password manager
  - two-factor authentication (2FA)
- **Ads and trackers:** why to block them; filter lists in one sentence
- **Private mode:** what it hides (history on this computer) and what it does not hide (from the site, your employer or your internet provider)

### «Детальніше» page (`more.md`, optional, not in the test) ✅

Written: 8 sections (DNS, what https encrypts, what to do after phishing, password guessing time chart, how 2FA codes work with real TOTP codes, how uBlock works with measurements 36 vs 1 domains, cookies, public Wi-Fi and updates); pictures from `recording/more_l3.py`. Original topic list:

- How a web address finds a site (DNS: a name is turned into a number address)
- What cookies are
- How a 2FA app works (the code changes every 30 seconds)
- What to do if you entered your data on a phishing site: change the password, call the bank, turn on 2FA
- How uBlock works in detail: a diagram of the page's requests, filter lists and hiding empty spaces
- Public Wi-Fi: what is risky there
- Why to install browser and system updates

## Practice — clips (as recorded)

| ID | Type | What is shown |
|---|---|---|
| L3-01 | annotated screenshot | Firefox window (sinoptik.ua, uBlock pinned), 7 numbered areas |
| L3-02 | GIF | Search in the address bar; "quotes"; site:gov.ua |
| L3-03 | GIF | Ctrl+T, switch tabs, close, Ctrl+Shift+T |
| L3-04 | GIF | Star → bookmark → Зберегти; Ctrl+Shift+B bookmarks bar |
| L3-05 | GIF | Ctrl+Shift+P private window (mask icon, explanation), Ctrl+Shift+W |
| L3-06 | MP4 | Domain of diia.gov.ua; site icon → «Захищене з’єднання» → details (MP4: the site has an animated background, GIF was 9.4 MB) |
| L3-07 | picture | Fictional phishing email («ТвійБанк»), 5 numbered signs |
| L3-08 | GIF | Practice sign-up page (local server, POST, nothing stored): generated password → save → menu → Паролі |
| L3-09 | GIF | addons.mozilla.org → check author/badges → Додати до Firefox → Додати → keep «Закріпити» → OK |
| L3-10 | GIF | sinoptik.ua with uBlock: badge counter, popup stats |
| L3-11 | GIF | Power button off → F5 (ads appear) → on again → F5 |

Pinning the uBlock icon is part of L3-09 (the install dialog has the checkbox), so there is no separate pin clip.
Lesson-page pictures: `media/url-anatomy.png`, `media/L3-07.png` — `recording/theory_l3.py`.
Practice files: `files/login-demo.html`, `files/done.html`; served by `recording/serve.py` (http://localhost:8765) while recording.

## Додаткове завдання (необов'язкове)

_Not required and not done in class. If a student submits it, the teacher grades it. Marked in the book as «Необов'язково»; the book also explains how to submit it._

1. Find an official document on a government site with `site:gov.ua`.
2. Look at 5 given web addresses and say which ones are fake, and why.
3. Make a passphrase and check its strength (rules in the lesson; no real passwords anywhere).

## Test topics (10 questions)

1. Which part of an address is the domain
2. What the padlock really means
3. Which of the given addresses is fake
4. A sign of phishing
5. A strong password example
6. Why to use different passwords
7. What 2FA is
8. What private mode does NOT hide
9. How an ad blocker decides what to block (filter lists)
10. Where to install add-ons safely from
