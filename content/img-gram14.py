# -*- coding: utf-8 -*-
# Картинки к статье «Что нужно знать для HSK 1–4»
# Обложка     — зеркальная диаграмма: слева прибавка слов, справа прибавка конструкций
# Инфографика — два ряда чисел грамматики по уровням и полоса расхождения
import sys
sys.path.insert(0, "/home/user/Kitai-Shool/content")
from gram14 import (GRAM_A, GRAM_B, CUM_A, CUM_B, WORDS, DIFF, COLLECTIONS,
                    SPREAD_TIMES)

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

# ───────────────────── обложка: зеркальная диаграмма ─────────────────────
WMAX = float(max(WORDS.values()))          # 1000
GMAX = WMAX                                 # шкала общая: так видна разница
SIDE = 400                                  # пикселей на самое длинное крыло

rows = ""
for l in (1, 2, 3, 4):
    wl = int(round(SIDE * WORDS[l] / WMAX))
    gl = int(round(SIDE * GRAM_A[l] / GMAX))
    rows += ('<div class="r">'
             '<div class="left"><span class="v">+' + str(WORDS[l]) + '</span>'
             '<div class="bar w" style="width:' + str(wl) + 'px"></div></div>'
             '<div class="lv">HSK ' + str(l) + '</div>'
             '<div class="right"><div class="bar g" style="width:' + str(gl) + 'px"></div>'
             '<span class="v">+' + str(GRAM_A[l]) + '</span></div>'
             '</div>')
assert rows.count('class="r"') == 4

HERO_CSS = BASE + """
html,body{width:1200px;height:630px}
.card{width:1200px;height:630px;padding:26px 48px 20px 64px}
.head{display:flex;justify-content:space-between;align-items:flex-end;gap:30px;margin-bottom:12px}
h1{font-size:40px;max-width:21ch}
.tip{flex:0 0 330px}
.cols{display:flex;align-items:center;margin-bottom:8px}
.cols .c{flex:1 1 0;font-size:12.5px;font-weight:700;letter-spacing:.11em;
 text-transform:uppercase;color:var(--taupe)}
.cols .c.l{text-align:right;padding-right:18px}
.cols .c.r{text-align:left;padding-left:18px}
.cols .c.m{flex:0 0 96px;text-align:center}
.chart{flex:1 1 auto;display:flex;flex-direction:column;justify-content:center;gap:16px}
.r{display:flex;align-items:center}
.left{flex:1 1 0;display:flex;align-items:center;justify-content:flex-end;gap:12px}
.right{flex:1 1 0;display:flex;align-items:center;justify-content:flex-start;gap:12px}
.lv{flex:0 0 96px;text-align:center;font-size:18px;font-weight:700;color:var(--brick)}
.bar{height:34px;border-radius:7px;min-width:22px}
.bar.w{background:var(--brick)}
.bar.g{background:#C9718A}
.v{font-size:19px;font-weight:700;color:var(--ink)}
"""

hero = ('<!DOCTYPE html><html lang="ru"><head><meta charset="utf-8">' + FONTS
        + "<style>" + VARS + HERO_CSS + "</style></head><body><div class=\"card\">"
        + '<div class="head"><div>'
        + '<div class="eyebrow">Требования уровней 1–4</div>'
        + '<h1>Словарь растёт вдвое, <i>грамматика стоит на месте</i></h1></div>'
        + '<div class="tip"><b>Шкала у обоих крыльев одна.</b> Поэтому и видно, насколько прибавка слов больше прибавки конструкций</div></div>'
        + '<div class="cols"><div class="c l">Новых слов</div>'
          '<div class="c m">Уровень</div>'
          '<div class="c r">Новых конструкций</div></div>'
        + '<div class="chart">' + rows + '</div>'
        + '<div class="foot"><span class="lb">На четвёртом уровне</span>'
        + '<span class="vl">слов вдвое больше, чем на третьем, конструкций — <b>'
        + str(GRAM_A[4]) + '</b> против <b>' + str(GRAM_A[3]) + '</b></span>'
        + '<span class="lb">Вывод</span>'
        + '<span class="vl">нагрузка уходит в лексику</span></div>'
        + "</div></body></html>")

# ───────────────────── инфографика: два ряда чисел ─────────────────────
grid = ""
for l in (1, 2, 3, 4):
    same = DIFF[l] == 0
    grid += ('<div class="gr' + (" same" if same else "") + '">'
             '<div class="lv">HSK ' + str(l) + '</div>'
             '<div class="cell"><b>+' + str(GRAM_A[l]) + '</b>'
             '<span>всего ' + str(CUM_A[l]) + '</span></div>'
             '<div class="gap">' + ("ряды совпали" if same
                                     else "разница " + str(DIFF[l])) + '</div>'
             '<div class="cell b"><b>+' + str(GRAM_B[l]) + '</b>'
             '<span>всего ' + str(CUM_B[l]) + '</span></div></div>')
assert grid.count('class="gr') == 4 and grid.count("same") == 1

FIG_CSS = BASE + """
html,body{width:1200px;height:500px}
.card{width:1200px;height:500px;padding:22px 48px 16px 64px}
.head{display:flex;justify-content:space-between;align-items:flex-end;gap:30px;margin-bottom:12px}
h1{font-size:34px;max-width:24ch}
.tip{flex:0 0 330px}
.hdr{display:flex;align-items:center;gap:12px;margin-bottom:8px}
.hdr div{font-size:12.5px;font-weight:700;letter-spacing:.11em;text-transform:uppercase;
 color:var(--taupe);text-align:center}
.hdr .h1x{flex:0 0 96px}
.hdr .h2x,.hdr .h4x{flex:0 0 210px}
.hdr .h3x{flex:1 1 0}
.table{flex:1 1 auto;display:flex;flex-direction:column;justify-content:center;gap:9px}
.gr{display:flex;align-items:center;gap:12px}
.lv{flex:0 0 96px;font-size:18px;font-weight:700;color:var(--brick);text-align:center}
.cell{flex:0 0 210px;background:var(--surface);border:1px solid var(--hair);
 border-left:4px solid var(--brick);border-radius:12px;padding:8px 14px;text-align:center}
.cell.b{border-left-color:#C9718A}
.cell b{display:block;font-size:24px;font-weight:700;color:var(--ink);line-height:1}
.cell span{display:block;font-size:13px;color:var(--taupe);margin-top:3px}
.gap{flex:1 1 0;text-align:center;font-size:14px;color:var(--ink-2);
 border-top:1px dashed var(--grey);border-bottom:1px dashed var(--grey);padding:7px 0}
.gr.same .gap{color:var(--brick);font-weight:600;border-color:var(--brick)}
"""

fig = ('<!DOCTYPE html><html lang="ru"><head><meta charset="utf-8">' + FONTS
       + "<style>" + VARS + FIG_CSS + "</style></head><body><div class=\"card\">"
       + '<div class="head"><div>'
       + '<div class="eyebrow">Грамматика по уровням</div>'
       + '<h1>Два ряда чисел, <i>и ни один не подтверждён</i></h1></div>'
       + '<div class="tip"><b>Расхождение — единицы пунктов.</b> Но единой версии нет, '
         'и выбирать между рядами не из чего</div></div>'
       + '<div class="hdr"><div class="h1x">Уровень</div><div class="h2x">Ряд A</div>'
         '<div class="h3x">Расхождение</div><div class="h4x">Ряд B</div></div>'
       + '<div class="table">' + grid + '</div>'
       + '<div class="foot"><span class="lb">Накопительно к HSK 4</span>'
       + '<span class="vl"><b>' + str(CUM_A[4]) + '</b> против <b>' + str(CUM_B[4])
       + '</b> пунктов</span>'
       + '<span class="lb">Сторонние сборники</span>'
       + '<span class="vl">от ' + str(min(COLLECTIONS)) + ' до ' + str(max(COLLECTIONS))
       + ' пунктов — разброс в ' + str(SPREAD_TIMES).replace(".", ",")
       + ' раза</span></div>'
       + "</div></body></html>")

open(S + "gr14-hero.html", "w", encoding="utf-8").write(hero)
open(S + "gr14-info.html", "w", encoding="utf-8").write(fig)
print("готово: gr14-hero.html, gr14-info.html")
