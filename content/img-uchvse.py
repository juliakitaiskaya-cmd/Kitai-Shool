# -*- coding: utf-8 -*-
# Картинки к статье «HSK Standard Course: учебники по уровням»
# Обложка     — три ступени счёта: шесть уровней, девять томов, двадцать семь книг
# Инфографика — девять томов в ряд: у четырёх словарь подтверждён, у пяти поле пустое
import sys
sys.path.insert(0, "/home/user/Kitai-Shool/content")
from uch_vse import (VOLUMES, KIT, LEVELS, VOLS_PER_LEVEL, ONE_VOLUME, TWO_VOLUMES,
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

# ─────────── инфографика: девять томов, словарь известен по четырём ───────────
TOP_W = max(v[3] for v in KNOWN)
MAXH, MINH = 176, 42
cols = ""
for lvl, tag, les, w in VOLUMES:
    if w:
        h = round(MINH + (MAXH - MINH) * w / TOP_W)
        inner = ('<div class="bar on" style="height:%dpx"><span>%d</span></div>'
                 '<div class="les">%d уроков</div>' % (h, w, les))
    else:
        inner = ('<div class="bar off"><span>нет<br>данных</span></div>'
                 '<div class="les">%s</div>' % ("%d уроков" % les if les else "—"))
    cols += '<div class="cl%s"><div class="tag">%s</div>%s</div>' % (
        "" if w else " dim", tag, inner)
assert cols.count('class="bar on"') == len(KNOWN) == 4
assert cols.count('class="bar off"') == len(UNKNOWN) == 5

kit_items = "".join(
    '<div class="ki%s"><b>%s</b><span>%s</span></div>'
    % ("" if need else " no", name, what) for name, what, need in KIT)
assert kit_items.count('class="ki no"') == 1, "одна книга из трёх ученику не нужна"

info = """<!DOCTYPE html><html lang="ru"><head><meta charset="utf-8">
%(fonts)s
<style>
%(vars)s
*{margin:0;box-sizing:border-box}html,body{width:1200px;height:%(h)dpx}
.wrap{width:1200px;height:%(h)dpx;background:linear-gradient(180deg,#fff 0%%,var(--cream) 46%%,var(--cream-2) 100%%);font-family:'Inter',sans-serif;padding:30px 48px 26px;display:flex;flex-direction:column;position:relative;overflow:hidden}
.wrap:before{content:"";position:absolute;left:0;right:0;top:0;height:9px;background:var(--brick)}
.top{display:flex;align-items:flex-end;justify-content:space-between;gap:34px;margin-bottom:20px}
.eyebrow{color:var(--brick);font-weight:700;font-size:15.5px;letter-spacing:.19em;text-transform:uppercase;margin-bottom:7px}
h2{font-family:'Cormorant Garamond',serif;font-weight:600;font-size:34px;line-height:1.08;color:var(--ink);max-width:25ch}
h2 i{font-style:italic;color:var(--brick)}
.hint0{flex:0 0 346px;background:var(--surface);border:1px solid var(--hair);border-left:4px solid var(--brick);border-radius:13px;padding:11px 17px;font-size:14px;color:var(--ink-2);line-height:1.35}
.hint0 b{color:var(--ink)}

.grid{flex:1 1 auto;min-height:0;display:flex;align-items:flex-end;gap:10px}
.cl{flex:1 1 0;display:flex;flex-direction:column;align-items:center}
.tag{font-size:16px;font-weight:700;color:var(--ink);margin-bottom:8px}
.cl.dim .tag{color:var(--taupe)}
.bar{width:100%%;border-radius:10px;display:flex;align-items:flex-start;justify-content:center;padding-top:10px}
.bar.on{background:var(--brick-soft);border:1px solid var(--brick)}
.bar.on span{font-family:'Cormorant Garamond',serif;font-weight:700;font-size:27px;color:var(--brick-d);line-height:1}
.bar.off{height:70px;background:transparent;border:2px dashed var(--hair);align-items:center;padding-top:0}
.bar.off span{font-size:12.5px;color:var(--taupe);text-align:center;line-height:1.25}
.les{margin-top:8px;font-size:12.5px;color:var(--ink-2)}
.cl.dim .les{color:var(--taupe)}

.kit{margin-top:16px;flex:0 0 auto;display:flex;gap:10px}
.ki{flex:1 1 0;background:var(--surface);border:1px solid var(--brick);border-radius:12px;padding:10px 16px}
.ki.no{border-color:var(--hair);border-style:dashed;background:transparent}
.ki b{display:block;font-size:15px;color:var(--ink);margin-bottom:3px}
.ki.no b{color:var(--taupe)}
.ki span{font-size:13px;color:var(--ink-2);line-height:1.3}

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
      <div class="eyebrow">Девять томов</div>
      <h2>Словарь известен <i>по четырём томам из девяти</i></h2>
    </div>
    <div class="hint0">Цифра — сколько слов в томе. <b>Пунктиром отмечены тома, по которым подтверждённых данных нет: ни по одному второму тому цифры не нашлось.</b></div>
  </div>

  <div class="grid">%(cols)s</div>

  <div class="kit">%(kit)s</div>

  <div class="foot">
    <div class="msg">На старших уровнях <b>номер на обложке называет уровень, а не объём</b>: проверяйте букву рядом с цифрой</div>
    <div class="brand"><span class="dot2"></span><b>Kitai School</b><span>&middot; kitai-school.ru</span></div>
  </div>
</div>
</body></html>""" % dict(fonts=FONTS, vars=VARS, h=570, cols=cols, kit=kit_items)

assert "%%" not in info, "в разметке остались двойные проценты"
open(S + "uchvse-info.html", "w", encoding="utf-8").write(info)

print("ok | томов:", TOTAL_VOLUMES, "| книг:", TOTAL_BOOKS,
      "| с цифрой:", [v[1] for v in KNOWN], "| без:", [v[1] for v in UNKNOWN])
