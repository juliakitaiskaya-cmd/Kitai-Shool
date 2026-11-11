# -*- coding: utf-8 -*-
# Картинки к статье «Частица 了 (le) в китайском языке»
# Обложка     — до и после: три пары фраз без частицы и с ней
# Инфографика — ось времени, на которой частица стоит во всех трёх точках
import sys
sys.path.insert(0, "/home/user/Kitai-Shool/content")
from le import PAIRS, TIMELINE, ROLES

S = ("/tmp/claude-0/-home-user-Kitai-Shool/a463bfca-82a9-56fd-ae09-42a7257ff999/"
     "scratchpad/")

FONTS = ("<link href=\"https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,600;0,700;1,600"
         "&family=Inter:wght@400;500;600;700&family=Noto+Serif+SC:wght@600;700&display=swap\" rel=\"stylesheet\">")
VARS = (":root{--brick:#A41E3A;--brick-d:#841630;--brick-soft:#F7E6EB;--ink:#2C2420;--ink-2:#5A4F45;"
        "--taupe:#8B7D6B;--cream:#FAF7F2;--cream-2:#F3EDE3;--hair:#EAE3D8;--surface:#fff;"
        "--grey-soft:#EFEDE8}")

assert len(PAIRS) == 3 and len(TIMELINE) == 3


def mark_le(ex):
    """Подсветить саму частицу внутри фразы."""
    return ex.replace("了", '<em>了</em>')


# ─────────── обложка: до и после ───────────
rows = ""
for a, apy, atr, b, bpy, btr, role in PAIRS:
    assert "了" not in a and "了" in b
    rows += ("""<div class="pr">
  <div class="half">
    <span class="lbl">без частицы</span>
    <span class="zh">%(a)s</span>
    <span class="tr">%(atr)s</span>
  </div>
  <div class="arrow"><span>+ 了</span></div>
  <div class="half on">
    <span class="lbl">с частицей</span>
    <span class="zh">%(b)s</span>
    <span class="tr">%(btr)s</span>
  </div>
  <div class="role">%(role)s</div>
</div>""" % dict(a=a, atr=atr, b=mark_le(b), btr=btr, role=role))
assert rows.count('class="pr"') == 3

hero = """<!DOCTYPE html><html lang="ru"><head><meta charset="utf-8">
%(fonts)s
<style>
%(vars)s
*{margin:0;box-sizing:border-box}html,body{width:1200px;height:630px}
.card{width:1200px;height:630px;background:radial-gradient(1040px 700px at 10%% 4%%, #fff 0%%, var(--cream) 54%%, var(--cream-2) 100%%);position:relative;overflow:hidden;font-family:'Inter',sans-serif;padding:28px 56px 50px 72px;display:flex;flex-direction:column}
.card:before{content:"";position:absolute;left:0;top:0;bottom:0;width:12px;background:var(--brick)}
.head{display:flex;justify-content:space-between;align-items:flex-end;gap:34px;margin-bottom:16px}
.eyebrow{color:var(--brick);font-weight:700;font-size:18px;letter-spacing:.19em;text-transform:uppercase;margin-bottom:8px}
h1{font-family:'Cormorant Garamond',serif;font-weight:600;font-size:38px;line-height:1.07;color:var(--ink);letter-spacing:-.3px;max-width:26ch}
h1 i{font-style:italic;color:var(--brick)}
.tip{flex:0 0 322px;background:var(--surface);border:1px solid var(--hair);border-left:4px solid var(--brick);border-radius:13px;padding:12px 18px;font-size:14.5px;color:var(--ink-2);line-height:1.38}
.tip b{color:var(--ink)}

.rows{flex:1 1 auto;display:flex;flex-direction:column;gap:12px}
.pr{flex:1 1 0;background:var(--surface);border:1px solid var(--hair);border-radius:15px;padding:12px 22px;display:flex;align-items:center;gap:20px}
.half{flex:0 0 300px;background:var(--grey-soft);border-radius:12px;padding:10px 16px}
.half.on{background:var(--brick-soft);border:1.5px solid var(--brick);padding:8.5px 14.5px}
.half .lbl{display:block;font-size:10.5px;letter-spacing:.1em;text-transform:uppercase;color:var(--taupe);margin-bottom:3px}
.half.on .lbl{color:var(--brick)}
.half .zh{display:block;font-family:'Noto Serif SC',serif;font-weight:600;font-size:27px;color:var(--ink);line-height:1.2}
.half .zh em{font-style:normal;color:var(--brick-d);border-bottom:3px solid var(--brick)}
.half .tr{display:block;font-size:14px;color:var(--ink-2);margin-top:4px}
.arrow{flex:0 0 auto;text-align:center}
.arrow span{display:inline-block;background:var(--brick);color:#fff;font-family:'Noto Serif SC',serif;font-weight:700;font-size:17px;border-radius:9px;padding:6px 12px}
.role{flex:1 1 auto;border-left:1px solid var(--hair);padding-left:24px;font-size:15.5px;font-weight:600;color:var(--brick-d);line-height:1.3}

.foot{margin-top:14px;display:flex;align-items:center;gap:18px;background:var(--surface);border:1px solid var(--hair);border-radius:13px;padding:11px 22px}
.foot b{font-size:12.5px;font-weight:700;letter-spacing:.11em;text-transform:uppercase;color:var(--brick);flex:0 0 auto}
.foot span{font-size:15px;color:var(--ink);line-height:1.36}

.brand{position:absolute;left:72px;bottom:16px;display:flex;align-items:center;gap:11px;color:var(--ink)}
.brand b{font-family:'Cormorant Garamond',serif;font-weight:700;font-size:24px}
.brand .bdot{width:10px;height:10px;border-radius:50%%;background:var(--brick)}
.brand span{color:var(--taupe);font-size:15px}
</style></head><body>
<div class="card">
  <div class="head">
    <div>
      <div class="eyebrow">Грамматика</div>
      <h1>Что меняет 了: <i>одна и та же фраза до и после</i></h1>
    </div>
    <div class="tip">Частица не переносит фразу в прошлое. <b>Она сообщает, что действие закончено или что положение дел стало другим.</b></div>
  </div>

  <div class="rows">%(rows)s</div>

  <div class="foot"><b>место решает</b><span>после глагола частица говорит про само действие, в конце фразы — про перемену</span></div>

  <div class="brand"><span class="bdot"></span><b>Kitai School</b><span>&middot; kitai-school.ru</span></div>
</div>
</body></html>""" % dict(fonts=FONTS, vars=VARS, rows=rows)

open(S + "le-hero.html", "w", encoding="utf-8").write(hero)

# ─────────── инфографика: ось времени ───────────
cells = ""
for mark, ex, py, tr, role in TIMELINE:
    assert "了" in ex
    cells += ("""<div class="tp">
  <div class="dot"></div>
  <div class="mark">%(mark)s</div>
  <div class="body">
    <span class="zh">%(ex)s</span>
    <span class="py">%(py)s</span>
    <span class="tr">%(tr)s</span>
  </div>
  <div class="role"><span>работа частицы</span>%(role)s</div>
</div>""" % dict(mark=mark, ex=mark_le(ex), py=py, tr=tr, role=role))
assert cells.count('class="tp"') == 3
assert "завтра" in cells, "будущее на оси обязательно"

info = """<!DOCTYPE html><html lang="ru"><head><meta charset="utf-8">
%(fonts)s
<style>
%(vars)s
*{margin:0;box-sizing:border-box}html,body{width:1200px;height:%(h)dpx}
.wrap{width:1200px;height:%(h)dpx;background:linear-gradient(180deg,#fff 0%%,var(--cream) 46%%,var(--cream-2) 100%%);font-family:'Inter',sans-serif;padding:30px 48px 26px;display:flex;flex-direction:column;position:relative;overflow:hidden}
.wrap:before{content:"";position:absolute;left:0;right:0;top:0;height:9px;background:var(--brick)}
.top{display:flex;align-items:flex-end;justify-content:space-between;gap:34px;margin-bottom:22px}
.eyebrow{color:var(--brick);font-weight:700;font-size:15.5px;letter-spacing:.19em;text-transform:uppercase;margin-bottom:7px}
h2{font-family:'Cormorant Garamond',serif;font-weight:600;font-size:34px;line-height:1.08;color:var(--ink);max-width:24ch}
h2 i{font-style:italic;color:var(--brick)}
.hint0{flex:0 0 342px;background:var(--surface);border:1px solid var(--hair);border-left:4px solid var(--brick);border-radius:13px;padding:11px 17px;font-size:14px;color:var(--ink-2);line-height:1.35}
.hint0 b{color:var(--ink)}

.axis{position:relative;flex:1 1 auto;min-height:0;display:flex;gap:18px;padding-top:30px}
.axis:before{content:"";position:absolute;left:30px;right:30px;top:12px;height:3px;background:var(--brick);opacity:.35;border-radius:2px}
.tp{flex:1 1 0;position:relative;display:flex;flex-direction:column;background:var(--surface);border:1px solid var(--hair);border-radius:15px;padding:18px 20px 16px}
.dot{position:absolute;top:-24px;left:50%%;transform:translateX(-50%%);width:17px;height:17px;border-radius:50%%;background:var(--brick);border:4px solid #fff;box-shadow:0 0 0 1px var(--hair)}
.mark{text-align:center;font-size:12px;font-weight:700;letter-spacing:.13em;text-transform:uppercase;color:var(--brick);padding-bottom:11px;border-bottom:1px solid var(--hair)}
.body{margin-top:14px;text-align:center}
.body .zh{display:block;font-family:'Noto Serif SC',serif;font-weight:600;font-size:27px;color:var(--ink);line-height:1.25}
.body .zh em{font-style:normal;color:var(--brick-d);border-bottom:3px solid var(--brick)}
.body .py{display:block;font-size:13.5px;color:var(--taupe);margin-top:5px}
.body .tr{display:block;font-size:15px;color:var(--ink-2);margin-top:7px;line-height:1.34}
.role{margin-top:auto;margin-top:14px;background:var(--brick-soft);border-radius:10px;padding:9px 12px;font-size:13.5px;font-weight:600;color:var(--brick-d);line-height:1.34;text-align:center}
.role span{display:block;font-size:10.5px;letter-spacing:.1em;text-transform:uppercase;color:var(--brick);font-weight:700;margin-bottom:3px}

.foot{margin-top:18px;flex:0 0 auto;display:flex;align-items:center;gap:18px}
.foot .msg{flex:1 1 auto;background:var(--surface);border:1px solid var(--hair);border-radius:14px;padding:11px 20px;font-size:14.5px;color:var(--ink);line-height:1.34}
.foot .msg b{color:var(--brick)}
.brand{display:flex;align-items:center;gap:10px;color:var(--ink);flex:0 0 auto}
.brand b{font-family:'Cormorant Garamond',serif;font-weight:700;font-size:23px}
.brand .dot2{width:9px;height:9px;border-radius:50%%;background:var(--brick)}
.brand span{color:var(--taupe);font-size:15px}
</style></head><body>
<div class="wrap">
  <div class="top">
    <div>
      <div class="eyebrow">Ось времени</div>
      <h2>Частица стоит везде — <i>значит, дело не во времени</i></h2>
    </div>
    <div class="hint0">Вчера, сейчас и завтра. <b>Время держат слова «вчера» и «завтра», а частица отвечает за завершённость и перемену.</b></div>
  </div>

  <div class="axis">%(cells)s</div>

  <div class="foot">
    <div class="msg">Фраза о завтрашнем дне и ставит точку в споре: <b>будь частица прошедшим временем, в последней колонке её бы не было</b></div>
    <div class="brand"><span class="dot2"></span><b>Kitai School</b><span>&middot; kitai-school.ru</span></div>
  </div>
</div>
</body></html>""" % dict(fonts=FONTS, vars=VARS, h=505, cells=cells)

open(S + "le-info.html", "w", encoding="utf-8").write(info)

print("ok | пар:", len(PAIRS), "| точек оси:", len(TIMELINE))
