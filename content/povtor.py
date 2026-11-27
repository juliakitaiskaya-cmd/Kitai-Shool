# -*- coding: utf-8 -*-
import re, sys, glob, os
SKIP = ["Юлия Горяина", "Китаист, докторант", "Kitai School", "Записаться", "Шаньдунского университета", "основатель Kitai", "山大",
        "Частые вопросы", "Частые ошибки", "Чего в статье нет", "Источники",
        "popup:zayavka", "форматы и программа",
        # пункты бокового меню — они одинаковы во всех статьях по устройству
        "Разделы", "Онлайн-курсы", "Экзамены HSK", "Китайский детям",
        "Индивидуально", "Учёба в Китае", "Блог"]
def vis(p):
    s = open(p, encoding="utf-8").read()
    s = s[s.index('<main id="ks-art">'):s.index('</main>')] if '<main id="ks-art">' in s else s
    v = re.sub(r"<[^>]+>", " ", re.sub(r"(?s)<(script|style).*?</\1>", " ", s))
    return re.sub(r"\s+", " ", v)
def grams(t, n=60, step=3):
    return {t[i:i+n] for i in range(0, max(0, len(t)-n), step)}
me = sys.argv[1]
mv = vis("blog/%s.html" % me)
mg = grams(mv)
tot = 0
for p in sorted(glob.glob("blog/*.html")):
    b = os.path.basename(p)[:-5]
    if b == me or ".TILDA" in b or b.startswith("_"):
        continue
    try: og = grams(vis(p))
    except Exception: continue
    inter = [g for g in (mg & og) if not any(k in g for k in SKIP)]
    if inter:
        tot += len(inter)
        print("%-50s %d" % (b, len(inter)))
        for g in sorted(inter)[:4]:
            print("    …%s…" % g)
print("всего совпадений:", tot)
