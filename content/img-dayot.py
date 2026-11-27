# -*- coding: utf-8 -*-
# Картинки к статье «Что даёт знание китайского на HSK 4»
# Обложка     — две шкалы: по номеру ступени и по числу слов
# Инфографика — прибавка слов по ступеням и накопительная линия
import sys
sys.path.insert(0, "/home/user/Kitai-Shool/content")
from dayot import (CUR, CUR_STEPS, LEVELS, TARGET, BY_NUMBER, BY_WORDS, GAP,
                   LEFT, LEFT_TIMES)

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

# ───────────────────── обложка: две шкалы одна под другой ─────────────────────
BAR_W = 1000


def scale(label, pct, caption, strong):
    w = int(round(BAR_W * pct / 100.0))
    return ('<div class="sc' + (" alt" if strong else "") + '">'
            '<div class="sl">' + label + '</div>'
            '<div class="track"><div class="fill" style="width:' + str(w) + 'px">'
            '</div><div class="mark" style="left:' + str(w) + 'px"></div>'
            '<div class="val" style="left:' + str(w) + 'px">'
            + str(pct).replace(".", ",") + '&nbsp;%</div></div>'
            '<div class="sc-cap">' + caption + "</div></div>")


assert BY_NUMBER > BY_WORDS, "номер завышает пройденный путь"
scales = (scale("Как подсказывает номер ступени", BY_NUMBER,
                "четвёртая из шести — значит, две трети позади", False)
          + scale("Как на самом деле, по числу слов", BY_WORDS,
                  "две тысячи слов из пяти тысяч четырёхсот", True))
assert scales.count('class="sc') == 4   # два блока + две подписи sc-cap

HERO_CSS = BASE + """
html,body{width:1200px;height:630px}
.card{width:1200px;height:630px;padding:26px 48px 18px 64px}
h1{font-size:40px;max-width:58ch;margin-bottom:5px}
.sub{font-size:15.5px;color:var(--ink-2);margin-bottom:28px;max-width:96ch;line-height:1.3}
.sc{margin-bottom:62px}
.sl{font-size:14px;font-weight:700;letter-spacing:.1em;text-transform:uppercase;
 color:var(--taupe);margin-bottom:12px}
.sc.alt .sl{color:var(--brick)}
.track{position:relative;width:1000px;height:66px;background:var(--grey-soft);
 border:1px solid var(--hair);border-radius:9px}
.fill{height:100%;border-radius:8px 0 0 8px;background:#D7C9BC}
.sc.alt .fill{background:linear-gradient(90deg,#C9637A 0%,var(--brick) 100%)}
.mark{position:absolute;top:-9px;bottom:-9px;width:3px;background:var(--ink);
 border-radius:2px}
.sc.alt .mark{background:var(--brick-d)}
.val{position:absolute;top:17px;margin-left:14px;font-size:24px;
 font-weight:700;color:var(--ink);white-space:nowrap}
.sc.alt .val{color:var(--brick)}
.sc-cap{font-size:15.5px;color:var(--ink-2);margin-top:13px}
.gap{background:var(--surface);border:1px solid var(--hair);border-left:4px solid var(--brick);
 border-radius:13px;padding:13px 18px;font-size:16px;color:var(--ink-2);line-height:1.4;
 margin-top:auto}
.gap b{color:var(--ink)}
"""

hero = ('<!DOCTYPE html><html lang="ru"><head><meta charset="utf-8">' + FONTS
        + "<style>" + VARS + HERO_CSS + "</style></head><body><div class=\"card\">"
        + '<div class="eyebrow">Четвёртая ступень из шести</div>'
        + '<h1>Номер обещает две трети пути — <i>по словам это треть</i></h1>'
        + '<div class="sub">Две мерки одного и того же места на шкале: по счёту '
          'ступеней и по числу слов, которые к этому месту выучены</div>'
        + scales
        + '<div class="gap"><b>Разрыв — ' + str(GAP).replace(".", ",")
        + ' пункта.</b> Он работает против человека: кажется, что осталось '
          'меньше трети, а осталось больше половины</div>'
        + '<div class="foot"><span class="lb">Словник</span>'
        + '<span class="vl">по нашим разборам ступеней, действующий '
          'стандарт</span>'
        + '<span class="lb">Расчёт</span>'
        + '<span class="vl">наш</span></div>'
        + "</div></body></html>")

# ───────────── инфографика: прибавка по ступеням и накопление ─────────────
BMAX = 188.0
SMAX = max(CUR_STEPS)
NAMES = ["Первая", "Вторая", "Третья", "Четвёртая", "Пятая", "Шестая"]
assert len(NAMES) == LEVELS == len(CUR_STEPS)


def fmt(v):
    return "{:,}".format(v).replace(",", "&nbsp;")


bars = ""
for i in range(LEVELS):
    h = max(6, int(round(BMAX * CUR_STEPS[i] / float(SMAX))))
    hot = (i == TARGET - 1)
    bars += ('<div class="b' + (" hot" if hot else "") + '">'
             '<div class="bn">+' + fmt(CUR_STEPS[i]) + '</div>'
             '<div class="bar" style="height:' + str(h) + 'px"></div>'
             '<div class="bs">' + NAMES[i] + '</div>'
             '<div class="bc">' + fmt(CUR[i]) + "</div></div>")
assert bars.count('class="b"') + bars.count('class="b hot"') == LEVELS
assert bars.count("hot") == 1

FIG_CSS = BASE + """
html,body{width:1200px;height:520px}
.card{width:1200px;height:520px;padding:22px 48px 14px 64px}
.head{display:flex;justify-content:space-between;align-items:flex-start;gap:34px;
 margin-bottom:14px}
h1{font-size:31px;max-width:40ch}
.tip{background:var(--surface);border:1px solid var(--hair);border-left:4px solid var(--brick);
 border-radius:13px;padding:10px 15px;font-size:13px;color:var(--ink-2);line-height:1.33;
 flex:0 0 310px}
.tip b{color:var(--ink)}
.plot{flex:1 1 auto;display:flex;align-items:flex-end;gap:22px;padding-bottom:2px}
.b{flex:1 1 0;display:flex;flex-direction:column;align-items:center;text-align:center}
.bn{font-size:17px;font-weight:700;color:var(--ink-2);margin-bottom:7px}
.b.hot .bn{color:var(--brick);font-size:20px}
.bar{width:100%;max-width:112px;border-radius:8px 8px 0 0;
 background:linear-gradient(180deg,#C9637A 0%,var(--brick) 100%);opacity:.42}
.b.hot .bar{opacity:1}
.bs{font-size:15px;font-weight:700;color:var(--ink);margin-top:10px;
 border-top:2px solid var(--hair);width:100%;max-width:112px;padding-top:8px}
.b.hot .bs{color:var(--brick)}
.bc{font-size:14px;color:var(--taupe);margin-top:5px;font-weight:600}
.legend{display:flex;gap:30px;font-size:14px;color:var(--ink-2);margin-top:12px;
 line-height:1.35}
.legend b{color:var(--ink)}
"""

fig = ('<!DOCTYPE html><html lang="ru"><head><meta charset="utf-8">' + FONTS
       + "<style>" + VARS + FIG_CSS + "</style></head><body><div class=\"card\">"
       + '<div class="head"><div>'
       + '<div class="eyebrow">Ступени разной длины</div>'
       + '<h1>Шаги растут к верху шкалы, <i>а не идут ровно</i></h1></div>'
       + '<div class="tip"><b>Столбец — сколько слов прибавляет ступень.</b> '
         'Под названием — сколько набрано всего к этому месту</div></div>'
       + '<div class="plot">' + bars + "</div>"
       + '<div class="legend">'
         '<span><b>Четвёртая ступень</b> — две тысячи слов, это треть '
         'словаря</span>'
         '<span><b>До шестой</b> остаётся ещё ' + fmt(LEFT) + ', в '
       + str(LEFT_TIMES).replace(".", ",") + ' раза больше набранного</span>'
         '<span>Последний шаг один почти равен <b>всему началу пути</b></span>'
         '</div>'
       + '<div class="foot"><span class="lb">Словник</span>'
       + '<span class="vl">по нашим разборам ступеней, действующий стандарт</span>'
       + '<span class="lb">Расчёт</span>'
       + '<span class="vl">наш</span></div>'
       + "</div></body></html>")

open(S + "dyt-hero.html", "w", encoding="utf-8").write(hero)
open(S + "dyt-info.html", "w", encoding="utf-8").write(fig)
print("готово: dyt-hero.html, dyt-info.html")
