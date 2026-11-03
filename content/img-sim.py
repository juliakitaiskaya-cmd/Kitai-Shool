# -*- coding: utf-8 -*-
# Картинки к статье «Символы китайской культуры»
# Обложка     — круг тайцзи с подписями 阴 и 阳
# Инфографика — шесть красных печатей, по одной на символ
S = ("/tmp/claude-0/-home-user-Kitai-Shool/a463bfca-82a9-56fd-ae09-42a7257ff999/"
     "scratchpad/")

FONTS = ("<link href=\"https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,600;0,700;1,600"
         "&family=Inter:wght@400;500;600;700&family=Noto+Serif+SC:wght@600;700&display=swap\" rel=\"stylesheet\">")
VARS = (":root{--brick:#A41E3A;--brick-d:#841630;--brick-soft:#F7E6EB;--ink:#2C2420;--ink-2:#5A4F45;"
        "--taupe:#8B7D6B;--cream:#FAF7F2;--cream-2:#F3EDE3;--hair:#EAE3D8;--surface:#fff;"
        "--seal:#B0202F;--seal-d:#7E1420;--yin:#2C2420;--yang:#FBF7EF}")

# ─────────── шесть символов ───────────
# (знак, чтение, русское название, одна строка значения)
SYMBOLS = [
    ("龙", "lóng", "Дракон", "власть и благая сила, связан с водой"),
    ("凤凰", "fènghuáng", "Феникс", "парный дракону образ"),
    ("太极", "tàijí", "Тайцзи", "знак, в котором соединены инь и ян"),
    ("麒麟", "qílín", "Цилинь", "благовещее существо"),
    ("龟", "guī", "Черепаха", "долголетие и устойчивость"),
    ("鹤", "hè", "Журавль", "долголетие, часто в паре с сосной"),
]

# ── проверки данных
assert len(SYMBOLS) == 6, "символов должно быть шесть, их %d" % len(SYMBOLS)
signs = [s[0] for s in SYMBOLS]
assert len(signs) == len(set(signs)), "символ назван дважды"
for z, py, ru, mean in SYMBOLS:
    assert all([z, py, ru, mean]), "у символа %s не хватает поля" % z
    assert len(mean) <= 46, "строка значения у %s длиннее кадра" % z
# занятое соседями в данные не попало
TAKEN = ["熊猫", "福", "囍", "红", "黄", "紫"]
blob = "".join(z for z, py, ru, mean in SYMBOLS)
bad = [c for c in TAKEN if c in blob]
assert not bad, "в данные попало занятое соседями: %s" % bad
assert "панд" not in " ".join(s[2] + s[3] for s in SYMBOLS).lower(), "панда разбирается у соседа"

# ─────────── обложка ───────────
hero = """<!DOCTYPE html><html lang="ru"><head><meta charset="utf-8">
%(fonts)s
<style>
%(vars)s
*{margin:0;box-sizing:border-box}html,body{width:1200px;height:630px}
.card{width:1200px;height:630px;background:radial-gradient(1020px 680px at 12%% 8%%, #fff 0%%, var(--cream) 50%%, var(--cream-2) 100%%);position:relative;overflow:hidden;font-family:'Inter',sans-serif;padding:56px 52px 0 72px;display:flex;justify-content:space-between}
.card:before{content:"";position:absolute;left:0;top:0;bottom:0;width:12px;background:var(--brick)}
.txt{flex:0 0 520px;padding-top:12px}
.eyebrow{color:var(--brick);font-weight:700;font-size:18px;letter-spacing:.19em;text-transform:uppercase;margin-bottom:14px}
h1{font-family:'Cormorant Garamond',serif;font-weight:600;font-size:44px;line-height:1.06;color:var(--ink);letter-spacing:-.4px}
h1 i{font-style:italic;color:var(--brick)}
.sub{font-size:18px;color:var(--ink-2);line-height:1.42;max-width:32ch;margin-top:17px}
.tip{display:inline-block;margin-top:22px;background:var(--surface);border:1px solid var(--hair);border-left:4px solid var(--brick);border-radius:13px;padding:14px 20px;font-size:15.5px;color:var(--ink-2);line-height:1.38;max-width:35ch}
.tip b{color:var(--ink)}

.scene{flex:0 0 448px;display:flex;flex-direction:column;align-items:center;padding-top:10px}
.tj{position:relative;width:412px;height:412px;border-radius:50%%;background:linear-gradient(90deg,var(--yang) 0%%,var(--yang) 50%%,var(--yin) 50%%,var(--yin) 100%%);box-shadow:0 16px 34px rgba(44,36,32,.24);overflow:hidden;border:2px solid #2C2420}
.tj:before,.tj:after{content:"";position:absolute;left:50%%;width:206px;height:206px;border-radius:50%%;transform:translateX(-50%%)}
.tj:before{top:0;background:var(--yang)}
.tj:after{bottom:0;background:var(--yin)}
.dot{position:absolute;left:50%%;width:64px;height:64px;border-radius:50%%;transform:translateX(-50%%);z-index:3}
.dot.a{top:71px;background:var(--yin)}
.dot.b{bottom:71px;background:var(--yang)}
.lbl{position:absolute;z-index:4;font-family:'Noto Serif SC',serif;font-weight:700;font-size:46px}
.lbl.l{left:70px;top:50%%;transform:translateY(-50%%);color:var(--yin)}
.lbl.r{right:70px;top:50%%;transform:translateY(-50%%);color:var(--yang)}
.tjwrap{position:relative;width:412px;height:412px}
.cap{margin-top:26px;text-align:center;font-size:16.5px;color:var(--ink-2);line-height:1.42;max-width:32ch}
.cap b{color:var(--ink)}
.brand{position:absolute;left:72px;bottom:28px;display:flex;align-items:center;gap:11px;color:var(--ink)}
.brand b{font-family:'Cormorant Garamond',serif;font-weight:700;font-size:26px}
.brand .bdot{width:10px;height:10px;border-radius:50%%;background:var(--brick)}
.brand span{color:var(--taupe);font-size:16px}
</style></head><body>
<div class="card">
  <div class="txt">
    <div class="eyebrow">Культура</div>
    <h1>Символы китайской культуры: <i>дракон, инь-ян и смыслы, которые они несут</i></h1>
    <div class="sub">За привычными образами стоят идеи — и почти всегда не те, которых ждёшь со стороны.</div>
    <div class="tip"><b>Инь и ян — не добро и зло</b> и не борьба: это две стороны одного, и внутри каждой есть часть другой.</div>
    <div class="brand"><span class="bdot"></span><b>Kitai School</b><span>&middot; kitai-school.ru</span></div>
  </div>

  <div class="scene">
    <div class="tjwrap">
      <div class="tj"><span class="dot a"></span><span class="dot b"></span></div>
      <span class="lbl l">阳</span>
      <span class="lbl r">阴</span>
    </div>
    <div class="cap">Знак называется <b>太极</b> — «великий предел»</div>
  </div>
</div>
</body></html>""" % dict(fonts=FONTS, vars=VARS)

open(S + "sim-hero.html", "w", encoding="utf-8").write(hero)

# ─────────── инфографика: шесть печатей ───────────
seals = "".join(
    '<div class="sl"><div class="seal"><b>%s</b></div>'
    '<div class="nm">%s</div><div class="py">%s</div><div class="mn">%s</div></div>'
    % (z, ru, py, mean) for z, py, ru, mean in SYMBOLS)

# четыре темы, разобранные отдельно
ELSEWHERE = ["панда", "цвета", "числа", "знак счастья"]
assert len(ELSEWHERE) == 4, "ссылок должно быть четыре"
links = " · ".join(ELSEWHERE)

info = """<!DOCTYPE html><html lang="ru"><head><meta charset="utf-8">
%(fonts)s
<style>
%(vars)s
*{margin:0;box-sizing:border-box}html,body{width:1200px;height:%(h)dpx}
.wrap{width:1200px;height:%(h)dpx;background:linear-gradient(180deg,#fff 0%%,var(--cream) 40%%,var(--cream-2) 100%%);font-family:'Inter',sans-serif;padding:38px 48px 30px;display:flex;flex-direction:column;position:relative;overflow:hidden}
.wrap:before{content:"";position:absolute;left:0;right:0;top:0;height:9px;background:var(--brick)}
.top{display:flex;align-items:flex-end;justify-content:space-between;gap:34px;margin-bottom:26px}
.eyebrow{color:var(--brick);font-weight:700;font-size:15.5px;letter-spacing:.19em;text-transform:uppercase;margin-bottom:8px}
h2{font-family:'Cormorant Garamond',serif;font-weight:600;font-size:38px;line-height:1.07;color:var(--ink);max-width:19ch}
h2 i{font-style:italic;color:var(--brick)}
.hint{flex:0 0 404px;background:var(--surface);border:1px solid var(--hair);border-left:4px solid var(--brick);border-radius:13px;padding:12px 18px;font-size:15px;color:var(--ink-2);line-height:1.36}
.hint b{color:var(--ink)}

.grid{display:grid;grid-template-columns:repeat(3,1fr);gap:26px 22px}
.sl{text-align:center}
.seal{width:132px;height:132px;margin:0 auto 12px;border-radius:9px;background:linear-gradient(160deg,var(--seal) 0%%,var(--seal-d) 100%%);display:flex;align-items:center;justify-content:center;box-shadow:0 10px 20px rgba(126,20,32,.26);position:relative}
.seal:before{content:"";position:absolute;inset:7px;border:2px solid rgba(255,245,235,.5);border-radius:5px}
.seal b{font-family:'Noto Serif SC',serif;font-weight:700;font-size:48px;line-height:1;color:#FFF3E6;position:relative;z-index:2;letter-spacing:-2px}
.nm{font-size:17px;font-weight:700;color:var(--ink)}
.py{font-size:13px;color:var(--taupe);margin-top:1px}
.mn{font-size:13.5px;color:var(--ink-2);line-height:1.32;margin-top:6px;padding:0 6px}

.else{display:flex;align-items:center;gap:16px;background:var(--surface);border:1px solid var(--hair);border-radius:14px;padding:13px 20px;margin-top:26px}
.else .lb{flex:0 0 auto;font-size:15px;font-weight:700;color:var(--ink)}
.else .ls{flex:1 1 auto;font-size:14.5px;color:var(--ink-2)}

.foot{margin-top:auto;display:flex;align-items:center;gap:18px;padding-top:18px}
.foot .msg{flex:1 1 auto;background:var(--brick-soft);border:1px solid var(--brick);border-radius:14px;padding:11px 20px;font-size:14.5px;color:var(--ink);line-height:1.34}
.foot .msg b{color:var(--brick)}
.brand{display:flex;align-items:center;gap:10px;color:var(--ink);flex:0 0 auto}
.brand b{font-family:'Cormorant Garamond',serif;font-weight:700;font-size:23px}
.brand .dot2{width:9px;height:9px;border-radius:50%%;background:var(--brick)}
.brand span{color:var(--taupe);font-size:15px}
</style></head><body>
<div class="wrap">
  <div class="top">
    <div>
      <div class="eyebrow">Шесть символов</div>
      <h2>Что они значат — <i>и чего от них не ждут</i></h2>
    </div>
    <div class="hint">Порядка по важности тут нет: <b>назначать главный символ — дело вкуса, а не справки.</b></div>
  </div>

  <div class="grid">%(seals)s</div>

  <div class="else">
    <span class="lb">Разобрано отдельно:</span>
    <span class="ls">%(links)s — у каждого своя страница, и пересказывать её здесь незачем</span>
  </div>

  <div class="foot">
    <div class="msg">Мифических существ показываем <b>как образы</b>: преданий о их происхождении тут нет — версии расходятся</div>
    <div class="brand"><span class="dot2"></span><b>Kitai School</b><span>&middot; kitai-school.ru</span></div>
  </div>
</div>
</body></html>""" % dict(fonts=FONTS, vars=VARS, h=742, seals=seals, links=links)

open(S + "sim-info.html", "w", encoding="utf-8").write(info)

print("ok | символов:", len(SYMBOLS), "| ссылок на соседей:", len(ELSEWHERE))
print("занятого соседями в данных нет:", TAKEN)
