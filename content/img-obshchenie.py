# -*- coding: utf-8 -*-
# Новые картинки к расширенной статье «Как общаются китайцы»
# Обложка    — айсберг: слова над водой, смысл под водой
# Инфографика — весы: слова на одной чаше, ситуация на другой
S = "/tmp/claude-0/-home-user-Kitai-Shool/a463bfca-82a9-56fd-ae09-42a7257ff999/scratchpad/"

FONTS = ("<link href=\"https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,600;0,700;1,600"
         "&family=Inter:wght@400;500;600;700&family=Noto+Serif+SC:wght@600;700&display=swap\" rel=\"stylesheet\">")
VARS = (":root{--brick:#A41E3A;--brick-d:#841630;--brick-soft:#F7E6EB;--ink:#2C2420;--ink-2:#5A4F45;"
        "--taupe:#8B7D6B;--cream:#FAF7F2;--cream-2:#F3EDE3;--hair:#EAE3D8;--surface:#fff;"
        "--green:#1E7A46;--green-soft:#E3F6E9;--amber:#C08A2E;--amber-s:#FBF2DF;--blue:#2F5D8C;--blue-s:#E7EEF6;"
        "--sea:#3E6A8C;--sea-d:#2A4C66;--sea-l:#CFE0EC}")

# ------------------------------------------------------------------ обложка
hero = """<!DOCTYPE html><html lang="ru"><head><meta charset="utf-8">
%s
<style>
%s
*{margin:0;box-sizing:border-box}html,body{width:1200px;height:630px}
.card{width:1200px;height:630px;background:radial-gradient(1100px 680px at 15%% 10%%, #fff 0%%, var(--cream) 55%%, var(--cream-2) 100%%);position:relative;overflow:hidden;font-family:'Inter',sans-serif;display:flex;align-items:center;justify-content:space-between;padding:0 64px 0 72px}
.card:before{content:"";position:absolute;left:0;top:0;bottom:0;width:12px;background:var(--brick)}
.txt{flex:0 0 468px}
.eyebrow{color:var(--brick);font-weight:700;font-size:18px;letter-spacing:.19em;text-transform:uppercase;margin-bottom:12px}
h1{font-family:'Cormorant Garamond',serif;font-weight:600;font-size:52px;line-height:1.05;color:var(--ink);letter-spacing:-.4px}
h1 i{font-style:italic;color:var(--brick)}
.sub{font-size:18px;color:var(--ink-2);line-height:1.42;max-width:30ch;margin-top:16px}
.cnt{display:inline-flex;align-items:center;gap:11px;margin-top:24px;background:var(--surface);border:1px solid var(--hair);border-radius:14px;padding:11px 17px;box-shadow:0 4px 14px rgba(44,36,32,.05)}
.cnt b{font-family:'Noto Serif SC',serif;font-weight:700;font-size:23px;color:var(--brick);line-height:1}
.cnt span{font-size:14.5px;color:var(--ink-2)}
.brand{position:absolute;left:72px;bottom:32px;display:flex;align-items:center;gap:11px;color:var(--ink)}
.brand b{font-family:'Cormorant Garamond',serif;font-weight:700;font-size:26px}
.brand .bdot{width:10px;height:10px;border-radius:50%%;background:var(--brick)}
.brand span{color:var(--taupe);font-size:16px}

/* айсберг */
.sea{flex:0 0 536px;height:470px;position:relative;border-radius:20px;overflow:hidden;border:1px solid var(--hair);box-shadow:0 18px 40px rgba(44,36,32,.18);background:linear-gradient(180deg,#FBF7F0 0%%,#F3EFE6 27%%,var(--sea-l) 27%%,#9FBDD2 62%%,var(--sea) 100%%)}
.waterline{position:absolute;left:0;right:0;top:27%%;height:2px;background:rgba(62,106,140,.55)}
.wl-lab{position:absolute;right:14px;top:calc(27%% - 22px);font-size:11px;letter-spacing:.14em;color:#4A6B82;font-weight:700}
.tip{position:absolute;left:50%%;top:74px;transform:translateX(-50%%);width:0;height:0;border-left:78px solid transparent;border-right:78px solid transparent;border-bottom:54px solid #FFFFFF;filter:drop-shadow(0 4px 10px rgba(44,36,32,.18))}
.tip-txt{position:absolute;left:50%%;top:18px;transform:translateX(-50%%);text-align:center;width:260px}
.tip-txt b{display:block;font-family:'Noto Serif SC',serif;font-weight:700;font-size:25px;color:var(--ink);line-height:1.1}
.tip-txt span{display:block;font-size:13px;color:var(--ink-2);margin-top:2px}
.deep{position:absolute;left:50%%;top:calc(27%% + 2px);transform:translateX(-50%%);width:388px;height:300px;background:linear-gradient(180deg,rgba(255,255,255,.93) 0%%,rgba(240,246,250,.86) 100%%);clip-path:polygon(22%% 0%%, 78%% 0%%, 100%% 58%%, 62%% 100%%, 26%% 96%%, 0%% 46%%);display:flex;flex-direction:column;align-items:center;justify-content:center;padding:26px 34px;text-align:center}
.deep .k{font-size:11px;font-weight:700;letter-spacing:.14em;color:var(--brick);margin-bottom:10px}
.deep .l{font-size:16.5px;color:var(--ink);line-height:1.42}
.deep .l b{color:var(--brick)}
</style></head><body>
<div class="card">
  <div class="txt">
    <div class="eyebrow">Речевой этикет</div>
    <h1>Как общаться <i>в Китае</i></h1>
    <div class="sub">Прямого «нет» вы почти не услышите. Ответ передают формой, а не словом</div>
    <div class="cnt"><b>听话听音</b><span>слушая речь, слушай её звучание</span></div>
  </div>
  <div class="sea">
    <div class="waterline"></div>
    <div class="wl-lab">СКАЗАНО</div>
    <div class="tip"></div>
    <div class="tip-txt"><b>我再看看</b><span>«я ещё посмотрю»</span></div>
    <div class="deep">
      <div class="k">ЧТО ЭТО ЗНАЧИТ</div>
      <div class="l">Срока нет, следующего шага нет, разговор свернули — <b>значит, ответ уже дан</b></div>
    </div>
  </div>
  <div class="brand"><span class="bdot"></span><b>Kitai School</b><span>&middot; kitai-school.ru</span></div>
</div>
</body></html>""" % (FONTS, VARS)

open(S + "ob-hero.html", "w", encoding="utf-8").write(hero)

# -------------------------------------------------------------- инфографика
WEIGHTS = [
    ("Назвали срок?", "нет"),
    ("Куда пошёл разговор?", "в сторону"),
    ("Что было через неделю?", "тишина"),
]

ws = "\n".join(
    '<div class="w"><span class="q">%s</span><span class="a">%s</span></div>' % w for w in WEIGHTS)

info = """<!DOCTYPE html><html lang="ru"><head><meta charset="utf-8">
%s
<style>
%s
*{margin:0;box-sizing:border-box}html,body{width:1200px;height:HGTpx}
.wrap{width:1200px;height:HGTpx;background:linear-gradient(180deg,#fff 0%%,var(--cream) 46%%,var(--cream-2) 100%%);font-family:'Inter',sans-serif;padding:32px 46px 26px;display:flex;flex-direction:column}
.top{display:flex;align-items:flex-end;justify-content:space-between;gap:30px;margin-bottom:10px}
.eyebrow{color:var(--brick);font-weight:700;font-size:14.5px;letter-spacing:.17em;text-transform:uppercase;margin-bottom:7px}
h2{font-family:'Cormorant Garamond',serif;font-weight:600;font-size:40px;line-height:1.07;color:var(--ink);letter-spacing:-.3px}
h2 i{font-style:italic;color:var(--brick)}
.hint{flex:0 0 352px;background:var(--surface);border:1px solid var(--hair);border-left:4px solid var(--brick);border-radius:12px;padding:12px 17px;font-size:14.5px;color:var(--ink-2);line-height:1.36}
.hint b{color:var(--ink)}

/* весы: правая чаша тяжелее, поэтому коромысло опускается вправо */
.scales{position:relative;height:338px;margin-top:6px}
.beam{position:absolute;left:50%%;top:58px;transform:translateX(-50%%) rotate(6deg);width:700px;height:10px;background:linear-gradient(180deg,#5A4F45,#3A322C);border-radius:6px;box-shadow:0 5px 12px rgba(44,36,32,.18)}
.pivot{position:absolute;left:50%%;top:36px;transform:translateX(-50%%);width:0;height:0;border-left:24px solid transparent;border-right:24px solid transparent;border-bottom:32px solid #5A4F45}
.post{position:absolute;left:50%%;top:66px;transform:translateX(-50%%);width:15px;height:234px;background:linear-gradient(180deg,#5A4F45,#3A322C)}
.base{position:absolute;left:50%%;top:296px;transform:translateX(-50%%);width:250px;height:15px;background:#3A322C;border-radius:8px}
.rope{position:absolute;width:2px;background:#6E6155}
.rope.l{left:204px;top:24px;height:28px}
.rope.r{left:904px;top:98px;height:32px}
.knot{position:absolute;width:12px;height:12px;border-radius:50%%;background:#5A4F45}
.knot.l{left:199px;top:18px}
.knot.r{left:899px;top:92px}

.pan{position:absolute;width:380px;background:var(--surface);border:1px solid var(--hair);border-radius:16px;box-shadow:0 12px 26px rgba(44,36,32,.13);padding:14px 20px 16px}
.pan .t{font-size:11.5px;font-weight:700;letter-spacing:.13em;color:var(--taupe);margin-bottom:9px}
.pan.left{left:14px;top:52px}
.pan.right{left:714px;top:130px;border-color:var(--brick)}
.pan.right .t{color:var(--brick)}

.say{display:flex;align-items:baseline;gap:12px;flex-wrap:wrap}
.say .h{font-family:'Noto Serif SC',serif;font-weight:700;font-size:32px;color:var(--ink);line-height:1.1}
.say .p{font-size:13.5px;color:var(--taupe)}
.say2{font-size:14.5px;color:var(--ink-2);margin-top:7px;line-height:1.35}

.w{display:flex;align-items:center;justify-content:space-between;gap:14px;padding:7px 0;border-bottom:1px dotted var(--hair)}
.w:last-child{border-bottom:0}
.w .q{font-size:14px;color:var(--ink-2)}
.w .a{flex:0 0 auto;font-size:13.5px;font-weight:600;color:var(--brick);background:var(--brick-soft);border-radius:8px;padding:3px 10px}

.foot{margin-top:auto;display:flex;align-items:center;gap:18px;padding-top:12px}
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
      <div class="eyebrow">Как понять, что это отказ</div>
      <h2>Слова весят меньше, <i>чем ситуация вокруг них</i></h2>
    </div>
    <div class="hint">Одна и та же фраза значит разное в зависимости от того, что стоит рядом. <b>Смотреть нужно на конкретику</b>, а не на вежливость формулировки.</div>
  </div>

  <div class="scales">
    <div class="pivot"></div>
    <div class="beam"></div>
    <div class="post"></div>
    <div class="base"></div>
    <div class="rope l"></div><div class="knot l"></div>
    <div class="rope r"></div><div class="knot r"></div>

    <div class="pan left">
      <div class="t">ЧТО СКАЗАНО</div>
      <div class="say"><span class="h">我再看看</span><span class="p">wǒ zài kànkan</span></div>
      <div class="say2">«я ещё посмотрю» — звучит вежливо и ни к чему не обязывает</div>
    </div>

    <div class="pan right">
      <div class="t">ЧТО СТОИТ РЯДОМ</div>
%s
    </div>
  </div>

  <div class="foot">
    <div class="msg">Одно «посмотрю» ещё ничего не решает. <b>«Посмотрю» без срока и без продолжения — это «нет»</b></div>
    <div class="brand"><span class="dot2"></span><b>Kitai School</b><span>&middot; kitai-school.ru</span></div>
  </div>
</div>
</body></html>""" % (FONTS, VARS, ws)

info = info.replace("HGT", "584")
open(S + "ob-info.html", "w", encoding="utf-8").write(info)
print("ok")
