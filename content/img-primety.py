# -*- coding: utf-8 -*-
# Картинки к статье «Китайские приметы и суеверия»
# Обложка    — красный ромб с перевёрнутым 福
# Инфографика — четыре пары карточек, соединённые дугой созвучия
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
.card{width:1200px;height:630px;background:radial-gradient(1100px 680px at 16%% 8%%, #fff 0%%, var(--cream) 54%%, var(--cream-2) 100%%);position:relative;overflow:hidden;font-family:'Inter',sans-serif;display:flex;align-items:center;justify-content:space-between;padding:0 86px 0 72px}
.card:before{content:"";position:absolute;left:0;top:0;bottom:0;width:12px;background:var(--brick)}
.txt{flex:0 0 540px}
.eyebrow{color:var(--brick);font-weight:700;font-size:18px;letter-spacing:.19em;text-transform:uppercase;margin-bottom:12px}
h1{font-family:'Cormorant Garamond',serif;font-weight:600;font-size:53px;line-height:1.05;color:var(--ink);letter-spacing:-.5px;max-width:520px}
h1 i{font-style:italic;color:var(--brick)}
.sub{font-size:18px;color:var(--ink-2);line-height:1.42;max-width:32ch;margin-top:16px}
.counts{display:flex;gap:12px;margin-top:26px}
.cnt{background:var(--surface);border:1px solid var(--hair);border-radius:14px;padding:11px 15px;text-align:center;box-shadow:0 4px 14px rgba(44,36,32,.05)}
.cnt b{display:block;font-family:'Cormorant Garamond',serif;font-size:27px;font-weight:700;color:var(--brick);line-height:1.1}
.cnt b.han{font-family:'Noto Serif SC',serif;font-size:21px}
.cnt span{font-size:11.5px;color:var(--taupe);letter-spacing:.04em}
.brand{position:absolute;left:72px;bottom:32px;display:flex;align-items:center;gap:11px;color:var(--ink)}
.brand b{font-family:'Cormorant Garamond',serif;font-weight:700;font-size:26px}
.brand .bdot{width:10px;height:10px;border-radius:50%%;background:var(--brick)}
.brand span{color:var(--taupe);font-size:16px}

/* ромб с перевёрнутым 福 */
.art{flex:0 0 400px;display:flex;flex-direction:column;align-items:center}
.dia{width:250px;height:250px;background:linear-gradient(145deg,#B32442,#8E1630);transform:rotate(45deg);border-radius:14px;display:flex;align-items:center;justify-content:center;box-shadow:0 18px 44px rgba(44,36,32,.26);border:3px solid #D9A94E}
.dia .g{font-family:'Noto Serif SC',serif;font-weight:700;font-size:140px;line-height:1;color:#F7E3C0;transform:rotate(135deg)}
.cap{margin-top:52px;text-align:center;max-width:368px}
.cap .l{font-size:20px;font-weight:600;color:var(--ink-2)}
.cap .l b{font-family:'Noto Serif SC',serif;font-weight:700;font-size:25px}
.cap .l b{color:var(--brick)}
.cap .d{font-size:15px;color:var(--ink-2);line-height:1.42;margin-top:9px}
</style></head><body>
<div class="card">
  <div class="txt">
    <div class="eyebrow">Культура</div>
    <h1>Китайские приметы <i>и суеверия</i></h1>
    <div class="sub">Почти каждая держится на том, что одно слово звучит как другое. Знаешь механизм — объяснишь любую</div>
    <div class="counts">
      <div class="cnt"><b>3</b><span>МЕХАНИЗМА</span></div>
      <div class="cnt"><b class="han">岁岁平安</b><span>ЕСЛИ РАЗБИЛ</span></div>
      <div class="cnt"><b class="han">本命年</b><span>ГОД СВОЕГО ЗНАКА</span></div>
    </div>
  </div>
  <div class="art">
    <div class="dia"><span class="g">福</span></div>
    <div class="cap">
      <div class="l"><b>福倒</b> звучит как <b>福到</b></div>
      <div class="d">«Счастье перевёрнуто» — значит «счастье пришло». Поэтому знак и вешают вверх ногами</div>
    </div>
  </div>
  <div class="brand"><span class="bdot"></span><b>Kitai School</b><span>&middot; kitai-school.ru</span></div>
</div>
</body></html>""" % (FONTS, VARS)

open(S + "pr-hero.html", "w", encoding="utf-8").write(hero)

# -------------------------------------------------------------- инфографика
PAIRS = [
    ("碎", "suì", "разбиться", "岁", "suì", "год",
     "Разбил посуду — скажи <b>岁岁平安</b>", "«мира и покоя из года в год». Молчать хуже, чем разбить"),
    ("发", "fà", "волосы", "发", "fā", "разбогатеть",
     "В первый день года <b>не моют голову</b>", "знак один и тот же — выходит, что смываешь богатство"),
    ("福倒", "fú dào", "счастье перевёрнуто", "福到", "fú dào", "счастье пришло",
     "Знак 福 вешают <b>вверх ногами</b>", "единственная пара здесь, где созвучие полное"),
    ("四", "sì", "четыре", "死", "sǐ", "смерть",
     "Четвёрку <b>избегают</b> в номерах и этажах", "тоны разные, созвучие неточное — и всё равно работает"),
]

rows = "\n".join(
    '<div class="row">'
    '<div class="pair">'
    '<div class="cd"><span class="h">%s</span><span class="p">%s</span><span class="r">%s</span></div>'
    '<div class="lnk"><span class="arc"></span><span class="lb">звучит как</span></div>'
    '<div class="cd b"><span class="h">%s</span><span class="p">%s</span><span class="r">%s</span></div>'
    '</div>'
    '<div class="out"><div class="t">%s</div><div class="d">%s</div></div>'
    '</div>' % p for p in PAIRS)

info = """<!DOCTYPE html><html lang="ru"><head><meta charset="utf-8">
%s
<style>
%s
*{margin:0;box-sizing:border-box}html,body{width:1200px;height:HGTpx}
.wrap{width:1200px;height:HGTpx;background:linear-gradient(180deg,#fff 0%%,var(--cream) 46%%,var(--cream-2) 100%%);font-family:'Inter',sans-serif;padding:32px 46px 26px;display:flex;flex-direction:column}
.top{display:flex;align-items:flex-end;justify-content:space-between;gap:30px;margin-bottom:22px}
.eyebrow{color:var(--brick);font-weight:700;font-size:14.5px;letter-spacing:.17em;text-transform:uppercase;margin-bottom:7px}
h2{font-family:'Cormorant Garamond',serif;font-weight:600;font-size:40px;line-height:1.07;color:var(--ink);letter-spacing:-.3px}
h2 i{font-style:italic;color:var(--brick)}
.hint{flex:0 0 346px;background:var(--surface);border:1px solid var(--hair);border-left:4px solid var(--brick);border-radius:12px;padding:12px 17px;font-size:14.5px;color:var(--ink-2);line-height:1.36}
.hint b{color:var(--ink)}

.rows{display:flex;flex-direction:column;gap:12px}
.row{display:flex;align-items:center;gap:26px;background:var(--surface);border:1px solid var(--hair);border-radius:16px;padding:13px 22px;box-shadow:0 5px 16px rgba(44,36,32,.05)}
.pair{flex:0 0 436px;display:flex;align-items:center}
.cd{flex:0 0 152px;text-align:center;background:var(--cream);border:1px solid var(--hair);border-radius:12px;padding:9px 6px 10px}
.cd.b{background:var(--brick-soft);border-color:#E7C9D2}
.cd .h{display:block;font-family:'Noto Serif SC',serif;font-weight:700;font-size:30px;line-height:1.1;color:var(--ink)}
.cd.b .h{color:var(--brick)}
.cd .p{display:block;font-size:12.5px;color:var(--taupe);letter-spacing:.03em;margin-top:2px}
.cd .r{display:block;font-size:13px;color:var(--ink-2);margin-top:3px}
.lnk{flex:1 1 auto;display:flex;flex-direction:column;align-items:center;justify-content:flex-start;padding:0 6px}
.arc{display:block;width:96px;height:22px;border:2px dashed var(--taupe);border-bottom:none;border-radius:60px 60px 0 0;opacity:.75}
.lb{font-size:11.5px;color:var(--taupe);letter-spacing:.05em;margin-top:5px}
.out{flex:1 1 auto;border-left:1px solid var(--hair);padding-left:24px}
.out .t{font-size:17px;color:var(--ink);line-height:1.3}
.out .t b{color:var(--brick)}
.out .d{font-size:14px;color:var(--ink-2);line-height:1.4;margin-top:4px}

.foot{margin-top:auto;display:flex;align-items:center;gap:18px;padding-top:16px}
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
      <div class="eyebrow">Механизм созвучия</div>
      <h2>Примета начинается там, где <i>одно слово звучит как другое</i></h2>
    </div>
    <div class="hint">Слева — слово или действие, справа — то, с чем оно совпало по звучанию. <b>Из этого совпадения и вырастает правило</b>.</div>
  </div>

  <div class="rows">
%s
  </div>

  <div class="foot">
    <div class="msg">Поэтому примету, которую видишь впервые, часто можно <b>разгадать на слух</b> — достаточно спросить, на что это похоже</div>
    <div class="brand"><span class="dot2"></span><b>Kitai School</b><span>&middot; kitai-school.ru</span></div>
  </div>
</div>
</body></html>""" % (FONTS, VARS, rows)

info = info.replace("HGT", "800")
open(S + "pr-info.html", "w", encoding="utf-8").write(info)
print("ok")
