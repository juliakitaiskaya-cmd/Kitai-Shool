# -*- coding: utf-8 -*-
# Картинки к статье «HSK 4 — это intermediate?»
# Обложка     — воронка: 300 значений → 6 уровней → 5 слов
# Инфографика — полоса баллов 0–300: весь отрезок от порога даёт один сертификат
import sys
sys.path.insert(0, "/home/user/Kitai-Shool/content")
from interm import STEPS, LOSS, TOP, THRESHOLD, SPREAD, SHARE, NARROW_1

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

# ───────────────────── обложка: воронка из трёх ступеней ─────────────────────
# высота столбца показывает, сколько значений остаётся на каждом шаге;
# шкала логарифмическая, иначе второй и третий столбцы были бы неразличимы
import math
HMAX = 238.0
heights = [int(round(HMAX * math.log10(v + 1) / math.log10(LOSS[0] + 1)))
           for v in LOSS]
assert heights[0] > heights[1] > heights[2], "воронка сужается: %s" % heights

cols = ""
for (where, was, now, left), h in zip(STEPS, heights):
    cols += ('<div class="col"><div class="n">' + str(left) + '</div>'
             '<div class="bar" style="height:' + str(h) + 'px"></div>'
             '<div class="wh">' + where + '</div>'
             '<div class="wt">' + now + "</div></div>")
assert cols.count('class="col"') == 3

HERO_CSS = BASE + """
html,body{width:1200px;height:630px}
.card{width:1200px;height:630px;padding:28px 48px 20px 64px}
h1{font-size:44px;max-width:46ch;margin-bottom:6px}
.sub{font-size:16px;color:var(--ink-2);margin-bottom:14px;max-width:84ch;line-height:1.35}
.row{flex:1 1 auto;display:flex;align-items:flex-end;gap:30px}
.cols{flex:1 1 auto;display:flex;align-items:flex-end;gap:34px}
.col{flex:1 1 0;display:flex;flex-direction:column;align-items:center;text-align:center}
.n{font-size:36px;font-weight:700;color:var(--brick);line-height:1;margin-bottom:7px;
 letter-spacing:-1px}
.bar{width:100%;max-width:168px;border-radius:12px 12px 0 0;
 background:linear-gradient(180deg,#B8304B 0%,var(--brick) 100%)}
.wh{font-size:16px;font-weight:700;color:var(--ink);margin-top:10px;
 border-top:2px solid var(--hair);width:100%;max-width:168px;padding-top:8px}
.wt{font-size:13px;color:var(--ink-2);line-height:1.3;margin-top:5px;max-width:178px}
.aside{flex:0 0 266px;background:var(--surface);border:1px solid var(--hair);
 border-left:4px solid var(--brick);border-radius:14px;padding:16px 18px;
 margin-bottom:34px}
.aside b{display:block;font-size:18px;color:var(--ink);line-height:1.25}
.aside span{display:block;font-size:14px;color:var(--ink-2);line-height:1.35;
 margin-top:8px}
"""

hero = ('<!DOCTYPE html><html lang="ru"><head><meta charset="utf-8">' + FONTS
        + "<style>" + VARS + HERO_CSS + "</style></head><body><div class=\"card\">"
        + '<div class="eyebrow">Уровень словами и уровень числом</div>'
        + '<h1>Чем дальше от экзамена, <i>тем меньше смысла остаётся</i></h1>'
        + '<div class="sub">Сколько различимых значений остаётся на каждом шаге. '
          'Высота столбцов по сжатой шкале: иначе второй и третий были бы '
          'неразличимы</div>'
        + '<div class="row"><div class="cols">' + cols + '</div>'
        + '<div class="aside"><b>Обратно не восстанавливается</b>'
          '<span>По слову нельзя назвать ни уровень, ни балл — как по слову '
          '«высокий» нельзя назвать рост в сантиметрах</span></div></div>'
        + '<div class="foot"><span class="lb">Что писать</span>'
        + '<span class="vl">экзамен, <b>номер уровня и год</b> — это '
          'проверяемо</span>'
        + '<span class="lb">Расчёт</span>'
        + '<span class="vl">наш, по нашим же разборам баллов</span></div>'
        + "</div></body></html>")

# ───────────────────── инфографика: полоса баллов ─────────────────────
W = 980
x_th = int(round(W * THRESHOLD / float(TOP)))
w_pass = W - x_th
assert x_th + w_pass == W

ticks = ""
for v in (0, 60, 120, THRESHOLD, 240, TOP):
    x = int(round(W * v / float(TOP)))
    cls = "tk hot" if v == THRESHOLD else "tk"
    ticks += ('<div class="' + cls + '" style="left:' + str(x) + 'px">'
              '<div class="tl"></div><div class="tn">' + str(v) + "</div></div>")
assert ticks.count('class="tk') == 6

FIG_CSS = BASE + """
html,body{width:1200px;height:520px}
.card{width:1200px;height:520px;padding:22px 48px 14px 64px}
.head{display:flex;justify-content:space-between;align-items:flex-start;gap:34px;
 margin-bottom:22px}
h1{font-size:33px;max-width:46ch}
.tip{background:var(--surface);border:1px solid var(--hair);border-left:4px solid var(--brick);
 border-radius:13px;padding:10px 15px;font-size:13px;color:var(--ink-2);line-height:1.33;
 flex:0 0 300px}
.tip b{color:var(--ink)}
.plot{flex:1 1 auto;display:flex;flex-direction:column;justify-content:center;
 padding-left:4px}
.scale{position:relative;height:286px}
.track{position:absolute;left:0;top:72px;height:116px;width:980px;border-radius:12px;
 background:var(--grey-soft);border:1px solid var(--hair)}
.pass{position:absolute;top:72px;height:116px;border-radius:0 14px 14px 0;
 background:linear-gradient(90deg,#C9637A 0%,var(--brick) 100%);
 display:flex;align-items:center;justify-content:center;color:#fff;
 font-weight:700;text-align:center;padding:0 16px;line-height:1.3;font-size:19px}
.fail{position:absolute;top:72px;height:116px;display:flex;align-items:center;
 justify-content:center;font-size:15px;color:var(--taupe);font-weight:600}
.tk{position:absolute;top:198px;transform:translateX(-50%);text-align:center}
.tl{width:2px;height:12px;background:var(--grey);margin:0 auto}
.tn{font-size:14px;font-weight:700;color:var(--ink-2);margin-top:4px}
.tk.hot .tl{background:var(--brick);width:3px;height:140px;margin-top:-128px}
.tk.hot .tn{color:var(--brick);font-size:17px}
.cap{position:absolute;top:22px;font-size:14px;font-weight:700;color:var(--brick)}
.note{margin-top:14px;font-size:16px;color:var(--ink-2);line-height:1.4;max-width:96ch}
.note b{color:var(--ink)}
"""

fig = ('<!DOCTYPE html><html lang="ru"><head><meta charset="utf-8">' + FONTS
       + "<style>" + VARS + FIG_CSS + "</style></head><body><div class=\"card\">"
       + '<div class="head"><div>'
       + '<div class="eyebrow">Один сертификат на сто двадцать баллов</div>'
       + '<h1>Порог взят — и дальше <i>все одинаковые</i></h1></div>'
       + '<div class="tip"><b>Полоса — все возможные баллы старших уровней.</b> '
         'Закрашен отрезок, который даёт сданный уровень</div></div>'
       + '<div class="plot"><div class="scale">'
       + '<div class="track"></div>'
       + '<div class="fail" style="left:0;width:' + str(x_th) + 'px">уровень не сдан</div>'
       + '<div class="pass" style="left:' + str(x_th) + 'px;width:' + str(w_pass)
       + 'px">один и тот же сертификат на всём этом отрезке</div>'
       + '<div class="cap" style="left:' + str(x_th + 10) + 'px">порог '
       + str(THRESHOLD) + ' из ' + str(TOP) + ' — ' + str(SHARE) + ' %</div>'
       + ticks + '</div>'
       + '<div class="note">В самом сертификате балл стоит рядом с уровнем — а в анкете остаётся <b>одно слово на весь закрашенный отрезок</b>. Поэтому слово и не говорит, где внутри уровня человек находится</div></div>'
       + '<div class="foot"><span class="lb">Разброс</span>'
       + '<span class="vl"><b>' + str(SPREAD) + ' баллов</b> между тем, кто взял порог '
         'впритык, и тем, кто почти не ошибался</span>'
       + '<span class="lb">Расчёт</span>'
       + '<span class="vl">наш, по нашим же разборам баллов</span></div>'
       + "</div></body></html>")

open(S + "int-hero.html", "w", encoding="utf-8").write(hero)
open(S + "int-info.html", "w", encoding="utf-8").write(fig)
print("готово: int-hero.html, int-info.html")
