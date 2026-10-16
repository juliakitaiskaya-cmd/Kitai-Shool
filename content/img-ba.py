# -*- coding: utf-8 -*-
# Картинки к статье «Конструкция 把»
# Обложка    — посылка со штампом: объект взяли и что-то с ним сделали
# Инфографика — пропускной турникет: четыре условия подряд
S = "/tmp/claude-0/-home-user-Kitai-Shool/a463bfca-82a9-56fd-ae09-42a7257ff999/scratchpad/"

FONTS = ("<link href=\"https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,600;0,700;1,600"
         "&family=Inter:wght@400;500;600;700&family=Noto+Serif+SC:wght@600;700&display=swap\" rel=\"stylesheet\">")
VARS = (":root{--brick:#A41E3A;--brick-d:#841630;--brick-soft:#F7E6EB;--ink:#2C2420;--ink-2:#5A4F45;"
        "--taupe:#8B7D6B;--cream:#FAF7F2;--cream-2:#F3EDE3;--hair:#EAE3D8;--surface:#fff;"
        "--green:#1E7A46;--green-soft:#E3F6E9;--amber:#C08A2E;--amber-s:#FBF2DF;--blue:#2F5D8C;--blue-s:#E7EEF6;"
        "--kraft:#D8BE96;--kraft-d:#C2A277;--kraft-l:#E6D2B2}")

# ------------------------------------------------------------------ обложка
hero = """<!DOCTYPE html><html lang="ru"><head><meta charset="utf-8">
%s
<style>
%s
*{margin:0;box-sizing:border-box}html,body{width:1200px;height:630px}
.card{width:1200px;height:630px;background:radial-gradient(1100px 680px at 15%% 10%%, #fff 0%%, var(--cream) 55%%, var(--cream-2) 100%%);position:relative;overflow:hidden;font-family:'Inter',sans-serif;display:flex;align-items:center;justify-content:space-between;padding:0 68px 0 72px}
.card:before{content:"";position:absolute;left:0;top:0;bottom:0;width:12px;background:var(--brick)}
.txt{flex:0 0 476px}
.eyebrow{color:var(--brick);font-weight:700;font-size:18px;letter-spacing:.19em;text-transform:uppercase;margin-bottom:12px}
h1{font-family:'Cormorant Garamond',serif;font-weight:600;font-size:52px;line-height:1.05;color:var(--ink);letter-spacing:-.4px}
h1 i{font-style:italic;color:var(--brick)}
h1 .han{font-family:'Noto Serif SC',serif;font-weight:700;font-size:52px}
.sub{font-size:18px;color:var(--ink-2);line-height:1.42;max-width:31ch;margin-top:16px}
.form{display:inline-flex;align-items:center;gap:9px;margin-top:24px;background:var(--surface);border:1px solid var(--hair);border-radius:13px;padding:11px 16px;font-size:15px;color:var(--ink-2);box-shadow:0 4px 12px rgba(44,36,32,.05)}
.form b{font-family:'Noto Serif SC',serif;font-weight:700;font-size:19px;color:var(--brick)}
.brand{position:absolute;left:72px;bottom:32px;display:flex;align-items:center;gap:11px;color:var(--ink)}
.brand b{font-family:'Cormorant Garamond',serif;font-weight:700;font-size:26px}
.brand .bdot{width:10px;height:10px;border-radius:50%%;background:var(--brick)}
.brand span{color:var(--taupe);font-size:16px}

/* посылка */
.art{flex:0 0 512px;display:flex;flex-direction:column;align-items:center}
.box{position:relative;width:360px;height:264px;background:linear-gradient(180deg,var(--kraft-l) 0%%,var(--kraft) 58%%,var(--kraft-d) 100%%);border:2px solid #B2905F;border-radius:10px;box-shadow:0 18px 38px rgba(44,36,32,.2)}
.box:before{content:"";position:absolute;left:0;right:0;top:46px;height:3px;background:rgba(0,0,0,.12)}
.tape{position:absolute;left:50%%;top:-2px;transform:translateX(-50%%);width:74px;height:268px;background:linear-gradient(180deg,rgba(255,255,255,.55),rgba(255,255,255,.3));border-left:1px solid rgba(0,0,0,.08);border-right:1px solid rgba(0,0,0,.08)}
.tag{position:absolute;left:30px;top:88px;width:150px;background:#FDFBF4;border:1px solid #CBB893;border-radius:7px;padding:12px 14px;box-shadow:0 5px 12px rgba(44,36,32,.14)}
.tag .h{font-family:'Noto Serif SC',serif;font-weight:700;font-size:40px;color:var(--ink);line-height:1}
.tag .p{font-size:13px;color:var(--taupe);margin-top:3px}
.tag .r{font-size:13.5px;color:var(--ink-2);margin-top:6px;border-top:1px dotted #D9C9A9;padding-top:6px}
.stamp{position:absolute;right:26px;top:104px;width:122px;height:122px;border:4px solid var(--brick);border-radius:8px;display:flex;align-items:center;justify-content:center;transform:rotate(-9deg);background:rgba(255,255,255,.14)}
.stamp span{font-family:'Noto Serif SC',serif;font-weight:700;font-size:74px;color:var(--brick);line-height:1}
.result{margin-top:20px;display:flex;align-items:center;gap:12px;background:var(--surface);border:1px solid var(--hair);border-left:4px solid var(--green);border-radius:13px;padding:12px 18px;box-shadow:0 5px 14px rgba(44,36,32,.06)}
.result .h{font-family:'Noto Serif SC',serif;font-weight:700;font-size:22px;color:var(--ink);line-height:1}
.result .t{font-size:14.5px;color:var(--ink-2);line-height:1.34}
.result .t b{color:var(--green)}
</style></head><body>
<div class="card">
  <div class="txt">
    <div class="eyebrow">Грамматика</div>
    <h1>Конструкция <i><span class="han">把</span></i></h1>
    <div class="sub">Она не переставляет слова, а говорит, что с предметом сделали — и чем это кончилось</div>
    <div class="form"><b>把</b> &nbsp;подлежащее + 把 + объект + глагол + результат</div>
  </div>
  <div class="art">
    <div class="box">
      <div class="tape"></div>
      <div class="tag">
        <div class="h">书</div>
        <div class="p">shū · книга</div>
        <div class="r">объект, о котором уже знают</div>
      </div>
      <div class="stamp"><span>把</span></div>
    </div>
    <div class="result">
      <span class="h">放在桌子上</span>
      <span class="t">fàng zài zhuōzi shang<br><b>результат обязателен</b></span>
    </div>
  </div>
  <div class="brand"><span class="bdot"></span><b>Kitai School</b><span>&middot; kitai-school.ru</span></div>
</div>
</body></html>""" % (FONTS, VARS)

open(S + "ba-hero.html", "w", encoding="utf-8").write(hero)

# -------------------------------------------------------------- инфографика
GATES = [
    ("1", "Объект известен?", "把书…", "не «какую-то книгу», а ту самую"),
    ("2", "Глагол что-то делает?", "把…放", "не 知道, не 相信, не 希望"),
    ("3", "После глагола есть элемент?", "…放在桌子上", "голый глагол не годится"),
    ("4", "Отрицание перед 把?", "没把…", "а не после: 把…没…"),
]

gates = "\n".join(
    '<div class="gate">'
    '  <div class="num">%s</div>'
    '  <div class="q">%s</div>'
    '  <div class="ex"><span class="han">%s</span></div>'
    '  <div class="no">%s</div>'
    '</div>' % g for g in GATES)

info = """<!DOCTYPE html><html lang="ru"><head><meta charset="utf-8">
%s
<style>
%s
*{margin:0;box-sizing:border-box}html,body{width:1200px;height:HGTpx}
.wrap{width:1200px;height:HGTpx;background:linear-gradient(180deg,#fff 0%%,var(--cream) 46%%,var(--cream-2) 100%%);font-family:'Inter',sans-serif;padding:32px 46px 26px;display:flex;flex-direction:column}
.top{display:flex;align-items:flex-end;justify-content:space-between;gap:30px;margin-bottom:24px}
.eyebrow{color:var(--brick);font-weight:700;font-size:14.5px;letter-spacing:.17em;text-transform:uppercase;margin-bottom:7px}
h2{font-family:'Cormorant Garamond',serif;font-weight:600;font-size:40px;line-height:1.07;color:var(--ink);letter-spacing:-.3px}
h2 i{font-style:italic;color:var(--brick)}
.hint{flex:0 0 346px;background:var(--surface);border:1px solid var(--hair);border-left:4px solid var(--brick);border-radius:12px;padding:12px 17px;font-size:14.5px;color:var(--ink-2);line-height:1.36}
.hint b{color:var(--ink)}

.track{display:flex;align-items:stretch;gap:0}
.start{flex:0 0 150px;display:flex;flex-direction:column;align-items:center;justify-content:center;background:var(--cream-2);border:1px dashed var(--taupe);border-radius:14px 4px 4px 14px;padding:14px 12px;text-align:center}
.start .h{font-family:'Noto Serif SC',serif;font-weight:700;font-size:26px;color:var(--ink);line-height:1.15}
.start .t{font-size:12.5px;color:var(--taupe);margin-top:6px;line-height:1.3}

.gate{flex:1 1 0;position:relative;background:var(--surface);border:1px solid var(--hair);border-left:0;padding:16px 16px 18px;display:flex;flex-direction:column;align-items:center;text-align:center}
.gate:before{content:"";position:absolute;left:0;top:14px;bottom:14px;width:4px;background:var(--brick);border-radius:2px}
.num{width:28px;height:28px;border-radius:50%%;background:var(--brick);color:#fff;font-size:14px;font-weight:700;display:flex;align-items:center;justify-content:center}
.q{font-size:15px;font-weight:600;color:var(--ink);line-height:1.3;margin-top:9px;min-height:40px}
.ex{margin-top:8px;background:var(--cream);border:1px solid var(--hair);border-radius:9px;padding:7px 12px}
.ex .han{font-family:'Noto Serif SC',serif;font-weight:700;font-size:20px;color:var(--brick);line-height:1.1}
.no{font-size:12.5px;color:var(--ink-2);line-height:1.35;margin-top:9px}

.fin{flex:0 0 164px;display:flex;flex-direction:column;align-items:center;justify-content:center;background:var(--green-soft);border:1px solid #BFE3CC;border-radius:4px 14px 14px 4px;padding:14px 12px;text-align:center}
.fin .h{font-family:'Noto Serif SC',serif;font-weight:700;font-size:19px;color:var(--green);line-height:1.2}
.fin .t{font-size:12.5px;color:#2C5E42;margin-top:6px;line-height:1.3}

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
      <div class="eyebrow">Четыре условия подряд</div>
      <h2>Предложение проходит <i>четыре проверки</i></h2>
    </div>
    <div class="hint">Если хоть одна не пройдена, конструкция не собирается. <b>Чаще всего спотыкаются на третьей</b>: глагол оставляют без результата.</div>
  </div>

  <div class="track">
    <div class="start">
      <div class="h">我…书…放</div>
      <div class="t">хочу сказать,<br>что сделал с книгой</div>
    </div>
%s
    <div class="fin">
      <div class="h">我把书放在<br>桌子上了</div>
      <div class="t">предложение собрано</div>
    </div>
  </div>

  <div class="foot">
    <div class="msg">Проверка, которая снимает больше всего ошибок: <b>сказали ли вы, чем дело кончилось</b></div>
    <div class="brand"><span class="dot2"></span><b>Kitai School</b><span>&middot; kitai-school.ru</span></div>
  </div>
</div>
</body></html>""" % (FONTS, VARS, gates)

info = info.replace("HGT", "476")
open(S + "ba-info.html", "w", encoding="utf-8").write(info)
print("ok")
