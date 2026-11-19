# -*- coding: utf-8 -*-
# Картинки к статье «Слова HSK 3»
# Обложка     — три линии, растущие по уровням: слова, знаки для чтения, знаки для письма
# Инфографика — две сетки по сто клеток: сколько новых знаков на сто новых слов
import sys
sys.path.insert(0, "/home/user/Kitai-Shool/content")
from slova3 import SCALE, W_NEW, R_NEW, PER_100, FIRST_RATIO, THIRD_RATIO, WRITE_FROM

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

# ───────────────────── обложка: три линии по уровням ─────────────────────
W, H = 980, 300                 # поле графика
PAD_L, PAD_B = 0, 0
MAXV = float(SCALE[3]["words"][1])      # 1000 — верх шкалы
SERIES = [
    ("Слова", [SCALE[l]["words"][1] for l in (1, 2, 3)], "solid"),
    ("Знаки читать", [SCALE[l]["read"][1] for l in (1, 2, 3)], "read"),
    ("Знаки писать", [SCALE[l]["write"][1] for l in (1, 2, 3)], "write"),
]
assert [s[1][-1] for s in SERIES] == [1000, 655, 250]


PADX, PADT = 22, 34


def pt(i, v):
    x = PADX + (W - 2 * PADX) * i / 2.0
    y = PADT + (H - PADT) - (H - PADT) * v / MAXV
    return x, y


svg = ['<svg width="%d" height="%d" viewBox="0 0 %d %d">' % (W, H + 8, W, H + 8)]
# горизонтальные направляющие
for frac in (0.25, 0.5, 0.75, 1.0):
    y = PADT + (H - PADT) - (H - PADT) * frac
    svg.append('<line x1="0" y1="%.1f" x2="%d" y2="%.1f" stroke="#EAE3D8" stroke-width="1"/>'
               % (y, W, y))
COLORS = {"solid": ("#A41E3A", "none", 4), "read": ("#C9718A", "none", 3),
          "write": ("#8B7D6B", "6 5", 3)}
for name, vals, kind in SERIES:
    col, dash, wd = COLORS[kind]
    idx = [i for i, v in enumerate(vals) if v > 0]
    pts = [pt(i, vals[i]) for i in idx]
    d = " ".join("%s%.1f,%.1f" % ("M" if i == 0 else "L", x, y)
                 for i, (x, y) in enumerate(pts))
    svg.append('<path d="%s" fill="none" stroke="%s" stroke-width="%d" '
               'stroke-linecap="round" stroke-linejoin="round"%s/>'
               % (d, col, wd, '' if dash == "none" else ' stroke-dasharray="%s"' % dash))
    for k, (x, y) in enumerate(pts):
        i = idx[k]
        svg.append('<circle cx="%.1f" cy="%.1f" r="7" fill="#fff" stroke="%s" '
                   'stroke-width="3"/>' % (x, y, col))
        anchor = "start" if i == 0 else ("end" if i == 2 else "middle")
        dx = 14 if i == 0 else (-14 if i == 2 else 0)
        dy = 26 if kind == "read" else -15      # подписи чтения уводим под точку
        svg.append('<text x="%.1f" y="%.1f" font-family="Inter" font-size="19" '
                   'font-weight="700" fill="%s" text-anchor="%s">%d</text>'
                   % (x + dx, y + dy, col, anchor, vals[i]))
svg.append("</svg>")
chart = "".join(svg)
assert chart.count("<path") == 3 and chart.count("<circle") == 8, chart.count("<circle")

legend = "".join('<div class="lg"><i class="sw %s"></i>%s</div>' % (k, n)
                 for n, v, k in SERIES)

HERO_CSS = BASE + """
html,body{width:1200px;height:630px}
.card{width:1200px;height:630px;padding:26px 48px 20px 64px}
.head{display:flex;justify-content:space-between;align-items:flex-end;gap:30px;margin-bottom:10px}
h1{font-size:40px;max-width:21ch}
.tip{flex:0 0 340px}
.plot{flex:1 1 auto;display:flex;flex-direction:column;justify-content:center}
.axis{display:flex;margin-top:8px}
.axis div{flex:1 1 0;font-size:17px;font-weight:700;color:var(--brick);text-align:center}
.axis div:first-child{text-align:left}
.axis div:last-child{text-align:right}
.legend{display:flex;gap:26px;margin-top:12px}
.lg{display:flex;align-items:center;gap:9px;font-size:14.5px;color:var(--ink-2)}
.sw{width:26px;height:4px;border-radius:2px;background:var(--brick)}
.sw.read{background:#C9718A}
.sw.write{background:var(--taupe);height:0;border-top:3px dashed var(--taupe)}
"""

hero = ('<!DOCTYPE html><html lang="ru"><head><meta charset="utf-8">' + FONTS
        + "<style>" + VARS + HERO_CSS + "</style></head><body><div class=\"card\">"
        + '<div class="head"><div>'
        + '<div class="eyebrow">Лексика третьего уровня</div>'
        + '<h1>На уровне не один список, <i>а три</i></h1></div>'
        + '<div class="tip"><b>Писать требуют не всё, что читать.</b> И начинается письмо '
          'не с первого уровня, а со второго</div></div>'
        + '<div class="plot">' + chart
        + '<div class="axis"><div>HSK 1</div><div>HSK 2</div><div>HSK 3</div></div>'
        + '<div class="legend">' + legend + '</div></div>'
        + '<div class="foot"><span class="lb">К концу третьего уровня</span>'
        + '<span class="vl"><b>' + str(SCALE[3]["words"][1]) + '</b> слов, <b>'
        + str(SCALE[3]["read"][1]) + '</b> знаков читать и <b>'
        + str(SCALE[3]["write"][1]) + '</b> писать</span>'
        + '<span class="lb">Письмо</span>'
        + '<span class="vl">начинается с HSK ' + str(WRITE_FROM) + '</span></div>'
        + "</div></body></html>")

# ───────────────────── инфографика: две сетки по сто клеток ─────────────────────
FIRST_100 = int(round(FIRST_RATIO * 100))
assert FIRST_100 == 82 and PER_100 == 57


def grid(filled, title, note, accent):
    cells = "".join('<i class="c' + (" on" if k < filled else "") + '"></i>'
                    for k in range(100))
    return ('<div class="gbox"><div class="gt"><b>' + title + '</b><span>' + note
            + '</span></div><div class="grid ' + accent + '">' + cells + '</div>'
            '<div class="gn"><b>' + str(filled) + '</b> новых знаков на сто новых слов'
            '</div></div>')


grids = (grid(FIRST_100, "HSK 1", "почти каждое слово приносит новый знак", "a")
         + grid(PER_100, "HSK 3", "новых знаков заметно меньше", "b"))
assert grids.count('class="gbox"') == 2 and grids.count('class="c') == 200

FIG_CSS = BASE + """
html,body{width:1200px;height:490px}
.card{width:1200px;height:490px;padding:24px 48px 18px 64px}
.head{display:flex;justify-content:space-between;align-items:flex-end;gap:30px;margin-bottom:14px}
h1{font-size:34px;max-width:24ch}
.tip{flex:0 0 330px}
.grids{flex:1 1 auto;display:flex;align-items:center;justify-content:space-around;gap:40px}
.gbox{display:flex;flex-direction:column;gap:10px}
.gt{display:flex;align-items:baseline;gap:12px}
.gt b{font-size:20px;color:var(--brick)}
.gt span{font-size:14px;color:var(--taupe)}
.grid{display:grid;grid-template-columns:repeat(10,17px);gap:4px}
.c{width:17px;height:17px;border-radius:4px;background:var(--grey-soft);display:block}
.grid.a .c.on{background:#C9718A}
.grid.b .c.on{background:var(--brick)}
.gn{font-size:15px;color:var(--ink-2)}
.gn b{color:var(--ink);font-size:17px}
"""

fig = ('<!DOCTYPE html><html lang="ru"><head><meta charset="utf-8">' + FONTS
       + "<style>" + VARS + FIG_CSS + "</style></head><body><div class=\"card\">"
       + '<div class="head"><div>'
       + '<div class="eyebrow">Почему слова кажутся сложнее</div>'
       + '<h1>Новых знаков всё меньше, <i>новых слов всё больше</i></h1></div>'
       + '<div class="tip"><b>Клетка — один новый знак.</b> Чем их меньше, тем чаще '
         'новое слово собрано из знакомого</div></div>'
       + '<div class="grids">' + grids + '</div>'
       + '<div class="foot"><span class="lb">На третьем уровне</span>'
       + '<span class="vl"><b>' + str(R_NEW) + '</b> новых знаков на <b>' + str(W_NEW)
       + '</b> новых слов</span>'
       + '<span class="lb">Вывод</span>'
       + '<span class="vl">подсказки от знака почти нет</span></div>'
       + "</div></body></html>")

open(S + "sl3-hero.html", "w", encoding="utf-8").write(hero)
open(S + "sl3-info.html", "w", encoding="utf-8").write(fig)
print("готово: sl3-hero.html, sl3-info.html")
