# -*- coding: utf-8 -*-
# Картинки к статье «Частицы в китайском языке»
# Обложка     — веер концовок: одна основа фразы и три разные частицы в конце
# Инфографика — карта групп: четыре плитки, в каждой три частицы группы
import sys
sys.path.insert(0, "/home/user/Kitai-Shool/content")
from chasticy import GROUPS, FAN, BASE

S = ("/tmp/claude-0/-home-user-Kitai-Shool/a463bfca-82a9-56fd-ae09-42a7257ff999/"
     "scratchpad/")

FONTS = ("<link href=\"https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,600;0,700;1,600"
         "&family=Inter:wght@400;500;600;700&family=Noto+Serif+SC:wght@600;700&display=swap\" rel=\"stylesheet\">")
VARS = (":root{--brick:#A41E3A;--brick-d:#841630;--brick-soft:#F7E6EB;--ink:#2C2420;--ink-2:#5A4F45;"
        "--taupe:#8B7D6B;--cream:#FAF7F2;--cream-2:#F3EDE3;--hair:#EAE3D8;--surface:#fff;"
        "--grey-soft:#EFEDE8}")

assert len(GROUPS) == 4 and len(FAN) == 3

# ─────────── обложка: веер концовок ───────────
rows = ""
for sign, ex, py, tr, role, expect in FAN:
    tail = ex[len(BASE[0]):]
    assert ex.startswith(BASE[0])
    rows += ("""<div class="br">
  <span class="base">%(base)s</span>
  <span class="tail">%(tail)s</span>
  <div class="txt">
    <span class="py">%(py)s</span>
    <span class="tr">%(tr)s</span>
  </div>
  <div class="exp"><span>что это значит</span>%(expect)s</div>
  <div class="role">%(role)s</div>
</div>""" % dict(base=BASE[0], tail=tail, py=py, tr=tr, role=role, expect=expect))
assert rows.count('class="br"') == 3

hero = """<!DOCTYPE html><html lang="ru"><head><meta charset="utf-8">
%(fonts)s
<style>
%(vars)s
*{margin:0;box-sizing:border-box}html,body{width:1200px;height:630px}
.card{width:1200px;height:630px;background:radial-gradient(1040px 700px at 10%% 4%%, #fff 0%%, var(--cream) 54%%, var(--cream-2) 100%%);position:relative;overflow:hidden;font-family:'Inter',sans-serif;padding:28px 56px 50px 72px;display:flex;flex-direction:column}
.card:before{content:"";position:absolute;left:0;top:0;bottom:0;width:12px;background:var(--brick)}
.head{display:flex;justify-content:space-between;align-items:flex-end;gap:34px;margin-bottom:14px}
.eyebrow{color:var(--brick);font-weight:700;font-size:18px;letter-spacing:.19em;text-transform:uppercase;margin-bottom:8px}
h1{font-family:'Cormorant Garamond',serif;font-weight:600;font-size:38px;line-height:1.07;color:var(--ink);letter-spacing:-.3px;max-width:26ch}
h1 i{font-style:italic;color:var(--brick)}
.tip{flex:0 0 320px;background:var(--surface);border:1px solid var(--hair);border-left:4px solid var(--brick);border-radius:13px;padding:12px 18px;font-size:14.5px;color:var(--ink-2);line-height:1.38}
.tip b{color:var(--ink)}

.rows{flex:1 1 auto;display:flex;flex-direction:column;gap:13px}
.br{flex:1 1 0;background:var(--surface);border:1px solid var(--hair);border-radius:15px;padding:12px 26px;display:flex;align-items:center;gap:0}
.base{font-family:'Noto Serif SC',serif;font-weight:600;font-size:38px;color:var(--ink-2);line-height:1.1;flex:0 0 auto}
.tail{font-family:'Noto Serif SC',serif;font-weight:700;font-size:38px;color:var(--brick-d);line-height:1.1;flex:0 0 auto;background:var(--brick-soft);border-radius:9px;padding:2px 10px;margin-left:6px}
.txt{flex:0 0 300px;padding-left:30px}
.txt .py{display:block;font-size:14px;color:var(--taupe)}
.txt .tr{display:block;font-size:19px;color:var(--ink);font-weight:600;margin-top:3px}
.exp{flex:1 1 auto;padding-left:26px;font-size:14.5px;color:var(--ink-2);line-height:1.34}
.exp span{display:block;font-size:10.5px;letter-spacing:.1em;text-transform:uppercase;color:var(--taupe);margin-bottom:3px}
.role{flex:0 0 190px;text-align:right;font-size:16px;font-weight:700;color:var(--brick);border-left:1px solid var(--hair);padding-left:24px}

.foot{margin-top:13px;display:flex;align-items:center;gap:18px;background:var(--surface);border:1px solid var(--hair);border-radius:13px;padding:11px 22px}
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
      <h1>Одна фраза, три концовки: <i>знак в конце решает всё</i></h1>
    </div>
    <div class="tip">Слова те же, порядок тот же. <b>Меняется только знак в конце — и вместе с ним весь смысл.</b></div>
  </div>

  <div class="rows">%(rows)s</div>

  <div class="foot"><b>без концовки</b><span>фраза «%(base)s» повисает: непонятно, спрашиваете вы, зовёте или сообщаете</span></div>

  <div class="brand"><span class="bdot"></span><b>Kitai School</b><span>&middot; kitai-school.ru</span></div>
</div>
</body></html>""" % dict(fonts=FONTS, vars=VARS, rows=rows, base=BASE[0])

open(S + "chast-hero.html", "w", encoding="utf-8").write(hero)

# ─────────── инфографика: карта групп ───────────
tiles = ""
for i, (name, what, members, ex, py, tr) in enumerate(GROUPS, start=1):
    chips = "".join('<span class="ch">%s</span>' % m for m in members)
    tiles += ("""<div class="tl">
  <div class="num">%(i)d</div>
  <div class="name">%(name)s</div>
  <div class="what">%(what)s</div>
  <div class="chips">%(chips)s</div>
  <div class="ex"><span class="zh">%(ex)s</span><span class="tr">%(tr)s</span></div>
</div>""" % dict(i=i, name=name, what=what, chips=chips, ex=ex, tr=tr))
assert tiles.count('class="tl"') == 4
assert tiles.count('class="ch"') == 12, "по три частицы в каждой из четырёх групп"

info = """<!DOCTYPE html><html lang="ru"><head><meta charset="utf-8">
%(fonts)s
<style>
%(vars)s
*{margin:0;box-sizing:border-box}html,body{width:1200px;height:%(h)dpx}
.wrap{width:1200px;height:%(h)dpx;background:linear-gradient(180deg,#fff 0%%,var(--cream) 46%%,var(--cream-2) 100%%);font-family:'Inter',sans-serif;padding:30px 48px 26px;display:flex;flex-direction:column;position:relative;overflow:hidden}
.wrap:before{content:"";position:absolute;left:0;right:0;top:0;height:9px;background:var(--brick)}
.top{display:flex;align-items:flex-end;justify-content:space-between;gap:34px;margin-bottom:18px}
.eyebrow{color:var(--brick);font-weight:700;font-size:15.5px;letter-spacing:.19em;text-transform:uppercase;margin-bottom:7px}
h2{font-family:'Cormorant Garamond',serif;font-weight:600;font-size:34px;line-height:1.08;color:var(--ink);max-width:24ch}
h2 i{font-style:italic;color:var(--brick)}
.hint0{flex:0 0 346px;background:var(--surface);border:1px solid var(--hair);border-left:4px solid var(--brick);border-radius:13px;padding:11px 17px;font-size:14px;color:var(--ink-2);line-height:1.35}
.hint0 b{color:var(--ink)}

.grid{flex:1 1 auto;min-height:0;display:grid;grid-template-columns:1fr 1fr;grid-template-rows:1fr 1fr;gap:14px}
.tl{position:relative;background:var(--surface);border:1px solid var(--hair);border-radius:15px;padding:14px 20px 13px 22px;display:flex;flex-direction:column}
.num{position:absolute;top:13px;right:18px;font-family:'Cormorant Garamond',serif;font-weight:700;font-size:30px;color:var(--hair);line-height:1}
.name{font-size:18px;font-weight:700;color:var(--ink)}
.what{font-size:13.5px;color:var(--taupe);margin-top:3px;padding-bottom:10px;border-bottom:1px solid var(--hair)}
.chips{display:flex;gap:9px;margin-top:11px}
.ch{font-family:'Noto Serif SC',serif;font-weight:700;font-size:27px;color:var(--brick-d);background:var(--brick-soft);border-radius:10px;padding:4px 14px;line-height:1.25}
.ex{margin-top:auto;padding-top:11px;display:flex;align-items:baseline;gap:12px}
.ex .zh{font-family:'Noto Serif SC',serif;font-weight:600;font-size:21px;color:var(--ink)}
.ex .tr{font-size:14px;color:var(--ink-2)}

.foot{margin-top:16px;flex:0 0 auto;display:flex;align-items:center;gap:18px}
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
      <div class="eyebrow">Карта групп</div>
      <h2>Четыре группы частиц <i>и что делает каждая</i></h2>
    </div>
    <div class="hint0">Деление рабочее, а не единственно верное. <b>Оно нужно, чтобы не перебирать знаки наугад, а искать в нужной группе.</b></div>
  </div>

  <div class="grid">%(tiles)s</div>

  <div class="foot">
    <div class="msg">Три частицы — <b>吗, 的 и 了</b> — разобраны у нас отдельными статьями; здесь они только названы</div>
    <div class="brand"><span class="dot2"></span><b>Kitai School</b><span>&middot; kitai-school.ru</span></div>
  </div>
</div>
</body></html>""" % dict(fonts=FONTS, vars=VARS, h=620, tiles=tiles)

open(S + "chast-info.html", "w", encoding="utf-8").write(info)

print("ok | групп:", len(GROUPS), "| концовок:", len(FAN))
