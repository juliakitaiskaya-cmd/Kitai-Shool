# -*- coding: utf-8 -*-
# Картинки к статье «Какой китайский учить»
# Обложка    — дорожный указатель с двумя стрелками: упрощённые и традиционные
# Инфографика — пульт с тремя переключателями: что вы на самом деле выбираете
S = "/tmp/claude-0/-home-user-Kitai-Shool/a463bfca-82a9-56fd-ae09-42a7257ff999/scratchpad/"

FONTS = ("<link href=\"https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,600;0,700;1,600"
         "&family=Inter:wght@400;500;600;700&family=Noto+Serif+SC:wght@600;700&display=swap\" rel=\"stylesheet\">")
VARS = (":root{--brick:#A41E3A;--brick-d:#841630;--brick-soft:#F7E6EB;--ink:#2C2420;--ink-2:#5A4F45;"
        "--taupe:#8B7D6B;--cream:#FAF7F2;--cream-2:#F3EDE3;--hair:#EAE3D8;--surface:#fff;"
        "--green:#1E7A46;--green-soft:#E3F6E9;--amber:#C08A2E;--amber-s:#FBF2DF;--blue:#2F5D8C;--blue-s:#E7EEF6;"
        "--post:#B7AE9E;--post-2:#9C9385}")

# ------------------------------------------------------------------ обложка
hero = """<!DOCTYPE html><html lang="ru"><head><meta charset="utf-8">
%s
<style>
%s
*{margin:0;box-sizing:border-box}html,body{width:1200px;height:630px}
.card{width:1200px;height:630px;background:radial-gradient(1100px 680px at 18%% 12%%, #fff 0%%, var(--cream) 54%%, var(--cream-2) 100%%);position:relative;overflow:hidden;font-family:'Inter',sans-serif;padding:54px 60px 0 72px;display:flex;justify-content:space-between}
.card:before{content:"";position:absolute;left:0;top:0;bottom:0;width:12px;background:var(--brick)}
.txt{flex:0 0 530px;padding-top:6px}
.eyebrow{color:var(--brick);font-weight:700;font-size:18px;letter-spacing:.19em;text-transform:uppercase;margin-bottom:13px}
h1{font-family:'Cormorant Garamond',serif;font-weight:600;font-size:50px;line-height:1.06;color:var(--ink);letter-spacing:-.4px}
h1 i{font-style:italic;color:var(--brick)}
.sub{font-size:18.5px;color:var(--ink-2);line-height:1.42;max-width:34ch;margin-top:16px}
.note{display:inline-block;margin-top:26px;background:var(--surface);border:1px solid var(--hair);border-left:4px solid var(--brick);border-radius:13px;padding:13px 19px;font-size:15.5px;color:var(--ink-2);line-height:1.36;max-width:36ch}
.note b{color:var(--ink)}

/* дорожный указатель */
.sign{flex:0 0 492px;position:relative;height:510px}
.post{position:absolute;left:222px;top:40px;width:26px;bottom:34px;background:linear-gradient(90deg,var(--post-2),var(--post),var(--post-2));border-radius:4px}
.base{position:absolute;left:158px;bottom:16px;width:154px;height:20px;border-radius:50%%;background:rgba(44,36,32,.13);filter:blur(2px)}
.plate{position:absolute;height:120px;display:flex;align-items:center;gap:13px;padding:0 20px;border:2px solid;border-radius:12px;box-shadow:0 10px 22px rgba(44,36,32,.16);background:var(--surface)}
.plate .han{font-family:'Noto Serif SC',serif;font-weight:700;font-size:56px;line-height:1}
.plate .lab{font-size:17px;font-weight:700;color:var(--ink);line-height:1.2}
.plate .lab span{display:block;font-size:14px;font-weight:400;color:var(--taupe);margin-top:5px;line-height:1.3}
.l{left:0;top:58px;width:258px;border-color:var(--brick);justify-content:flex-end;clip-path:polygon(46px 0, 100%% 0, 100%% 100%%, 46px 100%%, 0 50%%)}
.l .han{color:var(--brick)}
.r{left:234px;top:250px;width:258px;border-color:var(--blue);clip-path:polygon(0 0, calc(100%% - 46px) 0, 100%% 50%%, calc(100%% - 46px) 100%%, 0 100%%)}
.r .han{color:var(--blue)}
.brand{position:absolute;left:72px;bottom:30px;display:flex;align-items:center;gap:11px;color:var(--ink)}
.brand b{font-family:'Cormorant Garamond',serif;font-weight:700;font-size:26px}
.brand .bdot{width:10px;height:10px;border-radius:50%%;background:var(--brick)}
.brand span{color:var(--taupe);font-size:16px}
</style></head><body>
<div class="card">
  <div class="txt">
    <div class="eyebrow">Выбор</div>
    <h1>Какой китайский учить: <i>упрощённые или традиционные</i></h1>
    <div class="sub">Речь выбирать почти не приходится — путунхуа. А письменность это настоящая развилка, и зависит она от того, куда вы собираетесь</div>
    <div class="note"><b>Это развилка, а не ступени:</b> традиционное письмо не «продвинутый уровень» упрощённого</div>
  </div>
  <div class="sign">
    <div class="post"></div>
    <div class="base"></div>
    <div class="plate l">
      <div class="lab" style="text-align:right">Упрощённые<span>материк, Сингапур, HSK</span></div>
      <div class="han">汉</div>
    </div>
    <div class="plate r">
      <div class="han">漢</div>
      <div class="lab">Традиционные<span>Тайвань, Гонконг, Макао</span></div>
    </div>
  </div>
  <div class="brand"><span class="bdot"></span><b>Kitai School</b><span>&middot; kitai-school.ru</span></div>
</div>
</body></html>""" % (FONTS, VARS)

open(S + "kk-hero.html", "w", encoding="utf-8").write(hero)

# -------------------------------------------------------------- инфографика
SWITCHES = [
    ("Вариант речи", "путунхуа", "диалект", "left", "#8B7D6B",
     "Закреплён", "Школа, вузы, работа, экзамены — везде путунхуа. Диалект добавляют под конкретную задачу"),
    ("Письменность", "упрощённые", "традиционные", "both", "#A41E3A",
     "Выбираете вы", "Зависит от того, куда вы собираетесь: материк и Сингапур или Тайвань, Гонконг и Макао"),
    ("Произносительный стандарт", "пекинский", "тайваньский", "left", "#8B7D6B",
     "Почти закреплён", "Различия есть, но на понимание не влияют: это нюансы, а не отдельный язык"),
]

rows = "\n".join(
    '<div class="row">'
    '  <div class="name">%s<span style="color:%s">%s</span></div>'
    '  <div class="sw %s"><i class="a">%s</i><b class="knob"></b><i class="b">%s</i></div>'
    '  <div class="what">%s</div>'
    '</div>' % (nm, col, state, mode, a, b, what)
    for nm, a, b, mode, col, state, what in SWITCHES)

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
.hint{flex:0 0 352px;background:var(--surface);border:1px solid var(--hair);border-left:4px solid var(--brick);border-radius:12px;padding:12px 17px;font-size:14.5px;color:var(--ink-2);line-height:1.36}
.hint b{color:var(--ink)}

.rows{display:flex;flex-direction:column;gap:14px}
.row{display:flex;align-items:center;gap:22px;background:var(--surface);border:1px solid var(--hair);border-radius:14px;padding:15px 20px;box-shadow:0 5px 14px rgba(44,36,32,.05)}
.name{flex:0 0 226px;font-size:16.5px;font-weight:600;color:var(--ink);line-height:1.25}
.name span{display:block;font-size:13px;font-weight:700;margin-top:4px;text-transform:uppercase;letter-spacing:.07em}

.sw{flex:0 0 352px;display:flex;align-items:center;gap:11px}
.sw i{font-style:normal;font-size:14.5px;line-height:1.2;flex:1 1 0;text-align:center;padding:7px 4px;border-radius:8px;border:1px solid var(--hair);color:var(--taupe);background:var(--cream)}
.sw .knob{position:relative;flex:0 0 64px;height:30px;border-radius:16px;background:var(--cream-2);border:1px solid var(--hair);display:block}
.sw .knob:after{content:"";position:absolute;top:3px;width:22px;height:22px;border-radius:50%%;background:var(--ink-2)}
.sw.left .knob:after{left:4px}
.sw.left .a{color:var(--ink);font-weight:600;background:#fff;border-color:var(--ink-2)}
.sw.both .knob{background:var(--brick-soft);border-color:var(--brick)}
.sw.both .knob:after{left:4px;background:var(--brick)}
.sw.both .knob:before{content:"";position:absolute;top:3px;right:4px;width:22px;height:22px;border-radius:50%%;background:var(--brick);opacity:.45}
.sw.both .a,.sw.both .b{color:var(--ink);font-weight:600;background:#fff;border-color:var(--brick)}
.what{flex:1 1 auto;font-size:14.5px;color:var(--ink-2);line-height:1.34;border-left:1px solid var(--hair);padding-left:20px}

.foot{margin-top:auto;display:flex;align-items:center;gap:18px;padding-top:18px}
.foot .msg{flex:1 1 auto;background:var(--brick-soft);border:1px solid var(--brick);border-radius:14px;padding:12px 21px;font-size:15.5px;color:var(--ink);line-height:1.34}
.foot .msg b{color:var(--brick)}
.brand{display:flex;align-items:center;gap:10px;color:var(--ink);flex:0 0 auto}
.brand b{font-family:'Cormorant Garamond',serif;font-weight:700;font-size:23px}
.brand .dot2{width:9px;height:9px;border-radius:50%%;background:var(--brick)}
.brand span{color:var(--taupe);font-size:15px}
</style></head><body>
<div class="wrap">
  <div class="top">
    <div>
      <div class="eyebrow">Что вы выбираете</div>
      <h2>Три развилки — <i>и только одна настоящая</i></h2>
    </div>
    <div class="hint">Вопрос «какой китайский» на деле распадается на три. <b>Два переключателя стоят в заводском положении</b>, и трогать их почти никому не нужно.</div>
  </div>

  <div class="rows">
%s
  </div>

  <div class="foot">
    <div class="msg">Поэтому разговор о выборе — это почти всегда разговор о письменности: <b>упрощённые или традиционные</b></div>
    <div class="brand"><span class="dot2"></span><b>Kitai School</b><span>&middot; kitai-school.ru</span></div>
  </div>
</div>
</body></html>""" % (FONTS, VARS, rows)

info = info.replace("HGT", "500")
open(S + "kk-info.html", "w", encoding="utf-8").write(info)
print("ok")
