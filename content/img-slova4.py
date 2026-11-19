# -*- coding: utf-8 -*-
# Картинки к статье «Слова HSK 4»
# Обложка     — определитель с ветвлением: сколько строк в файле и что это за список
# Инфографика — числовая ось с засечками на 1000, 1200 и 2000
import sys
sys.path.insert(0, "/home/user/Kitai-Shool/content")
from slova4 import (COUNTS, WORDS_NEW, WORDS_TOTAL, OLD_TOTAL, OLD_NEW, DIFF_OLD,
                    OLD_GROWTH)

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

# ───────────────────── обложка: определитель с ветвлением ─────────────────────
BRANCHES = [(c[1], c[0], c[2]) for c in COUNTS]
assert len(BRANCHES) == 4 and BRANCHES[0][0] == str(WORDS_TOTAL)
# в определителе удобнее идти от короткого к длинному
ORDER = [1, 2, 0, 3]
cards = ""
for k in ORDER:
    num, name, why = BRANCHES[k]
    other = " other" if not num.isdigit() else ""
    cards += ('<div class="br' + other + '"><div class="num">' + num + '</div>'
              '<div class="nm">' + name + '</div>'
              '<div class="wh">' + why + '</div></div>')
assert cards.count('class="br') == 4 and cards.count("other") == 1

HERO_CSS = BASE + """
html,body{width:1200px;height:630px}
.card{width:1200px;height:630px;padding:26px 48px 20px 64px}
.head{display:flex;justify-content:space-between;align-items:flex-end;gap:30px;margin-bottom:16px}
h1{font-size:40px;max-width:21ch}
.tip{flex:0 0 330px}
.q{display:flex;align-items:center;gap:14px;margin-bottom:14px}
.q b{font-size:19px;color:var(--ink)}
.q i{font-style:normal;font-size:13px;font-weight:700;letter-spacing:.11em;
 text-transform:uppercase;color:#fff;background:var(--brick);border-radius:8px;padding:6px 11px}
.q:after{content:"";flex:1 1 0;height:1px;background:var(--hair)}
.q2{display:flex;align-items:center;gap:14px;padding-top:6px;padding-bottom:4px}
.q2 b{font-size:16.5px;font-weight:600;color:var(--ink-2)}
.q2 i{font-style:normal;font-size:13px;font-weight:700;letter-spacing:.11em;
 text-transform:uppercase;color:var(--brick);border:1px solid var(--brick);
 border-radius:8px;padding:5px 11px;flex:0 0 auto}
.rows{flex:1 1 auto;display:flex;gap:14px;align-items:center}
.br{flex:1 1 0;background:var(--surface);border:1px solid var(--hair);
 border-top:4px solid var(--brick);border-radius:13px;padding:18px;
 display:flex;flex-direction:column;gap:8px;min-height:208px}
.br.other{border-top-color:var(--grey);border-style:dashed;background:transparent}
.num{font-size:30px;font-weight:700;color:var(--brick);line-height:1}
.br.other .num{font-size:19px;color:var(--taupe);line-height:1.2}
.nm{font-size:17px;font-weight:600;color:var(--ink);line-height:1.2}
.wh{font-size:14px;color:var(--ink-2);line-height:1.35}
"""

hero = ('<!DOCTYPE html><html lang="ru"><head><meta charset="utf-8">' + FONTS
        + "<style>" + VARS + HERO_CSS + "</style></head><body><div class=\"card\">"
        + '<div class="head"><div>'
        + '<div class="eyebrow">Лексика четвёртого уровня</div>'
        + '<h1>«Все слова HSK 4» — <i>это четыре разных списка</i></h1></div>'
        + '<div class="tip"><b>Ни один из них не ошибочный.</b> Это ответы на разные '
          'вопросы, и путают их из-за одинакового названия</div></div>'
        + '<div class="q"><i>Шаг первый</i><b>Сколько строк в вашем файле?</b></div>'
        + '<div class="rows">' + cards + '</div>'
        + '<div class="q2"><i>Шаг второй</i><b>Прочитайте первые двадцать строк: '
          'накопительный список начинается со слов первого уровня</b></div>'
        + '<div class="foot"><span class="lb">Действующая шкала</span>'
        + '<span class="vl"><b>' + str(WORDS_TOTAL) + '</b> слов всего, из них <b>'
        + str(WORDS_NEW) + '</b> новых на уровне</span>'
        + '<span class="lb">Прежняя</span>'
        + '<span class="vl">' + str(OLD_TOTAL) + ', разница в ' + str(DIFF_OLD)
        + ' позиций</span></div>'
        + "</div></body></html>")

# ───────────────────── инфографика: числовая ось ─────────────────────
AXW = 1010.0
MAXV = float(WORDS_TOTAL)
MARKS = [
    (WORDS_NEW, "прибавка уровня", "рабочий список", True),
    (OLD_TOTAL, "прежний стандарт", "короче действующего", True),
    (WORDS_TOTAL, "весь словарь уровня", "вместе с младшими", True),
]
assert [m[0] for m in MARKS] == [1000, 1200, 2000]

ticks = ""
HIGH = {1000: 118}          # разводим близкие засечки по высоте
for v, name, why, up in MARKS:
    x = AXW * v / MAXV
    stem = HIGH.get(v, 22)
    ticks += ('<div class="mk" style="left:' + str(int(round(x))) + 'px">'
              '<div class="bub"><b>' + str(v) + '</b><span>' + name + '</span>'
              '<i>' + why + '</i></div>'
              '<div class="stem" style="height:' + str(stem) + 'px"></div></div>')
assert ticks.count('class="mk"') == 3

FIG_CSS = BASE + """
html,body{width:1200px;height:470px}
.card{width:1200px;height:470px;padding:24px 48px 18px 64px}
.head{display:flex;justify-content:space-between;align-items:flex-end;gap:30px;margin-bottom:10px}
h1{font-size:34px;max-width:24ch}
.tip{flex:0 0 330px}
.axis-wrap{flex:1 1 auto;position:relative;display:flex;align-items:flex-end;
 padding-bottom:58px}
.axis{position:absolute;left:0;bottom:46px;width:1010px;height:6px;border-radius:3px;
 background:linear-gradient(90deg,var(--brick-soft),var(--brick))}
.mk{position:absolute;bottom:46px;transform:translateX(-50%)}
.stem{width:3px;background:var(--brick);margin:0 auto}
.bub{background:var(--surface);border:1px solid var(--hair);border-bottom:3px solid var(--brick);
 border-radius:12px;padding:9px 12px;width:184px;text-align:center;margin-bottom:6px}
.bub b{display:block;font-size:26px;font-weight:700;color:var(--brick);line-height:1}
.bub span{display:block;font-size:14.5px;font-weight:600;color:var(--ink);margin-top:4px}
.bub i{display:block;font-style:normal;font-size:12.5px;color:var(--taupe);margin-top:2px}
.zero{position:absolute;left:0;bottom:18px;font-size:13px;color:var(--taupe)}
.other{position:absolute;right:0;bottom:12px;width:300px;font-size:13.5px;color:var(--ink-2);
 border-left:3px dashed var(--grey);padding-left:12px;line-height:1.35}
"""

fig = ('<!DOCTYPE html><html lang="ru"><head><meta charset="utf-8">' + FONTS
       + "<style>" + VARS + FIG_CSS + "</style></head><body><div class=\"card\">"
       + '<div class="head"><div>'
       + '<div class="eyebrow">Как опознать свой список</div>'
       + '<h1>Три ориентира на одной оси <i>и всё остальное</i></h1></div>'
       + '<div class="tip"><b>Смотрите на число позиций.</b> Оно почти всегда говорит, '
         'по какому счёту собран файл</div></div>'
       + '<div class="axis-wrap"><div class="axis"></div>' + ticks
       + '<div class="zero">0 позиций</div>'
       + '</div>'
       + '<div class="foot"><span class="lb">Любое другое число</span>'
       + '<span class="vl">выборка по урокам учебника или авторская подборка: '
         'с уровнем её не сверить</span>'
       + '<span class="lb">Проверка надёжнее счёта</span>'
       + '<span class="vl">накопительный список начинается со слов первого уровня</span>'
       + '</div>'
       + "</div></body></html>")

open(S + "sl4-hero.html", "w", encoding="utf-8").write(hero)
open(S + "sl4-info.html", "w", encoding="utf-8").write(fig)
print("готово: sl4-hero.html, sl4-info.html")
