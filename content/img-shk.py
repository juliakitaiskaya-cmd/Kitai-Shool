# -*- coding: utf-8 -*-
# Картинки к статье «Правила в китайских школах»
# Обложка     — школьная форма на вешалке
# Инфографика — лист свода 中小学生守则 без текста и шесть правил с метками
S = ("/tmp/claude-0/-home-user-Kitai-Shool/a463bfca-82a9-56fd-ae09-42a7257ff999/"
     "scratchpad/")

FONTS = ("<link href=\"https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,600;0,700;1,600"
         "&family=Inter:wght@400;500;600;700&family=Noto+Serif+SC:wght@600;700&display=swap\" rel=\"stylesheet\">")
VARS = (":root{--brick:#A41E3A;--brick-d:#841630;--brick-soft:#F7E6EB;--ink:#2C2420;--ink-2:#5A4F45;"
        "--taupe:#8B7D6B;--cream:#FAF7F2;--cream-2:#F3EDE3;--hair:#EAE3D8;--surface:#fff;"
        "--navy:#2E3B52;--navy-d:#1F2838;--navy-l:#44556F;--good:#1E7A46;--good-soft:#E8F3EC;"
        "--sky:#39597F;--sky-soft:#E7EDF4;--paper:#FBF7EC}")

hero = """<!DOCTYPE html><html lang="ru"><head><meta charset="utf-8">
%(fonts)s
<style>
%(vars)s
*{margin:0;box-sizing:border-box}html,body{width:1200px;height:630px}
.card{width:1200px;height:630px;background:radial-gradient(1050px 660px at 14%% 10%%, #fff 0%%, var(--cream) 52%%, var(--cream-2) 100%%);position:relative;overflow:hidden;font-family:'Inter',sans-serif;padding:76px 56px 0 72px;display:flex;justify-content:space-between}
.card:before{content:"";position:absolute;left:0;top:0;bottom:0;width:12px;background:var(--brick)}
.txt{flex:0 0 470px;padding-top:4px}
.eyebrow{color:var(--brick);font-weight:700;font-size:18px;letter-spacing:.19em;text-transform:uppercase;margin-bottom:13px}
h1{font-family:'Cormorant Garamond',serif;font-weight:600;font-size:45px;line-height:1.07;color:var(--ink);letter-spacing:-.4px}
h1 i{font-style:italic;color:var(--brick)}
.sub{font-size:18px;color:var(--ink-2);line-height:1.42;max-width:30ch;margin-top:16px}
.tip{display:inline-block;margin-top:22px;background:var(--surface);border:1px solid var(--hair);border-left:4px solid var(--brick);border-radius:13px;padding:13px 19px;font-size:15.5px;color:var(--ink-2);line-height:1.36;max-width:34ch}
.tip b{color:var(--ink)}

.scene{flex:0 0 520px;padding-top:0;display:flex;flex-direction:column;align-items:center}
.rail{width:330px;height:5px;border-radius:3px;background:var(--hair)}
.hook{width:26px;height:30px;border:5px solid var(--taupe);border-left:none;border-bottom:none;border-radius:0 16px 0 0;margin:-3px auto 0;transform:translateX(-11px)}
.bar{width:214px;height:5px;background:var(--taupe);border-radius:3px;margin:0 auto;position:relative}
.bar:before,.bar:after{content:"";position:absolute;top:-40px;width:5px;height:44px;background:var(--taupe);border-radius:3px}
.bar:before{left:0;transform:rotate(26deg);transform-origin:bottom left}
.bar:after{right:0;transform:rotate(-26deg);transform-origin:bottom right}
.jacket{position:relative;width:272px;height:252px;margin:-6px auto 0;background:linear-gradient(140deg,var(--navy-l) 0%%,var(--navy) 46%%,var(--navy-d) 100%%);clip-path:polygon(28%% 0%%,72%% 0%%,100%% 15%%,100%% 47%%,79%% 52%%,79%% 100%%,21%% 100%%,21%% 52%%,0%% 47%%,0%% 15%%);filter:drop-shadow(0 16px 26px rgba(44,36,32,.26))}
.jacket .zip{position:absolute;left:50%%;top:9%%;bottom:0;width:2px;background:rgba(255,255,255,.3);transform:translateX(-50%%)}
.jacket .st{position:absolute;top:17%%;height:31%%;width:9px;background:rgba(255,255,255,.72)}
.jacket .st.l{left:5%%}
.jacket .st.r{right:5%%}
.jacket .band{position:absolute;left:21%%;right:21%%;bottom:0;height:16px;background:rgba(255,255,255,.14)}
.jacket .col{position:absolute;left:28%%;right:28%%;top:0;height:16px;background:rgba(255,255,255,.2)}
.tag{position:absolute;right:-26px;top:120px;background:var(--surface);border:1px solid var(--hair);border-radius:14px;padding:12px 18px 14px;box-shadow:0 10px 20px rgba(44,36,32,.18);text-align:center}
.tag .h{font-family:'Noto Serif SC',serif;font-size:28px;color:var(--ink);line-height:1.15}
.tag .p{font-size:13.5px;color:var(--ink-2);font-style:italic;margin-top:3px}
.tag .r{font-size:14.5px;color:var(--brick);font-weight:700;margin-top:1px}
.wrapj{position:relative;width:330px}
.cap{margin-top:24px;text-align:center;font-size:16.5px;color:var(--ink-2);line-height:1.42;max-width:40ch}
.note{margin-top:20px;background:var(--surface);border:1px solid var(--hair);border-radius:13px;padding:12px 20px;font-size:15px;color:var(--ink-2);line-height:1.4;text-align:center;max-width:450px}
.note b{color:var(--brick)}
.cap b{color:var(--ink)}
.brand{position:absolute;left:72px;bottom:28px;display:flex;align-items:center;gap:11px;color:var(--ink)}
.brand b{font-family:'Cormorant Garamond',serif;font-weight:700;font-size:26px}
.brand .bdot{width:10px;height:10px;border-radius:50%%;background:var(--brick)}
.brand span{color:var(--taupe);font-size:16px}
</style></head><body>
<div class="card">
  <div class="txt">
    <div class="eyebrow">Образование</div>
    <h1>Правила <i>в китайских школах</i></h1>
    <div class="sub">Форма каждый день, телефон остаётся дома, линейка по понедельникам</div>
    <div class="tip"><b>Часть правил одинакова почти везде,</b> часть каждая школа устанавливает сама — и это две разные вещи</div>
  </div>
  <div class="scene">
    <div class="rail"></div>
    <div class="hook"></div>
    <div class="wrapj">
      <div class="bar"></div>
      <div class="jacket">
        <div class="col"></div><div class="zip"></div>
        <div class="st l"></div><div class="st r"></div><div class="band"></div>
      </div>
      <div class="tag">
        <div class="h">校服</div>
        <div class="p">xiàofú</div>
        <div class="r">школьная форма</div>
      </div>
    </div>
    <div class="cap">Форма чаще спортивного кроя <b>и одинаковая для всех</b> — её носят каждый учебный день</div>
    <div class="note">А вот причёска, длина волос и украшения — <b>это уже решает конкретная школа</b></div>
  </div>
  <div class="brand"><span class="bdot"></span><b>Kitai School</b><span>&middot; kitai-school.ru</span></div>
</div>
</body></html>""" % dict(fonts=FONTS, vars=VARS)

open(S + "shk-hero.html", "w", encoding="utf-8").write(hero)

# --------------------------------------------------------------- инфографика
RULES = [
    ("校服", "xiàofú", "Форма каждый учебный день", "почти везде", "all"),
    ("手机", "shǒujī", "Телефон в школу не приносят", "по указанию", "doc"),
    ("升旗仪式", "shēngqí yíshì", "Линейка в начале недели", "почти везде", "all"),
    ("早读", "zǎodú", "Чтение вслух до первого урока", "часто", "often"),
    ("发型", "fàxíng", "Требования к причёске и виду", "решает школа", "own"),
    ("请假", "qǐngjià", "Пропуск — только по заявлению", "почти везде", "all"),
]

MARKS = {"all": "почти везде", "doc": "по указанию", "often": "часто",
         "own": "решает школа"}
for r in RULES:
    assert r[3] == MARKS[r[4]], "метка и подпись разошлись: %s" % r[0]
assert sum(1 for r in RULES if r[4] == "own") == 1, "правило школы должно быть одно"

rules = "".join(
    '<div class="rl"><div class="rh">%s</div><div class="rp">%s</div>'
    '<div class="rt">%s</div><div class="rm %s">%s</div></div>'
    % (han, py, txt, cls, mark) for han, py, txt, mark, cls in RULES)

lines = "".join('<div class="ln">%s</div>' % ('<i></i>' * 7) for _ in range(9))

info = """<!DOCTYPE html><html lang="ru"><head><meta charset="utf-8">
%(fonts)s
<style>
%(vars)s
*{margin:0;box-sizing:border-box}html,body{width:1200px;height:700px}
.wrap{width:1200px;height:700px;background:linear-gradient(180deg,#fff 0%%,var(--cream) 46%%,var(--cream-2) 100%%);font-family:'Inter',sans-serif;padding:30px 46px 26px;display:flex;flex-direction:column}
.top{display:flex;align-items:flex-end;justify-content:space-between;gap:30px;margin-bottom:18px}
.eyebrow{color:var(--brick);font-weight:700;font-size:14.5px;letter-spacing:.17em;text-transform:uppercase;margin-bottom:7px}
h2{font-family:'Cormorant Garamond',serif;font-weight:600;font-size:38px;line-height:1.07;color:var(--ink);letter-spacing:-.3px}
h2 i{font-style:italic;color:var(--brick)}
.hint{flex:0 0 392px;background:var(--surface);border:1px solid var(--hair);border-left:4px solid var(--brick);border-radius:12px;padding:12px 17px;font-size:14.5px;color:var(--ink-2);line-height:1.36}
.hint b{color:var(--ink)}

.body{display:flex;gap:22px;flex:0 0 auto}
.sheet{flex:0 0 360px;background:var(--paper);border:1px solid var(--hair);border-radius:14px;padding:20px 22px 18px;box-shadow:0 10px 20px rgba(44,36,32,.09);position:relative}
.sheet:before{content:"";position:absolute;left:50%%;top:-9px;transform:translateX(-50%%);width:18px;height:18px;border-radius:50%%;background:var(--brick);box-shadow:0 2px 5px rgba(44,36,32,.3)}
.sh{font-family:'Noto Serif SC',serif;font-size:25px;color:var(--ink);text-align:center;line-height:1.2}
.sp{font-size:13px;color:var(--ink-2);font-style:italic;text-align:center;margin-top:2px}
.sq{font-size:13.5px;color:var(--ink-2);text-align:center;margin-top:3px}
.lines{margin-top:15px;display:flex;flex-direction:column;gap:9px}
.ln{display:flex;gap:6px;justify-content:center}
.ln i{width:30px;height:21px;border-radius:5px;background:#E4DCC9}
.sfoot{margin-top:16px;font-size:13.5px;color:var(--brick-d);text-align:center;font-weight:700;line-height:1.35}

.right{flex:1 1 auto;display:flex;flex-direction:column}
.sep{display:flex;align-items:center;gap:14px;margin-bottom:11px}
.sep span{font-size:15px;font-weight:700;color:var(--brick-d);white-space:nowrap}
.sep i{flex:1 1 auto;height:1px;background:var(--hair)}
.grid{display:flex;flex-wrap:wrap;gap:11px}
.rl{flex:0 0 calc(50%% - 6px);background:var(--surface);border:1px solid var(--hair);border-radius:13px;padding:11px 15px 12px;box-shadow:0 3px 9px rgba(44,36,32,.04)}
.rh{font-family:'Noto Serif SC',serif;font-size:22px;color:var(--ink);line-height:1.15}
.rp{font-size:12.5px;color:var(--ink-2);font-style:italic}
.rt{font-size:14px;color:var(--ink);margin-top:4px;line-height:1.3}
.rm{display:inline-block;margin-top:7px;font-size:12.5px;font-weight:700;border-radius:999px;padding:4px 11px}
.rm.all{background:var(--good-soft);color:var(--good)}
.rm.doc{background:var(--sky-soft);color:var(--sky)}
.rm.often{background:var(--cream-2);color:var(--ink-2)}
.rm.own{background:var(--brick-soft);color:var(--brick-d)}

.foot{margin-top:auto;display:flex;align-items:center;gap:18px;padding-top:16px}
.foot .msg{flex:1 1 auto;background:var(--brick-soft);border:1px solid var(--brick);border-radius:14px;padding:11px 21px;font-size:15px;color:var(--ink);line-height:1.34}
.foot .msg b{color:var(--brick)}
.brand{display:flex;align-items:center;gap:10px;color:var(--ink);flex:0 0 auto}
.brand b{font-family:'Cormorant Garamond',serif;font-weight:700;font-size:23px}
.brand .dot2{width:9px;height:9px;border-radius:50%%;background:var(--brick)}
.brand span{color:var(--taupe);font-size:15px}
</style></head><body>
<div class="wrap">
  <div class="top">
    <div>
      <div class="eyebrow">Школьные правила</div>
      <h2>Общий свод <i>и правила каждой школы</i></h2>
    </div>
    <div class="hint">Есть короткий государственный свод для всех и есть распорядок, который школа устанавливает сама. <b>Путать их не стоит.</b></div>
  </div>

  <div class="body">
    <div class="sheet">
      <div class="sh">中小学生守则</div>
      <div class="sp">Zhōng xiǎo xuéshēng shǒuzé</div>
      <div class="sq">правила для учащихся, лист на стене</div>
      <div class="lines">%(lines)s</div>
      <div class="sfoot">Девять строк по семь знаков.<br>Целиком не цитируем: ручаться за каждое слово не могу</div>
    </div>
    <div class="right">
      <div class="sep"><span>Как это выглядит в обычный день</span><i></i></div>
      <div class="grid">%(rules)s</div>
    </div>
  </div>

  <div class="foot">
    <div class="msg">Всё описанное — <b>про обычную городскую государственную школу</b>; частные и международные живут иначе</div>
    <div class="brand"><span class="dot2"></span><b>Kitai School</b><span>&middot; kitai-school.ru</span></div>
  </div>
</div>
</body></html>""" % dict(fonts=FONTS, vars=VARS, lines=lines, rules=rules)

open(S + "shk-info.html", "w", encoding="utf-8").write(info)
print("ok | правил:", len(RULES), "| строк свода: 9")
