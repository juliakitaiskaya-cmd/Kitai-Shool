# -*- coding: utf-8 -*-
# Картинки к статье «Огонь на китайском (火)»
# Обложка    — спичечный коробок: знак на этикетке
# Инфографика — две позиции ключа: слева 火, внизу 灬
S = "/tmp/claude-0/-home-user-Kitai-Shool/a463bfca-82a9-56fd-ae09-42a7257ff999/scratchpad/"

FONTS = ("<link href=\"https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,600;0,700;1,600"
         "&family=Inter:wght@400;500;600;700&family=Noto+Serif+SC:wght@600;700&display=swap\" rel=\"stylesheet\">")
VARS = (":root{--brick:#A41E3A;--brick-d:#841630;--brick-soft:#F7E6EB;--ink:#2C2420;--ink-2:#5A4F45;"
        "--taupe:#8B7D6B;--cream:#FAF7F2;--cream-2:#F3EDE3;--hair:#EAE3D8;--surface:#fff;"
        "--green:#1E7A46;--green-s:#E3F6E9;--amber:#C08A2E;--amber-s:#FBF2DF;--blue:#2F5D8C;--blue-s:#E7EEF6;"
        "--box:#B5442E;--box-2:#8E3222;--kraft:#DCC9A9;--kraft-2:#C6B08C;--wood:#E6D3AE;--flame:#E58E2A}")

hero = """<!DOCTYPE html><html lang="ru"><head><meta charset="utf-8">
%s
<style>
%s
*{margin:0;box-sizing:border-box}html,body{width:1200px;height:630px}
.card{width:1200px;height:630px;background:radial-gradient(1050px 660px at 14%% 12%%, #fff 0%%, var(--cream) 52%%, var(--cream-2) 100%%);position:relative;overflow:hidden;font-family:'Inter',sans-serif;padding:52px 46px 0 72px;display:flex;justify-content:space-between}
.card:before{content:"";position:absolute;left:0;top:0;bottom:0;width:12px;background:var(--brick)}
.txt{flex:0 0 510px;padding-top:4px}
.eyebrow{color:var(--brick);font-weight:700;font-size:18px;letter-spacing:.19em;text-transform:uppercase;margin-bottom:13px}
h1{font-family:'Cormorant Garamond',serif;font-weight:600;font-size:46px;line-height:1.06;color:var(--ink);letter-spacing:-.4px}
h1 i{font-style:italic;color:var(--brick)}
.sub{font-size:18px;color:var(--ink-2);line-height:1.42;max-width:32ch;margin-top:16px}
.note{display:inline-block;margin-top:22px;background:var(--surface);border:1px solid var(--hair);border-left:4px solid var(--brick);border-radius:13px;padding:13px 19px;font-size:15.5px;color:var(--ink-2);line-height:1.36;max-width:34ch}
.note b{color:var(--ink)}

/* спичечный коробок */
.scene{flex:0 0 520px;position:relative;height:482px;display:flex;flex-direction:column;align-items:center;justify-content:flex-start;padding-top:60px}
.match{position:absolute;left:150px;top:18px;width:11px;height:112px;background:linear-gradient(180deg,var(--wood),#D2BC92);border-radius:3px;transform:rotate(16deg);box-shadow:0 4px 9px rgba(44,36,32,.18)}
.match:before{content:"";position:absolute;left:-4px;top:-16px;width:19px;height:22px;border-radius:50%%;background:radial-gradient(circle at 40%% 35%%, #E8762A, #A5301C)}
.box{width:356px;height:242px;border-radius:12px;background:linear-gradient(168deg,var(--box),var(--box-2));box-shadow:0 18px 34px rgba(90,40,28,.3);padding:20px;position:relative}
.box:after{content:"";position:absolute;left:0;right:0;bottom:16px;height:26px;background:repeating-linear-gradient(45deg,rgba(0,0,0,.26) 0 4px,rgba(255,255,255,.06) 4px 8px)}
.label{height:166px;border-radius:8px;background:linear-gradient(170deg,var(--kraft),var(--kraft-2));display:flex;flex-direction:column;align-items:center;justify-content:center;box-shadow:inset 0 0 0 2px rgba(120,90,60,.3)}
.label .han{font-family:'Noto Serif SC',serif;font-size:92px;color:#43301F;line-height:1}
.label .py{font-size:19px;color:#6B5134;margin-top:6px;font-style:italic}
.cap{margin-top:30px;text-align:center;font-size:16.5px;color:var(--ink-2);line-height:1.42;max-width:38ch}
.cap b{color:var(--ink)}
.brand{position:absolute;left:72px;bottom:28px;display:flex;align-items:center;gap:11px;color:var(--ink)}
.brand b{font-family:'Cormorant Garamond',serif;font-weight:700;font-size:26px}
.brand .bdot{width:10px;height:10px;border-radius:50%%;background:var(--brick)}
.brand span{color:var(--taupe);font-size:16px}
</style></head><body>
<div class="card">
  <div class="txt">
    <div class="eyebrow">Иероглифы</div>
    <h1>Огонь <i>на китайском</i></h1>
    <div class="sub">Четыре черты, рисунок пламени — и один из самых заметных ключей в письменности</div>
    <div class="note"><b>Внизу знака огонь выглядит иначе:</b> 火 превращается в четыре точки 灬 — как в 热 и 煮</div>
  </div>
  <div class="scene">
    <div class="match"></div>
    <div class="box">
      <div class="label"><span class="han">火</span><span class="py">huǒ · огонь</span></div>
    </div>
    <div class="cap">Знак учат на первых занятиях, а встречают потом <b>в десятках слов — от 火车 до 火锅</b></div>
  </div>
  <div class="brand"><span class="bdot"></span><b>Kitai School</b><span>&middot; kitai-school.ru</span></div>
</div>
</body></html>""" % (FONTS, VARS)

open(S + "og-hero.html", "w", encoding="utf-8").write(hero)

# -------------------------------------------------------------- инфографика
LEFT = [("烧", "shāo", "жечь"), ("灯", "dēng", "лампа"), ("炒", "chǎo", "жарить"),
        ("烤", "kǎo", "запекать")]
BOTTOM = [("热", "rè", "горячий"), ("煮", "zhǔ", "варить"), ("照", "zhào", "светить"),
          ("煎", "jiān", "жарить на сковороде")]


def ex(items):
    return "\n".join(
        '<div class="ex"><span class="han">%s</span><span class="py">%s</span>'
        '<span class="ru">%s</span></div>' % i for i in items)


info = """<!DOCTYPE html><html lang="ru"><head><meta charset="utf-8">
%s
<style>
%s
*{margin:0;box-sizing:border-box}html,body{width:1200px;height:HGTpx}
.wrap{width:1200px;height:HGTpx;background:linear-gradient(180deg,#fff 0%%,var(--cream) 46%%,var(--cream-2) 100%%);font-family:'Inter',sans-serif;padding:32px 46px 32px;display:flex;flex-direction:column}
.top{display:flex;align-items:flex-end;justify-content:space-between;gap:30px;margin-bottom:20px}
.eyebrow{color:var(--brick);font-weight:700;font-size:14.5px;letter-spacing:.17em;text-transform:uppercase;margin-bottom:7px}
h2{font-family:'Cormorant Garamond',serif;font-weight:600;font-size:40px;line-height:1.07;color:var(--ink);letter-spacing:-.3px}
h2 i{font-style:italic;color:var(--brick)}
.hint{flex:0 0 380px;background:var(--surface);border:1px solid var(--hair);border-left:4px solid var(--brick);border-radius:12px;padding:12px 17px;font-size:14.5px;color:var(--ink-2);line-height:1.36}
.hint b{color:var(--ink)}

.rows{display:flex;flex-direction:column;gap:16px}
.row{display:flex;align-items:center;gap:26px;background:var(--surface);border:1px solid var(--hair);border-radius:16px;padding:18px 24px;box-shadow:0 5px 14px rgba(44,36,32,.05)}
.cell{flex:0 0 136px;height:136px;border:2px dashed #CFC5B6;border-radius:10px;position:relative;background:#FCFAF6}
.zone{position:absolute;background:var(--brick-soft);border:2px solid var(--brick);border-radius:7px;display:flex;align-items:center;justify-content:center;font-family:'Noto Serif SC',serif;color:var(--brick)}
.zone.l{left:6px;top:6px;bottom:6px;width:44px;font-size:26px}
.zone.b{left:6px;right:6px;bottom:6px;height:38px;font-size:22px;letter-spacing:4px}
.lab{flex:0 0 206px}
.lab b{display:block;font-size:19px;color:var(--ink);line-height:1.25}
.lab span{display:block;font-size:14.5px;color:var(--ink-2);margin-top:6px;line-height:1.36}
.exs{flex:1 1 auto;display:flex;gap:12px}
.ex{flex:1 1 0;background:var(--cream);border:1px solid var(--hair);border-radius:11px;padding:11px 8px;text-align:center}
.ex .han{display:block;font-family:'Noto Serif SC',serif;font-size:30px;color:var(--ink);line-height:1.1}
.ex .py{display:block;font-size:13px;color:var(--taupe);font-style:italic;margin-top:4px}
.ex .ru{display:block;font-size:13.5px;color:var(--ink-2);margin-top:2px}

.foot{margin-top:auto;display:flex;align-items:center;gap:18px;padding-top:20px}
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
      <div class="eyebrow">Один ключ, две позиции</div>
      <h2>Слева 火, <i>внизу четыре точки</i></h2>
    </div>
    <div class="hint">Четыре точки внизу — <b>не всегда огонь</b>: в традиционном 馬 это ноги коня. Позицию стоит проверять по смыслу слова.</div>
  </div>

  <div class="rows">
    <div class="row">
      <div class="cell"><div class="zone l">火</div></div>
      <div class="lab"><b>Слева</b><span>Знак сжимается по ширине, но форму сохраняет</span></div>
      <div class="exs">
%s
      </div>
    </div>
    <div class="row">
      <div class="cell"><div class="zone b">灬</div></div>
      <div class="lab"><b>Внизу</b><span>Превращается в четыре точки — 四点底</span></div>
      <div class="exs">
%s
      </div>
    </div>
  </div>

  <div class="foot">
    <div class="msg">Узнавать ключ в обеих позициях <b>полезнее, чем учить знаки по одному</b></div>
    <div class="brand"><span class="dot2"></span><b>Kitai School</b><span>&middot; kitai-school.ru</span></div>
  </div>
</div>
</body></html>""" % (FONTS, VARS, ex(LEFT), ex(BOTTOM))

info = info.replace("HGT", "582")
open(S + "og-info.html", "w", encoding="utf-8").write(info)
print("ok")
