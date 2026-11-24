# -*- coding: utf-8 -*-
# Картинки к статье «Международные экзамены по китайскому»
# Обложка     — сетка «экзамен × навык»: ни одна строка не заполнена целиком
# Инфографика — круг из четырёх навыков, поделённый между двумя экзаменами
import sys
sys.path.insert(0, "/home/user/Kitai-Shool/content")
from mezhd import (EXAMS, SKILLS, COVER, LEVELS, HSK_N, SPEAK_N, AUD, READ,
                   WRITE, SPEAK)

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

CAP = {AUD: "Аудирование", READ: "Чтение", WRITE: "Письмо", SPEAK: "Речь"}
WHO = {"HSK": "все, кто учит язык", "HSKK": "кому нужна речь", "YCT": "школьники"}
assert set(WHO) == {e[0] for e in EXAMS}

# ───────────────────── обложка: сетка «экзамен × навык» ─────────────────────
head_cells = "".join('<div class="hc">' + CAP[s] + "</div>" for s in SKILLS)
grid = ""
for name, who, lvl, cover, form in EXAMS:
    grid += ('<div class="rh"><b>' + name + '</b><span>' + WHO[name]
             + '<br>' + str(lvl) + ' уровня</span></div>')
    for sk in SKILLS:
        if sk in cover:
            grid += '<div class="cell yes">✓</div>'
        else:
            grid += '<div class="cell no">—</div>'
assert grid.count('class="cell yes"') == HSK_N + SPEAK_N + len(COVER["YCT"])
assert grid.count('class="cell no"') == 3 * len(SKILLS) - grid.count('class="cell yes"')

HERO_CSS = BASE + """
html,body{width:1200px;height:630px}
.card{width:1200px;height:630px;padding:28px 48px 20px 64px}
h1{font-size:43px;max-width:30ch;margin-bottom:6px}
.sub{font-size:17px;color:var(--ink-2);margin-bottom:22px}
.wrap{flex:1 1 auto;display:flex;align-items:center}
.grid{flex:1 1 auto;display:grid;grid-template-columns:214px repeat(4,1fr);gap:9px}
.hc{font-size:14px;font-weight:700;letter-spacing:.05em;text-transform:uppercase;
 color:var(--taupe);text-align:center;padding-bottom:4px}
.corner{}
.rh{display:flex;flex-direction:column;justify-content:center;padding-right:12px}
.rh b{font-size:23px;color:var(--ink)}
.rh span{font-size:13px;color:var(--taupe);line-height:1.3;margin-top:3px}
.cell{height:74px;border-radius:11px;display:flex;align-items:center;justify-content:center;
 font-size:26px;font-weight:700}
.cell.yes{background:var(--brick);color:#fff;border:1px solid var(--brick-d)}
.cell.no{background:var(--surface);color:var(--hair);border:1px solid var(--hair)}
"""

hero = ('<!DOCTYPE html><html lang="ru"><head><meta charset="utf-8">' + FONTS
        + "<style>" + VARS + HERO_CSS + "</style></head><body><div class=\"card\">"
        + '<div class="eyebrow">Международные экзамены по китайскому</div>'
        + '<h1>Ни один экзамен <i>не проверяет язык целиком</i></h1>'
        + '<div class="sub">Четыре навыка и три экзамена: ни одна строка '
          'не заполнена полностью</div>'
        + '<div class="wrap"><div class="grid">'
        + '<div class="corner"></div>' + head_cells + grid + '</div></div>'
        + '<div class="foot"><span class="lb">Вывод</span>'
        + '<span class="vl">чтобы подтвердить язык целиком, <b>сдавать придётся '
          'дважды</b></span>'
        + '<span class="lb">Разбор</span>'
        + '<span class="vl">наш, по нашим же статьям об экзаменах</span></div>'
        + "</div></body></html>")

# ───────────────────── инфографика: круг из четырёх навыков ─────────────────
# три четверти круга — письменный экзамен, одна четверть — устный
QUARTER = 90
SEG = []
for i, sk in enumerate(SKILLS):
    owner = "HSK" if sk in COVER["HSK"] else "HSKK"
    SEG.append((sk, owner, i * QUARTER))
assert [o for s, o, a in SEG].count("HSK") == 3
assert [o for s, o, a in SEG].count("HSKK") == 1

# конический градиент: три сектора одного цвета, четвёртый другого
STOPS = []
for sk, owner, start in SEG:
    col = "var(--brick)" if owner == "HSK" else "#C9637A"
    STOPS.append("%s %ddeg %ddeg" % (col, start, start + QUARTER))
CONIC = "conic-gradient(from 0deg, " + ", ".join(STOPS) + ")"

# подписи ставятся по центрам секторов: conic-gradient идёт по часовой
# стрелке от двенадцати часов, значит первый навык занимает верх-право
CORNERS = ["top:-10px;left:58%", "bottom:-10px;left:58%",
           "bottom:-10px;right:58%", "top:-10px;right:58%"]
labels = ""
for (sk, owner, start), style in zip(SEG, CORNERS):
    cls = "lb2" + ("" if owner == "HSK" else " alt")
    labels += ('<div class="' + cls + '" style="' + style + '">'
               + CAP[sk] + "</div>")
assert labels.count("lb2") == 4
assert labels.count("alt") == 1, "подсвечена ровно одна подпись — навык устного"
# порядок подписей должен совпадать с порядком секторов
assert [sk for sk, o, a in SEG] == SKILLS, "сектора идут в порядке навыков"

FIG_CSS = BASE + """
html,body{width:1200px;height:520px}
.card{width:1200px;height:520px;padding:22px 48px 14px 64px}
.head{display:flex;justify-content:space-between;align-items:flex-start;gap:34px;
 margin-bottom:10px}
h1{font-size:30px;max-width:27ch}
.tip{background:var(--surface);border:1px solid var(--hair);border-left:4px solid var(--brick);
 border-radius:13px;padding:10px 15px;font-size:13px;color:var(--ink-2);line-height:1.33;
 flex:0 0 302px}
.tip b{color:var(--ink)}
.body{flex:1 1 auto;display:flex;align-items:center;gap:52px}
.ring{flex:0 0 286px;height:286px;position:relative;margin:14px 0}
.disc{width:286px;height:286px;border-radius:50%;background:CONIC_BG}
.hole{position:absolute;left:50%;top:50%;transform:translate(-50%,-50%);width:128px;
 height:128px;border-radius:50%;background:var(--cream);display:flex;align-items:center;
 justify-content:center;text-align:center;font-size:14px;font-weight:700;color:var(--ink-2);
 line-height:1.25;padding:0 10px}
.lb2{position:absolute;background:var(--surface);border:1px solid var(--hair);
 border-radius:8px;padding:4px 11px;font-size:13.5px;font-weight:600;color:var(--ink);
 white-space:nowrap}
.lb2.alt{background:#C9637A;border-color:#B8304B;color:#fff}
.legend{flex:1 1 auto;display:flex;flex-direction:column;gap:18px}
.lg{display:flex;gap:14px;align-items:flex-start}
.sw{flex:0 0 26px;height:26px;border-radius:7px;margin-top:2px}
.sw.a{background:var(--brick)}
.sw.b{background:#C9637A}
.lgt b{display:block;font-size:19px;color:var(--ink)}
.lgt span{font-size:14.5px;color:var(--ink-2);line-height:1.35}
"""
FIG_CSS = FIG_CSS.replace("CONIC_BG", CONIC)

fig = ('<!DOCTYPE html><html lang="ru"><head><meta charset="utf-8">' + FONTS
       + "<style>" + VARS + FIG_CSS + "</style></head><body><div class=\"card\">"
       + '<div class="head"><div>'
       + '<div class="eyebrow">Четыре навыка, два экзамена</div>'
       + '<h1>Полный круг собирается <i>только из двух сертификатов</i></h1></div>'
       + '<div class="tip"><b>Круг — это язык целиком.</b> Каждая четверть — один '
         'навык, цвет — экзамен, который его проверяет</div></div>'
       + '<div class="body"><div class="ring"><div class="disc"></div>'
       + '<div class="hole">Язык<br>целиком</div>' + labels + '</div>'
       + '<div class="legend">'
       + '<div class="lg"><span class="sw a"></span><div class="lgt">'
         '<b>Письменный экзамен</b><span>закрывает три четверти: аудирование, '
         'чтение и письмо. Речь не проверяется вовсе</span></div></div>'
       + '<div class="lg"><span class="sw b"></span><div class="lgt">'
         '<b>Устный экзамен</b><span>закрывает оставшуюся четверть. Отдельная '
         'регистрация, отдельный сертификат, три уровня вместо шести</span></div></div>'
       + '</div></div>'
       + '<div class="foot"><span class="lb">Что это значит</span>'
       + '<span class="vl">подтвердить язык целиком — это <b>две записи и два '
         'сертификата</b></span>'
       + '<span class="lb">Разбор</span>'
       + '<span class="vl">наш, а не официальная классификация</span></div>'
       + "</div></body></html>")

open(S + "mzd-hero.html", "w", encoding="utf-8").write(hero)
open(S + "mzd-info.html", "w", encoding="utf-8").write(fig)
print("готово: mzd-hero.html, mzd-info.html")
