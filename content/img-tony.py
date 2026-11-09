# -*- coding: utf-8 -*-
# Картинки к статье «Тоны в китайском языке»
# Обложка     — «что сказал — что услышали»: четыре реплики на одном слоге
# Инфографика — ступени высоты: пять уровней и четыре траектории
import sys
sys.path.insert(0, "/home/user/Kitai-Shool/content")
from tones import TONES, NEUTRAL, HIGHEST, LOWEST

S = ("/tmp/claude-0/-home-user-Kitai-Shool/a463bfca-82a9-56fd-ae09-42a7257ff999/"
     "scratchpad/")

FONTS = ("<link href=\"https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,600;0,700;1,600"
         "&family=Inter:wght@400;500;600;700&family=Noto+Serif+SC:wght@600;700&display=swap\" rel=\"stylesheet\">")
VARS = (":root{--brick:#A41E3A;--brick-d:#841630;--brick-soft:#F7E6EB;--ink:#2C2420;--ink-2:#5A4F45;"
        "--taupe:#8B7D6B;--cream:#FAF7F2;--cream-2:#F3EDE3;--hair:#EAE3D8;--surface:#fff;"
        "--paper:#FFFDF8;--good:#2F6F4F;--good-soft:#E8F3EC;--grey:#8A8178;--grey-soft:#EFEDE8}")

assert len(TONES) == 4, "основных тонов четыре"
assert (LOWEST, HIGHEST) == (1, 5), "шкала от 1 до 5"
assert all("конопля" not in str(t) for t in TONES), "слова «конопля» в данных нет"
assert len(set(t[7] for t in TONES)) == 4, "траектории должны различаться"

# ─────────── обложка: «что сказал — что услышали» ───────────
lines = ""
for num, name, move, digits, syl, han, mean, pts in TONES:
    lines += ('<div class="ln">'
              '<div class="said"><span class="no">%d-й тон</span>'
              '<span class="syl">%s</span><span class="mv">%s</span></div>'
              '<div class="arr"></div>'
              '<div class="heard"><span class="zh">%s</span>'
              '<span class="tr">%s</span></div>'
              '</div>' % (num, syl, move, han, mean))
assert lines.count('class="ln"') == 4, "на обложке четыре реплики"

hero = """<!DOCTYPE html><html lang="ru"><head><meta charset="utf-8">
%(fonts)s
<style>
%(vars)s
*{margin:0;box-sizing:border-box}html,body{width:1200px;height:630px}
.card{width:1200px;height:630px;background:radial-gradient(1040px 700px at 12%% 4%%, #fff 0%%, var(--cream) 54%%, var(--cream-2) 100%%);position:relative;overflow:hidden;font-family:'Inter',sans-serif;padding:30px 56px 52px 72px;display:flex;flex-direction:column}
.card:before{content:"";position:absolute;left:0;top:0;bottom:0;width:12px;background:var(--brick)}
.head{display:flex;justify-content:space-between;align-items:flex-end;gap:34px;margin-bottom:18px}
.eyebrow{color:var(--brick);font-weight:700;font-size:18px;letter-spacing:.19em;text-transform:uppercase;margin-bottom:9px}
h1{font-family:'Cormorant Garamond',serif;font-weight:600;font-size:37px;line-height:1.07;color:var(--ink);letter-spacing:-.3px;max-width:23ch}
h1 i{font-style:italic;color:var(--brick)}
.tip{flex:0 0 330px;background:var(--surface);border:1px solid var(--hair);border-left:4px solid var(--brick);border-radius:13px;padding:13px 18px;font-size:15px;color:var(--ink-2);line-height:1.38}
.tip b{color:var(--ink)}

.cols{display:flex;gap:0;margin-bottom:9px;padding:0 2px}
.cols div{font-size:12px;font-weight:700;letter-spacing:.14em;text-transform:uppercase;color:var(--taupe)}
.cols .c1{flex:1 1 auto}
.cols .c2{flex:0 0 404px}

.lines{display:flex;flex-direction:column;gap:11px}
.ln{display:flex;align-items:stretch;gap:0}
.said{flex:1 1 auto;background:var(--surface);border:1px solid var(--hair);border-radius:13px 0 0 13px;border-right:0;display:flex;align-items:center;gap:20px;padding:11px 22px}
.said .no{flex:0 0 94px;font-size:13px;font-weight:600;color:var(--taupe)}
.said .syl{font-size:31px;font-weight:600;color:var(--ink);line-height:1;flex:0 0 92px}
.said .mv{font-size:15px;color:var(--ink-2)}
.arr{flex:0 0 46px;background:var(--surface);border-top:1px solid var(--hair);border-bottom:1px solid var(--hair);position:relative}
.arr:before{content:"";position:absolute;left:8px;top:50%%;width:22px;height:2px;background:var(--taupe)}
.arr:after{content:"";position:absolute;left:24px;top:50%%;margin-top:-4px;border:5px solid transparent;border-left-color:var(--taupe)}
.heard{flex:0 0 404px;background:var(--brick-soft);border:1px solid var(--brick);border-radius:0 13px 13px 0;display:flex;align-items:center;gap:18px;padding:11px 24px}
.heard .zh{font-family:'Noto Serif SC',serif;font-weight:700;font-size:38px;color:var(--brick-d);line-height:1;flex:0 0 46px}
.heard .tr{font-size:17px;color:var(--ink);font-weight:500}

.foot{margin-top:16px;display:flex;align-items:center;gap:18px;background:var(--surface);border:1px solid var(--hair);border-radius:13px;padding:12px 22px}
.foot b{font-size:12.5px;font-weight:700;letter-spacing:.11em;text-transform:uppercase;color:var(--brick);flex:0 0 auto}
.foot span{font-size:15.5px;color:var(--ink);line-height:1.36}

.brand{position:absolute;left:72px;bottom:17px;display:flex;align-items:center;gap:11px;color:var(--ink)}
.brand b{font-family:'Cormorant Garamond',serif;font-weight:700;font-size:25px}
.brand .bdot{width:10px;height:10px;border-radius:50%%;background:var(--brick)}
.brand span{color:var(--taupe);font-size:16px}
</style></head><body>
<div class="card">
  <div class="head">
    <div>
      <div class="eyebrow">Фонетика</div>
      <h1>Тоны в китайском языке: <i>один слог, четыре слова</i></h1>
    </div>
    <div class="tip">Звуки везде одни и те же — <b>меняется только высота голоса</b>. Собеседник слышит не акцент, а другое слово.</div>
  </div>

  <div class="cols"><div class="c1">что произнесли</div><div class="c2">что услышали</div></div>
  <div class="lines">%(lines)s</div>

  <div class="foot"><b>и пятое</b><span>слог без своей высоты — нейтральный: <span style="font-family:'Noto Serif SC',serif">%(nh)s</span> %(ns)s, короткий и безударный</span></div>

  <div class="brand"><span class="bdot"></span><b>Kitai School</b><span>&middot; kitai-school.ru</span></div>
</div>
</body></html>""" % dict(fonts=FONTS, vars=VARS, lines=lines, nh=NEUTRAL[5], ns=NEUTRAL[4])

open(S + "tony-hero.html", "w", encoding="utf-8").write(hero)

# ─────────── инфографика: ступени высоты ───────────
PLOT_W, PLOT_H = 172, 152          # размер поля одной траектории
PAD = 14
LEFT = 22                          # поле слева под цифры уровней


def ylevel(lvl):
    """Высота уровня шкалы 1–5 в координатах поля."""
    return PLOT_H - PAD - (PLOT_H - 2 * PAD) * (lvl - 1) / 4.0


def path(pts):
    """Ломаная по точкам шкалы 1–5 внутри поля PLOT_W × PLOT_H."""
    n = len(pts)
    xs = [LEFT + PAD + (PLOT_W - LEFT - 2 * PAD) * i / (n - 1) for i in range(n)]
    ys = [ylevel(p) for p in pts]
    return " ".join("%.1f,%.1f" % (x, y) for x, y in zip(xs, ys)), xs, ys


assert abs(ylevel(5) - PAD) < 0.01 and abs(ylevel(1) - (PLOT_H - PAD)) < 0.01, \
    "уровни 5 и 1 должны лечь на края поля"

cards = ""
for num, name, move, digits, syl, han, mean, pts in TONES:
    d, xs, ys = path(pts)
    grid = "".join('<line x1="%d" y1="%.1f" x2="%d" y2="%.1f" />'
                   % (LEFT, ylevel(lvl), PLOT_W, ylevel(lvl)) for lvl in range(1, 6))
    marks = "".join('<text x="%d" y="%.1f">%d</text>' % (LEFT - 8, ylevel(lvl) + 4, lvl)
                    for lvl in range(1, 6))
    dots = "".join('<circle cx="%.1f" cy="%.1f" r="5" />' % (x, y)
                   for x, y in zip(xs, ys))
    cards += ("""<div class="tc">
  <div class="th"><b>%(num)d-й тон</b><span class="dig">%(dig)s</span></div>
  <svg viewBox="0 0 %(w)d %(h)d" width="%(w)d" height="%(h)d">
    <g class="g">%(grid)s</g>
    <g class="lv">%(marks)s</g>
    <polyline class="tr" points="%(d)s" />
    <g class="dt">%(dots)s</g>
  </svg>
  <div class="tm">%(move)s</div>
  <div class="tw"><span class="zh">%(han)s</span><span class="sy">%(syl)s</span><span class="mn">%(mean)s</span></div>
</div>""" % dict(num=num, dig=digits, w=PLOT_W, h=PLOT_H, grid=grid, marks=marks, d=d, dots=dots,
                 move=move, han=han, syl=syl, mean=mean))
assert cards.count('class="tc"') == 4, "на инфографике четыре траектории"
assert all(str(p) in cards for t in TONES for p in [t[3]]), "записи высот должны попасть в карточки"

info = """<!DOCTYPE html><html lang="ru"><head><meta charset="utf-8">
%(fonts)s
<style>
%(vars)s
*{margin:0;box-sizing:border-box}html,body{width:1200px;height:%(h)dpx}
.wrap{width:1200px;height:%(h)dpx;background:linear-gradient(180deg,#fff 0%%,var(--cream) 44%%,var(--cream-2) 100%%);font-family:'Inter',sans-serif;padding:34px 48px 24px;display:flex;flex-direction:column;position:relative;overflow:hidden}
.wrap:before{content:"";position:absolute;left:0;right:0;top:0;height:9px;background:var(--brick)}
.top{display:flex;align-items:flex-end;justify-content:space-between;gap:34px;margin-bottom:20px}
.eyebrow{color:var(--brick);font-weight:700;font-size:15.5px;letter-spacing:.19em;text-transform:uppercase;margin-bottom:8px}
h2{font-family:'Cormorant Garamond',serif;font-weight:600;font-size:36px;line-height:1.08;color:var(--ink);max-width:23ch}
h2 i{font-style:italic;color:var(--brick)}
.hint{flex:0 0 376px;background:var(--surface);border:1px solid var(--hair);border-left:4px solid var(--brick);border-radius:13px;padding:12px 18px;font-size:14.5px;color:var(--ink-2);line-height:1.36}
.hint b{color:var(--ink)}

.body{display:flex;gap:16px;align-items:stretch}
.cards{flex:1 1 auto;display:flex;gap:14px}
.tc{flex:1 1 0;background:var(--surface);border:1px solid var(--hair);border-radius:14px;padding:12px 11px 13px;display:flex;flex-direction:column;align-items:center}
.th{display:flex;align-items:baseline;gap:10px;align-self:stretch;justify-content:space-between;margin-bottom:4px}
.th b{font-size:16px;color:var(--ink)}
.th .dig{font-size:17px;font-weight:700;color:var(--brick);font-variant-numeric:tabular-nums}
.tc svg{display:block}
.g line{stroke:var(--hair);stroke-width:1}
.lv text{fill:var(--taupe);font-family:'Inter',sans-serif;font-size:11px;font-weight:600;text-anchor:end}
.tr{fill:none;stroke:var(--brick);stroke-width:5;stroke-linejoin:round;stroke-linecap:round}
.dt circle{fill:var(--brick-d)}
.tm{font-size:14px;color:var(--ink-2);margin:6px 0 9px;text-align:center}
.tw{display:flex;align-items:center;gap:9px;background:var(--brick-soft);border:1px solid var(--brick);border-radius:10px;padding:7px 12px;align-self:stretch;justify-content:center}
.tw .zh{font-family:'Noto Serif SC',serif;font-weight:700;font-size:24px;color:var(--brick-d);line-height:1}
.tw .sy{font-size:16px;font-weight:600;color:var(--ink)}
.tw .mn{font-size:13px;color:var(--ink-2)}

.side{flex:0 0 190px;display:flex;flex-direction:column;gap:12px}
.ntr{background:var(--grey-soft);border:1px dashed var(--grey);border-radius:14px;padding:13px 15px;flex:1 1 auto}
.ntr b{display:block;font-size:14.5px;color:var(--ink);margin-bottom:7px}
.ntr .pt{display:flex;align-items:center;gap:9px;margin:9px 0 10px}
.ntr .pt em{width:13px;height:13px;border-radius:50%%;background:var(--grey);display:block}
.ntr .pt span{font-family:'Noto Serif SC',serif;font-weight:700;font-size:22px;color:var(--ink)}
.ntr p{font-size:13px;color:var(--ink-2);line-height:1.4}

.foot{margin-top:16px;display:flex;align-items:center;gap:18px}
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
      <div class="eyebrow">Высота, а не громкость</div>
      <h2>Пять уровней голоса и <i>четыре траектории</i></h2>
    </div>
    <div class="hint">Цифры под названием тона — <b>высота начала и конца</b> по шкале от 1 до 5, где 1 — низ обычного голоса, а 5 — верх.</div>
  </div>

  <div class="body">
    <div class="cards">%(cards)s</div>
    <div class="side">
      <div class="ntr">
        <b>Нейтральный слог</b>
        <div class="pt"><em></em><span>%(nh)s</span></div>
        <p>Своей высоты нет: произносится коротко и без ударения, а высота остаётся от предыдущего слога. Знака тона в записи у него тоже нет.</p>
      </div>
    </div>
  </div>

  <div class="foot">
    <div class="msg">Второй и третий тоны оба заканчиваются выше, чем начались: <b>разница у них в начале слога</b>, а не в конце</div>
    <div class="brand"><span class="dot2"></span><b>Kitai School</b><span>&middot; kitai-school.ru</span></div>
  </div>
</div>
</body></html>""" % dict(fonts=FONTS, vars=VARS, h=560, cards=cards, nh=NEUTRAL[5])

open(S + "tony-info.html", "w", encoding="utf-8").write(info)

print("ok | тонов:", len(TONES), "+ нейтральный | шкала:", LOWEST, "-", HIGHEST,
      "| записи:", ", ".join(t[3] for t in TONES))
