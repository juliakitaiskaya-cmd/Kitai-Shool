# -*- coding: utf-8 -*-
# Картинки к статье «Тест на уровень китайского языка»
# Обложка     — две колоды вопросов: короткий тест и настоящий экзамен
# Инфографика — две падающие кривые везения на логарифмической оси
import math
import sys
sys.path.insert(0, "/home/user/Kitai-Shool/content")
from urtest import TABLE, SHORT, REAL, SHORT_ONE_IN, REAL_ONE_IN, COIN_ONE_IN, one_in

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

# ───────────────────── обложка: две колоды вопросов ─────────────────────
# в колонке по десять карточек в ряд; закрашены те, что «мог бы угадать»


def deck(n, per_row=10):
    cells = ""
    for i in range(n):
        cells += '<div class="q"></div>'
    return '<div class="deck" style="grid-template-columns:repeat(%d,1fr)">%s</div>' % (
        per_row, cells)


def pane(title, n, verdict, strong):
    return ('<div class="pane' + (" alt" if strong else "") + '">'
            '<div class="pt">' + title + '</div>'
            '<div class="pn">' + str(n) + ' вопросов</div>'
            + deck(n) +
            '<div class="pv">' + verdict + "</div></div>")


panes = (pane("Короткий тест в интернете", SHORT,
              "порог берёт наугад<br><b>каждый пятьдесят первый</b>", False)
         + pane("Самый короткий настоящий экзамен", REAL,
                "наугад — <b>один случай<br>из "
                + "{:,}".format(REAL_ONE_IN).replace(",", "&nbsp;") + "</b>", True))
assert panes.count('class="pane') == 2

HERO_CSS = BASE + """
html,body{width:1200px;height:630px}
.card{width:1200px;height:630px;padding:26px 48px 18px 64px}
h1{font-size:39px;max-width:60ch;margin-bottom:5px}
.sub{font-size:15px;color:var(--ink-2);margin-bottom:14px;max-width:96ch;line-height:1.3}
.row{display:flex;align-items:flex-start;gap:46px}
.pane{flex:1 1 0;display:flex;flex-direction:column;align-items:flex-start}
.pt{font-size:13px;font-weight:700;letter-spacing:.1em;text-transform:uppercase;
 color:var(--taupe);margin-bottom:6px}
.pn{font-size:26px;font-weight:700;color:var(--ink);margin-bottom:12px}
.pane.alt .pn{color:var(--brick)}
.deck{display:grid;gap:8px;width:100%;max-width:520px}
.q{aspect-ratio:1/1;border-radius:5px;background:var(--grey-soft);
 border:1px solid var(--hair)}
.pane.alt .q{background:linear-gradient(180deg,#C9637A 0%,var(--brick) 100%);
 border-color:var(--brick-d)}
.pv{font-size:16px;color:var(--ink-2);margin-top:14px;line-height:1.35;max-width:470px}
.pv b{color:var(--ink);font-size:18px}
.band{margin-top:auto;background:var(--surface);border:1px solid var(--hair);
 border-left:4px solid var(--brick);border-radius:13px;padding:13px 18px;
 font-size:16px;color:var(--ink-2);line-height:1.4}
.band b{color:var(--ink)}
.pane.alt .pv b{color:var(--brick)}
"""

hero = ('<!DOCTYPE html><html lang="ru"><head><meta charset="utf-8">' + FONTS
        + "<style>" + VARS + HERO_CSS + "</style></head><body><div class=\"card\">"
        + '<div class="eyebrow">Длина решает больше, чем вопросы</div>'
        + '<h1>Столько вопросов нужно, <i>чтобы отличить знание от везения</i></h1>'
        + '<div class="sub">Одна клетка — один вопрос. Вероятность взять порог '
          'в три пятых, отвечая полностью наугад при четырёх вариантах</div>'
        + '<div class="row">' + panes + '</div>'
        + '<div class="band"><b>Перелом проходит примерно по двум десяткам вопросов.</b> До него результат наполовину про удачу, после — уже в основном про знание</div>'
        + '<div class="foot"><span class="lb">Поэтому</span>'
        + '<span class="vl">короткий тест грубо отделяет начинающего от '
          'продолжающего, но <b>ступень назвать не может</b></span>'
        + '<span class="lb">Расчёт</span>'
        + '<span class="vl">наш, по сочетаниям</span></div>'
        + "</div></body></html>")

# ───────────────────── инфографика: две кривые везения ─────────────────────
W, H = 980, 232
PAD_L, PAD_B = 0, 0
LO = -13.0          # нижняя граница оси: 10 в минус тринадцатой


def ypos(p):
    """Вероятность → координата по вертикали (ноль сверху)."""
    if p <= 0:
        return H
    lg = max(LO, math.log10(p))
    return H * (0.0 - lg) / (0.0 - LO)


xs = [i * W / float(len(TABLE) - 1) for i in range(len(TABLE))]
pts4 = " ".join("%.1f,%.1f" % (x, ypos(t[2])) for x, t in zip(xs, TABLE))
pts2 = " ".join("%.1f,%.1f" % (x, ypos(t[3])) for x, t in zip(xs, TABLE))
assert len(pts4.split()) == len(TABLE) == len(pts2.split())
assert ypos(TABLE[0][3]) < ypos(TABLE[-1][3]), "линия двух вариантов идёт вниз"
assert ypos(TABLE[0][2]) < ypos(TABLE[-1][2]), "линия четырёх вариантов идёт вниз"

dots = ""
for x, t in zip(xs, TABLE):
    for p, cls in ((t[3], "d2"), (t[2], "d4")):
        dots += '<circle class="%s" cx="%.1f" cy="%.1f" r="5"/>' % (cls, x, ypos(p))

ticks = ""
for x, t in zip(xs, TABLE):
    hot = t[0] in (SHORT, REAL)
    ticks += ('<div class="tk' + (" hot" if hot else "") + '" style="left:'
              + str(int(round(x))) + 'px">' + str(t[0]) + "</div>")
assert ticks.count("hot") == 2

# подписи у ключевых точек
def note(idx, p, text, dy, dx=12):
    return ('<div class="nt" style="left:%dpx;top:%dpx">%s</div>'
            % (int(round(xs[idx])) + dx, int(round(ypos(p))) + dy, text))


notes = (note(0, TABLE[0][3], "каждый второй", -30)
         + note(1, TABLE[1][2], "каждый 51-й", -32)
         + note(3, TABLE[3][3], "каждый седьмой", -30)
         + note(3, TABLE[3][2], "один из 353&nbsp;861", -34, 16))

FIG_CSS = BASE + """
html,body{width:1200px;height:520px}
.card{width:1200px;height:520px;padding:22px 48px 14px 64px}
.head{display:flex;justify-content:space-between;align-items:flex-start;gap:34px;
 margin-bottom:10px}
h1{font-size:31px;max-width:38ch}
.tip{background:var(--surface);border:1px solid var(--hair);border-left:4px solid var(--brick);
 border-radius:13px;padding:10px 15px;font-size:13px;color:var(--ink-2);line-height:1.33;
 flex:0 0 310px}
.tip b{color:var(--ink)}
.plot{flex:1 1 auto;display:flex;flex-direction:column;justify-content:center}
.chart{position:relative;width:980px;height:232px;margin-top:6px}
svg{position:absolute;left:0;top:0;overflow:visible}
polyline{fill:none;stroke-width:3.4}
.l2{stroke:var(--taupe);stroke-dasharray:9 6}
.l4{stroke:var(--brick)}
circle.d2{fill:var(--taupe)}
circle.d4{fill:var(--brick)}
.nt{position:absolute;font-size:13.5px;font-weight:700;color:var(--ink);
 white-space:nowrap;background:rgba(255,255,255,.82);padding:1px 5px;border-radius:5px}
.axis{position:relative;width:980px;height:30px;border-top:2px solid var(--hair);
 margin-top:8px}
.tk{position:absolute;top:7px;transform:translateX(-50%);font-size:15px;font-weight:700;
 color:var(--ink-2)}
.tk.hot{color:var(--brick);font-size:17px}
.legend{display:flex;gap:28px;font-size:14px;color:var(--ink-2);margin-top:8px}
.legend b{color:var(--ink)}
.legend i{font-style:normal;display:inline-block;width:26px;height:4px;border-radius:2px;
 margin-right:8px;vertical-align:middle}
.legend .k4{background:var(--brick)}
.legend .k2{background:var(--taupe)}
"""

fig = ('<!DOCTYPE html><html lang="ru"><head><meta charset="utf-8">' + FONTS
       + "<style>" + VARS + FIG_CSS + "</style></head><body><div class=\"card\">"
       + '<div class="head"><div>'
       + '<div class="eyebrow">Вероятность пройти наугад</div>'
       + '<h1>Чем длиннее тест, <i>тем меньше в нём везения</i></h1></div>'
       + '<div class="tip"><b>Вертикаль сжата: каждый шаг вниз — вдесятеро '
         'меньше.</b> Иначе нижняя линия прижалась бы к самому низу и стала '
         'неразличимой</div></div>'
       + '<div class="plot"><div class="chart">'
       + '<svg width="' + str(W) + '" height="' + str(H) + '">'
       + '<polyline class="l2" points="' + pts2 + '"/>'
       + '<polyline class="l4" points="' + pts4 + '"/>'
       + dots + "</svg>" + notes + "</div>"
       + '<div class="axis">' + ticks + "</div>"
       + '<div class="legend">'
         '<span><i class="k2"></i><b>«Верно или нет»</b> — два варианта</span>'
         '<span><i class="k4"></i><b>Четыре варианта</b> — как в большинстве '
         'заданий</span>'
         '<span>По горизонтали — <b>сколько вопросов в тесте</b></span></div>'
       + '</div>'
       + '<div class="foot"><span class="lb">Отмечены</span>'
       + '<span class="vl"><b>' + str(SHORT) + ' и ' + str(REAL) + '</b> — '
         'обычный онлайн-тест и самый короткий настоящий экзамен</span>'
       + '<span class="lb">Расчёт</span>'
       + '<span class="vl">наш, по сочетаниям</span></div>'
       + "</div></body></html>")

open(S + "urt-hero.html", "w", encoding="utf-8").write(hero)
open(S + "urt-info.html", "w", encoding="utf-8").write(fig)
print("готово: urt-hero.html, urt-info.html")
