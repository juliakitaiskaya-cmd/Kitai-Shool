# -*- coding: utf-8 -*-
# Картинки к статье «Учебник HSK 4»
# Обложка     — полоса прибавки уровня из трёх частей: том 4A, оценка 4B и добор
# Инфографика — две колонки: что написано в объявлении и что это значит
import sys
sys.path.insert(0, "/home/user/Kitai-Shool/content")
from uch4 import (VOL_A, VOL_B, STEP_NEW, STEP_OLD, A_WORDS, B_EST, A_SHARE, BOTH_SHARE,
                  REST, BOOKS_STUDENT, LEVEL_NEW)

S = ("/tmp/claude-0/-home-user-Kitai-Shool/a463bfca-82a9-56fd-ae09-42a7257ff999/"
     "scratchpad/")

FONTS = ('<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,'
         'wght@0,600;0,700;1,600&family=Inter:wght@400;500;600;700&display=swap" '
         'rel="stylesheet">')
VARS = (":root{--brick:#A41E3A;--brick-d:#841630;--brick-soft:#F7E6EB;--ink:#2C2420;"
        "--ink-2:#5A4F45;--taupe:#8B7D6B;--cream:#FAF7F2;--cream-2:#F3EDE3;--hair:#EAE3D8;"
        "--surface:#fff;--grey-soft:#EFEDE8;--grey:#9A9289}")

BASE = """
*{margin:0;box-sizing:border-box}
.card{position:relative;overflow:hidden;font-family:'Inter',sans-serif;
 background:radial-gradient(1040px 700px at 6% 2%, #fff 0%, var(--cream) 56%, var(--cream-2) 100%);
 display:flex;flex-direction:column}
.card:before{content:"";position:absolute;left:0;top:0;bottom:0;width:12px;background:var(--brick)}
.eyebrow{color:var(--brick);font-weight:700;font-size:17px;letter-spacing:.19em;
 text-transform:uppercase;margin-bottom:7px}
h1{font-family:'Cormorant Garamond',serif;font-weight:600;line-height:1.06;
 color:var(--ink);letter-spacing:-.3px}
h1 i{font-style:italic;color:var(--brick)}
.tip{background:var(--surface);border:1px solid var(--hair);border-left:4px solid var(--brick);
 border-radius:13px;padding:12px 17px;font-size:14px;color:var(--ink-2);line-height:1.36}
.tip b{color:var(--ink)}
.foot{display:flex;align-items:center;gap:14px;margin-top:auto;border-top:1px solid var(--hair);
 padding-top:12px}
.foot .lb{font-size:12px;font-weight:700;letter-spacing:.11em;text-transform:uppercase;
 color:var(--taupe);flex:0 0 auto}
.foot .vl{font-size:14px;color:var(--ink-2)}
.foot .vl b{color:var(--ink)}
"""

# ───────────────────────── обложка: полоса прибавки ─────────────────────────
assert A_WORDS + B_EST + REST == STEP_NEW, "три части складываются в прибавку уровня"
PARTS = [
    ("Том " + VOL_A[0], A_WORDS, "подтверждено", "p1"),
    ("Том " + VOL_B[0], B_EST, "оценка", "p2"),
    ("Добор сверх книг", REST, "расчёт", "p3"),
]
seg = ""
for name, val, st, cls in PARTS:
    w = round(100.0 * val / STEP_NEW, 2)
    seg += ('<div class="sg ' + cls + '" style="flex:0 0 ' + str(w) + '%">'
            '<s>' + st + '</s><b>' + str(val) + '</b><i>' + name + '</i></div>')
assert seg.count('class="sg') == 3

HERO_CSS = BASE + """
html,body{width:1200px;height:630px}
.card{width:1200px;height:630px;padding:26px 48px 22px 64px}
.head{display:flex;justify-content:space-between;align-items:flex-end;gap:30px;margin-bottom:22px}
h1{font-size:40px;max-width:24ch}
.tip{flex:0 0 330px}
.stage{flex:1 1 auto;display:flex;flex-direction:column;justify-content:center}
.scale{display:flex;align-items:stretch;height:210px;border-radius:16px;overflow:hidden;
 border:1px solid var(--brick)}
.sg{display:flex;flex-direction:column;justify-content:center;padding:0 22px;min-width:0}
.sg.p1{background:var(--brick);color:#fff}
.sg.p2{background:var(--brick-soft)}
.sg.p3{background:repeating-linear-gradient(135deg,transparent,transparent 9px,
 rgba(154,146,137,.18) 9px,rgba(154,146,137,.18) 18px);border-left:1px dashed var(--grey)}
.sg s{display:block;text-decoration:none;font-size:11px;font-weight:700;letter-spacing:.11em;
 text-transform:uppercase;margin-bottom:8px;color:var(--brick)}
.sg.p1 s{color:#fff;opacity:.85}
.sg.p3 s{color:var(--grey)}
.sg b{display:block;font-size:44px;font-weight:700;line-height:1;margin-bottom:8px;
 color:var(--ink)}
.sg.p1 b{color:#fff}
.sg.p3 b{color:var(--taupe)}
.sg i{font-style:normal;font-size:15px;color:var(--ink-2);line-height:1.3}
.sg.p1 i{color:#fff;opacity:.9}
.sg.p3 i{color:var(--taupe)}
.axis{display:flex;justify-content:space-between;margin-top:12px;font-size:13.5px;
 color:var(--taupe)}
.axis b{color:var(--ink)}
"""

hero = ('<!DOCTYPE html><html lang="ru"><head><meta charset="utf-8">' + FONTS
        + "<style>" + VARS + HERO_CSS + "</style></head><body><div class=\"card\">"
        + '<div class="head"><div>'
        + '<div class="eyebrow">Учебник четвёртого уровня</div>'
        + '<h1>Одна книга — <i>меньше трети уровня</i></h1></div>'
        + '<div class="tip"><b>Это прибавка на уровне.</b> К концу четвёртого уровня нужно '
        + str(LEVEL_NEW) + ' слов накопительно</div></div>'
        + '<div class="stage"><div class="scale">' + seg + '</div>'
        + '<div class="axis"><span>прибавка четвёртого уровня — <b>' + str(STEP_NEW)
        + ' слов</b></span><span>две книги дают <b>' + str(BOTH_SHARE) + ' %</b></span></div>'
        + '</div>'
        + '<div class="foot"><span class="lb">Ученику нужно</span>'
        + '<span class="vl"><b>' + str(BOOKS_STUDENT) + ' книги</b>: учебник и тетрадь '
          'каждого тома</span>'
        + '<span class="lb">Статус</span>'
        + '<span class="vl">второй том — оценка, добор — расчёт</span></div>'
        + "</div></body></html>")

# ───────────────────────── инфографика: объявление против книги ──────────────
ROWS = [
    ("«Учебник HSK 4»", "может быть первой или второй книгой уровня"),
    ("«Полный курс уровня»", "в томе около " + str(A_WORDS) + " слов из "
     + str(STEP_NEW) + ", которые добавляет уровень"),
    ("«Всё для подготовки»", "записи сделаны к урокам книги, а не к заданиям экзамена"),
]
rows = ""
for left, right in ROWS:
    rows += ('<div class="rw"><div class="ad">' + left + '</div>'
             '<div class="ar"></div><div class="re">' + right + '</div></div>')
assert rows.count('class="rw"') == 3

FIG_CSS = BASE + """
html,body{width:1200px;height:470px}
.card{width:1200px;height:470px;padding:26px 48px 22px 64px}
.head{display:flex;justify-content:space-between;align-items:flex-end;gap:30px;margin-bottom:18px}
h1{font-size:34px;max-width:24ch}
.tip{flex:0 0 330px}
.cols{display:flex;gap:16px;margin-bottom:10px;font-size:12px;font-weight:700;
 letter-spacing:.11em;text-transform:uppercase;color:var(--taupe)}
.cols span:first-child{flex:0 0 330px}
.cols span:last-child{flex:1 1 0;padding-left:60px}
.list{flex:1 1 auto;display:flex;flex-direction:column;justify-content:center;gap:12px}
.rw{display:flex;align-items:center;gap:16px}
.ad{flex:0 0 330px;background:var(--surface);border:1px dashed var(--grey);border-radius:12px;
 padding:14px 16px;font-size:17px;color:var(--taupe);line-height:1.25}
.ar{flex:0 0 44px;height:2px;background:var(--brick);position:relative}
.ar:after{content:"";position:absolute;right:0;top:-5px;border-left:11px solid var(--brick);
 border-top:6px solid transparent;border-bottom:6px solid transparent}
.re{flex:1 1 0;background:var(--brick-soft);border:1px solid var(--brick);border-radius:12px;
 padding:14px 18px;font-size:16px;color:var(--ink);line-height:1.3}
"""

fig = ('<!DOCTYPE html><html lang="ru"><head><meta charset="utf-8">' + FONTS
       + "<style>" + VARS + FIG_CSS + "</style></head><body><div class=\"card\">"
       + '<div class="head"><div>'
       + '<div class="eyebrow">Объявление и книга</div>'
       + '<h1>Что написано <i>и что это значит</i></h1></div>'
       + '<div class="tip"><b>Проверяется за минуту.</b> Буква на обложке, число уроков '
         'и список слов уровня</div></div>'
       + '<div class="cols"><span>в объявлении</span><span>на самом деле</span></div>'
       + '<div class="list">' + rows + '</div>'
       + '<div class="foot"><span class="lb">Добор</span>'
       + '<span class="vl">около <b>' + str(REST) + ' слов</b> сверх двух книг</span>'
       + '<span class="lb">Одна книга</span>'
       + '<span class="vl"><b>' + str(A_SHARE) + ' %</b> прибавки уровня</span></div>'
       + "</div></body></html>")

open(S + "uch4-hero.html", "w", encoding="utf-8").write(hero)
open(S + "uch4-info.html", "w", encoding="utf-8").write(fig)
print("готово: uch4-hero.html, uch4-info.html")
