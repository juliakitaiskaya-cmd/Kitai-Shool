# -*- coding: utf-8 -*-
# Картинки к статье «Как китайцы учат свой язык»
# Обложка    — страница букваря: пиньинь над знаком
# Инфографика — клетка 田字格 и четыре шага обучения грамоте
S = "/tmp/claude-0/-home-user-Kitai-Shool/a463bfca-82a9-56fd-ae09-42a7257ff999/scratchpad/"

FONTS = ("<link href=\"https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,600;0,700;1,600"
         "&family=Inter:wght@400;500;600;700&family=Noto+Serif+SC:wght@600;700&display=swap\" rel=\"stylesheet\">")
VARS = (":root{--brick:#A41E3A;--brick-d:#841630;--brick-soft:#F7E6EB;--ink:#2C2420;--ink-2:#5A4F45;"
        "--taupe:#8B7D6B;--cream:#FAF7F2;--cream-2:#F3EDE3;--hair:#EAE3D8;--surface:#fff;"
        "--green:#1E7A46;--green-s:#E3F6E9;--amber:#C08A2E;--amber-s:#FBF2DF;--blue:#2F5D8C;--blue-s:#E7EEF6;"
        "--paper:#FFFDF7;--rule:#D8CDB8;--grid:#D9CFBC;--pencil:#4A4034}")

hero = """<!DOCTYPE html><html lang="ru"><head><meta charset="utf-8">
%s
<style>
%s
*{margin:0;box-sizing:border-box}html,body{width:1200px;height:630px}
.card{width:1200px;height:630px;background:radial-gradient(1050px 660px at 14%% 12%%, #fff 0%%, var(--cream) 52%%, var(--cream-2) 100%%);position:relative;overflow:hidden;font-family:'Inter',sans-serif;padding:52px 46px 0 72px;display:flex;justify-content:space-between}
.card:before{content:"";position:absolute;left:0;top:0;bottom:0;width:12px;background:var(--brick)}
.txt{flex:0 0 506px;padding-top:4px}
.eyebrow{color:var(--brick);font-weight:700;font-size:18px;letter-spacing:.19em;text-transform:uppercase;margin-bottom:13px}
h1{font-family:'Cormorant Garamond',serif;font-weight:600;font-size:44px;line-height:1.07;color:var(--ink);letter-spacing:-.4px}
h1 i{font-style:italic;color:var(--brick)}
.sub{font-size:18px;color:var(--ink-2);line-height:1.42;max-width:32ch;margin-top:16px}
.note{display:inline-block;margin-top:22px;background:var(--surface);border:1px solid var(--hair);border-left:4px solid var(--brick);border-radius:13px;padding:13px 19px;font-size:15.5px;color:var(--ink-2);line-height:1.36;max-width:34ch}
.note b{color:var(--ink)}

/* страница букваря */
.scene{flex:0 0 520px;position:relative;height:482px;display:flex;align-items:flex-start;justify-content:center;padding-top:34px}
.page{width:404px;height:396px;background:var(--paper);border:1px solid #E6DCC6;border-radius:8px;box-shadow:0 16px 32px rgba(44,36,32,.17);padding:24px 26px;display:flex;flex-direction:column;position:relative}
.page:before{content:"";position:absolute;left:0;top:0;bottom:0;width:30px;border-right:1px dashed var(--rule);background:#FBF6EA;border-radius:8px 0 0 8px}
.head{display:flex;align-items:baseline;justify-content:space-between;padding-left:18px;border-bottom:1px solid var(--rule);padding-bottom:10px}
.head b{font-size:15px;color:var(--ink-2);letter-spacing:.04em}
.head span{font-size:13px;color:var(--taupe)}
.mid{flex:1 1 auto;display:flex;align-items:center;justify-content:center;gap:26px;padding-left:18px}
.cell{width:170px;height:170px;border:2px solid var(--brick);border-radius:4px;position:relative;background:#fff}
.cell:before,.cell:after{content:"";position:absolute;background:transparent;border-color:rgba(164,30,58,.45);border-style:dashed}
.cell:before{left:50%%;top:0;bottom:0;border-left-width:1px;border-left-style:dashed}
.cell:after{top:50%%;left:0;right:0;border-top-width:1px;border-top-style:dashed}
.cell .han{position:absolute;inset:0;display:flex;align-items:center;justify-content:center;font-family:'Noto Serif SC',serif;font-size:116px;color:var(--pencil);line-height:1}
.right{display:flex;flex-direction:column;align-items:center;gap:8px}
.py{font-size:30px;color:var(--brick);font-style:italic}
.ru{font-size:17px;color:var(--ink-2)}
.strokes{display:flex;gap:7px;margin-top:6px}
.strokes i{width:34px;height:34px;border:1px dashed var(--grid);border-radius:4px;display:flex;align-items:center;justify-content:center;font-family:'Noto Serif SC',serif;font-size:19px;color:#9A9084;font-style:normal}
.foot{padding-left:18px;border-top:1px solid var(--rule);padding-top:10px;font-size:13.5px;color:var(--taupe)}
.cap{position:absolute;left:0;right:0;bottom:12px;text-align:center;font-size:16px;color:var(--ink-2)}
.cap b{color:var(--ink)}
.brand{position:absolute;left:72px;bottom:28px;display:flex;align-items:center;gap:11px;color:var(--ink)}
.brand b{font-family:'Cormorant Garamond',serif;font-weight:700;font-size:26px}
.brand .bdot{width:10px;height:10px;border-radius:50%%;background:var(--brick)}
.brand span{color:var(--taupe);font-size:16px}
</style></head><body>
<div class="card">
  <div class="txt">
    <div class="eyebrow">Школа</div>
    <h1>Как китайцы <i>учат свой язык</i></h1>
    <div class="sub">Первый класс начинается не с иероглифов, а с пиньиня: сперва звуки и тоны</div>
    <div class="note"><b>Дальше — черты, клетка 田字格 и диктанты:</b> знаки учат писать, а не только узнавать</div>
  </div>
  <div class="scene">
    <div class="page">
      <div class="head"><b>语文 · 一年级</b><span>стр. 12</span></div>
      <div class="mid">
        <div class="cell"><span class="han">水</span></div>
        <div class="right">
          <div class="py">shuǐ</div>
          <div class="ru">вода</div>
          <div class="strokes"><i>亅</i><i>乛</i><i>丿</i><i>乀</i></div>
        </div>
      </div>
      <div class="foot">Пропись: обведи и напиши сам</div>
    </div>
    <div class="cap">Страница букваря выглядит <b>примерно так</b></div>
  </div>
  <div class="brand"><span class="bdot"></span><b>Kitai School</b><span>&middot; kitai-school.ru</span></div>
</div>
</body></html>""" % (FONTS, VARS)

open(S + "yk-hero.html", "w", encoding="utf-8").write(hero)

# -------------------------------------------------------------- инфографика
STEPS = [
    ("1", "Пиньинь", "первые недели уходят на звуки, тоны и чтение по слогам"),
    ("2", "Черты и ключи", "порядок черт, базовые элементы, из чего собран знак"),
    ("3", "Прописи", "сначала обводят по серому, потом пишут знак сами"),
    ("4", "Диктанты 听写", "учитель называет слово, дети пишут знаки по памяти"),
]

steps = "\n".join(
    '<div class="st"><div class="n">%s</div><div class="bd"><b>%s</b><span>%s</span></div></div>'
    % s for s in STEPS)

info = """<!DOCTYPE html><html lang="ru"><head><meta charset="utf-8">
%s
<style>
%s
*{margin:0;box-sizing:border-box}html,body{width:1200px;height:HGTpx}
.wrap{width:1200px;height:HGTpx;background:linear-gradient(180deg,#fff 0%%,var(--cream) 46%%,var(--cream-2) 100%%);font-family:'Inter',sans-serif;padding:32px 46px 30px;display:flex;flex-direction:column}
.top{display:flex;align-items:flex-end;justify-content:space-between;gap:30px;margin-bottom:20px}
.eyebrow{color:var(--brick);font-weight:700;font-size:14.5px;letter-spacing:.17em;text-transform:uppercase;margin-bottom:7px}
h2{font-family:'Cormorant Garamond',serif;font-weight:600;font-size:40px;line-height:1.07;color:var(--ink);letter-spacing:-.3px}
h2 i{font-style:italic;color:var(--brick)}
.hint{flex:0 0 384px;background:var(--surface);border:1px solid var(--hair);border-left:4px solid var(--brick);border-radius:12px;padding:12px 17px;font-size:14.5px;color:var(--ink-2);line-height:1.36}
.hint b{color:var(--ink)}

.main{display:flex;gap:32px;align-items:center}
.cellwrap{flex:0 0 268px;display:flex;flex-direction:column;align-items:center;gap:12px}
.cell{width:230px;height:230px;border:3px solid var(--brick);border-radius:5px;position:relative;background:#fff;box-shadow:0 6px 16px rgba(44,36,32,.08)}
.cell .v{position:absolute;left:50%%;top:0;bottom:0;border-left:1px dashed rgba(164,30,58,.5)}
.cell .h{position:absolute;top:50%%;left:0;right:0;border-top:1px dashed rgba(164,30,58,.5)}
.cell .d1{position:absolute;left:0;top:0;width:100%%;height:100%%;background:linear-gradient(to bottom right, transparent calc(50%% - 1px), rgba(164,30,58,.3) 50%%, transparent calc(50%% + 1px))}
.cell .d2{position:absolute;left:0;top:0;width:100%%;height:100%%;background:linear-gradient(to bottom left, transparent calc(50%% - 1px), rgba(164,30,58,.3) 50%%, transparent calc(50%% + 1px))}
.cell .han{position:absolute;inset:0;display:flex;align-items:center;justify-content:center;font-family:'Noto Serif SC',serif;font-size:150px;color:var(--ink);line-height:1}
.cellwrap .lab{font-size:15px;color:var(--ink-2);text-align:center;line-height:1.36}
.cellwrap .lab b{color:var(--ink)}

.steps{flex:1 1 auto;display:flex;flex-direction:column;gap:12px}
.st{display:flex;align-items:center;gap:18px;background:var(--surface);border:1px solid var(--hair);border-radius:13px;padding:13px 20px;box-shadow:0 4px 12px rgba(44,36,32,.05)}
.st .n{flex:0 0 42px;height:42px;border-radius:50%%;background:var(--brick-soft);border:1px solid var(--brick);color:var(--brick);font-size:19px;font-weight:700;display:flex;align-items:center;justify-content:center}
.st .bd{display:flex;flex-direction:column}
.st .bd b{font-size:17px;color:var(--ink);line-height:1.25}
.st .bd span{font-size:14.5px;color:var(--ink-2);margin-top:4px;line-height:1.36}

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
      <div class="eyebrow">Обучение грамоте</div>
      <h2>Четыре шага <i>и клетка с диагоналями</i></h2>
    </div>
    <div class="hint">Сроки и порядок <b>различаются по учебникам</b>: это общая картина, а не единое расписание для всех школ.</div>
  </div>

  <div class="main">
    <div class="cellwrap">
      <div class="cell">
        <div class="d1"></div><div class="d2"></div>
        <div class="v"></div><div class="h"></div>
        <span class="han">永</span>
      </div>
      <div class="lab"><b>田字格</b> — клетка с диагоналями: знак должен занять центр, а не угол</div>
    </div>
    <div class="steps">
%s
    </div>
  </div>

  <div class="foot">
    <div class="msg">Ребёнок к этому моменту <b>уже говорит</b> — ему остаётся связать звучание с начертанием</div>
    <div class="brand"><span class="dot2"></span><b>Kitai School</b><span>&middot; kitai-school.ru</span></div>
  </div>
</div>
</body></html>""" % (FONTS, VARS, steps)

info = info.replace("HGT", "560")
open(S + "yk-info.html", "w", encoding="utf-8").write(info)
print("ok")
