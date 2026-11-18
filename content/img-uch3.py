# -*- coding: utf-8 -*-
# Картинки к статье «Учебник HSK 3»
# Обложка     — три столбика прибавки по уровням: третий равен сумме первых двух
# Инфографика — матрица: что проверяет экзамен и есть ли это в комплекте тома
import sys
sys.path.insert(0, "/home/user/Kitai-Shool/content")
from uch3 import (MATRIX, STEP_NEW, STEP_OLD, SCALE, TWO_FIRST, LESSONS, LESSONS_FIRST,
                  REST, COVER, SWITCH)

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

# ───────────────────────── обложка: столбики прибавки ─────────────────────────
assert STEP_NEW[3] == TWO_FIRST == STEP_NEW[1] + STEP_NEW[2]
MAXS = float(STEP_NEW[3])
HMAX = 300  # пикселей на самый высокий столбик

bars = ""
for lvl in (1, 2, 3):
    h = int(round(HMAX * STEP_NEW[lvl] / MAXS))
    cls = "b3" if lvl == 3 else ""
    bars += ('<div class="col"><div class="val">+' + str(STEP_NEW[lvl]) + '</div>'
             '<div class="bar ' + cls + '" style="height:' + str(h) + 'px"></div>'
             '<div class="lv">HSK ' + str(lvl) + '</div>'
             '<div class="tot">всего ' + str(SCALE[lvl][1]) + '</div></div>')
    if lvl == 1:
        bars += '<div class="op">+</div>'
    if lvl == 2:
        bars += '<div class="op">=</div>'
assert bars.count('class="col"') == 3 and bars.count('class="op"') == 2

HERO_CSS = BASE + """
html,body{width:1200px;height:630px}
.card{width:1200px;height:630px;padding:26px 48px 22px 64px}
.head{display:flex;justify-content:space-between;align-items:flex-end;gap:30px;margin-bottom:12px}
h1{font-size:40px;max-width:23ch}
.tip{flex:0 0 330px}
.chart{flex:1 1 auto;display:flex;align-items:flex-end;justify-content:flex-start;gap:44px;
 padding-bottom:6px}
.col{flex:0 0 250px;display:flex;flex-direction:column;align-items:center}
.val{font-size:30px;font-weight:700;color:var(--ink);margin-bottom:10px}
.bar{width:200px;border-radius:12px 12px 0 0;background:var(--brick-soft);
 border:1px solid var(--brick);border-bottom:none}
.bar.b3{background:var(--brick);border-color:var(--brick-d)}
.lv{margin-top:12px;font-size:19px;font-weight:700;color:var(--brick);
 border-top:2px solid var(--hair);padding-top:10px;width:100%;text-align:center}
.tot{font-size:13.5px;color:var(--taupe);margin-top:4px}
.op{flex:0 0 auto;font-size:40px;font-weight:700;color:var(--taupe);padding-bottom:70px}
"""

hero = ('<!DOCTYPE html><html lang="ru"><head><meta charset="utf-8">' + FONTS
        + "<style>" + VARS + HERO_CSS + "</style></head><body><div class=\"card\">"
        + '<div class="head"><div>'
        + '<div class="eyebrow">Учебник третьего уровня</div>'
        + '<h1>Третий уровень весит <i>как первые два вместе</i></h1></div>'
        + '<div class="tip"><b>Это прибавка на уровне</b>, а не весь словарь: '
          'к концу третьего уровня нужно ' + str(SCALE[3][1]) + ' слов</div></div>'
        + '<div class="chart">' + bars + '</div>'
        + '<div class="foot"><span class="lb">Расчёт</span>'
        + '<span class="vl">' + str(STEP_NEW[1]) + ' + ' + str(STEP_NEW[2]) + ' = <b>'
        + str(STEP_NEW[3]) + '</b>, по действующим накопительным шкалам</span>'
        + '<span class="lb">В томе</span>'
        + '<span class="vl">' + str(LESSONS) + ' уроков против ' + str(LESSONS_FIRST)
        + ' на первом уровне</span></div>'
        + "</div></body></html>")

# ───────────────────────── инфографика: матрица ─────────────────────────
rows = ""
for name, yes, why in MATRIX:
    rows += ('<div class="mr' + ("" if yes else " no") + '">'
             '<div class="nm">' + name + '</div>'
             '<div class="mk">' + ("есть в комплекте" if yes else "в комплекте нет") + '</div>'
             '<div class="wh">' + why + '</div></div>')
assert rows.count('class="mr') == 3 and rows.count("no") >= 1

FIG_CSS = BASE + """
html,body{width:1200px;height:440px}
.card{width:1200px;height:440px;padding:26px 48px 22px 64px}
.head{display:flex;justify-content:space-between;align-items:flex-end;gap:30px;margin-bottom:16px}
h1{font-size:34px;max-width:25ch}
.tip{flex:0 0 330px}
.grid{flex:1 1 auto;display:flex;flex-direction:column;justify-content:center;gap:12px}
.mr{display:flex;align-items:center;gap:16px;background:var(--surface);
 border:1px solid var(--hair);border-left:5px solid var(--brick);border-radius:13px;
 padding:15px 18px}
.mr.no{border-left-color:var(--grey);border-style:dashed;background:transparent}
.nm{flex:0 0 340px;font-size:19px;font-weight:600;color:var(--ink);line-height:1.2}
.mr.no .nm{color:var(--taupe)}
.mk{flex:0 0 190px;font-size:12.5px;font-weight:700;letter-spacing:.09em;text-transform:uppercase;
 color:#fff;background:var(--brick);border-radius:8px;padding:7px 12px;text-align:center}
.mr.no .mk{background:var(--grey-soft);color:var(--taupe)}
.wh{flex:1 1 0;font-size:15px;color:var(--ink-2);line-height:1.35}
"""

fig = ('<!DOCTYPE html><html lang="ru"><head><meta charset="utf-8">' + FONTS
       + "<style>" + VARS + FIG_CSS + "</style></head><body><div class=\"card\">"
       + '<div class="head"><div>'
       + '<div class="eyebrow">Книга и экзамен</div>'
       + '<h1>Два навыка из трёх <i>комплект закрывает</i></h1></div>'
       + '<div class="tip"><b>Третий не закрывает ни одна книга.</b> С ' + SWITCH
       + ' устная часть входит внутрь экзамена</div></div>'
       + '<div class="grid">' + rows + '</div>'
       + '<div class="foot"><span class="lb">Комплект тома</span>'
       + '<span class="vl">учебник, рабочая тетрадь и книга для преподавателя</span>'
       + '<span class="lb">Добор по словам</span>'
       + '<span class="vl">около <b>' + str(REST) + '</b> сверх книги</span></div>'
       + "</div></body></html>")

open(S + "uch3-hero.html", "w", encoding="utf-8").write(hero)
open(S + "uch3-info.html", "w", encoding="utf-8").write(fig)
print("готово: uch3-hero.html, uch3-info.html")
