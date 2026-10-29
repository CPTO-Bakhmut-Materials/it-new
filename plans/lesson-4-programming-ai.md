# Урок 4. Основи програмування та робота зі ШІ (Geany + Python, Duck.ai)

**Time:** 35 min — theory 5, programming 15, AI 12, AI rules 3 (test is separate, not counted)
**Goal:** the student writes and runs a small Python program, reads an error message, and uses an AI assistant to explain, fix and improve code, with sensible caution.
**Sample files:** `files/calc.py` (finished calculator), `files/buggy.py` (the same program with 2 mistakes)

## Що знадобиться

- Windows: install the **Python install manager** from python.org or the Microsoft Store (the old installer with «Add python.exe to PATH» is deprecated since 3.14 and will not ship for 3.16+); `python` then works by itself. Linux usually has Python already.
- Install Geany (geany.org).
- For the AI part: a browser and duck.ai (no sign-up).

## Theory

### On the lesson page (one screen)

- A program is a recipe of exact steps for the computer; an algorithm is that recipe.
- A programming language; Python and why it suits beginners.
- What an AI chatbot is: it predicts likely text. It can be wrong while sounding confident ("hallucinations").

### «Детальніше» page (`more.md`, optional, not in the test) ✅

Written: 8 sections (Hello World in 5 languages — compiled and run; interpreter vs compiler; Python speed measured 1 thousand…100 million additions; variable names with real Python errors; how LLMs write + two real different answers + a real honest «no such function» answer; local open-source AI; what happens to chat data; installing Python on Windows today); pictures from `recording/more_l4.py`. Original topic list:

- Other languages and what they are used for (JavaScript: websites; C#: games; SQL: databases)
- How the computer runs Python code (interpreter)
- Rules for naming variables
- How AI models are trained, in simple words
- Open-source AI models that run on your own computer
- What AI services do with what you type

## Clips (as recorded)

| ID | Type | What is shown |
|---|---|---|
| L4-01 | annotated screenshot | Geany with calc.py, 7 numbered areas |
| L4-02 | GIF | Файл → Зберегти як… → hello.py; type print(...) — colours appear |
| L4-03 | GIF | Ctrl+S, F5, output window, Enter |
| L4-04 | GIF | input() + variable, run, type a name |
| L4-05 | GIF | Ctrl+N, paste calc.py, save, run with 12 and 4 |
| L4-06 | GIF | age.py: if / else, indentation; two runs (20 and 15) |
| L4-07 | GIF | Remove a bracket → SyntaxError, line 2, ^ → fix → runs |
| L4-08 | GIF | duck.ai, first question, «Продовжити» (terms), answer, «ШІ може помилятися» |
| L4-09 | picture | Weak vs good request (who + what + how + data) |
| L4-10 | GIF | New chat: «я новачок… поясни кожен рядок» + calc.py → explanation |
| L4-11 | GIF | New chat: error text + buggy.py → AI finds both bugs |
| L4-12 | GIF | Same chat as L4-10: add a zero-division check → copy code → Geany → run with 0 |
| L4-13 | GIF | Everyday use: polite message to a manager → «зроби коротше» |

Long AI waits are cut out of the GIFs (marked «ШІ думає… (очікування пропущено)»).
Lesson-page pictures: `media/program-flow.png`, `media/L4-09.png` — `recording/theory_l4.py`.

## Part C: rules for using AI (text, no clips)

- Check facts and test code; AI can be confidently wrong.
- Never paste personal data, passwords or work secrets.
- In studies, use AI as a tutor, not a ghostwriter; follow the teacher's rules.
- Ask follow-up questions; refine the request.

## Додаткове завдання (необов'язкове)

_Not required and not done in class. If a student submits it, the teacher grades it. Marked in the book as «Необов'язково»; the book also explains how to submit it._

Write a program that asks for a temperature in °C and prints °F. If something goes wrong, ask the AI to explain the error, not just to give the answer.

## Test topics (10 questions)

1. What a program or an algorithm is
2. What `print()` does
3. What `input()` does
4. Why the file needs the `.py` extension
5. Which key runs a program in Geany (F5)
6. What a line number in an error message tells you
7. A good request to an AI (pick the best of 4)
8. What an AI "hallucination" is
9. What must not be pasted into an AI chat
10. What to do with code written by AI before using it
