# -*- coding: utf-8 -*-
# Картинки к статье «Традиции китайцев»
# Обложка     — стена с рамками: три ряда поколений и знак поколения в каждом
# Инфографика — 4-2-1: состав семьи по трём периодам
import sys
sys.path.insert(0, "/home/user/Kitai-Shool/content")
from tradicii import GENS, FAMILY, ONE

S = ("/tmp/claude-0/-home-user-Kitai-Shool/a463bfca-82a9-56fd-ae09-42a7257ff999/"
     "scratchpad/")

FONTS = ("<link href=\"https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,600;0,700;1,600"
         "&family=Inter:wght@400;500;600;700&family=Noto+Serif+SC:wght@600;700&display=swap\" rel=\"stylesheet\">")
VARS = (":root{--brick:#A41E3A;--brick-d:#841630;--brick-soft:#F7E6EB;--ink:#2C2420;--ink-2:#5A4F45;"
        "--taupe:#8B7D6B;--cream:#FAF7F2;--cream-2:#F3EDE3;--hair:#EAE3D8;--surface:#fff;"
        "--paper:#FFFDF8;--good:#2F6F4F;--good-soft:#E8F3EC;--grey:#8A8178;--grey-soft:#EFEDE8}")

assert len(GENS) == 3, "рядов поколений три"
assert (ONE[2], ONE[3], ONE[4]) == (4, 2, 1), "схема 4-2-1"
assert [f[0] for f in FAMILY] == sorted(f[0] for f in FAMILY), "периоды по возрастанию"

# ─────────── обложка: стена с рамками ───────────
rows_html = ""
for lvl, who, han, py, mean in GENS:
    slots = "".join('<i><em></em><span class="zh">%s</span><em></em></i>' % han
                    for _ in range(3))
    rows_html += ('<div class="row"><div class="lbl"><b>%s</b><span>%s</span></div>'
                  '<div class="frames">%s</div>'
                  '<div class="mark"><span class="zh">%s</span><span class="py">%s</span>'
                  '<span class="mn">%s</span></div></div>' % (who, lvl, slots, han, py, mean))
assert rows_html.count('class="row"') == 3, "на обложке три ряда поколений"

hero = """<!DOCTYPE html><html lang="ru"><head><meta charset="utf-8">
%(fonts)s
<style>
%(vars)s
*{margin:0;box-sizing:border-box}html,body{width:1200px;height:630px}
.card{width:1200px;height:630px;background:radial-gradient(1040px 700px at 12%% 4%%, #fff 0%%, var(--cream) 54%%, var(--cream-2) 100%%);position:relative;overflow:hidden;font-family:'Inter',sans-serif;padding:30px 56px 52px 72px;display:flex;flex-direction:column}
.card:before{content:"";position:absolute;left:0;top:0;bottom:0;width:12px;background:var(--brick)}
.head{display:flex;justify-content:space-between;align-items:flex-end;gap:34px;margin-bottom:20px}
.eyebrow{color:var(--brick);font-weight:700;font-size:18px;letter-spacing:.19em;text-transform:uppercase;margin-bottom:9px}
h1{font-family:'Cormorant Garamond',serif;font-weight:600;font-size:37px;line-height:1.07;color:var(--ink);letter-spacing:-.3px;max-width:23ch}
h1 i{font-style:italic;color:var(--brick)}
.tip{flex:0 0 330px;background:var(--surface);border:1px solid var(--hair);border-left:4px solid var(--brick);border-radius:13px;padding:13px 18px;font-size:15px;color:var(--ink-2);line-height:1.38}
.tip b{color:var(--ink)}

.wall{display:flex;flex-direction:column;gap:17px}
.row{display:flex;align-items:center;gap:20px}
.lbl{flex:0 0 176px}
.lbl b{display:block;font-size:17px;color:var(--ink);line-height:1.2}
.lbl span{font-size:12.5px;color:var(--taupe)}
.frames{flex:1 1 auto;display:flex;gap:14px}
.frames i{flex:1 1 0;height:106px;background:var(--paper);border:3px solid #D9CEBE;border-radius:7px;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:5px;box-shadow:0 2px 0 rgba(44,36,32,.07)}
.frames i em{width:52px;height:7px;border-radius:4px;background:var(--cream-2);display:block}
.frames i .zh{font-family:'Noto Serif SC',serif;font-weight:700;font-size:32px;color:var(--brick-d);line-height:1}
.mark{flex:0 0 212px;background:var(--brick-soft);border:1px solid var(--brick);border-radius:12px;padding:9px 14px;display:flex;align-items:baseline;gap:9px}
.mark .zh{font-family:'Noto Serif SC',serif;font-weight:700;font-size:26px;color:var(--brick-d);line-height:1}
.mark .py{font-size:14px;font-weight:600;color:var(--ink)}
.mark .mn{font-size:13px;color:var(--ink-2)}

.foot{margin-top:15px;display:flex;align-items:center;gap:18px;background:var(--surface);border:1px solid var(--hair);border-radius:13px;padding:11px 22px}
.foot b{font-size:12.5px;font-weight:700;letter-spacing:.11em;text-transform:uppercase;color:var(--brick);flex:0 0 auto}
.foot span{font-size:15px;color:var(--ink);line-height:1.36}

.brand{position:absolute;left:72px;bottom:17px;display:flex;align-items:center;gap:11px;color:var(--ink)}
.brand b{font-family:'Cormorant Garamond',serif;font-weight:700;font-size:25px}
.brand .bdot{width:10px;height:10px;border-radius:50%%;background:var(--brick)}
.brand span{color:var(--taupe);font-size:16px}
</style></head><body>
<div class="card">
  <div class="head">
    <div>
      <div class="eyebrow">Культура</div>
      <h1>Традиции китайцев: <i>место в семье видно по имени</i></h1>
    </div>
    <div class="tip">У каждого поколения рода был <b>свой знак</b>: его ставили в имена всем детям этого поколения.</div>
  </div>

  <div class="wall">%(rows)s</div>

  <div class="foot"><b>важно</b><span>знаки здесь условные: это пример устройства, а не чья-то родословная — имён и фамилий мы не придумываем</span></div>

  <div class="brand"><span class="bdot"></span><b>Kitai School</b><span>&middot; kitai-school.ru</span></div>
</div>
</body></html>""" % dict(fonts=FONTS, vars=VARS, rows=rows_html)

open(S + "trad-hero.html", "w", encoding="utf-8").write(hero)

# ─────────── инфографика: 4-2-1 ───────────
def people(n, cls):
    return "".join('<u class="%s"></u>' % cls for _ in range(n))


YEAR_LABELS = {1979: "до 1979", 2016: "с 2016", 2021: "с 2021"}
assert set(YEAR_LABELS) == set(f[0] for f in FAMILY), \
    "подписи лет должны совпадать с годами из данных"

cols = ""
for year, cap, gp, par, kids, note in FAMILY:
    big = " on" if (gp, par, kids) == (ONE[2], ONE[3], ONE[4]) else ""
    cols += ("""<div class="col%(big)s">
  <div class="ch"><b>%(cap)s</b><span>%(year)s</span></div>
  <div class="tier"><span class="tl">старшие</span><div class="ppl">%(gp)s</div><em>%(gpn)d</em></div>
  <div class="tier"><span class="tl">родители</span><div class="ppl">%(par)s</div><em>%(parn)d</em></div>
  <div class="tier"><span class="tl">дети</span><div class="ppl">%(kid)s</div><em>%(kidn)d</em></div>
  <div class="cn">%(note)s</div>
</div>""" % dict(big=big, cap=cap, year=YEAR_LABELS[year], note=note,
                 gp=people(gp, "g"), par=people(par, "p"), kid=people(kids, "k"),
                 gpn=gp, parn=par, kidn=kids))
assert cols.count('class="col') == 3, "на инфографике три периода"
assert cols.count("<u ") == sum(f[2] + f[3] + f[4] for f in FAMILY), \
    "число человечков должно совпадать с данными"

info = """<!DOCTYPE html><html lang="ru"><head><meta charset="utf-8">
%(fonts)s
<style>
%(vars)s
*{margin:0;box-sizing:border-box}html,body{width:1200px;height:%(h)dpx}
.wrap{width:1200px;height:%(h)dpx;background:linear-gradient(180deg,#fff 0%%,var(--cream) 44%%,var(--cream-2) 100%%);font-family:'Inter',sans-serif;padding:34px 48px 24px;display:flex;flex-direction:column;position:relative;overflow:hidden}
.wrap:before{content:"";position:absolute;left:0;right:0;top:0;height:9px;background:var(--brick)}
.top{display:flex;align-items:flex-end;justify-content:space-between;gap:34px;margin-bottom:20px}
.eyebrow{color:var(--brick);font-weight:700;font-size:15.5px;letter-spacing:.19em;text-transform:uppercase;margin-bottom:8px}
h2{font-family:'Cormorant Garamond',serif;font-weight:600;font-size:36px;line-height:1.08;color:var(--ink);max-width:23ch}
h2 i{font-style:italic;color:var(--brick)}
.hint{flex:0 0 372px;background:var(--surface);border:1px solid var(--hair);border-left:4px solid var(--brick);border-radius:13px;padding:12px 18px;font-size:14.5px;color:var(--ink-2);line-height:1.36}
.hint b{color:var(--ink)}

.cols{display:flex;gap:18px;flex:1 1 auto}
.col{flex:1 1 0;background:var(--surface);border:1px solid var(--hair);border-radius:15px;padding:14px 18px 13px;display:flex;flex-direction:column}
.col.on{border-color:var(--brick);background:var(--brick-soft)}
.ch{display:flex;align-items:baseline;justify-content:space-between;gap:10px;margin-bottom:10px;padding-bottom:9px;border-bottom:1px solid var(--hair)}
.ch b{font-size:17px;color:var(--ink)}
.ch span{font-size:15px;font-weight:700;color:var(--brick);font-variant-numeric:tabular-nums}
.tier{display:flex;align-items:center;gap:12px;margin:17px 0}
.tier .tl{flex:0 0 82px;font-size:13.5px;color:var(--taupe)}
.ppl{flex:1 1 auto;display:flex;gap:9px;flex-wrap:wrap}
.ppl u{width:30px;height:30px;border-radius:50%%;display:block;text-decoration:none}
.ppl u.g{background:#C9BBA6}
.ppl u.p{background:var(--taupe)}
.ppl u.k{background:var(--brick)}
.tier em{flex:0 0 24px;text-align:right;font-style:normal;font-size:17px;font-weight:700;color:var(--ink);font-variant-numeric:tabular-nums}
.cn{margin-top:auto;padding-top:12px;border-top:1px solid var(--hair);font-size:14px;color:var(--ink-2);line-height:1.38}
.col.on .cn{color:var(--ink)}

.foot{margin-top:16px;display:flex;align-items:center;gap:18px}
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
      <div class="eyebrow">Состав семьи</div>
      <h2>Схема 4-2-1: <i>шестеро взрослых на одного ребёнка</i></h2>
    </div>
    <div class="hint">Ограничения рождаемости начались в 1979 году, второй ребёнок разрешён всем с 2016-го, третий — с 2021-го. <b>След остался в составе семьи.</b></div>
  </div>

  <div class="cols">%(cols)s</div>

  <div class="foot">
    <div class="msg">Единственный ребёнок вырастает — и по традиции отвечает <b>за двоих родителей и четверых стариков</b></div>
    <div class="brand"><span class="dot2"></span><b>Kitai School</b><span>&middot; kitai-school.ru</span></div>
  </div>
</div>
</body></html>""" % dict(fonts=FONTS, vars=VARS, h=560, cols=cols)

open(S + "trad-info.html", "w", encoding="utf-8").write(info)

print("ok | рядов поколений:", len(GENS), "| периодов:", len(FAMILY),
      "| схема:", "%d-%d-%d" % (ONE[2], ONE[3], ONE[4]))
