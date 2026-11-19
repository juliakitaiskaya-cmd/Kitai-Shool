# -*- coding: utf-8 -*-
# Картинки к статье «Можно ли сдать HSK онлайн»
# Обложка     — три ворот подряд: уровень, дата, страна
# Инфографика — схема двух стран и вынесенная верхняя ступень
import sys
sys.path.insert(0, "/home/user/Kitai-Shool/content")
from online import CONDS, TOP_BAND, DEADLINE_MIN, DEADLINE_MAX

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

# ───────────────────── обложка: три ворот ─────────────────────
gates = ""
for i, (name, what, st) in enumerate(CONDS, start=1):
    gates += ('<div class="gate"><div class="num">' + str(i) + '</div>'
              '<div class="nm">' + name + '</div>'
              '<div class="wh">' + what + '</div>'
              '<div class="lock">решаете не вы</div></div>')
    if i < len(CONDS):
        gates += '<div class="arrow">→</div>'
assert gates.count('class="gate"') == 3 and gates.count('class="arrow"') == 2

HERO_CSS = BASE + """
html,body{width:1200px;height:630px}
.card{width:1200px;height:630px;padding:26px 48px 20px 64px}
.head{display:flex;justify-content:space-between;align-items:flex-end;gap:30px;margin-bottom:16px}
h1{font-size:40px;max-width:22ch}
.tip{flex:0 0 330px}
.row{flex:1 1 auto;display:flex;align-items:center;gap:16px}
.gate{flex:1 1 0;background:var(--surface);border:1px solid var(--hair);
 border-top:4px solid var(--brick);border-radius:14px;padding:20px 20px 16px;
 display:flex;flex-direction:column;gap:9px;min-height:240px}
.num{width:36px;height:36px;border-radius:10px;background:var(--brick-soft);
 color:var(--brick);font-size:18px;font-weight:700;display:flex;align-items:center;
 justify-content:center}
.nm{font-size:23px;font-weight:700;color:var(--ink)}
.wh{font-size:15px;color:var(--ink-2);line-height:1.38}
.lock{margin-top:auto;font-size:12.5px;font-weight:700;letter-spacing:.09em;
 text-transform:uppercase;color:var(--taupe);border-top:1px dashed var(--grey);
 padding-top:10px}
.arrow{flex:0 0 auto;font-size:28px;color:var(--taupe)}
"""

hero = ('<!DOCTYPE html><html lang="ru"><head><meta charset="utf-8">' + FONTS
        + "<style>" + VARS + HERO_CSS + "</style></head><body><div class=\"card\">"
        + '<div class="head"><div>'
        + '<div class="eyebrow">Экзамен из дома</div>'
        + '<h1>Три условия, <i>и ни одно не зависит от вас</i></h1></div>'
        + '<div class="tip"><b>Техника решает в последнюю очередь.</b> Сначала нужно '
          'пройти все три условия, иначе формат просто не откроют</div></div>'
        + '<div class="row">' + gates + '</div>'
        + '<div class="foot"><span class="lb">Что это значит</span>'
        + '<span class="vl">ответ на «можно ли» всегда про ваш уровень, вашу дату и '
          'вашу страну</span>'
        + '<span class="lb">Запись закрывается</span>'
        + '<span class="vl">за ' + str(DEADLINE_MIN) + '–' + str(DEADLINE_MAX)
        + ' дней, считайте по большему</span></div>'
        + "</div></body></html>")

# ───────────────────── инфографика: две страны ─────────────────────
FIG_CSS = BASE + """
html,body{width:1200px;height:490px}
.card{width:1200px;height:490px;padding:24px 48px 18px 64px}
.head{display:flex;justify-content:space-between;align-items:flex-end;gap:30px;margin-bottom:14px}
h1{font-size:34px;max-width:24ch}
.tip{flex:0 0 330px}
.scene{flex:1 1 auto;display:flex;align-items:center;gap:20px}
.country{flex:0 0 300px;background:var(--surface);border:1px solid var(--hair);
 border-radius:16px;padding:16px 18px;min-height:188px;display:flex;flex-direction:column;
 gap:10px}
.country.b{background:transparent;border-style:dashed;border-color:var(--grey)}
.cname{font-size:12.5px;font-weight:700;letter-spacing:.11em;text-transform:uppercase;
 color:var(--taupe)}
.step{display:flex;align-items:center;gap:10px;font-size:15.5px;color:var(--ink)}
.dot{width:12px;height:12px;border-radius:50%;background:var(--brick);flex:0 0 auto}
.step.off{color:var(--grey)}
.step.off .dot{background:var(--grey-soft);border:1px solid var(--grey)}
.cross{flex:1 1 0;position:relative;height:120px;display:flex;align-items:center;
 justify-content:center}
.line{position:absolute;left:0;right:0;top:50%;height:3px;background:var(--grey-soft)}
.ban{position:relative;background:var(--cream);border:2px solid var(--brick);
 color:var(--brick);border-radius:12px;padding:9px 16px;font-size:15px;font-weight:600;
 text-align:center;line-height:1.3}
.top{flex:0 0 230px;background:var(--brick);color:#fff;border-radius:16px;padding:16px 18px;
 min-height:188px;display:flex;flex-direction:column;gap:8px}
.top .t1{font-size:12.5px;font-weight:700;letter-spacing:.11em;text-transform:uppercase;
 opacity:.85}
.top .t2{font-size:30px;font-weight:700;line-height:1}
.top .t3{font-size:15px;line-height:1.35;margin-top:auto}
"""

fig = ('<!DOCTYPE html><html lang="ru"><head><meta charset="utf-8">' + FONTS
       + "<style>" + VARS + FIG_CSS + "</style></head><body><div class=\"card\">"
       + '<div class="head"><div>'
       + '<div class="eyebrow">Страна и уровень</div>'
       + '<h1>Сдают там же, <i>где записались</i></h1></div>'
       + '<div class="tip"><b>Перенести сдачу через границу нельзя.</b> Это главное, '
         'на чём спотыкаются уезжающие</div></div>'
       + '<div class="scene">'
       + '<div class="country"><div class="cname">Страна записи</div>'
         '<div class="step"><i class="dot"></i>Регистрация</div>'
         '<div class="step"><i class="dot"></i>Экзамен в тот же день сессии</div>'
         '<div class="step"><i class="dot"></i>Документ и фотография</div></div>'
       + '<div class="cross"><div class="line"></div>'
         '<div class="ban">Записаться здесь,<br>а сдать в другой стране нельзя</div></div>'
       + '<div class="country b"><div class="cname">Другая страна</div>'
         '<div class="step off"><i class="dot"></i>Регистрация не переносится</div>'
         '<div class="step off"><i class="dot"></i>Сдача не засчитывается</div>'
         '<div class="step off"><i class="dot"></i>Нужна новая запись на месте</div></div>'
       + '<div class="top"><div class="t1">Верхняя ступень</div>'
         '<div class="t2">HSK ' + TOP_BAND + '</div>'
         '<div class="t3">домашнего формата нет вовсе: только в центре</div></div>'
       + '</div>'
       + '<div class="foot"><span class="lb">Что проверять первым</span>'
       + '<span class="vl">где вы будете в день экзамена — там и записывайтесь</span>'
       + '</div>'
       + "</div></body></html>")

open(S + "onl-hero.html", "w", encoding="utf-8").write(hero)
open(S + "onl-info.html", "w", encoding="utf-8").write(fig)
print("готово: onl-hero.html, onl-info.html")
