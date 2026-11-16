# -*- coding: utf-8 -*-
# Картинки к статье «HSK 1: что нужно знать»
# Обложка     — два круга словаря: площадь пропорциональна числу слов
# Инфографика — пять требований «было → стало» с меткой статуса у каждого
import sys, math
sys.path.insert(0, "/home/user/Kitai-Shool/content")
from hsk1 import (REQS, CONF, DESC, WORDS_OLD, WORDS_NEW, CHARS_READ, CHARS_WRITE, SPEED,
                  GROWTH, WRITE_SHARE, CONFIRMED, UNCONFIRMED, NEW_WORK, PER_WEEK, WEEKS)

S = ("/tmp/claude-0/-home-user-Kitai-Shool/a463bfca-82a9-56fd-ae09-42a7257ff999/"
     "scratchpad/")

FONTS = ("<link href=\"https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,600;0,700;1,600"
         "&family=Inter:wght@400;500;600;700&display=swap\" rel=\"stylesheet\">")
VARS = (":root{--brick:#A41E3A;--brick-d:#841630;--brick-soft:#F7E6EB;--ink:#2C2420;--ink-2:#5A4F45;"
        "--taupe:#8B7D6B;--cream:#FAF7F2;--cream-2:#F3EDE3;--hair:#EAE3D8;--surface:#fff;"
        "--grey-soft:#EFEDE8;--grey:#9A9289}")

# ─────────── обложка: два круга, площадь по числу слов ───────────
D_NEW = 288
D_OLD = round(D_NEW * math.sqrt(float(WORDS_OLD) / WORDS_NEW))
assert D_OLD < D_NEW, "прежний круг меньше действующего"
assert abs(D_OLD - round(D_NEW / math.sqrt(2))) <= 1, \
    "диаметр считается из корня отношения, а не на глаз"

hero = """<!DOCTYPE html><html lang="ru"><head><meta charset="utf-8">
%(fonts)s
<style>
%(vars)s
*{margin:0;box-sizing:border-box}html,body{width:1200px;height:630px}
.card{width:1200px;height:630px;background:radial-gradient(1040px 700px at 8%% 4%%, #fff 0%%, var(--cream) 54%%, var(--cream-2) 100%%);position:relative;overflow:hidden;font-family:'Inter',sans-serif;padding:28px 56px 50px 72px;display:flex;flex-direction:column}
.card:before{content:"";position:absolute;left:0;top:0;bottom:0;width:12px;background:var(--brick)}
.head{display:flex;justify-content:space-between;align-items:flex-end;gap:34px;margin-bottom:10px}
.eyebrow{color:var(--brick);font-weight:700;font-size:18px;letter-spacing:.19em;text-transform:uppercase;margin-bottom:8px}
h1{font-family:'Cormorant Garamond',serif;font-weight:600;font-size:39px;line-height:1.08;color:var(--ink);letter-spacing:-.3px;max-width:26ch}
h1 i{font-style:italic;color:var(--brick)}
.tip{flex:0 0 320px;background:var(--surface);border:1px solid var(--hair);border-left:4px solid var(--brick);border-radius:13px;padding:12px 18px;font-size:14.5px;color:var(--ink-2);line-height:1.38}
.tip b{color:var(--ink)}

.mid{flex:1 1 auto;min-height:0;display:flex;align-items:center;gap:40px}
.circles{flex:0 0 auto;display:flex;align-items:flex-end;gap:34px;padding-left:14px}
.cw{display:flex;flex-direction:column;align-items:center}
.ci{border-radius:50%%;display:flex;align-items:center;justify-content:center}
.ci.old{width:%(dold)dpx;height:%(dold)dpx;background:var(--grey-soft);border:1px solid var(--hair)}
.ci.new{width:%(dnew)dpx;height:%(dnew)dpx;background:var(--brick-soft);border:2px solid var(--brick)}
.ci b{font-family:'Cormorant Garamond',serif;font-weight:700;line-height:1}
.ci.old b{font-size:54px;color:var(--taupe)}
.ci.new b{font-size:76px;color:var(--brick-d)}
.cl{margin-top:12px;font-size:14.5px;color:var(--ink-2);text-align:center}
.cl b{display:block;font-size:16px;color:var(--ink);margin-bottom:2px}
.cw.o .cl b{color:var(--taupe)}

.right{flex:1 1 auto;display:flex;flex-direction:column;gap:12px}
.rc{background:var(--surface);border:1px solid var(--hair);border-radius:14px;padding:13px 20px}
.rc.on{border-color:var(--brick)}
.rc .n{font-family:'Cormorant Garamond',serif;font-weight:700;font-size:32px;color:var(--ink);line-height:1}
.rc.on .n{color:var(--brick)}
.rc .t{margin-top:5px;font-size:14.5px;color:var(--ink-2);line-height:1.34}
.rc .t b{color:var(--ink)}
.note{font-size:13px;color:var(--taupe);line-height:1.35}

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
      <div class="eyebrow">HSK 1</div>
      <h1>Слов стало <i>вдвое больше</i></h1>
    </div>
    <div class="tip">Круги нарисованы по площади: во втором ровно вдвое больше места. <b>И впервые появилось письмо от руки.</b></div>
  </div>

  <div class="mid">
    <div class="circles">
      <div class="cw o">
        <div class="ci old"><b>%(wold)d</b></div>
        <div class="cl"><b>было</b>прежняя редакция</div>
      </div>
      <div class="cw">
        <div class="ci new"><b>%(wnew)d</b></div>
        <div class="cl"><b>стало</b>действующие требования</div>
      </div>
    </div>

    <div class="right">
      <div class="rc"><div class="n">около %(read)d</div><div class="t">знаков нужно <b>узнавать</b></div></div>
      <div class="rc on"><div class="n">около %(write)d</div><div class="t">знаков нужно <b>писать от руки</b> — этого требования раньше не было</div></div>
      <div class="note">Цифры по знакам взяты из описаний: официального подтверждения я не нашла</div>
    </div>
  </div>

  <div class="foot"><b>что это значит</b><span>список на сто пятьдесят слов закрывает половину уровня, а навык письма не закрывает вовсе</span></div>

  <div class="brand"><span class="bdot"></span><b>Kitai School</b><span>&middot; kitai-school.ru</span></div>
</div>
</body></html>""" % dict(fonts=FONTS, vars=VARS, dold=D_OLD, dnew=D_NEW,
                         wold=WORDS_OLD, wnew=WORDS_NEW, read=CHARS_READ, write=CHARS_WRITE)

assert "%%" not in hero, "в разметке остались двойные проценты"
open(S + "hsk1-hero.html", "w", encoding="utf-8").write(hero)

# ─────────── инфографика: пять требований со статусами ───────────
rows = ""
for name, was, now, st in REQS:
    ok = st == CONF
    rows += ("""<div class="rw%(cls)s">
  <div class="st">%(st)s</div>
  <div class="key">%(key)s</div>
  <div class="was">%(was)s</div>
  <div class="arr">&rarr;</div>
  <div class="now">%(now)s</div>
</div>""" % dict(cls="" if ok else " soft", key=name, was=was, now=now, st=st))
assert rows.count('class="rw"') == len(CONFIRMED) == 1
assert rows.count('class="rw soft"') == len(UNCONFIRMED) == 4

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
.hint0{flex:0 0 352px;background:var(--surface);border:1px solid var(--hair);border-left:4px solid var(--brick);border-radius:13px;padding:11px 17px;font-size:14px;color:var(--ink-2);line-height:1.35}
.hint0 b{color:var(--ink)}

.rows{flex:1 1 auto;min-height:0;display:flex;flex-direction:column;gap:10px}
.rw{flex:1 1 0;background:var(--surface);border:1px solid var(--brick);border-radius:13px;padding:10px 18px;display:flex;align-items:center;gap:14px}
.rw.soft{border-color:var(--hair);border-style:dashed}
.rw .st{flex:0 0 136px;font-size:11.5px;font-weight:700;letter-spacing:.07em;text-transform:uppercase;color:var(--brick)}
.rw.soft .st{color:var(--grey)}
.rw .key{flex:0 0 196px;font-size:16px;font-weight:600;color:var(--ink)}
.rw.soft .key{color:var(--ink-2)}
.rw .was{flex:1 1 0;font-size:14px;color:var(--taupe);line-height:1.3}
.rw .arr{flex:0 0 26px;text-align:center;color:var(--brick);font-size:19px}
.rw .now{flex:1 1 0;font-size:14.5px;color:var(--ink);line-height:1.3;background:var(--brick-soft);border-radius:9px;padding:8px 13px;font-weight:600}
.rw.soft .now{background:var(--grey-soft);color:var(--ink-2);font-weight:400}

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
      <div class="eyebrow">Пять требований</div>
      <h2>Подтверждено одно, <i>остальное — по описаниям</i></h2>
    </div>
    <div class="hint0">Слева у каждой строки стоит, откуда взято. <b>Сплошной рамкой — то, что я проверила; пунктиром — то, что нашла только в сторонних описаниях.</b></div>
  </div>

  <div class="rows">%(rows)s</div>

  <div class="foot">
    <div class="msg">Планировать подготовку стоит <b>по словарю</b>: это единственная цифра, в которой я уверена</div>
    <div class="brand"><span class="dot2"></span><b>Kitai School</b><span>&middot; kitai-school.ru</span></div>
  </div>
</div>
</body></html>""" % dict(fonts=FONTS, vars=VARS, h=600, rows=rows)

assert "%%" not in info, "в разметке остались двойные проценты"
open(S + "hsk1-info.html", "w", encoding="utf-8").write(info)

print("ok | круги:", D_OLD, D_NEW, "| подтверждено:", len(CONFIRMED),
      "| по описаниям:", len(UNCONFIRMED), "| в неделю:", PER_WEEK)
