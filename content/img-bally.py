# -*- coding: utf-8 -*-
# Картинки к статье «Баллы HSKK»
# Обложка     — шкала от 0 до 100 с отметкой порога
# Инфографика — состав экзамена блоками по уровням
import sys
sys.path.insert(0, "/home/user/Kitai-Shool/content")
from bally import LEVELS, TOTALS, MAX_SCORE, PASS_SCORE, VALID_YEARS

S = ("/tmp/claude-0/-home-user-Kitai-Shool/a463bfca-82a9-56fd-ae09-42a7257ff999/"
     "scratchpad/")

FONTS = ("<link href=\"https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,600;0,700;1,600"
         "&family=Inter:wght@400;500;600;700&family=Noto+Serif+SC:wght@600;700&display=swap\" rel=\"stylesheet\">")
VARS = (":root{--brick:#A41E3A;--brick-d:#841630;--brick-soft:#F7E6EB;--ink:#2C2420;--ink-2:#5A4F45;"
        "--taupe:#8B7D6B;--cream:#FAF7F2;--cream-2:#F3EDE3;--hair:#EAE3D8;--surface:#fff;"
        "--grey-soft:#EFEDE8;--good:#2F6F4F}")

assert len(LEVELS) == 3
assert 0 < PASS_SCORE < MAX_SCORE
PCT = 100.0 * PASS_SCORE / MAX_SCORE

# ─────────── обложка: шкала с порогом ───────────
chips = "".join(
    '<div class="lv"><b>%s</b><span class="han">%s</span><i>%d заданий</i></div>'
    % (name, cn, TOTALS[name]) for name, cn, tasks, minutes, prep in LEVELS)
assert chips.count('class="lv"') == 3

ticks = ""
for v in range(0, MAX_SCORE + 1, 10):
    cls = " big" if v in (0, PASS_SCORE, MAX_SCORE) else ""
    ticks += '<span class="tk%s" style="left:%.4f%%"><i></i><b>%d</b></span>' % (
        cls, 100.0 * v / MAX_SCORE, v)

hero = """<!DOCTYPE html><html lang="ru"><head><meta charset="utf-8">
%(fonts)s
<style>
%(vars)s
*{margin:0;box-sizing:border-box}html,body{width:1200px;height:630px}
.card{width:1200px;height:630px;background:radial-gradient(1040px 700px at 10%% 4%%, #fff 0%%, var(--cream) 54%%, var(--cream-2) 100%%);position:relative;overflow:hidden;font-family:'Inter',sans-serif;padding:28px 56px 50px 72px;display:flex;flex-direction:column}
.card:before{content:"";position:absolute;left:0;top:0;bottom:0;width:12px;background:var(--brick)}
.head{display:flex;justify-content:space-between;align-items:flex-end;gap:34px;margin-bottom:26px}
.eyebrow{color:var(--brick);font-weight:700;font-size:18px;letter-spacing:.19em;text-transform:uppercase;margin-bottom:8px}
h1{font-family:'Cormorant Garamond',serif;font-weight:600;font-size:38px;line-height:1.07;color:var(--ink);letter-spacing:-.3px;max-width:24ch}
h1 i{font-style:italic;color:var(--brick)}
.tip{flex:0 0 322px;background:var(--surface);border:1px solid var(--hair);border-left:4px solid var(--brick);border-radius:13px;padding:12px 18px;font-size:14.5px;color:var(--ink-2);line-height:1.38}
.tip b{color:var(--ink)}

.scalebox{flex:1 1 auto;background:var(--surface);border:1px solid var(--hair);border-radius:16px;padding:34px 44px 24px;margin-bottom:16px;display:flex;flex-direction:column;justify-content:center}
.scale{position:relative;height:56px;margin:0 0 34px}
.bar{position:absolute;left:0;right:0;top:0;height:18px;border-radius:9px;background:var(--grey-soft);overflow:hidden}
.fill{position:absolute;left:0;top:0;bottom:0;width:%(pct).4f%%;background:var(--brick-soft);border-right:3px solid var(--brick)}
.tk{position:absolute;top:21px;transform:translateX(-50%%);text-align:center}
.tk i{display:block;width:1px;height:10px;background:var(--hair);margin:0 auto 2px}
.tk b{display:block;font-size:11.5px;color:var(--taupe);font-weight:500}
.tk.big i{width:2px;height:14px;background:var(--taupe)}
.tk.big b{font-size:14px;color:var(--ink);font-weight:700}
.pin{position:absolute;left:%(pct).4f%%;top:60px;transform:translateX(-50%%);text-align:center;white-space:nowrap}
.pin .lbl{display:inline-block;background:var(--brick);color:#fff;font-size:13.5px;font-weight:700;border-radius:8px;padding:5px 13px}
.pin .sub{display:block;font-size:13px;color:var(--ink-2);margin-top:5px}
.zones{display:flex;gap:16px;margin-top:46px}
.zone{flex:1 1 0;border-radius:11px;padding:9px 14px;font-size:14px;line-height:1.35}
.zone.no{background:var(--grey-soft);color:var(--ink-2)}
.zone.yes{background:var(--brick-soft);color:var(--brick-d);font-weight:600}

.lvs{display:flex;gap:14px}
.lv{flex:1 1 0;background:var(--surface);border:1px solid var(--hair);border-radius:13px;padding:10px 16px;display:flex;align-items:center;gap:12px}
.lv b{font-size:16.5px;color:var(--ink)}
.lv .han{font-family:'Noto Serif SC',serif;font-weight:700;font-size:19px;color:var(--brick-d)}
.lv i{margin-left:auto;font-style:normal;font-size:14px;color:var(--taupe)}
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
      <div class="eyebrow">Экзамены</div>
      <h1>Баллы HSKK: <i>порог один на все три уровня</i></h1>
    </div>
    <div class="tip">Считается общая сумма. <b>Отдельного порога по частям экзамена в описаниях нет.</b></div>
  </div>

  <div class="scalebox">
    <div class="scale">
      <div class="bar"><span class="fill"></span></div>
      %(ticks)s
      <div class="pin"><span class="lbl">%(pass)d — порог</span><span class="sub">одинаково на 初级, 中级 и 高级</span></div>
    </div>
    <div class="zones">
      <div class="zone no">ниже %(pass)d — экзамен не сдан, пересдавать целиком</div>
      <div class="zone yes">%(pass)d и выше — сдан; результат действует %(years)d года</div>
    </div>
  </div>

  <div class="lvs">%(chips)s</div>

  <div class="foot"><b>чего нет</b><span>разбивки «столько-то баллов за задание» в открытых описаниях экзамена не публикуют</span></div>

  <div class="brand"><span class="bdot"></span><b>Kitai School</b><span>&middot; kitai-school.ru</span></div>
</div>
</body></html>""" % dict(fonts=FONTS, vars=VARS, ticks=ticks, chips=chips,
                         pct=PCT, **{"pass": PASS_SCORE, "years": VALID_YEARS})

assert "%%" not in hero, "в разметке остались двойные проценты"
open(S + "bally-hero.html", "w", encoding="utf-8").write(hero)

# ─────────── инфографика: состав экзамена блоками ───────────
MAXN = max(TOTALS.values())
cols = ""
for name, cn, tasks, minutes, prep in LEVELS:
    bars = ""
    for title, n in tasks:
        cells = "".join('<i></i>' for _ in range(n))
        bars += ('<div class="task"><div class="tname"><span class="han">%s</span>'
                 '<b>%d</b></div><div class="cells">%s</div></div>'
                 % (title, n, cells))
    speak = minutes - prep
    cols += ("""<div class="col">
  <div class="chead"><b>%(name)s</b><span class="han">%(cn)s</span></div>
  <div class="tasks">%(bars)s</div>
  <div class="total"><span>всего заданий</span><b>%(total)d</b></div>
  <div class="time">
    <div class="tbar"><span class="prep" style="width:%(prepw).2f%%"></span></div>
    <div class="tleg"><span><i class="d1"></i>подготовка %(prep)d мин</span><span><i class="d2"></i>остальное %(speak)d мин</span></div>
    <div class="tall">%(minutes)d минут всего</div>
  </div>
</div>""" % dict(name=name, cn=cn, bars=bars, total=TOTALS[name], minutes=minutes,
                 prep=prep, speak=speak, prepw=100.0 * prep / minutes))
assert cols.count('class="col"') == 3
assert cols.count("<i></i>") == sum(TOTALS.values()) == 47

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
.hint0{flex:0 0 344px;background:var(--surface);border:1px solid var(--hair);border-left:4px solid var(--brick);border-radius:13px;padding:11px 17px;font-size:14px;color:var(--ink-2);line-height:1.35}
.hint0 b{color:var(--ink)}

.cols{flex:1 1 auto;min-height:0;display:flex;gap:16px}
.col{flex:1 1 0;background:var(--surface);border:1px solid var(--hair);border-radius:15px;padding:14px 18px 13px;display:flex;flex-direction:column}
.chead{display:flex;align-items:baseline;gap:10px;padding-bottom:10px;border-bottom:1px solid var(--hair)}
.chead b{font-size:18px;color:var(--ink)}
.chead .han{font-family:'Noto Serif SC',serif;font-weight:700;font-size:17px;color:var(--brick-d)}
.tasks{margin-top:12px;display:flex;flex-direction:column;gap:10px}
.task .tname{display:flex;align-items:baseline;gap:8px;margin-bottom:5px}
.task .tname .han{font-family:'Noto Serif SC',serif;font-weight:600;font-size:16px;color:var(--ink)}
.task .tname b{font-size:13px;color:var(--taupe);font-weight:600}
.cells{display:flex;flex-wrap:wrap;gap:4px}
.cells i{display:block;width:13px;height:13px;border-radius:3px;background:var(--brick);opacity:.82}
.total{margin-top:14px;padding-top:11px;border-top:1px dashed var(--hair);display:flex;align-items:baseline;justify-content:space-between}
.total span{font-size:12px;letter-spacing:.09em;text-transform:uppercase;color:var(--taupe)}
.total b{font-family:'Cormorant Garamond',serif;font-size:30px;color:var(--brick-d);line-height:1}
.time{margin-top:auto;padding-top:13px}
.tbar{height:11px;border-radius:6px;background:var(--brick);opacity:.82;overflow:hidden;position:relative}
.tbar .prep{position:absolute;left:0;top:0;bottom:0;background:var(--brick-soft)}
.tleg{display:flex;gap:14px;margin-top:7px;flex-wrap:wrap}
.tleg span{display:flex;align-items:center;gap:5px;font-size:12px;color:var(--ink-2)}
.tleg i{width:9px;height:9px;border-radius:2px;display:block}
.tleg .d1{background:var(--brick-soft);border:1px solid var(--hair)}
.tleg .d2{background:var(--brick);opacity:.82}
.tall{margin-top:6px;font-size:14.5px;font-weight:600;color:var(--ink)}

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
      <div class="eyebrow">Состав экзамена</div>
      <h2>Заданий меньше, <i>а минут больше</i></h2>
    </div>
    <div class="hint0">Один квадрат — одно задание. <b>От начального уровня к высшему их становится вчетверо меньше, зато каждое звучит дольше.</b></div>
  </div>

  <div class="cols">%(cols)s</div>

  <div class="foot">
    <div class="msg">Сколько баллов весит каждое задание — <b>в открытых описаниях не публикуется</b>, поэтому считать удобнее минуты говорения</div>
    <div class="brand"><span class="dot2"></span><b>Kitai School</b><span>&middot; kitai-school.ru</span></div>
  </div>
</div>
</body></html>""" % dict(fonts=FONTS, vars=VARS, h=600, cols=cols)

assert "%%" not in info, "в разметке остались двойные проценты"
open(S + "bally-info.html", "w", encoding="utf-8").write(info)

print("ok | уровней:", len(LEVELS), "| квадратов:", sum(TOTALS.values()), "| порог:", PASS_SCORE)
