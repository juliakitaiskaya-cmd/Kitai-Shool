# -*- coding: utf-8 -*-
# Картинки к статье «Список слов HSK по уровням»
# Обложка     — парные столбцы: прежний словник и действующий, с коэффициентом
# Инфографика — три уровня, по каждому три цифры: черновик, действующий, прежний
import sys
sys.path.insert(0, "/home/user/Kitai-Shool/content")
from slova import (OLD, NEW, NEW_TOP, DRAFT, DRAFT_YEAR, FINAL_MONTH, LEVELS, OLD_D, NEW_D,
                   DRAFT_D, DRAFT_GAP, RATIO, NEW_STEPS, STALE_SIGNS, FINAL_WHEN)

S = ("/tmp/claude-0/-home-user-Kitai-Shool/a463bfca-82a9-56fd-ae09-42a7257ff999/"
     "scratchpad/")

FONTS = ("<link href=\"https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,600;0,700;1,600"
         "&family=Inter:wght@400;500;600;700&display=swap\" rel=\"stylesheet\">")
VARS = (":root{--brick:#A41E3A;--brick-d:#841630;--brick-soft:#F7E6EB;--ink:#2C2420;--ink-2:#5A4F45;"
        "--taupe:#8B7D6B;--cream:#FAF7F2;--cream-2:#F3EDE3;--hair:#EAE3D8;--surface:#fff;"
        "--grey-soft:#EFEDE8;--grey:#9A9289}")


def sp(n):
    """Разряды отделяем узким пробелом: 5400 → 5 400."""
    s = str(n)
    return s if len(s) < 4 else s[:-3] + " " + s[-3:]


# ─────────── обложка: парные столбцы ───────────
TOP = max(NEW_D[l] for l in LEVELS)
MAXH, MINH = 232, 13
assert TOP == NEW_D[6]

pairs = ""
for lvl in LEVELS:
    ho = round(MINH + (MAXH - MINH) * (OLD_D[lvl] - 0) / TOP)
    hn = round(MINH + (MAXH - MINH) * (NEW_D[lvl] - 0) / TOP)
    pairs += ("""<div class="pr">
  <div class="bars">
    <div class="bw"><span class="v old">%(vo)s</span><div class="b old" style="height:%(ho)dpx"></div></div>
    <div class="bw"><span class="v new">%(vn)s</span><div class="b new" style="height:%(hn)dpx"></div></div>
  </div>
  <div class="lv">HSK %(lvl)d</div>
  <div class="rt">&times;%(rt)s</div>
</div>""" % dict(vo=sp(OLD_D[lvl]), vn=sp(NEW_D[lvl]), ho=ho, hn=hn, lvl=lvl,
                 rt=("%.2f" % RATIO[lvl]).rstrip("0").rstrip(".").replace(".", ",")))
assert pairs.count('class="pr"') == 6
assert pairs.count('class="b old"') == 6 and pairs.count('class="b new"') == 6

hero = """<!DOCTYPE html><html lang="ru"><head><meta charset="utf-8">
%(fonts)s
<style>
%(vars)s
*{margin:0;box-sizing:border-box}html,body{width:1200px;height:630px}
.card{width:1200px;height:630px;background:radial-gradient(1040px 700px at 8%% 4%%, #fff 0%%, var(--cream) 54%%, var(--cream-2) 100%%);position:relative;overflow:hidden;font-family:'Inter',sans-serif;padding:26px 56px 50px 72px;display:flex;flex-direction:column}
.card:before{content:"";position:absolute;left:0;top:0;bottom:0;width:12px;background:var(--brick)}
.head{display:flex;justify-content:space-between;align-items:flex-end;gap:34px;margin-bottom:14px}
.eyebrow{color:var(--brick);font-weight:700;font-size:18px;letter-spacing:.19em;text-transform:uppercase;margin-bottom:8px}
h1{font-family:'Cormorant Garamond',serif;font-weight:600;font-size:38px;line-height:1.08;color:var(--ink);letter-spacing:-.3px;max-width:29ch}
h1 i{font-style:italic;color:var(--brick)}
.tip{flex:0 0 318px;background:var(--surface);border:1px solid var(--hair);border-left:4px solid var(--brick);border-radius:13px;padding:12px 18px;font-size:14.5px;color:var(--ink-2);line-height:1.38}
.tip b{color:var(--ink)}

.key{display:flex;gap:22px;margin-bottom:10px;font-size:13.5px;color:var(--ink-2)}
.key i{font-style:normal;display:inline-flex;align-items:center;gap:7px}
.key .sw{width:15px;height:15px;border-radius:4px;display:inline-block}
.key .sw.o{background:var(--grey-soft);border:1px solid var(--hair)}
.key .sw.n{background:var(--brick-soft);border:1px solid var(--brick)}

.stage{flex:1 1 auto;min-height:0;display:flex;align-items:flex-end;gap:16px}
.pr{flex:1 1 0;display:flex;flex-direction:column;align-items:center}
.bars{width:100%%;display:flex;align-items:flex-end;justify-content:center;gap:9px}
.bw{flex:1 1 0;display:flex;flex-direction:column;align-items:center}
.v{font-size:15px;font-weight:600;margin-bottom:6px;white-space:nowrap}
.v.old{color:var(--taupe)}
.v.new{color:var(--brick-d);font-size:16.5px;font-weight:700}
.b{width:100%%;border-radius:7px 7px 0 0}
.b.old{background:var(--grey-soft);border:1px solid var(--hair);border-bottom:none}
.b.new{background:var(--brick-soft);border:1px solid var(--brick);border-bottom:none}
.lv{width:100%%;text-align:center;border-top:3px solid var(--taupe);padding-top:8px;font-size:16px;font-weight:700;color:var(--ink)}
.rt{margin-top:6px;font-size:14px;font-weight:700;color:var(--brick)}

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
      <div class="eyebrow">Словарь по уровням</div>
      <h1>Требования выросли <i>неравномерно</i></h1>
    </div>
    <div class="tip">Цифры накопительные: сколько слов нужно знать к концу уровня. <b>Под парой — во сколько раз стало больше.</b></div>
  </div>

  <div class="key">
    <i><span class="sw o"></span>прежний стандарт</i>
    <i><span class="sw n"></span>действующий словник</i>
  </div>

  <div class="stage">%(pairs)s</div>

  <div class="foot"><b>что это значит</b><span>на первом уровне слов стало вдвое больше, а на шестом разница почти исчезает: вся прибавка пришлась на начало пути</span></div>

  <div class="brand"><span class="bdot"></span><b>Kitai School</b><span>&middot; kitai-school.ru</span></div>
</div>
</body></html>""" % dict(fonts=FONTS, vars=VARS, pairs=pairs)

assert "%%" not in hero, "в разметке остались двойные проценты"
open(S + "slova-hero.html", "w", encoding="utf-8").write(hero)

# ─────────── инфографика: черновик против действующего ───────────
cards = ""
for lvl, draft in DRAFT:
    cards += ("""<div class="cd">
  <div class="hd">HSK %(lvl)d</div>
  <div class="num stale"><b>%(draft)s</b><span>черновик %(yr)d года</span></div>
  <div class="num live"><b>%(live)s</b><span>действующий словник</span></div>
  <div class="num past"><b>%(past)s</b><span>прежний стандарт</span></div>
  <div class="gap">лишних слов в черновике: <b>%(gap)s</b></div>
</div>""" % dict(lvl=lvl, draft=sp(draft), live=sp(NEW_D[lvl]), past=sp(OLD_D[lvl]),
                 gap=sp(DRAFT_GAP[lvl]), yr=DRAFT_YEAR))
assert cards.count('class="cd"') == len(DRAFT) == 3
assert cards.count('class="num stale"') == 3

signs = "".join('<div class="sg"><b>%s</b><span>%s</span></div>' % (a, b)
                for a, b in STALE_SIGNS)
assert signs.count('class="sg"') == len(STALE_SIGNS) == 3

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
.hint0{flex:0 0 348px;background:var(--surface);border:1px solid var(--hair);border-left:4px solid var(--brick);border-radius:13px;padding:11px 17px;font-size:14px;color:var(--ink-2);line-height:1.35}
.hint0 b{color:var(--ink)}

.cards{flex:1 1 auto;min-height:0;display:flex;gap:14px}
.cd{flex:1 1 0;background:var(--surface);border:1px solid var(--hair);border-radius:14px;padding:14px 18px 13px;display:flex;flex-direction:column}
.hd{font-size:19px;font-weight:700;color:var(--ink);margin-bottom:11px}
.num{display:flex;align-items:baseline;gap:11px;padding:8px 12px;border-radius:10px;margin-bottom:7px}
.num b{font-family:'Cormorant Garamond',serif;font-weight:700;font-size:30px;line-height:1;min-width:76px}
.num span{font-size:12.5px;line-height:1.25}
.num.stale{background:var(--grey-soft);border:1px dashed var(--grey)}
.num.stale b{color:var(--grey);text-decoration:line-through}
.num.stale span{color:var(--taupe)}
.num.live{background:var(--brick-soft);border:1px solid var(--brick)}
.num.live b{color:var(--brick-d)}
.num.live span{color:var(--ink)}
.num.past{background:transparent;border:1px solid var(--hair)}
.num.past b{color:var(--taupe)}
.num.past span{color:var(--taupe)}
.gap{margin-top:auto;padding-top:9px;font-size:13px;color:var(--ink-2)}
.gap b{color:var(--brick)}

.signs{margin-top:16px;flex:0 0 auto;display:flex;gap:11px}
.sg{flex:1 1 0;background:var(--surface);border:1px solid var(--hair);border-left:4px solid var(--brick);border-radius:12px;padding:10px 15px}
.sg b{display:block;font-size:14.5px;color:var(--ink);margin-bottom:2px}
.sg span{font-size:13px;color:var(--ink-2);line-height:1.3}

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
      <div class="eyebrow">Три цифры на один уровень</div>
      <h2>Списки из сети считают <i>по черновику</i></h2>
    </div>
    <div class="hint0">Перечёркнуто то, что устарело. <b>Действующий словник опубликован в %(fm)s и требования младших уровней снизил.</b></div>
  </div>

  <div class="cards">%(cards)s</div>

  <div class="signs">%(signs)s</div>

  <div class="foot">
    <div class="msg">Проверить список просто: <b>посчитайте в нём позиции</b> и сравните с действующей цифрой своего уровня</div>
    <div class="brand"><span class="dot2"></span><b>Kitai School</b><span>&middot; kitai-school.ru</span></div>
  </div>
</div>
</body></html>""" % dict(fonts=FONTS, vars=VARS, h=556, cards=cards, signs=signs, fm=FINAL_WHEN)

assert "%%" not in info, "в разметке остались двойные проценты"
open(S + "slova-info.html", "w", encoding="utf-8").write(info)

print("ok | отношение:", [(l, RATIO[l]) for l in LEVELS],
      "| расхождение с черновиком:", DRAFT_GAP)
