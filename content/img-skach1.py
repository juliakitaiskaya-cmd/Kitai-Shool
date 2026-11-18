# -*- coding: utf-8 -*-
# Картинки к статье «Скачать учебник HSK 1»
# Обложка     — три карточки-вердикта: что ищут и есть ли это официально
# Инфографика — четыре строки того, что есть законно, с источником и статусом
import sys
sys.path.insert(0, "/home/user/Kitai-Shool/content")
from skach1 import WANTED, LEGAL, CONF, NOCONF, NO_COUNT, YES_COUNT

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

# ───────────────────────── обложка: три вердикта ─────────────────────────
cards = ""
for name, yes, why in WANTED:
    cards += ('<div class="vd' + ("" if yes else " no") + '">'
              '<div class="w">' + ("да" if yes else "нет") + '</div>'
              '<div class="nm">' + name + '</div>'
              '<div class="wh">' + why + '</div></div>')
assert cards.count('class="vd') == 3 and cards.count(">нет<") == NO_COUNT == 2

HERO_CSS = BASE + """
html,body{width:1200px;height:630px}
.card{width:1200px;height:630px;padding:26px 48px 22px 64px}
.head{display:flex;justify-content:space-between;align-items:flex-end;gap:30px;margin-bottom:22px}
h1{font-size:40px;max-width:23ch}
.tip{flex:0 0 330px}
.cards{flex:1 1 auto;display:flex;align-items:stretch;gap:18px}
.vd{flex:1 1 0;border-radius:16px;padding:22px 24px;display:flex;flex-direction:column;
 justify-content:center;border:1px solid var(--brick);background:var(--brick-soft)}
.vd.no{border:1px dashed var(--grey);background:transparent}
.w{font-family:'Cormorant Garamond',serif;font-size:58px;font-weight:700;line-height:1;
 color:var(--brick);margin-bottom:14px}
.vd.no .w{color:var(--grey)}
.nm{font-size:21px;font-weight:600;color:var(--ink);margin-bottom:10px;line-height:1.2}
.vd.no .nm{color:var(--taupe)}
.wh{font-size:14.5px;color:var(--ink-2);line-height:1.38}
.vd.no .wh{color:var(--taupe)}
"""

hero = ('<!DOCTYPE html><html lang="ru"><head><meta charset="utf-8">' + FONTS
        + "<style>" + VARS + HERO_CSS + "</style></head><body><div class=\"card\">"
        + '<div class="head"><div>'
        + '<div class="eyebrow">Скачать учебник первого уровня</div>'
        + '<h1>Из трёх вещей официально есть <i>одна</i></h1></div>'
        + '<div class="tip"><b>Так устроена вся серия.</b> Ответ одинаков для любого номера '
          'уровня на обложке</div></div>'
        + '<div class="cards">' + cards + '</div>'
        + '<div class="foot"><span class="lb">Что это значит</span>'
        + '<span class="vl">официального файла учебника <b>не существует</b> — ни платно, '
          'ни бесплатно</span>'
        + '<span class="lb">Звук</span>'
        + '<span class="vl">привязан к купленной книге</span></div>'
        + "</div></body></html>")

# ───────────────────────── инфографика: что есть законно ─────────────────────────
rows = ""
for i, (what, where, st) in enumerate(LEGAL, start=1):
    ok = st == CONF
    rows += ('<div class="lr' + ("" if ok else " soft") + '">'
             '<div class="n">' + str(i) + '</div>'
             '<div class="wt">' + what + '</div>'
             '<div class="wr">' + where + '</div>'
             '<div class="st">' + st + '</div></div>')
assert rows.count('class="lr') == 4 and rows.count("soft") == 1

FIG_CSS = BASE + """
html,body{width:1200px;height:510px}
.card{width:1200px;height:510px;padding:26px 48px 22px 64px}
.head{display:flex;justify-content:space-between;align-items:flex-end;gap:30px;margin-bottom:16px}
h1{font-size:34px;max-width:24ch}
.tip{flex:0 0 330px}
.list{flex:1 1 auto;display:flex;flex-direction:column;justify-content:center;gap:11px}
.lr{display:flex;align-items:center;gap:14px;background:var(--surface);
 border:1px solid var(--hair);border-left:5px solid var(--brick);border-radius:13px;
 padding:13px 16px}
.lr.soft{border-left-color:var(--grey);border-style:dashed}
.n{flex:0 0 30px;height:30px;border-radius:50%;background:var(--brick);color:#fff;
 font-size:14px;font-weight:700;display:flex;align-items:center;justify-content:center}
.lr.soft .n{background:var(--grey-soft);color:var(--taupe)}
.wt{flex:0 0 300px;font-size:18px;font-weight:600;color:var(--ink);line-height:1.2}
.lr.soft .wt{color:var(--taupe)}
.wr{flex:1 1 0;font-size:15px;color:var(--ink-2);line-height:1.3}
.st{flex:0 0 190px;font-size:11.5px;font-weight:700;letter-spacing:.09em;text-transform:uppercase;
 color:var(--brick);text-align:right}
.lr.soft .st{color:var(--grey)}
"""

fig = ('<!DOCTYPE html><html lang="ru"><head><meta charset="utf-8">' + FONTS
       + "<style>" + VARS + FIG_CSS + "</style></head><body><div class=\"card\">"
       + '<div class="head"><div>'
       + '<div class="eyebrow">Первый уровень</div>'
       + '<h1>Что есть <i>в электронном виде законно</i></h1></div>'
       + '<div class="tip"><b>Три строки проверены, четвёртая нет.</b> Про электронные '
         'издания на русском подтверждения у меня не нашлось</div></div>'
       + '<div class="list">' + rows + '</div>'
       + '<div class="foot"><span class="lb">Чего нет</span>'
       + '<span class="vl">учебника и рабочей тетради — <b>ни в каком виде</b></span>'
       + '<span class="lb">Без покупки</span>'
       + '<span class="vl">доступны словник и образцы заданий</span></div>'
       + "</div></body></html>")

open(S + "sk1-hero.html", "w", encoding="utf-8").write(hero)
open(S + "sk1-info.html", "w", encoding="utf-8").write(fig)
print("готово: sk1-hero.html, sk1-info.html")
