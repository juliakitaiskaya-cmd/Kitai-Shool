# -*- coding: utf-8 -*-
# Картинки к статье «Скачать учебник HSK 4»
# Обложка     — две книжные полки: у прежней серии четыре корешка,
#               у новой два корешка и два пустых места на месте тетрадей
# Инфографика — лестница запроса из трёх сужающихся ступеней: 4 → 2 → 0
import sys
sys.path.insert(0, "/home/user/Kitai-Shool/content")
from skach4 import (STEPS, OLD_FOR_PUPIL, NEW_TEXTBOOKS, NEW_SERIES, OLD_SERIES,
                    VOL_A, VOL_B, WB_LEVELS)

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

# ───────────────────────── обложка: две полки с корешками ─────────────────────
# корешок: (подпись сверху, том, есть ли книга)
OLD_SPINES = [("Учебник", VOL_A, True), ("Тетрадь", VOL_A, True),
              ("Учебник", VOL_B, True), ("Тетрадь", VOL_B, True)]
NEW_SPINES = [("Учебник", VOL_A, True), ("Тетрадь", VOL_A, False),
              ("Учебник", VOL_B, True), ("Тетрадь", VOL_B, False)]
assert sum(1 for a, b, c in OLD_SPINES if c) == OLD_FOR_PUPIL
assert sum(1 for a, b, c in NEW_SPINES if c) == NEW_TEXTBOOKS


def shelf(name, note, spines, count):
    sp = ""
    for kind, vol, has in spines:
        if has:
            sp += ('<div class="sp"><span class="k">' + kind + '</span>'
                   '<span class="v">' + vol + '</span></div>')
        else:
            sp += ('<div class="sp gap"><span class="k">' + kind + '</span>'
                   '<span class="v">нет</span></div>')
    return ('<div class="shelf"><div class="sh-head"><div class="sh-n">' + name + '</div>'
            '<div class="sh-cnt">' + str(count) + '</div>'
            '<div class="sh-cl">книги ученику</div>'
            '<div class="sh-note">' + note + '</div></div>'
            '<div class="spines">' + sp + '</div><div class="board"></div></div>')


shelves = (shelf(OLD_SERIES, "прежний стандарт, комплект полный",
                 OLD_SPINES, OLD_FOR_PUPIL)
           + shelf(NEW_SERIES, "новый стандарт, тетрадей нет",
                   NEW_SPINES, NEW_TEXTBOOKS))
assert shelves.count('class="shelf"') == 2
assert shelves.count("gap") == 2, "два пустых места — на месте тетрадей"

HERO_CSS = BASE + """
html,body{width:1200px;height:630px}
.card{width:1200px;height:630px;padding:24px 48px 20px 64px}
.head{display:flex;justify-content:space-between;align-items:flex-end;gap:30px;margin-bottom:14px}
h1{font-size:40px;max-width:22ch}
.tip{flex:0 0 340px}
.shelves{flex:1 1 auto;display:flex;flex-direction:column;justify-content:center;gap:22px}
.shelf{display:flex;flex-direction:column}
.sh-head{display:flex;align-items:baseline;gap:12px;margin-bottom:8px}
.sh-n{font-size:18px;font-weight:700;color:var(--ink)}
.sh-note{font-size:14px;color:var(--taupe)}
.sh-cnt{font-size:26px;font-weight:700;color:var(--brick);margin-left:6px}
.sh-cl{font-size:13px;color:var(--taupe);margin-right:10px}
.spines{display:flex;align-items:flex-end;gap:14px;height:116px}
.sp{flex:0 0 180px;height:116px;border-radius:7px 7px 0 0;background:var(--brick);
 border:1px solid var(--brick-d);display:flex;flex-direction:column;justify-content:center;
 align-items:center;gap:5px;color:#fff}
.sp .k{font-size:13.5px;font-weight:600;letter-spacing:.03em}
.sp .v{font-size:21px;font-weight:700}
.sp.gap{background:transparent;border:2px dashed var(--grey);height:92px}
.sp.gap .k{color:var(--taupe)}
.sp.gap .v{color:var(--grey);font-size:17px}
.board{height:9px;border-radius:4px;background:var(--cream-2);border:1px solid var(--hair);
 width:776px}
"""

hero = ('<!DOCTYPE html><html lang="ru"><head><meta charset="utf-8">' + FONTS
        + "<style>" + VARS + HERO_CSS + "</style></head><body><div class=\"card\">"
        + '<div class="head"><div>'
        + '<div class="eyebrow">Учебник четвёртого уровня</div>'
        + '<h1>За словом «учебник» <i>стоит не одна книга</i></h1></div>'
        + '<div class="tip"><b>Уровень идёт двумя томами.</b> У прежней серии к каждому '
          'тому есть тетрадь, у новой тетрадей нет ни к одному</div></div>'
        + '<div class="shelves">' + shelves + '</div>'
        + '<div class="foot"><span class="lb">Ученику на уровень</span>'
        + '<span class="vl"><b>' + str(OLD_FOR_PUPIL) + '</b> книги у прежней серии против '
        + '<b>' + str(NEW_TEXTBOOKS) + '</b> у новой</span>'
        + '<span class="lb">Тетради новой серии</span>'
        + '<span class="vl">изданы для уровней '
        + " и ".join(str(x) for x in WB_LEVELS) + ', выше — нет</span></div>'
        + "</div></body></html>")

# ───────────────────────── инфографика: лестница запроса ─────────────────────
WIDE, NARROW = 1010, 720
steps_html = ""
for i, (name, what, n, why) in enumerate(STEPS):
    w = WIDE - (WIDE - NARROW) * i // (len(STEPS) - 1)
    cls = " zero" if n == 0 else ""
    steps_html += ('<div class="st' + cls + '" style="width:' + str(w) + 'px">'
                   '<div class="num">' + str(n) + '</div>'
                   '<div class="txt"><div class="nm">' + name + '</div>'
                   '<div class="wt">' + what + '</div></div>'
                   '<div class="why">' + why + '</div></div>')
assert steps_html.count('class="st') == 3 and steps_html.count("zero") == 1

FIG_CSS = BASE + """
html,body{width:1200px;height:490px}
.card{width:1200px;height:490px;padding:24px 48px 20px 64px}
.head{display:flex;justify-content:space-between;align-items:flex-end;gap:30px;margin-bottom:14px}
h1{font-size:34px;max-width:24ch}
.tip{flex:0 0 330px}
.ladder{flex:1 1 auto;display:flex;flex-direction:column;justify-content:center;gap:11px}
.st{display:flex;align-items:center;gap:16px;background:var(--surface);
 border:1px solid var(--hair);border-left:5px solid var(--brick);border-radius:13px;
 padding:13px 18px}
.st.zero{border-left-color:var(--grey);border-style:dashed;background:transparent}
.num{flex:0 0 52px;height:52px;border-radius:12px;background:var(--brick);color:#fff;
 font-size:26px;font-weight:700;display:flex;align-items:center;justify-content:center}
.st.zero .num{background:var(--grey-soft);color:var(--taupe)}
.txt{flex:0 0 320px}
.nm{font-size:12.5px;font-weight:700;letter-spacing:.09em;text-transform:uppercase;
 color:var(--taupe);margin-bottom:3px}
.wt{font-size:16px;font-weight:600;color:var(--ink);line-height:1.25}
.why{flex:1 1 0;min-width:0;font-size:14px;color:var(--ink-2);line-height:1.34}
"""

fig = ('<!DOCTYPE html><html lang="ru"><head><meta charset="utf-8">' + FONTS
       + "<style>" + VARS + FIG_CSS + "</style></head><body><div class=\"card\">"
       + '<div class="head"><div>'
       + '<div class="eyebrow">Запрос и действительность</div>'
       + '<h1>Ищут четыре книги, <i>а в цифре нет ни одной</i></h1></div>'
       + '<div class="tip"><b>Цифра в кружке — сколько книг.</b> Лестница сужается на '
         'каждой ступени</div></div>'
       + '<div class="ladder">' + steps_html + '</div>'
       + '<div class="foot"><span class="lb">Что выдают официально</span>'
       + '<span class="vl">звук к урокам по коду из книги</span>'
       + '<span class="lb">Что лежит открыто</span>'
       + '<span class="vl">словник уровня и образцы заданий</span></div>'
       + "</div></body></html>")

open(S + "sk4-hero.html", "w", encoding="utf-8").write(hero)
open(S + "sk4-info.html", "w", encoding="utf-8").write(fig)
print("готово: sk4-hero.html, sk4-info.html")
