# -*- coding: utf-8 -*-
# Картинки к статье «Бесплатная подготовка к HSK»
# Обложка     — два списка рядом: что берётся бесплатно и чего бесплатно не выйдет
# Инфографика — растущая лестница «слов на одно задание» против ровной линии
#               «доля заданий, которые можно проверить самому»
import sys
sys.path.insert(0, "/home/user/Kitai-Shool/content")
from bespl import LEVELS, PER_MIN, PER_MAX, PER_TIMES

S = ("/tmp/claude-0/-home-user-Kitai-Shool/a463bfca-82a9-56fd-ae09-42a7257ff999/"
     "scratchpad/")

FONTS = ('<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,'
         'wght@0,600;0,700;1,600&family=Inter:wght@400;500;600;700&display=swap" '
         'rel="stylesheet">')
VARS = (":root{--brick:#A41E3A;--brick-d:#841630;--brick-soft:#F7E6EB;--ink:#2C2420;"
        "--ink-2:#5A4F45;--taupe:#8B7D6B;--cream:#FAF7F2;--cream-2:#F3EDE3;--hair:#EAE3D8;"
        "--surface:#fff;--grey-soft:#EFEDE8;--grey:#9A9289;--green:#4A6B4F}")

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

# ───────────────────── обложка: два списка ─────────────────────
FREE_SHORT = [
    "Описание уровня со списком слов",
    "Формат заданий и прогоны по времени",
    "Словарь и тексты своего уровня",
    "Собственный голос на записи",
]
PAID_SHORT = [
    "Взнос за регистрацию на экзамен",
    "Проверка письменной работы",
    "Постановка тонов и звуков",
]
assert len(FREE_SHORT) == 4 and len(PAID_SHORT) == 3

TICK = ('<svg viewBox="0 0 24 24" width="22" height="22" aria-hidden="true">'
        '<path d="M4 13l5 5L20 6" fill="none" stroke="currentColor" stroke-width="3" '
        'stroke-linecap="round" stroke-linejoin="round"/></svg>')
SLASH = ('<svg viewBox="0 0 24 24" width="22" height="22" aria-hidden="true">'
         '<path d="M6 19L19 5" fill="none" stroke="currentColor" stroke-width="3" '
         'stroke-linecap="round"/></svg>')


def col(kind, head, note, items, mark, foot):
    lis = "".join('<li><span class="ic">' + mark + "</span><span>" + t + "</span></li>"
                  for t in items)
    return ('<div class="col ' + kind + '"><div class="ch">' + head + '</div>'
            '<div class="cn">' + note + '</div><ul>' + lis + "</ul>"
            '<div class="cf">' + foot + "</div></div>")


HERO_CSS = BASE + """
html,body{width:1200px;height:630px}
.card{width:1200px;height:630px;padding:28px 48px 20px 64px}
h1{font-size:46px;max-width:23ch;margin-bottom:20px}
.cols{flex:1 1 auto;display:flex;align-items:stretch;gap:26px}
.col{flex:1 1 0;background:var(--surface);border:1px solid var(--hair);border-radius:16px;
 padding:18px 22px 16px}
.col.yes{border-top:5px solid var(--green)}
.col.no{border-top:5px solid var(--brick)}
.ch{font-size:22px;font-weight:700;color:var(--ink)}
.cn{font-size:13.5px;color:var(--taupe);margin:3px 0 12px}
.col ul{list-style:none;display:flex;flex-direction:column;gap:14px;flex:1 1 auto;justify-content:space-evenly}
.cf{margin-top:auto;padding-top:14px;border-top:1px solid var(--hair);font-size:14px;color:var(--taupe);line-height:1.35}
.col{display:flex;flex-direction:column}
.col li{display:flex;gap:12px;align-items:flex-start;font-size:18.5px;line-height:1.32;
 color:var(--ink-2)}
.ic{flex:0 0 22px;margin-top:1px}
.col.yes .ic{color:var(--green)}
.col.no .ic{color:var(--brick)}
"""

hero = ('<!DOCTYPE html><html lang="ru"><head><meta charset="utf-8">' + FONTS
        + "<style>" + VARS + HERO_CSS + "</style></head><body><div class=\"card\">"
        + '<div class="eyebrow">Бесплатная подготовка к HSK</div>'
        + '<h1>Бесплатен <i>материал</i>, а не обучение</h1>'
        + '<div class="cols">'
        + col("yes", "Берётся бесплатно", "одинаково на любом уровне, с первого по пятый",
              FREE_SHORT, TICK,
              "Это весь материал. План, порядок и дисциплину к нему придётся добавить "
              "самому — бесплатный материал всё равно требует порядка")
        + col("no", "Бесплатно не выйдет", "ни на одном уровне, сколько ни искать",
              PAID_SHORT, SLASH,
              "Здесь нужен человек: свою письменную работу и своё произношение "
              "оценить самому нельзя, а взнос за экзамен платят все")
        + '</div>'
        + '<div class="foot"><span class="lb">Граница</span>'
        + '<span class="vl">бесплатно закрывается то, что <b>можно проверить самому</b></span>'
        + '<span class="lb">Разбор</span>'
        + '<span class="vl">по уровням HSK 1–5</span></div>'
        + "</div></body></html>")

# ───────────────────── инфографика: лестница и ровная линия ─────────────────────
PER = [(l.n, l.per_task) for l in LEVELS]
SH = [(l.n, l.share) for l in LEVELS]
assert [p for n, p in PER] == [7.5, 8.3, 12.5, 20.0, 36.0]

BAR_MAX = 162.0          # высота столбика для самого большого значения
steps = ""
for n, v in PER:
    h = int(round(BAR_MAX * v / PER_MAX))
    steps += ('<div class="st"><div class="vl">' + str(v).replace(".", ",") + '</div>'
              '<div class="bar" style="height:' + str(h) + 'px"></div>'
              '<div class="lv">HSK ' + str(n) + "</div></div>")
assert steps.count('class="st"') == 5

# нижняя панель: та же пятёрка колонок, шкала от нуля до ста процентов
PH = 60.0
dots = ""
for i, (n, v) in enumerate(SH):
    y = int(round(PH * v / 100.0))
    dots += ('<div class="dt" style="left:' + str(10 + i * 20) + '%;height:'
             + str(y) + 'px"><span>'
             + str(v).replace(".0", "").replace(".", ",") + '&nbsp;%</span></div>')
assert dots.count('class="dt"') == 5

FIG_CSS = BASE + """
html,body{width:1200px;height:520px}
.card{width:1200px;height:520px;padding:22px 48px 14px 64px}
.head{display:flex;justify-content:space-between;align-items:flex-start;gap:34px;
 margin-bottom:10px}
h1{font-size:29px;max-width:25ch}
.tip{background:var(--surface);border:1px solid var(--hair);border-left:4px solid var(--brick);
 border-radius:13px;padding:10px 15px;font-size:13px;color:var(--ink-2);line-height:1.33;
 flex:0 0 300px}
.tip b{color:var(--ink)}
.stairs{display:flex;align-items:flex-end;gap:26px;height:214px;padding-left:4px}
.st{flex:1 1 0;display:flex;flex-direction:column;align-items:center;justify-content:flex-end}
.vl{font-size:20px;font-weight:700;color:var(--brick);margin-bottom:5px}
.bar{width:100%;max-width:138px;background:linear-gradient(180deg,#B8304B 0%,var(--brick) 100%);
 border-radius:10px 10px 0 0}
.lv{font-size:14px;font-weight:600;color:var(--ink-2);margin-top:7px;
 border-top:2px solid var(--hair);width:100%;max-width:138px;text-align:center;padding-top:5px}
.panel{margin-top:8px;background:var(--surface);border:1px solid var(--hair);
 border-radius:13px;padding:8px 18px 8px 20px;display:flex;align-items:flex-end;gap:18px;
 height:92px}
.pl{flex:0 0 300px;font-size:12.5px;color:var(--ink-2);line-height:1.3;padding-bottom:2px}
.pl b{color:var(--ink)}
.plot{flex:1 1 auto;position:relative;height:84px}
.dt{position:absolute;bottom:0;transform:translateX(-50%);width:34px;
 background:linear-gradient(180deg,#E8B9C6 0%,var(--brick-soft) 100%);
 border-radius:7px 7px 0 0;font-size:12.5px;font-weight:700;color:var(--brick-d)}
.dt span{position:absolute;bottom:100%;left:50%;transform:translateX(-50%);
 margin-bottom:5px;white-space:nowrap}
.base{position:absolute;left:0;right:0;bottom:0;height:2px;background:var(--hair)}
.zero{position:absolute;left:0;bottom:3px;font-size:11px;color:var(--taupe)}
"""

fig = ('<!DOCTYPE html><html lang="ru"><head><meta charset="utf-8">' + FONTS
       + "<style>" + VARS + FIG_CSS + "</style></head><body><div class=\"card\">"
       + '<div class="head"><div>'
       + '<div class="eyebrow">Пять уровней, один расчёт</div>'
       + '<h1>Формат бесплатному доступен весь, <i>а объём — нет</i></h1></div>'
       + '<div class="tip"><b>Ступень — сколько выученных слов приходится на одно '
         'задание экзамена.</b> Словник уровня поделён на число заданий</div></div>'
       + '<div class="stairs">' + steps + '</div>'
       + '<div class="panel"><div class="pl"><b>А доля заданий, которые можно проверить '
         'самому, почти не меняется.</b> Шкала от нуля до ста процентов</div>'
       + '<div class="plot">' + dots
       + '<div class="zero">0 %</div><div class="base"></div></div></div>'
       + '<div class="foot"><span class="lb">Крайние значения</span>'
       + '<span class="vl"><b>' + str(PER_MIN).replace(".", ",") + '</b> и <b>'
       + str(int(PER_MAX)) + '</b> слов на задание — разница в '
       + str(PER_TIMES).replace(".", ",") + ' раза</span>'
       + '<span class="lb">Расчёт</span>'
       + '<span class="vl">по словнику действующего стандарта</span></div>'
       + "</div></body></html>")

open(S + "bsp-hero.html", "w", encoding="utf-8").write(hero)
open(S + "bsp-info.html", "w", encoding="utf-8").write(fig)
print("готово: bsp-hero.html, bsp-info.html")
