# -*- coding: utf-8 -*-
# Картинки к статье «CSCA: что сдавать и как готовиться»
# Обложка     — матрица «кому что сдавать»
# Инфографика — два блока экзамена рядом и плотность вопросов
import sys
sys.path.insert(0, "/home/user/Kitai-Shool/content")
from csca import SUBJECTS, TRACKS, SEC, SCORE_MAX, LANG, SCI

S = ("/tmp/claude-0/-home-user-Kitai-Shool/a463bfca-82a9-56fd-ae09-42a7257ff999/"
     "scratchpad/")

FONTS = ("<link href=\"https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,600;0,700;1,600"
         "&family=Inter:wght@400;500;600;700&family=Noto+Serif+SC:wght@600;700&display=swap\" rel=\"stylesheet\">")
VARS = (":root{--brick:#A41E3A;--brick-d:#841630;--brick-soft:#F7E6EB;--ink:#2C2420;--ink-2:#5A4F45;"
        "--taupe:#8B7D6B;--cream:#FAF7F2;--cream-2:#F3EDE3;--hair:#EAE3D8;--surface:#fff;"
        "--grey-soft:#EFEDE8}")

assert len(SUBJECTS) == 4 and len(TRACKS) == 3

# какие предметы входят в набор: по китайскому имени предмета
MARKS = {}
for tname, items in TRACKS:
    joined = " ".join(items)
    row = {}
    for name, cn, q, mins, lang, st in SUBJECTS:
        if cn in joined:
            row[cn] = "выбор" if "или" in joined and cn in ("物理", "化学") else "да"
        else:
            row[cn] = "нет"
    MARKS[tname] = row
assert MARKS[TRACKS[2][0]]["专业汉语"] == "нет", "в англоязычной программе языковой части нет"
assert all(MARKS[t[0]]["数学"] == "да" for t in TRACKS), "математика во всех наборах"

head_cells = "".join(
    '<div class="hc"><span class="han">%s</span><b>%s</b></div>' % (cn, name.split()[0])
    for name, cn, q, mins, lang, st in SUBJECTS)

rows = ""
for tname, items in TRACKS:
    cells = ""
    for name, cn, q, mins, lang, st in SUBJECTS:
        v = MARKS[tname][cn]
        if v == "да":
            cells += '<div class="cl yes"><span>●</span>сдаёте</div>'
        elif v == "выбор":
            cells += '<div class="cl may"><span>○</span>по специальности</div>'
        else:
            cells += '<div class="cl no"><span>—</span>не сдаёте</div>'
    rows += '<div class="row"><div class="rname">%s</div>%s</div>' % (tname, cells)
assert rows.count('class="row"') == 3
assert rows.count('class="cl ') == 12

hero = """<!DOCTYPE html><html lang="ru"><head><meta charset="utf-8">
%(fonts)s
<style>
%(vars)s
*{margin:0;box-sizing:border-box}html,body{width:1200px;height:630px}
.card{width:1200px;height:630px;background:radial-gradient(1040px 700px at 10%% 4%%, #fff 0%%, var(--cream) 54%%, var(--cream-2) 100%%);position:relative;overflow:hidden;font-family:'Inter',sans-serif;padding:28px 56px 50px 72px;display:flex;flex-direction:column}
.card:before{content:"";position:absolute;left:0;top:0;bottom:0;width:12px;background:var(--brick)}
.head{display:flex;justify-content:space-between;align-items:flex-end;gap:34px;margin-bottom:18px}
.eyebrow{color:var(--brick);font-weight:700;font-size:18px;letter-spacing:.19em;text-transform:uppercase;margin-bottom:8px}
h1{font-family:'Cormorant Garamond',serif;font-weight:600;font-size:38px;line-height:1.07;color:var(--ink);letter-spacing:-.3px;max-width:26ch}
h1 i{font-style:italic;color:var(--brick)}
.tip{flex:0 0 318px;background:var(--surface);border:1px solid var(--hair);border-left:4px solid var(--brick);border-radius:13px;padding:12px 18px;font-size:14.5px;color:var(--ink-2);line-height:1.38}
.tip b{color:var(--ink)}

.grid{flex:1 1 auto;background:var(--surface);border:1px solid var(--hair);border-radius:16px;padding:16px 20px 14px;display:flex;flex-direction:column}
.ghead{display:flex;gap:10px;padding-bottom:11px;border-bottom:1px solid var(--hair)}
.ghead .sp{flex:0 0 268px}
.hc{flex:1 1 0;text-align:center}
.hc .han{display:block;font-family:'Noto Serif SC',serif;font-weight:700;font-size:20px;color:var(--brick-d);line-height:1.1}
.hc b{display:block;font-size:12.5px;color:var(--taupe);font-weight:600;margin-top:3px}
.row{flex:1 1 0;display:flex;gap:10px;align-items:center;border-bottom:1px solid var(--cream-2)}
.row:last-child{border-bottom:none}
.rname{flex:0 0 268px;font-size:15.5px;font-weight:600;color:var(--ink);line-height:1.3;padding-right:12px}
.cl{flex:1 1 0;text-align:center;border-radius:10px;padding:9px 4px;font-size:12.5px;line-height:1.25}
.cl span{display:block;font-size:17px;margin-bottom:2px}
.cl.yes{background:var(--brick-soft);color:var(--brick-d);font-weight:700}
.cl.may{background:var(--cream-2);color:var(--ink-2);font-weight:600}
.cl.no{background:var(--grey-soft);color:var(--taupe)}

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
      <div class="eyebrow">Поступление</div>
      <h1>CSCA: <i>набор предметов определяет программа</i></h1>
    </div>
    <div class="tip">Не вы выбираете, что сдавать. <b>Сначала узнайте требования своей специальности.</b></div>
  </div>

  <div class="grid">
    <div class="ghead"><div class="sp"></div>%(head)s</div>
    %(rows)s
  </div>

  <div class="foot"><b>и отдельно</b><span>выпускники подготовительных факультетов при вузах программы стипендий экзамен не сдают вовсе</span></div>

  <div class="brand"><span class="bdot"></span><b>Kitai School</b><span>&middot; kitai-school.ru</span></div>
</div>
</body></html>""" % dict(fonts=FONTS, vars=VARS, head=head_cells, rows=rows)

assert "%%" not in hero, "в разметке остались двойные проценты"
open(S + "csca2-hero.html", "w", encoding="utf-8").write(hero)

# ─────────── инфографика: плотность ───────────
lname, lcn, lq, lmin, llang, lst = LANG
sname, scn, sq, smin, slang, sst = SCI[0]
MAXQ = max(lq, sq)


def block(cls, name, cn, q, mins, lang, sec, note):
    bars = "".join('<i></i>' for _ in range(q))
    return ("""<div class="bk %(cls)s">
  <div class="bhead"><span class="han">%(cn)s</span><b>%(name)s</b></div>
  <div class="nums"><div class="nm"><b>%(q)d</b><span>вопросов</span></div><div class="nm"><b>%(mins)d</b><span>минут</span></div></div>
  <div class="dots">%(bars)s</div>
  <div class="sec"><b>%(sec)d секунд</b><span>на один вопрос</span></div>
  <div class="note">%(note)s</div>
</div>""" % dict(cls=cls, cn=cn, name=name, q=q, mins=mins, bars=bars, sec=sec, note=note))


blocks = (block("lang", lname, lcn, lq, lmin, llang, SEC[lname],
                "только на китайском · два направления: гуманитарное и STEM")
          + block("sci", "каждый предмет", "数学 · 物理 · 化学", sq, smin, slang, SEC[sname],
                  "на китайском или на английском — по выбору"))
assert blocks.count('class="bk ') == 2
assert blocks.count("<i></i>") == lq + sq == 128

info = """<!DOCTYPE html><html lang="ru"><head><meta charset="utf-8">
%(fonts)s
<style>
%(vars)s
*{margin:0;box-sizing:border-box}html,body{width:1200px;height:%(h)dpx}
.wrap{width:1200px;height:%(h)dpx;background:linear-gradient(180deg,#fff 0%%,var(--cream) 46%%,var(--cream-2) 100%%);font-family:'Inter',sans-serif;padding:30px 48px 26px;display:flex;flex-direction:column;position:relative;overflow:hidden}
.wrap:before{content:"";position:absolute;left:0;right:0;top:0;height:9px;background:var(--brick)}
.top{display:flex;align-items:flex-end;justify-content:space-between;gap:34px;margin-bottom:20px}
.eyebrow{color:var(--brick);font-weight:700;font-size:15.5px;letter-spacing:.19em;text-transform:uppercase;margin-bottom:7px}
h2{font-family:'Cormorant Garamond',serif;font-weight:600;font-size:34px;line-height:1.08;color:var(--ink);max-width:23ch}
h2 i{font-style:italic;color:var(--brick)}
.hint0{flex:0 0 340px;background:var(--surface);border:1px solid var(--hair);border-left:4px solid var(--brick);border-radius:13px;padding:11px 17px;font-size:14px;color:var(--ink-2);line-height:1.35}
.hint0 b{color:var(--ink)}

.blocks{flex:1 1 auto;min-height:0;display:flex;gap:18px}
.bk{flex:1 1 0;background:var(--surface);border:1px solid var(--hair);border-radius:15px;padding:16px 22px 14px;display:flex;flex-direction:column}
.bk.lang{border-color:var(--brick)}
.bhead{display:flex;align-items:baseline;gap:11px;padding-bottom:11px;border-bottom:1px solid var(--hair)}
.bhead .han{font-family:'Noto Serif SC',serif;font-weight:700;font-size:21px;color:var(--brick-d)}
.bhead b{font-size:16.5px;color:var(--ink)}
.nums{display:flex;gap:28px;margin-top:13px}
.nm b{font-family:'Cormorant Garamond',serif;font-size:38px;color:var(--ink);line-height:1}
.nm span{display:block;font-size:12.5px;color:var(--taupe);margin-top:2px}
.dots{display:flex;flex-wrap:wrap;gap:4px;margin-top:14px}
.dots i{display:block;width:11px;height:11px;border-radius:3px;background:var(--brick);opacity:.8}
.bk.sci .dots i{opacity:.45}
.sec{margin-top:auto;padding-top:14px;display:flex;align-items:baseline;gap:9px}
.sec b{font-size:23px;color:var(--brick-d);font-weight:700}
.sec span{font-size:13.5px;color:var(--ink-2)}
.note{margin-top:10px;background:var(--cream-2);border-radius:9px;padding:8px 12px;font-size:13px;color:var(--ink-2);line-height:1.34}

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
      <div class="eyebrow">Формат</div>
      <h2>Языковая часть плотнее, <i>чем кажется</i></h2>
    </div>
    <div class="hint0">Один квадрат — один вопрос. <b>Секунды на вопрос посчитаны из числа вопросов и длительности.</b></div>
  </div>

  <div class="blocks">%(blocks)s</div>

  <div class="foot">
    <div class="msg">Шкала одинаковая — <b>%(score)d баллов за предмет</b>; задания везде с выбором ответа, сочинений нет</div>
    <div class="brand"><span class="dot2"></span><b>Kitai School</b><span>&middot; kitai-school.ru</span></div>
  </div>
</div>
</body></html>""" % dict(fonts=FONTS, vars=VARS, h=520, blocks=blocks, score=SCORE_MAX)

assert "%%" not in info, "в разметке остались двойные проценты"
open(S + "csca2-info.html", "w", encoding="utf-8").write(info)

print("ok | наборов:", len(TRACKS), "| вопросов:", lq, "против", sq,
      "| секунд:", SEC[lname], "против", SEC[sname])
