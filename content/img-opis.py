# -*- coding: utf-8 -*-
# Картинки к статье «Уровни китайского языка и их описание»
# Обложка     — верстовые столбы: на каждом уровне подпись, что отсюда можете
# Инфографика — карта готовности: ситуации против уровней
import sys
sys.path.insert(0, "/home/user/Kitai-Shool/content")
from opis import SCEN, MILES, MAX_LEVEL

S = ("/tmp/claude-0/-home-user-Kitai-Shool/a463bfca-82a9-56fd-ae09-42a7257ff999/"
     "scratchpad/")

FONTS = ("<link href=\"https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,600;0,700;1,600"
         "&family=Inter:wght@400;500;600;700&family=Noto+Serif+SC:wght@600;700&display=swap\" rel=\"stylesheet\">")
VARS = (":root{--brick:#A41E3A;--brick-d:#841630;--brick-soft:#F7E6EB;--ink:#2C2420;--ink-2:#5A4F45;"
        "--taupe:#8B7D6B;--cream:#FAF7F2;--cream-2:#F3EDE3;--hair:#EAE3D8;--surface:#fff;"
        "--paper:#FFFDF8;--good:#2F6F4F;--good-soft:#E8F3EC;--grey:#8A8178;--grey-soft:#EFEDE8}")

assert len(MILES) == MAX_LEVEL
assert len(SCEN) == 7

# ─────────── обложка: верстовые столбы ───────────
posts = ""
for i, (lvl, what) in enumerate(MILES):
    h = 42 + i * 30          # столб растёт вместе с уровнем
    posts += ('<div class="post"><div class="plate">%s</div>'
              '<div class="pole" style="height:%dpx"><span>%d</span></div></div>'
              % (what, h, lvl))
assert posts.count('class="post"') == MAX_LEVEL
assert posts.count('class="pole"') == MAX_LEVEL

hero = """<!DOCTYPE html><html lang="ru"><head><meta charset="utf-8">
%(fonts)s
<style>
%(vars)s
*{margin:0;box-sizing:border-box}html,body{width:1200px;height:630px}
.card{width:1200px;height:630px;background:radial-gradient(1040px 700px at 12%% 4%%, #fff 0%%, var(--cream) 54%%, var(--cream-2) 100%%);position:relative;overflow:hidden;font-family:'Inter',sans-serif;padding:28px 56px 50px 72px;display:flex;flex-direction:column}
.card:before{content:"";position:absolute;left:0;top:0;bottom:0;width:12px;background:var(--brick)}
.head{display:flex;justify-content:space-between;align-items:flex-end;gap:34px;margin-bottom:18px}
.eyebrow{color:var(--brick);font-weight:700;font-size:18px;letter-spacing:.19em;text-transform:uppercase;margin-bottom:8px}
h1{font-family:'Cormorant Garamond',serif;font-weight:600;font-size:36px;line-height:1.07;color:var(--ink);letter-spacing:-.3px;max-width:22ch}
h1 i{font-style:italic;color:var(--brick)}
.tip{flex:0 0 324px;background:var(--surface);border:1px solid var(--hair);border-left:4px solid var(--brick);border-radius:13px;padding:12px 18px;font-size:14.5px;color:var(--ink-2);line-height:1.38}
.tip b{color:var(--ink)}

.road{flex:1 1 auto;display:flex;align-items:flex-end;gap:14px;position:relative;padding-bottom:16px}
.road:after{content:"";position:absolute;left:0;right:0;bottom:0;height:3px;background:var(--hair);border-radius:2px}
.post{flex:1 1 0;display:flex;flex-direction:column;align-items:center;justify-content:flex-end;gap:9px}
.plate{background:var(--surface);border:1px solid var(--hair);border-radius:11px;padding:10px 12px;font-size:13.5px;color:var(--ink-2);line-height:1.34;text-align:center;min-height:76px;display:flex;align-items:center}
.pole{width:52px;background:var(--brick-soft);border:1px solid var(--brick);border-radius:9px 9px 0 0;display:flex;align-items:flex-start;justify-content:center;padding-top:8px}
.pole span{font-size:22px;font-weight:700;color:var(--brick-d);line-height:1}

.foot{margin-top:16px;display:flex;align-items:center;gap:18px;background:var(--surface);border:1px solid var(--hair);border-radius:13px;padding:11px 22px}
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
      <div class="eyebrow">Обучение</div>
      <h1>Уровни китайского языка: <i>что вы умеете на каждой отметке</i></h1>
    </div>
    <div class="tip">Уровень удобнее описывать делами, а не числом слов. <b>Важнее не номер, а список того, что уже получается.</b></div>
  </div>

  <div class="road">%(posts)s</div>

  <div class="foot"><b>и обратная сторона</b><span>на каждой отметке есть и то, чего пока нет: именно эта половина показывает, куда двигаться дальше</span></div>

  <div class="brand"><span class="bdot"></span><b>Kitai School</b><span>&middot; kitai-school.ru</span></div>
</div>
</body></html>""" % dict(fonts=FONTS, vars=VARS, posts=posts)

open(S + "opis-hero.html", "w", encoding="utf-8").write(hero)

# ─────────── инфографика: карта готовности ───────────
head_cells = "".join('<div class="hc">%d</div>' % n for n in range(1, MAX_LEVEL + 1))
rows_html = ""
for what, lvl, can, cant in SCEN:
    cells = ""
    for n in range(1, MAX_LEVEL + 1):
        if n < lvl:
            cells += '<div class="c no"></div>'
        elif n == lvl:
            cells += '<div class="c on">с этой</div>'
        else:
            cells += '<div class="c yes"></div>'
    rows_html += ('<div class="r"><div class="rl">%s</div>%s'
                  '<div class="rc">%s</div></div>' % (what, cells, can))
assert rows_html.count('class="r"') == len(SCEN)
assert rows_html.count('class="c on"') == len(SCEN), "у каждой ситуации одна отметка начала"

info = """<!DOCTYPE html><html lang="ru"><head><meta charset="utf-8">
%(fonts)s
<style>
%(vars)s
*{margin:0;box-sizing:border-box}html,body{width:1200px;height:%(h)dpx}
.wrap{width:1200px;height:%(h)dpx;background:linear-gradient(180deg,#fff 0%%,var(--cream) 44%%,var(--cream-2) 100%%);font-family:'Inter',sans-serif;padding:28px 48px 18px;display:flex;flex-direction:column;position:relative;overflow:hidden}
.wrap:before{content:"";position:absolute;left:0;right:0;top:0;height:9px;background:var(--brick)}
.top{display:flex;align-items:flex-end;justify-content:space-between;gap:34px;margin-bottom:14px}
.eyebrow{color:var(--brick);font-weight:700;font-size:15.5px;letter-spacing:.19em;text-transform:uppercase;margin-bottom:7px}
h2{font-family:'Cormorant Garamond',serif;font-weight:600;font-size:33px;line-height:1.08;color:var(--ink);max-width:24ch}
h2 i{font-style:italic;color:var(--brick)}
.hint{flex:0 0 346px;background:var(--surface);border:1px solid var(--hair);border-left:4px solid var(--brick);border-radius:13px;padding:11px 17px;font-size:14px;color:var(--ink-2);line-height:1.35}
.hint b{color:var(--ink)}

.grid{flex:1 1 auto;min-height:0;display:flex;flex-direction:column;gap:6px}
.hr{display:flex;align-items:center;gap:6px;padding-bottom:2px}
.hr .rl{flex:0 0 190px;font-size:12px;font-weight:700;letter-spacing:.12em;text-transform:uppercase;color:var(--taupe)}
.hr .rc{flex:0 0 268px;font-size:12px;font-weight:700;letter-spacing:.12em;text-transform:uppercase;color:var(--taupe);padding-left:10px}
.hc{flex:1 1 0;text-align:center;font-size:13px;font-weight:700;color:var(--taupe)}
.r{flex:1 1 0;display:flex;align-items:stretch;gap:6px}
.rl{flex:0 0 190px;display:flex;align-items:center;font-size:14px;color:var(--ink);font-weight:500}
.c{flex:1 1 0;border-radius:8px;display:flex;align-items:center;justify-content:center;font-size:11.5px;font-weight:700;color:#fff}
.c.no{background:var(--grey-soft)}
.c.on{background:var(--brick)}
.c.yes{background:var(--brick-soft);border:1px solid var(--brick)}
.rc{flex:0 0 268px;display:flex;align-items:center;font-size:13px;color:var(--ink-2);line-height:1.3;padding-left:10px}

.foot{margin-top:12px;flex:0 0 auto;display:flex;align-items:center;gap:18px}
.foot .msg{flex:1 1 auto;background:var(--surface);border:1px solid var(--hair);border-radius:14px;padding:10px 20px;font-size:14px;color:var(--ink);line-height:1.34}
.foot .msg b{color:var(--brick)}
.brand{display:flex;align-items:center;gap:10px;color:var(--ink);flex:0 0 auto}
.brand b{font-family:'Cormorant Garamond',serif;font-weight:700;font-size:23px}
.brand .dot2{width:9px;height:9px;border-radius:50%%;background:var(--brick)}
.brand span{color:var(--taupe);font-size:15px}
</style></head><body>
<div class="wrap">
  <div class="top">
    <div>
      <div class="eyebrow">Карта готовности</div>
      <h2>С какого уровня <i>ситуация перестаёт быть проблемой</i></h2>
    </div>
    <div class="hint">Серое — ещё трудно, тёмная клетка — отсюда справляетесь, светлая — дальше только легче. <b>Быт идёт впереди работы с текстом.</b></div>
  </div>

  <div class="grid">
    <div class="hr"><div class="rl">ситуация</div>%(head)s<div class="rc">что получается</div></div>
    %(rows)s
  </div>

  <div class="foot">
    <div class="msg">Номер уровня важен для вуза и работодателя, а для себя полезнее <b>список дел, с которыми справляетесь</b></div>
    <div class="brand"><span class="dot2"></span><b>Kitai School</b><span>&middot; kitai-school.ru</span></div>
  </div>
</div>
</body></html>""" % dict(fonts=FONTS, vars=VARS, h=560, head=head_cells, rows=rows_html)

open(S + "opis-info.html", "w", encoding="utf-8").write(info)

print("ok | вех:", len(MILES), "| сценариев:", len(SCEN), "| шкала до:", MAX_LEVEL)
