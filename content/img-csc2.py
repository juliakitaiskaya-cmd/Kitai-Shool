# -*- coding: utf-8 -*-
# Картинки к переработанной статье «Стипендия CSC»
# Обложка     — лестница из семи ступеней, подача на верхней
# Инфографика — четыре фильтра выбора вуза, список сужается
import sys
sys.path.insert(0, "/home/user/Kitai-Shool/content")
from csc import CHAIN, PICK

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

# ───────────────── обложка: лестница из семи ступеней ─────────────────
N = len(CHAIN)
assert N == 7
STEP_W, STEP_H = 148, 34

steps = ""
for i, (name, _note) in enumerate(CHAIN):
    last = (i == N - 1)
    steps += ('<div class="st' + (" top" if last else "") + '">'
              '<div class="sn">' + str(i + 1) + "</div>"
              '<div class="sbar" style="height:' + str(STEP_H * (i + 1)) + 'px">'
              '</div><div class="sl">' + name + "</div></div>")
assert steps.count('class="st') == N and steps.count("top") == 1

HERO_CSS = BASE + """
html,body{width:1200px;height:630px}
.card{width:1200px;height:630px;padding:26px 48px 18px 64px}
h1{font-size:39px;max-width:60ch;margin-bottom:5px}
.sub{font-size:15.5px;color:var(--ink-2);margin-bottom:16px;max-width:98ch;line-height:1.3}
.row{flex:1 1 auto;display:flex;align-items:flex-end;gap:10px}
.st{flex:1 1 0;display:flex;flex-direction:column;align-items:center;text-align:center}
.sn{font-size:15px;font-weight:700;color:var(--taupe);margin-bottom:6px}
.st.top .sn{color:var(--brick);font-size:18px}
.sbar{width:100%;max-width:""" + str(STEP_W) + """px;border-radius:9px 9px 0 0;
 background:var(--grey-soft);border:1px solid var(--hair);border-bottom:0}
.st.top .sbar{background:linear-gradient(180deg,#C9637A 0%,var(--brick) 100%);
 border-color:var(--brick-d)}
.sl{font-size:13.5px;color:var(--ink-2);margin-top:9px;border-top:2px solid var(--hair);
 padding-top:8px;width:100%;line-height:1.3;min-height:58px}
.st.top .sl{color:var(--brick);font-weight:700}
.band{margin-top:14px;background:var(--surface);border:1px solid var(--hair);
 border-left:4px solid var(--brick);border-radius:13px;padding:13px 18px;
 font-size:16px;color:var(--ink-2);line-height:1.4}
.band b{color:var(--ink)}
"""

hero = ('<!DOCTYPE html><html lang="ru"><head><meta charset="utf-8">' + FONTS
        + "<style>" + VARS + HERO_CSS + "</style></head><body><div class=\"card\">"
        + '<div class="eyebrow">Порядок работы</div>'
        + '<h1>Заявку подают последней — <i>а не первой</i></h1>'
        + '<div class="sub">До подачи идёт шесть шагов, и решается всё '
          'на них. Кандидата выдвигает вуз или посольство, поэтому начинают '
          'с программы и руководителя</div>'
        + '<div class="row">' + steps + "</div>"
        + '<div class="band"><b>Главное слово — номинация.</b> Пока нет '
          'того, кто вас выдвинет, форма заявки не имеет значения</div>'
        + '<div class="foot"><span class="lb">Источник</span>'
        + '<span class="vl">наша практика сопровождения поступающих</span>'
        + '<span class="lb">Чего здесь нет</span>'
        + '<span class="vl">сумм, сроков и названий вузов</span></div>'
        + "</div></body></html>")

# ───────────────── инфографика: четыре фильтра ─────────────────
WID = [820, 620, 440, 260]
assert len(WID) == len(PICK) == 4
assert WID == sorted(WID, reverse=True), "список сужается"

filts = ""
for i, ((name, note), w) in enumerate(zip(PICK, WID)):
    filts += ('<div class="fr"><div class="fn">' + str(i + 1) + "</div>"
              '<div class="fb" style="width:' + str(w) + 'px">'
              '<div class="ft">' + name + "</div></div>"
              '<div class="fd">' + note + "</div></div>")
assert filts.count('class="fr"') == 4

FIG_CSS = BASE + """
html,body{width:1200px;height:520px}
.card{width:1200px;height:520px;padding:22px 48px 14px 64px}
.head{display:flex;justify-content:space-between;align-items:flex-start;gap:34px;
 margin-bottom:14px}
h1{font-size:30px;max-width:40ch}
.tip{background:var(--surface);border:1px solid var(--hair);border-left:4px solid var(--brick);
 border-radius:13px;padding:10px 15px;font-size:13px;color:var(--ink-2);line-height:1.33;
 flex:0 0 300px}
.tip b{color:var(--ink)}
.fr{display:flex;align-items:center;gap:14px;margin-bottom:14px}
.fn{flex:0 0 30px;font-size:16px;font-weight:700;color:var(--taupe);text-align:right}
.fb{height:58px;border-radius:11px;background:linear-gradient(90deg,#E3A7B6 0%,var(--brick) 100%);
 display:flex;align-items:center;padding:0 20px;flex:0 0 auto}
.ft{color:#fff;font-size:17px;font-weight:700;line-height:1.2}
.fd{font-size:14px;color:var(--ink-2);line-height:1.35;flex:1 1 0;max-width:330px}
.tail{font-size:15.5px;color:var(--ink-2);margin-top:4px;line-height:1.4}
.tail b{color:var(--ink)}
"""

fig = ('<!DOCTYPE html><html lang="ru"><head><meta charset="utf-8">' + FONTS
       + "<style>" + VARS + FIG_CSS + "</style></head><body><div class=\"card\">"
       + '<div class="head"><div>'
       + '<div class="eyebrow">Выбор вуза под заявку</div>'
       + '<h1>Четыре признака, <i>и после каждого список короче</i></h1></div>'
       + '<div class="tip"><b>Ширина полосы — сколько вариантов остаётся.</b> '
         'Конкретных вузов и городов мы не называем: списки участников '
         'пересматриваются</div></div>'
       + filts
       + '<div class="tail"><b>Узкий список в конце — это хорошо.</b> Широкий '
         'означает, что выбор ещё не сделан, и план обучения получится '
         'общим</div>'
       + '<div class="foot"><span class="lb">Источник</span>'
       + '<span class="vl">наша практика работы с заявками</span>'
       + '<span class="lb">Проверять</span>'
       + '<span class="vl">в положении той программы, куда подаёте</span></div>'
       + "</div></body></html>")

open(S + "cscg-hero.html", "w", encoding="utf-8").write(hero)
open(S + "cscg-info.html", "w", encoding="utf-8").write(fig)
print("готово: cscg-hero.html, cscg-info.html")
