# -*- coding: utf-8 -*-
# Картинки к статье «„Привет“ по-китайски»
# Обложка    — две клавиши клавиатуры: 你 и 好
# Инфографика — детали пазла: из чего собран каждый знак
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
.card{width:1200px;height:630px;background:radial-gradient(1100px 680px at 15%% 10%%, #fff 0%%, var(--cream) 55%%, var(--cream-2) 100%%);position:relative;overflow:hidden;font-family:'Inter',sans-serif;display:flex;align-items:center;justify-content:space-between;padding:0 70px 0 72px}
.card:before{content:"";position:absolute;left:0;top:0;bottom:0;width:12px;background:var(--brick)}
.txt{flex:0 0 500px}
.eyebrow{color:var(--brick);font-weight:700;font-size:18px;letter-spacing:.19em;text-transform:uppercase;margin-bottom:12px}
h1{font-family:'Cormorant Garamond',serif;font-weight:600;font-size:50px;line-height:1.06;color:var(--ink);letter-spacing:-.4px;max-width:490px}
h1 i{font-style:italic;color:var(--brick)}
.sub{font-size:18px;color:var(--ink-2);line-height:1.42;max-width:31ch;margin-top:16px}
.brand{position:absolute;left:72px;bottom:32px;display:flex;align-items:center;gap:11px;color:var(--ink)}
.brand b{font-family:'Cormorant Garamond',serif;font-weight:700;font-size:26px}
.brand .bdot{width:10px;height:10px;border-radius:50%%;background:var(--brick)}
.brand span{color:var(--taupe);font-size:16px}

/* две клавиши */
.keys{flex:0 0 532px;display:flex;flex-direction:column;align-items:center;gap:22px}
.sum{display:flex;align-items:center;gap:14px;background:var(--surface);border:1px solid var(--hair);border-radius:14px;padding:11px 22px;box-shadow:0 4px 14px rgba(44,36,32,.06)}
.sum .h{font-family:'Noto Serif SC',serif;font-weight:700;font-size:30px;color:var(--brick);line-height:1}
.sum .p{font-size:17px;font-weight:600;color:var(--ink)}
.sum .t{font-size:15px;color:var(--taupe)}
.krow{display:flex;gap:30px;align-items:flex-start}
.kwrap{text-align:center}
.key{width:186px;height:186px;border-radius:20px;background:linear-gradient(180deg,#fff 0%%,#F4EFE7 72%%,#E6DCCB 100%%);border:1px solid #D9CFBD;box-shadow:0 12px 0 #D5C9B4, 0 20px 30px rgba(44,36,32,.22);display:flex;align-items:center;justify-content:center;position:relative}
.key:after{content:"";position:absolute;left:13px;right:13px;top:11px;height:62px;border-radius:14px;background:linear-gradient(180deg,rgba(255,255,255,.95),rgba(255,255,255,0))}
.key span{font-family:'Noto Serif SC',serif;font-weight:700;font-size:96px;line-height:1;color:var(--ink);position:relative;z-index:1}
.kwrap .py{font-size:22px;font-weight:600;color:var(--brick);margin-top:20px;letter-spacing:.02em}
.kwrap .ru{font-size:15px;color:var(--taupe);margin-top:2px}
.nokey{width:100%%;background:var(--surface);border:1px solid var(--hair);border-left:4px solid var(--brick);border-radius:14px;padding:13px 20px;font-size:16px;color:var(--ink-2);line-height:1.36}
.nokey b{color:var(--ink)}
</style></head><body>
<div class="card">
  <div class="txt">
    <div class="eyebrow">Первые слова</div>
    <h1>«Привет»<br><i>по-китайски</i></h1>
    <div class="sub">Это два знака, а не один: 你 «ты» и 好 «хорошо». И у каждого своя сборка</div>
  </div>
  <div class="keys">
    <div class="krow">
      <div class="kwrap">
        <div class="key"><span>你</span></div>
        <div class="py">nǐ</div>
        <div class="ru">ты</div>
      </div>
      <div class="kwrap">
        <div class="key"><span>好</span></div>
        <div class="py">hǎo</div>
        <div class="ru">хорошо</div>
      </div>
    </div>
    <div class="sum"><span class="h">你好</span><span class="p">nǐ hǎo</span><span class="t">&middot; привет, здравствуйте</span></div>
    <div class="nokey">Клавиши со значением <b>«здравствуйте»</b> не существует — как и такого иероглифа</div>
  </div>
  <div class="brand"><span class="bdot"></span><b>Kitai School</b><span>&middot; kitai-school.ru</span></div>
</div>
</body></html>""" % (FONTS, VARS)

open(S + "pv-hero.html", "w", encoding="utf-8").write(hero)

# -------------------------------------------------------------- инфографика
# знак, чтение, перевод, (деталь1, подпись1), (деталь2, подпись2), черт, вывод
SIGNS = [
    ("你", "nǐ", "ты",
     ("亻", "«человек» — ключ, отвечает за смысл"),
     ("尔", "подсказывает звучание"),
     "7", "знак слева-направо: сначала пишут 亻"),
    ("好", "hǎo", "хорошо",
     ("女", "«женщина»"),
     ("子", "«ребёнок»"),
     "6", "в приветствии значит «хорошо», а не «добрый»"),
    ("您", "nín", "вы (вежливо)",
     ("你", "«ты» целиком, сверху"),
     ("心", "«сердце», снизу"),
     "11", "вежливая форма: к 你 добавлено 心"),
]

rows = "\n".join(
    '<div class="sign">'
    '  <div class="tile"><span class="g">%s</span><span class="py">%s</span><span class="tr">%s</span></div>'
    '  <div class="eq">=</div>'
    '  <div class="pieces">'
    '    <div class="pc"><span class="ph">%s</span><span class="pl">%s</span></div>'
    '    <div class="plus">+</div>'
    '    <div class="pc r"><span class="ph">%s</span><span class="pl">%s</span></div>'
    '  </div>'
    '  <div class="meta"><span class="n">%s</span><span class="nl">ЧЕРТ</span><span class="note">%s</span></div>'
    '</div>' % (g, py, tr, d1[0], d1[1], d2[0], d2[1], n, note)
    for g, py, tr, d1, d2, n, note in SIGNS)

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
.hint{flex:0 0 352px;background:var(--surface);border:1px solid var(--hair);border-left:4px solid var(--brick);border-radius:12px;padding:12px 17px;font-size:14.5px;color:var(--ink-2);line-height:1.36}
.hint b{color:var(--ink)}

.signs{display:flex;flex-direction:column;gap:16px}
.sign{display:flex;align-items:center;gap:20px;background:var(--surface);border:1px solid var(--hair);border-radius:16px;padding:15px 22px;box-shadow:0 5px 16px rgba(44,36,32,.05)}
.tile{flex:0 0 136px;text-align:center;background:var(--cream);border:1px solid var(--hair);border-radius:13px;padding:10px 6px 11px}
.tile .g{display:block;font-family:'Noto Serif SC',serif;font-weight:700;font-size:52px;line-height:1.02;color:var(--brick)}
.tile .py{display:block;font-size:15px;font-weight:600;color:var(--ink);margin-top:5px}
.tile .tr{display:block;font-size:12.5px;color:var(--taupe);margin-top:1px}
.eq{flex:0 0 auto;font-family:'Cormorant Garamond',serif;font-weight:600;font-size:40px;color:var(--taupe);line-height:1}

/* детали пазла */
.pieces{flex:1 1 auto;display:flex;align-items:center;gap:26px}
.pc{flex:1 1 0;position:relative;background:var(--cream-2);border:1.5px solid #DCD2C2;border-radius:12px;padding:13px 20px 13px 22px;display:flex;align-items:center;gap:15px;min-height:84px}
.pc:after{content:"";position:absolute;right:-13px;top:50%%;transform:translateY(-50%%);width:24px;height:24px;border-radius:50%%;background:var(--cream-2);border:1.5px solid #DCD2C2;clip-path:inset(0 0 0 50%%)}
.pc.r{background:var(--brick-soft);border-color:#E7C9D2}
.pc.r:before{content:"";position:absolute;left:-2px;top:50%%;transform:translateY(-50%%);width:24px;height:24px;border-radius:50%%;background:var(--surface);border:1.5px solid #E7C9D2;clip-path:inset(0 50%% 0 0)}
.pc.r:after{display:none}
.pc .ph{flex:0 0 auto;font-family:'Noto Serif SC',serif;font-weight:700;font-size:38px;line-height:1;color:var(--ink)}
.pc.r .ph{color:var(--brick)}
.pc .pl{font-size:14.5px;color:var(--ink-2);line-height:1.34}
.plus{flex:0 0 auto;font-family:'Cormorant Garamond',serif;font-weight:600;font-size:34px;color:var(--taupe);line-height:1}

.meta{flex:0 0 184px;text-align:center;border-left:1px solid var(--hair);padding-left:18px}
.meta .n{display:block;font-family:'Cormorant Garamond',serif;font-weight:700;font-size:44px;line-height:1;color:var(--ink)}
.meta .nl{display:block;font-size:10.5px;font-weight:700;letter-spacing:.12em;color:var(--taupe);margin-top:2px}
.meta .note{display:block;font-size:12.5px;color:var(--ink-2);line-height:1.32;margin-top:7px}

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
      <div class="eyebrow">Из чего собрано приветствие</div>
      <h2>Два знака — и каждый <i>сам собран из частей</i></h2>
    </div>
    <div class="hint">Одного иероглифа со значением «здравствуйте» нет. <b>你好 — это два знака</b>, и внутри каждого видно, из чего он сложен.</div>
  </div>

  <div class="signs">
%s
  </div>

  <div class="foot">
    <div class="msg">Записывается <b>nǐ hǎo</b>, а звучит <b>ní hǎo</b>: два третьих тона подряд, первый читается вторым</div>
    <div class="brand"><span class="dot2"></span><b>Kitai School</b><span>&middot; kitai-school.ru</span></div>
  </div>
</div>
</body></html>""" % (FONTS, VARS, rows)

info = info.replace("HGT", "716")
open(S + "pv-info.html", "w", encoding="utf-8").write(info)
print("ok")
