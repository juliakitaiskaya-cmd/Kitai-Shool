# -*- coding: utf-8 -*-
# Картинки к статье «Учебник HSK 2»
# Обложка     — три плитки с числами, одна из них пустая: числа по тому не подтверждены
# Инфографика — три добора после книги: что, почему и каким действием проверить
import sys
sys.path.insert(0, "/home/user/Kitai-Shool/content")
from uch2 import (EXTRA, LEVEL_NEW, LEVEL_OLD, LESSONS, VOL_WORDS, COVER, REST, STEP_NEW)

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

# ───────────────────────── обложка: три плитки, одна пустая ─────────────────────────
assert LESSONS is None and VOL_WORDS is None, "пустая плитка берётся из данных, а не придумана"

TILES = [
    ("Действующий словник уровня", str(LEVEL_NEW), "слов к концу второго уровня", "now"),
    ("Прежний словник уровня", str(LEVEL_OLD), "под него и собран том", "old"),
    ("Уроков в томе", "?", "подтвердить не удалось", "none"),
]
tiles = ""
for lbl, num, sub, cls in TILES:
    tiles += ('<div class="tl ' + cls + '"><s>' + lbl + '</s><b>' + num + '</b>'
              '<i>' + sub + '</i></div>')
assert tiles.count('class="tl') == 3 and tiles.count(">?<") == 1

HERO_CSS = BASE + """
html,body{width:1200px;height:630px}
.card{width:1200px;height:630px;padding:26px 48px 22px 64px}
.head{display:flex;justify-content:space-between;align-items:flex-end;gap:30px;margin-bottom:24px}
h1{font-size:41px;max-width:23ch}
.tip{flex:0 0 330px}
.tiles{flex:1 1 auto;display:flex;align-items:center;gap:18px}
.tl{flex:1 1 0;align-self:stretch;border-radius:16px;padding:24px 26px;
 display:flex;flex-direction:column;justify-content:center;border:1px solid var(--brick);
 background:var(--surface)}
.tl.old{background:var(--brick-soft)}
.tl.none{border:1px dashed var(--grey);background:transparent}
.tl s{display:block;text-decoration:none;font-size:12px;font-weight:700;letter-spacing:.11em;
 text-transform:uppercase;color:var(--brick);margin-bottom:12px}
.tl.none s{color:var(--grey)}
.tl b{display:block;font-size:70px;font-weight:700;color:var(--ink);line-height:1;
 margin-bottom:12px}
.tl.none b{color:var(--grey);font-size:70px}
.tl i{font-style:normal;font-size:15px;color:var(--ink-2);line-height:1.35}
.tl.none i{color:var(--taupe)}
"""

hero = ('<!DOCTYPE html><html lang="ru"><head><meta charset="utf-8">' + FONTS
        + "<style>" + VARS + HERO_CSS + "</style></head><body><div class=\"card\">"
        + '<div class="head"><div>'
        + '<div class="eyebrow">Учебник второго уровня</div>'
        + '<h1>Два числа известны, <i>третье приходится считать самому</i></h1></div>'
        + '<div class="tip"><b>Прочерк честнее догадки.</b> Описания второго тома расходятся '
          'между собой, и подставлять любое из них нельзя</div></div>'
        + '<div class="tiles">' + tiles + '</div>'
        + '<div class="foot"><span class="lb">Расчёт</span>'
        + '<span class="vl">том закрывает <b>' + str(COVER) + ' %</b> уровня, добрать — '
          'около <b>' + str(REST) + ' слов</b></span>'
        + '<span class="lb">Как считать</span>'
        + '<span class="vl">по оглавлению своего издания</span></div>'
        + "</div></body></html>")

# ───────────────────────── инфографика: три добора ─────────────────────────
rows = ""
for i, (what, why, how) in enumerate(EXTRA, start=1):
    rows += ('<div class="ex">'
             '<div class="n">' + str(i) + '</div>'
             '<div class="wt"><b>' + what + '</b><s>' + why + '</s></div>'
             '<div class="hw"><i>проверка</i>' + how + '</div>'
             '</div>')
assert rows.count('class="ex"') == 3

FIG_CSS = BASE + """
html,body{width:1200px;height:530px}
.card{width:1200px;height:530px;padding:26px 48px 22px 64px}
.head{display:flex;justify-content:space-between;align-items:flex-end;gap:30px;margin-bottom:18px}
h1{font-size:34px;max-width:24ch}
.tip{flex:0 0 330px}
.list{flex:1 1 auto;display:flex;flex-direction:column;justify-content:center;gap:12px}
.ex{display:flex;align-items:stretch;gap:16px;background:var(--surface);
 border:1px solid var(--hair);border-radius:14px;padding:14px 18px}
.n{flex:0 0 32px;height:32px;border-radius:50%;background:var(--brick);color:#fff;
 font-size:15px;font-weight:700;display:flex;align-items:center;justify-content:center}
.wt{flex:1 1 0}
.wt b{display:block;font-size:19px;font-weight:600;color:var(--ink);margin-bottom:5px}
.wt s{display:block;text-decoration:none;font-size:14px;color:var(--ink-2);line-height:1.35}
.hw{flex:0 0 400px;background:var(--brick-soft);border-radius:11px;padding:10px 14px;
 font-size:14.5px;color:var(--ink);line-height:1.35}
.hw i{display:block;font-style:normal;font-size:11px;font-weight:700;letter-spacing:.11em;
 text-transform:uppercase;color:var(--brick);margin-bottom:4px}
"""

fig = ('<!DOCTYPE html><html lang="ru"><head><meta charset="utf-8">' + FONTS
       + "<style>" + VARS + FIG_CSS + "</style></head><body><div class=\"card\">"
       + '<div class="head"><div>'
       + '<div class="eyebrow">После тома</div>'
       + '<h1>Три добора, <i>которых не видно по страницам</i></h1></div>'
       + '<div class="tip"><b>Каждый проверяется действием.</b> Не ощущением «вроде прошёл», '
         'а конкретной задачей на несколько минут</div></div>'
       + '<div class="list">' + rows + '</div>'
       + '<div class="foot"><span class="lb">Слова</span>'
       + '<span class="vl">добрать около <b>' + str(REST) + '</b> сверх книги</span>'
       + '<span class="lb">Письмо</span>'
       + '<span class="vl">в экзамене второго уровня его нет, в требованиях есть</span></div>'
       + "</div></body></html>")

open(S + "uch2-hero.html", "w", encoding="utf-8").write(hero)
open(S + "uch2-info.html", "w", encoding="utf-8").write(fig)
print("готово: uch2-hero.html, uch2-info.html")
