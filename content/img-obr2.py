# -*- coding: utf-8 -*-
# Картинки к статье «Уважительные обращения в Китае»
# Обложка     — реплики в облачках: как окликают и кого
# Инфографика — карта мест: куда пришёл, так и зовёшь
import sys
sys.path.insert(0, "/home/user/Kitai-Shool/content")
from obrash import ADDR, PREFIX

S = ("/tmp/claude-0/-home-user-Kitai-Shool/a463bfca-82a9-56fd-ae09-42a7257ff999/"
     "scratchpad/")

FONTS = ("<link href=\"https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,600;0,700;1,600"
         "&family=Inter:wght@400;500;600;700&family=Noto+Serif+SC:wght@600;700&display=swap\" rel=\"stylesheet\">")
VARS = (":root{--brick:#A41E3A;--brick-d:#841630;--brick-soft:#F7E6EB;--ink:#2C2420;--ink-2:#5A4F45;"
        "--taupe:#8B7D6B;--cream:#FAF7F2;--cream-2:#F3EDE3;--hair:#EAE3D8;--surface:#fff;"
        "--paper:#FFFDF8;--good:#2F6F4F;--good-soft:#E8F3EC;--grey:#8A8178;--grey-soft:#EFEDE8}")

BY = {a[0]: a for a in ADDR}
for need in ("师傅", "老师", "老板", "阿姨"):
    assert need in BY, "на обложке нужно обращение %s" % need
assert "先生" not in BY, "先生 разобран у соседа — на картинки не берём"

# ─────────── обложка: четыре реплики ───────────
SPEECH = ["师傅", "老师", "老板", "阿姨"]
bub = ""
for han in SPEECH:
    _, py, mean, place, who, note = BY[han]
    bub += ('<div class="bub"><div class="say"><span class="zh">%s</span>'
            '<span class="py">%s</span></div>'
            '<div class="to"><b>%s</b><span>%s</span></div></div>'
            % (han, py, mean, who))
assert bub.count('class="bub"') == 4, "на обложке четыре реплики"

hero = """<!DOCTYPE html><html lang="ru"><head><meta charset="utf-8">
%(fonts)s
<style>
%(vars)s
*{margin:0;box-sizing:border-box}html,body{width:1200px;height:630px}
.card{width:1200px;height:630px;background:radial-gradient(1040px 700px at 12%% 4%%, #fff 0%%, var(--cream) 54%%, var(--cream-2) 100%%);position:relative;overflow:hidden;font-family:'Inter',sans-serif;padding:30px 56px 52px 72px;display:flex;flex-direction:column}
.card:before{content:"";position:absolute;left:0;top:0;bottom:0;width:12px;background:var(--brick)}
.head{display:flex;justify-content:space-between;align-items:flex-end;gap:34px;margin-bottom:22px}
.eyebrow{color:var(--brick);font-weight:700;font-size:18px;letter-spacing:.19em;text-transform:uppercase;margin-bottom:9px}
h1{font-family:'Cormorant Garamond',serif;font-weight:600;font-size:37px;line-height:1.07;color:var(--ink);letter-spacing:-.3px;max-width:23ch}
h1 i{font-style:italic;color:var(--brick)}
.tip{flex:0 0 330px;background:var(--surface);border:1px solid var(--hair);border-left:4px solid var(--brick);border-radius:13px;padding:13px 18px;font-size:15px;color:var(--ink-2);line-height:1.38}
.tip b{color:var(--ink)}

.bubs{display:flex;flex-direction:column;gap:14px;flex:1 1 auto}
.bub{display:flex;align-items:stretch;gap:0}
.say{flex:0 0 342px;background:var(--brick-soft);border:1px solid var(--brick);border-radius:16px 16px 16px 4px;padding:11px 24px;display:flex;align-items:baseline;gap:14px;position:relative}
.say .zh{font-family:'Noto Serif SC',serif;font-weight:700;font-size:40px;color:var(--brick-d);line-height:1.15}
.say .py{font-size:19px;color:var(--ink);font-weight:600}
.to{flex:1 1 auto;margin-left:26px;background:var(--surface);border:1px solid var(--hair);border-radius:13px;padding:11px 22px;display:flex;align-items:center;gap:16px}
.to b{flex:0 0 136px;font-size:17px;color:var(--ink)}
.to span{font-size:15.5px;color:var(--ink-2);line-height:1.35}

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
      <div class="eyebrow">Этикет</div>
      <h1>Уважительные обращения в Китае: <i>зовут по роли, а не по полу</i></h1>
    </div>
    <div class="tip">Универсального «простите» здесь нет. <b>Сначала называют человека</b> — и только потом задают вопрос.</div>
  </div>

  <div class="bubs">%(bub)s</div>

  <div class="foot"><b>и ещё</b><span>внутри коллектива работают приставки <span style="font-family:'Noto Serif SC',serif">小</span> и <span style="font-family:'Noto Serif SC',serif">老</span> перед фамилией: они задают не вежливость, а дистанцию</span></div>

  <div class="brand"><span class="bdot"></span><b>Kitai School</b><span>&middot; kitai-school.ru</span></div>
</div>
</body></html>""" % dict(fonts=FONTS, vars=VARS, bub=bub)

open(S + "obr2-hero.html", "w", encoding="utf-8").write(hero)

# ─────────── инфографика: карта мест ───────────
SPOTS = [
    ("такси", "师傅"),
    ("магазин", "美女"),
    ("школа", "老师"),
    ("лавка", "老板"),
    ("ресторан", "服务员"),
    ("двор", "阿姨"),
]
for place, han in SPOTS:
    assert han in BY, "обращение %s должно быть в данных" % han
    assert place in BY[han][3], "место «%s» должно стоять у обращения %s" % (place, han)
assert len(SPOTS) == 6, "мест на карте шесть"
assert len(set(h for _, h in SPOTS)) == 6, \
    "на карте шесть разных обращений, а не одно и то же дважды"

spots = ""
for place, han in SPOTS:
    _, py, mean, _, who, note = BY[han]
    warn = ('<div class="warn">%s</div>' % note) if note else ""
    spots += ("""<div class="spot">
  <div class="pl">%(place)s</div>
  <div class="sz"><span class="zh">%(han)s</span><span class="py">%(py)s</span></div>
  <div class="who">%(who)s</div>
  %(warn)s
</div>""" % dict(place=place, han=han, py=py, who=who, warn=warn))
assert spots.count('class="spot"') == 6, "на карте шесть точек"

info = """<!DOCTYPE html><html lang="ru"><head><meta charset="utf-8">
%(fonts)s
<style>
%(vars)s
*{margin:0;box-sizing:border-box}html,body{width:1200px;height:%(h)dpx}
.wrap{width:1200px;height:%(h)dpx;background:linear-gradient(180deg,#fff 0%%,var(--cream) 44%%,var(--cream-2) 100%%);font-family:'Inter',sans-serif;padding:32px 48px 22px;display:flex;flex-direction:column;position:relative;overflow:hidden}
.wrap:before{content:"";position:absolute;left:0;right:0;top:0;height:9px;background:var(--brick)}
.top{display:flex;align-items:flex-end;justify-content:space-between;gap:34px;margin-bottom:18px}
.eyebrow{color:var(--brick);font-weight:700;font-size:15.5px;letter-spacing:.19em;text-transform:uppercase;margin-bottom:8px}
h2{font-family:'Cormorant Garamond',serif;font-weight:600;font-size:35px;line-height:1.08;color:var(--ink);max-width:24ch}
h2 i{font-style:italic;color:var(--brick)}
.hint{flex:0 0 358px;background:var(--surface);border:1px solid var(--hair);border-left:4px solid var(--brick);border-radius:13px;padding:12px 18px;font-size:14.5px;color:var(--ink-2);line-height:1.36}
.hint b{color:var(--ink)}

.map{flex:1 1 auto;display:grid;grid-template-columns:repeat(3,1fr);gap:14px}
.spot{background:var(--surface);border:1px solid var(--hair);border-radius:14px;padding:13px 17px 12px;display:flex;flex-direction:column;position:relative}
.spot:before{content:"";position:absolute;left:17px;top:0;width:34px;height:4px;background:var(--brick);border-radius:0 0 3px 3px}
.pl{font-size:12px;font-weight:700;letter-spacing:.13em;text-transform:uppercase;color:var(--taupe);margin-bottom:8px}
.sz{display:flex;align-items:baseline;gap:10px;margin-bottom:7px}
.sz .zh{font-family:'Noto Serif SC',serif;font-weight:700;font-size:31px;color:var(--brick-d);line-height:1.1}
.sz .py{font-size:15px;font-weight:600;color:var(--ink)}
.who{font-size:14px;color:var(--ink-2);line-height:1.38}
.warn{margin-top:auto;padding-top:9px;font-size:12.5px;color:var(--brick);line-height:1.3}

.foot{margin-top:15px;display:flex;align-items:center;gap:18px}
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
      <div class="eyebrow">Куда пришёл, так и зовёшь</div>
      <h2>Обращение подсказывает <i>само место</i></h2>
    </div>
    <div class="hint">Один и тот же человек за рулём — <b>師傅</b>, в своей лавке — <b>老板</b>, у себя во дворе — <b>叔叔</b>.</div>
  </div>

  <div class="map">%(spots)s</div>

  <div class="foot">
    <div class="msg">Если роль неясна, берите <b>老师</b>: оно уважительное и почти нигде не звучит неуместно</div>
    <div class="brand"><span class="dot2"></span><b>Kitai School</b><span>&middot; kitai-school.ru</span></div>
  </div>
</div>
</body></html>""" % dict(fonts=FONTS, vars=VARS, h=560, spots=spots)

# на картинке знаки должны быть в упрощённом написании, как в тексте
info = info.replace("師傅", "师傅")
assert "師" not in info, "на картинке только упрощённые знаки"

open(S + "obr2-info.html", "w", encoding="utf-8").write(info)

print("ok | обращений:", len(ADDR), "| реплик:", len(SPEECH), "| мест:", len(SPOTS),
      "| приставок:", len(PREFIX))
