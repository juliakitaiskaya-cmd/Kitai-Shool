# -*- coding: utf-8 -*-
# Картинки к статье «Скачать учебник HSK 2»
# Обложка     — две книжные карточки рядом: прежняя серия и новая
# Инфографика — три строки: что из материалов бывает в электронном виде
import sys
sys.path.insert(0, "/home/user/Kitai-Shool/content")
from skach2 import (EDITIONS, DIGITAL, NEW_SERIES, NEW_SERIES_CN, OLD_SERIES, CONF, DESCR)

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

# ───────────────────────── обложка: две серии ─────────────────────────
BOOKS = [
    (OLD_SERIES, "", "под прежний стандарт", "предыдущее поколение",
     "готовит к экзамену прежнего формата; язык даёт тот же самый",
     "учебник, тетрадь и пособие для преподавателя", "old"),
    (NEW_SERIES, NEW_SERIES_CN, "под новый стандарт", "тома уровня вышли в 2026 году",
     "готовит к экзамену после перехода; в описаниях заявлены цифровые материалы",
     "учебник и рабочая тетрадь", "new"),
]
books = ""
for name, cn, std, when, about, kit, cls in BOOKS:
    books += ('<div class="bk ' + cls + '">'
              '<div class="nm">' + name + '</div>'
              + ('<div class="cn han">' + cn + '</div>' if cn else '<div class="cn"></div>')
              + '<div class="st">' + std + '</div>'
              '<div class="wh">' + when + '</div>'
              '<div class="ab">' + about + '</div>'
              '<div class="kt"><s>в комплекте</s>' + kit + '</div>'
              '</div>')
assert books.count('class="bk') == 2

HERO_CSS = BASE + """
html,body{width:1200px;height:630px}
.card{width:1200px;height:630px;padding:26px 48px 22px 64px}
.head{display:flex;justify-content:space-between;align-items:flex-end;gap:30px;margin-bottom:20px}
h1{font-size:40px;max-width:23ch}
.tip{flex:0 0 330px}
.books{flex:1 1 auto;display:flex;align-items:stretch;gap:22px}
.bk{flex:1 1 0;border-radius:16px;padding:22px 26px;display:flex;flex-direction:column;
 border:1px solid var(--brick);background:var(--surface)}
.bk.new{background:var(--brick-soft)}
.bk.old{border:1px dashed var(--grey)}
.nm{font-size:27px;font-weight:700;color:var(--ink);line-height:1.1;margin-bottom:4px}
.bk.old .nm{color:var(--taupe)}
.cn{font-family:'Noto Serif SC',serif;font-size:20px;color:var(--brick);min-height:28px;
 margin-bottom:12px}
.st{font-size:12px;font-weight:700;letter-spacing:.11em;text-transform:uppercase;
 color:var(--brick);margin-bottom:10px}
.bk.old .st{color:var(--grey)}
.wh{font-size:16px;color:var(--ink-2);line-height:1.35;margin-bottom:14px}
.ab{font-size:15px;color:var(--ink);line-height:1.4;margin-bottom:auto}
.bk.old .ab{color:var(--ink-2)}
.kt{margin-top:16px;padding-top:12px;border-top:1px solid var(--hair);font-size:15px;
 color:var(--ink);line-height:1.35}
.kt s{display:block;text-decoration:none;font-size:11px;font-weight:700;letter-spacing:.11em;
 text-transform:uppercase;color:var(--taupe);margin-bottom:5px}
"""

hero = ('<!DOCTYPE html><html lang="ru"><head><meta charset="utf-8">' + FONTS
        + "<style>" + VARS + HERO_CSS + "</style></head><body><div class=\"card\">"
        + '<div class="head"><div>'
        + '<div class="eyebrow">Учебник второго уровня</div>'
        + '<h1>Под одним номером <i>две разные книги</i></h1></div>'
        + '<div class="tip"><b>Обе официальные.</b> Это не переиздание одной серии, '
          'а два поколения книг, которые продаются одновременно</div></div>'
        + '<div class="books">' + books + '</div>'
        + '<div class="foot"><span class="lb">Что проверять</span>'
        + '<span class="vl">название серии на обложке, <b>год издания</b> и состав '
          'комплекта</span>'
        + '<span class="lb">В цифре</span>'
        + '<span class="vl">книг нет ни у одной</span></div>'
        + "</div></body></html>")

# ───────────────────────── инфографика: что есть в цифре ─────────────────────────
rows = ""
for name, yes, why, st in DIGITAL:
    rows += ('<div class="dr' + ("" if yes else " no") + '">'
             '<div class="vd">' + ("да" if yes else "нет") + '</div>'
             '<div class="nm">' + name + '</div>'
             '<div class="wh">' + why + '</div>'
             '<div class="st' + (" soft" if st == DESCR else "") + '">' + st + '</div>'
             '</div>')
assert rows.count('class="dr') == 3 and rows.count("soft") == 1

FIG_CSS = BASE + """
html,body{width:1200px;height:450px}
.card{width:1200px;height:450px;padding:26px 48px 22px 64px}
.head{display:flex;justify-content:space-between;align-items:flex-end;gap:30px;margin-bottom:16px}
h1{font-size:34px;max-width:24ch}
.tip{flex:0 0 330px}
.list{flex:1 1 auto;display:flex;flex-direction:column;justify-content:center;gap:12px}
.dr{display:flex;align-items:center;gap:16px;background:var(--surface);
 border:1px solid var(--hair);border-left:5px solid var(--brick);border-radius:13px;
 padding:14px 18px}
.dr.no{border-left-color:var(--grey);border-style:dashed;background:transparent}
.vd{flex:0 0 62px;font-family:'Cormorant Garamond',serif;font-size:34px;font-weight:700;
 color:var(--brick);line-height:1}
.dr.no .vd{color:var(--grey)}
.nm{flex:0 0 310px;font-size:18px;font-weight:600;color:var(--ink);line-height:1.2}
.dr.no .nm{color:var(--taupe)}
.wh{flex:1 1 0;font-size:15px;color:var(--ink-2);line-height:1.3}
.st{flex:0 0 180px;font-size:11.5px;font-weight:700;letter-spacing:.09em;text-transform:uppercase;
 color:var(--brick);text-align:right}
.st.soft{color:var(--taupe)}
"""

fig = ('<!DOCTYPE html><html lang="ru"><head><meta charset="utf-8">' + FONTS
       + "<style>" + VARS + FIG_CSS + "</style></head><body><div class=\"card\">"
       + '<div class="head"><div>'
       + '<div class="eyebrow">Второй уровень</div>'
       + '<h1>Что бывает <i>в электронном виде</i></h1></div>'
       + '<div class="tip"><b>Средняя строка держится на описаниях продавцов.</b> '
         'У издательства я её не проверяла</div></div>'
       + '<div class="list">' + rows + '</div>'
       + '<div class="foot"><span class="lb">Главное</span>'
       + '<span class="vl">цифровые материалы — <b>не электронная книга</b></span>'
       + '<span class="lb">Звук</span>'
       + '<span class="vl">привязан к тому, в котором напечатан код</span></div>'
       + "</div></body></html>")

open(S + "sk2-hero.html", "w", encoding="utf-8").write(hero)
open(S + "sk2-info.html", "w", encoding="utf-8").write(fig)
print("готово: sk2-hero.html, sk2-info.html")
