# -*- coding: utf-8 -*-
# Картинки к статье «Как сдать HSK»
# Обложка     — два ряда шагов: как делают обычно и как стоит
# Инфографика — лента из десяти шагов: ваши и календарные
import sys
sys.path.insert(0, "/home/user/Kitai-Shool/content")
from kaksdat import (STEPS, USUAL, YOU, CAL, BY_CAL, TOTAL, CAL_N, YOU_N,
                     DATE_STEP, DATE_USUAL, DATE_SHIFT, FIRST_CAL)

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
.foot{display:flex;align-items:center;gap:14px;margin-top:auto;border-top:1px solid var(--hair);
 padding-top:12px}
.foot .lb{font-size:12px;font-weight:700;letter-spacing:.11em;text-transform:uppercase;
 color:var(--taupe);flex:0 0 auto}
.foot .vl{font-size:14px;color:var(--ink-2)}
.foot .vl b{color:var(--ink)}
"""

SHORT = {
    1: "Понять, зачем",
    2: "Выбрать уровень",
    3: "Выбрать дату",
    4: "Измерить себя",
    5: "Посчитать срок",
    6: "Записаться",
    7: "Заниматься",
    8: "Прогнать формат",
    9: "Экзамен",
    10: "Результат",
}
assert set(SHORT) == {s[0] for s in STEPS}
WHO = {s[0]: s[2] for s in STEPS}

# ───────────────────── обложка: два ряда шагов ─────────────────────
def row(order, label, note, mark_date):
    cells = ""
    for pos, n in enumerate(order, start=1):
        cls = "c"
        if n == DATE_STEP:
            cls += " date"
        cells += ('<div class="' + cls + '"><span class="p">' + str(pos) + '</span>'
                  '<span class="t">' + SHORT[n] + "</span></div>")
    return ('<div class="band"><div class="bl"><b>' + label + '</b><span>' + note
            + "</span></div>" + '<div class="cells">' + cells + "</div></div>")


assert USUAL.index(DATE_STEP) + 1 == DATE_USUAL

HERO_CSS = BASE + """
html,body{width:1200px;height:630px}
.card{width:1200px;height:630px;padding:30px 48px 20px 64px}
h1{font-size:45px;max-width:28ch;margin-bottom:6px}
.sub{font-size:17px;color:var(--ink-2);margin-bottom:26px}
.bands{flex:1 1 auto;display:flex;flex-direction:column;justify-content:space-evenly;
 gap:30px;position:relative}
.band{display:flex;align-items:center;gap:20px}
.bl{flex:0 0 186px;font-size:14px;color:var(--taupe);line-height:1.3}
.bl b{display:block;font-size:19px;color:var(--ink);margin-bottom:3px}
.cells{flex:1 1 auto;display:flex;gap:7px}
.c{flex:1 1 0;background:var(--surface);border:1px solid var(--hair);border-radius:10px;
 padding:13px 5px 12px;text-align:center}
.c .p{display:block;font-size:12px;font-weight:700;color:var(--taupe)}
.c .t{display:block;font-size:12.5px;color:var(--ink-2);line-height:1.22;margin-top:4px}
.c.date{background:var(--brick);border-color:var(--brick-d)}
.c.date .p,.c.date .t{color:#fff}
.arrow{position:absolute;left:206px;right:0;top:50%;height:0}
.arrow .ln{position:absolute;height:2px;background:var(--brick);top:-1px;
 border-radius:2px}
.arrow .lb{position:absolute;top:-28px;font-size:13px;font-weight:700;color:var(--brick);
 background:var(--cream);padding:0 8px;white-space:nowrap}
"""

# стрелка от позиции DATE_USUAL (верхний ряд) к позиции DATE_STEP (нижний)
left_pct = (DATE_STEP - 0.5) * 100.0 / TOTAL
right_pct = (DATE_USUAL - 0.5) * 100.0 / TOTAL
arrow = ('<div class="arrow"><div class="ln" style="left:' + ("%.1f" % left_pct)
         + '%;width:' + ("%.1f" % (right_pct - left_pct)) + '%"></div>'
         + '<div class="lb" style="left:' + ("%.1f" % left_pct) + '%">на '
         + str(DATE_SHIFT) + " позиции раньше</div></div>")

hero = ('<!DOCTYPE html><html lang="ru"><head><meta charset="utf-8">' + FONTS
        + "<style>" + VARS + HERO_CSS + "</style></head><body><div class=\"card\">"
        + '<div class="eyebrow">Как сдать HSK</div>'
        + '<h1>Выбор даты — <i>не последний шаг, а третий</i></h1>'
        + '<div class="sub">Один и тот же маршрут, два порядка. Отмечен шаг '
          '«выбрать дату»</div>'
        + '<div class="bands">'
        + row(USUAL, "Как делают обычно", "дату смотрят, когда «уже готовы»", True)
        + row([s[0] for s in STEPS], "Как стоит",
              "дата задаёт срок, а не наоборот", True)
        + arrow + '</div>'
        + '<div class="foot"><span class="lb">Почему это важно</span>'
        + '<span class="vl">срок подготовки считается <b>до даты</b>, '
          'а не наоборот</span>'
        + '<span class="lb">Деление</span>'
        + '<span class="vl">наше, из практики занятий</span></div>'
        + "</div></body></html>")

# ───────────────────── инфографика: лента из десяти шагов ─────────────────────
tape = ""
for n, what, who, when, end in STEPS:
    cls = "tc cal" if who == CAL else "tc you"
    tape += ('<div class="' + cls + '"><div class="tn">' + str(n) + '</div>'
             '<div class="tt">' + SHORT[n] + '</div>'
             '<div class="tw">' + ("календарь" if who == CAL else "вы") + "</div></div>")
assert tape.count('class="tc cal"') == CAL_N
assert tape.count('class="tc you"') == YOU_N

FIG_CSS = BASE + """
html,body{width:1200px;height:520px}
.card{width:1200px;height:520px;padding:22px 48px 14px 64px}
.head{display:flex;justify-content:space-between;align-items:flex-start;gap:34px;
 margin-bottom:16px}
h1{font-size:30px;max-width:26ch}
.tip{background:var(--surface);border:1px solid var(--hair);border-left:4px solid var(--brick);
 border-radius:13px;padding:10px 15px;font-size:13px;color:var(--ink-2);line-height:1.33;
 flex:0 0 306px}
.tip b{color:var(--ink)}
.tape{flex:1 1 auto;display:flex;align-items:center;gap:8px}
.tc{flex:1 1 0;border-radius:12px;padding:26px 7px 24px;text-align:center;
 display:flex;flex-direction:column;align-items:center;justify-content:center}
.tc.you{background:var(--surface);border:1px solid var(--hair)}
.tc.cal{background:var(--brick);border:1px solid var(--brick-d)}
.tn{width:30px;height:30px;border-radius:50%;display:flex;align-items:center;
 justify-content:center;font-size:15px;font-weight:700}
.tc.you .tn{background:var(--grey-soft);color:var(--ink-2)}
.tc.cal .tn{background:#fff;color:var(--brick-d)}
.tt{font-size:13.5px;line-height:1.24;margin-top:11px;font-weight:600}
.tc.you .tt{color:var(--ink)}
.tc.cal .tt{color:#fff}
.tw{font-size:11px;letter-spacing:.06em;text-transform:uppercase;margin-top:14px;
 font-weight:700}
.tc.you .tw{color:var(--taupe)}
.tc.cal .tw{color:#F0C8D2}
"""

fig = ('<!DOCTYPE html><html lang="ru"><head><meta charset="utf-8">' + FONTS
       + "<style>" + VARS + FIG_CSS + "</style></head><body><div class=\"card\">"
       + '<div class="head"><div>'
       + '<div class="eyebrow">Десять шагов маршрута</div>'
       + '<h1>Четыре шага из десяти <i>зависят не от вас</i></h1></div>'
       + '<div class="tip"><b>Тёмные шаги назначает календарь центра.</b> Их нельзя '
         'передвинуть, отложить или ускорить — планировать нужно от них</div></div>'
       + '<div class="tape">' + tape + '</div>'
       + '<div class="foot"><span class="lb">Главное</span>'
       + '<span class="vl">первый календарный шаг — <b>' + str(FIRST_CAL)
       + '-й по счёту</b>: расписание вмешивается раньше, чем начинается '
         'подготовка</span>'
       + '<span class="lb">Деление</span>'
       + '<span class="vl">наше, из практики занятий</span></div>'
       + "</div></body></html>")

open(S + "ksd-hero.html", "w", encoding="utf-8").write(hero)
open(S + "ksd-info.html", "w", encoding="utf-8").write(fig)
print("готово: ksd-hero.html, ksd-info.html")
