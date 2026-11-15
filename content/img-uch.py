# -*- coding: utf-8 -*-
# Картинки к статье «Учебники HSK 3.0»
# Обложка     — две полки: корешки новой и прежней серии
# Инфографика — комплектность по девяти уровням
import sys
sys.path.insert(0, "/home/user/Kitai-Shool/content")
from uchebniki import SERIES, LEVELS, WORKBOOK_PARTS, PAIRED, BY_SKILL, NEW, OLD

S = ("/tmp/claude-0/-home-user-Kitai-Shool/a463bfca-82a9-56fd-ae09-42a7257ff999/"
     "scratchpad/")

FONTS = ("<link href=\"https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,600;0,700;1,600"
         "&family=Inter:wght@400;500;600;700&family=Noto+Serif+SC:wght@600;700&display=swap\" rel=\"stylesheet\">")
VARS = (":root{--brick:#A41E3A;--brick-d:#841630;--brick-soft:#F7E6EB;--ink:#2C2420;--ink-2:#5A4F45;"
        "--taupe:#8B7D6B;--cream:#FAF7F2;--cream-2:#F3EDE3;--hair:#EAE3D8;--surface:#fff;"
        "--grey-soft:#EFEDE8;--grey:#9A9289}")

assert len(SERIES) == 2 and len(LEVELS) == 9

# ─────────── обложка: две полки ───────────
SPINES = {NEW: 6, OLD: 5}  # сколько корешков рисуем на полке
shelves = ""
for name, cn, std, status, kit in SERIES:
    new = name == NEW
    spines = ""
    for i in range(SPINES[name]):
        spines += ('<i class="sp%s"><span>HSK %d</span></i>'
                   % (" on" if new else "", i + 1))
    shelves += ("""<div class="sh%(cls)s">
  <div class="books">%(spines)s</div>
  <div class="plank"></div>
  <div class="label">
    <b>%(name)s</b><span class="han">%(cn)s</span>
    <div class="std">%(std)s</div>
    <div class="kit">%(kit)s</div>
  </div>
</div>""" % dict(cls=" new" if new else "", spines=spines, name=name, cn=cn,
                 std=std, kit=kit))
assert shelves.count('class="sh') == 2
assert shelves.count('class="sp on"') == SPINES[NEW]

hero = """<!DOCTYPE html><html lang="ru"><head><meta charset="utf-8">
%(fonts)s
<style>
%(vars)s
*{margin:0;box-sizing:border-box}html,body{width:1200px;height:630px}
.card{width:1200px;height:630px;background:radial-gradient(1040px 700px at 10%% 4%%, #fff 0%%, var(--cream) 54%%, var(--cream-2) 100%%);position:relative;overflow:hidden;font-family:'Inter',sans-serif;padding:28px 56px 50px 72px;display:flex;flex-direction:column}
.card:before{content:"";position:absolute;left:0;top:0;bottom:0;width:12px;background:var(--brick)}
.head{display:flex;justify-content:space-between;align-items:flex-end;gap:34px;margin-bottom:20px}
.eyebrow{color:var(--brick);font-weight:700;font-size:18px;letter-spacing:.19em;text-transform:uppercase;margin-bottom:8px}
h1{font-family:'Cormorant Garamond',serif;font-weight:600;font-size:38px;line-height:1.07;color:var(--ink);letter-spacing:-.3px;max-width:26ch}
h1 i{font-style:italic;color:var(--brick)}
.tip{flex:0 0 318px;background:var(--surface);border:1px solid var(--hair);border-left:4px solid var(--brick);border-radius:13px;padding:12px 18px;font-size:14.5px;color:var(--ink-2);line-height:1.38}
.tip b{color:var(--ink)}

.shelves{flex:1 1 auto;display:flex;gap:22px}
.sh{flex:1 1 0;background:var(--surface);border:1px solid var(--hair);border-radius:15px;padding:18px 22px 16px;display:flex;flex-direction:column}
.sh.new{border-color:var(--brick)}
.books{flex:1 1 auto;display:flex;align-items:flex-end;gap:7px;min-height:160px}
.sp{flex:1 1 0;height:132px;border-radius:4px 4px 2px 2px;background:var(--grey-soft);border:1px solid var(--hair);display:flex;align-items:center;justify-content:center}
.sp span{font-size:13px;color:var(--taupe);font-weight:700;writing-mode:vertical-rl;transform:rotate(180deg);letter-spacing:.08em}
.sp.on{background:var(--brick-soft);border-color:var(--brick);height:152px}
.sp.on span{color:var(--brick-d)}
.plank{height:8px;border-radius:3px;background:var(--taupe);opacity:.45;margin-top:7px}
.label{margin-top:14px}
.label b{font-size:19px;color:var(--ink)}
.label .han{font-family:'Noto Serif SC',serif;font-weight:700;font-size:17px;color:var(--brick-d);margin-left:10px}
.label .std{margin-top:7px;display:inline-block;font-size:13px;font-weight:700;letter-spacing:.06em;text-transform:uppercase;color:#fff;background:var(--grey);border-radius:7px;padding:4px 11px}
.sh.new .label .std{background:var(--brick)}
.label .kit{margin-top:10px;font-size:14px;color:var(--ink-2);line-height:1.38}

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
      <div class="eyebrow">Подготовка</div>
      <h1>Учебники под новый стандарт: <i>серия одна, и это не «Стандартный курс»</i></h1>
    </div>
    <div class="tip">Названия похожи, стандарты разные. <b>Смотреть нужно на серию, а не на цифру в объявлении.</b></div>
  </div>

  <div class="shelves">%(shelves)s</div>

  <div class="foot"><b>при покупке</b><span>серии «Стандартный курс 3.0» не существует: так помечают перепутанный товар</span></div>

  <div class="brand"><span class="bdot"></span><b>Kitai School</b><span>&middot; kitai-school.ru</span></div>
</div>
</body></html>""" % dict(fonts=FONTS, vars=VARS, shelves=shelves)

assert "%%" not in hero, "в разметке остались двойные проценты"
open(S + "uch-hero.html", "w", encoding="utf-8").write(hero)

# ─────────── инфографика: комплектность по уровням ───────────
cols = ""
for lvl, kit in LEVELS:
    pair = "учебник" in kit
    items = "".join(
        '<div class="it%s">%s</div>' % (" book" if pair else " skill", t) for t in kit)
    cols += ("""<div class="cl%(cls)s">
  <div class="lv">%(lvl)d</div>
  <div class="items">%(items)s</div>
</div>""" % dict(cls=" pair" if pair else " skills", lvl=lvl, items=items))
assert cols.count('class="cl pair"') == len(PAIRED) == 6
assert cols.count('class="cl skills"') == len(BY_SKILL) == 3

wb_items = "".join('<span>%s</span>' % p for p in WORKBOOK_PARTS)

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
.hint0{flex:0 0 342px;background:var(--surface);border:1px solid var(--hair);border-left:4px solid var(--brick);border-radius:13px;padding:11px 17px;font-size:14px;color:var(--ink-2);line-height:1.35}
.hint0 b{color:var(--ink)}

.grid{flex:1 1 auto;min-height:0;display:flex;gap:10px}
.cl{flex:1 1 0;background:var(--surface);border:1px solid var(--hair);border-radius:13px;padding:12px 10px 11px;display:flex;flex-direction:column;align-items:center}
.cl.skills{border-color:var(--brick);background:var(--brick-soft)}
.lv{font-family:'Cormorant Garamond',serif;font-weight:700;font-size:34px;color:var(--ink);line-height:1;margin-bottom:11px}
.cl.skills .lv{color:var(--brick-d)}
.items{display:flex;flex-direction:column;gap:6px;width:100%%}
.it{border-radius:8px;padding:8px 6px;font-size:12.5px;text-align:center;line-height:1.25}
.it.book{background:var(--grey-soft);color:var(--ink-2);font-weight:600}
.it.skill{background:#fff;border:1px solid var(--brick);color:var(--brick-d);font-weight:600;padding:6px 4px;font-size:12px}

.wb{margin-top:16px;flex:0 0 auto;background:var(--surface);border:1px solid var(--hair);border-radius:14px;padding:12px 20px;display:flex;align-items:center;gap:14px}
.wb b{font-size:12.5px;font-weight:700;letter-spacing:.11em;text-transform:uppercase;color:var(--brick);flex:0 0 auto}
.wb span{background:var(--cream-2);border-radius:9px;padding:7px 13px;font-size:14px;color:var(--ink);margin-right:9px}

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
      <div class="eyebrow">Комплект по уровням</div>
      <h2>До шестого — две книги, <i>дальше четыре</i></h2>
    </div>
    <div class="hint0">На младших уровнях учебник идёт с тетрадью. <b>На старших единого учебника нет: тома собраны по навыкам.</b></div>
  </div>

  <div class="grid">%(cols)s</div>

  <div class="wb"><b>в тетради</b>%(wb)s</div>

  <div class="foot">
    <div class="msg">Выбирать том стоит <b>по доле слов, которые вы узнаёте</b>, а не по номеру уровня, который собираетесь сдавать</div>
    <div class="brand"><span class="dot2"></span><b>Kitai School</b><span>&middot; kitai-school.ru</span></div>
  </div>
</div>
</body></html>""" % dict(fonts=FONTS, vars=VARS, h=500, cols=cols, wb=wb_items)

assert "%%" not in info, "в разметке остались двойные проценты"
open(S + "uch-info.html", "w", encoding="utf-8").write(info)

print("ok | серий:", len(SERIES), "| уровней:", len(LEVELS),
      "| пара:", len(PAIRED), "| по навыкам:", len(BY_SKILL))
