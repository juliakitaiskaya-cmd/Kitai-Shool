# -*- coding: utf-8 -*-
# Картинки к статье «Указательные местоимения в китайском»
# Обложка     — шкала дальности: где проходит граница между 这 и 那
# Инфографика — конструктор фразы 这两本书 и тот же набор без счётного слова
import sys
sys.path.insert(0, "/home/user/Kitai-Shool/content")
from ukaz import PAIRS, PHRASE, BROKEN, SCALE

S = ("/tmp/claude-0/-home-user-Kitai-Shool/a463bfca-82a9-56fd-ae09-42a7257ff999/"
     "scratchpad/")

FONTS = ("<link href=\"https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,600;0,700;1,600"
         "&family=Inter:wght@400;500;600;700&family=Noto+Serif+SC:wght@600;700&display=swap\" rel=\"stylesheet\">")
VARS = (":root{--brick:#A41E3A;--brick-d:#841630;--brick-soft:#F7E6EB;--ink:#2C2420;--ink-2:#5A4F45;"
        "--taupe:#8B7D6B;--cream:#FAF7F2;--cream-2:#F3EDE3;--hair:#EAE3D8;--surface:#fff;"
        "--paper:#FFFDF8;--good:#2F6F4F;--good-soft:#E8F3EC;--grey:#8A8178;--grey-soft:#EFEDE8}")

assert len(SCALE) == 4, "на шкале четыре отметки"
assert len(PHRASE) == 4 and len(BROKEN) == 3, "четыре блока против трёх"

# ─────────── обложка: шкала дальности ───────────
marks = ""
for i, (where, han, py) in enumerate(SCALE):
    near = han.startswith("这")
    marks += ('<div class="mk%s"><div class="dot"></div>'
              '<div class="wh">%s</div>'
              '<div class="sayz"><span class="zh">%s</span><span class="py">%s</span></div>'
              '</div>' % (" far" if not near else "", where, han, py))
assert marks.count('class="mk') == 4, "четыре отметки на шкале"
NEAR_N = sum(1 for s_ in SCALE if s_[1].startswith("这"))
FAR_N = len(SCALE) - NEAR_N
assert NEAR_N == FAR_N == 2, "две ближние отметки и две дальние"

hero = """<!DOCTYPE html><html lang="ru"><head><meta charset="utf-8">
%(fonts)s
<style>
%(vars)s
*{margin:0;box-sizing:border-box}html,body{width:1200px;height:630px}
.card{width:1200px;height:630px;background:radial-gradient(1040px 700px at 12%% 4%%, #fff 0%%, var(--cream) 54%%, var(--cream-2) 100%%);position:relative;overflow:hidden;font-family:'Inter',sans-serif;padding:30px 56px 52px 72px;display:flex;flex-direction:column}
.card:before{content:"";position:absolute;left:0;top:0;bottom:0;width:12px;background:var(--brick)}
.head{display:flex;justify-content:space-between;align-items:flex-end;gap:34px;margin-bottom:10px}
.eyebrow{color:var(--brick);font-weight:700;font-size:18px;letter-spacing:.19em;text-transform:uppercase;margin-bottom:9px}
h1{font-family:'Cormorant Garamond',serif;font-weight:600;font-size:37px;line-height:1.07;color:var(--ink);letter-spacing:-.3px;max-width:22ch}
h1 i{font-style:italic;color:var(--brick)}
.tip{flex:0 0 330px;background:var(--surface);border:1px solid var(--hair);border-left:4px solid var(--brick);border-radius:13px;padding:13px 18px;font-size:15px;color:var(--ink-2);line-height:1.38}
.tip b{color:var(--ink)}

.scale{flex:1 1 auto;position:relative;display:flex;align-items:flex-start;padding-top:96px}
.line{position:absolute;left:0;right:0;top:108px;height:4px;background:linear-gradient(90deg,var(--brick) 0%%,var(--brick) 46%%,var(--taupe) 54%%,var(--taupe) 100%%);border-radius:3px}
.zones{position:absolute;left:0;right:0;top:62px;display:flex;font-size:12.5px;font-weight:700;letter-spacing:.14em;text-transform:uppercase}
.zones .z1{flex:0 0 50%%;color:var(--brick)}
.zones .z2{flex:0 0 50%%;color:var(--taupe);text-align:right}
.mk{flex:1 1 0;position:relative;padding-top:30px;text-align:center}
.mk .dot{position:absolute;left:50%%;top:4px;transform:translateX(-50%%);width:19px;height:19px;border-radius:50%%;background:var(--brick);border:4px solid #fff;box-shadow:0 0 0 1px var(--brick)}
.mk.far .dot{background:var(--taupe);box-shadow:0 0 0 1px var(--taupe)}
.mk .wh{font-size:15px;color:var(--ink-2);margin-bottom:18px;min-height:42px;padding:0 10px;line-height:1.3}
.sayz{display:inline-flex;align-items:baseline;gap:10px;background:var(--brick-soft);border:1px solid var(--brick);border-radius:13px;padding:14px 22px}
.mk.far .sayz{background:var(--grey-soft);border-color:var(--grey)}
.sayz .zh{font-family:'Noto Serif SC',serif;font-weight:700;font-size:33px;color:var(--brick-d);line-height:1.15}
.mk.far .sayz .zh{color:var(--ink)}
.sayz .py{font-size:14.5px;color:var(--ink-2);font-weight:600}

.foot{margin-top:18px;display:flex;align-items:center;gap:18px;background:var(--surface);border:1px solid var(--hair);border-radius:13px;padding:12px 22px}
.foot b{font-size:12.5px;font-weight:700;letter-spacing:.11em;text-transform:uppercase;color:var(--brick);flex:0 0 auto}
.foot span{font-size:15.5px;color:var(--ink);line-height:1.36}

.brand{position:absolute;left:72px;bottom:17px;display:flex;align-items:center;gap:11px;color:var(--ink)}
.brand b{font-family:'Cormorant Garamond',serif;font-weight:700;font-size:25px}
.brand .bdot{width:10px;height:10px;border-radius:50%%;background:var(--brick)}
.brand span{color:var(--taupe);font-size:16px}
</style></head><body>
<div class="card">
  <div class="head">
    <div>
      <div class="eyebrow">Грамматика</div>
      <h1>Указательные местоимения: <i>граница проходит по расстоянию</i></h1>
    </div>
    <div class="tip">Не по размеру и не по важности предмета. <b>Ближе ко мне — <span style="font-family:'Noto Serif SC',serif">这</span>, дальше — <span style="font-family:'Noto Serif SC',serif">那</span>.</b></div>
  </div>

  <div class="scale">
    <div class="zones"><div class="z1">ближняя зона</div><div class="z2">дальняя зона</div></div>
    <div class="line"></div>
    %(marks)s
  </div>

  <div class="foot"><b>и правило</b><span>между местоимением и предметом стоит счётное слово: <span style="font-family:'Noto Serif SC',serif">这本书</span>, а не <span style="font-family:'Noto Serif SC',serif">这书</span></span></div>

  <div class="brand"><span class="bdot"></span><b>Kitai School</b><span>&middot; kitai-school.ru</span></div>
</div>
</body></html>""" % dict(fonts=FONTS, vars=VARS, marks=marks)

open(S + "ukaz-hero.html", "w", encoding="utf-8").write(hero)

# ─────────── инфографика: конструктор фразы ───────────
blocks = ""
for han, py, role in PHRASE:
    blocks += ('<div class="blk"><span class="zh">%s</span><span class="py">%s</span>'
               '<span class="role">%s</span></div>' % (han, py, role))
assert blocks.count('class="blk"') == 4

bad_blocks = ""
for han, py, role in PHRASE:
    if han in BROKEN:
        bad_blocks += ('<div class="blk off"><span class="zh">%s</span>'
                       '<span class="py">%s</span><span class="role">%s</span></div>'
                       % (han, py, role))
    else:
        bad_blocks += ('<div class="gap"><span>нет</span><b>%s</b></div>' % role)
assert bad_blocks.count('class="gap"') == 1, "пропущен ровно один блок"

full_han = "".join(b[0] for b in PHRASE)
broken_han = "".join(BROKEN)
assert full_han == "这两本书" and broken_han == "这两书", "строки собираются из данных"

info = """<!DOCTYPE html><html lang="ru"><head><meta charset="utf-8">
%(fonts)s
<style>
%(vars)s
*{margin:0;box-sizing:border-box}html,body{width:1200px;height:%(h)dpx}
.wrap{width:1200px;height:%(h)dpx;background:linear-gradient(180deg,#fff 0%%,var(--cream) 44%%,var(--cream-2) 100%%);font-family:'Inter',sans-serif;padding:32px 48px 22px;display:flex;flex-direction:column;position:relative;overflow:hidden}
.wrap:before{content:"";position:absolute;left:0;right:0;top:0;height:9px;background:var(--brick)}
.top{display:flex;align-items:flex-end;justify-content:space-between;gap:34px;margin-bottom:22px}
.eyebrow{color:var(--brick);font-weight:700;font-size:15.5px;letter-spacing:.19em;text-transform:uppercase;margin-bottom:8px}
h2{font-family:'Cormorant Garamond',serif;font-weight:600;font-size:35px;line-height:1.08;color:var(--ink);max-width:24ch}
h2 i{font-style:italic;color:var(--brick)}
.hint{flex:0 0 352px;background:var(--surface);border:1px solid var(--hair);border-left:4px solid var(--brick);border-radius:13px;padding:12px 18px;font-size:14.5px;color:var(--ink-2);line-height:1.36}
.hint b{color:var(--ink)}

.rows{flex:1 1 auto;display:flex;flex-direction:column;gap:18px}
.row{flex:1 1 0;background:var(--surface);border:1px solid var(--hair);border-radius:15px;padding:16px 20px;display:flex;align-items:center;gap:20px}
.row.ok{border-color:var(--good);background:var(--good-soft)}
.row.no{border-color:var(--brick);background:var(--brick-soft)}
.tag{flex:0 0 118px;font-size:13px;font-weight:700;letter-spacing:.1em;text-transform:uppercase}
.row.ok .tag{color:var(--good)}
.row.no .tag{color:var(--brick)}
.chain{flex:1 1 auto;display:flex;align-items:stretch;gap:11px}
.blk{flex:1 1 0;background:var(--surface);border:1px solid var(--hair);border-radius:11px;padding:12px 10px;text-align:center;display:flex;flex-direction:column;justify-content:center}
.blk .zh{display:block;font-family:'Noto Serif SC',serif;font-weight:700;font-size:34px;color:var(--ink);line-height:1.15}
.blk .py{display:block;font-size:13px;color:var(--ink-2);margin-top:1px}
.blk .role{display:block;font-size:11.5px;color:var(--taupe);margin-top:5px}
.gap{flex:1 1 0;border:2px dashed var(--brick);border-radius:11px;padding:9px 10px;text-align:center;display:flex;flex-direction:column;justify-content:center;gap:4px}
.gap span{font-size:22px;font-weight:700;color:var(--brick);line-height:1}
.gap b{font-size:11.5px;color:var(--brick);font-weight:600}
.res{flex:0 0 212px;text-align:right}
.res .ph{font-family:'Noto Serif SC',serif;font-weight:700;font-size:31px;color:var(--ink);line-height:1.2}
.row.no .res .ph{color:var(--brick-d);text-decoration:line-through}
.res .tr{font-size:13.5px;color:var(--ink-2);margin-top:3px}

.foot{margin-top:18px;display:flex;align-items:center;gap:18px}
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
      <div class="eyebrow">Порядок сборки</div>
      <h2>Фраза держится <i>на счётном слове</i></h2>
    </div>
    <div class="hint">Порядок всегда один: <b>указательное, число, счётное слово, предмет</b>. Убрать можно только число.</div>
  </div>

  <div class="rows">
    <div class="row ok">
      <div class="tag">так говорят</div>
      <div class="chain">%(blocks)s</div>
      <div class="res"><div class="ph">%(full)s</div><div class="tr">эти две книги</div></div>
    </div>
    <div class="row no">
      <div class="tag">так нельзя</div>
      <div class="chain">%(bad)s</div>
      <div class="res"><div class="ph">%(broken)s</div><div class="tr">фраза не держится</div></div>
    </div>
  </div>

  <div class="foot">
    <div class="msg">Исключение одно: после <b>这些</b> и <b>那些</b> счётное слово уже не нужно — количество выражено самим словом</div>
    <div class="brand"><span class="dot2"></span><b>Kitai School</b><span>&middot; kitai-school.ru</span></div>
  </div>
</div>
</body></html>""" % dict(fonts=FONTS, vars=VARS, h=560, blocks=blocks, bad=bad_blocks,
                         full=full_han, broken=broken_han)

open(S + "ukaz-info.html", "w", encoding="utf-8").write(info)

print("ok | пар:", len(PAIRS), "| блоков:", len(PHRASE), "| отметок:", len(SCALE),
      "| фраза:", full_han, "против", broken_han)
