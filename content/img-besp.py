# -*- coding: utf-8 -*-
# Картинки к статье «Бесплатное обучение китайскому под HSK 3.0»
# Обложка     — путь к сертификату с платными воротами
# Инфографика — полосы «докуда дотягивает бесплатное» по навыкам
import sys
sys.path.insert(0, "/home/user/Kitai-Shool/content")
from besplatno import SKILLS, GATES, FREE, PART, PAID, BY_STATE, HARD

S = ("/tmp/claude-0/-home-user-Kitai-Shool/a463bfca-82a9-56fd-ae09-42a7257ff999/"
     "scratchpad/")

FONTS = ("<link href=\"https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,600;0,700;1,600"
         "&family=Inter:wght@400;500;600;700&family=Noto+Serif+SC:wght@600;700&display=swap\" rel=\"stylesheet\">")
VARS = (":root{--brick:#A41E3A;--brick-d:#841630;--brick-soft:#F7E6EB;--ink:#2C2420;--ink-2:#5A4F45;"
        "--taupe:#8B7D6B;--cream:#FAF7F2;--cream-2:#F3EDE3;--hair:#EAE3D8;--surface:#fff;"
        "--grey-soft:#EFEDE8;--good:#2F6F4F;--good-soft:#E8F3EC}")

assert len(SKILLS) == 6 and len(GATES) == 4

# ─────────── обложка: путь с воротами ───────────
STAGES = [
    ("старт", "выбрали уровень"),
    ("лексика и чтение", "проходится даром"),
    ("формат и аудирование", "даром наполовину"),
    ("письмо и звук", "нужна проверка"),
    ("экзамен", "взнос обязателен"),
    ("сертификат", "получен"),
]
assert len(STAGES) == 6

PAID_AT = {3, 4}  # индексы этапов, перед которыми стоят ворота
road = ""
for i, (name, note) in enumerate(STAGES):
    gate = ""
    if i in PAID_AT:
        gate = '<div class="gate"><span>!</span>платно</div>'
    road += ("""%(gate)s<div class="st%(cls)s">
  <div class="dot"></div>
  <div class="sname">%(name)s</div>
  <div class="snote">%(note)s</div>
</div>""" % dict(gate=gate, name=name, note=note,
                 cls=" paid" if i in PAID_AT else ""))
assert road.count('class="gate"') == len(PAID_AT) == 2
assert road.count('class="st') == 6

hero = """<!DOCTYPE html><html lang="ru"><head><meta charset="utf-8">
%(fonts)s
<style>
%(vars)s
*{margin:0;box-sizing:border-box}html,body{width:1200px;height:630px}
.card{width:1200px;height:630px;background:radial-gradient(1040px 700px at 10%% 4%%, #fff 0%%, var(--cream) 54%%, var(--cream-2) 100%%);position:relative;overflow:hidden;font-family:'Inter',sans-serif;padding:28px 56px 50px 72px;display:flex;flex-direction:column}
.card:before{content:"";position:absolute;left:0;top:0;bottom:0;width:12px;background:var(--brick)}
.head{display:flex;justify-content:space-between;align-items:flex-end;gap:34px;margin-bottom:24px}
.eyebrow{color:var(--brick);font-weight:700;font-size:18px;letter-spacing:.19em;text-transform:uppercase;margin-bottom:8px}
h1{font-family:'Cormorant Garamond',serif;font-weight:600;font-size:38px;line-height:1.07;color:var(--ink);letter-spacing:-.3px;max-width:27ch}
h1 i{font-style:italic;color:var(--brick)}
.tip{flex:0 0 322px;background:var(--surface);border:1px solid var(--hair);border-left:4px solid var(--brick);border-radius:13px;padding:12px 18px;font-size:14.5px;color:var(--ink-2);line-height:1.38}
.tip b{color:var(--ink)}

.roadbox{flex:1 1 auto;background:var(--surface);border:1px solid var(--hair);border-radius:16px;padding:22px 28px 18px;display:flex;flex-direction:column;justify-content:center}
.road{position:relative;display:flex;align-items:flex-start;gap:0}
.road:before{content:"";position:absolute;left:18px;right:18px;top:9px;height:4px;background:var(--hair);border-radius:2px}
.st{flex:1 1 0;position:relative;text-align:center;padding:0 6px}
.dot{width:20px;height:20px;border-radius:50%%;background:var(--good);border:4px solid #fff;box-shadow:0 0 0 1px var(--hair);margin:0 auto 11px}
.st.paid .dot{background:var(--brick)}
.sname{font-size:15px;font-weight:700;color:var(--ink);line-height:1.25}
.snote{font-size:13px;color:var(--taupe);margin-top:4px;line-height:1.3}
.st.paid .snote{color:var(--brick)}
.gate{flex:0 0 44px;position:relative;text-align:center;padding-top:1px}
.gate span{display:block;width:34px;height:34px;margin:0 auto 5px;border-radius:9px;background:var(--brick);color:#fff;font-size:17px;font-weight:700;line-height:34px}
.gate{font-size:11px;letter-spacing:.08em;text-transform:uppercase;color:var(--brick);font-weight:700}

.legend{display:flex;gap:22px;margin-top:22px;justify-content:center}
.gates{display:flex;gap:13px;margin-top:14px;flex:0 0 auto}
.gt{flex:1 1 0;background:var(--surface);border:1px solid var(--hair);border-radius:12px;padding:10px 14px}
.gt.hard{border-color:var(--brick);background:var(--brick-soft)}
.gt b{display:block;font-size:14px;color:var(--ink);line-height:1.3}
.gt span{display:block;font-size:12.5px;color:var(--taupe);margin-top:4px}
.gt.hard span{color:var(--brick);font-weight:600}
.lg{display:flex;align-items:center;gap:8px;font-size:14px;color:var(--ink-2)}
.lg i{width:13px;height:13px;border-radius:50%%;display:block}
.lg .g{background:var(--good)}
.lg .r{background:var(--brick)}

.foot{margin-top:14px;flex:0 0 auto;display:flex;align-items:center;gap:18px;background:var(--surface);border:1px solid var(--hair);border-radius:13px;padding:11px 22px}
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
      <div class="eyebrow">Подготовка</div>
      <h1>Путь к сертификату: <i>где даром, а где придётся заплатить</i></h1>
    </div>
    <div class="tip">Большая часть пути проходится самостоятельно. <b>Но два шлюза не обходятся никак.</b></div>
  </div>

  <div class="roadbox">
    <div class="road">%(road)s</div>
    <div class="legend">
      <div class="lg"><i class="g"></i>проходится без денег</div>
      <div class="lg"><i class="r"></i>здесь нужен человек или взнос</div>
    </div>
  </div>

  <div class="gates">%(gates)s</div>

  <div class="foot"><b>главное</b><span>если бюджет мал, покупайте проверку, а не объяснения: прочитать можно самому, услышать свою ошибку — нет</span></div>

  <div class="brand"><span class="bdot"></span><b>Kitai School</b><span>&middot; kitai-school.ru</span></div>
</div>
</body></html>""" % dict(fonts=FONTS, vars=VARS, road=road,
         gates="".join('<div class="gt%s"><b>%s</b><span>%s</span></div>'
                       % (" hard" if around == "обойти нельзя" else "", what, around)
                       for what, cost, around in GATES))

assert "%%" not in hero, "в разметке остались двойные проценты"
open(S + "besp-hero.html", "w", encoding="utf-8").write(hero)

# ─────────── инфографика: полосы по навыкам ───────────
CLS = {FREE: "free", PART: "part", PAID: "paid"}
bars = ""
for name, pct, state, how, limit in SKILLS:
    bars += ("""<div class="br">
  <div class="bname">%(name)s<span>%(state)s</span></div>
  <div class="track"><span class="fill %(cls)s" style="width:%(pct)d%%"></span><b class="pct">%(pct)d%%</b></div>
  <div class="lim">%(limit)s</div>
</div>""" % dict(name=name, state=state, cls=CLS[state], pct=pct, limit=limit))
assert bars.count('class="br"') == 6
assert bars.count('class="fill free"') == 2 and bars.count('class="fill paid"') == 2

info = """<!DOCTYPE html><html lang="ru"><head><meta charset="utf-8">
%(fonts)s
<style>
%(vars)s
*{margin:0;box-sizing:border-box}html,body{width:1200px;height:%(h)dpx}
.wrap{width:1200px;height:%(h)dpx;background:linear-gradient(180deg,#fff 0%%,var(--cream) 46%%,var(--cream-2) 100%%);font-family:'Inter',sans-serif;padding:30px 48px 26px;display:flex;flex-direction:column;position:relative;overflow:hidden}
.wrap:before{content:"";position:absolute;left:0;right:0;top:0;height:9px;background:var(--brick)}
.top{display:flex;align-items:flex-end;justify-content:space-between;gap:34px;margin-bottom:18px}
.eyebrow{color:var(--brick);font-weight:700;font-size:15.5px;letter-spacing:.19em;text-transform:uppercase;margin-bottom:7px}
h2{font-family:'Cormorant Garamond',serif;font-weight:600;font-size:34px;line-height:1.08;color:var(--ink);max-width:23ch}
h2 i{font-style:italic;color:var(--brick)}
.hint0{flex:0 0 346px;background:var(--surface);border:1px solid var(--hair);border-left:4px solid var(--brick);border-radius:13px;padding:11px 17px;font-size:14px;color:var(--ink-2);line-height:1.35}
.hint0 b{color:var(--ink)}

.bars{flex:1 1 auto;min-height:0;display:flex;flex-direction:column;gap:11px}
.br{flex:1 1 0;background:var(--surface);border:1px solid var(--hair);border-radius:13px;padding:11px 20px;display:flex;align-items:center;gap:20px}
.bname{flex:0 0 212px;font-size:16.5px;font-weight:700;color:var(--ink);line-height:1.2}
.bname span{display:block;font-size:12px;font-weight:600;color:var(--taupe);margin-top:3px;text-transform:uppercase;letter-spacing:.08em}
.track{flex:0 0 400px;position:relative;height:22px;background:var(--grey-soft);border-radius:11px;overflow:visible}
.fill{position:absolute;left:0;top:0;bottom:0;border-radius:11px}
.fill.free{background:var(--good);opacity:.85}
.fill.part{background:var(--brick);opacity:.55}
.fill.paid{background:var(--brick);opacity:.9}
.pct{position:absolute;right:-52px;top:1px;font-size:15px;font-weight:700;color:var(--ink-2)}
.lim{flex:1 1 auto;padding-left:44px;font-size:13.5px;color:var(--ink-2);line-height:1.34}

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
      <div class="eyebrow">Границы бесплатного</div>
      <h2>Докуда дотягивает <i>самостоятельная работа</i></h2>
    </div>
    <div class="hint0">Длина полосы — часть навыка, которую вы закроете сами. <b>Доли оценены по опыту занятий, это не измерение.</b></div>
  </div>

  <div class="bars">%(bars)s</div>

  <div class="foot">
    <div class="msg">Чем ниже в списке, <b>тем сильнее нужен человек со стороны</b>: там, где нет эталона, самопроверка не работает</div>
    <div class="brand"><span class="dot2"></span><b>Kitai School</b><span>&middot; kitai-school.ru</span></div>
  </div>
</div>
</body></html>""" % dict(fonts=FONTS, vars=VARS, h=720, bars=bars)

assert "%%" not in info, "в разметке остались двойные проценты"
open(S + "besp-info.html", "w", encoding="utf-8").write(info)

print("ok | этапов:", len(STAGES), "| ворот:", len(PAID_AT), "| навыков:", len(SKILLS))
