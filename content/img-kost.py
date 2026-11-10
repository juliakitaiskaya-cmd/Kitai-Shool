# -*- coding: utf-8 -*-
# Картинки к статье «Традиционный костюм в Китае»
# Обложка     — ярлыки от одежды: название, эпоха, что это за вещь
# Инфографика — линия пояса по эпохам: пять схем силуэта
import sys
sys.path.insert(0, "/home/user/Kitai-Shool/content")
from kostyum import ERAS, RANKS

S = ("/tmp/claude-0/-home-user-Kitai-Shool/a463bfca-82a9-56fd-ae09-42a7257ff999/"
     "scratchpad/")

FONTS = ("<link href=\"https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,600;0,700;1,600"
         "&family=Inter:wght@400;500;600;700&family=Noto+Serif+SC:wght@600;700&display=swap\" rel=\"stylesheet\">")
VARS = (":root{--brick:#A41E3A;--brick-d:#841630;--brick-soft:#F7E6EB;--ink:#2C2420;--ink-2:#5A4F45;"
        "--taupe:#8B7D6B;--cream:#FAF7F2;--cream-2:#F3EDE3;--hair:#EAE3D8;--surface:#fff;"
        "--paper:#FFFDF8;--good:#2F6F4F;--good-soft:#E8F3EC;--grey:#8A8178;--grey-soft:#EFEDE8}")

assert len(ERAS) == 5, "эпох пять"
assert ERAS[-1][6] is None, "у последней эпохи линия талии не задана"


def years(a, b):
    if a < 0:
        return "%d до н. э. — %d н. э." % (-a, b)
    return "%d—%d" % (a, b)


# ─────────── обложка: три ярлыка ───────────
TAGS = [
    ("汉服", "hànfú", "ханьская линия", "семейство фасонов от древности до Мин"),
    ("旗袍", "qípáo", "маньчжурская линия", "одно платье, нынешний вид — XX век"),
    ("唐装", "tángzhuāng", "вопреки названию", "не эпоха Тан, а цинская куртка"),
]
assert len(TAGS) == 3, "на обложке три ярлыка"
assert len(set(t[0] for t in TAGS)) == 3, "названия на ярлыках не повторяются"

tags_html = ""
for han, py, kind, what in TAGS:
    tags_html += ('<div class="tag"><span class="hole"></span>'
                  '<div class="tin"><div class="zh">%s</div><div class="py">%s</div>'
                  '<div class="kind">%s</div><div class="what">%s</div></div></div>'
                  % (han, py, kind, what))

hero = """<!DOCTYPE html><html lang="ru"><head><meta charset="utf-8">
%(fonts)s
<style>
%(vars)s
*{margin:0;box-sizing:border-box}html,body{width:1200px;height:630px}
.card{width:1200px;height:630px;background:radial-gradient(1040px 700px at 12%% 4%%, #fff 0%%, var(--cream) 54%%, var(--cream-2) 100%%);position:relative;overflow:hidden;font-family:'Inter',sans-serif;padding:30px 56px 52px 72px;display:flex;flex-direction:column}
.card:before{content:"";position:absolute;left:0;top:0;bottom:0;width:12px;background:var(--brick)}
.head{display:flex;justify-content:space-between;align-items:flex-end;gap:34px;margin-bottom:26px}
.eyebrow{color:var(--brick);font-weight:700;font-size:18px;letter-spacing:.19em;text-transform:uppercase;margin-bottom:9px}
h1{font-family:'Cormorant Garamond',serif;font-weight:600;font-size:37px;line-height:1.07;color:var(--ink);letter-spacing:-.3px;max-width:23ch}
h1 i{font-style:italic;color:var(--brick)}
.tip{flex:0 0 334px;background:var(--surface);border:1px solid var(--hair);border-left:4px solid var(--brick);border-radius:13px;padding:13px 18px;font-size:15px;color:var(--ink-2);line-height:1.38}
.tip b{color:var(--ink)}

.tags{display:flex;gap:26px;align-items:stretch;flex:1 1 auto}
.tag{flex:1 1 0;background:var(--paper);border:1px solid var(--hair);border-radius:12px;padding:22px 24px 24px;display:flex;flex-direction:column;position:relative;box-shadow:0 3px 0 rgba(44,36,32,.05)}
.tag:before{content:"";position:absolute;left:0;right:0;top:0;height:5px;background:var(--brick);border-radius:12px 12px 0 0}
.hole{position:absolute;top:18px;right:18px;width:15px;height:15px;border-radius:50%%;border:2px solid var(--hair);background:var(--cream-2);display:block}
.tin{padding-top:4px;display:flex;flex-direction:column;flex:1 1 auto}
.tin .zh{font-family:'Noto Serif SC',serif;font-weight:700;font-size:58px;color:var(--ink);line-height:1.1}
.tin .py{font-size:19px;color:var(--brick);font-weight:600;margin-top:4px}
.tin .kind{margin-top:auto;padding-top:18px;font-size:12px;font-weight:700;letter-spacing:.12em;text-transform:uppercase;color:var(--taupe)}
.tin .what{margin-top:8px;font-size:16.5px;color:var(--ink-2);line-height:1.4;min-height:46px}

.foot{margin-top:22px;display:flex;align-items:center;gap:18px;background:var(--surface);border:1px solid var(--hair);border-radius:13px;padding:12px 22px}
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
      <div class="eyebrow">Культура</div>
      <h1>Традиционный костюм в Китае: <i>за одним словом три разных вещи</i></h1>
    </div>
    <div class="tip">Спрашивать «как он выглядит» бесполезно. <b>Нужно называть линию и эпоху</b> — иначе ответов будет несколько.</div>
  </div>

  <div class="tags">%(tags)s</div>

  <div class="foot"><b>дальше</b><span>в статье — силуэт по эпохам, знаки ранга на одежде чиновников и драконий халат императора</span></div>

  <div class="brand"><span class="bdot"></span><b>Kitai School</b><span>&middot; kitai-school.ru</span></div>
</div>
</body></html>""" % dict(fonts=FONTS, vars=VARS, tags=tags_html)

open(S + "kost-hero.html", "w", encoding="utf-8").write(hero)

# ─────────── инфографика: линия пояса по эпохам ───────────
FIG_H = 158          # высота схемы силуэта
cards = ""
for name, a, b, han, py, mean, belt, note in ERAS:
    if belt is None:
        belt_html = ('<div class="noline"><span>талия не обозначена</span></div>')
        mark = '<div class="bval">—</div>'
    else:
        top = FIG_H * belt
        belt_html = ('<div class="belt" style="top:%.1fpx"></div>'
                     '<div class="blab" style="top:%.1fpx">пояс</div>' % (top, top - 19))
        mark = '<div class="bval">%d %%%%</div>' % round(belt * 100)
    cards += ("""<div class="ec">
  <div class="eh"><b>%(name)s</b><span>%(yrs)s</span></div>
  <div class="fig">
    <div class="body"></div>
    <div class="head2"></div>
    %(belt)s
  </div>
  <div class="ez"><span class="zh">%(han)s</span><span class="py">%(py)s</span></div>
  <div class="em">%(mean)s</div>
</div>""" % dict(name=name, yrs=years(a, b), belt=belt_html, han=han, py=py, mean=mean))
assert cards.count('class="ec"') == 5, "на инфографике пять эпох"
assert cards.count('class="belt"') == 4, "пояс отмечен у четырёх эпох из пяти"

info = """<!DOCTYPE html><html lang="ru"><head><meta charset="utf-8">
%(fonts)s
<style>
%(vars)s
*{margin:0;box-sizing:border-box}html,body{width:1200px;height:%(h)dpx}
.wrap{width:1200px;height:%(h)dpx;background:linear-gradient(180deg,#fff 0%%,var(--cream) 44%%,var(--cream-2) 100%%);font-family:'Inter',sans-serif;padding:32px 48px 22px;display:flex;flex-direction:column;position:relative;overflow:hidden}
.wrap:before{content:"";position:absolute;left:0;right:0;top:0;height:9px;background:var(--brick)}
.top{display:flex;align-items:flex-end;justify-content:space-between;gap:34px;margin-bottom:18px}
.eyebrow{color:var(--brick);font-weight:700;font-size:15.5px;letter-spacing:.19em;text-transform:uppercase;margin-bottom:8px}
h2{font-family:'Cormorant Garamond',serif;font-weight:600;font-size:35px;line-height:1.08;color:var(--ink);max-width:24ch}
h2 i{font-style:italic;color:var(--brick)}
.hint{flex:0 0 360px;background:var(--surface);border:1px solid var(--hair);border-left:4px solid var(--brick);border-radius:13px;padding:12px 18px;font-size:14.5px;color:var(--ink-2);line-height:1.36}
.hint b{color:var(--ink)}

.cols{display:flex;gap:14px;flex:1 1 auto}
.ec{flex:1 1 0;background:var(--surface);border:1px solid var(--hair);border-radius:14px;padding:11px 12px 12px;display:flex;flex-direction:column;align-items:center}
.eh{align-self:stretch;text-align:center;padding-bottom:8px;border-bottom:1px solid var(--hair);margin-bottom:8px}
.eh b{display:block;font-size:17px;color:var(--ink);line-height:1.2}
.eh span{font-size:11.5px;color:var(--taupe)}
.fig{position:relative;width:112px;height:%(fh)dpx}
.body{position:absolute;left:50%%;top:24px;transform:translateX(-50%%);width:78px;height:%(bh)dpx;background:linear-gradient(180deg,var(--cream-2) 0%%,#E7DFD2 100%%);border:1px solid var(--hair);border-radius:38px 38px 10px 10px}
.head2{position:absolute;left:50%%;top:0;transform:translateX(-50%%);width:27px;height:27px;border-radius:50%%;background:var(--cream-2);border:1px solid var(--hair)}
.belt{position:absolute;left:8px;right:8px;height:7px;background:var(--brick);border-radius:4px}
.blab{position:absolute;right:0;font-size:11px;font-weight:700;color:var(--brick);letter-spacing:.06em}
.noline{position:absolute;left:-10px;right:-10px;bottom:-6px;text-align:center}
.noline span{font-size:11px;color:var(--ink-2);background:var(--surface);border:1px solid var(--hair);padding:4px 9px;border-radius:7px;display:inline-block;line-height:1.3}
.ez{margin-top:11px;display:flex;align-items:baseline;gap:8px;justify-content:center;flex-wrap:wrap}
.ez .zh{font-family:'Noto Serif SC',serif;font-weight:700;font-size:23px;color:var(--brick-d);line-height:1}
.ez .py{font-size:13px;color:var(--ink-2)}
.em{margin-top:6px;font-size:13px;color:var(--ink-2);text-align:center;line-height:1.35}

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
      <div class="eyebrow">Силуэт по эпохам</div>
      <h2>Эпоха видна <i>по линии пояса</i></h2>
    </div>
    <div class="hint">Узор и цвет менялись и внутри одной эпохи, а посадка задана кроем. <b>Поэтому смотреть нужно на пояс.</b></div>
  </div>

  <div class="cols">%(cards)s</div>

  <div class="foot">
    <div class="msg">При Тан юбку подвязывали <b>под грудью</b>, при Сун пояс возвращался на талию, а при Цин талию <b>не обозначали вовсе</b></div>
    <div class="brand"><span class="dot2"></span><b>Kitai School</b><span>&middot; kitai-school.ru</span></div>
  </div>
</div>
</body></html>""" % dict(fonts=FONTS, vars=VARS, h=560, cards=cards, fh=FIG_H, bh=FIG_H - 24)

open(S + "kost-info.html", "w", encoding="utf-8").write(info)

print("ok | эпох:", len(ERAS), "| ярлыков:", len(TAGS), "| позиций рангов:", len(RANKS))
