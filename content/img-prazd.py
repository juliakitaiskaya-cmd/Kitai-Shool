# -*- coding: utf-8 -*-
# Картинки к статье «Китайские традиционные праздники»
# Обложка    — отрывной лист лунного календаря: одна лунная дата и плавающая наша
# Инфографика — год по кругу: дуги лунных дат и жёсткая точка Цинмина
import math

S = ("/tmp/claude-0/-home-user-Kitai-Shool/a463bfca-82a9-56fd-ae09-42a7257ff999/"
     "scratchpad/")

FONTS = ("<link href=\"https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,600;0,700;1,600"
         "&family=Inter:wght@400;500;600;700&family=Noto+Serif+SC:wght@600;700&display=swap\" rel=\"stylesheet\">")
VARS = (":root{--brick:#A41E3A;--brick-d:#841630;--brick-soft:#F7E6EB;--ink:#2C2420;--ink-2:#5A4F45;"
        "--taupe:#8B7D6B;--cream:#FAF7F2;--cream-2:#F3EDE3;--hair:#EAE3D8;--surface:#fff;"
        "--paper:#FDFBF6;--gold:#B9873F;--slate:#2F5D8C;--moss:#4B6A4F;--plum:#6E3A5E}")

# ------------------------------------------------------------------ обложка
hero = """<!DOCTYPE html><html lang="ru"><head><meta charset="utf-8">
%s
<style>
%s
*{margin:0;box-sizing:border-box}html,body{width:1200px;height:630px}
.card{width:1200px;height:630px;background:radial-gradient(1050px 660px at 14%% 12%%, #fff 0%%, var(--cream) 52%%, var(--cream-2) 100%%);position:relative;overflow:hidden;font-family:'Inter',sans-serif;padding:52px 46px 0 72px;display:flex;justify-content:space-between}
.card:before{content:"";position:absolute;left:0;top:0;bottom:0;width:12px;background:var(--brick)}
.txt{flex:0 0 492px;padding-top:6px}
.eyebrow{color:var(--brick);font-weight:700;font-size:18px;letter-spacing:.19em;text-transform:uppercase;margin-bottom:13px}
h1{font-family:'Cormorant Garamond',serif;font-weight:600;font-size:46px;line-height:1.07;color:var(--ink);letter-spacing:-.4px}
h1 i{font-style:italic;color:var(--brick)}
.sub{font-size:18px;color:var(--ink-2);line-height:1.42;max-width:31ch;margin-top:16px}
.tip{display:inline-block;margin-top:22px;background:var(--surface);border:1px solid var(--hair);border-left:4px solid var(--brick);border-radius:13px;padding:13px 19px;font-size:15.5px;color:var(--ink-2);line-height:1.36;max-width:34ch}
.tip b{color:var(--ink)}

/* отрывной лист календаря */
.scene{flex:0 0 486px;padding-top:34px;display:flex;flex-direction:column;align-items:center}
.sheet{position:relative;width:352px;background:var(--paper);border:1px solid var(--hair);border-radius:8px 8px 12px 12px;box-shadow:0 20px 34px rgba(44,36,32,.2);padding:40px 28px 24px;text-align:center}
.sheet:before{content:"";position:absolute;left:0;right:0;top:0;height:22px;background:var(--cream-2);border-radius:8px 8px 0 0;border-bottom:1px solid var(--hair)}
.holes{position:absolute;left:0;right:0;top:6px;display:flex;justify-content:center;gap:40px}
.holes i{width:13px;height:13px;border-radius:50%%;background:var(--cream);border:1px solid #DCD2C2;box-shadow:inset 0 1px 2px rgba(0,0,0,.12)}
.sheet .mon{font-size:13px;letter-spacing:.17em;text-transform:uppercase;color:var(--taupe);margin-top:4px}
.sheet .han{font-family:'Noto Serif SC',serif;font-size:62px;color:var(--brick);line-height:1.08;margin-top:6px}
.sheet .py{font-size:17px;color:var(--ink-2);font-style:italic;margin-top:4px}
.sheet .lunar{margin-top:16px;padding-top:15px;border-top:1px dashed #D8CDBB}
.sheet .lunar .lh{font-size:12.5px;letter-spacing:.13em;text-transform:uppercase;color:var(--taupe)}
.sheet .lunar .lv{font-family:'Noto Serif SC',serif;font-size:31px;color:var(--ink);margin-top:5px}
.sheet .lunar .lp{font-size:14.5px;color:var(--ink-2);margin-top:3px}
.band{margin-top:18px;background:var(--brick-soft);border:1px solid var(--brick);border-radius:11px;padding:10px 14px;font-size:14.5px;color:var(--ink);line-height:1.32}
.band b{color:var(--brick-d)}
.cap{margin-top:20px;text-align:center;font-size:16.5px;color:var(--ink-2);line-height:1.4;max-width:35ch}
.cap b{color:var(--ink)}
.brand{position:absolute;left:72px;bottom:28px;display:flex;align-items:center;gap:11px;color:var(--ink)}
.brand b{font-family:'Cormorant Garamond',serif;font-weight:700;font-size:26px}
.brand .bdot{width:10px;height:10px;border-radius:50%%;background:var(--brick)}
.brand span{color:var(--taupe);font-size:16px}
</style></head><body>
<div class="card">
  <div class="txt">
    <div class="eyebrow">Культура</div>
    <h1>Традиционные праздники <i>Китая</i></h1>
    <div class="sub">Лунная дата у праздника одна и та же, а наша — каждый год другая</div>
    <div class="tip"><b>Новый год — это первый день первого лунного месяца.</b> В нашем календаре он приходится на разные дни</div>
  </div>
  <div class="scene">
    <div class="sheet">
      <div class="holes"><i></i><i></i></div>
      <div class="mon">главный день года</div>
      <div class="han">春节</div>
      <div class="py">chūnjié</div>
      <div class="lunar">
        <div class="lh">по лунному календарю</div>
        <div class="lv">正月初一</div>
        <div class="lp">zhēngyuè chūyī — первый день первого месяца</div>
      </div>
      <div class="band">В нашем календаре — <b>между 21 января и 20 февраля</b></div>
    </div>
    <div class="cap">Одна дата у праздника, <b>две записи в календаре</b></div>
  </div>
  <div class="brand"><span class="bdot"></span><b>Kitai School</b><span>&middot; kitai-school.ru</span></div>
</div>
</body></html>""" % (FONTS, VARS)

open(S + "pr-hero.html", "w", encoding="utf-8").write(hero)

# --------------------------------------------------------------- инфографика
DAYS = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
MON = ["янв", "фев", "мар", "апр", "май", "июн",
       "июл", "авг", "сен", "окт", "ноя", "дек"]


def ang(month, day):
    """Угол на круге года: 0° — 1 января, по часовой стрелке."""
    return (month - 1) * 30.0 + (day - 1) / DAYS[month - 1] * 30.0


# номер, дорожка, цвет, начало и конец разлёта по нашему календарю
ARCS = [
    (1, 0, "var(--brick)",  (1, 21), (2, 20), "春节"),
    (2, 1, "var(--gold)",   (2, 4),  (3, 6),  "元宵节"),
    (3, 0, "var(--slate)",  (4, 4),  (4, 6),  "清明节"),
    (4, 1, "var(--moss)",   (5, 30), (6, 26), "端午节"),
    (5, 0, "var(--plum)",   (9, 8),  (10, 8), "中秋节"),
    (6, 1, "var(--taupe)",  (10, 7), (11, 5), "重阳节"),
]

TRACK = [(156, 174), (128, 146)]  # внутренний и внешний радиус дорожки
CX = CY = 220

months = "".join(
    '<span class="mn" style="left:%.1fpx;top:%.1fpx">%s</span>'
    % (CX + 201 * math.sin(math.radians(ang(i + 1, 16))) - 20,
       CY - 201 * math.cos(math.radians(ang(i + 1, 16))) - 9, MON[i])
    for i in range(12))

ring_css = []
ring_div = []
marks = []
for num, tr, col, a, b, name in ARCS:
    a0, a1 = ang(*a), ang(*b)
    ri, ro = TRACK[tr]
    ring_css.append(
        ".arc%d{background:conic-gradient(from 0deg, transparent 0 %.2fdeg, %s %.2fdeg %.2fdeg, "
        "transparent %.2fdeg 360deg);-webkit-mask-image:radial-gradient(circle at center, "
        "transparent 0 %dpx, #000 %dpx %dpx, transparent %dpx)}"
        % (num, a0, col, a0, a1, a1, ri, ri, ro, ro))
    ring_div.append('<div class="ring arc%d"></div>' % num)
    mid = math.radians((a0 + a1) / 2)
    rc = (ri + ro) / 2
    marks.append(
        '<span class="mk" style="left:%.1fpx;top:%.1fpx;background:%s">%d</span>'
        % (CX + rc * math.sin(mid) - 13, CY - rc * math.cos(mid) - 13, col, num))

LEG = [
    (1, "var(--brick)", "春节", "chūnjié", "1-й день 1-го месяца", "21 янв — 20 фев"),
    (2, "var(--gold)", "元宵节", "yuánxiāojié", "15-й день 1-го месяца", "фев — начало марта"),
    (3, "var(--slate)", "清明节", "qīngmíngjié", "солнечная дата", "4—6 апреля"),
    (4, "var(--moss)", "端午节", "duānwǔjié", "5-й день 5-го месяца", "конец мая — июнь"),
    (5, "var(--plum)", "中秋节", "zhōngqiūjié", "15-й день 8-го месяца", "сентябрь — начало октября"),
    (6, "var(--taupe)", "重阳节", "chóngyángjié", "9-й день 9-го месяца", "октябрь — начало ноября"),
]

legend = "\n".join(
    '  <div class="lr"><span class="no" style="background:%s">%d</span>'
    '<span class="hn">%s</span><span class="pn">%s</span>'
    '<span class="ln">%s</span><span class="gr">%s</span></div>'
    % (col, no, han, py, lunar, greg) for no, col, han, py, lunar, greg in LEG)

info = """<!DOCTYPE html><html lang="ru"><head><meta charset="utf-8">
%(fonts)s
<style>
%(vars)s
*{margin:0;box-sizing:border-box}html,body{width:1200px;height:HGTpx}
.wrap{width:1200px;height:HGTpx;background:linear-gradient(180deg,#fff 0%%,var(--cream) 46%%,var(--cream-2) 100%%);font-family:'Inter',sans-serif;padding:30px 44px 26px;display:flex;flex-direction:column}
.top{display:flex;align-items:flex-end;justify-content:space-between;gap:30px;margin-bottom:16px}
.eyebrow{color:var(--brick);font-weight:700;font-size:14.5px;letter-spacing:.17em;text-transform:uppercase;margin-bottom:7px}
h2{font-family:'Cormorant Garamond',serif;font-weight:600;font-size:40px;line-height:1.07;color:var(--ink);letter-spacing:-.3px}
h2 i{font-style:italic;color:var(--brick)}
.hint{flex:0 0 372px;background:var(--surface);border:1px solid var(--hair);border-left:4px solid var(--brick);border-radius:12px;padding:12px 17px;font-size:14.5px;color:var(--ink-2);line-height:1.36}
.hint b{color:var(--ink)}

.main{display:flex;gap:30px;align-items:center}
.dial{position:relative;flex:0 0 440px;width:440px;height:440px}
.face{position:absolute;inset:0;border-radius:50%%;background:conic-gradient(from 0deg,
  var(--cream-2) 0 30deg, var(--surface) 30deg 60deg, var(--cream-2) 60deg 90deg, var(--surface) 90deg 120deg,
  var(--cream-2) 120deg 150deg, var(--surface) 150deg 180deg, var(--cream-2) 180deg 210deg, var(--surface) 210deg 240deg,
  var(--cream-2) 240deg 270deg, var(--surface) 270deg 300deg, var(--cream-2) 300deg 330deg, var(--surface) 330deg 360deg);
  -webkit-mask-image:radial-gradient(circle at center, transparent 0 186px, #000 186px 220px, transparent 220px);
  box-shadow:0 6px 16px rgba(44,36,32,.07)}
.hoop{position:absolute;inset:0;border-radius:50%%;border:1px solid var(--hair)}
.hoop2{position:absolute;left:34px;top:34px;width:372px;height:372px;border-radius:50%%;border:1px solid var(--hair)}
.ring{position:absolute;inset:0;border-radius:50%%}
%(rings)s
.mn{position:absolute;width:40px;text-align:center;font-size:11.5px;color:var(--taupe);letter-spacing:.03em}
.mk{position:absolute;width:26px;height:26px;border-radius:50%%;color:#fff;font-size:14px;font-weight:700;display:flex;align-items:center;justify-content:center;box-shadow:0 2px 5px rgba(44,36,32,.22)}
.core{position:absolute;left:115px;top:162px;width:210px;text-align:center}
.core .ch{font-family:'Noto Serif SC',serif;font-size:34px;color:var(--ink)}
.core .cp{font-size:14px;color:var(--ink-2);font-style:italic;margin-top:2px}
.core .cd{font-size:13px;color:var(--taupe);margin-top:8px;line-height:1.32}

.side{flex:1 1 auto;background:var(--surface);border:1px solid var(--hair);border-radius:16px;padding:16px 20px 14px;box-shadow:0 5px 14px rgba(44,36,32,.06)}
.side .sh{display:flex;font-size:11.5px;letter-spacing:.11em;text-transform:uppercase;color:var(--taupe);padding-bottom:9px;border-bottom:1px solid var(--hair);margin-bottom:4px}
.side .sh span:nth-child(1){flex:0 0 34px}
.side .sh span:nth-child(2){flex:0 0 150px}
.side .sh span:nth-child(3){flex:0 0 160px}
.side .sh span:nth-child(4){flex:1 1 auto}
.lr{display:flex;align-items:center;padding:9px 0;border-bottom:1px solid var(--cream-2)}
.lr:last-child{border-bottom:none}
.no{flex:0 0 24px;height:24px;border-radius:50%%;color:#fff;font-size:13px;font-weight:700;display:flex;align-items:center;justify-content:center;margin-right:10px}
.hn{flex:0 0 76px;font-family:'Noto Serif SC',serif;font-size:21px;color:var(--ink)}
.pn{flex:0 0 114px;font-size:14px;color:var(--ink-2);font-style:italic}
.ln{flex:0 0 160px;font-size:14px;color:var(--ink)}
.gr{flex:1 1 auto;font-size:14px;color:var(--brick-d);font-weight:600}
.note{margin-top:11px;font-size:13.5px;color:var(--ink-2);line-height:1.34}
.note b{color:var(--ink)}

.foot{margin-top:auto;display:flex;align-items:center;gap:18px;padding-top:14px}
.foot .msg{flex:1 1 auto;background:var(--brick-soft);border:1px solid var(--brick);border-radius:14px;padding:12px 21px;font-size:15px;color:var(--ink);line-height:1.34}
.foot .msg b{color:var(--brick)}
.brand{display:flex;align-items:center;gap:10px;color:var(--ink);flex:0 0 auto}
.brand b{font-family:'Cormorant Garamond',serif;font-weight:700;font-size:23px}
.brand .dot2{width:9px;height:9px;border-radius:50%%;background:var(--brick)}
.brand span{color:var(--taupe);font-size:15px}
</style></head><body>
<div class="wrap">
  <div class="top">
    <div>
      <div class="eyebrow">Календарь</div>
      <h2>Год по кругу: <i>где даты плавают</i></h2>
    </div>
    <div class="hint">Дуга — это разлёт даты по нашему календарю от года к году. <b>У Цинмина дуги почти нет</b>: он считается по солнцу, а не по луне.</div>
  </div>

  <div class="main">
    <div class="dial">
      <div class="face"></div>
      <div class="hoop"></div>
      <div class="hoop2"></div>
%(ringdiv)s
%(months)s
%(marks)s
      <div class="core">
        <div class="ch">农历</div>
        <div class="cp">nónglì</div>
        <div class="cd">лунно-солнечный календарь:<br>месяц начинается с новолуния</div>
      </div>
    </div>

    <div class="side">
      <div class="sh"><span></span><span>Праздник</span><span>Лунная дата</span><span>В нашем календаре</span></div>
%(legend)s
      <div class="note"><b>七夕 (qīxī) и 腊八节 (làbājié)</b> устроены так же: 7-й день 7-го месяца и 8-й день 12-го. <b>А 国庆节 1 октября и 劳动节 1 мая</b> — государственные даты, они стоят на месте, потому что считаются по нашему календарю.</div>
    </div>
  </div>

  <div class="foot">
    <div class="msg">Запоминать стоит <b>лунную дату, а не число в нашем календаре</b> — она у праздника одна</div>
    <div class="brand"><span class="dot2"></span><b>Kitai School</b><span>&middot; kitai-school.ru</span></div>
  </div>
</div>
</body></html>""" % dict(
    fonts=FONTS, vars=VARS,
    rings="\n".join(ring_css),
    ringdiv="\n".join("      " + d for d in ring_div),
    months="      " + months,
    marks="\n".join("      " + m for m in marks),
    legend=legend)

info = info.replace("HGT", "640")
open(S + "pr-info.html", "w", encoding="utf-8").write(info)
assert [a[0] for a in ARCS] == [l[0] for l in LEG], "нумерация круга и легенды разошлась"
print("ok, дуг на круге:", len(ARCS), "| строк в легенде:", len(LEG))
