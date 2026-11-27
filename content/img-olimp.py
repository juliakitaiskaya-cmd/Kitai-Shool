# -*- coding: utf-8 -*-
# Картинки к статье «Олимпиада по китайскому: почему экзамен к ней не готовит»
# Обложка     — два табло «что известно заранее»
# Инфографика — неподвижный порог против плавающей границы призового места
import sys
sys.path.insert(0, "/home/user/Kitai-Shool/content")
from olimp import KNOWN, SHARE

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

# ───────────────────── обложка: два табло ─────────────────────
SHORT = ["Список материала", "Формат заданий", "Что считается успехом",
         "Свой результат"]
assert len(SHORT) == len(KNOWN) == 4


def mark(v):
    if v == "да":
        return '<span class="m yes">есть</span>'
    if v == "нет":
        return '<span class="m no">нет</span>'
    return '<span class="m part">отчасти</span>'


def board(title, col, strong):
    rows = "".join('<div class="r"><span class="rn">' + SHORT[i] + "</span>"
                   + mark(KNOWN[i][col]) + "</div>" for i in range(4))
    return ('<div class="bd' + (" alt" if strong else "") + '">'
            '<div class="bt">' + title + "</div>" + rows + "</div>")


boards = (board("Экзамен", 1, False) + board("Олимпиада", 2, True))
assert boards.count('class="bd') == 2
assert boards.count("yes") == 4 and boards.count('class="m no"') == 3

HERO_CSS = BASE + """
html,body{width:1200px;height:630px}
.card{width:1200px;height:630px;padding:26px 48px 18px 64px}
h1{font-size:39px;max-width:58ch;margin-bottom:5px}
.sub{font-size:15.5px;color:var(--ink-2);margin-bottom:22px;max-width:96ch;line-height:1.3}
.row{display:flex;gap:40px}
.bd{flex:1 1 0;background:var(--surface);border:1px solid var(--hair);
 border-radius:15px;padding:20px 24px 12px;box-shadow:0 2px 9px rgba(44,36,32,.05)}
.bd.alt{border-left:5px solid var(--brick)}
.bt{font-size:23px;font-weight:700;color:var(--ink);margin-bottom:18px;
 border-bottom:2px solid var(--hair);padding-bottom:13px}
.bd.alt .bt{color:var(--brick)}
.r{display:flex;align-items:center;justify-content:space-between;gap:16px;
 padding:16px 0;border-bottom:1px solid var(--hair)}
.r:last-child{border-bottom:0}
.rn{font-size:16.5px;color:var(--ink-2)}
.m{font-size:14px;font-weight:700;letter-spacing:.05em;padding:4px 13px;
 border-radius:20px;white-space:nowrap}
.m.yes{color:#fff;background:var(--brick)}
.m.no{color:var(--taupe);background:var(--grey-soft)}
.m.part{color:var(--ink);background:#E7D9C7}
.band{margin-top:auto;background:var(--surface);border:1px solid var(--hair);
 border-left:4px solid var(--brick);border-radius:13px;padding:13px 18px;
 font-size:16px;color:var(--ink-2);line-height:1.4}
.band b{color:var(--ink)}
"""

hero = ('<!DOCTYPE html><html lang="ru"><head><meta charset="utf-8">' + FONTS
        + "<style>" + VARS + HERO_CSS + "</style></head><body><div class=\"card\">"
        + '<div class="eyebrow">Что известно до начала</div>'
        + '<h1>К экзамену готовятся по списку — <i>а к олимпиаде списка нет</i></h1>'
        + '<div class="sub">Четыре вещи, которые участник знает заранее. '
          'У экзамена их знают все четыре, у олимпиады — почти ни одной</div>'
        + '<div class="row">' + boards + "</div>"
        + '<div class="band"><b>Поэтому подготовка разная.</b> Экзамен учит '
          'проходить список до конца, олимпиада — справляться с тем, чего '
          'в списке не было</div>'
        + '<div class="foot"><span class="lb">Источник</span>'
        + '<span class="vl">устройство двух форматов и наша практика '
          'занятий</span>'
        + '<span class="lb">Чего здесь нет</span>'
        + '<span class="vl">названий, городов и дат</span></div>'
        + "</div></body></html>")

# ───────── инфографика: неподвижный порог и плавающая граница ─────────
# ширины заданы в пикселях, поэтому и колонки фиксированные: иначе
# заливки считаются от одной ширины, а рисуются в другой
EXW = 452          # полоса экзамена
SEW = 300          # полоса сезона внутри правой колонки
x_th = int(round(EXW * SHARE / 100.0))
assert 0 < x_th < EXW

# четыре условных сезона: граница призового места каждый раз на новом месте
SEASONS = [("первый", 52), ("второй", 67), ("третий", 61), ("четвёртый", 74)]
assert len({p for _, p in SEASONS}) == len(SEASONS), "граница каждый раз другая"
assert all(10 < p < 95 for _, p in SEASONS)

rows = ""
for name, p in SEASONS:
    x = int(round(SEW * p / 100.0))
    rows += ('<div class="sr"><div class="sn">' + name + '</div>'
             '<div class="st"><div class="sb" style="width:' + str(x) + 'px">'
             '</div><div class="sm" style="left:' + str(x) + 'px"></div></div>'
             "</div>")
assert rows.count('class="sr"') == len(SEASONS)

FIG_CSS = BASE + """
html,body{width:1200px;height:520px}
.card{width:1200px;height:520px;padding:22px 48px 14px 64px}
.head{display:flex;justify-content:space-between;align-items:flex-start;gap:34px;
 margin-bottom:16px}
h1{font-size:30px;max-width:44ch}
.tip{background:var(--surface);border:1px solid var(--hair);border-left:4px solid var(--brick);
 border-radius:13px;padding:10px 15px;font-size:13px;color:var(--ink-2);line-height:1.33;
 flex:0 0 300px}
.tip b{color:var(--ink)}
.cols{flex:1 1 auto;display:flex;gap:52px;align-items:flex-start}
.half{flex:0 0 """ + str(EXW) + """px}
.ht{font-size:14px;font-weight:700;letter-spacing:.1em;text-transform:uppercase;
 color:var(--taupe);margin-bottom:18px;white-space:nowrap}
.half.alt .ht{color:var(--brick)}
.exam{position:relative;width:""" + str(EXW) + """px;height:104px;
 background:var(--grey-soft);border:1px solid var(--hair);border-radius:10px}
.exfill{position:absolute;left:0;top:0;bottom:0;border-radius:9px 0 0 9px;
 background:#D7C9BC}
.exline{position:absolute;top:-12px;bottom:-12px;width:4px;background:var(--ink);
 border-radius:2px}
.exval{position:absolute;top:38px;margin-left:14px;font-size:20px;
 font-weight:700;color:var(--ink);white-space:nowrap}
.excap{font-size:15.5px;color:var(--ink-2);margin-top:34px;line-height:1.45}
.sr{display:flex;align-items:center;gap:16px;margin-bottom:26px}
.sn{flex:0 0 108px;font-size:14.5px;color:var(--taupe);font-weight:600;
 text-align:right;white-space:nowrap}
.st{position:relative;width:""" + str(SEW) + """px;height:38px;
 background:var(--grey-soft);border:1px solid var(--hair);border-radius:7px}
.sb{position:absolute;left:0;top:0;bottom:0;border-radius:6px 0 0 6px;
 background:linear-gradient(90deg,#E3A7B6 0%,var(--brick) 100%)}
.sm{position:absolute;top:-6px;bottom:-6px;width:4px;background:var(--brick-d);
 border-radius:2px}
.olcap{font-size:15.5px;color:var(--ink-2);margin-top:18px;line-height:1.45;
 max-width:430px}
.olcap b{color:var(--ink)}
"""

fig = ('<!DOCTYPE html><html lang="ru"><head><meta charset="utf-8">' + FONTS
       + "<style>" + VARS + FIG_CSS + "</style></head><body><div class=\"card\">"
       + '<div class="head"><div>'
       + '<div class="eyebrow">Порог против места</div>'
       + '<h1>Одна черта стоит на месте, <i>другая каждый раз новая</i></h1></div>'
       + '<div class="tip"><b>Сезоны взяты как пример.</b> Настоящие границы '
         'мы не называем: они зависят от работ участников и объявляются '
         'после</div></div>'
       + '<div class="cols">'
       + '<div class="half"><div class="ht">Экзамен: порог</div>'
       + '<div class="exam"><div class="exfill" style="width:' + str(x_th)
       + 'px"></div><div class="exline" style="left:' + str(x_th) + 'px"></div>'
       + '<div class="exval" style="left:' + str(x_th) + 'px">'
       + str(SHARE) + '&nbsp;%</div></div>'
       + '<div class="excap">Черта известна заранее и не двигается. Набрали '
         'больше — сдали, независимо от того, как справились остальные. '
         'И так каждый год.</div>'
       + "</div>"
       + '<div class="half alt"><div class="ht">Олимпиада: призовая '
         'граница</div>' + rows
       + '<div class="olcap">Граница складывается из чужих работ, поэтому '
         '<b>одна и та же работа бывает призовой в один сезон и непризовой '
         'в другой</b>.</div>'
       + "</div></div>"
       + '<div class="foot"><span class="lb">Порог экзамена</span>'
       + '<span class="vl">по нашим разборам системы оценки</span>'
       + '<span class="lb">Границы сезонов</span>'
       + '<span class="vl">условный пример, не данные</span></div>'
       + "</div></body></html>")

open(S + "olm-hero.html", "w", encoding="utf-8").write(hero)
open(S + "olm-info.html", "w", encoding="utf-8").write(fig)
print("готово: olm-hero.html, olm-info.html")
