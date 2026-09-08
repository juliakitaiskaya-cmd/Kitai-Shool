# -*- coding: utf-8 -*-
import calendar
S = "/tmp/claude-0/-home-user-Kitai-Shool/a463bfca-82a9-56fd-ae09-42a7257ff999/scratchpad/"

FONTS = ("<link href=\"https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,600;0,700;1,600"
         "&family=Inter:wght@400;500;600;700&family=Noto+Serif+SC:wght@600;700&display=swap\" rel=\"stylesheet\">")
VARS = (":root{--brick:#A41E3A;--brick-d:#841630;--brick-soft:#F7E6EB;--ink:#2C2420;--ink-2:#5A4F45;"
        "--taupe:#8B7D6B;--cream:#FAF7F2;--cream-2:#F3EDE3;--hair:#EAE3D8;--surface:#fff;"
        "--green:#1E7A46;--green-soft:#E3F6E9;--amber:#C08A2E;--amber-s:#FBF2DF;--blue:#2F5D8C;--blue-s:#E7EEF6}")

# ---------------------------------------------------------------- обложка
def month(name, m, marks):
    wk = "".join('<div class="wd">%s</div>' % d for d in ["пн", "вт", "ср", "чт", "пт", "сб", "вс"])
    cells = []
    for week in calendar.monthcalendar(2026, m):
        for d in week:
            if d == 0:
                cells.append('<div class="dc empty"></div>')
            else:
                cls = marks.get(d, "")
                cells.append('<div class="dc %s">%d</div>' % (cls, d))
    return ('<div class="cal"><div class="mn">%s</div><div class="grid">%s%s</div></div>'
            % (name, wk, "".join(cells)))

hero = """<!DOCTYPE html><html lang="ru"><head><meta charset="utf-8">
%s
<style>
%s
*{margin:0;box-sizing:border-box}html,body{width:1200px;height:630px}
.card{width:1200px;height:630px;background:radial-gradient(1200px 700px at 84%% 12%%, #fff 0%%, var(--cream) 55%%, var(--cream-2) 100%%);display:flex;align-items:center;padding:0 52px 0 76px;position:relative;overflow:hidden;font-family:'Inter',sans-serif}
.card:before{content:"";position:absolute;left:0;top:0;bottom:0;width:12px;background:var(--brick)}
.seal{position:absolute;right:40px;top:26px;width:92px;height:92px;border:2.5px solid var(--brick);border-radius:14px;display:flex;align-items:center;justify-content:center;color:var(--brick);font-family:'Noto Serif SC',serif;font-weight:700;font-size:33px;opacity:.9}
.txt{flex:0 0 372px;max-width:372px}
.eyebrow{color:var(--brick);font-weight:700;font-size:19px;letter-spacing:.19em;text-transform:uppercase;margin-bottom:14px}
h1{font-family:'Cormorant Garamond',serif;font-weight:600;font-size:54px;line-height:1.03;color:var(--ink);letter-spacing:-.5px}
h1 i{font-style:italic;color:var(--brick)}
.sub{font-size:18.5px;color:var(--ink-2);line-height:1.42;max-width:21ch;margin-top:18px}
.brand{position:absolute;left:76px;bottom:34px;display:flex;align-items:center;gap:12px;color:var(--ink)}
.brand b{font-family:'Cormorant Garamond',serif;font-weight:700;font-size:28px}.brand .bdot{width:11px;height:11px;border-radius:50%%;background:var(--brick)}.brand span{color:var(--taupe);font-size:17px}

.art{flex:1 1 auto;display:flex;align-items:center;justify-content:center;padding-right:6px}
.cals{display:flex;gap:22px;align-items:stretch}
.col{display:flex;flex-direction:column;gap:12px;flex:0 0 auto}
.cal{background:var(--surface);border:1px solid var(--hair);border-radius:18px;padding:15px 18px 18px;box-shadow:0 8px 24px rgba(44,36,32,.09)}
.mn{font-family:'Cormorant Garamond',serif;font-weight:700;font-size:24px;color:var(--ink);text-align:center;margin-bottom:9px}
.grid{display:grid;grid-template-columns:repeat(7,40px);gap:5px}
.wd{font-size:11px;font-weight:700;letter-spacing:.06em;text-transform:uppercase;color:var(--taupe);text-align:center;padding-bottom:3px}
.dc{height:38px;display:flex;align-items:center;justify-content:center;font-size:15px;color:var(--ink-2);border-radius:10px}
.dc.empty{visibility:hidden}
.dc.amber{background:var(--amber);color:#fff;font-weight:700;box-shadow:0 0 0 3px var(--amber-s)}
.dc.brick{background:var(--brick);color:#fff;font-weight:700;box-shadow:0 0 0 3px var(--brick-soft)}
.key{display:flex;align-items:flex-start;gap:9px;background:var(--surface);border:1px solid var(--hair);border-radius:13px;padding:10px 15px;font-size:13.5px;color:var(--ink-2);line-height:1.3}
.key b{color:var(--ink);display:block;font-size:14px}
.sw{flex:0 0 14px;height:14px;border-radius:4px;margin-top:3px}
.sw.a{background:var(--amber)}.sw.b{background:var(--brick)}
</style></head><body>
<div class="card"><div class="seal">考试</div>
<div class="txt">
  <div class="eyebrow">Экзамены</div>
  <h1>Даты сдачи <i>HSK</i></h1>
  <div class="sub">Дата экзамена общая для всех. Срок записи — у каждого центра свой</div>
</div>
<div class="art">
  <div class="cals">
    <div class="col">%s<div class="key"><span class="sw a"></span><span><b>13 октября</b>где-то запись закрывается, где-то открывается</span></div></div>
    <div class="col">%s<div class="key"><span class="sw b"></span><span><b>13 декабря</b>экзамен сразу в семи городах</span></div></div>
  </div>
</div>
<div class="brand"><span class="bdot"></span><b>Kitai School</b><span>&middot; kitai-school.ru</span></div></div>
</body></html>""" % (FONTS, VARS,
                     month("Октябрь", 10, {13: "amber"}),
                     month("Декабрь", 12, {13: "brick"}))
open(S + "dsh-hero.html", "w", encoding="utf-8").write(hero)

# ---------------------------------------------------------------- инфографика
# окна записи на экзамен 13 декабря 2026, в днях до экзамена
ROWS = [
    ("Петербург", "СПбГУ",            88, 61, "16.09 – 13.10", "bad"),
    ("Владивосток", "ДВФУ",           68, 39, "06.10 – 04.11", ""),
    ("Благовещенск", "БГПУ",          61, 49, "13.10 – 25.10", ""),
    ("Петербург", "ПРОМТЕХДИЗАЙН",    61, 37, "13.10 – 06.11", ""),
    ("Москва", "МГЛУ",                61, 30, "13.10 – 13.11", ""),
    ("Москва", "«Хуамин»",            61, 30, "13.10 – 13.11", ""),
    ("Красноярск", "КГПУ",            61, 30, "13.10 – 13.11", ""),
    ("Сочи", "гимназия «Сириус»",     61, 30, "13.10 – 13.11", ""),
    ("Ростов-на-Дону", "ДГТУ",        61, 10, "13.10 – 03.12", "good"),
]
MAX = 90.0
def pct(d):           # d — дней до экзамена → доля слева направо
    return (MAX - d) / MAX * 100.0

bars = []
for city, c, o, cl, win, kind in ROWS:
    left, right = pct(o), pct(cl)
    bars.append(
        '<div class="row"><div class="lbl"><b>%s</b><span>%s</span></div>'
        '<div class="track"><div class="bar %s" style="left:%.2f%%;width:%.2f%%">'
        '<span class="days">%d</span></div></div>'
        '<div class="win">%s</div></div>' % (city, c, kind, left, right - left, cl, win))

ticks = "".join('<div class="tk%s" style="left:%.2f%%"><span>%s</span></div>'
                % (" last" if d == 0 else "", pct(d), "экзамен" if d == 0 else "−%d" % d)
                for d in (90, 75, 60, 45, 30, 15, 0))

info = """<!DOCTYPE html><html lang="ru"><head><meta charset="utf-8">
%s
<style>
%s
*{margin:0;box-sizing:border-box}html,body{width:1200px;height:HEIGHTpx}
.wrap{width:1200px;height:HEIGHTpx;background:var(--cream);position:relative;overflow:hidden;font-family:'Inter',sans-serif;padding:20px 58px 16px 72px}
.wrap:before{content:"";position:absolute;left:0;top:0;bottom:0;width:14px;background:var(--brick)}
.top{display:flex;align-items:flex-end;justify-content:space-between;gap:24px}
.eyebrow{color:var(--brick);font-weight:700;font-size:16px;letter-spacing:.2em;text-transform:uppercase;margin-bottom:5px}
h2{font-family:'Cormorant Garamond',serif;font-weight:700;font-size:39px;color:var(--ink);line-height:1.02;letter-spacing:-.5px}
h2 i{font-style:italic;color:var(--brick)}
.hint{flex:0 0 306px;font-size:13.5px;color:var(--ink-2);line-height:1.34;border-left:3px solid var(--brick);padding-left:14px}
.hint b{color:var(--brick)}

.chart{margin-top:16px;background:#fff;border:1px solid var(--hair);border-radius:18px;padding:14px 22px 10px;box-shadow:0 5px 16px rgba(44,36,32,.06)}
.head{display:flex;align-items:flex-end;font-size:11.5px;font-weight:700;letter-spacing:.1em;text-transform:uppercase;color:var(--taupe);padding-bottom:7px;border-bottom:1px solid var(--hair)}
.head .h1c{flex:0 0 196px}.head .h2c{flex:1 1 auto;text-align:center}.head .h3c{flex:0 0 118px;text-align:right}

.axis{position:relative;height:20px;flex:1 1 auto}
.tk{position:absolute;top:0;transform:translateX(-50%%);font-size:11px;color:var(--taupe);white-space:nowrap}
.tk.last{transform:translateX(-100%%);padding-right:7px;color:var(--brick);font-weight:700}
.tk span{display:block}

.row{display:flex;align-items:center;gap:0;padding:7px 0;border-bottom:1px solid #F4EFE7}
.row:last-child{border-bottom:none}
.lbl{flex:0 0 196px}
.lbl b{display:block;font-size:14.5px;color:var(--ink);line-height:1.1}
.lbl span{font-size:12.5px;color:var(--taupe)}
.track{flex:1 1 auto;position:relative;height:26px;background:linear-gradient(90deg,#FBF8F3,#F3EDE3);border-radius:8px}
.track:after{content:"";position:absolute;right:0;top:-4px;bottom:-4px;width:2px;background:var(--brick)}
.bar{position:absolute;top:3px;bottom:3px;background:var(--blue);border-radius:7px;display:flex;align-items:center;justify-content:flex-end;padding-right:8px}
.bar.bad{background:var(--brick)}
.bar.good{background:var(--green)}
.days{font-size:11.5px;font-weight:700;color:#fff;letter-spacing:.02em}
.win{flex:0 0 118px;text-align:right;font-size:13px;color:var(--ink-2);white-space:nowrap}

.foot{margin-top:14px;display:flex;align-items:center;gap:16px}
.foot .msg{flex:1 1 auto;background:var(--brick-soft);border:1px solid var(--brick);border-radius:14px;padding:11px 20px;font-size:15.5px;color:var(--ink);line-height:1.34}
.foot .msg b{color:var(--brick)}
.brand{display:flex;align-items:center;gap:10px;color:var(--ink);flex:0 0 auto}
.brand b{font-family:'Cormorant Garamond',serif;font-weight:700;font-size:23px}.brand .dot{width:9px;height:9px;border-radius:50%%;background:var(--brick)}.brand span{color:var(--taupe);font-size:15px}
</style></head><body>
<div class="wrap">
  <div class="top">
    <div>
      <div class="eyebrow">Один экзамен — 13 декабря</div>
      <h2>Девять центров — <i>девять окон записи</i></h2>
    </div>
    <div class="hint">Полоса — время, когда запись открыта. Цифра на конце — <b>за сколько дней до экзамена</b> она закроется.</div>
  </div>

  <div class="chart">
    <div class="head"><div class="h1c">Город и центр</div><div class="h2c"><div class="axis">%s</div></div><div class="h3c">Окно записи</div></div>
    %s
  </div>

  <div class="foot">
    <div class="msg">В Петербурге запись на этот экзамен закроется <b>13 октября</b> — ровно в тот день, когда в Москве она только откроется</div>
    <div class="brand"><span class="dot"></span><b>Kitai School</b><span>&middot; kitai-school.ru</span></div>
  </div>
</div>
</body></html>""" % (FONTS, VARS, ticks, "\n    ".join(bars))

info = info.replace("HEIGHT", "690")
open(S + "dsh-info.html", "w", encoding="utf-8").write(info)
print("ok")
