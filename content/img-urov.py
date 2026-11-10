# -*- coding: utf-8 -*-
# Картинки к статье «Уровни знания китайского»
# Обложка     — две шкалы рядом: шесть нынешних уровней и девять новых
# Инфографика — три ступени: девять уровней по трём ступеням
import sys
sys.path.insert(0, "/home/user/Kitai-Shool/content")
from urovni import LEVELS, BANDS, EXAM79, OLD_MAX

S = ("/tmp/claude-0/-home-user-Kitai-Shool/a463bfca-82a9-56fd-ae09-42a7257ff999/"
     "scratchpad/")

FONTS = ("<link href=\"https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,600;0,700;1,600"
         "&family=Inter:wght@400;500;600;700&family=Noto+Serif+SC:wght@600;700&display=swap\" rel=\"stylesheet\">")
VARS = (":root{--brick:#A41E3A;--brick-d:#841630;--brick-soft:#F7E6EB;--ink:#2C2420;--ink-2:#5A4F45;"
        "--taupe:#8B7D6B;--cream:#FAF7F2;--cream-2:#F3EDE3;--hair:#EAE3D8;--surface:#fff;"
        "--paper:#FFFDF8;--good:#2F6F4F;--good-soft:#E8F3EC;--grey:#8A8178;--grey-soft:#EFEDE8}")

assert len(LEVELS) == 9 and len(BANDS) == 3
assert OLD_MAX == 6, "в нынешней шкале шесть уровней"

# ─────────── обложка: две шкалы ───────────
# слева столько же строк, сколько справа: верхние три пустые, чтобы уровни совпали по высоте
GAP = len(LEVELS) - OLD_MAX
old_col = ('<div class="cell none" style="flex:%d 1 0">'
           'в нынешней шкале таких уровней нет</div>' % GAP)
old_col += "".join('<div class="cell old">HSK %d</div>' % n
                   for n in range(OLD_MAX, 0, -1))
new_col = ""
for num, band, what, note in reversed(LEVELS):
    cls = " new" if num > OLD_MAX else " same"
    new_col += '<div class="cell%s">%d уровень</div>' % (cls, num)
assert new_col.count("class=") == 9, "справа девять строк"
assert old_col.count("cell old") == OLD_MAX, \
    "слева ровно столько строк, сколько уровней в нынешней шкале"
assert 'style="flex:%d 1 0"' % GAP in old_col, \
    "верхний блок слева занимает место трёх недостающих уровней"

SAME = sum(1 for num, *_ in LEVELS if num <= OLD_MAX)
assert SAME == OLD_MAX, "те же номера сохраняют шесть уровней"

hero = """<!DOCTYPE html><html lang="ru"><head><meta charset="utf-8">
%(fonts)s
<style>
%(vars)s
*{margin:0;box-sizing:border-box}html,body{width:1200px;height:630px}
.card{width:1200px;height:630px;background:radial-gradient(1040px 700px at 12%% 4%%, #fff 0%%, var(--cream) 54%%, var(--cream-2) 100%%);position:relative;overflow:hidden;font-family:'Inter',sans-serif;padding:28px 56px 50px 72px;display:flex;flex-direction:column}
.card:before{content:"";position:absolute;left:0;top:0;bottom:0;width:12px;background:var(--brick)}
.head{display:flex;justify-content:space-between;align-items:flex-end;gap:34px;margin-bottom:16px}
.eyebrow{color:var(--brick);font-weight:700;font-size:18px;letter-spacing:.19em;text-transform:uppercase;margin-bottom:8px}
h1{font-family:'Cormorant Garamond',serif;font-weight:600;font-size:36px;line-height:1.07;color:var(--ink);letter-spacing:-.3px;max-width:22ch}
h1 i{font-style:italic;color:var(--brick)}
.tip{flex:0 0 326px;background:var(--surface);border:1px solid var(--hair);border-left:4px solid var(--brick);border-radius:13px;padding:12px 18px;font-size:14.5px;color:var(--ink-2);line-height:1.38}
.tip b{color:var(--ink)}

.cols{flex:1 1 auto;display:flex;align-items:stretch;gap:0}
.col{flex:0 0 300px;display:flex;flex-direction:column;gap:5px}
.col .ch{font-size:12.5px;font-weight:700;letter-spacing:.13em;text-transform:uppercase;color:var(--taupe);margin-bottom:5px;text-align:center}
.col.right .ch{color:var(--brick)}
.cell{flex:1 1 0;background:var(--surface);border:1px solid var(--hair);border-radius:9px;display:flex;align-items:center;justify-content:center;font-size:16px;color:var(--ink);font-weight:600}
.cell.old,.cell.same{background:var(--grey-soft)}
.cell.none{background:transparent;border:2px dashed var(--hair);color:var(--taupe);font-size:14px;font-weight:500;text-align:center;padding:0 18px;line-height:1.35}
.cell.new{background:var(--brick-soft);border-color:var(--brick);color:var(--brick-d)}
.mid{flex:1 1 auto;display:flex;flex-direction:column;align-items:center;justify-content:center;padding:0 24px;gap:14px}
.arrow{font-size:46px;color:var(--brick);line-height:1}
.midnote{font-size:14px;color:var(--ink-2);text-align:center;line-height:1.4;max-width:300px}
.midlab{font-size:12.5px;font-weight:700;letter-spacing:.13em;text-transform:uppercase;color:var(--taupe)}

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
      <div class="eyebrow">Экзамены</div>
      <h1>Уровни знания китайского: <i>было шесть, стало девять</i></h1>
    </div>
    <div class="tip">Прежние уровни сохранили номера, а три новых достроили сверху. <b>Совпадение номеров не значит совпадения требований.</b></div>
  </div>

  <div class="cols">
    <div class="col left"><div class="ch">нынешняя шкала</div>%(old)s</div>
    <div class="mid"><div class="midlab">номера сохранены</div><div class="arrow">→</div><div class="midnote">слева и справа серым отмечены одни и те же шесть уровней; красным — три новых, которых в нынешней шкале нет</div></div>
    <div class="col right"><div class="ch">новый стандарт</div>%(new)s</div>
  </div>

  <div class="foot"><b>итого</b><span>девять уровней вместо шести, собранных в три ступени: начальную, среднюю и высшую</span></div>

  <div class="brand"><span class="bdot"></span><b>Kitai School</b><span>&middot; kitai-school.ru</span></div>
</div>
</body></html>""" % dict(fonts=FONTS, vars=VARS, old=old_col, new=new_col)

open(S + "urov-hero.html", "w", encoding="utf-8").write(hero)

# ─────────── инфографика: три ступени ───────────
by_num = {l[0]: l for l in LEVELS}
cards = ""
for name, nums, purpose in BANDS:
    top = name == "высшая"
    cells = ""
    for n in nums:
        num, band, what, note = by_num[n]
        cells += ('<div class="lv"><span class="n">%d</span><span class="w">%s</span></div>'
                  % (num, what))
    # у верхней ступени подпись вынесена в подвал картинки, чтобы карточка не переполнялась
    extra = "" if top else ('<div class="note">%s</div>' % purpose)
    cards += ('<div class="band%s"><div class="bh"><b>%s ступень</b>'
              '<span>уровни %d–%d</span></div>%s%s</div>'
              % (" top" if top else "", name, nums[0], nums[-1], cells, extra))
assert cards.count('class="band') == 3
assert cards.count('class="lv"') == 9

info = """<!DOCTYPE html><html lang="ru"><head><meta charset="utf-8">
%(fonts)s
<style>
%(vars)s
*{margin:0;box-sizing:border-box}html,body{width:1200px;height:%(h)dpx}
.wrap{width:1200px;height:%(h)dpx;background:linear-gradient(180deg,#fff 0%%,var(--cream) 44%%,var(--cream-2) 100%%);font-family:'Inter',sans-serif;padding:26px 48px 18px;display:flex;flex-direction:column;position:relative;overflow:hidden}
.wrap:before{content:"";position:absolute;left:0;right:0;top:0;height:9px;background:var(--brick)}
.top{display:flex;align-items:flex-end;justify-content:space-between;gap:34px;margin-bottom:14px}
.eyebrow{color:var(--brick);font-weight:700;font-size:15.5px;letter-spacing:.19em;text-transform:uppercase;margin-bottom:7px}
h2{font-family:'Cormorant Garamond',serif;font-weight:600;font-size:32px;line-height:1.08;color:var(--ink);max-width:24ch}
h2 i{font-style:italic;color:var(--brick)}
.hint{flex:0 0 350px;background:var(--surface);border:1px solid var(--hair);border-left:4px solid var(--brick);border-radius:13px;padding:11px 17px;font-size:14px;color:var(--ink-2);line-height:1.35}
.hint b{color:var(--ink)}

.bands{flex:1 1 auto;min-height:0;display:flex;gap:16px}
.band{flex:1 1 0;min-height:0;background:var(--surface);border:1px solid var(--hair);border-radius:15px;padding:12px 15px 16px;display:flex;flex-direction:column}
.band.top{border-color:var(--brick);background:var(--brick-soft)}
.bh{display:flex;align-items:baseline;justify-content:space-between;gap:10px;padding-bottom:8px;border-bottom:1px solid var(--hair);margin-bottom:9px}
.bh b{font-size:17px;color:var(--ink)}
.band.top .bh b{color:var(--brick-d)}
.bh span{font-size:13px;font-weight:700;color:var(--brick);font-variant-numeric:tabular-nums}
.lv{display:flex;align-items:flex-start;gap:10px;margin-bottom:8px}
.lv .n{flex:0 0 28px;height:28px;border-radius:9px;background:var(--cream-2);border:1px solid var(--hair);display:flex;align-items:center;justify-content:center;font-size:15px;font-weight:700;color:var(--ink)}
.band.top .lv .n{background:var(--brick);border-color:var(--brick);color:#fff}
.lv .w{font-size:13px;color:var(--ink-2);line-height:1.32;padding-top:5px}
.note{margin-top:auto;padding-top:9px;border-top:1px solid var(--hair);font-size:12.5px;color:var(--ink-2);line-height:1.32}
.band.top .note{color:var(--brick-d);font-weight:500}

.foot{margin-top:13px;flex:0 0 auto;display:flex;align-items:center;gap:18px}
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
      <div class="eyebrow">Новый стандарт</div>
      <h2>Три ступени <i>и девять уровней</i></h2>
    </div>
    <div class="hint">Нижние шесть уровней сохранили номера, верхняя ступень появилась впервые: <b>раньше потолком был HSK 6</b>.</div>
  </div>

  <div class="bands">%(cards)s</div>

  <div class="foot">
    <div class="msg">Экзамен верхней ступени — <b>один на три уровня: %(tasks)d заданий, около %(minutes)d минут, пять навыков вместе с переводом</b>. Первый прошёл %(first)s, словарь — %(vocab)s</div>
    <div class="brand"><span class="dot2"></span><b>Kitai School</b><span>&middot; kitai-school.ru</span></div>
  </div>
</div>
</body></html>""" % dict(fonts=FONTS, vars=VARS, h=560, cards=cards, tasks=EXAM79["задания"],
                         minutes=EXAM79["минуты"], first=EXAM79["первый экзамен"],
                         vocab=EXAM79["словарь"])

open(S + "urov-info.html", "w", encoding="utf-8").write(info)

print("ok | уровней:", len(LEVELS), "| ступеней:", len(BANDS),
      "| старая шкала:", OLD_MAX, "| экзамен:", EXAM79["задания"], "заданий")
