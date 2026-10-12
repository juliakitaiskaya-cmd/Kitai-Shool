# -*- coding: utf-8 -*-
# Картинки к статье «Как поступить на языковые курсы в Китай»
# Обложка    — разворот паспорта с визовой наклейкой: тип визы выбирает длительность
# Инфографика — кассовая лента: три этапа платежей и что из них не вернут
S = "/tmp/claude-0/-home-user-Kitai-Shool/a463bfca-82a9-56fd-ae09-42a7257ff999/scratchpad/"

FONTS = ("<link href=\"https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,600;0,700;1,600"
         "&family=Inter:wght@400;500;600;700&family=Noto+Serif+SC:wght@600;700&display=swap\" rel=\"stylesheet\">")
VARS = (":root{--brick:#A41E3A;--brick-d:#841630;--brick-soft:#F7E6EB;--ink:#2C2420;--ink-2:#5A4F45;"
        "--taupe:#8B7D6B;--cream:#FAF7F2;--cream-2:#F3EDE3;--hair:#EAE3D8;--surface:#fff;"
        "--green:#1E7A46;--green-soft:#E3F6E9;--amber:#C08A2E;--amber-s:#FBF2DF;--blue:#2F5D8C;--blue-s:#E7EEF6}")

# ------------------------------------------------------------------ обложка
hero = """<!DOCTYPE html><html lang="ru"><head><meta charset="utf-8">
%s
<style>
%s
*{margin:0;box-sizing:border-box}html,body{width:1200px;height:630px}
.card{width:1200px;height:630px;background:radial-gradient(1100px 680px at 16%% 8%%, #fff 0%%, var(--cream) 54%%, var(--cream-2) 100%%);position:relative;overflow:hidden;font-family:'Inter',sans-serif;display:flex;align-items:center;justify-content:space-between;padding:0 58px 0 72px}
.card:before{content:"";position:absolute;left:0;top:0;bottom:0;width:12px;background:var(--brick)}
.txt{flex:0 0 540px}
.eyebrow{color:var(--brick);font-weight:700;font-size:18px;letter-spacing:.19em;text-transform:uppercase;margin-bottom:12px}
h1{font-family:'Cormorant Garamond',serif;font-weight:600;font-size:46px;line-height:1.08;color:var(--ink);letter-spacing:-.4px;max-width:540px}
h1 i{font-style:italic;color:var(--brick)}
.sub{font-size:18px;color:var(--ink-2);line-height:1.42;max-width:30ch;margin-top:16px}
.counts{display:flex;gap:12px;margin-top:25px}
.cnt{background:var(--surface);border:1px solid var(--hair);border-radius:14px;padding:11px 15px;text-align:center;box-shadow:0 4px 14px rgba(44,36,32,.05)}
.cnt b{display:block;font-family:'Cormorant Garamond',serif;font-size:27px;font-weight:700;color:var(--brick);line-height:1.05}
.cnt span{font-size:12px;color:var(--taupe);letter-spacing:.04em}
.brand{position:absolute;left:72px;bottom:32px;display:flex;align-items:center;gap:11px;color:var(--ink)}
.brand b{font-family:'Cormorant Garamond',serif;font-weight:700;font-size:26px}
.brand .bdot{width:10px;height:10px;border-radius:50%%;background:var(--brick)}
.brand span{color:var(--taupe);font-size:16px}

/* разворот паспорта */
.spread{flex:0 0 520px;position:relative}
.book{position:relative;display:flex;height:338px;border-radius:14px;overflow:hidden;box-shadow:0 18px 40px rgba(44,36,32,.18);border:1px solid #D9CFC0}
.pg{flex:1 1 0;background:linear-gradient(180deg,#FDFBF7 0%%,#F6F1E8 100%%);padding:20px 22px;position:relative}
.pg.l{border-right:2px solid #E3D9C9}
.pg.l:after{content:"";position:absolute;right:-1px;top:0;bottom:0;width:14px;background:linear-gradient(90deg,rgba(44,36,32,.10),rgba(44,36,32,0))}
.ptitle{font-size:10.5px;letter-spacing:.22em;color:var(--taupe);font-weight:700;margin-bottom:14px}
.photo{width:88px;height:100px;border:1.5px solid #CFC3B2;border-radius:6px;background:repeating-linear-gradient(135deg,#EFE8DC 0 6px,#F6F1E8 6px 12px);margin-bottom:14px}
.fld{margin-bottom:9px}
.fld .k{font-size:9.5px;letter-spacing:.14em;color:#B3A694;font-weight:700}
.fld .v{height:7px;background:#DED3C2;border-radius:3px;margin-top:4px}
.fld .v.s{width:62%%}.fld .v.m{width:84%%}

/* визовая наклейка */
.visa{position:absolute;right:18px;top:26px;width:258px;background:var(--surface);border:1.5px solid var(--hair);border-radius:10px;padding:13px 15px 15px;box-shadow:0 8px 20px rgba(44,36,32,.14)}
.vh{display:flex;align-items:center;justify-content:space-between;border-bottom:1px solid var(--hair);padding-bottom:8px;margin-bottom:11px}
.vh .cn{font-family:'Noto Serif SC',serif;font-weight:700;font-size:16px;color:var(--ink)}
.vh .en{font-size:10.5px;letter-spacing:.2em;color:var(--taupe);font-weight:700}
.big{font-family:'Cormorant Garamond',serif;font-weight:700;font-size:72px;line-height:.92;color:var(--brick);text-align:center;margin:2px 0 8px}
.vrow{display:flex;justify-content:space-between;align-items:baseline;font-size:11.5px;padding:5px 0;border-bottom:1px dotted var(--hair)}
.vrow:last-child{border-bottom:0}
.vrow .k{color:var(--taupe);letter-spacing:.04em}
.vrow .v{color:var(--ink);font-weight:600}
.stamp{position:absolute;left:24px;bottom:16px;width:74px;height:74px;border:2.5px solid var(--brick);border-radius:50%%;display:flex;align-items:center;justify-content:center;color:var(--brick);font-family:'Noto Serif SC',serif;font-weight:700;font-size:22px;background:rgba(255,255,255,.88);transform:rotate(-12deg);opacity:.95}
.cap{margin-top:16px;font-size:14.5px;color:var(--ink-2);line-height:1.4;text-align:center;max-width:470px}
.cap b{color:var(--ink)}
</style></head><body>
<div class="card">
  <div class="txt">
    <div class="eyebrow">Поступление</div>
    <h1>Как поступить <i>на языковые курсы в Китай</i></h1>
    <div class="sub">Заявку подают прямо в вуз. Дальше всё решает календарь и то, что придёт обратно по почте</div>
    <div class="counts">
      <div class="cnt"><b>2</b><span>НАБОРА В ГОД</span></div>
      <div class="cnt"><b>JW202</b><span>ЕСЛИ ПЛАТИТЕ САМИ</span></div>
      <div class="cnt"><b>24 ч</b><span>НА РЕГИСТРАЦИЮ</span></div>
    </div>
  </div>
  <div class="spread">
    <div class="book">
      <div class="pg l">
        <div class="ptitle">ПАСПОРТ</div>
        <div class="photo"></div>
        <div class="fld"><div class="k">ФАМИЛИЯ</div><div class="v m"></div></div>
        <div class="fld"><div class="k">ИМЯ</div><div class="v s"></div></div>
        <div class="fld"><div class="k">ДАТА РОЖДЕНИЯ</div><div class="v s"></div></div>
      </div>
      <div class="pg r"></div>
      <div class="stamp">入境</div>
    </div>
    <div class="visa">
      <div class="vh"><span class="cn">签证</span><span class="en">VISA</span></div>
      <div class="big">X2</div>
      <div class="vrow"><span class="k">ЦЕЛЬ</span><span class="v">учёба</span></div>
      <div class="vrow"><span class="k">ПРОГРАММА</span><span class="v">до 180 дней</span></div>
      <div class="vrow"><span class="k">ФОРМА ВУЗА</span><span class="v">JW202</span></div>
    </div>
    <div class="cap">Тип визы выбирает <b>длительность программы</b>, а не то, платите вы сами или едете по стипендии</div>
  </div>
  <div class="brand"><span class="bdot"></span><b>Kitai School</b><span>&middot; kitai-school.ru</span></div>
</div>
</body></html>""" % (FONTS, VARS)

open(S + "yk-hero.html", "w", encoding="utf-8").write(hero)

# -------------------------------------------------------------- инфографика
W = 760
TEETH = 20
step = W / TEETH

pts_top = []
for i in range(TEETH * 2 + 1):
    x = i * step / 2
    y = "12px" if i % 2 == 0 else "0px"
    pts_top.append("%.1fpx %s" % (x, y))
pts_bot = []
for i in range(TEETH * 2, -1, -1):
    x = i * step / 2
    y = "calc(100% - 12px)" if i % 2 == 0 else "100%"
    pts_bot.append("%.1fpx %s" % (x, y))
CLIP = "polygon(" + ", ".join(pts_top) + ", " + ", ".join(pts_bot) + ")"


def row(name, cn, mark, bad=True):
    cls = "no" if bad else "maybe"
    cn = '<span class="cn">%s</span>' % cn if cn else ""
    return ('<div class="r"><span class="nm">%s %s</span><span class="dot"></span>'
            '<span class="mk %s">%s</span></div>' % (name, cn, cls, mark))


BLOCKS = [
    ("Этап 1 — до подачи", [
        row("Переводы и заверение документов", "", "не вернут"),
        row("Медицинская форма", "", "не вернут"),
    ]),
    ("Этап 2 — вместе с заявкой", [
        row("Регистрационный взнос", "报名费", "не вернут"),
    ]),
    ("Этап 3 — после зачисления", [
        row("Плата за обучение", "学费", "по правилам вуза", False),
        row("Депозит за общежитие", "", "по правилам вуза", False),
        row("Консульский сбор за визу", "", "не вернут"),
    ]),
]

blocks = "\n".join(
    '<div class="bl"><div class="bt">%s</div>%s</div>' % (t, "".join(rs)) for t, rs in BLOCKS)

info = """<!DOCTYPE html><html lang="ru"><head><meta charset="utf-8">
%s
<style>
%s
*{margin:0;box-sizing:border-box}html,body{width:1200px;height:HGTpx}
.wrap{width:1200px;height:HGTpx;background:linear-gradient(180deg,#fff 0%%,var(--cream) 46%%,var(--cream-2) 100%%);font-family:'Inter',sans-serif;padding:32px 46px 26px;display:flex;flex-direction:column}
.top{display:flex;align-items:flex-end;justify-content:space-between;gap:30px;margin-bottom:20px}
.eyebrow{color:var(--brick);font-weight:700;font-size:14.5px;letter-spacing:.17em;text-transform:uppercase;margin-bottom:7px}
h2{font-family:'Cormorant Garamond',serif;font-weight:600;font-size:40px;line-height:1.07;color:var(--ink);letter-spacing:-.3px}
h2 i{font-style:italic;color:var(--brick)}
.hint{flex:0 0 362px;background:var(--surface);border:1px solid var(--hair);border-left:4px solid var(--brick);border-radius:12px;padding:12px 17px;font-size:14.5px;color:var(--ink-2);line-height:1.36}
.hint b{color:var(--ink)}

.mid{flex:1 1 auto;display:flex;justify-content:center;align-items:flex-start}
.rc{width:760px;background:#fff;clip-path:CLIPPATH;padding:26px 32px 24px;filter:drop-shadow(0 10px 20px rgba(44,36,32,.13));font-family:'Courier New',ui-monospace,monospace}
.rh{text-align:center;border-bottom:2px dashed #CFC6B8;padding-bottom:12px;margin-bottom:16px}
.rh .t{font-size:17px;font-weight:700;letter-spacing:.16em;color:var(--ink)}
.rh .s{font-size:12.5px;color:var(--taupe);letter-spacing:.06em;margin-top:5px}
.bl{margin-bottom:14px}
.bt{font-size:12px;font-weight:700;letter-spacing:.11em;text-transform:uppercase;color:var(--brick);margin-bottom:7px}
.r{display:flex;align-items:baseline;gap:8px;padding:4px 0;font-size:14.5px;color:var(--ink)}
.r .nm{flex:0 0 auto}
.r .cn{font-family:'Noto Serif SC',serif;font-weight:700;font-size:13.5px;color:var(--taupe)}
.r .dot{flex:1 1 auto;border-bottom:1.5px dotted #C9BFAF;transform:translateY(-4px)}
.r .mk{flex:0 0 auto;font-weight:700;font-size:13.5px;letter-spacing:.02em}
.r .mk.no{color:var(--brick)}
.r .mk.maybe{color:var(--blue)}
.tot{border-top:2px dashed #CFC6B8;margin-top:16px;padding-top:14px;font-size:15px;color:var(--ink);line-height:1.4;text-align:center}
.tot b{color:var(--brick)}

.foot{display:flex;align-items:center;gap:18px;padding-top:16px}
.foot .msg{flex:1 1 auto;background:var(--brick-soft);border:1px solid var(--brick);border-radius:14px;padding:12px 21px;font-size:16px;color:var(--ink);line-height:1.34}
.foot .msg b{color:var(--brick)}
.brand{display:flex;align-items:center;gap:10px;color:var(--ink);flex:0 0 auto}
.brand b{font-family:'Cormorant Garamond',serif;font-weight:700;font-size:23px}
.brand .dot2{width:9px;height:9px;border-radius:50%%;background:var(--brick)}
.brand span{color:var(--taupe);font-size:15px}
</style></head><body>
<div class="wrap">
  <div class="top">
    <div>
      <div class="eyebrow">Деньги на входе</div>
      <h2>Что платят до начала занятий — <i>и что из этого не вернут</i></h2>
    </div>
    <div class="hint">Платежи идут <b>тремя волнами</b>, и первая уходит ещё до того, как станет известно решение вуза. Сумм здесь нет: они разные у всех и меняются каждый год.</div>
  </div>

  <div class="mid">
    <div class="rc">
      <div class="rh">
        <div class="t">ЯЗЫКОВАЯ ПРОГРАММА</div>
        <div class="s">платежи до первого дня занятий</div>
      </div>
%s
      <div class="tot">Правила возврата читают <b>до оплаты</b>, а не после</div>
    </div>
  </div>

  <div class="foot">
    <div class="msg">Регистрационный взнос платят <b>вместе с заявкой</b> — то есть до того, как узнают, приняли вас или нет</div>
    <div class="brand"><span class="dot2"></span><b>Kitai School</b><span>&middot; kitai-school.ru</span></div>
  </div>
</div>
</body></html>""" % (FONTS, VARS, blocks)

info = info.replace("CLIPPATH", CLIP).replace("HGT", "652")
open(S + "yk-info.html", "w", encoding="utf-8").write(info)
print("ok")
