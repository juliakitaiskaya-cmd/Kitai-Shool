# -*- coding: utf-8 -*-
# Картинки к статье «Сколько классов учатся в Китае»
# Обложка     — три плитки ступеней 小学 / 初中 / 高中
# Инфографика — дорожка из двенадцати клеток-классов
S = ("/tmp/claude-0/-home-user-Kitai-Shool/a463bfca-82a9-56fd-ae09-42a7257ff999/"
     "scratchpad/")

FONTS = ("<link href=\"https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,600;0,700;1,600"
         "&family=Inter:wght@400;500;600;700&family=Noto+Serif+SC:wght@600;700&display=swap\" rel=\"stylesheet\">")
VARS = (":root{--brick:#A41E3A;--brick-d:#841630;--brick-soft:#F7E6EB;--ink:#2C2420;--ink-2:#5A4F45;"
        "--taupe:#8B7D6B;--cream:#FAF7F2;--cream-2:#F3EDE3;--hair:#EAE3D8;--surface:#fff;"
        "--paper:#FFFDF8;--good:#2F6F4F;--good-soft:#E8F3EC;--gold:#B5873A;--gold-soft:#F6EEDF}")

# ─────────── данные: три ступени ───────────
# (знак, чтение, русское имя, лет, возраст начала, обязательная ли)
STAGES = [
    ("小学", "xiǎoxué", "Начальная школа", 6, 6, True),
    ("初中", "chūzhōng", "Средняя школа", 3, 12, True),
    ("高中", "gāozhōng", "Старшая школа", 3, 15, False),
]
EXAMS = {9: ("中考", "zhōngkǎo", "экзамен в конце девятого класса: по нему решают, кто пойдёт в старшую школу"),
         12: ("高考", "gāokǎo", "выпускной экзамен, по нему поступают в вузы")}

# ── проверки данных
assert len(STAGES) == 3, "ступеней должно быть три"
TOTAL = sum(s[3] for s in STAGES)
assert TOTAL == 12, "классов должно быть двенадцать, вышло %d" % TOTAL
age = STAGES[0][4]
for zh, py, name, yrs, start, must in STAGES:
    assert start == age, "возраст начала %s не сходится с концом предыдущей ступени" % name
    age += yrs
END_AGE = age
assert END_AGE == 18, "школа должна заканчиваться к восемнадцати, вышло %d" % END_AGE
OBLIG = sum(s[3] for s in STAGES if s[5])
assert OBLIG == 9, "обязательных лет должно быть девять, вышло %d" % OBLIG
assert max(EXAMS) == TOTAL, "последний экзамен приходится на конец школы"
assert OBLIG in EXAMS, "развилка стоит после девятого класса"

# статистика Минобразования за 2024 год
STATS = [
    ("Начальных школ", "136 332", "около 105,84 млн учеников"),
    ("Средних 初中", "52 054", "около 53,86 млн"),
    ("Старшей ступени", "22 617", "около 41,52 млн"),
]
assert len(STATS) == 3, "строк статистики должно быть три"

# ─────────── обложка: три плитки ступеней ───────────
tiles = ""
for i, (zh, py, name, yrs, start, must) in enumerate(STAGES):
    tiles += ('<div class="tile%s"><div class="zh">%s</div><div class="py">%s</div>'
              '<div class="nm">%s</div><div class="yr">%d года</div>'
              '<div class="ag">с %d до %d лет</div>'
              '<div class="ob">%s</div></div>'
              % ("" if must else " free", zh, py, name,
                 yrs, start, start + yrs,
                 "обязательная" if must else "по выбору"))
    if i < len(STAGES) - 1:
        ex = EXAMS.get(sum(s[3] for s in STAGES[:i + 1]))
        tiles += ('<div class="gap">%s</div>'
                  % ('<span class="ex">%s</span>' % ex[0] if ex else "<span class=\"ar\">→</span>"))
tiles = tiles.replace("6 года", "6 лет")

hero = """<!DOCTYPE html><html lang="ru"><head><meta charset="utf-8">
%(fonts)s
<style>
%(vars)s
*{margin:0;box-sizing:border-box}html,body{width:1200px;height:630px}
.card{width:1200px;height:630px;background:radial-gradient(1020px 680px at 12%% 8%%, #fff 0%%, var(--cream) 50%%, var(--cream-2) 100%%);position:relative;overflow:hidden;font-family:'Inter',sans-serif;padding:50px 56px 0 72px;display:flex;flex-direction:column}
.card:before{content:"";position:absolute;left:0;top:0;bottom:0;width:12px;background:var(--brick)}
.head{display:flex;justify-content:space-between;align-items:flex-end;gap:30px}
.eyebrow{color:var(--brick);font-weight:700;font-size:18px;letter-spacing:.19em;text-transform:uppercase;margin-bottom:12px}
h1{font-family:'Cormorant Garamond',serif;font-weight:600;font-size:43px;line-height:1.07;color:var(--ink);letter-spacing:-.4px;max-width:17ch}
h1 i{font-style:italic;color:var(--brick)}
.tip{flex:0 0 400px;background:var(--surface);border:1px solid var(--hair);border-left:4px solid var(--brick);border-radius:13px;padding:13px 18px;font-size:15.5px;color:var(--ink-2);line-height:1.38}
.tip b{color:var(--ink)}

.row{display:flex;align-items:stretch;gap:0;margin-top:34px}
.tile{flex:1 1 0;background:var(--surface);border:1px solid var(--hair);border-top:5px solid var(--brick);border-radius:14px;padding:18px 18px 16px;text-align:center;box-shadow:0 10px 22px rgba(44,36,32,.1)}
.tile.free{border-top-color:var(--gold);background:var(--gold-soft)}
.zh{font-family:'Noto Serif SC',serif;font-weight:700;font-size:40px;color:var(--ink);line-height:1}
.py{font-size:13px;color:var(--taupe);margin-top:3px}
.nm{font-size:17px;font-weight:700;color:var(--ink);margin-top:10px}
.yr{font-family:'Cormorant Garamond',serif;font-weight:700;font-size:27px;color:var(--brick);margin-top:7px;line-height:1}
.tile.free .yr{color:var(--gold)}
.ag{font-size:14px;color:var(--ink-2);margin-top:5px}
.ob{font-size:12.5px;color:var(--taupe);margin-top:9px;letter-spacing:.04em;text-transform:uppercase;font-weight:700}
.gap{flex:0 0 96px;display:flex;align-items:center;justify-content:center}
.ar{font-size:30px;color:var(--taupe);font-weight:300;line-height:1}
.ex{display:inline-block;background:var(--brick);color:#fff;font-family:'Noto Serif SC',serif;font-weight:700;font-size:19px;padding:7px 11px;border-radius:9px}
.under{margin-top:26px;display:flex;align-items:center;gap:16px}
.under .msg{flex:1 1 auto;font-size:16.5px;color:var(--ink-2);line-height:1.4}
.under .msg b{color:var(--ink)}
.brand{display:flex;align-items:center;gap:11px;color:var(--ink);flex:0 0 auto}
.brand b{font-family:'Cormorant Garamond',serif;font-weight:700;font-size:26px}
.brand .bdot{width:10px;height:10px;border-radius:50%%;background:var(--brick)}
.brand span{color:var(--taupe);font-size:16px}
</style></head><body>
<div class="card">
  <div class="head">
    <div>
      <div class="eyebrow">Школа в Китае</div>
      <h1>Сколько классов учатся в Китае: <i>двенадцать и три ступени</i></h1>
    </div>
    <div class="tip"><b>Первые девять лет обязательные</b>, старшая школа в эту часть уже не входит — и поэтому экзамен после девятого класса решает так много.</div>
  </div>

  <div class="row">%(tiles)s</div>

  <div class="under">
    <div class="msg">Между ступенями стоят экзамены: <b>中考</b> после девятого класса и <b>高考</b> в конце школы</div>
    <div class="brand"><span class="bdot"></span><b>Kitai School</b><span>&middot; kitai-school.ru</span></div>
  </div>
</div>
</body></html>""" % dict(fonts=FONTS, vars=VARS, tiles=tiles)

open(S + "kl-hero.html", "w", encoding="utf-8").write(hero)

# ─────────── инфографика: дорожка из клеток ───────────
cells = ""
n = 0
for zh, py, name, yrs, start, must in STAGES:
    inner = ""
    for k in range(yrs):
        n += 1
        inner += ('<div class="cl%s"><span class="no">%d</span><span class="ag">%d</span></div>'
                  % ("" if must else " free", n, start + k))
    cells += ('<div class="grp%s"><div class="cells">%s</div>'
              '<div class="lbl"><b class="zh">%s</b><span class="nm">%s</span>'
              '<span class="yy">%d года</span></div></div>'
              % ("" if must else " free", inner, zh, name, yrs))
    if n in EXAMS and n < TOTAL:
        ex = EXAMS[n]
        cells += ('<div class="exam"><span class="zh">%s</span><span class="py">%s</span>'
                  '<span class="cm">%s</span></div>' % ex)
cells = cells.replace("6 года", "6 лет")

stat_rows = "".join(
    '<div class="sr"><span class="k">%s</span><span class="v">%s</span><span class="c">%s</span></div>'
    % t for t in STATS)

info = """<!DOCTYPE html><html lang="ru"><head><meta charset="utf-8">
%(fonts)s
<style>
%(vars)s
*{margin:0;box-sizing:border-box}html,body{width:1200px;height:%(h)dpx}
.wrap{width:1200px;height:%(h)dpx;background:linear-gradient(180deg,#fff 0%%,var(--cream) 40%%,var(--cream-2) 100%%);font-family:'Inter',sans-serif;padding:38px 48px 30px;display:flex;flex-direction:column;position:relative;overflow:hidden}
.wrap:before{content:"";position:absolute;left:0;right:0;top:0;height:9px;background:var(--brick)}
.top{display:flex;align-items:flex-end;justify-content:space-between;gap:34px;margin-bottom:28px}
.eyebrow{color:var(--brick);font-weight:700;font-size:15.5px;letter-spacing:.19em;text-transform:uppercase;margin-bottom:8px}
h2{font-family:'Cormorant Garamond',serif;font-weight:600;font-size:38px;line-height:1.07;color:var(--ink);max-width:21ch}
h2 i{font-style:italic;color:var(--brick)}
.hint{flex:0 0 400px;background:var(--surface);border:1px solid var(--hair);border-left:4px solid var(--brick);border-radius:13px;padding:12px 18px;font-size:15px;color:var(--ink-2);line-height:1.36}
.hint b{color:var(--ink)}

.road{display:flex;align-items:flex-start;gap:14px}
.grp{display:flex;flex-direction:column}
.cells{display:flex;gap:7px}
.cl{width:58px;height:66px;border-radius:9px;background:var(--brick);display:flex;flex-direction:column;align-items:center;justify-content:center;gap:3px}
.cl.free{background:var(--gold)}
.cl .no{font-family:'Cormorant Garamond',serif;font-weight:700;font-size:25px;color:#fff;line-height:1}
.cl .ag{font-size:11px;color:rgba(255,255,255,.82)}
.lbl{margin-top:11px;text-align:center}
.lbl .zh{display:inline-block;font-family:'Noto Serif SC',serif;font-weight:700;font-size:21px;color:var(--ink)}
.lbl .nm{display:block;font-size:13.5px;font-weight:700;color:var(--ink);margin-top:2px}
.lbl .yy{display:block;font-size:12.5px;color:var(--taupe);margin-top:2px}

.exam{flex:0 0 138px;display:flex;flex-direction:column;align-items:center;padding-top:6px}
.exam .zh{font-family:'Noto Serif SC',serif;font-weight:700;font-size:21px;color:#fff;background:var(--ink);padding:6px 10px;border-radius:9px}
.exam .py{font-size:11.5px;color:var(--taupe);margin-top:5px}
.exam .cm{font-size:11.5px;color:var(--ink-2);margin-top:4px;text-align:center;line-height:1.26}

.legend{display:flex;gap:26px;margin-top:24px}
.lg{display:flex;align-items:center;gap:9px;font-size:14.5px;color:var(--ink-2)}
.lg i{width:22px;height:14px;border-radius:4px;display:block}
.lg.a i{background:var(--brick)}
.lg.b i{background:var(--gold)}

.stats{margin-top:22px;display:flex;gap:14px}
.sr{flex:1 1 0;background:var(--surface);border:1px solid var(--hair);border-radius:13px;padding:13px 16px}
.sr .k{display:block;font-size:12.5px;font-weight:700;letter-spacing:.1em;text-transform:uppercase;color:var(--taupe)}
.sr .v{display:block;font-family:'Cormorant Garamond',serif;font-weight:700;font-size:30px;color:var(--brick);line-height:1;margin-top:6px}
.sr .c{display:block;font-size:13px;color:var(--ink-2);margin-top:5px}

.foot{margin-top:auto;display:flex;align-items:center;gap:18px;padding-top:18px}
.foot .msg{flex:1 1 auto;background:var(--brick-soft);border:1px solid var(--brick);border-radius:14px;padding:11px 20px;font-size:14.5px;color:var(--ink);line-height:1.34}
.foot .msg b{color:var(--brick)}
.brand{display:flex;align-items:center;gap:10px;color:var(--ink);flex:0 0 auto}
.brand b{font-family:'Cormorant Garamond',serif;font-weight:700;font-size:23px}
.brand .dot2{width:9px;height:9px;border-radius:50%%;background:var(--brick)}
.brand span{color:var(--taupe);font-size:15px}
</style></head><body>
<div class="wrap">
  <div class="top">
    <div>
      <div class="eyebrow">Школа в Китае</div>
      <h2>Двенадцать классов — <i>и выбор после девятого</i></h2>
    </div>
    <div class="hint">В клетке — номер класса и возраст, в котором его обычно начинают. <b>После девятого класса обязательная школа заканчивается</b>: дальше идут либо в старшую школу, либо в профучилище.</div>
  </div>

  <div class="road">%(cells)s</div>

  <div class="legend">
    <span class="lg a"><i></i>обязательное образование 义务教育</span>
    <span class="lg b"><i></i>старшая школа — по выбору</span>
  </div>

  <div class="stats">%(stats)s</div>

  <div class="foot">
    <div class="msg">Числа школ и учащихся — <b>по таблицам Министерства образования КНР за 2024 год</b>; у статистического бюро по старшей ступени цифры другие</div>
    <div class="brand"><span class="dot2"></span><b>Kitai School</b><span>&middot; kitai-school.ru</span></div>
  </div>
</div>
</body></html>""" % dict(fonts=FONTS, vars=VARS, h=628, cells=cells, stats=stat_rows)

open(S + "kl-info.html", "w", encoding="utf-8").write(info)

print("ok | классов:", TOTAL, "| обязательных лет:", OBLIG, "| конец школы:", END_AGE)
print("ступени:", [(s[0], s[3], s[4]) for s in STAGES])
