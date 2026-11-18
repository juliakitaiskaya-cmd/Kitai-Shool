# -*- coding: utf-8 -*-
# Картинки к статье «Учебник HSK 1»
# Обложка     — шкала словаря уровня: что закрывает том и сколько остаётся добрать
# Инфографика — один урок, разложенный на четыре подхода с временем
import sys
sys.path.insert(0, "/home/user/Kitai-Shool/content")
from uch1 import (STEPS, LESSONS, VOL_WORDS, LEVEL_WORDS, OLD_LEVEL_WORDS, COVER, REST,
                  MIN_PER_LESSON)

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

# ───────────────────────── обложка: шкала словаря ─────────────────────────
assert COVER == 50 and VOL_WORDS + REST == LEVEL_WORDS

HERO_CSS = BASE + """
html,body{width:1200px;height:630px}
.card{width:1200px;height:630px;padding:26px 48px 22px 64px}
.head{display:flex;justify-content:space-between;align-items:flex-end;gap:30px;margin-bottom:20px}
h1{font-size:42px;max-width:23ch}
.tip{flex:0 0 330px}
.stage{flex:1 1 auto;display:flex;flex-direction:column;justify-content:center}
.scale{display:flex;align-items:stretch;height:220px;border:1px solid var(--brick);
 border-radius:16px;overflow:hidden}
.part{display:flex;flex-direction:column;justify-content:center;padding:0 26px}
.part.has{flex:0 0 50%;background:var(--brick-soft);border-right:1px solid var(--brick)}
.part.gap{flex:1 1 auto;background:repeating-linear-gradient(135deg,transparent,transparent 9px,
 rgba(154,146,137,.16) 9px,rgba(154,146,137,.16) 18px)}
.part s{display:block;text-decoration:none;font-size:12px;font-weight:700;letter-spacing:.11em;
 text-transform:uppercase;margin-bottom:8px}
.part.has s{color:var(--brick)}
.part.gap s{color:var(--grey)}
.part b{display:block;font-size:46px;font-weight:700;color:var(--ink);line-height:1;
 margin-bottom:7px}
.part.gap b{color:var(--taupe)}
.part i{font-style:normal;font-size:16px;color:var(--ink-2);line-height:1.3}
.axis{display:flex;justify-content:space-between;margin-top:12px;font-size:13px;
 color:var(--taupe)}
.axis b{color:var(--ink)}
.note{margin-top:20px;display:flex;gap:12px;align-items:center}
.note span{font-size:16px;color:var(--ink-2);line-height:1.35}
.note em{font-style:normal;font-weight:700;color:var(--brick)}
"""

hero = ('<!DOCTYPE html><html lang="ru"><head><meta charset="utf-8">' + FONTS
        + "<style>" + VARS + HERO_CSS + "</style></head><body><div class=\"card\">"
        + '<div class="head"><div>'
        + '<div class="eyebrow">Учебник первого уровня</div>'
        + '<h1>Одна книга закрывает <i>половину словаря</i></h1></div>'
        + '<div class="tip"><b>Это не брак книги.</b> Том собран под прежний объём уровня, '
          'а требования с тех пор выросли вдвое</div></div>'
        + '<div class="stage">'
        + '<div class="scale">'
        + '<div class="part has"><s>есть в томе</s><b>' + str(VOL_WORDS) + ' слов</b>'
          '<i>' + str(LESSONS) + ' уроков, примерно по десять слов на урок</i></div>'
        + '<div class="part gap"><s>добрать после книги</s><b>' + str(REST) + ' слов</b>'
          '<i>по списку действующего уровня</i></div>'
        + '</div>'
        + '<div class="axis"><span>шкала словаря уровня</span><span>действующий словник — '
          '<b>' + str(LEVEL_WORDS) + ' слов</b></span></div>'
        + '<div class="note"><span>Прежний объём уровня был <em>'
        + str(OLD_LEVEL_WORDS) + ' слов</em> — ровно столько в томе и лежит</span></div>'
        + '</div>'
        + '<div class="foot"><span class="lb">Вывод</span>'
        + '<span class="vl">пройденный том — это <b>половина уровня</b>, а не весь</span>'
        + '<span class="lb">Статус</span>'
        + '<span class="vl">наш расчёт из двух проверенных чисел</span></div>'
        + "</div></body></html>")

assert str(VOL_WORDS) in hero and str(REST) in hero and str(LEVEL_WORDS) in hero

# ───────────────────────── инфографика: четыре подхода ─────────────────────────
cols = ""
for i, (name, what, mins) in enumerate(STEPS, start=1):
    mark = ""
    if i == 2:
        mark = '<em>до чтения глазами</em>'
    cols += ('<div class="st' + (" key" if i == 2 else "") + '">'
             '<div class="num">' + str(i) + '</div>'
             '<div class="nm">' + name + '</div>'
             '<div class="wt">' + what + '</div>'
             + mark +
             '<div class="mn">' + str(mins) + ' мин</div>'
             '</div>')
assert cols.count('class="st') == 4 and cols.count("key") == 1

FIG_CSS = BASE + """
html,body{width:1200px;height:430px}
.card{width:1200px;height:430px;padding:26px 48px 22px 64px}
.head{display:flex;justify-content:space-between;align-items:flex-end;gap:30px;margin-bottom:18px}
h1{font-size:34px;max-width:24ch}
.tip{flex:0 0 330px}
.row{flex:1 1 auto;display:flex;align-items:stretch;gap:12px}
.st{flex:1 1 0;background:var(--surface);border:1px solid var(--hair);border-radius:14px;
 padding:16px 18px;display:flex;flex-direction:column;position:relative}
.st.key{border:2px solid var(--brick);background:var(--brick-soft)}
.num{width:28px;height:28px;border-radius:50%;background:var(--brick);color:#fff;
 font-size:14px;font-weight:700;display:flex;align-items:center;justify-content:center;
 margin-bottom:10px}
.nm{font-size:19px;font-weight:600;color:var(--ink);margin-bottom:8px}
.wt{font-size:14.5px;color:var(--ink-2);line-height:1.38}
.st em{font-style:normal;display:inline-block;margin-top:9px;font-size:11.5px;font-weight:700;
 letter-spacing:.09em;text-transform:uppercase;color:#fff;background:var(--brick);
 border-radius:7px;padding:4px 10px}
.mn{margin-top:auto;padding-top:12px;border-top:1px solid var(--hair);font-size:17px;
 font-weight:700;color:var(--brick)}
"""

fig = ('<!DOCTYPE html><html lang="ru"><head><meta charset="utf-8">' + FONTS
       + "<style>" + VARS + FIG_CSS + "</style></head><body><div class=\"card\">"
       + '<div class="head"><div>'
       + '<div class="eyebrow">Один урок</div>'
       + '<h1>Четыре подхода, <i>а не чтение подряд</i></h1></div>'
       + '<div class="tip"><b>Запись слушают до чтения.</b> Иначе вы не слушаете, '
         'а вспоминаете прочитанное</div></div>'
       + '<div class="row">' + cols + '</div>'
       + '<div class="foot"><span class="lb">Урок целиком</span>'
       + '<span class="vl">около <b>' + str(MIN_PER_LESSON) + ' минут</b> работы</span>'
       + '<span class="lb">Можно</span>'
       + '<span class="vl">разложить подходы на два-три дня</span></div>'
       + "</div></body></html>")

open(S + "uch1-hero.html", "w", encoding="utf-8").write(hero)
open(S + "uch1-info.html", "w", encoding="utf-8").write(fig)
print("готово: uch1-hero.html, uch1-info.html")
