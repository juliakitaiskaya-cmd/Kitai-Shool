# -*- coding: utf-8 -*-
# Картинки к статье «Тест HSK: какой экзамен вы сдаёте»
# Обложка     — полоса времени с отметкой перехода и три ступени уровней
# Инфографика — пять различий «было — стало» с меткой источника у каждого
import sys
sys.path.insert(0, "/home/user/Kitai-Shool/content")
from test_hsk import (CHANGES, BANDS, STEPS, OFFICIAL, REPORTED, START_DATE, LAST_OLD,
                      SYLLABUS_OUT, LEVELS_OLD, LEVELS_NEW, CONFIRMED, UNCONFIRMED,
                      SPEAKING_FROM)

S = ("/tmp/claude-0/-home-user-Kitai-Shool/a463bfca-82a9-56fd-ae09-42a7257ff999/"
     "scratchpad/")

FONTS = ("<link href=\"https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,600;0,700;1,600"
         "&family=Inter:wght@400;500;600;700&display=swap\" rel=\"stylesheet\">")
VARS = (":root{--brick:#A41E3A;--brick-d:#841630;--brick-soft:#F7E6EB;--ink:#2C2420;--ink-2:#5A4F45;"
        "--taupe:#8B7D6B;--cream:#FAF7F2;--cream-2:#F3EDE3;--hair:#EAE3D8;--surface:#fff;"
        "--grey-soft:#EFEDE8;--grey:#9A9289}")

assert LEVELS_NEW == 9 and len(BANDS) == 3

# ─────────── обложка: полоса времени ───────────
bands = ""
for name, levels in BANDS:
    cells = "".join('<i>%d</i>' % l for l in levels)
    bands += ('<div class="bd"><div class="bn">%s ступень</div><div class="bl">%s</div></div>'
              % (name.capitalize(), cells))
assert bands.count('class="bd"') == 3
assert bands.count("<i>") == LEVELS_NEW

hero = """<!DOCTYPE html><html lang="ru"><head><meta charset="utf-8">
%(fonts)s
<style>
%(vars)s
*{margin:0;box-sizing:border-box}html,body{width:1200px;height:630px}
.card{width:1200px;height:630px;background:radial-gradient(1040px 700px at 8%% 4%%, #fff 0%%, var(--cream) 54%%, var(--cream-2) 100%%);position:relative;overflow:hidden;font-family:'Inter',sans-serif;padding:28px 56px 50px 72px;display:flex;flex-direction:column}
.card:before{content:"";position:absolute;left:0;top:0;bottom:0;width:12px;background:var(--brick)}
.head{display:flex;justify-content:space-between;align-items:flex-end;gap:34px;margin-bottom:22px}
.eyebrow{color:var(--brick);font-weight:700;font-size:18px;letter-spacing:.19em;text-transform:uppercase;margin-bottom:8px}
h1{font-family:'Cormorant Garamond',serif;font-weight:600;font-size:38px;line-height:1.08;color:var(--ink);letter-spacing:-.3px;max-width:27ch}
h1 i{font-style:italic;color:var(--brick)}
.tip{flex:0 0 322px;background:var(--surface);border:1px solid var(--hair);border-left:4px solid var(--brick);border-radius:13px;padding:12px 18px;font-size:14.5px;color:var(--ink-2);line-height:1.38}
.tip b{color:var(--ink)}

.line{position:relative;margin:0 6px 26px;padding-top:4px}
.track{height:12px;border-radius:6px;background:linear-gradient(90deg,var(--grey-soft) 0%%,var(--grey-soft) 50%%,var(--brick-soft) 50%%,var(--brick-soft) 100%%);border:1px solid var(--hair)}
.mark{position:absolute;left:50%%;top:-6px;bottom:-30px;width:3px;background:var(--brick);transform:translateX(-50%%)}
.mark span{position:absolute;left:50%%;bottom:-24px;transform:translateX(-50%%);white-space:nowrap;background:var(--brick);color:#fff;font-size:13.5px;font-weight:700;border-radius:7px;padding:5px 13px}
.ends{display:flex;justify-content:space-between;margin-top:14px}
.end{flex:0 0 46%%}
.end.r{text-align:right}
.end b{display:block;font-size:19px;color:var(--ink);margin-bottom:3px}
.end.l b{color:var(--taupe)}
.end.r b{color:var(--brick-d)}
.end span{font-size:14px;color:var(--ink-2);line-height:1.35}

.bands{display:flex;gap:16px;margin-top:auto}
.bd{flex:1 1 0;background:var(--surface);border:1px solid var(--hair);border-radius:14px;padding:15px 20px}
.bn{font-size:14.5px;color:var(--ink-2);margin-bottom:10px}
.bl{display:flex;gap:8px}
.bl i{font-style:normal;flex:1 1 0;height:56px;border-radius:9px;background:var(--brick-soft);border:1px solid var(--brick);color:var(--brick-d);font-weight:700;font-size:19px;display:flex;align-items:center;justify-content:center}

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
      <div class="eyebrow">Тест HSK</div>
      <h1>С декабря экзамен <i>другой</i></h1>
    </div>
    <div class="tip">Уровней стало девять вместо шести. <b>Пробники прежнего формата показывают тест, которого больше не будет.</b></div>
  </div>

  <div class="line">
    <div class="track"></div>
    <div class="mark"><span>%(start)s</span></div>
    <div class="ends">
      <div class="end l"><b>прежний формат</b><span>последняя обычная сессия уровней с первого по шестой — %(last)s</span></div>
      <div class="end r"><b>новый формат</b><span>описание опубликовано в %(syl)s, экзамен по нему — с %(start)s</span></div>
    </div>
  </div>

  <div class="bands">%(bands)s</div>

  <div class="foot"><b>что ещё меняется</b><span>устная часть с третьего уровня входит в сам экзамен, а на первых двух появляются требования к письму от руки</span></div>

  <div class="brand"><span class="bdot"></span><b>Kitai School</b><span>&middot; kitai-school.ru</span></div>
</div>
</body></html>""" % dict(fonts=FONTS, vars=VARS, bands=bands, start=START_DATE,
                         last=LAST_OLD, syl=SYLLABUS_OUT)

assert "%%" not in hero, "в разметке остались двойные проценты"
open(S + "testhsk-hero.html", "w", encoding="utf-8").write(hero)

# ─────────── инфографика: пять различий с метками источника ───────────
rows = ""
for key, was, now, status in CHANGES:
    ok = status == OFFICIAL
    rows += ("""<div class="rw%(cls)s">
  <div class="key">%(key)s</div>
  <div class="was">%(was)s</div>
  <div class="arr">&rarr;</div>
  <div class="now">%(now)s</div>
  <div class="st">%(st)s</div>
</div>""" % dict(cls="" if ok else " soft", key=key, was=was, now=now,
                 st="подтверждено" if ok else "по описаниям"))
assert rows.count('class="rw"') == len(CONFIRMED) == 4
assert rows.count('class="rw soft"') == len(UNCONFIRMED) == 1

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
.cap .c1{flex:0 0 184px}
.cap .c2{flex:1 1 0}
.cap .c3{flex:0 0 26px}
.cap .c4{flex:1 1 0}
.cap .c5{flex:0 0 120px;text-align:right}

.rows{flex:1 1 auto;min-height:0;display:flex;flex-direction:column;gap:9px}
.rw{flex:1 1 0;background:var(--surface);border:1px solid var(--hair);border-radius:13px;padding:10px 18px;display:flex;align-items:center;gap:14px}
.rw.soft{border-style:dashed;border-color:var(--grey)}
.rw .key{flex:0 0 184px;font-size:15.5px;font-weight:600;color:var(--ink)}
.rw.soft .key{color:var(--taupe)}
.rw .was{flex:1 1 0;font-size:14px;color:var(--taupe);line-height:1.3}
.rw .arr{flex:0 0 26px;text-align:center;color:var(--brick);font-size:19px}
.rw .now{flex:1 1 0;font-size:14px;color:var(--ink);line-height:1.3;background:var(--brick-soft);border-radius:9px;padding:8px 13px}
.rw.soft .now{background:var(--grey-soft);color:var(--ink-2)}
.rw .st{flex:0 0 120px;text-align:right;font-size:12px;font-weight:700;letter-spacing:.06em;text-transform:uppercase;color:var(--brick)}
.rw.soft .st{color:var(--grey)}

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
      <div class="eyebrow">Было и стало</div>
      <h2>Пять различий, <i>одно без подтверждения</i></h2>
    </div>
    <div class="hint0">Справа у каждой строки стоит, откуда взято. <b>Пунктиром отмечено то, что собрано по сторонним описаниям: официального подтверждения я не нашла.</b></div>
  </div>

  <div class="cap">
    <div class="c1">что</div>
    <div class="c2">было</div>
    <div class="c3"></div>
    <div class="c4">стало</div>
    <div class="c5">источник</div>
  </div>

  <div class="rows">%(rows)s</div>

  <div class="foot">
    <div class="msg">Устная часть с третьего уровня <b>входит в экзамен</b>, а не сдаётся отдельно — это меняет план подготовки целиком</div>
    <div class="brand"><span class="dot2"></span><b>Kitai School</b><span>&middot; kitai-school.ru</span></div>
  </div>
</div>
</body></html>""" % dict(fonts=FONTS, vars=VARS, h=712, rows=rows)

assert "%%" not in info, "в разметке остались двойные проценты"
open(S + "testhsk-info.html", "w", encoding="utf-8").write(info)

print("ok | уровней:", LEVELS_NEW, "| подтверждено:", len(CONFIRMED),
      "| по описаниям:", len(UNCONFIRMED), "| устная с:", SPEAKING_FROM)
