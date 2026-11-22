# -*- coding: utf-8 -*-
# Картинки к статье «Регистрация на HSK»
# Обложка     — два календарных месяца: последний день записи и день экзамена
# Инфографика — точечная шкала: двадцать строк расписания по длине промежутка
import calendar
import sys
sys.path.insert(0, "/home/user/Kitai-Shool/content")
from zapis import DAYS, MIN_D, MAX_D, MEDIAN, MONTH_N, TOTAL_N, CHECKED

S = ("/tmp/claude-0/-home-user-Kitai-Shool/a463bfca-82a9-56fd-ae09-42a7257ff999/"
     "scratchpad/")

FONTS = ('<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,'
         'wght@0,600;0,700;1,600&family=Inter:wght@400;500;600;700&display=swap" '
         'rel="stylesheet">')
VARS = (":root{--brick:#A41E3A;--brick-d:#841630;--brick-soft:#F7E6EB;--ink:#2C2420;"
        "--ink-2:#5A4F45;--taupe:#8B7D6B;--cream:#FAF7F2;--cream-2:#F3EDE3;--hair:#EAE3D8;"
        "--surface:#fff;--grey-soft:#EFEDE8;--grey:#9A9289}")

BASE = """
*{margin:0;box-sizing:border-box}
.card{position:relative;overflow:hidden;font-family:'Inter',sans-serif;
 background:radial-gradient(1040px 700px at 6% 2%, #fff 0%, var(--cream) 56%, var(--cream-2) 100%);
 display:flex;flex-direction:column}
.card:before{content:"";position:absolute;left:0;top:0;bottom:0;width:12px;background:var(--brick)}
.eyebrow{color:var(--brick);font-weight:700;font-size:17px;letter-spacing:.19em;
 text-transform:uppercase;margin-bottom:7px}
h1{font-family:'Cormorant Garamond',serif;font-weight:600;line-height:1.06;
 color:var(--ink);letter-spacing:-.3px}
h1 i{font-style:italic;color:var(--brick)}
.tip{background:var(--surface);border:1px solid var(--hair);border-left:4px solid var(--brick);
 border-radius:13px;padding:12px 17px;font-size:14px;color:var(--ink-2);line-height:1.36}
.tip b{color:var(--ink)}
.foot{display:flex;align-items:center;gap:14px;margin-top:auto;border-top:1px solid var(--hair);
 padding-top:12px}
.foot .lb{font-size:12px;font-weight:700;letter-spacing:.11em;text-transform:uppercase;
 color:var(--taupe);flex:0 0 auto}
.foot .vl{font-size:14px;color:var(--ink-2)}
.foot .vl b{color:var(--ink)}
"""

# ───────────────────── обложка: два календарных месяца ─────────────────────
# Пример на осенней сессии: запись до 13 ноября, экзамен 13 декабря
YEAR = 2026
MONTHS = [(11, "Ноябрь", 13, "последний день записи"),
          (12, "Декабрь", 13, "экзамен")]
assert MONTHS[1][2] - MONTHS[0][2] == 0, "число одно и то же, месяц следующий"

WD = ["пн", "вт", "ср", "чт", "пт", "сб", "вс"]


def month_html(m, name, mark, caption):
    cal = calendar.Calendar(firstweekday=0).monthdayscalendar(YEAR, m)
    head = "".join('<div class="wd">' + w + "</div>" for w in WD)
    cells = ""
    for week in cal:
        for d in week:
            if d == 0:
                cells += '<div class="dz"></div>'
                continue
            cls = "d"
            if m == 11 and d > mark:
                cls += " after"
            if m == 12 and d < mark:
                cls += " after"
            if d == mark:
                cls += " mark"
            cells += '<div class="' + cls + '">' + str(d) + "</div>"
    return ('<div class="mon"><div class="mn">' + name + " " + str(YEAR) + '</div>'
            '<div class="grid">' + head + cells + '</div>'
            '<div class="cap"><b>' + str(mark) + " " + name.lower()[:-1] + 'я</b> — '
            + caption + '</div></div>')


months = "".join(month_html(*x) for x in MONTHS)
assert months.count('class="mon"') == 2 and months.count("mark") == 2

HERO_CSS = BASE + """
html,body{width:1200px;height:630px}
.card{width:1200px;height:630px;padding:26px 48px 20px 64px}
.head{display:flex;justify-content:space-between;align-items:flex-end;gap:30px;margin-bottom:14px}
h1{font-size:40px;max-width:21ch}
.tip{flex:0 0 330px}
.cals{flex:1 1 auto;display:flex;align-items:flex-start;gap:26px;padding-top:6px}
.mon{flex:0 0 352px}
.mn{font-size:17px;font-weight:700;color:var(--brick);margin-bottom:8px}
.grid{display:grid;grid-template-columns:repeat(7,46px);gap:4px}
.wd{font-size:11.5px;font-weight:700;letter-spacing:.06em;text-transform:uppercase;
 color:var(--taupe);text-align:center;padding-bottom:2px}
.d,.dz{height:40px;border-radius:9px;display:flex;align-items:center;justify-content:center;
 font-size:15px;color:var(--ink);background:var(--surface);border:1px solid var(--hair)}
.dz{background:transparent;border-color:transparent}
.d.after{background:var(--brick-soft);border-color:var(--brick-soft);color:var(--brick)}
.d.mark{background:var(--brick);border-color:var(--brick-d);color:#fff;font-weight:700}
.cap{font-size:14px;color:var(--ink-2);margin-top:10px;line-height:1.35}
.cap b{color:var(--ink)}
.gapbox{flex:1 1 0;text-align:center;padding-top:150px}
.gapbox .n{font-size:40px;font-weight:700;color:var(--brick);line-height:1}
.gapbox .t{font-size:15px;color:var(--ink-2);margin-top:6px;line-height:1.35}
"""

hero = ('<!DOCTYPE html><html lang="ru"><head><meta charset="utf-8">' + FONTS
        + "<style>" + VARS + HERO_CSS + "</style></head><body><div class=\"card\">"
        + '<div class="head"><div>'
        + '<div class="eyebrow">Два срока одного экзамена</div>'
        + '<h1>Запись закрывается <i>за месяц до экзамена</i></h1></div>'
        + '<div class="tip"><b>Залитые дни — это ожидание.</b> Записаться в них уже '
          'нельзя, а экзамен ещё не наступил</div></div>'
        + '<div class="cals">' + month_html(*MONTHS[0])
        + '<div class="gapbox"><div class="n">30</div>'
          '<div class="t">дней между последним днём записи и экзаменом</div></div>'
        + month_html(*MONTHS[1]) + '</div>'
        + '<div class="foot"><span class="lb">В середине расчёта</span>'
        + '<span class="vl"><b>' + str(MEDIAN) + '</b> день: у ' + str(MONTH_N)
        + ' строк из ' + str(TOTAL_N) + ' промежуток ровно месяц</span>'
        + '<span class="lb">Пример</span>'
        + '<span class="vl">из расписания, сверенного ' + CHECKED + '</span></div>'
        + "</div></body></html>")

# ───────────────────── инфографика: точечная шкала ─────────────────────
LO, HI = 20, 63
W = 1010


def x_of(d):
    return (d - LO) * W / float(HI - LO)


from collections import Counter
cnt = Counter(DAYS)
dots = ""
for d in sorted(cnt):
    for k in range(cnt[d]):
        dots += ('<div class="dot" style="left:' + str(int(round(x_of(d)))) + 'px;'
                 'bottom:' + str(52 + k * 26) + 'px"></div>')
assert dots.count('class="dot"') == TOTAL_N

ticks = ""
for d in (22, 31, 40, 50, 61):
    ticks += ('<div class="tk" style="left:' + str(int(round(x_of(d)))) + 'px">'
              '<div class="tl"></div><div class="tn">' + str(d) + '</div></div>')
assert ticks.count('class="tk"') == 5

FIG_CSS = BASE + """
html,body{width:1200px;height:500px}
.card{width:1200px;height:500px;padding:24px 48px 16px 64px}
.head{display:flex;justify-content:space-between;align-items:flex-end;gap:30px;margin-bottom:10px}
h1{font-size:34px;max-width:24ch}
.tip{flex:0 0 330px}
.plot{flex:1 1 auto;position:relative}
.axis{position:absolute;left:0;right:0;bottom:42px;height:3px;background:var(--hair)}
.dot{position:absolute;width:20px;height:20px;border-radius:50%;background:var(--brick);
 transform:translateX(-50%)}
.tk{position:absolute;bottom:4px;transform:translateX(-50%);text-align:center}
.tl{width:2px;height:10px;background:var(--grey);margin:0 auto}
.tn{font-size:14px;font-weight:700;color:var(--ink-2);margin-top:3px}
.band{position:absolute;bottom:42px;top:0;background:var(--brick-soft);opacity:.55;
 border-radius:10px}
.lab{position:absolute;font-size:14px;color:var(--ink-2);line-height:1.3}
"""

band_l = int(round(x_of(29.5)))
band_w = int(round(x_of(31.5) - x_of(29.5)))

fig = ('<!DOCTYPE html><html lang="ru"><head><meta charset="utf-8">' + FONTS
       + "<style>" + VARS + FIG_CSS + "</style></head><body><div class=\"card\">"
       + '<div class="head"><div>'
       + '<div class="eyebrow">Двадцать строк расписания</div>'
       + '<h1>Чаще всего месяц, <i>но бывает и втрое дольше</i></h1></div>'
       + '<div class="tip"><b>Точка — одна строка расписания.</b> По горизонтали — '
         'сколько дней между закрытием записи и экзаменом</div></div>'
       + '<div class="plot">'
       + '<div class="band" style="left:' + str(band_l) + 'px;width:'
       + str(max(band_w, 28)) + 'px"></div>'
       + '<div class="lab" style="left:' + str(band_l + 40) + 'px;bottom:196px">'
         '<b>30–31 день</b><br>одиннадцать строк из двадцати</div>'
       + '<div class="lab" style="left:6px;bottom:140px">самый короткий<br>случай</div>'
       + '<div class="lab" style="right:0;bottom:140px;text-align:right">два месяца<br>'
         'до экзамена</div>'
       + dots + '<div class="axis"></div>' + ticks + '</div>'
       + '<div class="foot"><span class="lb">Крайние значения</span>'
       + '<span class="vl"><b>' + str(MIN_D) + '</b> и <b>' + str(MAX_D)
       + '</b> дня — разница почти втрое</span>'
       + '<span class="lb">Расчёт</span>'
       + '<span class="vl">по расписанию, сверенному ' + CHECKED + '</span></div>'
       + "</div></body></html>")

open(S + "reg-hero.html", "w", encoding="utf-8").write(hero)
open(S + "reg-info.html", "w", encoding="utf-8").write(fig)
print("готово: reg-hero.html, reg-info.html")
