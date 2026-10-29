# -*- coding: utf-8 -*-
# Картинки к статье «Праздник фонарей»
# Обложка     — красный фонарь с подвешенной запиской-загадкой
# Инфографика — пятнадцать дней цикла и разрез двух шариков: 汤圆 против 元宵
S = ("/tmp/claude-0/-home-user-Kitai-Shool/a463bfca-82a9-56fd-ae09-42a7257ff999/"
     "scratchpad/")

FONTS = ("<link href=\"https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,600;0,700;1,600"
         "&family=Inter:wght@400;500;600;700&family=Noto+Serif+SC:wght@600;700&display=swap\" rel=\"stylesheet\">")
VARS = (":root{--brick:#A41E3A;--brick-d:#841630;--brick-soft:#F7E6EB;--ink:#2C2420;--ink-2:#5A4F45;"
        "--taupe:#8B7D6B;--cream:#FAF7F2;--cream-2:#F3EDE3;--hair:#EAE3D8;--surface:#fff;"
        "--lamp:#C8223F;--lamp-d:#8E1430;--lamp-l:#E2496A;--gold:#C9A227;--gold-d:#9A7A1A;"
        "--sky:#39597F;--sky-soft:#E7EDF4;--good:#1E7A46}")

ribs = "".join('<i style="left:%d%%"></i>' % x for x in (18, 34, 50, 66, 82))

hero = """<!DOCTYPE html><html lang="ru"><head><meta charset="utf-8">
%(fonts)s
<style>
%(vars)s
*{margin:0;box-sizing:border-box}html,body{width:1200px;height:630px}
.card{width:1200px;height:630px;background:radial-gradient(1050px 660px at 14%% 10%%, #fff 0%%, var(--cream) 52%%, var(--cream-2) 100%%);position:relative;overflow:hidden;font-family:'Inter',sans-serif;padding:76px 56px 0 72px;display:flex;justify-content:space-between}
.card:before{content:"";position:absolute;left:0;top:0;bottom:0;width:12px;background:var(--brick)}
.txt{flex:0 0 470px;padding-top:4px}
.eyebrow{color:var(--brick);font-weight:700;font-size:18px;letter-spacing:.19em;text-transform:uppercase;margin-bottom:13px}
h1{font-family:'Cormorant Garamond',serif;font-weight:600;font-size:45px;line-height:1.07;color:var(--ink);letter-spacing:-.4px}
h1 i{font-style:italic;color:var(--brick)}
.sub{font-size:18px;color:var(--ink-2);line-height:1.42;max-width:30ch;margin-top:16px}
.tip{display:inline-block;margin-top:22px;background:var(--surface);border:1px solid var(--hair);border-left:4px solid var(--brick);border-radius:13px;padding:13px 19px;font-size:15.5px;color:var(--ink-2);line-height:1.36;max-width:34ch}
.tip b{color:var(--ink)}

.scene{flex:0 0 500px;display:flex;flex-direction:column;align-items:center;padding-top:0}
.stage{position:relative;width:420px;height:368px;display:flex;justify-content:center}
.glow{position:absolute;left:50%%;top:96px;transform:translateX(-50%%);width:420px;height:300px;border-radius:50%%;background:radial-gradient(closest-side, rgba(226,110,70,.3), rgba(226,110,70,0) 72%%)}
.cord{position:absolute;left:50%%;top:0;width:2px;height:40px;background:var(--taupe);transform:translateX(-50%%)}
.lamp{position:absolute;left:50%%;top:40px;transform:translateX(-50%%);width:214px}
.capt,.capb{width:96px;height:17px;margin:0 auto;background:linear-gradient(180deg,var(--gold),var(--gold-d));border-radius:4px}
.body{position:relative;width:214px;height:168px;border-radius:50%%/46%%;background:radial-gradient(60%% 55%% at 36%% 32%%, var(--lamp-l), var(--lamp) 56%%, var(--lamp-d));box-shadow:0 14px 28px rgba(44,36,32,.26), inset -14px -10px 26px rgba(0,0,0,.18)}
.body i{position:absolute;top:4%%;bottom:4%%;width:2px;background:rgba(0,0,0,.14)}
.body .ch{position:absolute;left:0;right:0;top:50%%;transform:translateY(-50%%);text-align:center;font-family:'Noto Serif SC',serif;font-size:52px;color:#FBE9C8;letter-spacing:.06em}
.tassel{width:7px;height:44px;margin:0 auto;background:linear-gradient(180deg,var(--brick-d),var(--lamp));border-radius:0 0 4px 4px}
.slip{position:absolute;right:-6px;top:236px;width:138px;background:#FDF6E6;border:1px solid var(--hair);border-radius:9px;padding:11px 13px;box-shadow:0 8px 16px rgba(44,36,32,.18);transform:rotate(3deg)}
.slip:before{content:"";position:absolute;left:50%%;top:-40px;width:1px;height:40px;background:var(--taupe)}
.slip .l{font-size:11.5px;color:var(--taupe);letter-spacing:.09em;text-transform:uppercase;font-weight:700}
.slip .h{font-family:'Noto Serif SC',serif;font-size:21px;color:var(--ink);margin-top:3px}
.slip .p{font-size:12.5px;color:var(--ink-2);font-style:italic}
.slip .r{font-size:12.5px;color:var(--brick);font-weight:700;margin-top:2px}
.cap{margin-top:18px;text-align:center;font-size:16.5px;color:var(--ink-2);line-height:1.42;max-width:40ch}
.cap b{color:var(--ink)}
.brand{position:absolute;left:72px;bottom:28px;display:flex;align-items:center;gap:11px;color:var(--ink)}
.brand b{font-family:'Cormorant Garamond',serif;font-weight:700;font-size:26px}
.brand .bdot{width:10px;height:10px;border-radius:50%%;background:var(--brick)}
.brand span{color:var(--taupe);font-size:16px}
</style></head><body>
<div class="card">
  <div class="txt">
    <div class="eyebrow">Праздники</div>
    <h1>Праздник фонарей: <i>чем кончается Новый год</i></h1>
    <div class="sub">Пятнадцатый день первого лунного месяца — первое полнолуние года</div>
    <div class="tip"><b>На фонарях вешают загадки.</b> Отгадал — снимаешь записку и получаешь мелкий приз</div>
  </div>
  <div class="scene">
    <div class="stage">
      <div class="glow"></div>
      <div class="cord"></div>
      <div class="lamp">
        <div class="capt"></div>
        <div class="body">%(ribs)s<div class="ch">福</div></div>
        <div class="capb"></div>
        <div class="tassel"></div>
      </div>
      <div class="slip">
        <div class="l">загадка</div>
        <div class="h">灯谜</div>
        <div class="p">dēngmí</div>
        <div class="r">загадка на фонаре</div>
      </div>
    </div>
    <div class="cap">Фонарь, свет и круглая луна — <b>три вещи, вокруг которых собран весь вечер</b></div>
  </div>
  <div class="brand"><span class="bdot"></span><b>Kitai School</b><span>&middot; kitai-school.ru</span></div>
</div>
</body></html>""" % dict(fonts=FONTS, vars=VARS, ribs=ribs)

open(S + "fon-hero.html", "w", encoding="utf-8").write(hero)

# --------------------------------------------------------------- инфографика
DAYS = 15
dots = "".join(
    '<div class="dot %s"><span>%d</span></div>'
    % ("first" if i == 1 else "last" if i == DAYS else "", i)
    for i in range(1, DAYS + 1))

assert dots.count("first") == 1 and dots.count("last") == 1, "края цикла не по одному"
assert dots.count('class="dot') == 15, "дней не пятнадцать"

BALL = [
    ("汤圆", "tāngyuán", "юг", "Тесто замешивают и начинку в него заворачивают",
     "поверхность гладкая", "smooth"),
    ("元宵", "yuánxiāo", "север", "Твёрдую начинку катают в сухой рисовой муке",
     "слой за слоем, поверхность матовая", "rolled"),
]

assert len(BALL) == 2 and {b[2] for b in BALL} == {"юг", "север"}, "сторон не две"

balls = "".join(
    '<div class="bc"><div class="bl">'
    '<div class="ring %s"><div class="core"></div></div></div>'
    '<div class="bt"><div class="bh">%s <small>%s</small></div>'
    '<div class="bg">%s</div><div class="bd">%s</div><div class="bn">%s</div></div></div>'
    % (cls, han, py, reg, how, note) for han, py, reg, how, note, cls in BALL)

LEX = [
    ("灯笼", "dēnglong", "фонарь"),
    ("灯会", "dēnghuì", "фонарная ярмарка"),
    ("猜灯谜", "cāi dēngmí", "отгадывать загадки"),
    ("舞龙", "wǔlóng", "танец дракона"),
]

assert len(LEX) == 4, "слов не четыре"

lex = "".join(
    '<div class="lx"><div class="lh">%s</div><div class="lp">%s</div>'
    '<div class="lr">%s</div></div>' % w for w in LEX)

info = """<!DOCTYPE html><html lang="ru"><head><meta charset="utf-8">
%(fonts)s
<style>
%(vars)s
*{margin:0;box-sizing:border-box}html,body{width:1200px;height:620px}
.wrap{width:1200px;height:620px;background:linear-gradient(180deg,#fff 0%%,var(--cream) 46%%,var(--cream-2) 100%%);font-family:'Inter',sans-serif;padding:30px 46px 26px;display:flex;flex-direction:column}
.top{display:flex;align-items:flex-end;justify-content:space-between;gap:30px;margin-bottom:20px}
.eyebrow{color:var(--brick);font-weight:700;font-size:14.5px;letter-spacing:.17em;text-transform:uppercase;margin-bottom:7px}
h2{font-family:'Cormorant Garamond',serif;font-weight:600;font-size:38px;line-height:1.07;color:var(--ink);letter-spacing:-.3px}
h2 i{font-style:italic;color:var(--brick)}
.hint{flex:0 0 384px;background:var(--surface);border:1px solid var(--hair);border-left:4px solid var(--brick);border-radius:12px;padding:12px 17px;font-size:14.5px;color:var(--ink-2);line-height:1.36}
.hint b{color:var(--ink)}

.band{background:var(--surface);border:1px solid var(--hair);border-radius:14px;padding:16px 20px 14px;flex:0 0 auto}
.row{display:flex;align-items:center;gap:7px}
.dot{flex:1 1 0;height:34px;border-radius:9px;background:var(--cream-2);display:flex;align-items:center;justify-content:center;font-size:13.5px;color:var(--taupe);font-weight:600}
.dot.first{background:var(--brick-soft);color:var(--brick-d);border:2px solid var(--brick)}
.dot.last{background:var(--brick);color:#fff;border:2px solid var(--brick-d)}
.ends{display:flex;justify-content:space-between;margin-top:9px;font-size:14px}
.ends b{font-family:'Noto Serif SC',serif;font-size:18px;color:var(--ink);vertical-align:-1px}
.ends .l{color:var(--ink-2)}
.ends .r{color:var(--brick-d);font-weight:700}

.sep{display:flex;align-items:center;gap:16px;margin:18px 0 12px}
.sep span{font-size:15px;font-weight:700;color:var(--brick-d);white-space:nowrap}
.sep i{flex:1 1 auto;height:1px;background:var(--hair)}
.balls{display:flex;gap:16px}
.bc{flex:1 1 0;background:var(--surface);border:1px solid var(--hair);border-radius:14px;padding:14px 18px;display:flex;gap:16px;align-items:center}
.bl{flex:0 0 auto}
.ring{width:84px;height:84px;border-radius:50%%;display:flex;align-items:center;justify-content:center}
.ring.smooth{background:#F4F0E6;border:5px solid #E2D9C4}
.ring.rolled{background:repeating-radial-gradient(circle, #F4F0E6 0 5px, #E6DCC6 5px 9px);border:3px dashed #D8CCB0}
.core{width:38px;height:38px;border-radius:50%%;background:linear-gradient(145deg,#7A5A3A,#4E3822)}
.bt{flex:1 1 auto}
.bh{font-family:'Noto Serif SC',serif;font-size:25px;color:var(--ink);line-height:1.15}
.bh small{font-family:'Inter',sans-serif;font-size:13px;color:var(--ink-2);font-style:italic}
.bg{display:inline-block;margin-top:5px;font-size:12.5px;font-weight:700;color:var(--sky);background:var(--sky-soft);border-radius:999px;padding:3px 11px}
.bd{font-size:14px;color:var(--ink);margin-top:6px;line-height:1.3}
.bn{font-size:13px;color:var(--ink-2);margin-top:3px}

.lex{display:flex;gap:12px;margin-top:14px}
.lx{flex:1 1 0;background:var(--surface);border:1px solid var(--hair);border-radius:12px;padding:10px 15px 11px;text-align:center}
.lh{font-family:'Noto Serif SC',serif;font-size:21px;color:var(--ink);line-height:1.15}
.lp{font-size:12.5px;color:var(--ink-2);font-style:italic}
.lr{font-size:13.5px;color:var(--brick-d);font-weight:700;margin-top:2px}
.foot{margin-top:auto;display:flex;align-items:center;gap:18px;padding-top:14px}
.foot .msg{flex:1 1 auto;background:var(--brick-soft);border:1px solid var(--brick);border-radius:14px;padding:11px 21px;font-size:15px;color:var(--ink);line-height:1.34}
.foot .msg b{color:var(--brick)}
.brand{display:flex;align-items:center;gap:10px;color:var(--ink);flex:0 0 auto}
.brand b{font-family:'Cormorant Garamond',serif;font-weight:700;font-size:23px}
.brand .dot2{width:9px;height:9px;border-radius:50%%;background:var(--brick)}
.brand span{color:var(--taupe);font-size:15px}
</style></head><body>
<div class="wrap">
  <div class="top">
    <div>
      <div class="eyebrow">元宵节</div>
      <h2>Пятнадцатый день <i>и два шарика</i></h2>
    </div>
    <div class="hint">Праздник фонарей закрывает новогодний цикл. <b>А шарики, которые в этот вечер едят, на севере и на юге делают по-разному.</b></div>
  </div>

  <div class="band">
    <div class="row">%(dots)s</div>
    <div class="ends">
      <div class="l">первый день — <b>春节</b>, Новый год</div>
      <div class="r">пятнадцатый — <b>元宵节</b>, фонари</div>
    </div>
  </div>

  <div class="sep"><span>Одно блюдо, два способа</span><i></i></div>
  <div class="balls">%(balls)s</div>
  <div class="lex">%(lex)s</div>

  <div class="foot">
    <div class="msg">Начинка одна и та же — <b>разница в том, лепят тесто вокруг неё или катают в муке</b></div>
    <div class="brand"><span class="dot2"></span><b>Kitai School</b><span>&middot; kitai-school.ru</span></div>
  </div>
</div>
</body></html>""" % dict(fonts=FONTS, vars=VARS, dots=dots, balls=balls, lex=lex)

open(S + "fon-info.html", "w", encoding="utf-8").write(info)
print("ok | дней:", DAYS, "| шариков:", len(BALL), "| слов:", len(LEX))
