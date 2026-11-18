# -*- coding: utf-8 -*-
# Картинки к статье «Слова HSK 1»
# Обложка     — алфавитная лента словника и под ней чужая тематическая разбивка
# Инфографика — круги, площадь которых пропорциональна числам уровня
import math
import sys
sys.path.insert(0, "/home/user/Kitai-Shool/content")
from slova1 import WORDS, CHARS_READ, GRAMMAR, OLD_WORDS, GAP, RATIO, ORDER

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

# ───────────────────── обложка: лента против разбивки ─────────────────────
LETTERS = ["A", "B", "C", "D", "E", "F", "G", "H", "J", "K", "L", "M",
           "N", "P", "Q", "R", "S", "T", "W", "X", "Y", "Z"]
band = "".join('<div class="cell">' + c + "</div>" for c in LETTERS)
assert band.count('class="cell"') == len(LETTERS) == 22

# чужая разбивка: группы разного размера, числа — доли ленты, а не слова словника
GROUPS = [("Семья", 3), ("Еда", 4), ("Числа", 3), ("Время", 4),
          ("Места", 3), ("Глаголы", 5)]
assert sum(w for n, w in GROUPS) == 22, "группы покрывают ту же ленту целиком"
cuts = "".join('<div class="grp" style="flex:' + str(w) + ' 1 0"><span>' + n
               + '</span></div>' for n, w in GROUPS)
assert cuts.count('class="grp"') == 6

HERO_CSS = BASE + """
html,body{width:1200px;height:630px}
.card{width:1200px;height:630px;padding:26px 48px 20px 64px}
.head{display:flex;justify-content:space-between;align-items:flex-end;gap:30px;margin-bottom:18px}
h1{font-size:40px;max-width:22ch}
.tip{flex:0 0 340px}
.zone{flex:1 1 auto;display:flex;flex-direction:column;justify-content:center;gap:16px}
.arrow{display:flex;align-items:center;gap:12px;color:var(--taupe);font-size:14px}
.arrow:before,.arrow:after{content:"";flex:1 1 0;height:1px;background:var(--hair)}
.lb-row{font-size:12.5px;font-weight:700;letter-spacing:.11em;text-transform:uppercase;
 color:var(--taupe);margin-bottom:9px}
.lb-row b{color:var(--brick)}
.band{display:flex;gap:5px}
.cell{flex:1 1 0;height:92px;border-radius:8px;background:var(--brick);color:#fff;
 display:flex;align-items:center;justify-content:center;font-size:19px;font-weight:700}
.cuts{display:flex;gap:9px}
.grp{height:92px;border-radius:10px;border:2px dashed var(--grey);background:transparent;
 display:flex;flex-direction:column;align-items:center;justify-content:center;gap:3px}
.grp span{font-size:16px;font-weight:600;color:var(--ink-2)}
.grp i{font-style:normal;font-size:12.5px;color:var(--taupe)}
"""

hero = ('<!DOCTYPE html><html lang="ru"><head><meta charset="utf-8">' + FONTS
        + "<style>" + VARS + HERO_CSS + "</style></head><body><div class=\"card\">"
        + '<div class="head"><div>'
        + '<div class="eyebrow">Лексика первого уровня</div>'
        + '<h1>В словнике слова стоят <i>по алфавиту, а не по темам</i></h1></div>'
        + '<div class="tip"><b>Тематический список — чужая разбивка.</b> У одного '
          'составителя тем двенадцать, у другого восемь, и ни одна не обязательна</div></div>'
        + '<div class="zone">'
        + '<div><div class="lb-row">Как устроен словник: <b>' + ORDER + '</b></div>'
        + '<div class="band">' + band + '</div></div>'
        + '<div class="arrow">одни и те же триста слов, разложенные по-чужому</div>'
        + '<div><div class="lb-row">Как режут список составители подборок</div>'
        + '<div class="cuts">' + cuts + '</div></div>'
        + '</div>'
        + '<div class="foot"><span class="lb">На уровне</span>'
        + '<span class="vl"><b>' + str(WORDS) + '</b> слов по действующему стандарту против '
        + str(OLD_WORDS) + ' по прежнему</span>'
        + '<span class="lb">Тем в словнике</span>'
        + '<span class="vl">ни одной</span></div>'
        + "</div></body></html>")

# ───────────────────── инфографика: круги по площади ─────────────────────
BIG = 230.0                      # диаметр самого большого круга
root = math.sqrt(float(WORDS))
CIRCLES = [
    (WORDS, "слов", "в словнике уровня", True),
    (CHARS_READ, "знаков", "для узнавания", True),
    (GRAMMAR, "пунктов", "грамматики уровня", True),
]
balls = ""
for n, unit, why, solid in CIRCLES:
    d = int(round(BIG * math.sqrt(float(n)) / root))
    balls += ('<div class="ball"><div class="disc" style="width:' + str(d) + 'px;height:'
              + str(d) + 'px"><b>' + str(n) + '</b><span>' + unit + '</span></div>'
              '<div class="cap">' + why + '</div></div>')
balls += ('<div class="ball"><div class="disc dash" style="width:110px;height:110px">'
          '<b>—</b><span>знаков</span></div>'
          '<div class="cap">для письма от руки: числа нет</div></div>')
assert balls.count('class="ball"') == 4 and balls.count("dash") == 1

FIG_CSS = BASE + """
html,body{width:1200px;height:470px}
.card{width:1200px;height:470px;padding:24px 48px 18px 64px}
.head{display:flex;justify-content:space-between;align-items:flex-end;gap:30px;margin-bottom:10px}
h1{font-size:34px;max-width:24ch}
.tip{flex:0 0 330px}
.balls{flex:1 1 auto;display:flex;align-items:flex-end;justify-content:space-around;gap:18px;padding-bottom:4px}
.ball{display:flex;flex-direction:column;align-items:center;justify-content:flex-end;gap:9px;height:100%}
.disc{border-radius:50%;background:var(--brick);color:#fff;display:flex;flex-direction:column;
 align-items:center;justify-content:center;gap:1px}
.disc b{font-size:34px;font-weight:700;line-height:1}
.disc span{font-size:13px;font-weight:600;opacity:.92}
.disc.dash{background:transparent;border:2px dashed var(--grey);color:var(--taupe)}
.disc.dash b{font-size:30px}
.cap{font-size:14px;color:var(--ink-2);text-align:center;max-width:200px;line-height:1.3}
"""

fig = ('<!DOCTYPE html><html lang="ru"><head><meta charset="utf-8">' + FONTS
       + "<style>" + VARS + FIG_CSS + "</style></head><body><div class=\"card\">"
       + '<div class="head"><div>'
       + '<div class="eyebrow">Что входит в первый уровень</div>'
       + '<h1>Слов больше, чем знаков, <i>всего на ' + str(GAP) + '</i></h1></div>'
       + '<div class="tip"><b>Площадь круга — величина числа.</b> На первом уровне слово '
         'и знак почти совпадают</div></div>'
       + '<div class="balls">' + balls + '</div>'
       + '<div class="foot"><span class="lb">Расчёт</span>'
       + '<span class="vl">около <b>' + str(RATIO).replace(".", ",")
       + '</b> слова на один знак</span>'
       + '<span class="lb">Знаки для письма</span>'
       + '<span class="vl">источники расходятся, число не называем</span></div>'
       + "</div></body></html>")

open(S + "sl1-hero.html", "w", encoding="utf-8").write(hero)
open(S + "sl1-info.html", "w", encoding="utf-8").write(fig)
print("готово: sl1-hero.html, sl1-info.html")
