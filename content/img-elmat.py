# -*- coding: utf-8 -*-
# Картинки к статье «HSK Standard Course в электронном виде»
# Обложка     — две колонки: что открывается кодом и что остаётся на бумаге
# Инфографика — пять различий копии из сети, с колонкой последствий
import sys
sys.path.insert(0, "/home/user/Kitai-Shool/content")
from el_mat import PARTS, DIFFS, DIGITAL, PAPER, AUDIO_WAY, BOOKS_IN_KIT

S = ("/tmp/claude-0/-home-user-Kitai-Shool/a463bfca-82a9-56fd-ae09-42a7257ff999/"
     "scratchpad/")

FONTS = ("<link href=\"https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,600;0,700;1,600"
         "&family=Inter:wght@400;500;600;700&display=swap\" rel=\"stylesheet\">")
VARS = (":root{--brick:#A41E3A;--brick-d:#841630;--brick-soft:#F7E6EB;--ink:#2C2420;--ink-2:#5A4F45;"
        "--taupe:#8B7D6B;--cream:#FAF7F2;--cream-2:#F3EDE3;--hair:#EAE3D8;--surface:#fff;"
        "--grey-soft:#EFEDE8;--grey:#9A9289}")

assert len(DIGITAL) == 2 and len(PAPER) == 3

# ─────────── обложка: две колонки ───────────
def cells(items, on):
    """Подпись пишем только там, где есть что сказать: способ получить."""
    out = ""
    for name, digital, how in items:
        tail = "<span>%s</span>" % how.capitalize() if how else ""
        out += ('<div class="it%s"><b>%s</b>%s</div>'
                % ("" if on else " off", name.capitalize(), tail))
    return out


left = cells(DIGITAL, True)
right = cells(PAPER, False)
assert left.count('class="it"') == 2 and right.count('class="it off"') == 3

hero = """<!DOCTYPE html><html lang="ru"><head><meta charset="utf-8">
%(fonts)s
<style>
%(vars)s
*{margin:0;box-sizing:border-box}html,body{width:1200px;height:630px}
.card{width:1200px;height:630px;background:radial-gradient(1040px 700px at 8%% 4%%, #fff 0%%, var(--cream) 54%%, var(--cream-2) 100%%);position:relative;overflow:hidden;font-family:'Inter',sans-serif;padding:28px 56px 50px 72px;display:flex;flex-direction:column}
.card:before{content:"";position:absolute;left:0;top:0;bottom:0;width:12px;background:var(--brick)}
.head{display:flex;justify-content:space-between;align-items:flex-end;gap:34px;margin-bottom:20px}
.eyebrow{color:var(--brick);font-weight:700;font-size:18px;letter-spacing:.19em;text-transform:uppercase;margin-bottom:8px}
h1{font-family:'Cormorant Garamond',serif;font-weight:600;font-size:38px;line-height:1.08;color:var(--ink);letter-spacing:-.3px;max-width:28ch}
h1 i{font-style:italic;color:var(--brick)}
.tip{flex:0 0 318px;background:var(--surface);border:1px solid var(--hair);border-left:4px solid var(--brick);border-radius:13px;padding:12px 18px;font-size:14.5px;color:var(--ink-2);line-height:1.38}
.tip b{color:var(--ink)}

.cols{flex:1 1 auto;min-height:0;display:flex;gap:22px}
.col{flex:1 1 0;background:var(--surface);border:1px solid var(--hair);border-radius:15px;padding:16px 20px 18px;display:flex;flex-direction:column}
.col.yes{border-color:var(--brick)}
.ch{display:flex;align-items:center;gap:11px;margin-bottom:14px}
.ch i{font-style:normal;width:30px;height:30px;border-radius:50%%;display:flex;align-items:center;justify-content:center;font-weight:700;font-size:17px;flex:0 0 auto;background:var(--grey-soft);color:var(--taupe)}
.col.yes .ch i{background:var(--brick);color:#fff}
.ch b{font-size:17.5px;color:var(--ink)}
.col.no .ch b{color:var(--taupe)}
.items{display:flex;flex-direction:column;gap:9px}
.it{border-radius:11px;padding:10px 14px;background:var(--brick-soft);border:1px solid var(--brick)}
.it.off{background:transparent;border:1px dashed var(--hair)}
.it b{display:block;font-size:15.5px;color:var(--ink);margin-bottom:2px}
.it.off b{color:var(--taupe)}
.it span{font-size:13px;color:var(--ink-2);line-height:1.3}
.sum{margin-top:auto;padding-top:14px;font-size:13.5px;color:var(--ink-2);line-height:1.36}

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
      <div class="eyebrow">Электронные материалы</div>
      <h1>В цифре официально есть <i>только звук</i></h1>
    </div>
    <div class="tip">Код на обложке открывает запись к урокам. <b>Самих книг в легальном доступе я не нашла ни одной.</b></div>
  </div>

  <div class="cols">
    <div class="col yes">
      <div class="ch"><i>&#10003;</i><b>Открывается кодом</b></div>
      <div class="items">%(left)s</div>
      <div class="sum">Код печатают на задней обложке каждого тома — он открывает запись к урокам именно вашего издания</div>
    </div>
    <div class="col no">
      <div class="ch"><i>&mdash;</i><b>Остаётся на бумаге</b></div>
      <div class="items">%(right)s</div>
      <div class="sum">Официальной цифровой версии я не нашла ни для одной из трёх книг комплекта</div>
    </div>
  </div>

  <div class="foot"><b>что это значит</b><span>звук можно получить к своему экземпляру, а книги придётся купить: все %(books)s книги комплекта выходят только на бумаге</span></div>

  <div class="brand"><span class="bdot"></span><b>Kitai School</b><span>&middot; kitai-school.ru</span></div>
</div>
</body></html>""" % dict(fonts=FONTS, vars=VARS, left=left, right=right, books={3: "три"}[BOOKS_IN_KIT])

assert "%%" not in hero, "в разметке остались двойные проценты"
open(S + "elmat-hero.html", "w", encoding="utf-8").write(hero)

# ─────────── инфографика: пять различий ───────────
rows = ""
for i, (key, what, result) in enumerate(DIFFS, start=1):
    rows += ("""<div class="rw">
  <div class="n">%(n)d</div>
  <div class="key">%(key)s</div>
  <div class="what">%(what)s</div>
  <div class="arr">&rarr;</div>
  <div class="res">%(res)s</div>
</div>""" % dict(n=i, key=key.capitalize(), what=what, res=result))
assert rows.count('class="rw"') == len(DIFFS) == 5

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
.hint0{flex:0 0 352px;background:var(--surface);border:1px solid var(--hair);border-left:4px solid var(--brick);border-radius:13px;padding:11px 17px;font-size:14px;color:var(--ink-2);line-height:1.35}
.hint0 b{color:var(--ink)}

.cap{display:flex;gap:14px;padding:0 18px 8px;font-size:12px;font-weight:700;letter-spacing:.1em;text-transform:uppercase;color:var(--taupe)}
.cap .c1{flex:0 0 36px}
.cap .c2{flex:0 0 148px}
.cap .c3{flex:1 1 0}
.cap .c4{flex:0 0 26px}
.cap .c5{flex:1 1 0}

.rows{flex:1 1 auto;min-height:0;display:flex;flex-direction:column;gap:9px}
.rw{flex:1 1 0;background:var(--surface);border:1px solid var(--hair);border-radius:13px;padding:10px 18px;display:flex;align-items:center;gap:14px}
.rw .n{flex:0 0 36px;font-family:'Cormorant Garamond',serif;font-weight:700;font-size:28px;color:var(--brick);line-height:1}
.rw .key{flex:0 0 148px;font-size:16px;font-weight:600;color:var(--ink)}
.rw .what{flex:1 1 0;font-size:14px;color:var(--ink-2);line-height:1.32}
.rw .arr{flex:0 0 26px;text-align:center;color:var(--brick);font-size:19px}
.rw .res{flex:1 1 0;font-size:14px;color:var(--ink);line-height:1.32;background:var(--brick-soft);border-radius:9px;padding:8px 13px}

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
      <div class="eyebrow">Копия и комплект</div>
      <h2>Пять различий, <i>которые видно на занятии</i></h2>
    </div>
    <div class="hint0">Слева — что происходит с копией, справа — чем это оборачивается в работе. <b>Разница здесь не в принципах, а в том, чему вы научитесь.</b></div>
  </div>

  <div class="cap">
    <div class="c1"></div>
    <div class="c2">признак</div>
    <div class="c3">что с ним у копии</div>
    <div class="c4"></div>
    <div class="c5">чем оборачивается</div>
  </div>

  <div class="rows">%(rows)s</div>

  <div class="foot">
    <div class="msg">Звук к своему экземпляру берут <b>по коду на задней обложке</b> — у скачанного файла такого кода нет</div>
    <div class="brand"><span class="dot2"></span><b>Kitai School</b><span>&middot; kitai-school.ru</span></div>
  </div>
</div>
</body></html>""" % dict(fonts=FONTS, vars=VARS, h=680, rows=rows)

assert "%%" not in info, "в разметке остались двойные проценты"
open(S + "elmat-info.html", "w", encoding="utf-8").write(info)

print("ok | в цифре:", [p[0] for p in DIGITAL], "| на бумаге:", len(PAPER),
      "| различий:", len(DIFFS))
