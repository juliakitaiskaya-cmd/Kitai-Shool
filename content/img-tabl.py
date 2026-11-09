# -*- coding: utf-8 -*-
# Картинки к статье «Таблица китайских ключей»
# Обложка     — обрез словаря с вырубками по числу черт
# Инфографика — карта из всех 214 клеток, разложенных по группам
import sys
sys.path.insert(0, "/home/user/Kitai-Shool/content")
from radicals import RADICALS, COUNTS

S = ("/tmp/claude-0/-home-user-Kitai-Shool/a463bfca-82a9-56fd-ae09-42a7257ff999/"
     "scratchpad/")

FONTS = ("<link href=\"https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,600;0,700;1,600"
         "&family=Inter:wght@400;500;600;700&family=Noto+Serif+SC:wght@600;700&display=swap\" rel=\"stylesheet\">")
VARS = (":root{--brick:#A41E3A;--brick-d:#841630;--brick-soft:#F7E6EB;--ink:#2C2420;--ink-2:#5A4F45;"
        "--taupe:#8B7D6B;--cream:#FAF7F2;--cream-2:#F3EDE3;--hair:#EAE3D8;--surface:#fff;"
        "--paper:#FFFDF8;--good:#2F6F4F;--good-soft:#E8F3EC;--grey:#8A8178;--grey-soft:#EFEDE8}")

TOTAL = len(RADICALS)
assert TOTAL == 214, "ключей должно быть 214"
assert sum(n for s, n in COUNTS) == 214, "сумма по группам должна давать 214"
BIGGEST = max(COUNTS, key=lambda x: x[1])
FIRST6 = sum(n for s_, n in COUNTS[:6])
assert FIRST6 == 149, "в первых шести группах 149 ключей"
assert BIGGEST == (4, 34), "самая большая группа — четыре черты"

# вкладки обреза: первые группы показываем по отдельности, остальные одной
TABS = [s for s, n in COUNTS][:8]
OPEN_TAB = 4                     # какая вкладка открыта
assert OPEN_TAB in TABS, "открытая вкладка должна быть среди показанных"
OPEN_ROWS = [r for r in RADICALS if r[2] == OPEN_TAB][:10]
assert len(OPEN_ROWS) == 10, "на открытой странице показываем десять строк"
assert all(r[2] == OPEN_TAB for r in OPEN_ROWS), "строки должны быть из открытой группы"

def plural(n):
    """Окончание слова «ключ» при числе n: 1 ключ, 2 ключа, 5 ключей."""
    if 11 <= n % 100 <= 14:
        return "ей"
    last = n % 10
    return "" if last == 1 else ("а" if 2 <= last <= 4 else "ей")


assert [plural(n) for n in (1, 2, 5, 11, 21, 28)] == ["", "а", "ей", "ей", "", "ей"], \
    "склонение «ключ» считается неверно"

# ─────────── обложка: обрез словаря с вырубками ───────────
tabs_html = ""
for s in TABS:
    cls = " on" if s == OPEN_TAB else ""
    tabs_html += '<div class="tab%s"><b>%d</b><span>черт%s</span></div>' % (
        cls, s, "а" if s == 1 else ("ы" if s < 5 else ""))

rows_html = ""
for num, ch, st, ru in OPEN_ROWS:
    rows_html += ('<div class="rw"><span class="no">%d</span>'
                  '<span class="zh">%s</span><span class="ru">%s</span></div>' % (num, ch, ru))

hero = """<!DOCTYPE html><html lang="ru"><head><meta charset="utf-8">
%(fonts)s
<style>
%(vars)s
*{margin:0;box-sizing:border-box}html,body{width:1200px;height:630px}
.card{width:1200px;height:630px;background:radial-gradient(1040px 700px at 10%% 6%%, #fff 0%%, var(--cream) 52%%, var(--cream-2) 100%%);position:relative;overflow:hidden;font-family:'Inter',sans-serif;padding:32px 56px 54px 72px;display:flex;flex-direction:column}
.card:before{content:"";position:absolute;left:0;top:0;bottom:0;width:12px;background:var(--brick)}
.head{display:flex;justify-content:space-between;align-items:flex-end;gap:34px;margin-bottom:22px}
.eyebrow{color:var(--brick);font-weight:700;font-size:18px;letter-spacing:.19em;text-transform:uppercase;margin-bottom:10px}
h1{font-family:'Cormorant Garamond',serif;font-weight:600;font-size:37px;line-height:1.07;color:var(--ink);letter-spacing:-.3px;max-width:24ch}
h1 i{font-style:italic;color:var(--brick)}
.tip{flex:0 0 336px;background:var(--surface);border:1px solid var(--hair);border-left:4px solid var(--brick);border-radius:13px;padding:13px 18px;font-size:15px;color:var(--ink-2);line-height:1.38}
.tip b{color:var(--ink)}

.book{display:flex;align-items:stretch;gap:0;height:330px}
.page{flex:1 1 auto;background:var(--paper);border:1px solid var(--hair);border-right:0;border-radius:14px 0 0 14px;padding:18px 26px 16px;position:relative;box-shadow:inset -16px 0 24px -22px rgba(44,36,32,.3)}
.page .ttl{font-size:12.5px;font-weight:700;letter-spacing:.12em;text-transform:uppercase;color:var(--taupe);margin-bottom:12px}
.page .ttl b{color:var(--brick)}
.rows{display:grid;grid-template-columns:1fr 1fr;gap:9px 26px}
.rw{display:flex;align-items:baseline;gap:12px;border-bottom:1px dotted var(--hair);padding-bottom:7px}
.rw .no{flex:0 0 34px;font-size:13px;color:var(--taupe);font-weight:600}
.rw .zh{font-family:'Noto Serif SC',serif;font-weight:700;font-size:28px;color:var(--ink);line-height:1}
.rw .ru{font-size:14.5px;color:var(--ink-2)}
.page .more{margin-top:14px;font-size:13px;color:var(--taupe)}

.edge{flex:0 0 118px;display:flex;flex-direction:column;gap:4px;padding:6px 0}
.tab{flex:1 1 0;background:var(--cream-2);border:1px solid var(--hair);border-left:3px solid var(--taupe);border-radius:0 9px 9px 0;display:flex;align-items:center;gap:7px;padding-left:12px;color:var(--taupe)}
.tab b{font-size:19px;line-height:1}
.tab span{font-size:11.5px}
.tab.on{background:var(--brick);border-color:var(--brick);border-left-color:var(--brick-d);color:#fff;padding-left:16px}
.tab.on b{font-size:23px}
.tab.on span{color:#F6D8DF}

.foot{margin-top:16px;display:flex;align-items:center;gap:18px;background:var(--brick-soft);border:1px solid var(--brick);border-radius:13px;padding:12px 22px}
.foot b{font-size:12.5px;font-weight:700;letter-spacing:.11em;text-transform:uppercase;color:var(--brick);flex:0 0 auto}
.foot span{font-size:15.5px;color:var(--ink);line-height:1.36}

.brand{position:absolute;left:72px;bottom:19px;display:flex;align-items:center;gap:11px;color:var(--ink)}
.brand b{font-family:'Cormorant Garamond',serif;font-weight:700;font-size:26px}
.brand .bdot{width:10px;height:10px;border-radius:50%%;background:var(--brick)}
.brand span{color:var(--taupe);font-size:16px}
</style></head><body>
<div class="card">
  <div class="head">
    <div>
      <div class="eyebrow">Иероглифика</div>
      <h1>Таблица китайских ключей: <i>все 214 знаков системы Канси</i></h1>
    </div>
    <div class="tip">Список устроен как <b>указатель в конце книги</b>: вкладки по числу черт, внутри — ключи с номерами.</div>
  </div>

  <div class="book">
    <div class="page">
      <div class="ttl">группа <b>%(open)d черты</b> — %(cnt)d ключей</div>
      <div class="rows">%(rows)s</div>
      <div class="more">…и ещё %(rest)d ключ%(suf)s в этой группе</div>
    </div>
    <div class="edge">%(tabs)s</div>
  </div>

  <div class="foot"><b>всего</b><span>%(total)d ключей в %(groups)d группах — от одной черты до двадцати трёх</span></div>

  <div class="brand"><span class="bdot"></span><b>Kitai School</b><span>&middot; kitai-school.ru</span></div>
</div>
</body></html>""" % dict(
    fonts=FONTS, vars=VARS, tabs=tabs_html, rows=rows_html, open=OPEN_TAB,
    cnt=dict(COUNTS)[OPEN_TAB], rest=dict(COUNTS)[OPEN_TAB] - len(OPEN_ROWS),
    suf=plural(dict(COUNTS)[OPEN_TAB] - len(OPEN_ROWS)),
    total=TOTAL, groups=len(COUNTS))

open(S + "tabl-hero.html", "w", encoding="utf-8").write(hero)

# ─────────── инфографика: карта из 214 клеток ───────────
blocks = ""
for strokes, n in COUNTS:
    cells = "".join('<i></i>' for _ in range(n))
    big = " big" if (strokes, n) == BIGGEST else ""
    blocks += ('<div class="gr%s"><div class="gh"><b>%d</b><span>%d</span></div>'
               '<div class="cells">%s</div></div>' % (big, strokes, n, cells))

info = """<!DOCTYPE html><html lang="ru"><head><meta charset="utf-8">
%(fonts)s
<style>
%(vars)s
*{margin:0;box-sizing:border-box}html,body{width:1200px;height:%(h)dpx}
.wrap{width:1200px;height:%(h)dpx;background:linear-gradient(180deg,#fff 0%%,var(--cream) 42%%,var(--cream-2) 100%%);font-family:'Inter',sans-serif;padding:38px 48px 26px;display:flex;flex-direction:column;position:relative;overflow:hidden}
.wrap:before{content:"";position:absolute;left:0;right:0;top:0;height:9px;background:var(--brick)}
.top{display:flex;align-items:flex-end;justify-content:space-between;gap:34px;margin-bottom:22px}
.eyebrow{color:var(--brick);font-weight:700;font-size:15.5px;letter-spacing:.19em;text-transform:uppercase;margin-bottom:8px}
h2{font-family:'Cormorant Garamond',serif;font-weight:600;font-size:38px;line-height:1.07;color:var(--ink);max-width:22ch}
h2 i{font-style:italic;color:var(--brick)}
.hint{flex:0 0 388px;background:var(--surface);border:1px solid var(--hair);border-left:4px solid var(--brick);border-radius:13px;padding:12px 18px;font-size:15px;color:var(--ink-2);line-height:1.36}
.hint b{color:var(--ink)}

.map{display:flex;flex-wrap:wrap;gap:10px;align-content:flex-start}
.gr{background:var(--surface);border:1px solid var(--hair);border-radius:11px;padding:9px 11px 10px}
.gr.big{border-color:var(--brick);background:var(--brick-soft)}
.gh{display:flex;align-items:baseline;gap:6px;margin-bottom:7px}
.gh b{font-size:16px;color:var(--ink);line-height:1}
.gr.big .gh b{color:var(--brick-d)}
.gh span{font-size:11.5px;color:var(--taupe)}
.cells{display:flex;flex-wrap:wrap;gap:3px;max-width:148px}
.cells i{display:block;width:11px;height:11px;border-radius:2px;background:#D9CEBE}
.gr.big .cells i{background:var(--brick)}

.foot{margin-top:auto;display:flex;align-items:center;gap:18px;padding-top:18px}
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
      <div class="eyebrow">Карта всех 214</div>
      <h2>Каждая клетка — ключ, <i>каждая рамка — группа</i></h2>
    </div>
    <div class="hint">Группы идут по числу черт: от одной до двадцати трёх. <b>Самая большая — четыре черты</b>, в ней %(bn)d ключей.</div>
  </div>

  <div class="map">%(blocks)s</div>

  <div class="foot">
    <div class="msg">В первые шесть групп попадает <b>%(f6)d ключей из %(total)d</b> — дальше ключи встречаются всё реже</div>
    <div class="brand"><span class="dot2"></span><b>Kitai School</b><span>&middot; kitai-school.ru</span></div>
  </div>
</div>
</body></html>""" % dict(fonts=FONTS, vars=VARS, h=520, blocks=blocks, bn=BIGGEST[1],
         f6=FIRST6, total=TOTAL)

open(S + "tabl-info.html", "w", encoding="utf-8").write(info)

print("ok | ключей:", TOTAL, "| групп:", len(COUNTS), "| вкладок:", len(TABS),
      "| открыта:", OPEN_TAB, "| самая большая:", BIGGEST)
