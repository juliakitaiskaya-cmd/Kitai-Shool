# -*- coding: utf-8 -*-
# Картинки к статье «Несчастливое число в Китае»
# Обложка    — автомобильный номерной знак: суеверие видно там, где число выбирают
# Инфографика — панель лифта с пропущенными этажами
S = "/tmp/claude-0/-home-user-Kitai-Shool/a463bfca-82a9-56fd-ae09-42a7257ff999/scratchpad/"

FONTS = ("<link href=\"https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,600;0,700;1,600"
         "&family=Inter:wght@400;500;600;700&family=Noto+Serif+SC:wght@600;700&display=swap\" rel=\"stylesheet\">")
VARS = (":root{--brick:#A41E3A;--brick-d:#841630;--brick-soft:#F7E6EB;--ink:#2C2420;--ink-2:#5A4F45;"
        "--taupe:#8B7D6B;--cream:#FAF7F2;--cream-2:#F3EDE3;--hair:#EAE3D8;--surface:#fff;"
        "--green:#1E7A46;--green-s:#E3F6E9;--amber:#C08A2E;--amber-s:#FBF2DF;--blue:#2F5D8C;--blue-s:#E7EEF6;"
        "--plate:#1A4F93;--plate-2:#143C70;--panel:#3B3733;--panel-2:#2B2825;--btn:#F1ECE3}")

hero = """<!DOCTYPE html><html lang="ru"><head><meta charset="utf-8">
%s
<style>
%s
*{margin:0;box-sizing:border-box}html,body{width:1200px;height:630px}
.card{width:1200px;height:630px;background:radial-gradient(1050px 660px at 14%% 12%%, #fff 0%%, var(--cream) 52%%, var(--cream-2) 100%%);position:relative;overflow:hidden;font-family:'Inter',sans-serif;padding:52px 46px 0 72px;display:flex;justify-content:space-between}
.card:before{content:"";position:absolute;left:0;top:0;bottom:0;width:12px;background:var(--brick)}
.txt{flex:0 0 512px;padding-top:4px}
.eyebrow{color:var(--brick);font-weight:700;font-size:18px;letter-spacing:.19em;text-transform:uppercase;margin-bottom:13px}
h1{font-family:'Cormorant Garamond',serif;font-weight:600;font-size:46px;line-height:1.06;color:var(--ink);letter-spacing:-.4px}
h1 i{font-style:italic;color:var(--brick)}
.sub{font-size:18px;color:var(--ink-2);line-height:1.42;max-width:32ch;margin-top:16px}
.note{display:inline-block;margin-top:22px;background:var(--surface);border:1px solid var(--hair);border-left:4px solid var(--brick);border-radius:13px;padding:13px 19px;font-size:15.5px;color:var(--ink-2);line-height:1.36;max-width:34ch}
.note b{color:var(--ink)}

/* номерной знак */
.scene{flex:0 0 528px;position:relative;height:482px;display:flex;flex-direction:column;align-items:center;justify-content:flex-start;padding-top:112px}
.plate{width:452px;height:148px;border-radius:14px;background:linear-gradient(168deg,var(--plate),var(--plate-2));border:4px solid #fff;box-shadow:0 16px 34px rgba(26,45,70,.32);display:flex;align-items:center;justify-content:center;gap:14px;transform:rotate(-2deg)}
.plate span{color:#fff;font-family:'Inter',sans-serif;font-weight:700;font-size:64px;letter-spacing:2px;line-height:1}
.plate .han{font-family:'Noto Serif SC',serif;font-size:56px;font-weight:600}
.plate .dot{width:12px;height:12px;border-radius:50%%;background:#fff;opacity:.9}
.cap{margin-top:34px;text-align:left;font-size:16.5px;color:var(--ink-2);line-height:1.44;max-width:40ch;align-self:flex-start;padding-left:30px}
.cap b{color:var(--ink)}
.tiny{margin-top:14px;font-size:14px;color:var(--taupe);align-self:flex-start;padding-left:30px}
.brand{position:absolute;left:72px;bottom:28px;display:flex;align-items:center;gap:11px;color:var(--ink)}
.brand b{font-family:'Cormorant Garamond',serif;font-weight:700;font-size:26px}
.brand .bdot{width:10px;height:10px;border-radius:50%%;background:var(--brick)}
.brand span{color:var(--taupe);font-size:16px}
</style></head><body>
<div class="card">
  <div class="txt">
    <div class="eyebrow">Числа и суеверия</div>
    <h1>Несчастливое число <i>в Китае</i></h1>
    <div class="sub">Четвёрка известна всем, но плохих чисел больше одного — и почти каждое правило местное</div>
    <div class="note"><b>Суеверие живёт не в языке, а в нумерации:</b> там, где число можно выбрать, его выбирают</div>
  </div>
  <div class="scene">
    <div class="plate">
      <span class="han">苏</span><span>A</span><span class="dot"></span><span>4&nbsp;4&nbsp;4&nbsp;4</span>
    </div>
    <div class="cap">Четвёрка известна, но она не одна: есть ещё <b>14 и 24, седьмой месяц, тройка в подарке и возрастные 73 и 84</b></div>
    <div class="tiny">Номер на картинке условный</div>
  </div>
  <div class="brand"><span class="bdot"></span><b>Kitai School</b><span>&middot; kitai-school.ru</span></div>
</div>
</body></html>""" % (FONTS, VARS)

open(S + "ch-hero.html", "w", encoding="utf-8").write(hero)

# -------------------------------------------------------------- инфографика
ROWS = [(12, 15), (10, 11), (8, 9), (6, 7), (3, 5), (1, 2)]
grid = "\n".join(
    '<div class="btn">%d</div><div class="btn">%d</div>' % r for r in ROWS)

NOTES = [
    ("4", "四 sì", "созвучно 死 sǐ «умереть»: тона разные, но сходства хватило"),
    ("14", "十四 shísì", "в кантонском близко к 實死 «непременно умрёт» — хуже простой четвёрки"),
    ("24", "二十四 èrshísì", "в кантонском близко к 易死 «легко умереть»"),
    ("13", "十三 shísān", "созвучия нет: в Гонконге его пропускают по западной привычке"),
]

notes = "\n".join(
    '<div class="nt"><div class="num">%s</div><div class="bd"><b>%s</b><span>%s</span></div></div>'
    % n for n in NOTES)

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
.hint{flex:0 0 384px;background:var(--surface);border:1px solid var(--hair);border-left:4px solid var(--brick);border-radius:12px;padding:12px 17px;font-size:14.5px;color:var(--ink-2);line-height:1.36}
.hint b{color:var(--ink)}

.main{display:flex;gap:34px;align-items:stretch}
.panel{flex:0 0 262px;background:linear-gradient(168deg,var(--panel),var(--panel-2));border-radius:22px;padding:24px 22px;box-shadow:0 14px 30px rgba(44,36,32,.26);display:flex;flex-direction:column;align-items:center}
.plabel{color:#CFC7BC;font-size:13px;letter-spacing:.14em;text-transform:uppercase;margin-bottom:16px}
.grid{display:grid;grid-template-columns:repeat(2,84px);gap:11px 18px;justify-content:center}
.btn{width:84px;height:42px;border-radius:10px;background:var(--btn);color:#262220;font-size:19px;font-weight:600;display:flex;align-items:center;justify-content:center;box-shadow:inset 0 -2px 0 rgba(0,0,0,.14)}
.gap{color:#8E8781;font-size:13px;margin-top:16px;text-align:center;line-height:1.4}

.right{flex:1 1 auto;display:flex;flex-direction:column;gap:12px;justify-content:center}
.nt{display:flex;align-items:center;gap:18px;background:var(--surface);border:1px solid var(--hair);border-radius:14px;padding:13px 20px;box-shadow:0 5px 13px rgba(44,36,32,.05)}
.nt .num{flex:0 0 72px;height:52px;border-radius:11px;background:var(--brick-soft);border:1px solid var(--brick);color:var(--brick);font-size:25px;font-weight:700;display:flex;align-items:center;justify-content:center}
.nt .bd{display:flex;flex-direction:column}
.nt .bd b{font-family:'Noto Serif SC',serif;font-size:19px;color:var(--ink);line-height:1.25}
.nt .bd span{font-size:15px;color:var(--ink-2);margin-top:5px;line-height:1.36}

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
      <div class="eyebrow">Как это выглядит на практике</div>
      <h2>Этажи, которых <i>нет в лифте</i></h2>
    </div>
    <div class="hint">Так пропускают <b>не везде и не всегда</b>: набор пропущенных номеров зависит от города, застройщика и языка, на котором считают созвучие.</div>
  </div>

  <div class="main">
    <div class="panel">
      <div class="plabel">Этаж</div>
      <div class="grid">
%s
      </div>
      <div class="gap">После 3 сразу 5,<br>после 12 сразу 15</div>
    </div>
    <div class="right">
%s
    </div>
  </div>

  <div class="foot">
    <div class="msg">Проверить просто: <b>посмотрите на кнопки в первом же лифте</b> — пропуски видно сразу</div>
    <div class="brand"><span class="dot2"></span><b>Kitai School</b><span>&middot; kitai-school.ru</span></div>
  </div>
</div>
</body></html>""" % (FONTS, VARS, grid, notes)

info = info.replace("HGT", "700")
open(S + "ch-info.html", "w", encoding="utf-8").write(info)
print("ok")
