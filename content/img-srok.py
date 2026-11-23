# -*- coding: utf-8 -*-
# Картинки к статье «Сколько готовиться к HSK»
# Обложка     — один вопрос и два разных ответа
# Инфографика — треугольная матрица «откуда → куда»: сколько слов выучить
import sys
sys.path.insert(0, "/home/user/Kitai-Shool/content")
from srok import NEW, gap, TIMES_3

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
.foot{display:flex;align-items:center;gap:14px;margin-top:auto;border-top:1px solid var(--hair);
 padding-top:12px}
.foot .lb{font-size:12px;font-weight:700;letter-spacing:.11em;text-transform:uppercase;
 color:var(--taupe);flex:0 0 auto}
.foot .vl{font-size:14px;color:var(--ink-2)}
.foot .vl b{color:var(--ink)}
"""

# ───────────────────── обложка: один вопрос, два ответа ─────────────────────
A_FROM2, A_FROM0 = gap(2, 3), gap(0, 3)
assert A_FROM0 == A_FROM2 * 2, "ответы отличаются ровно вдвое"

ANSWERS = [
    ("Если сдан HSK 2", A_FROM2, "выучить 500 слов", "это прибавка одного уровня"),
    ("Если начинаете с нуля", A_FROM0, "выучить 1000 слов",
     "плюс пиньинь, тоны и первые иероглифы"),
]


def ans(head, n, line, note, big):
    return ('<div class="ans' + (" big" if big else "") + '">'
            '<div class="ah">' + head + '</div>'
            '<div class="anum"><div class="an">' + str(n) + '</div>'
            '<div class="aw">слов, которые вас разделяют</div></div>'
            '<div class="at">' + note + "</div></div>")


HERO_CSS = BASE + """
html,body{width:1200px;height:630px}
.card{width:1200px;height:630px;padding:30px 48px 20px 64px}
h1{font-size:44px;max-width:31ch;margin-bottom:6px}
.sub{font-size:17px;color:var(--ink-2);margin-bottom:22px}
.row{flex:1 1 auto;display:flex;align-items:stretch;gap:24px}
.ans{flex:1 1 0;background:var(--surface);border:1px solid var(--hair);border-radius:16px;
 padding:20px 24px 18px;display:flex;flex-direction:column;justify-content:space-between;
 border-top:5px solid var(--grey)}
.ans.big{border-top-color:var(--brick)}
.ah{font-size:17px;font-weight:700;color:var(--taupe);letter-spacing:.04em;
 text-transform:uppercase}
.an{font-family:'Inter',sans-serif;font-size:84px;font-weight:700;line-height:1;
 letter-spacing:-2px;color:var(--ink)}
.ans.big .an{color:var(--brick)}
.anum{}
.aw{font-size:17px;color:var(--ink-2);margin-top:2px}
.at{font-size:15px;color:var(--ink-2);line-height:1.35;padding-top:14px;
 border-top:1px solid var(--hair)}
.vs{flex:0 0 58px;display:flex;align-items:center;justify-content:center;
 font-size:19px;font-weight:700;color:var(--taupe);letter-spacing:.06em}
"""

hero = ('<!DOCTYPE html><html lang="ru"><head><meta charset="utf-8">' + FONTS
        + "<style>" + VARS + HERO_CSS + "</style></head><body><div class=\"card\">"
        + '<div class="eyebrow">Сколько готовиться к HSK</div>'
        + '<h1>Один и тот же HSK 3 — <i>это два разных ответа</i></h1>'
        + '<div class="sub">Срок считается не до уровня, а от того уровня, '
          'который у вас уже есть</div>'
        + '<div class="row">'
        + ans(ANSWERS[0][0], ANSWERS[0][1], ANSWERS[0][2], ANSWERS[0][3], False)
        + '<div class="vs">вдвое</div>'
        + ans(ANSWERS[1][0], ANSWERS[1][1], ANSWERS[1][2], ANSWERS[1][3], True)
        + '</div>'
        + '<div class="foot"><span class="lb">Вывод</span>'
        + '<span class="vl">вопрос «сколько готовиться» <b>без второго числа ответа '
          'не имеет</b></span>'
        + '<span class="lb">Расчёт</span>'
        + '<span class="vl">по словнику действующего стандарта</span></div>'
        + "</div></body></html>")

# ───────────────────── инфографика: матрица «откуда → куда» ─────────────────
ROWS = [0, 1, 2, 3, 4]
COLS = [1, 2, 3, 4, 5]
NAMES = {0: "с нуля", 1: "HSK 1", 2: "HSK 2", 3: "HSK 3", 4: "HSK 4"}

head_cells = "".join('<div class="hc">до HSK ' + str(c) + "</div>" for c in COLS)
grid = ""
for a in ROWS:
    grid += '<div class="rh">' + NAMES[a] + "</div>"
    for b in COLS:
        if b <= a:
            grid += '<div class="cell empty">—</div>'
            continue
        cls = "cell"
        if b == a + 1:
            cls += " diag"
        if b in (3, 4):
            cls += " col"
        grid += '<div class="' + cls + '">' + str(gap(a, b)) + "</div>"
assert grid.count('class="cell') == 25

FIG_CSS = BASE + """
html,body{width:1200px;height:520px}
.card{width:1200px;height:520px;padding:22px 48px 14px 64px}
.head{display:flex;justify-content:space-between;align-items:flex-start;gap:34px;
 margin-bottom:12px}
h1{font-size:30px;max-width:25ch}
.tip{background:var(--surface);border:1px solid var(--hair);border-left:4px solid var(--brick);
 border-radius:13px;padding:10px 15px;font-size:13px;color:var(--ink-2);line-height:1.33;
 flex:0 0 310px}
.tip b{color:var(--ink)}
.wrap{flex:1 1 auto;display:flex;gap:16px;align-items:flex-start}
.tbl{flex:1 1 auto}
.grid{display:grid;grid-template-columns:118px repeat(5,1fr);gap:6px}
.hc{font-size:13.5px;font-weight:700;color:var(--taupe);text-transform:uppercase;
 letter-spacing:.05em;text-align:center;padding-bottom:4px}
.corner{}
.rh{font-size:15px;font-weight:700;color:var(--ink-2);display:flex;align-items:center;
 padding-right:8px}
.cell{height:50px;border-radius:9px;display:flex;align-items:center;justify-content:center;
 font-size:19px;font-weight:600;color:var(--ink);background:var(--surface);
 border:1px solid var(--hair)}
.cell.empty{background:transparent;border-color:transparent;color:var(--hair)}
.cell.col{background:var(--brick-soft);border-color:#E8C3CF;color:var(--brick-d);
 font-weight:700}
.cell.col.diag{background:var(--brick);border-color:var(--brick-d);color:#fff}
.legend{flex:0 0 212px;display:flex;flex-direction:column;gap:9px;padding-top:26px}
.lg{display:flex;gap:9px;align-items:flex-start;font-size:12.5px;color:var(--ink-2);
 line-height:1.3}
.sw{flex:0 0 18px;height:18px;border-radius:5px;border:1px solid var(--hair);margin-top:1px}
.sw.a{background:var(--brick-soft);border-color:#E8C3CF}
.sw.b{background:var(--brick);border-color:var(--brick-d)}
.sw.c{background:var(--surface);border-color:var(--hair)}
"""

fig = ('<!DOCTYPE html><html lang="ru"><head><meta charset="utf-8">' + FONTS
       + "<style>" + VARS + FIG_CSS + "</style></head><body><div class=\"card\">"
       + '<div class="head"><div>'
       + '<div class="eyebrow">Пятнадцать переходов</div>'
       + '<h1>Сколько слов выучить, <i>чтобы дойти до цели</i></h1></div>'
       + '<div class="tip"><b>Слева — уровень, который у вас есть. Сверху — тот, '
         'который сдаёте.</b> В клетке число слов, которые вас разделяют</div></div>'
       + '<div class="wrap"><div class="tbl"><div class="grid">'
       + '<div class="corner"></div>' + head_cells + grid
       + '</div></div>'
       + '<div class="legend">'
       + '<div class="lg"><span class="sw a"></span><span>Два столбца, вокруг которых '
         'идёт вся статья: <b>до HSK 3</b> и <b>до HSK 4</b></span></div>'
       + '<div class="lg"><span class="sw b"></span><span>Переход на соседний уровень '
         'внутри этих столбцов</span></div>'
       + '<div class="lg"><span class="sw c"></span><span>Все остальные клетки '
         'таблицы</span></div>'
       + '<div class="lg"><span style="flex:0 0 18px"></span><span>По столбцу число '
         'меняется <b>вдвое</b> — цель без старта ничего не говорит</span></div>'
       + '</div></div>'
       + '<div class="foot"><span class="lb">Крайние значения</span>'
       + '<span class="vl"><b>' + str(gap(1, 2)) + '</b> и <b>' + str(gap(0, 5))
       + '</b> слов — между самым коротким и самым длинным переходом</span>'
       + '<span class="lb">Расчёт</span>'
       + '<span class="vl">вычитанием по словнику действующего стандарта</span></div>'
       + "</div></body></html>")

open(S + "srk-hero.html", "w", encoding="utf-8").write(hero)
open(S + "srk-info.html", "w", encoding="utf-8").write(fig)
print("готово: srk-hero.html, srk-info.html")
