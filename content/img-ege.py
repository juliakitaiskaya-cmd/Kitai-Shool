# -*- coding: utf-8 -*-
# Картинки к статье «ЕГЭ по китайскому и HSK»
# Обложка     — две двери, у каждой свой ключ
# Инфографика — пять строк сравнения и полоса «что переносится»
import sys
sys.path.insert(0, "/home/user/Kitai-Shool/content")
from ege import WHO, OVERLAP

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

# ───────────────────── обложка: две двери ─────────────────────
DOOR = ('<div class="door"><div class="plate">%s</div>'
        '<div class="knob"></div></div>')


def gate(where, doc, note, strong):
    return ('<div class="gt' + (" alt" if strong else "") + '">'
            + DOOR % where +
            '<div class="key">' + doc + "</div>"
            '<div class="kn">' + note + "</div></div>")


gates = (gate("Российский вуз", "школьный экзамен",
              "его баллы идут в конкурс на место", False)
         + '<div class="cross">ключ не подходит<br>к соседней двери</div>'
         + gate("Китайский вуз", "международный сертификат",
                "он подтверждает владение языком", True))
assert gates.count('class="gt') == 2 and gates.count("cross") == 1

HERO_CSS = BASE + """
html,body{width:1200px;height:630px}
.card{width:1200px;height:630px;padding:26px 48px 18px 64px}
h1{font-size:39px;max-width:60ch;margin-bottom:5px}
.sub{font-size:15.5px;color:var(--ink-2);margin-bottom:20px;max-width:96ch;line-height:1.3}
.row{flex:1 1 auto;display:flex;align-items:flex-start;justify-content:center;
 gap:34px;padding-top:10px}
.gt{flex:0 0 330px;display:flex;flex-direction:column;align-items:center;
 text-align:center}
.door{position:relative;width:200px;height:236px;background:var(--surface);
 border:2px solid var(--hair);border-radius:12px 12px 4px 4px;
 box-shadow:0 3px 11px rgba(44,36,32,.07);display:flex;align-items:flex-start;
 justify-content:center;padding-top:34px}
.gt.alt .door{border-color:var(--brick)}
.plate{background:var(--grey-soft);border-radius:7px;padding:9px 13px;
 font-size:15.5px;font-weight:700;color:var(--ink);max-width:150px;line-height:1.25}
.gt.alt .plate{background:var(--brick-soft);color:var(--brick-d)}
.knob{position:absolute;right:18px;top:50%;width:13px;height:13px;border-radius:50%;
 background:var(--taupe)}
.gt.alt .knob{background:var(--brick)}
.key{font-size:19px;font-weight:700;color:var(--ink);margin-top:16px;
 border-top:2px solid var(--hair);padding-top:13px;width:100%;max-width:250px}
.gt.alt .key{color:var(--brick)}
.kn{font-size:14.5px;color:var(--ink-2);margin-top:7px;max-width:245px;line-height:1.35}
.cross{flex:0 0 172px;font-size:15px;font-weight:700;color:var(--taupe);
 text-align:center;line-height:1.35;margin-top:112px}
.band{margin-top:auto;background:var(--surface);border:1px solid var(--hair);
 border-left:4px solid var(--brick);border-radius:13px;padding:13px 18px;
 font-size:16px;color:var(--ink-2);line-height:1.4}
.band b{color:var(--ink)}
"""

hero = ('<!DOCTYPE html><html lang="ru"><head><meta charset="utf-8">' + FONTS
        + "<style>" + VARS + HERO_CSS + "</style></head><body><div class=\"card\">"
        + '<div class="eyebrow">Два экзамена — две двери</div>'
        + '<h1>Один документ открывает одну дверь — <i>и только её</i></h1>'
        + '<div class="sub">Сдача одного экзамена не засчитывается вместо '
          'другого ни в одну сторону: у них разные принимающие стороны</div>'
        + '<div class="row">' + gates + "</div>"
        + '<div class="band"><b>Поэтому выбирают не экзамен, а направление.</b> '
          'Сначала выясняют, кто будет читать документы, — экзамен из этого '
          'следует сам</div>'
        + '<div class="foot"><span class="lb">Источник</span>'
        + '<span class="vl">устройство приёма и наша практика</span>'
        + '<span class="lb">Чего здесь нет</span>'
        + '<span class="vl">состава и шкалы школьного экзамена</span></div>'
        + "</div></body></html>")

# ───────── инфографика: пять строк сравнения и полоса переноса ─────────
cmp_rows = ""
for a, b, c in WHO:
    cmp_rows += ('<div class="cr"><div class="cl">' + a + "</div>"
                 '<div class="cv one">' + b + "</div>"
                 '<div class="cv two">' + c + "</div></div>")
assert cmp_rows.count('class="cr"') == len(WHO) == 5

ov_items = ""
for a, b, c in OVERLAP:
    cls = "ov no" if b == "не переносится" else "ov"
    ov_items += ('<div class="' + cls + '"><div class="ovn">' + a + "</div>"
                 '<div class="ovv">' + b + "</div></div>")
assert (ov_items.count('<div class="ov">')
        + ov_items.count('<div class="ov no">')) == len(OVERLAP) == 4
assert ov_items.count('<div class="ov no">') == 2

FIG_CSS = BASE + """
html,body{width:1200px;height:520px}
.card{width:1200px;height:520px;padding:22px 48px 14px 64px}
.head{display:flex;justify-content:space-between;align-items:flex-start;gap:34px;
 margin-bottom:12px}
h1{font-size:29px;max-width:40ch}
.tip{background:var(--surface);border:1px solid var(--hair);border-left:4px solid var(--brick);
 border-radius:13px;padding:10px 15px;font-size:13px;color:var(--ink-2);line-height:1.33;
 flex:0 0 290px}
.tip b{color:var(--ink)}
.cmp{width:100%}
.cr{display:flex;align-items:stretch;border-bottom:1px solid var(--hair)}
.cr:first-child{border-top:1px solid var(--hair)}
.cl{flex:0 0 272px;font-size:14.5px;color:var(--taupe);font-weight:600;
 padding:11px 14px 11px 0;display:flex;align-items:center}
.cv{flex:1 1 0;font-size:15.5px;padding:11px 16px;display:flex;align-items:center;
 line-height:1.3}
.cv.one{background:rgba(239,237,232,.6);color:var(--ink)}
.cv.two{background:var(--brick-soft);color:var(--brick-d);font-weight:600}
.ovline{display:flex;align-items:center;gap:14px;margin-top:16px}
.ovt{flex:0 0 258px;font-size:14px;font-weight:700;letter-spacing:.09em;
 text-transform:uppercase;color:var(--taupe);text-align:right;line-height:1.3}
.ovs{flex:1 1 auto;display:flex;gap:12px}
.ov{flex:1 1 0;background:var(--brick);color:#fff;border-radius:11px;
 padding:11px 13px;text-align:center}
.ov.no{background:var(--grey-soft);color:var(--taupe)}
.ovn{font-size:15.5px;font-weight:700;line-height:1.2}
.ovv{font-size:13px;margin-top:5px;opacity:.92}
"""

fig = ('<!DOCTYPE html><html lang="ru"><head><meta charset="utf-8">' + FONTS
       + "<style>" + VARS + FIG_CSS + "</style></head><body><div class=\"card\">"
       + '<div class="head"><div>'
       + '<div class="eyebrow">Построчное сравнение</div>'
       + '<h1>Совпадений нет <i>ни в одной строке</i></h1></div>'
       + '<div class="tip"><b>Слева школьный экзамен, справа международный '
         'сертификат.</b> Состава и шкалы школьного экзамена здесь нет '
         'намеренно</div></div>'
       + '<div class="cmp">' + cmp_rows + "</div>"
       + '<div class="ovline"><div class="ovt">Что переносится между '
         'подготовками</div><div class="ovs">' + ov_items + "</div></div>"
       + '<div class="foot"><span class="lb">Устройство сертификата</span>'
       + '<span class="vl">по нашим разборам системы оценки</span>'
       + '<span class="lb">Школьный экзамен</span>'
       + '<span class="vl">правила на текущий год — у официальных '
         'документов</span></div>'
       + "</div></body></html>")

open(S + "ege-hero.html", "w", encoding="utf-8").write(hero)
open(S + "ege-info.html", "w", encoding="utf-8").write(fig)
print("готово: ege-hero.html, ege-info.html")
