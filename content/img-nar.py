# -*- coding: utf-8 -*-
# Картинки к статье «Наречия в китайском»
# Обложка    — три бусины на шнурке: средняя закреплена узелками
# Инфографика — окно в строке предложения: куда встаёт наречие и куда нет
S = ("/tmp/claude-0/-home-user-Kitai-Shool/a463bfca-82a9-56fd-ae09-42a7257ff999/"
     "scratchpad/")

FONTS = ("<link href=\"https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,600;0,700;1,600"
         "&family=Inter:wght@400;500;600;700&family=Noto+Serif+SC:wght@600;700&display=swap\" rel=\"stylesheet\">")
VARS = (":root{--brick:#A41E3A;--brick-d:#841630;--brick-soft:#F7E6EB;--ink:#2C2420;--ink-2:#5A4F45;"
        "--taupe:#8B7D6B;--cream:#FAF7F2;--cream-2:#F3EDE3;--hair:#EAE3D8;--surface:#fff;"
        "--cord:#8B7D6B;--bead:#F0E7D8;--bead-2:#DFD2BC;--good:#1E7A46;--good-s:#E3F6E9;"
        "--bad:#B4332A;--bad-s:#FBE9E7}")

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

/* бусины на шнурке */
.scene{flex:0 0 474px;padding-top:76px;display:flex;flex-direction:column;align-items:center}
.string{position:relative;width:464px;height:200px}
.cord{position:absolute;left:0;right:0;top:94px;height:5px;background:linear-gradient(90deg,rgba(139,125,107,.25),var(--cord) 12%%,var(--cord) 88%%,rgba(139,125,107,.25));border-radius:3px}
.bead{position:absolute;top:36px;width:118px;height:118px;border-radius:50%%;background:radial-gradient(circle at 34%% 30%%, #fff, var(--bead) 52%%, var(--bead-2));box-shadow:0 10px 20px rgba(44,36,32,.2), inset 0 -4px 10px rgba(0,0,0,.08);display:flex;align-items:center;justify-content:center}
.bead .h{font-family:'Noto Serif SC',serif;font-size:50px;color:var(--ink);line-height:1}
.b1{left:22px}
.b3{right:22px}
.b2{left:173px;background:radial-gradient(circle at 34%% 30%%, #fff, var(--brick-soft) 48%%, #EFC9D3);box-shadow:0 10px 22px rgba(120,20,42,.26), inset 0 -4px 10px rgba(120,20,42,.1)}
.b2 .h{color:var(--brick)}
.knot{position:absolute;top:84px;width:19px;height:25px;border-radius:50%%;background:var(--cord);box-shadow:0 2px 4px rgba(44,36,32,.25)}
.k1{left:156px}
.k2{left:289px}
.fix{position:absolute;left:173px;top:164px;width:118px;text-align:center;font-size:13.5px;font-weight:700;color:var(--brick-d);letter-spacing:.04em}
.cap{margin-top:16px;text-align:center;font-size:16.5px;color:var(--ink-2);line-height:1.4;max-width:38ch}
.cap b{color:var(--ink)}
.brand{position:absolute;left:72px;bottom:28px;display:flex;align-items:center;gap:11px;color:var(--ink)}
.brand b{font-family:'Cormorant Garamond',serif;font-weight:700;font-size:26px}
.brand .bdot{width:10px;height:10px;border-radius:50%%;background:var(--brick)}
.brand span{color:var(--taupe);font-size:16px}
</style></head><body>
<div class="card">
  <div class="txt">
    <div class="eyebrow">Грамматика</div>
    <h1>Наречия <i>в китайском</i></h1>
    <div class="sub">У них в предложении одно место, и подвинуть его нельзя</div>
    <div class="tip"><b>很 не всегда значит «очень».</b> В 我很好 это просто связка, и фраза переводится «у меня всё хорошо»</div>
  </div>
  <div class="scene">
    <div class="string">
      <div class="cord"></div>
      <div class="knot k1"></div>
      <div class="knot k2"></div>
      <div class="bead b1"><span class="h">我</span></div>
      <div class="bead b2"><span class="h">很</span></div>
      <div class="bead b3"><span class="h">好</span></div>
      <div class="fix">закреплено</div>
    </div>
    <div class="cap">Крайние бусины двигаются, <b>средняя сидит между узелками</b></div>
  </div>
  <div class="brand"><span class="bdot"></span><b>Kitai School</b><span>&middot; kitai-school.ru</span></div>
</div>
</body></html>""" % (FONTS, VARS)

open(S + "nar-hero.html", "w", encoding="utf-8").write(hero)

# --------------------------------------------------------------- инфографика
SLOTS = [
    ("我", "подлежащее", False),
    ("наречие", "его место", True),
    ("不", "отрицание", False),
    ("想", "сказуемое", False),
    ("去", "дополнение", False),
]

assert sum(s[2] for s in SLOTS) == 1, "окно наречия отмечено не один раз"

slots = "".join(
    '<div class="sl%s"><div class="lb">%s</div><div class="vv">%s</div></div>'
    % (" win" if win else "", lab, han) for han, lab, win in SLOTS)

SUBS = [
    ("很", "степень", "我很想去 — мне очень хочется пойти"),
    ("也", "охват", "我也想去 — я тоже хочу пойти"),
    ("已经", "время", "我已经想去了 — мне уже захотелось пойти"),
]

subs = "".join(
    '<div class="sb"><span class="h">%s</span><div><div class="t">%s</div>'
    '<div class="d">%s</div></div></div>' % s for s in SUBS)

BAD = [
    ("很我好", "наречие ушло в начало — так нельзя"),
    ("我好很", "наречие после сказуемого — тоже нет"),
]

bad = "".join(
    '<div class="bd"><span class="x">&times;</span><span class="h">%s</span>'
    '<span class="d">%s</span></div>' % b for b in BAD)

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
.hint{flex:0 0 372px;background:var(--surface);border:1px solid var(--hair);border-left:4px solid var(--brick);border-radius:12px;padding:12px 17px;font-size:14.5px;color:var(--ink-2);line-height:1.36}
.hint b{color:var(--ink)}

.line{display:flex;gap:10px;align-items:stretch;justify-content:center}
.sl{flex:1 1 0;background:var(--surface);border:2px solid var(--hair);border-radius:14px;padding:12px 10px 13px;text-align:center;box-shadow:0 4px 11px rgba(44,36,32,.05)}
.sl .lb{font-size:12.5px;color:var(--taupe);letter-spacing:.03em}
.sl .vv{font-family:'Noto Serif SC',serif;font-size:34px;color:var(--ink);line-height:1.2;margin-top:3px}
.sl.win{border-color:var(--brick);background:var(--brick-soft);border-style:dashed}
.sl.win .lb{color:var(--brick-d);font-weight:700}
.sl.win .vv{font-family:'Inter',sans-serif;font-size:19px;font-weight:700;color:var(--brick);line-height:2.1}

.subs{display:flex;gap:12px;margin-top:16px}
.sb{flex:1 1 0;background:var(--surface);border:1px solid var(--hair);border-radius:14px;padding:11px 16px;display:flex;align-items:center;gap:13px;box-shadow:0 4px 10px rgba(44,36,32,.04)}
.sb .h{font-family:'Noto Serif SC',serif;font-size:27px;color:var(--brick-d);flex:0 0 auto}
.sb .t{font-size:13px;color:var(--taupe);letter-spacing:.03em}
.sb .d{font-size:14px;color:var(--ink);margin-top:1px;line-height:1.3}

.bads{display:flex;gap:12px;margin-top:14px}
.bd{flex:1 1 0;background:var(--bad-s);border:1px solid #E9BFB9;border-radius:14px;padding:11px 16px;display:flex;align-items:center;gap:12px}
.bd .x{color:var(--bad);font-size:22px;font-weight:700;line-height:1}
.bd .h{font-family:'Noto Serif SC',serif;font-size:23px;color:var(--bad);text-decoration:line-through}
.bd .d{font-size:14px;color:#6B3A34;line-height:1.3}

.foot{margin-top:auto;display:flex;align-items:center;gap:18px;padding-top:16px}
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
      <div class="eyebrow">Место в предложении</div>
      <h2>У наречия <i>одно окно</i></h2>
    </div>
    <div class="hint">Оно идёт <b>после подлежащего и перед сказуемым</b> — вместе с отрицанием, если оно есть. В начало фразы, как по-русски, наречие не выносят.</div>
  </div>

  <div class="line">%(slots)s</div>
  <div class="subs">%(subs)s</div>
  <div class="bads">%(bad)s</div>

  <div class="foot">
    <div class="msg">Меняется наречие — <b>окно остаётся на том же месте</b></div>
    <div class="brand"><span class="dot2"></span><b>Kitai School</b><span>&middot; kitai-school.ru</span></div>
  </div>
</div>
</body></html>""" % dict(fonts=FONTS, vars=VARS, slots=slots, subs=subs, bad=bad)

info = info.replace("HGT", "495")
open(S + "nar-info.html", "w", encoding="utf-8").write(info)
print("ok, слотов:", len(SLOTS), "| подстановок:", len(SUBS), "| запретов:", len(BAD))
