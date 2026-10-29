#!/usr/bin/env python3
"""Build Google Forms quiz scripts and answer keys from tests/lesson-N.json.

    python3 tests/build.py            # all lessons
    python3 tests/build.py 1          # one lesson

Writes tests/lesson-N.gs (paste into script.google.com, run createForm)
and tests/lesson-N-key.md (answer key for the teacher, not part of the book).
Answer order is shuffled once here, with a fixed seed, so the correct answer
is not always first and the key stays stable between builds.
"""
import glob
import json
import os
import random
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
LETTERS = "АБВГ"

GS = """/**
 * {title}
 * Створює Google Форму-тест. Як запустити:
 *  1. Відкрийте https://script.google.com → «Новий проєкт».
 *  2. Видаліть увесь код у редакторі й вставте цей файл.
 *  3. Натисніть «Виконати» (функція createForm) і дозвольте доступ до Google Форм.
 *  4. Коротке посилання на форму (forms.gle/…) з'явиться в «Журналі виконання».
 * Згенеровано tests/build.py з tests/{src} — правте JSON, а не цей файл.
 */
function createForm() {{
  var form = FormApp.create({title_js});
  form.setDescription({desc_js});
  form.setIsQuiz(true);

  // Адреси e-mail не збираються; вхід у Google-акаунт не вимагається.
  try {{
    form.setEmailCollectionType(FormApp.EmailCollectionType.DO_NOT_COLLECT);
  }} catch (e) {{
    form.setCollectEmail(false);
  }}
  try {{ form.setRequireLogin(false); }} catch (e) {{}}  // лише для Google Workspace
  form.setLimitOneResponsePerUser(false);  // true вимагало б входу в акаунт
  form.setAllowResponseEdits(false);
  form.setShuffleQuestions(false);

  form.addTextItem().setTitle("Прізвище та ім'я").setRequired(true);
  form.addTextItem().setTitle("Група").setRequired(true);

  var questions = {questions_js};
  questions.forEach(function (q) {{
    var item = form.addMultipleChoiceItem();
    item.setTitle(q.q)
        .setChoices(q.options.map(function (o, i) {{
          return item.createChoice(o, i === q.correct);
        }}))
        .setPoints(1)
        .setRequired(true);
  }});

  var url = form.getPublishedUrl();
  var shortUrl = url;
  try {{ shortUrl = form.shortenFormUrl(url); }} catch (e) {{}}
  Logger.log("Коротке посилання для студентів: " + shortUrl);
  Logger.log("Повне посилання для студентів: " + url);
  Logger.log("Редагування форми: " + form.getEditUrl());
}}
"""


def build(path):
    with open(path, encoding="utf-8") as f:
        test = json.load(f)
    name = os.path.splitext(os.path.basename(path))[0]
    rnd = random.Random(name)
    qs = []
    for q in test["questions"]:
        options = [q["correct"], *q["wrong"]]
        rnd.shuffle(options)
        qs.append({"q": q["q"], "options": options, "correct": options.index(q["correct"])})
    assert len(qs) == 10, f"{path}: {len(qs)} questions, expected 10"

    js = lambda v: json.dumps(v, ensure_ascii=False)
    with open(os.path.join(HERE, name + ".gs"), "w", encoding="utf-8") as f:
        f.write(GS.format(title=test["title"], src=os.path.basename(path),
                          title_js=js(test["title"]), desc_js=js(test["description"]),
                          questions_js=json.dumps(qs, ensure_ascii=False, indent=2)
                          .replace("\n", "\n  ")))

    lines = [f"# Ключ: {test['title']}", "",
             "Для викладача. Не публікувати в книзі.", "",
             "| № | Запитання | Правильна відповідь |", "|---|---|---|"]
    for n, q in enumerate(qs, 1):
        lines.append(f"| {n} | {q['q']} | {LETTERS[q['correct']]}) {q['options'][q['correct']]} |")
    lines += ["", "## Варіанти відповідей", ""]
    for n, q in enumerate(qs, 1):
        lines.append(f"{n}. {q['q']}")
        for i, o in enumerate(q["options"]):
            mark = " ✔" if i == q["correct"] else ""
            lines.append(f"   - {LETTERS[i]}) {o}{mark}")
    with open(os.path.join(HERE, name + "-key.md"), "w", encoding="utf-8") as f:
        f.write("\n".join(lines) + "\n")
    print(f"{name}: .gs and key written; correct letters: "
          + "".join(LETTERS[q["correct"]] for q in qs))


if __name__ == "__main__":
    want = sys.argv[1:]
    for p in sorted(glob.glob(os.path.join(HERE, "lesson-*.json"))):
        if not want or any(p.endswith(f"lesson-{n}.json") for n in want):
            build(p)
