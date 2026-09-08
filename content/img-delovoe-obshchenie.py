# -*- coding: utf-8 -*-
import math
S = "/tmp/claude-0/-home-user-Kitai-Shool/a463bfca-82a9-56fd-ae09-42a7257ff999/scratchpad/"

FONTS = ("<link href=\"https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,600;0,700;1,600"
         "&family=Inter:wght@400;500;600;700&family=Noto+Serif+SC:wght@600;700&display=swap\" rel=\"stylesheet\">")
VARS = (":root{--brick:#A41E3A;--brick-d:#841630;--brick-soft:#F7E6EB;--ink:#2C2420;--ink-2:#5A4F45;"
        "--taupe:#8B7D6B;--cream:#FAF7F2;--cream-2:#F3EDE3;--hair:#EAE3D8;--surface:#fff;"
        "--green:#1E7A46;--green-soft:#E3F6E9;--amber:#C08A2E;--amber-s:#FBF2DF;--blue:#2F5D8C;--blue-s:#E7EEF6}")

# ------------------------------------------------------------------ обложка
hero = """<!DOCTYPE html><html lang="ru"><head><meta charset="utf-8">
FONTS
<style>
VARS
*{margin:0;box-sizing:border-box}html,body{width:1200px;height:630px}
.card{width:1200px;height:630px;background:radial-gradient(1100px 700px at 80pc 18pc, #fff 0pc, var(--cream) 56pc, var(--cream-2) 100pc);display:flex;align-items:center;padding:0 56px 0 76px;position:relative;overflow:hidden;font-family:'Inter',sans-serif}
.card:before{content:"";position:absolute;left:0;top:0;bottom:0;width:12px;background:var(--brick)}
.seal{position:absolute;right:40px;top:26px;width:92px;height:92px;border:2.5px solid var(--brick);border-radius:14px;display:flex;align-items:center;justify-content:center;color:var(--brick);font-family:'Noto Serif SC',serif;font-weight:700;font-size:32px;opacity:.9}
.txt{flex:0 0 400px;max-width:400px}
.eyebrow{color:var(--brick);font-weight:700;font-size:19px;letter-spacing:.19em;text-transform:uppercase;margin-bottom:14px}
h1{font-family:'Cormorant Garamond',serif;font-weight:600;font-size:50px;line-height:1.04;color:var(--ink);letter-spacing:-.5px}
h1 i{font-style:italic;color:var(--brick)}
.sub{font-size:18.5px;color:var(--ink-2);line-height:1.42;max-width:22ch;margin-top:18px}
.brand{position:absolute;left:76px;bottom:34px;display:flex;align-items:center;gap:12px;color:var(--ink)}
.brand b{font-family:'Cormorant Garamond',serif;font-weight:700;font-size:28px}.brand .bdot{width:11px;height:11px;border-radius:50pc;background:var(--brick)}.brand span{color:var(--taupe);font-size:17px}

.art{flex:1 1 auto;position:relative;height:470px}
.pc{position:absolute;background:var(--surface);border:1px solid var(--hair);border-radius:18px;box-shadow:0 10px 28px rgba(44,36,32,.11)}
.back2{left:96px;top:70px;width:400px;height:186px;transform:rotate(-6deg);opacity:.62}
.back1{left:118px;top:88px;width:400px;height:186px;transform:rotate(-3deg);opacity:.82}
.front{left:140px;top:112px;width:420px;padding:22px 26px 24px;border-color:var(--brick)}
.front .han{font-family:'Noto Serif SC',serif;font-weight:700;font-size:46px;color:var(--ink);line-height:1.05;letter-spacing:2px}
.front .py{font-size:17px;color:var(--brick);font-weight:600;margin-top:8px;letter-spacing:.01em}
.front .ru{font-size:16px;color:var(--ink-2);margin-top:7px;padding-top:10px;border-top:1px solid var(--hair)}
.badge{position:absolute;left:398px;top:344px;background:var(--brick);color:#fff;border-radius:999px;padding:11px 22px;font-size:17px;font-weight:700;box-shadow:0 8px 22px rgba(164,30,58,.3)}
.badge span{font-family:'Cormorant Garamond',serif;font-size:23px;margin-right:5px}
.tag{position:absolute;left:140px;top:52px;font-size:12.5px;font-weight:700;letter-spacing:.15em;text-transform:uppercase;color:var(--taupe)}
</style></head><body>
<div class="card"><div class="seal">商务</div>
<div class="txt">
  <div class="eyebrow">Деловое общение</div>
  <h1>Китайский <i>для переговоров</i></h1>
  <div class="sub">Не словарь, а готовые реплики: их произносят не задумываясь</div>
</div>
<div class="art">
  <div class="tag">Фраза №3</div>
  <div class="pc back2"></div>
  <div class="pc back1"></div>
  <div class="pc front">
    <div class="han">请多关照</div>
    <div class="py">qǐng duō guānzhào</div>
    <div class="ru">«Прошу вашего расположения» — говорят о себе сразу после того, как представились</div>
  </div>
  <div class="badge"><span>50</span> фраз в наборе</div>
</div>
<div class="brand"><span class="bdot"></span><b>Kitai School</b><span>&middot; kitai-school.ru</span></div></div>
</body></html>"""
hero = hero.replace("FONTS", FONTS).replace("VARS", VARS).replace("pc%", "%").replace("pc", "%")
# вернуть класс .pc, который пострадал от замены
hero = hero.replace('class="% back2"', 'class="pc back2"').replace('class="% back1"', 'class="pc back1"')
hero = hero.replace('class="% front"', 'class="pc front"').replace('.%{position:absolute;background', '.pc{position:absolute;background')
open(S + "del-hero.html", "w", encoding="utf-8").write(hero)

# ------------------------------------------------------------------ инфографика: дуга мягкости отказа
ROWS = [
    ("我们内部再商量一下", "wǒmen nèibù zài shāngliang yíxià", "Мы обсудим это внутри",
     "«пока нет, но дверь открыта»", "#1E7A46"),
    ("这样恐怕不太方便", "zhèyàng kǒngpà bú tài fāngbiàn", "Так, боюсь, будет неудобно",
     "«скорее нет» — но повод назван мягко", "#4E8A3C"),
    ("我需要跟领导汇报", "wǒ xūyào gēn lǐngdǎo huìbào", "Мне нужно доложить руководству",
     "«решаю не я» — вы берёте паузу", "#C08A2E"),
    ("目前我们做不到", "mùqián wǒmen zuò bu dào", "Сейчас мы этого не можем",
     "твёрдое «нет», но с оговоркой «сейчас»", "#B4552F"),
    ("这个条件我们接受不了", "zhège tiáojiàn wǒmen jiēshòu bu liǎo", "Это условие мы принять не можем",
     "прямое «нет» по этому условию", "#A41E3A"),
]

# точки на дуге: полуокружность, центр (350, 250), радиус 210
pts = []
for i in range(5):
    ang = math.pi - (math.pi / 4) * i          # 180° → 0°
    x = 350 + 245 * math.cos(ang)
    y = 290 - 245 * math.sin(ang)
    pts.append((x, y))

dots = "".join(
    '<circle cx="%.1f" cy="%.1f" r="22" fill="%s"/>'
    '<text x="%.1f" y="%.1f" text-anchor="middle" font-family="Cormorant Garamond,serif" '
    'font-size="24" font-weight="700" fill="#fff">%d</text>'
    % (x, y, ROWS[i][4], x, y + 8.5, i + 1)
    for i, (x, y) in enumerate(pts))

rows_html = "".join(
    '<div class="pr"><span class="n" style="background:%s">%d</span>'
    '<div class="tx"><div class="hz">%s</div><div class="py">%s &middot; %s</div>'
    '<div class="hear">%s</div></div></div>' % (c, i + 1, hz, py, ru, hear)
    for i, (hz, py, ru, hear, c) in enumerate(ROWS))

info = """<!DOCTYPE html><html lang="ru"><head><meta charset="utf-8">
FONTS
<style>
VARS
*{margin:0;box-sizing:border-box}html,body{width:1200px;height:HEIGHTpx}
.wrap{width:1200px;height:HEIGHTpx;background:var(--cream);position:relative;overflow:hidden;font-family:'Inter',sans-serif;padding:20px 58px 16px 72px}
.wrap:before{content:"";position:absolute;left:0;top:0;bottom:0;width:14px;background:var(--brick)}
.top{display:flex;align-items:flex-end;justify-content:space-between;gap:24px}
.eyebrow{color:var(--brick);font-weight:700;font-size:16px;letter-spacing:.2em;text-transform:uppercase;margin-bottom:5px}
h2{font-family:'Cormorant Garamond',serif;font-weight:700;font-size:36px;color:var(--ink);line-height:1.02;letter-spacing:-.5px}
h2 i{font-style:italic;color:var(--brick)}
.hint{flex:0 0 316px;font-size:13.5px;color:var(--ink-2);line-height:1.34;border-left:3px solid var(--brick);padding-left:14px}
.hint b{color:var(--brick)}

.body{display:flex;gap:20px;margin-top:14px;align-items:stretch}
.gauge{flex:0 0 486px;background:#fff;border:1px solid var(--hair);border-radius:20px;box-shadow:0 5px 16px rgba(44,36,32,.06);display:flex;align-items:center;justify-content:center}
.ginner{position:relative;width:470px;height:380px}
.ginner svg{display:block}
.gl{position:absolute;font-size:12.5px;font-weight:700;letter-spacing:.13em;text-transform:uppercase}
.gl.a{left:0;top:318px;color:var(--green)}
.gl.b{right:0;top:318px;color:var(--brick)}
.gcap{position:absolute;left:0;right:0;top:222px;text-align:center}
.gcap b{display:block;font-family:'Cormorant Garamond',serif;font-size:31px;font-weight:700;color:var(--ink);line-height:1}
.gcap span{display:block;font-size:13px;color:var(--taupe);margin-top:5px}

.list{flex:1 1 auto;display:flex;flex-direction:column;gap:9px}
.pr{display:flex;gap:13px;background:#fff;border:1px solid var(--hair);border-radius:14px;padding:10px 16px 11px;box-shadow:0 3px 12px rgba(44,36,32,.05)}
.pr .n{flex:0 0 27px;height:27px;border-radius:50pc;color:#fff;font-family:'Cormorant Garamond',serif;font-weight:700;font-size:16px;display:flex;align-items:center;justify-content:center;margin-top:3px}
.tx{flex:1 1 auto}
.hz{font-family:'Noto Serif SC',serif;font-weight:700;font-size:21px;color:var(--ink);line-height:1.15;letter-spacing:1px}
.py{font-size:12.5px;color:var(--ink-2);margin-top:3px}
.hear{font-size:13.5px;color:var(--brick);font-weight:600;margin-top:4px}

.foot{margin-top:14px;display:flex;align-items:center;gap:16px}
.foot .msg{flex:1 1 auto;background:var(--brick-soft);border:1px solid var(--brick);border-radius:14px;padding:11px 20px;font-size:15.5px;color:var(--ink);line-height:1.34}
.foot .msg b{color:var(--brick)}
.brand{display:flex;align-items:center;gap:10px;color:var(--ink);flex:0 0 auto}
.brand b{font-family:'Cormorant Garamond',serif;font-weight:700;font-size:23px}.brand .dot{width:9px;height:9px;border-radius:50pc;background:var(--brick)}.brand span{color:var(--taupe);font-size:15px}
</style></head><body>
<div class="wrap">
  <div class="top">
    <div>
      <div class="eyebrow">Как отказать самому</div>
      <h2>Пять способов сказать «нет» — <i>разной силы</i></h2>
    </div>
    <div class="hint">Партнёр слышит не сам отказ, а <b>его температуру</b>. Выбирать формулу стоит осознанно, а не какую вспомнили.</div>
  </div>

  <div class="body">
    <div class="gauge">
     <div class="ginner">
      <svg width="470" height="380" viewBox="0 0 700 380">
        <defs><linearGradient id="g" x1="0" y1="0" x2="1" y2="0">
          <stop offset="0" stop-color="#1E7A46"/><stop offset="0.5" stop-color="#C08A2E"/><stop offset="1" stop-color="#A41E3A"/>
        </linearGradient></defs>
        <path d="M105 290 A 245 245 0 0 1 595 290" fill="none" stroke="url(#g)" stroke-width="17" stroke-linecap="round"/>
        DOTS
      </svg>
      <div class="gcap"><b>Шкала отказа</b><span>от мягкого к прямому</span></div>
      <div class="gl a">Мягко</div>
      <div class="gl b">Прямо</div>
     </div>
    </div>
    <div class="list">ROWS</div>
  </div>

  <div class="foot">
    <div class="msg">Резкое <b>不行</b> без формулы почти не используют: оно читается не как позиция, а как неуважение</div>
    <div class="brand"><span class="dot"></span><b>Kitai School</b><span>&middot; kitai-school.ru</span></div>
  </div>
</div>
</body></html>"""
info = (info.replace("FONTS", FONTS).replace("VARS", VARS)
            .replace("50pc", "50%").replace("HEIGHTpx", "640px")
            .replace("DOTS", dots).replace("ROWS", rows_html))
open(S + "del-info.html", "w", encoding="utf-8").write(info)
print("ok")
