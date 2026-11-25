# -*- coding: utf-8 -*-
# Картинки к статье «Результаты HSK: что значит ваш балл»
# Обложка     — два одинаковых сертификата и разные стопки раскладов под ними
# Инфографика — столбцы раскладов по суммам и линия низшего возможного балла
import sys
sys.path.insert(0, "/home/user/Kitai-Shool/content")
from ball2 import TABLE, LOW, HIGH, P_LOW, P_HIGH, TIMES, FLOOR_HIGH, GUARD

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

# ───────────────── обложка: одинаковые сертификаты, разные стопки ─────────────────
# высота стопки линейна числу раскладов — отношение 6,5 видно без искажения
HMAX = 182.0
h_low = int(round(HMAX))
h_high = int(round(HMAX * P_HIGH / float(P_LOW)))
assert h_low > h_high * 4, "разница в высоте читается: %d и %d" % (h_low, h_high)

CERT = ('<div class="cert"><div class="cl"></div><div class="cl"></div>'
        '<div class="cl short"></div><div class="seal"></div></div>')


def pane(total, n, h, note):
    return ('<div class="pane">'
            '<div class="sum">' + str(total) + ' баллов</div>'
            + CERT +
            '<div class="same">тот же сертификат</div>'
            '<div class="stack" style="height:' + str(h) + 'px"></div>'
            '<div class="cnt">' + n + '</div>'
            '<div class="cap">раскладов по трём разделам</div>'
            '<div class="note">' + note + "</div></div>")


def fmt(v):
    return "{:,}".format(v).replace(",", "&nbsp;")


panes = (pane(LOW, fmt(P_LOW), h_low, "любой раздел может быть нулевым")
         + '<div class="vs">в ' + str(TIMES).replace(".", ",") + ' раза<br>меньше</div>'
         + pane(HIGH, fmt(P_HIGH), h_high,
                "ни один раздел не ниже " + str(FLOOR_HIGH)))
assert panes.count('class="pane"') == 2

HERO_CSS = BASE + """
html,body{width:1200px;height:630px}
.card{width:1200px;height:630px;padding:26px 48px 18px 64px}
h1{font-size:38px;max-width:60ch;margin-bottom:5px}
.sub{font-size:15px;color:var(--ink-2);margin-bottom:10px;max-width:96ch;line-height:1.3}
.row{flex:1 1 auto;display:flex;align-items:flex-start;justify-content:center;gap:30px}
.pane{flex:0 0 330px;display:flex;flex-direction:column;align-items:center;text-align:center}
.sum{font-size:23px;font-weight:700;color:var(--ink);margin-bottom:7px}
.cert{width:104px;height:66px;background:var(--surface);border:1px solid var(--hair);
 border-radius:7px;box-shadow:0 2px 7px rgba(44,36,32,.07);padding:13px 14px 0;
 position:relative}
.cl{height:5px;background:var(--grey-soft);border-radius:3px;margin-bottom:7px}
.cl.short{width:52%}
.seal{position:absolute;right:11px;bottom:10px;width:19px;height:19px;border-radius:50%;
 background:var(--brick-soft);border:2px solid var(--brick)}
.same{font-size:12px;color:var(--taupe);margin:6px 0 9px;letter-spacing:.04em}
.stack{width:100%;max-width:210px;border-radius:9px;
 background:repeating-linear-gradient(180deg,var(--brick) 0 7px,#C9637A 7px 10px)}
.cnt{font-size:30px;font-weight:700;color:var(--brick);line-height:1;margin-top:8px;
 border-top:2px solid var(--hair);padding-top:8px;width:100%;max-width:210px;
 letter-spacing:-.5px}
.cap{font-size:12.5px;color:var(--ink-2);margin-top:4px;max-width:210px;line-height:1.28}
.note{font-size:13px;color:var(--ink);margin-top:7px;max-width:220px;line-height:1.3;
 font-weight:600}
.vs{flex:0 0 112px;font-size:16px;font-weight:700;color:var(--taupe);text-align:center;
 line-height:1.3;margin-top:150px}
"""

hero = ('<!DOCTYPE html><html lang="ru"><head><meta charset="utf-8">' + FONTS
        + "<style>" + VARS + HERO_CSS + "</style></head><body><div class=\"card\">"
        + '<div class="eyebrow">Один уровень, разные результаты</div>'
        + '<h1>Сертификат одинаковый — <i>а определённости разное количество</i></h1>'
        + '<div class="sub">Сколькими способами складывается каждая сумма из трёх '
          'разделов по сто баллов. Высота стопки пропорциональна числу '
          'раскладов</div>'
        + '<div class="row">' + panes + '</div>'
        + '<div class="foot"><span class="lb">Главное</span>'
        + '<span class="vl">чем выше сумма, <b>тем меньше способов её собрать</b> '
          '— и тем больше число говорит о человеке</span>'
        + '<span class="lb">Расчёт</span>'
        + '<span class="vl">наш, перебором</span></div>'
        + "</div></body></html>")

# ───────────────── инфографика: столбцы раскладов и линия пола ─────────────────
BMAX = 212.0
PMAX = max(p for s, p, f in TABLE)
bars = ""
for s, p, f in TABLE:
    h = max(3, int(round(BMAX * p / float(PMAX))))
    hot = s in (LOW, HIGH)
    bars += ('<div class="b' + (" hot" if hot else "") + '">'
             '<div class="bn">' + fmt(p) + '</div>'
             '<div class="bar" style="height:' + str(h) + 'px"></div>'
             '<div class="bs">' + str(s) + '</div>'
             '<div class="bf' + (" on" if f else "") + '">' + str(f) + "</div></div>")
assert bars.count('class="b"') + bars.count('class="b hot"') == len(TABLE)
assert bars.count("hot") == 2

FIG_CSS = BASE + """
html,body{width:1200px;height:520px}
.card{width:1200px;height:520px;padding:22px 48px 14px 64px}
.head{display:flex;justify-content:space-between;align-items:flex-start;gap:34px;
 margin-bottom:14px}
h1{font-size:32px;max-width:40ch}
.tip{background:var(--surface);border:1px solid var(--hair);border-left:4px solid var(--brick);
 border-radius:13px;padding:10px 15px;font-size:13px;color:var(--ink-2);line-height:1.33;
 flex:0 0 300px}
.tip b{color:var(--ink)}
.plot{flex:1 1 auto;display:flex;align-items:flex-end;gap:16px;padding-bottom:4px}
.b{flex:1 1 0;display:flex;flex-direction:column;align-items:center;text-align:center}
.bn{font-size:14px;font-weight:700;color:var(--ink-2);margin-bottom:6px}
.bar{width:100%;max-width:92px;border-radius:7px 7px 0 0;
 background:linear-gradient(180deg,#C9637A 0%,var(--brick) 100%);opacity:.42}
.b.hot .bar{opacity:1}
.b.hot .bn{color:var(--brick);font-size:17px}
.bs{font-size:16px;font-weight:700;color:var(--ink);margin-top:9px;
 border-top:2px solid var(--hair);width:100%;max-width:92px;padding-top:7px}
.b.hot .bs{color:var(--brick)}
.bf{font-size:15px;font-weight:700;color:var(--grey);margin-top:7px;width:100%;
 max-width:92px;padding:4px 0;border-radius:6px;background:var(--grey-soft)}
.bf.on{color:#fff;background:var(--brick-d)}
.legend{display:flex;gap:26px;font-size:13.5px;color:var(--ink-2);margin-top:11px;
 line-height:1.35}
.legend b{color:var(--ink)}
.legend i{font-style:normal;display:inline-block;width:11px;height:11px;border-radius:3px;
 background:var(--brick-d);margin-right:6px}
"""

fig = ('<!DOCTYPE html><html lang="ru"><head><meta charset="utf-8">' + FONTS
       + "<style>" + VARS + FIG_CSS + "</style></head><body><div class=\"card\">"
       + '<div class="head"><div>'
       + '<div class="eyebrow">Чем выше сумма, тем меньше вариантов</div>'
       + '<h1>Столбец — сколько раскладов даёт сумма, <i>нижняя плашка — '
         'что гарантировано</i></h1></div>'
       + '<div class="tip"><b>Нижний ряд — самый низкий балл, который ещё возможен '
         'в разделе.</b> До двухсот баллов он нулевой, и уровень можно сдать '
         'с провалом</div></div>'
       + '<div class="plot">' + bars + '</div>'
       + '<div class="legend"><span><b>Верхнее число</b> — раскладов по трём '
         'разделам</span>'
       + '<span><i></i><b>Нижнее число</b> — гарантированный минимум в разделе, '
         'он отрывается от нуля после ' + str(GUARD - 1) + ' баллов</span></div>'
       + '<div class="foot"><span class="lb">Отмечены</span>'
       + '<span class="vl"><b>' + str(LOW) + ' и ' + str(HIGH) + '</b> — два '
         'результата, с которых начался разбор</span>'
       + '<span class="lb">Расчёт</span>'
       + '<span class="vl">наш, перебором</span></div>'
       + "</div></body></html>")

open(S + "bl2-hero.html", "w", encoding="utf-8").write(hero)
open(S + "bl2-info.html", "w", encoding="utf-8").write(fig)
print("готово: bl2-hero.html, bl2-info.html")
