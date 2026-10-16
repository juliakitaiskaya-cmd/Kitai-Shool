# -*- coding: utf-8 -*-
# Картинки к статье «„Доброе утро“ по-китайски»
# Обложка    — рассвет на горизонте: солнце из-за линии и знак 早
# Инфографика — вокзальное табло: приветствие переключается по времени
S = "/tmp/claude-0/-home-user-Kitai-Shool/a463bfca-82a9-56fd-ae09-42a7257ff999/scratchpad/"

FONTS = ("<link href=\"https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,600;0,700;1,600"
         "&family=Inter:wght@400;500;600;700&family=Noto+Serif+SC:wght@600;700&display=swap\" rel=\"stylesheet\">")
VARS = (":root{--brick:#A41E3A;--brick-d:#841630;--brick-soft:#F7E6EB;--ink:#2C2420;--ink-2:#5A4F45;"
        "--taupe:#8B7D6B;--cream:#FAF7F2;--cream-2:#F3EDE3;--hair:#EAE3D8;--surface:#fff;"
        "--green:#1E7A46;--green-soft:#E3F6E9;--amber:#C08A2E;--amber-s:#FBF2DF;--blue:#2F5D8C;--blue-s:#E7EEF6;"
        "--board:#241E1A;--board-2:#332B26;--flap:#3C332D}")

# ------------------------------------------------------------------ обложка
hero = """<!DOCTYPE html><html lang="ru"><head><meta charset="utf-8">
%s
<style>
%s
*{margin:0;box-sizing:border-box}html,body{width:1200px;height:630px}
.card{width:1200px;height:630px;background:radial-gradient(1100px 680px at 15%% 10%%, #fff 0%%, var(--cream) 55%%, var(--cream-2) 100%%);position:relative;overflow:hidden;font-family:'Inter',sans-serif;display:flex;align-items:center;justify-content:space-between;padding:0 72px}
.card:before{content:"";position:absolute;left:0;top:0;bottom:0;width:12px;background:var(--brick)}
.txt{flex:0 0 486px}
.eyebrow{color:var(--brick);font-weight:700;font-size:18px;letter-spacing:.19em;text-transform:uppercase;margin-bottom:12px}
h1{font-family:'Cormorant Garamond',serif;font-weight:600;font-size:50px;line-height:1.06;color:var(--ink);letter-spacing:-.4px}
h1 i{font-style:italic;color:var(--brick)}
.sub{font-size:18px;color:var(--ink-2);line-height:1.42;max-width:30ch;margin-top:16px}
.brand{position:absolute;left:72px;bottom:32px;display:flex;align-items:center;gap:11px;color:var(--ink)}
.brand b{font-family:'Cormorant Garamond',serif;font-weight:700;font-size:26px}
.brand .bdot{width:10px;height:10px;border-radius:50%%;background:var(--brick)}
.brand span{color:var(--taupe);font-size:16px}

/* рассвет */
.art{flex:0 0 520px}
.scene{position:relative;height:330px;border-radius:20px;overflow:hidden;border:1px solid var(--hair);box-shadow:0 18px 40px rgba(44,36,32,.18);background:linear-gradient(180deg,#F6E2C9 0%%,#F3D2AE 42%%,#EDBE92 70%%,#E3A878 100%%)}
.sun{position:absolute;left:50%%;bottom:30px;transform:translateX(-50%%);width:214px;height:214px;border-radius:50%%;background:radial-gradient(circle at 50%% 45%%, #F6D48C 0%%, #E8A94E 58%%, #D98F35 100%%);box-shadow:0 0 70px 24px rgba(232,169,78,.42)}
.han{position:absolute;left:50%%;bottom:112px;transform:translateX(-50%%);font-family:'Noto Serif SC',serif;font-weight:700;font-size:120px;line-height:1;color:#4A3524;text-shadow:0 2px 0 rgba(255,255,255,.3)}
.ground{position:absolute;left:0;right:0;bottom:0;height:88px;background:linear-gradient(180deg,#8B6B4E 0%%,#6E5340 100%%)}
.ground:before{content:"";position:absolute;left:0;right:0;top:0;height:2px;background:rgba(255,255,255,.35)}
.cap{position:absolute;left:0;right:0;bottom:0;height:88px;display:flex;align-items:center;justify-content:center;gap:26px;color:#FBF3E8}
.cap .one{text-align:center}
.cap .one b{display:block;font-family:'Noto Serif SC',serif;font-weight:700;font-size:25px;line-height:1.1}
.cap .one span{display:block;font-size:13px;color:#E6D6C2;margin-top:2px;letter-spacing:.03em}
.cap .sep{width:1px;height:38px;background:rgba(255,255,255,.3)}
.under{display:flex;align-items:center;gap:12px;margin-top:18px;background:var(--surface);border:1px solid var(--hair);border-left:4px solid var(--brick);border-radius:14px;padding:12px 18px;font-size:15.5px;color:var(--ink-2);line-height:1.36}
.under b{color:var(--ink)}
</style></head><body>
<div class="card">
  <div class="txt">
    <div class="eyebrow">Приветствия</div>
    <h1>«Доброе утро»<br><i>по-китайски</i></h1>
    <div class="sub">Полное 早上好 — всегда уместно. Но чаще слышно одно короткое слово</div>
  </div>
  <div class="art">
    <div class="scene">
      <div class="sun"></div>
      <div class="han">早</div>
      <div class="ground"></div>
      <div class="cap">
        <div class="one"><b>早上好</b><span>zǎoshang hǎo</span></div>
        <div class="sep"></div>
        <div class="one"><b>早</b><span>zǎo</span></div>
        <div class="sep"></div>
        <div class="one"><b>早安</b><span>zǎo'ān</span></div>
      </div>
    </div>
    <div class="under">Знак <b>早</b> значит «рано» — и сам по себе работает как приветствие</div>
  </div>
  <div class="brand"><span class="bdot"></span><b>Kitai School</b><span>&middot; kitai-school.ru</span></div>
</div>
</body></html>""" % (FONTS, VARS)

open(S + "ut-hero.html", "w", encoding="utf-8").write(hero)

# -------------------------------------------------------------- инфографика
ROWS = [
    ("早上好", "zǎoshang hǎo", "раннее утро", "早安", ""),
    ("上午好", "shàngwǔ hǎo", "ближе к полудню, звучит официально", "—", ""),
    ("下午好", "xiàwǔ hǎo", "вторая половина дня", "午安", ""),
    ("晚上好", "wǎnshang hǎo", "вечер, при встрече", "—", ""),
    ("晚安", "wǎn'ān", "перед сном — это прощание, а не приветствие", "晚安", "off"),
]

rows = "\n".join(
    '<div class="row %s">'
    '  <div class="flaps">%s</div>'
    '  <div class="py">%s</div>'
    '  <div class="when">%s</div>'
    '  <div class="tw">%s</div>'
    '</div>' % (
        cls,
        "".join('<span class="flap">%s</span>' % ch for ch in han),
        py, when, tw)
    for han, py, when, tw, cls in ROWS)

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
.hint{flex:0 0 344px;background:var(--surface);border:1px solid var(--hair);border-left:4px solid var(--brick);border-radius:12px;padding:12px 17px;font-size:14.5px;color:var(--ink-2);line-height:1.36}
.hint b{color:var(--ink)}

.board{background:var(--board);border-radius:16px;padding:16px 20px 18px;box-shadow:0 16px 34px rgba(44,36,32,.26)}
.head{display:flex;align-items:center;color:#A99A8C;font-size:11.5px;font-weight:700;letter-spacing:.14em;padding:0 2px 11px;border-bottom:1px solid #4A403A}
.head .c1{flex:0 0 212px}
.head .c2{flex:0 0 158px}
.head .c3{flex:1 1 auto}
.head .c4{flex:0 0 150px;text-align:right}
.row{display:flex;align-items:center;padding:12px 2px;border-bottom:1px dashed #413832}
.row:last-child{border-bottom:0}
.flaps{flex:0 0 212px;display:flex;gap:7px}
.flap{position:relative;display:flex;align-items:center;justify-content:center;width:46px;height:52px;background:linear-gradient(180deg,var(--flap) 0%%,var(--flap) 49%%,#352D28 50%%,#2E2722 100%%);border-radius:5px;font-family:'Noto Serif SC',serif;font-weight:700;font-size:28px;color:#F6EFE4;box-shadow:inset 0 0 0 1px rgba(255,255,255,.05)}
.flap:after{content:"";position:absolute;left:0;right:0;top:50%%;height:1px;background:rgba(0,0,0,.55)}
.py{flex:0 0 158px;color:#D8C9B6;font-size:14.5px;padding-left:14px}
.when{flex:1 1 auto;color:#B9AA99;font-size:14.5px;padding-left:8px;line-height:1.34}
.tw{flex:0 0 150px;text-align:right;font-family:'Noto Serif SC',serif;font-weight:700;font-size:21px;color:#E8B86A}
.row.off .flap{background:linear-gradient(180deg,#4A2A30 0%%,#4A2A30 49%%,#3E2228 50%%,#371E23 100%%);color:#FBD9E0}
.row.off .when{color:#E8A9B6}

.foot{margin-top:auto;display:flex;align-items:center;gap:18px;padding-top:18px}
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
      <div class="eyebrow">Приветствие переключается по времени</div>
      <h2>Не по вежливости, <i>а по часам</i></h2>
    </div>
    <div class="hint">Форма зависит от того, который час, а не от того, насколько вы близки. <b>Жёстких границ между частями дня нет</b> — ориентируются на полдень.</div>
  </div>

  <div class="board">
    <div class="head">
      <div class="c1">ФОРМА</div>
      <div class="c2">ЧТЕНИЕ</div>
      <div class="c3">КОГДА ГОВОРЯТ</div>
      <div class="c4">НА ТАЙВАНЕ</div>
    </div>
%s
  </div>

  <div class="foot">
    <div class="msg">На материке в ходу формы с <b>好</b>, на Тайване — с <b>安</b>. Это сложившаяся практика, а не правило</div>
    <div class="brand"><span class="dot2"></span><b>Kitai School</b><span>&middot; kitai-school.ru</span></div>
  </div>
</div>
</body></html>""" % (FONTS, VARS, rows)

info = info.replace("HGT", "640")
open(S + "ut-info.html", "w", encoding="utf-8").write(info)
print("ok")
