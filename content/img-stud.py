# -*- coding: utf-8 -*-
# Картинки к статье «Можно ли студентам работать в Китае»
# Обложка    — светофор: что запрещено, что с разрешения, что свободно
# Инфографика — три циферблата: лимиты часов
S = "/tmp/claude-0/-home-user-Kitai-Shool/a463bfca-82a9-56fd-ae09-42a7257ff999/scratchpad/"

FONTS = ("<link href=\"https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,600;0,700;1,600"
         "&family=Inter:wght@400;500;600;700&family=Noto+Serif+SC:wght@600;700&display=swap\" rel=\"stylesheet\">")
VARS = (":root{--brick:#A41E3A;--brick-d:#841630;--brick-soft:#F7E6EB;--ink:#2C2420;--ink-2:#5A4F45;"
        "--taupe:#8B7D6B;--cream:#FAF7F2;--cream-2:#F3EDE3;--hair:#EAE3D8;--surface:#fff;"
        "--green:#1E7A46;--green-s:#E3F6E9;--amber:#C08A2E;--amber-s:#FBF2DF;--blue:#2F5D8C;--blue-s:#E7EEF6;"
        "--case:#3A3733;--case-2:#2A2724;--red-on:#D8323F;--amb-on:#E7A92C;--grn-on:#2FA860}")

LIGHTS = [
    ("--red-on", "Нельзя", "трудоустройство, торговля, своё дело"),
    ("--amb-on", "С разрешения", "подработка при вузе в пределах лимита"),
    ("--grn-on", "Свободно", "практика по учебному плану вуза"),
]

lamps = "\n".join(
    '<div class="row">'
    '  <span class="lamp" style="background:var(%s);box-shadow:0 0 26px var(%s)"></span>'
    '  <div class="lab"><b>%s</b><span>%s</span></div>'
    '</div>' % (c, c, t, d) for c, t, d in LIGHTS)

hero = """<!DOCTYPE html><html lang="ru"><head><meta charset="utf-8">
%s
<style>
%s
*{margin:0;box-sizing:border-box}html,body{width:1200px;height:630px}
.card{width:1200px;height:630px;background:radial-gradient(1050px 660px at 14%% 12%%, #fff 0%%, var(--cream) 52%%, var(--cream-2) 100%%);position:relative;overflow:hidden;font-family:'Inter',sans-serif;padding:52px 46px 0 72px;display:flex;justify-content:space-between}
.card:before{content:"";position:absolute;left:0;top:0;bottom:0;width:12px;background:var(--brick)}
.txt{flex:0 0 496px;padding-top:4px}
.eyebrow{color:var(--brick);font-weight:700;font-size:18px;letter-spacing:.19em;text-transform:uppercase;margin-bottom:13px}
h1{font-family:'Cormorant Garamond',serif;font-weight:600;font-size:46px;line-height:1.06;color:var(--ink);letter-spacing:-.4px}
h1 i{font-style:italic;color:var(--brick)}
.sub{font-size:18px;color:var(--ink-2);line-height:1.42;max-width:31ch;margin-top:16px}
.note{display:inline-block;margin-top:22px;background:var(--surface);border:1px solid var(--hair);border-left:4px solid var(--brick);border-radius:13px;padding:13px 19px;font-size:15.5px;color:var(--ink-2);line-height:1.36;max-width:33ch}
.note b{color:var(--ink)}

/* светофор */
.tl{flex:0 0 560px;position:relative;height:482px;display:flex;align-items:flex-start;gap:26px;padding-top:6px}
.case{flex:0 0 132px;background:linear-gradient(170deg,var(--case),var(--case-2));border-radius:22px;padding:20px 0;display:flex;flex-direction:column;align-items:center;gap:26px;box-shadow:0 14px 30px rgba(44,36,32,.26)}
.hole{width:88px;height:88px;border-radius:50%%;background:#191714;display:flex;align-items:center;justify-content:center}
.rows{flex:1 1 auto;display:flex;flex-direction:column;gap:26px;padding-top:20px}
.row{height:88px;display:flex;align-items:center;gap:0}
.lamp{display:none}
.lab{display:flex;flex-direction:column;justify-content:center}
.lab b{font-size:19px;color:var(--ink);line-height:1.2}
.lab span{font-size:15px;color:var(--ink-2);margin-top:5px;line-height:1.3;max-width:30ch}
.brand{position:absolute;left:72px;bottom:28px;display:flex;align-items:center;gap:11px;color:var(--ink)}
.brand b{font-family:'Cormorant Garamond',serif;font-weight:700;font-size:26px}
.brand .bdot{width:10px;height:10px;border-radius:50%%;background:var(--brick)}
.brand span{color:var(--taupe);font-size:16px}
</style></head><body>
<div class="card">
  <div class="txt">
    <div class="eyebrow">Виза и работа</div>
    <h1>Можно ли студентам <i>работать в Китае</i></h1>
    <div class="sub">Учебная виза права работать не даёт: разрешена подработка при вузе, трудоустройство и коммерция запрещены прямо</div>
    <div class="note"><b>Опасен не размер заработка, а статус занятости:</b> неофициальные уроки за наличные — тоже работа</div>
  </div>
  <div class="tl">
    <div class="case">
      <div class="hole"><span style="width:72px;height:72px;border-radius:50%%;background:var(--red-on);box-shadow:0 0 28px var(--red-on)"></span></div>
      <div class="hole"><span style="width:72px;height:72px;border-radius:50%%;background:var(--amb-on);box-shadow:0 0 28px var(--amb-on)"></span></div>
      <div class="hole"><span style="width:72px;height:72px;border-radius:50%%;background:var(--grn-on);box-shadow:0 0 28px var(--grn-on)"></span></div>
    </div>
    <div class="rows">
%s
    </div>
  </div>
  <div class="brand"><span class="bdot"></span><b>Kitai School</b><span>&middot; kitai-school.ru</span></div>
</div>
</body></html>""" % (FONTS, VARS, lamps)

open(S + "sd-hero.html", "w", encoding="utf-8").write(hero)

# -------------------------------------------------------------- инфографика
DIALS = [
    ("8", "часов", "в неделю", "в обычное учебное время", 0.24, "#A41E3A", "#F7E6EB"),
    ("40", "часов", "в месяц", "суммарный потолок за месяц", 0.30, "#2F5D8C", "#E7EEF6"),
    ("16", "часов", "в неделю", "в зимние и летние каникулы", 0.46, "#1E7A46", "#E3F6E9"),
]

dials = "\n".join(
    '<div class="dl">'
    '  <div class="dial" style="background:conic-gradient(%s 0turn %.3fturn, #EDE6DA %.3fturn 1turn)">'
    '    <div class="hub"><b style="color:%s">%s</b><span>%s</span></div>'
    '  </div>'
    '  <div class="per" style="color:%s">%s</div>'
    '  <div class="what">%s</div>'
    '</div>' % (col, frac, frac, col, num, unit, col, per, what)
    for num, unit, per, what, frac, col, soft in DIALS)

info = """<!DOCTYPE html><html lang="ru"><head><meta charset="utf-8">
%s
<style>
%s
*{margin:0;box-sizing:border-box}html,body{width:1200px;height:HGTpx}
.wrap{width:1200px;height:HGTpx;background:linear-gradient(180deg,#fff 0%%,var(--cream) 46%%,var(--cream-2) 100%%);font-family:'Inter',sans-serif;padding:32px 46px 26px;display:flex;flex-direction:column}
.top{display:flex;align-items:flex-end;justify-content:space-between;gap:30px;margin-bottom:18px}
.eyebrow{color:var(--brick);font-weight:700;font-size:14.5px;letter-spacing:.17em;text-transform:uppercase;margin-bottom:7px}
h2{font-family:'Cormorant Garamond',serif;font-weight:600;font-size:40px;line-height:1.07;color:var(--ink);letter-spacing:-.3px}
h2 i{font-style:italic;color:var(--brick)}
.hint{flex:0 0 374px;background:var(--surface);border:1px solid var(--hair);border-left:4px solid var(--brick);border-radius:12px;padding:12px 17px;font-size:14.5px;color:var(--ink-2);line-height:1.36}
.hint b{color:var(--ink)}

.dials{display:flex;gap:22px;align-items:stretch}
.dl{flex:1 1 0;background:var(--surface);border:1px solid var(--hair);border-radius:14px;padding:20px 20px 18px;box-shadow:0 5px 14px rgba(44,36,32,.05);display:flex;flex-direction:column;align-items:center}
.dial{width:168px;height:168px;border-radius:50%%;display:flex;align-items:center;justify-content:center}
.hub{width:124px;height:124px;border-radius:50%%;background:#fff;display:flex;flex-direction:column;align-items:center;justify-content:center;box-shadow:inset 0 0 0 1px var(--hair)}
.hub b{font-family:'Cormorant Garamond',serif;font-size:46px;line-height:1}
.hub span{font-size:14px;color:var(--taupe);margin-top:2px}
.per{margin-top:15px;font-size:17px;font-weight:700;line-height:1.2}
.what{margin-top:8px;font-size:14.5px;color:var(--ink-2);line-height:1.34;text-align:center}

.foot{margin-top:auto;display:flex;align-items:center;gap:18px;padding-top:18px}
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
      <div class="eyebrow">Лимиты подработки</div>
      <h2>Сколько часов — <i>и ни часом больше</i></h2>
    </div>
    <div class="hint">По порядку 2022 года для подработки вне вуза нужен <b>действующий учебный вид на жительство со сроком более шести месяцев</b>. Сектора на циферблатах условные.</div>
  </div>

  <div class="dials">
%s
  </div>

  <div class="foot">
    <div class="msg">Превышение лимита юристы относят к нелегальной занятости: <b>штраф по закону — от 5 000 до 20 000 юаней</b></div>
    <div class="brand"><span class="dot2"></span><b>Kitai School</b><span>&middot; kitai-school.ru</span></div>
  </div>
</div>
</body></html>""" % (FONTS, VARS, dials)

info = info.replace("HGT", "560")
open(S + "sd-info.html", "w", encoding="utf-8").write(info)
print("ok")
