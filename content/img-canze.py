# -*- coding: utf-8 -*-
# Картинки к статье «Кто придумал китайские иероглифы»
# Обложка    — следы птицы на песке и знак рядом
# Инфографика — слои раскопа: где кончается бесспорное письмо
S = ("/tmp/claude-0/-home-user-Kitai-Shool/a463bfca-82a9-56fd-ae09-42a7257ff999/"
     "scratchpad/")

FONTS = ("<link href=\"https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,600;0,700;1,600"
         "&family=Inter:wght@400;500;600;700&family=Noto+Serif+SC:wght@600;700&display=swap\" rel=\"stylesheet\">")
VARS = (":root{--brick:#A41E3A;--brick-d:#841630;--brick-soft:#F7E6EB;--ink:#2C2420;--ink-2:#5A4F45;"
        "--taupe:#8B7D6B;--cream:#FAF7F2;--cream-2:#F3EDE3;--hair:#EAE3D8;--surface:#fff;"
        "--sand:#E8DCC6;--sand-2:#DBCBAE;--track:#9C8763;--soil-1:#D8C7A8;--soil-2:#C3AE88;"
        "--soil-3:#A8906A;--soil-4:#8C7554;--good:#1E7A46}")

hero = """<!DOCTYPE html><html lang="ru"><head><meta charset="utf-8">
%s
<style>
%s
*{margin:0;box-sizing:border-box}html,body{width:1200px;height:630px}
.card{width:1200px;height:630px;background:radial-gradient(1050px 660px at 14%% 12%%, #fff 0%%, var(--cream) 52%%, var(--cream-2) 100%%);position:relative;overflow:hidden;font-family:'Inter',sans-serif;padding:52px 46px 0 72px;display:flex;justify-content:space-between}
.card:before{content:"";position:absolute;left:0;top:0;bottom:0;width:12px;background:var(--brick)}
.txt{flex:0 0 500px;padding-top:6px}
.eyebrow{color:var(--brick);font-weight:700;font-size:18px;letter-spacing:.19em;text-transform:uppercase;margin-bottom:13px}
h1{font-family:'Cormorant Garamond',serif;font-weight:600;font-size:45px;line-height:1.07;color:var(--ink);letter-spacing:-.4px}
h1 i{font-style:italic;color:var(--brick)}
.sub{font-size:18px;color:var(--ink-2);line-height:1.42;max-width:31ch;margin-top:16px}
.tip{display:inline-block;margin-top:22px;background:var(--surface);border:1px solid var(--hair);border-left:4px solid var(--brick);border-radius:13px;padding:13px 19px;font-size:15.5px;color:var(--ink-2);line-height:1.36;max-width:35ch}
.tip b{color:var(--ink)}

/* следы на песке и знак */
.scene{flex:0 0 476px;padding-top:40px;display:flex;flex-direction:column;align-items:center}
.sand{position:relative;width:392px;height:330px;border-radius:16px;background:linear-gradient(170deg,#F2E9D8,var(--sand) 55%%,var(--sand-2));box-shadow:0 14px 28px rgba(44,36,32,.18), inset 0 2px 0 rgba(255,255,255,.5);overflow:hidden}
.sand:before{content:"";position:absolute;left:-40px;top:60px;width:500px;height:1px;background:rgba(140,117,84,.18)}
.sand:after{content:"";position:absolute;left:-40px;top:188px;width:500px;height:1px;background:rgba(140,117,84,.14)}
.tr{position:absolute;width:38px;height:38px}
.tr i{position:absolute;left:17px;top:0;width:3px;height:21px;background:var(--track);border-radius:2px;transform-origin:50%% 100%%}
.tr i:nth-child(1){transform:rotate(-38deg)}
.tr i:nth-child(2){transform:rotate(0deg)}
.tr i:nth-child(3){transform:rotate(38deg)}
.tr span{position:absolute;left:17px;top:19px;width:3px;height:12px;background:var(--track);border-radius:2px}
.han-box{position:absolute;right:28px;bottom:26px;background:rgba(255,255,255,.92);border:1px solid var(--hair);border-radius:14px;padding:12px 20px 14px;text-align:center;box-shadow:0 8px 16px rgba(44,36,32,.16)}
.han-box .h{font-family:'Noto Serif SC',serif;font-size:56px;line-height:1;color:var(--ink)}
.han-box .p{font-size:14px;color:var(--ink-2);font-style:italic;margin-top:4px}
.arrowc{position:absolute;right:196px;bottom:70px;font-size:26px;color:var(--taupe)}
.cap{margin-top:22px;text-align:center;font-size:16.5px;color:var(--ink-2);line-height:1.4;max-width:38ch}
.cap b{color:var(--ink)}
.brand{position:absolute;left:72px;bottom:28px;display:flex;align-items:center;gap:11px;color:var(--ink)}
.brand b{font-family:'Cormorant Garamond',serif;font-weight:700;font-size:26px}
.brand .bdot{width:10px;height:10px;border-radius:50%%;background:var(--brick)}
.brand span{color:var(--taupe);font-size:16px}
</style></head><body>
<div class="card">
  <div class="txt">
    <div class="eyebrow">История письменности</div>
    <h1>Кто придумал <i>китайские иероглифы</i></h1>
    <div class="sub">Предание называет имя, археология показывает другое</div>
    <div class="tip"><b>По легенде знаки подсмотрели в следах птиц.</b> У системы из тысяч знаков автора быть не может — и в статье видно, почему</div>
  </div>
  <div class="scene">
    <div class="sand">
TRACKS
      <span class="arrowc">&rarr;</span>
      <div class="han-box"><div class="h">鸟</div><div class="p">niǎo — птица</div></div>
    </div>
    <div class="cap">Красивое предание — <b>и три тысячи лет находок</b></div>
  </div>
  <div class="brand"><span class="bdot"></span><b>Kitai School</b><span>&middot; kitai-school.ru</span></div>
</div>
</body></html>""" % (FONTS, VARS)

TRACK_POS = [(44, 46, -14), (92, 94, 6), (52, 150, -8), (104, 198, 10), (58, 250, -4)]
tracks = "\n".join(
    '      <div class="tr" style="left:%dpx;top:%dpx;transform:rotate(%ddeg)">'
    '<i></i><i></i><i></i><span></span></div>' % t for t in TRACK_POS)
hero = hero.replace("TRACKS", tracks)

open(S + "canze-hero.html", "w", encoding="utf-8").write(hero)

# --------------------------------------------------------------- инфографика
LAYERS = [
    ("Сегодня", "печатный и рукописный знак", "今", "--soil-1",
     "та же система, что и три тысячи лет назад", False),
    ("Бронза", "надписи на ритуальных сосудах", "金", "--soil-2",
     "формы устойчивее, знаков больше", False),
    ("Кость", "гадательные надписи на костях и панцирях", "甲", "--soil-3",
     "древнейшее бесспорное письмо — более трёх тысяч лет", True),
    ("Керамика", "знаки на сосудах неолита", "?", "--soil-4",
     "старше, но письмом их большинство исследователей не считает", False),
]

assert len(LAYERS) == 4, "слоёв не четыре"
assert sum(l[5] for l in LAYERS) == 1, "граница письма отмечена не один раз"

layers = "\n".join(
    '      <div class="ly%s" style="background:var(%s)">'
    '<div class="lh"><span class="hn">%s</span></div>'
    '<div class="lb"><div class="lt">%s</div><div class="ld">%s</div></div>'
    '<div class="lx">%s</div></div>' % (" edge" if edge else "", col, han, name, what, note)
    for name, what, han, col, note, edge in LAYERS)

info = """<!DOCTYPE html><html lang="ru"><head><meta charset="utf-8">
%(fonts)s
<style>
%(vars)s
*{margin:0;box-sizing:border-box}html,body{width:1200px;height:HGTpx}
.wrap{width:1200px;height:HGTpx;background:linear-gradient(180deg,#fff 0%%,var(--cream) 46%%,var(--cream-2) 100%%);font-family:'Inter',sans-serif;padding:32px 46px 28px;display:flex;flex-direction:column}
.top{display:flex;align-items:flex-end;justify-content:space-between;gap:30px;margin-bottom:20px}
.eyebrow{color:var(--brick);font-weight:700;font-size:14.5px;letter-spacing:.17em;text-transform:uppercase;margin-bottom:7px}
h2{font-family:'Cormorant Garamond',serif;font-weight:600;font-size:40px;line-height:1.07;color:var(--ink);letter-spacing:-.3px}
h2 i{font-style:italic;color:var(--brick)}
.hint{flex:0 0 376px;background:var(--surface);border:1px solid var(--hair);border-left:4px solid var(--brick);border-radius:12px;padding:12px 17px;font-size:14.5px;color:var(--ink-2);line-height:1.36}
.hint b{color:var(--ink)}

.cut{border-radius:16px;overflow:hidden;box-shadow:0 8px 20px rgba(44,36,32,.12)}
.ly{display:flex;align-items:center;gap:20px;padding:14px 22px;position:relative}
.ly.edge{box-shadow:inset 0 3px 0 var(--brick), inset 0 -3px 0 var(--brick)}
.lh{flex:0 0 64px;height:64px;border-radius:12px;background:rgba(255,255,255,.78);display:flex;align-items:center;justify-content:center}
.lh .hn{font-family:'Noto Serif SC',serif;font-size:30px;color:var(--ink)}
.lb{flex:0 0 300px}
.lt{font-size:16px;font-weight:700;color:var(--ink)}
.ld{font-size:14px;color:#4A3F31;margin-top:2px}
.lx{flex:1 1 auto;font-size:14.5px;color:#3E3425;line-height:1.34}
.ly.edge .lx{font-weight:600;color:var(--brick-d)}

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
      <div class="eyebrow">Что под землёй</div>
      <h2>Автора нет — <i>есть слои</i></h2>
    </div>
    <div class="hint">Красным выделен слой, <b>ниже которого бесспорного письма уже нет</b>: находки есть, а письмо ли это — вопрос спорный.</div>
  </div>

  <div class="cut">
%(layers)s
  </div>

  <div class="foot">
    <div class="msg">На костях письмо <b>уже сложившееся</b> — значит, до него была долгая дорога</div>
    <div class="brand"><span class="dot2"></span><b>Kitai School</b><span>&middot; kitai-school.ru</span></div>
  </div>
</div>
</body></html>""" % dict(fonts=FONTS, vars=VARS, layers=layers)

info = info.replace("HGT", "620")
open(S + "canze-info.html", "w", encoding="utf-8").write(info)
print("ok, следов:", len(TRACK_POS), "| слоёв:", len(LAYERS))
