# -*- coding: utf-8 -*-
# Картинки к статье «Красный цвет в китайской культуре»
# Обложка    — бумажная вырезка 囍 на стекле, на просвет
# Инфографика — красный конверт в разрезе и три правила
S = ("/tmp/claude-0/-home-user-Kitai-Shool/a463bfca-82a9-56fd-ae09-42a7257ff999/"
     "scratchpad/")

FONTS = ("<link href=\"https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,600;0,700;1,600"
         "&family=Inter:wght@400;500;600;700&family=Noto+Serif+SC:wght@600;700&display=swap\" rel=\"stylesheet\">")
VARS = (":root{--brick:#A41E3A;--brick-d:#841630;--brick-soft:#F7E6EB;--ink:#2C2420;--ink-2:#5A4F45;"
        "--taupe:#8B7D6B;--cream:#FAF7F2;--cream-2:#F3EDE3;--hair:#EAE3D8;--surface:#fff;"
        "--paper-red:#C4203F;--paper-red-d:#9B1830;--gold:#C9A227;--gold-2:#E8CE7A;"
        "--glass:#EAF0F2;--money:#F6EFE2}")

hero = """<!DOCTYPE html><html lang="ru"><head><meta charset="utf-8">
%s
<style>
%s
*{margin:0;box-sizing:border-box}html,body{width:1200px;height:630px}
.card{width:1200px;height:630px;background:radial-gradient(1050px 660px at 14%% 12%%, #fff 0%%, var(--cream) 52%%, var(--cream-2) 100%%);position:relative;overflow:hidden;font-family:'Inter',sans-serif;padding:52px 46px 0 72px;display:flex;justify-content:space-between}
.card:before{content:"";position:absolute;left:0;top:0;bottom:0;width:12px;background:var(--brick)}
.txt{flex:0 0 500px;padding-top:6px}
.eyebrow{color:var(--brick);font-weight:700;font-size:18px;letter-spacing:.19em;text-transform:uppercase;margin-bottom:13px}
h1{font-family:'Cormorant Garamond',serif;font-weight:600;font-size:46px;line-height:1.07;color:var(--ink);letter-spacing:-.4px}
h1 i{font-style:italic;color:var(--brick)}
.sub{font-size:18px;color:var(--ink-2);line-height:1.42;max-width:31ch;margin-top:16px}
.tip{display:inline-block;margin-top:22px;background:var(--surface);border:1px solid var(--hair);border-left:4px solid var(--brick);border-radius:13px;padding:13px 19px;font-size:15.5px;color:var(--ink-2);line-height:1.36;max-width:35ch}
.tip b{color:var(--ink)}

/* вырезка на стекле */
.scene{flex:0 0 476px;padding-top:44px;display:flex;flex-direction:column;align-items:center}
.window{position:relative;width:352px;height:352px;border-radius:10px;background:linear-gradient(145deg,#F7FAFB 0%%,var(--glass) 46%%,#DCE6E9 100%%);border:10px solid #EFE9DE;box-shadow:0 16px 30px rgba(44,36,32,.18), inset 0 0 0 1px rgba(255,255,255,.7);overflow:hidden}
.window:before{content:"";position:absolute;left:-60px;top:-120px;width:150px;height:620px;background:rgba(255,255,255,.55);transform:rotate(22deg)}
.window:after{content:"";position:absolute;left:120px;top:-140px;width:58px;height:620px;background:rgba(255,255,255,.35);transform:rotate(22deg)}
.paper{position:absolute;left:50%%;top:50%%;transform:translate(-50%%,-50%%) rotate(-3deg);width:218px;height:218px;background:linear-gradient(160deg,var(--paper-red),var(--paper-red-d));border-radius:6px;box-shadow:0 8px 18px rgba(100,16,32,.3);display:flex;align-items:center;justify-content:center}
.paper .cut{font-family:'Noto Serif SC',serif;font-size:132px;line-height:1;color:#FBE9D6;text-shadow:0 1px 0 rgba(255,255,255,.5)}
.paper .corner{position:absolute;width:15px;height:15px;background:var(--glass);border-radius:50%%}
.paper .c1{left:-7px;top:-7px}.paper .c2{right:-7px;top:-7px}
.paper .c3{left:-7px;bottom:-7px}.paper .c4{right:-7px;bottom:-7px}
.cap{margin-top:22px;text-align:center;font-size:16.5px;color:var(--ink-2);line-height:1.4;max-width:38ch}
.cap b{color:var(--ink)}
.brand{position:absolute;left:72px;bottom:28px;display:flex;align-items:center;gap:11px;color:var(--ink)}
.brand b{font-family:'Cormorant Garamond',serif;font-weight:700;font-size:26px}
.brand .bdot{width:10px;height:10px;border-radius:50%%;background:var(--brick)}
.brand span{color:var(--taupe);font-size:16px}
</style></head><body>
<div class="card">
  <div class="txt">
    <div class="eyebrow">Культура</div>
    <h1>Красный цвет <i>в китайской культуре</i></h1>
    <div class="sub">Цвет радости и защиты — от свадьбы до конверта с деньгами</div>
    <div class="tip"><b>囍 — «двойное счастье»:</b> знак из двух 喜, который вырезают из красной бумаги к свадьбе</div>
  </div>
  <div class="scene">
    <div class="window">
      <div class="paper">
        <div class="cut">囍</div>
      </div>
    </div>
    <div class="cap">Вырезку клеят на окно — <b>и знак виден с обеих сторон</b></div>
  </div>
  <div class="brand"><span class="bdot"></span><b>Kitai School</b><span>&middot; kitai-school.ru</span></div>
</div>
</body></html>""" % (FONTS, VARS)

open(S + "kras-hero.html", "w", encoding="utf-8").write(hero)

# --------------------------------------------------------------- инфографика
RULES = [
    ("Кто кому", "Старшие — младшим, женатые — неженатым, гости — молодожёнам",
     "顺序"),
    ("Какие суммы", "Избегают числа 4, ценят 8; на радостные поводы суммы обычно чётные",
     "数字"),
    ("Как передают", "Двумя руками; при дарителе конверт не открывают",
     "礼节"),
]

rules = "".join(
    '<div class="rl"><div class="rn"><span class="hn">%s</span></div>'
    '<div class="rb"><div class="rt">%s</div><div class="rd">%s</div></div></div>'
    % (han, title, text) for title, text, han in RULES)

info = """<!DOCTYPE html><html lang="ru"><head><meta charset="utf-8">
%(fonts)s
<style>
%(vars)s
*{margin:0;box-sizing:border-box}html,body{width:1200px;height:HGTpx}
.wrap{width:1200px;height:HGTpx;background:linear-gradient(180deg,#fff 0%%,var(--cream) 46%%,var(--cream-2) 100%%);font-family:'Inter',sans-serif;padding:32px 46px 28px;display:flex;flex-direction:column}
.top{display:flex;align-items:flex-end;justify-content:space-between;gap:30px;margin-bottom:22px}
.eyebrow{color:var(--brick);font-weight:700;font-size:14.5px;letter-spacing:.17em;text-transform:uppercase;margin-bottom:7px}
h2{font-family:'Cormorant Garamond',serif;font-weight:600;font-size:40px;line-height:1.07;color:var(--ink);letter-spacing:-.3px}
h2 i{font-style:italic;color:var(--brick)}
.hint{flex:0 0 372px;background:var(--surface);border:1px solid var(--hair);border-left:4px solid var(--brick);border-radius:12px;padding:12px 17px;font-size:14.5px;color:var(--ink-2);line-height:1.36}
.hint b{color:var(--ink)}

.main{display:flex;gap:34px;align-items:center;padding-bottom:40px}
.env{position:relative;flex:0 0 344px;height:252px}
.flap{position:absolute;left:100px;top:2px;width:244px;height:212px;background:var(--money);border:1px solid #E6DCC6;border-radius:8px;box-shadow:0 6px 14px rgba(44,36,32,.12)}
.flap:before{content:"";position:absolute;left:18px;top:26px;right:18px;height:5px;background:#E2D6BC;border-radius:3px}
.flap:after{content:"";position:absolute;left:18px;top:44px;right:60px;height:5px;background:#EBE1CB;border-radius:3px}
.bill{position:absolute;left:30px;top:70px;width:200px;height:80px;background:linear-gradient(135deg,#F7EED6,#EADCB8);border:2px solid var(--gold);border-radius:5px;box-shadow:0 3px 7px rgba(44,36,32,.12)}
.bill:before{content:"";position:absolute;left:12px;top:12px;width:44px;height:44px;border-radius:50%%;border:2px solid var(--gold);opacity:.6}
.bill:after{content:"";position:absolute;right:12px;top:22px;width:88px;height:5px;background:var(--gold-2);border-radius:3px;box-shadow:0 14px 0 var(--gold-2)}
.front{position:absolute;left:0;top:38px;width:206px;height:206px;border-radius:10px;background:linear-gradient(155deg,var(--paper-red),var(--paper-red-d));box-shadow:0 12px 24px rgba(100,16,32,.3);display:flex;align-items:center;justify-content:center}
.front:before{content:"";position:absolute;inset:14px;border:2px solid var(--gold-2);border-radius:6px;opacity:.75}
.front .fu{font-family:'Noto Serif SC',serif;font-size:84px;color:var(--gold-2);line-height:1;text-shadow:0 2px 3px rgba(80,10,24,.45)}
.ecap{position:absolute;left:0;bottom:-32px;width:344px;text-align:center;font-size:14.5px;color:var(--ink-2)}
.ecap b{color:var(--ink)}

.side{flex:1 1 auto;display:flex;flex-direction:column;gap:12px}
.rl{display:flex;align-items:center;gap:15px;background:var(--surface);border:1px solid var(--hair);border-radius:15px;padding:13px 19px;box-shadow:0 4px 12px rgba(44,36,32,.05)}
.rn{flex:0 0 54px;height:54px;border-radius:13px;background:var(--brick-soft);display:flex;align-items:center;justify-content:center}
.rn .hn{font-family:'Noto Serif SC',serif;font-size:22px;color:var(--brick-d)}
.rt{font-size:15.5px;font-weight:700;color:var(--ink)}
.rd{font-size:14.5px;color:var(--ink-2);line-height:1.34;margin-top:2px}

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
      <div class="eyebrow">红包</div>
      <h2>Конверт важнее <i>того, что внутри</i></h2>
    </div>
    <div class="hint">Деньги в Китае не передают из рук в руки: их кладут в красный конверт. <b>Сам конверт и есть пожелание</b> — цвет работает как часть подарка.</div>
  </div>

  <div class="main">
    <div class="env">
      <div class="flap"><div class="bill"></div></div>
      <div class="front"><div class="fu">福</div></div>
      <div class="ecap">Лицевая сторона и <b>то, что внутри</b></div>
    </div>
    <div class="side">%(rules)s</div>
  </div>

  <div class="foot">
    <div class="msg">Сумма зависит от повода и близости — <b>а вот числа выбирают всегда</b></div>
    <div class="brand"><span class="dot2"></span><b>Kitai School</b><span>&middot; kitai-school.ru</span></div>
  </div>
</div>
</body></html>""" % dict(fonts=FONTS, vars=VARS, rules=rules)

info = info.replace("HGT", "540")
open(S + "kras-info.html", "w", encoding="utf-8").write(info)
assert len(RULES) == 3, "правил не три"
print("ok, правил у конверта:", len(RULES))
