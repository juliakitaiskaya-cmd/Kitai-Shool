# -*- coding: utf-8 -*-
# Картинки к статье «Частица 的 (de) в китайском языке»
# Обложка     — три слота в предложении: где стоит каждая частица
# Инфографика — позиционная линейка: одна ось предложения с тремя отметками
import sys
sys.path.insert(0, "/home/user/Kitai-Shool/content")
from de import PARTS, POSITIONS

S = ("/tmp/claude-0/-home-user-Kitai-Shool/a463bfca-82a9-56fd-ae09-42a7257ff999/"
     "scratchpad/")

FONTS = ("<link href=\"https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,600;0,700;1,600"
         "&family=Inter:wght@400;500;600;700&family=Noto+Serif+SC:wght@600;700&display=swap\" rel=\"stylesheet\">")
VARS = (":root{--brick:#A41E3A;--brick-d:#841630;--brick-soft:#F7E6EB;--ink:#2C2420;--ink-2:#5A4F45;"
        "--taupe:#8B7D6B;--cream:#FAF7F2;--cream-2:#F3EDE3;--hair:#EAE3D8;--surface:#fff;"
        "--grey-soft:#EFEDE8}")

assert len(PARTS) == 3
assert len(set(p[2] for p in PARTS)) == 3, "позиции не повторяются"

# ─────────── обложка: три слота ───────────
rows = ""
for sign, rd, pos, intro, ex, py, tr, hint, slots in PARTS:
    left, mid, right = slots
    assert mid == sign
    rows += ("""<div class="sl">
  <div class="scheme">
    <span class="box">%(left)s</span>
    <span class="plus">+</span>
    <span class="box part"><span class="zh">%(sign)s</span><span class="rd">de</span></span>
    <span class="plus">+</span>
    <span class="box">%(right)s</span>
  </div>
  <div class="ex"><span class="zh2">%(ex)s</span><span class="tr">%(tr)s</span></div>
</div>""" % dict(left=left, right=right, sign=sign, ex=ex, tr=tr))
assert rows.count('class="sl"') == 3

hero = """<!DOCTYPE html><html lang="ru"><head><meta charset="utf-8">
%(fonts)s
<style>
%(vars)s
*{margin:0;box-sizing:border-box}html,body{width:1200px;height:630px}
.card{width:1200px;height:630px;background:radial-gradient(1040px 700px at 10%% 4%%, #fff 0%%, var(--cream) 54%%, var(--cream-2) 100%%);position:relative;overflow:hidden;font-family:'Inter',sans-serif;padding:28px 56px 50px 72px;display:flex;flex-direction:column}
.card:before{content:"";position:absolute;left:0;top:0;bottom:0;width:12px;background:var(--brick)}
.head{display:flex;justify-content:space-between;align-items:flex-end;gap:34px;margin-bottom:16px}
.eyebrow{color:var(--brick);font-weight:700;font-size:18px;letter-spacing:.19em;text-transform:uppercase;margin-bottom:8px}
h1{font-family:'Cormorant Garamond',serif;font-weight:600;font-size:38px;line-height:1.07;color:var(--ink);letter-spacing:-.3px;max-width:27ch}
h1 i{font-style:italic;color:var(--brick)}
.tip{flex:0 0 330px;background:var(--surface);border:1px solid var(--hair);border-left:4px solid var(--brick);border-radius:13px;padding:12px 18px;font-size:14.5px;color:var(--ink-2);line-height:1.38}
.tip b{color:var(--ink)}

.rows{flex:1 1 auto;display:flex;flex-direction:column;gap:12px}
.sl{flex:1 1 0;background:var(--surface);border:1px solid var(--hair);border-radius:15px;padding:12px 24px;display:flex;align-items:center;gap:30px}
.scheme{flex:0 0 auto;display:flex;align-items:center;gap:11px}
.box{background:var(--grey-soft);border-radius:10px;padding:13px 16px;font-size:16px;font-weight:600;color:var(--ink-2);min-width:142px;text-align:center}
.box.part{background:var(--brick-soft);border:1.5px solid var(--brick);min-width:86px;padding:8px 14px}
.box.part .zh{display:block;font-family:'Noto Serif SC',serif;font-weight:700;font-size:28px;color:var(--brick-d);line-height:1.1}
.box.part .rd{display:block;font-size:12px;color:var(--brick);font-weight:600;margin-top:1px}
.plus{color:var(--taupe);font-size:17px;font-weight:700}
.ex{flex:1 1 auto;border-left:1px solid var(--hair);padding-left:28px}
.ex .zh2{display:block;font-family:'Noto Serif SC',serif;font-weight:600;font-size:24px;color:var(--ink);line-height:1.2}
.ex .tr{display:block;font-size:14.5px;color:var(--ink-2);margin-top:4px}

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
      <h1>Три частицы de: <i>различает их место, а не слух</i></h1>
    </div>
    <div class="tip">Все три читаются одинаково. <b>Выбор знака решает то, что стоит слева и справа от него.</b></div>
  </div>

  <div class="rows">%(rows)s</div>

  <div class="foot"><b>в разговоре</b><span>различать их не нужно: на слух это один и тот же слог, а смысл держит порядок слов</span></div>

  <div class="brand"><span class="bdot"></span><b>Kitai School</b><span>&middot; kitai-school.ru</span></div>
</div>
</body></html>""" % dict(fonts=FONTS, vars=VARS, rows=rows)

open(S + "de-hero.html", "w", encoding="utf-8").write(hero)

# ─────────── инфографика: позиционная линейка ───────────
MARKS = [
    ("перед существительным", PARTS[0]),
    ("после глагола", PARTS[1]),
    ("перед глаголом", PARTS[2]),
]
assert [m[0] for m in MARKS] == [p[2] for p in PARTS]
assert set(m[0] for m in MARKS) <= set(POSITIONS)

cells = ""
for place, (sign, rd, pos, intro, ex, py, tr, hint, slots) in MARKS:
    cells += ("""<div class="mk">
  <div class="pin"><span class="zh">%(sign)s</span></div>
  <div class="place">%(place)s</div>
  <div class="intro">вводит %(intro)s</div>
  <div class="card2">
    <span class="zh2">%(ex)s</span>
    <span class="py">%(py)s</span>
    <span class="tr">%(tr)s</span>
  </div>
  <div class="hint"><span>спросите себя</span>%(hint)s</div>
</div>""" % dict(sign=sign, place=place, intro=intro, ex=ex, py=py, tr=tr, hint=hint))
assert cells.count('class="mk"') == 3

info = """<!DOCTYPE html><html lang="ru"><head><meta charset="utf-8">
%(fonts)s
<style>
%(vars)s
*{margin:0;box-sizing:border-box}html,body{width:1200px;height:%(h)dpx}
.wrap{width:1200px;height:%(h)dpx;background:linear-gradient(180deg,#fff 0%%,var(--cream) 46%%,var(--cream-2) 100%%);font-family:'Inter',sans-serif;padding:30px 48px 26px;display:flex;flex-direction:column;position:relative;overflow:hidden}
.wrap:before{content:"";position:absolute;left:0;right:0;top:0;height:9px;background:var(--brick)}
.top{display:flex;align-items:flex-end;justify-content:space-between;gap:34px;margin-bottom:20px}
.eyebrow{color:var(--brick);font-weight:700;font-size:15.5px;letter-spacing:.19em;text-transform:uppercase;margin-bottom:7px}
h2{font-family:'Cormorant Garamond',serif;font-weight:600;font-size:34px;line-height:1.08;color:var(--ink);max-width:22ch}
h2 i{font-style:italic;color:var(--brick)}
.hint0{flex:0 0 340px;background:var(--surface);border:1px solid var(--hair);border-left:4px solid var(--brick);border-radius:13px;padding:11px 17px;font-size:14px;color:var(--ink-2);line-height:1.35}
.hint0 b{color:var(--ink)}

.axis{position:relative;flex:1 1 auto;min-height:0;display:flex;gap:18px;padding-top:34px}
.axis:before{content:"";position:absolute;left:0;right:0;top:16px;height:3px;background:var(--hair);border-radius:2px}
.mk{flex:1 1 0;position:relative;display:flex;flex-direction:column;background:var(--surface);border:1px solid var(--hair);border-radius:15px;padding:30px 20px 16px;margin-top:4px}
.pin{position:absolute;top:-26px;left:50%%;transform:translateX(-50%%);width:56px;height:56px;border-radius:50%%;background:var(--brick-soft);border:2px solid var(--brick);display:flex;align-items:center;justify-content:center}
.pin .zh{font-family:'Noto Serif SC',serif;font-weight:700;font-size:28px;color:var(--brick-d);line-height:1}
.place{text-align:center;font-size:16.5px;font-weight:700;color:var(--ink);margin-top:6px}
.intro{text-align:center;font-size:13.5px;color:var(--taupe);margin-top:5px;padding-bottom:12px;border-bottom:1px solid var(--hair)}
.card2{margin-top:12px;text-align:center}
.card2 .zh2{display:block;font-family:'Noto Serif SC',serif;font-weight:600;font-size:27px;color:var(--ink);line-height:1.2}
.card2 .py{display:block;font-size:13.5px;color:var(--taupe);margin-top:4px}
.card2 .tr{display:block;font-size:15px;color:var(--ink-2);margin-top:7px;line-height:1.34}
.hint{margin-top:auto;margin-top:12px;background:var(--cream-2);border-radius:10px;padding:9px 12px;font-size:13.5px;color:var(--ink);line-height:1.34;text-align:center}
.hint span{display:block;font-size:10.5px;letter-spacing:.1em;text-transform:uppercase;color:var(--taupe);margin-bottom:3px}

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
      <div class="eyebrow">Линейка предложения</div>
      <h2>Где стоит частица, <i>та и нужна</i></h2>
    </div>
    <div class="hint0">Знак выбирают по соседям слева и справа. <b>На слух все три одинаковы, поэтому ухо здесь не помощник.</b></div>
  </div>

  <div class="axis">%(cells)s</div>

  <div class="foot">
    <div class="msg">Порядок на линейке не случайный: <b>сначала описание предмета, потом оценка случившегося действия, потом способ будущего</b></div>
    <div class="brand"><span class="dot2"></span><b>Kitai School</b><span>&middot; kitai-school.ru</span></div>
  </div>
</div>
</body></html>""" % dict(fonts=FONTS, vars=VARS, h=540, cells=cells)

open(S + "de-info.html", "w", encoding="utf-8").write(info)

print("ok | частиц:", len(PARTS), "| позиции:", [p[2] for p in PARTS])
