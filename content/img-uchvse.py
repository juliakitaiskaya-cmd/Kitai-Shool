# -*- coding: utf-8 -*-
# Картинки к статье «HSK Standard Course: учебники по уровням»
# Обложка     — три ступени счёта: шесть уровней, девять томов, двадцать семь книг
# Инфографика — разбор комплекта: что лежит в учебнике, тетради и книге преподавателя
import sys
sys.path.insert(0, "/home/user/Kitai-Shool/content")
from uch_vse import (VOLUMES, KIT, INSIDE, HOW, LEVELS, VOLS_PER_LEVEL, ONE_VOLUME, TWO_VOLUMES,
                     TOTAL_VOLUMES, BOOKS_PER_VOLUME, TOTAL_BOOKS, KNOWN, UNKNOWN,
                     SERIES_NAME, SERIES_CN)

S = ("/tmp/claude-0/-home-user-Kitai-Shool/a463bfca-82a9-56fd-ae09-42a7257ff999/"
     "scratchpad/")

FONTS = ("<link href=\"https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,600;0,700;1,600"
         "&family=Inter:wght@400;500;600;700&family=Noto+Serif+SC:wght@600;700&display=swap\" rel=\"stylesheet\">")
VARS = (":root{--brick:#A41E3A;--brick-d:#841630;--brick-soft:#F7E6EB;--ink:#2C2420;--ink-2:#5A4F45;"
        "--taupe:#8B7D6B;--cream:#FAF7F2;--cream-2:#F3EDE3;--hair:#EAE3D8;--surface:#fff;"
        "--grey-soft:#EFEDE8;--grey:#9A9289}")

assert TOTAL_VOLUMES == 9 and TOTAL_BOOKS == 27

# ─────────── обложка: три ступени счёта ───────────
# ступень 1 — уровни, ступень 2 — тома, ступень 3 — книги
lvl_cells = "".join(
    '<i class="lc%s">%d</i>' % (" two" if VOLS_PER_LEVEL[l] == 2 else "", l) for l in LEVELS)
vol_cells = "".join(
    '<i class="vc%s">%s</i>' % (" two" if lvl in TWO_VOLUMES else "", tag)
    for lvl, tag, les, w in VOLUMES)
book_cells = "".join('<i class="bc"></i>' for _ in range(TOTAL_BOOKS))
assert lvl_cells.count("<i") == len(LEVELS) == 6
assert vol_cells.count("<i") == TOTAL_VOLUMES
assert book_cells.count("<i") == TOTAL_BOOKS
assert vol_cells.count('class="vc two"') == 6, "шесть томов приходятся на старшие уровни"

hero = """<!DOCTYPE html><html lang="ru"><head><meta charset="utf-8">
%(fonts)s
<style>
%(vars)s
*{margin:0;box-sizing:border-box}html,body{width:1200px;height:630px}
.card{width:1200px;height:630px;background:radial-gradient(1040px 700px at 8%% 4%%, #fff 0%%, var(--cream) 54%%, var(--cream-2) 100%%);position:relative;overflow:hidden;font-family:'Inter',sans-serif;padding:28px 56px 50px 72px;display:flex;flex-direction:column}
.card:before{content:"";position:absolute;left:0;top:0;bottom:0;width:12px;background:var(--brick)}
.head{display:flex;justify-content:space-between;align-items:flex-end;gap:34px;margin-bottom:18px}
.eyebrow{color:var(--brick);font-weight:700;font-size:18px;letter-spacing:.19em;text-transform:uppercase;margin-bottom:8px}
h1{font-family:'Cormorant Garamond',serif;font-weight:600;font-size:38px;line-height:1.08;color:var(--ink);letter-spacing:-.3px;max-width:30ch}
h1 i{font-style:italic;color:var(--brick)}
.tip{flex:0 0 318px;background:var(--surface);border:1px solid var(--hair);border-left:4px solid var(--brick);border-radius:13px;padding:12px 18px;font-size:14.5px;color:var(--ink-2);line-height:1.38}
.tip b{color:var(--ink)}

.rows{flex:1 1 auto;min-height:0;display:flex;flex-direction:column;gap:12px}
.rw{flex:1 1 0;background:var(--surface);border:1px solid var(--hair);border-radius:14px;padding:12px 20px;display:flex;align-items:center;gap:22px}
.rw.last{border-color:var(--brick);background:var(--brick-soft)}
.big{flex:0 0 140px;display:flex;align-items:baseline;gap:9px}
.big b{font-family:'Cormorant Garamond',serif;font-weight:700;font-size:52px;color:var(--brick);line-height:1}
.big span{font-size:14.5px;color:var(--ink-2)}
.cells{flex:1 1 auto;display:flex;align-items:center;justify-content:center;gap:7px;flex-wrap:wrap}
.cells i{font-style:normal;display:flex;align-items:center;justify-content:center;font-weight:700}
.lc{width:52px;height:52px;border-radius:10px;background:var(--grey-soft);border:1px solid var(--hair);color:var(--ink-2);font-size:17px}
.lc.two{background:var(--brick-soft);border-color:var(--brick);color:var(--brick-d)}
.lc{font-size:19px}
.vc{width:56px;height:44px;border-radius:7px;background:var(--grey-soft);border:1px solid var(--hair);color:var(--ink-2);font-size:14px}
.vc.two{background:var(--brick-soft);border-color:var(--brick);color:var(--brick-d)}
.bc{width:14px;height:30px;border-radius:3px;background:var(--grey-soft);border:1px solid var(--hair)}
.rw.last .bc{background:#fff;border-color:var(--brick)}
.cells.books{gap:5px;flex-wrap:nowrap}
.note{flex:0 0 268px;font-size:13.5px;color:var(--ink-2);line-height:1.34}
.note b{color:var(--ink)}

.brand{position:absolute;left:72px;bottom:16px;display:flex;align-items:center;gap:11px;color:var(--ink)}
.brand b{font-family:'Cormorant Garamond',serif;font-weight:700;font-size:24px}
.brand .bdot{width:10px;height:10px;border-radius:50%%;background:var(--brick)}
.brand span{color:var(--taupe);font-size:15px}
</style></head><body>
<div class="card">
  <div class="head">
    <div>
      <div class="eyebrow">Учебники</div>
      <h1>Уровней шесть, <i>а томов девять</i></h1>
    </div>
    <div class="tip">С четвёртого уровня том делится надвое. <b>«Учебник HSK 5» — это половина уровня, а не весь уровень.</b></div>
  </div>

  <div class="rows">
    <div class="rw">
      <div class="big"><b>%(nlvl)d</b><span>уровней</span></div>
      <div class="cells">%(lvl)s</div>
      <div class="note">Серия закрывает уровни с первого по шестой. <b>Красным — те, где томов два.</b></div>
    </div>

    <div class="rw">
      <div class="big"><b>%(nvol)d</b><span>томов</span></div>
      <div class="cells">%(vol)s</div>
      <div class="note">На младших уровнях один том, с четвёртого — <b>два, с буквами A и B</b></div>
    </div>

    <div class="rw last">
      <div class="big"><b>%(nbook)d</b><span>книг</span></div>
      <div class="cells books">%(book)s</div>
      <div class="note">В каждом томе <b>три книги</b>: учебник, тетрадь и книга для преподавателя</div>
    </div>
  </div>

  <div class="brand"><span class="bdot"></span><b>Kitai School</b><span>&middot; kitai-school.ru</span></div>
</div>
</body></html>""" % dict(fonts=FONTS, vars=VARS, nlvl=len(LEVELS), nvol=TOTAL_VOLUMES,
                         nbook=TOTAL_BOOKS, lvl=lvl_cells, vol=vol_cells, book=book_cells)

assert "%%" not in hero, "в разметке остались двойные проценты"
open(S + "uchvse-hero.html", "w", encoding="utf-8").write(hero)

# ─────────── инфографика: что лежит в каждой книге комплекта ───────────
NEED = [b for b in INSIDE if b[2]]
EXTRA = [b for b in INSIDE if not b[2]]
assert len(NEED) == 2 and len(EXTRA) == 1

HOW_D = dict((n, (verb, note)) for n, verb, note in HOW)

pages = ""
for name, parts, need in NEED:
    verb, note = HOW_D[name]
    items = "".join('<li>%s</li>' % p for p in parts)
    pages += ("""<div class="pg">
  <div class="ph"><b>%(name)s</b><i>%(verb)s</i></div>
  <ul class="pl">%(items)s</ul>
  <div class="pn">%(note)s</div>
</div>""" % dict(name=name.capitalize(), verb=verb, items=items, note=note[0].upper() + note[1:]))
assert pages.count('class="pg"') == 2
assert pages.count("<li>") == sum(len(p) for n, p, need in NEED)

ename, eparts, _ = EXTRA[0]
extra = ('<div class="ex"><div class="eh"><b>%s</b><i>не для ученика</i></div>'
         '<div class="el">%s</div></div>'
         % (ename.capitalize(), " · ".join(eparts)))

info = """<!DOCTYPE html><html lang="ru"><head><meta charset="utf-8">
%(fonts)s
<style>
%(vars)s
*{margin:0;box-sizing:border-box}html,body{width:1200px;height:%(h)dpx}
.wrap{width:1200px;height:%(h)dpx;background:linear-gradient(180deg,#fff 0%%,var(--cream) 46%%,var(--cream-2) 100%%);font-family:'Inter',sans-serif;padding:30px 48px 26px;display:flex;flex-direction:column;position:relative;overflow:hidden}
.wrap:before{content:"";position:absolute;left:0;right:0;top:0;height:9px;background:var(--brick)}
.top{display:flex;align-items:flex-end;justify-content:space-between;gap:34px;margin-bottom:20px}
.eyebrow{color:var(--brick);font-weight:700;font-size:15.5px;letter-spacing:.19em;text-transform:uppercase;margin-bottom:7px}
h2{font-family:'Cormorant Garamond',serif;font-weight:600;font-size:34px;line-height:1.08;color:var(--ink);max-width:24ch}
h2 i{font-style:italic;color:var(--brick)}
.hint0{flex:0 0 348px;background:var(--surface);border:1px solid var(--hair);border-left:4px solid var(--brick);border-radius:13px;padding:11px 17px;font-size:14px;color:var(--ink-2);line-height:1.35}
.hint0 b{color:var(--ink)}

.spread{flex:1 1 auto;min-height:0;display:flex;align-items:stretch;position:relative;background:var(--surface);border:1px solid var(--brick);border-radius:16px;overflow:hidden}
.spread:before{content:"";position:absolute;left:50%%;top:16px;bottom:16px;width:2px;background:var(--hair);transform:translateX(-50%%)}
.pg{flex:1 1 0;padding:20px 26px;display:flex;flex-direction:column}
.ph{display:flex;align-items:baseline;gap:12px;margin-bottom:14px}
.ph b{font-size:21px;color:var(--ink)}
.ph i{font-style:normal;font-size:12.5px;font-weight:700;letter-spacing:.11em;text-transform:uppercase;color:#fff;background:var(--brick);border-radius:7px;padding:4px 11px}
.pl{list-style:none;padding:0;margin:0}
.pl li{position:relative;padding:9px 0 9px 24px;font-size:16px;color:var(--ink-2);border-bottom:1px dashed var(--hair)}
.pl li:last-child{border-bottom:none}
.pl li:before{content:"";position:absolute;left:4px;top:17px;width:8px;height:8px;border-radius:50%%;background:var(--brick-soft);border:1px solid var(--brick)}
.pn{margin-top:auto;padding-top:14px;font-size:14px;color:var(--brick-d);font-weight:600}

.ex{margin-top:14px;flex:0 0 auto;background:transparent;border:1px dashed var(--grey);border-radius:13px;padding:12px 22px;display:flex;align-items:center;gap:18px}
.eh{display:flex;align-items:baseline;gap:11px;flex:0 0 auto}
.eh b{font-size:16.5px;color:var(--taupe)}
.eh i{font-style:normal;font-size:11.5px;font-weight:700;letter-spacing:.09em;text-transform:uppercase;color:var(--grey)}
.el{font-size:14px;color:var(--ink-2)}

.foot{margin-top:14px;flex:0 0 auto;display:flex;align-items:center;gap:18px}
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
      <div class="eyebrow">Комплект тома</div>
      <h2>Учебник читают, <i>тетрадь делают</i></h2>
    </div>
    <div class="hint0">Это разные книги с разными задачами. <b>Нового материала в тетради нет — она целиком про то, чтобы выученное закрепилось.</b></div>
  </div>

  <div class="spread">%(pages)s</div>

  %(extra)s

  <div class="foot">
    <div class="msg">Если выбирать приходится из-за денег, берите <b>том целиком уровнем ниже</b>, а не учебник без тетради на своём</div>
    <div class="brand"><span class="dot2"></span><b>Kitai School</b><span>&middot; kitai-school.ru</span></div>
  </div>
</div>
</body></html>""" % dict(fonts=FONTS, vars=VARS, h=600, pages=pages, extra=extra)

assert "%%" not in info, "в разметке остались двойные проценты"
open(S + "uchvse-info.html", "w", encoding="utf-8").write(info)

print("ok | нужных книг:", len(NEED), "| пунктов:", sum(len(p) for n, p, need in INSIDE),
      "| лишняя:", EXTRA[0][0])
