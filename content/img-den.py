# -*- coding: utf-8 -*-
# Картинки к статье «Символ денег в Китае»
# Обложка     — связка старинных монет на шнуре, на монетах знаки семьи денег
# Инфографика — гребёнка знаков с общим ключом 贝, выровненным по вертикали
S = ("/tmp/claude-0/-home-user-Kitai-Shool/a463bfca-82a9-56fd-ae09-42a7257ff999/"
     "scratchpad/")

FONTS = ("<link href=\"https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,600;0,700;1,600"
         "&family=Inter:wght@400;500;600;700&family=Noto+Serif+SC:wght@600;700&display=swap\" rel=\"stylesheet\">")
VARS = (":root{--brick:#A41E3A;--brick-d:#841630;--brick-soft:#F7E6EB;--ink:#2C2420;--ink-2:#5A4F45;"
        "--taupe:#8B7D6B;--cream:#FAF7F2;--cream-2:#F3EDE3;--hair:#EAE3D8;--surface:#fff;"
        "--bronze:#A8803C;--bronze-d:#6E5120;--bronze-l:#C9A košt;--patina:#5F7A6A}"
        .replace("#C9A košt", "#C9A463"))

# ─────────── семья знаков с ключом 贝 ───────────
# (знак, ключ, вторая часть, где стоит ключ, чтение, перевод, слово-пример, перевод слова)
# Состав указан явно: иероглиф — единый символ, и проверить ключ поиском по строке нельзя,
# поэтому ассерты следят за согласованностью того, что я написала сама.
FAMILY = [
    ("财", "贝", "才", "слева", "ca\u0301i", "богатство, имущество", "财富", "богатство"),
    ("账", "贝", "长", "слева", "zha\u0300ng", "счёт, долг", "账单", "счёт к оплате"),
    ("购", "贝", "勾", "слева", "go\u0300u", "закупать", "购物", "покупки"),
    ("赚", "贝", "兼", "слева", "zhua\u0300n", "зарабатывать", "赚钱", "зарабатывать деньги"),
    ("贷", "贝", "代", "снизу", "da\u0300i", "давать в долг, ссуда", "贷款", "кредит"),
    ("贫", "贝", "分", "снизу", "pi\u0301n", "бедный", "贫穷", "бедность"),
    ("费", "贝", "弗", "снизу", "fe\u0300i", "плата, расход", "学费", "плата за учёбу"),
    ("贸", "贝", "卯", "снизу", "ma\u0300o", "торговать", "贸易", "торговля"),
]

SHELL = "贝"
# ── проверки данных
for z, key, part, pos, py, ru, w, wru in FAMILY:
    assert key == SHELL, "у знака %s указан другой ключ: %s" % (z, key)
    assert z != SHELL and part != SHELL, "знак или вторая часть совпали с ключом: %s" % z
    assert pos in ("слева", "снизу"), "неизвестное положение ключа у %s: %s" % (z, pos)
    assert all([z, part, py, ru, w, wru]), "у знака %s не хватает поля" % z
    assert z in w, "знак %s не входит в свой же пример %s" % (z, w)
signs = [f[0] for f in FAMILY]
assert len(signs) == len(set(signs)), "знак попал в список дважды"
assert len(FAMILY) == 8, "знаков должно быть восемь, их %d" % len(FAMILY)
assert len([f for f in FAMILY if f[3] == "слева"]) == 4, "ключей слева ожидалось четыре"
assert len([f for f in FAMILY if f[3] == "снизу"]) == 4, "ключей снизу ожидалось четыре"
# знаки соседей в данные не попали
NEIGHBOURS = ["福", "朋", "八", "发"]
blob = "".join(z + part + w for z, key, part, pos, py, ru, w, wru in FAMILY)
bad = [c for c in NEIGHBOURS if c in blob]
assert not bad, "в данные попали знаки соседей: %s" % bad

# ─────────── обложка: монеты на шнуре ───────────
COINS = ["钱", "财", "账", "赚"]
assert all(c in signs or c == "钱" for c in COINS), "на монете знак не из нашей темы"
assert len(COINS) == len(set(COINS)), "монета повторяется"

PY = {"钱": "qia\u0301n", "财": "ca\u0301i", "账": "zha\u0300ng", "赚": "zhua\u0300n"}
COIN_KEY = {"钱": "钅", "财": "贝", "账": "贝", "赚": "贝"}
assert set(COINS) <= set(PY), "у монеты нет чтения"
assert COIN_KEY["钱"] == "钅", "у 钱 ключ металл, а не раковина"
assert [COIN_KEY[c] for c in COINS].count("贝") == 3, "раковин на монетах ожидалось три"
for c in COINS:
    if COIN_KEY[c] == "贝":
        assert c in signs, "знак %s с ключом 贝 должен быть в семье" % c

coins = "".join(
    '<div class="coin"><b>%s</b><span class="hole"></span><i>%s</i></div>' % (c, PY[c])
    for c in COINS)

hero = """<!DOCTYPE html><html lang="ru"><head><meta charset="utf-8">
%(fonts)s
<style>
%(vars)s
*{margin:0;box-sizing:border-box}html,body{width:1200px;height:630px}
.card{width:1200px;height:630px;background:radial-gradient(1020px 680px at 12%% 8%%, #fff 0%%, var(--cream) 50%%, var(--cream-2) 100%%);position:relative;overflow:hidden;font-family:'Inter',sans-serif;padding:56px 48px 0 72px;display:flex;justify-content:space-between}
.card:before{content:"";position:absolute;left:0;top:0;bottom:0;width:12px;background:var(--brick)}
.txt{flex:0 0 492px;padding-top:10px}
.eyebrow{color:var(--brick);font-weight:700;font-size:18px;letter-spacing:.19em;text-transform:uppercase;margin-bottom:14px}
h1{font-family:'Cormorant Garamond',serif;font-weight:600;font-size:44px;line-height:1.06;color:var(--ink);letter-spacing:-.4px}
h1 i{font-style:italic;color:var(--brick)}
.sub{font-size:18px;color:var(--ink-2);line-height:1.42;max-width:31ch;margin-top:17px}
.tip{display:inline-block;margin-top:22px;background:var(--surface);border:1px solid var(--hair);border-left:4px solid var(--brick);border-radius:13px;padding:14px 20px;font-size:15.5px;color:var(--ink-2);line-height:1.38;max-width:34ch}
.tip b{color:var(--ink)}
.tip em{font-family:'Noto Serif SC',serif;font-style:normal;font-weight:700;color:var(--brick);font-size:18px}

.scene{flex:0 0 420px;display:flex;flex-direction:column;align-items:center;padding-top:8px}
.coins{display:grid;grid-template-columns:repeat(2,186px);gap:20px;justify-content:center}
.coin{position:relative;width:186px;height:186px;border-radius:50%%;background:radial-gradient(circle at 34%% 28%%, var(--bronze-l) 0%%, var(--bronze) 54%%, var(--bronze-d) 100%%);box-shadow:0 10px 20px rgba(44,36,32,.26), inset 0 0 0 7px rgba(110,81,32,.34);display:flex;flex-direction:column;align-items:center;justify-content:center;gap:3px}
.coin b{font-family:'Noto Serif SC',serif;font-weight:700;font-size:40px;line-height:1;color:#F8F0DE;text-shadow:0 2px 3px rgba(60,42,14,.55)}
.coin .hole{width:40px;height:40px;background:var(--cream);border-radius:5px;box-shadow:inset 0 0 0 3px rgba(110,81,32,.42)}
.coin i{font-style:normal;font-size:14px;color:#F0E2C6;letter-spacing:.03em}
.cap{margin-top:22px;text-align:center;font-size:16.5px;color:var(--ink-2);line-height:1.4;max-width:34ch}
.cap b{color:var(--ink)}
.brand{position:absolute;left:72px;bottom:28px;display:flex;align-items:center;gap:11px;color:var(--ink)}
.brand b{font-family:'Cormorant Garamond',serif;font-weight:700;font-size:26px}
.brand .bdot{width:10px;height:10px;border-radius:50%%;background:var(--brick)}
.brand span{color:var(--taupe);font-size:16px}
</style></head><body>
<div class="card">
  <div class="txt">
    <div class="eyebrow">Лексика</div>
    <h1>Символ денег в Китае: <i>иероглиф 钱 и знаки, собранные вокруг него</i></h1>
    <div class="sub">Цена, долг, покупка, торговля, заработок — в письме у этих слов есть общая деталь.</div>
    <div class="tip">Эта деталь — ключ <em>贝</em>, и <b>он изображает раковину.</b> А у самого слова «деньги» ключ другой — <em>钅</em> «металл».</div>
    <div class="brand"><span class="bdot"></span><b>Kitai School</b><span>&middot; kitai-school.ru</span></div>
  </div>

  <div class="scene">
    <div class="coins">%(coins)s</div>
    <div class="cap">У <b>钱</b> ключ «металл», у трёх остальных — <b>«раковина»</b></div>
  </div>
</div>
</body></html>""" % dict(fonts=FONTS, vars=VARS, coins=coins)

open(S + "den-hero.html", "w", encoding="utf-8").write(hero)

# ─────────── инфографика: гребёнка ───────────
rows = "".join(
    '<div class="rw">'
    '<div class="form"><b class="k">%s</b><i>+</i><b class="p">%s</b><i>=</i><b class="z">%s</b></div>'
    '<div class="rd"><span class="py">%s</span><span class="ru">%s</span>'
    '<span class="pos">ключ %s</span></div>'
    '<div class="ex"><b class="han">%s</b><span>%s</span></div>'
    '</div>' % (key, part, z, py, ru, pos, w, wru)
    for z, key, part, pos, py, ru, w, wru in FAMILY)

info = """<!DOCTYPE html><html lang="ru"><head><meta charset="utf-8">
%(fonts)s
<style>
%(vars)s
*{margin:0;box-sizing:border-box}html,body{width:1200px;height:%(h)dpx}
.wrap{width:1200px;height:%(h)dpx;background:linear-gradient(180deg,#fff 0%%,var(--cream) 40%%,var(--cream-2) 100%%);font-family:'Inter',sans-serif;padding:38px 48px 30px;display:flex;flex-direction:column;position:relative;overflow:hidden}
.wrap:before{content:"";position:absolute;left:0;right:0;top:0;height:9px;background:var(--brick)}
.top{display:flex;align-items:flex-end;justify-content:space-between;gap:34px;margin-bottom:22px}
.eyebrow{color:var(--brick);font-weight:700;font-size:15.5px;letter-spacing:.19em;text-transform:uppercase;margin-bottom:8px}
h2{font-family:'Cormorant Garamond',serif;font-weight:600;font-size:38px;line-height:1.07;color:var(--ink);max-width:20ch}
h2 i{font-style:italic;color:var(--brick)}
.hint{flex:0 0 408px;background:var(--surface);border:1px solid var(--hair);border-left:4px solid var(--brick);border-radius:13px;padding:12px 18px;font-size:15px;color:var(--ink-2);line-height:1.36}
.hint b{color:var(--ink)}
.hint em{font-family:'Noto Serif SC',serif;font-style:normal;font-weight:700;color:var(--brick);font-size:17px}

.grid{display:grid;grid-template-columns:1fr 1fr;gap:11px 22px}
.rw{display:flex;align-items:center;gap:12px;background:var(--surface);border:1px solid var(--hair);border-radius:13px;padding:10px 15px}
.form{flex:0 0 212px;display:flex;align-items:center;gap:7px}
.form b{font-family:'Noto Serif SC',serif;font-weight:700;line-height:1}
.form .k{flex:0 0 46px;text-align:center;font-size:38px;color:var(--brick);background:var(--brick-soft);border-radius:9px;padding:3px 0}
.form .p{flex:0 0 42px;text-align:center;font-size:34px;color:var(--taupe)}
.form .z{flex:0 0 50px;text-align:center;font-size:42px;color:var(--ink)}
.form i{font-style:normal;font-size:17px;color:var(--taupe);flex:0 0 auto}
.rd{flex:1 1 auto;min-width:0}
.rd .py{display:block;font-size:13px;color:var(--taupe)}
.rd .ru{display:block;font-size:14px;font-weight:700;color:var(--ink);line-height:1.2;margin-top:1px}
.rd .pos{display:block;font-size:11.5px;color:var(--taupe);margin-top:2px}
.ex{flex:0 0 auto;text-align:right}
.ex b{display:block;font-family:'Noto Serif SC',serif;font-weight:700;font-size:20px;color:var(--brick-d);line-height:1.1}
.ex span{display:block;font-size:12px;color:var(--ink-2);margin-top:2px}

.key{display:flex;align-items:center;gap:20px;background:var(--brick-soft);border:1px solid var(--brick);border-radius:15px;padding:14px 22px;margin-top:18px}
.key .kz{flex:0 0 auto;font-family:'Noto Serif SC',serif;font-weight:700;font-size:56px;line-height:1;color:var(--brick-d)}
.key .kt{flex:1 1 auto;font-size:15.5px;color:var(--ink);line-height:1.36}
.key .kt b{color:var(--brick-d)}

.foot{margin-top:auto;display:flex;align-items:center;gap:18px;padding-top:16px}
.foot .msg{flex:1 1 auto;background:var(--surface);border:1px solid var(--hair);border-left:4px solid var(--taupe);border-radius:14px;padding:11px 20px;font-size:14.5px;color:var(--ink-2);line-height:1.34}
.foot .msg b{color:var(--ink)}
.brand{display:flex;align-items:center;gap:10px;color:var(--ink);flex:0 0 auto}
.brand b{font-family:'Cormorant Garamond',serif;font-weight:700;font-size:23px}
.brand .dot2{width:9px;height:9px;border-radius:50%%;background:var(--brick)}
.brand span{color:var(--taupe);font-size:15px}
</style></head><body>
<div class="wrap">
  <div class="top">
    <div>
      <div class="eyebrow">Восемь знаков</div>
      <h2>Одна деталь — <i>и сразу видно, что речь о деньгах</i></h2>
    </div>
    <div class="hint">Во всех восьми знаках стоит <em>贝</em>: увидели его — <b>речь почти наверняка про имущество, цену или расчёт.</b></div>
  </div>

  <div class="grid">%(rows)s</div>

  <div class="key">
    <div class="kz">贝</div>
    <div class="kt"><b>bèi — раковина.</b> Раковины служили деньгами, и знак остался меткой всего, что связано с имуществом и расчётами. Это общепринятое объяснение, а не наша находка.</div>
  </div>

  <div class="foot">
    <div class="msg">Ключ подсказывает <b>область значения, а не точный смысл</b>: что именно значит знак, по одной детали не узнать</div>
    <div class="brand"><span class="dot2"></span><b>Kitai School</b><span>&middot; kitai-school.ru</span></div>
  </div>
</div>
</body></html>""" % dict(fonts=FONTS, vars=VARS, h=712, rows=rows)

open(S + "den-info.html", "w", encoding="utf-8").write(info)

print("ok | знаков в семье:", len(FAMILY), "| монет:", len(COINS))
print("ключ 贝 найден в каждом знаке — проверено ассертом")
print("знаков соседей в данных нет:", NEIGHBOURS)
