# -*- coding: utf-8 -*-
# Картинки к статье «Тексты и диалоги для HSK 1–6»
# Обложка     — три одинаковые строки-образца с разным числом отмеченных слов
# Инфографика — три прохода по одному тексту по кругу
import sys
sys.path.insert(0, "/home/user/Kitai-Shool/content")
from teksty import COVERAGE, PASSES, PER_LINE, CONF, OURS

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

# ───────── обложка: три строки-образца, отмечены незнакомые слова ─────────
# В строке двадцать «слов». Сколько из них отмечено — считается из данных:
# доля незнакомых на сто слов, пересчитанная на двадцать.
WORDS_IN_ROW = 20
ROWS = []
for share, what, unknown, st in COVERAGE:
    marked = int(round(unknown * WORDS_IN_ROW / 100.0))
    ROWS.append((share, unknown, marked, what, st))
assert [r[2] for r in ROWS] == [0, 1, 2], "отмеченных слов в строке: %s" % [r[2] for r in ROWS]

# при двух на сто на двадцать слов приходится меньше одного — показываем
# это половинной меткой, иначе строка выглядела бы вовсе без отметок
HALF = {98: True, 95: False, 90: False}


def row_html(share, unknown, marked, what, st):
    cells = ""
    for i in range(WORDS_IN_ROW):
        cls = "w"
        if share == 98 and i == 7:
            cls += " half"
        elif share == 95 and i == 11:
            cls += " mark"
        elif share == 90 and i in (5, 14):
            cls += " mark"
        cells += '<div class="' + cls + '"></div>'
    tag = "исследования" if st == CONF else "наш вывод"
    return ('<div class="rw"><div class="rl"><b>' + str(share) + '&nbsp;%</b> знакомо'
            '<span class="tg">' + tag + '</span></div>'
            '<div class="line">' + cells + '</div>'
            '<div class="rr"><b>' + str(unknown) + '</b> незнакомых на сто слов<br>'
            '<span>' + what + "</span></div></div>")


rows_html = "".join(row_html(*r) for r in ROWS)
assert rows_html.count('class="rw"') == 3
assert rows_html.count("mark") == 3 and rows_html.count("half") == 1

HERO_CSS = BASE + """
html,body{width:1200px;height:630px}
.card{width:1200px;height:630px;padding:30px 48px 20px 64px}
h1{font-size:46px;max-width:27ch;margin-bottom:6px}
.sub{font-size:17px;color:var(--ink-2);margin-bottom:24px}
.rows{flex:1 1 auto;display:flex;flex-direction:column;justify-content:space-evenly}
.rw{display:flex;align-items:center;gap:22px}
.rl{flex:0 0 196px;font-size:15px;color:var(--ink-2)}
.rl b{display:block;font-size:26px;color:var(--ink);line-height:1.1}
.tg{display:inline-block;margin-top:4px;font-size:11px;font-weight:700;
 letter-spacing:.07em;text-transform:uppercase;color:var(--taupe);
 background:var(--grey-soft);border-radius:5px;padding:2px 7px}
.line{flex:1 1 auto;display:flex;gap:7px;align-items:center}
.w{flex:1 1 0;height:15px;border-radius:4px;background:#DCD6CB}
.w.mark{background:var(--brick);height:20px}
.w.half{background:linear-gradient(90deg,var(--brick) 50%,#DCD6CB 50%);height:20px}
.rr{flex:0 0 250px;font-size:14px;color:var(--ink-2);line-height:1.35}
.rr b{font-size:19px;color:var(--brick);font-weight:700}
.rr span{color:var(--taupe)}
"""

hero = ('<!DOCTYPE html><html lang="ru"><head><meta charset="utf-8">' + FONTS
        + "<style>" + VARS + HERO_CSS + "</style></head><body><div class=\"card\">"
        + '<div class="eyebrow">Тексты и диалоги для HSK 1–6</div>'
        + '<h1>Текст вашего уровня <i>определяется одной меркой</i></h1>'
        + '<div class="sub">Каждая полоса — одна строка в двадцать слов, отмечены '
          'незнакомые. Половина метки — меньше одного слова на строку</div>'
        + '<div class="rows">' + rows_html + '</div>'
        + '<div class="foot"><span class="lb">Проверка</span>'
        + '<span class="vl">посчитайте незнакомые слова <b>в одном абзаце</b> — '
          'это минута</span>'
        + '<span class="lb">Оговорка</span>'
        + '<span class="vl">доли получены на английском материале</span></div>'
        + "</div></body></html>")

# ───────── инфографика: три прохода по кругу ─────────
# чего на этом проходе делать не нужно
NOT = {
    "первый": "не лезть в словарь",
    "второй": "не пытаться запомнить всё сразу",
    "третий": "не читать про себя",
}
assert set(NOT) == {p[0] for p in PASSES}

# сколько занимает проход — качественная оценка из практики, без чисел
HOW_LONG = {
    "первый": "Самый быстрый: один раз насквозь",
    "второй": "Самый долгий: здесь основная работа",
    "третий": "Быстрый, но вслух и без спешки",
}
assert set(HOW_LONG) == set(NOT), "у каждого прохода сказано, сколько он занимает"

STEPS = []
for i, (name, what, why) in enumerate(PASSES, start=1):
    STEPS.append((i, name, what, why, NOT[name]))
assert len(STEPS) == 3

steps_html = ""
for i, name, what, why, nope in STEPS:
    steps_html += ('<div class="st"><div class="num">' + str(i) + '</div>'
                   '<div class="mid"><div class="nm">Проход ' + name + '</div>'
                   '<div class="wh">' + what[0].upper() + what[1:] + '</div>'
                   '<div class="wy">' + why[0].upper() + why[1:] + '</div>'
                   '<div class="hl">' + HOW_LONG[name] + '</div></div>'
                   '<div class="no">' + nope[0].upper() + nope[1:] + "</div></div>")
assert steps_html.count('class="st"') == 3

FIG_CSS = BASE + """
html,body{width:1200px;height:520px}
.card{width:1200px;height:520px;padding:22px 48px 14px 64px}
.head{display:flex;justify-content:space-between;align-items:flex-start;gap:34px;
 margin-bottom:14px}
h1{font-size:29px;max-width:31ch}
.tip{background:var(--surface);border:1px solid var(--hair);border-left:4px solid var(--brick);
 border-radius:13px;padding:10px 15px;font-size:13px;color:var(--ink-2);line-height:1.33;
 flex:0 0 312px}
.tip b{color:var(--ink)}
.flow{flex:1 1 auto;display:flex;align-items:stretch;gap:0}
.st{flex:1 1 0;background:var(--surface);border:1px solid var(--hair);border-radius:16px;
 padding:16px 20px 14px;display:flex;flex-direction:column;justify-content:space-between;
 position:relative;margin-right:30px}
.mid{}
.st:last-child{margin-right:0}
.st:not(:last-child):after{content:"";position:absolute;right:-22px;top:50%;
 width:14px;height:14px;border-top:3px solid var(--brick);border-right:3px solid var(--brick);
 transform:translateY(-50%) rotate(45deg)}
.num{width:34px;height:34px;border-radius:50%;background:var(--brick);color:#fff;
 font-size:18px;font-weight:700;display:flex;align-items:center;justify-content:center}
.nm{font-size:13px;font-weight:700;letter-spacing:.07em;text-transform:uppercase;
 color:var(--taupe);margin-top:10px}
.wh{font-size:19px;font-weight:600;color:var(--ink);line-height:1.26;margin-top:5px}
.wy{font-size:14px;color:var(--ink-2);line-height:1.35;margin-top:9px}
.hl{font-size:13px;color:var(--taupe);line-height:1.3;margin-top:12px;padding-left:11px;border-left:3px solid var(--hair)}
.no{padding-top:11px;border-top:1px solid var(--hair);font-size:13.5px;
 color:var(--brick-d);font-weight:600;line-height:1.3}
"""

fig = ('<!DOCTYPE html><html lang="ru"><head><meta charset="utf-8">' + FONTS
       + "<style>" + VARS + FIG_CSS + "</style></head><body><div class=\"card\">"
       + '<div class="head"><div>'
       + '<div class="eyebrow">Один текст, три прохода</div>'
       + '<h1>Три прохода по одному тексту <i>дают больше, чем три текста</i></h1></div>'
       + '<div class="tip"><b>Порядок важен, и словарь появляется только на втором '
         'проходе.</b> Внизу каждой карточки — то, чего на этом проходе делать '
         'не нужно</div></div>'
       + '<div class="flow">' + steps_html + '</div>'
       + '<div class="foot"><span class="lb">Условие</span>'
       + '<span class="vl">работает только с текстом, который <b>прошёл мерку</b> '
         'по незнакомым словам</span>'
       + '<span class="lb">Откуда</span>'
       + '<span class="vl">практика занятий, а не исследования</span></div>'
       + "</div></body></html>")

open(S + "tek-hero.html", "w", encoding="utf-8").write(hero)
open(S + "tek-info.html", "w", encoding="utf-8").write(fig)
print("готово: tek-hero.html, tek-info.html")
