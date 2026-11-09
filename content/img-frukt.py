# -*- coding: utf-8 -*-
# Картинки к статье «Счётное слово для фруктов»
# Обложка     — ценники на прилавке: у соседних товаров разные единицы счёта
# Инфографика — уровни дробления: один виноград и три способа его сосчитать
S = ("/tmp/claude-0/-home-user-Kitai-Shool/a463bfca-82a9-56fd-ae09-42a7257ff999/"
     "scratchpad/")

FONTS = ("<link href=\"https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,600;0,700;1,600"
         "&family=Inter:wght@400;500;600;700&family=Noto+Serif+SC:wght@500;600;700&display=swap\" rel=\"stylesheet\">")
VARS = (":root{--brick:#A41E3A;--brick-d:#841630;--brick-soft:#F7E6EB;--ink:#2C2420;--ink-2:#5A4F45;"
        "--taupe:#8B7D6B;--cream:#FAF7F2;--cream-2:#F3EDE3;--hair:#EAE3D8;--surface:#fff;"
        "--good:#2F6F4F;--good-soft:#E8F3EC;--grey:#8A8178;--grey-soft:#EFEDE8}")

# ─────────── данные: способы счёта ───────────
# продукт, чтение, перевод, классификатор, что именно считают, пример, перевод примера
WAYS = [
    ("苹果", "píngguǒ", "яблоко", "个", "плод целиком", "两个苹果", "два яблока"),
    ("葡萄", "pútáo", "виноград", "串", "гроздь", "一串葡萄", "гроздь винограда"),
    ("葡萄", "pútáo", "виноград", "颗", "отдельная ягода", "一颗葡萄", "одна виноградина"),
    ("米", "mǐ", "рис", "粒", "зёрнышко", "一粒米", "зёрнышко риса"),
    ("水果", "shuǐguǒ", "фрукты", "盘", "порция на тарелке", "一盘水果", "тарелка фруктов"),
]
# уровни дробления одного продукта: что берут, классификатор, пример, перевод
LEVELS = [
    ("целая гроздь", "串", "一串葡萄", "гроздь винограда"),
    ("одна ягода", "颗", "一颗葡萄", "одна виноградина"),
    ("порция на тарелке", "盘", "一盘葡萄", "тарелка винограда"),
]
DISPUTED = ("草莓", "cǎoméi", "клубника", "источники расходятся: встречается и 颗, и 个")
BAD = ["лучш", "хуже", "сложн", "легк", "красив", "правильн", "вкусн"]

# ── проверки данных
assert len(WAYS) == 5, "способов счёта должно быть пять"
assert len(LEVELS) == 3, "уровней дробления должно быть три"
grape = [w for w in WAYS if w[0] == "葡萄"]
assert len(grape) > 1, "у винограда должно быть больше одного способа счёта"
assert len(set(w[3] for w in grape)) == len(grape), "у винограда классификаторы должны различаться"
for zh, py, ru, cl, what, ex, exru in WAYS:
    assert zh and py and ru and cl and what and ex and exru, "у %s заполнены не все поля" % zh
    for v in (ru, what, exru):
        assert not any(b in v.lower() for b in BAD), "оценочное слово: %s" % v
assert all(w[3] not in ("瓣", "篮") for w in WAYS), "瓣 и 篮 не подтвердились"
assert DISPUTED[3].startswith("источники расходятся"), "у спорного случая нужна пометка"
assert len(set(l[1] for l in LEVELS)) == 3, "на уровнях классификаторы не должны повторяться"

# ─────────── обложка: ценники на прилавке ───────────
tags = ""
for zh, py, ru, cl, what, ex, exru in WAYS[:4]:
    tags += """  <div class="tag">
    <div class="hole"></div>
    <div class="name">%s</div>
    <div class="py">%s · %s</div>
    <div class="unit"><b>%s</b><span>%s</span></div>
    <div class="ex">%s</div>
    <div class="exru">%s</div>
  </div>""" % (zh, py, ru, cl, what, ex, exru)

hero = """<!DOCTYPE html><html lang="ru"><head><meta charset="utf-8">
%(fonts)s
<style>
%(vars)s
*{margin:0;box-sizing:border-box}html,body{width:1200px;height:630px}
.card{width:1200px;height:630px;background:radial-gradient(1040px 700px at 10%% 6%%, #fff 0%%, var(--cream) 52%%, var(--cream-2) 100%%);position:relative;overflow:hidden;font-family:'Inter',sans-serif;padding:32px 56px 54px 72px;display:flex;flex-direction:column}
.card:before{content:"";position:absolute;left:0;top:0;bottom:0;width:12px;background:var(--brick)}
.head{display:flex;justify-content:space-between;align-items:flex-end;gap:34px;margin-bottom:22px}
.eyebrow{color:var(--brick);font-weight:700;font-size:18px;letter-spacing:.19em;text-transform:uppercase;margin-bottom:10px}
h1{font-family:'Cormorant Garamond',serif;font-weight:600;font-size:36px;line-height:1.07;color:var(--ink);letter-spacing:-.3px;max-width:25ch}
h1 i{font-style:italic;color:var(--brick)}
h1 i em{font-family:'Noto Serif SC',serif;font-style:normal;font-weight:600;font-size:.94em;white-space:nowrap}
.tip{flex:0 0 330px;background:var(--surface);border:1px solid var(--hair);border-left:4px solid var(--brick);border-radius:13px;padding:13px 18px;font-size:15px;color:var(--ink-2);line-height:1.38}
.tip b{color:var(--ink)}

.shelf{display:flex;gap:16px;align-items:stretch}
.tag{flex:1 1 0;position:relative;background:#FFFEFA;border:1px solid var(--hair);border-radius:12px;padding:26px 16px 16px;text-align:center;box-shadow:0 2px 0 rgba(44,36,32,.04)}
.tag:before{content:"";position:absolute;left:0;right:0;top:0;height:7px;background:var(--brick);border-radius:12px 12px 0 0}
.hole{position:absolute;top:13px;left:50%%;transform:translateX(-50%%);width:13px;height:13px;border-radius:50%%;background:var(--cream-2);border:1px solid var(--hair)}
.tag .name{font-family:'Noto Serif SC',serif;font-weight:700;font-size:31px;color:var(--ink);line-height:1.1;margin-top:8px}
.tag .py{font-size:12.5px;color:var(--taupe);margin-top:2px}
.unit{margin:11px 0 9px;padding:8px 0;border-top:1px dashed var(--hair);border-bottom:1px dashed var(--hair)}
.unit b{display:block;font-family:'Noto Serif SC',serif;font-size:34px;color:var(--brick);line-height:1}
.unit span{display:block;font-size:12.5px;color:var(--taupe);margin-top:3px}
.tag .ex{font-family:'Noto Serif SC',serif;font-size:21px;color:var(--ink);line-height:1.2}
.tag .exru{font-size:12.5px;color:var(--ink-2);margin-top:3px}

.note{margin-top:16px;background:var(--brick-soft);border:1px solid var(--brick);border-radius:13px;padding:12px 22px;font-size:15.5px;color:var(--ink);line-height:1.36}
.note b{color:var(--brick)}

.brand{position:absolute;left:72px;bottom:19px;display:flex;align-items:center;gap:11px;color:var(--ink)}
.brand b{font-family:'Cormorant Garamond',serif;font-weight:700;font-size:26px}
.brand .bdot{width:10px;height:10px;border-radius:50%%;background:var(--brick)}
.brand span{color:var(--taupe);font-size:16px}
</style></head><body>
<div class="card">
  <div class="head">
    <div>
      <div class="eyebrow">Лексика</div>
      <h1>Счётное слово для фруктов: <i><em>个</em> для яблока, <em>串</em> для винограда, <em>颗</em> для мелких</i></h1>
    </div>
    <div class="tip">На одном прилавке — <b>разные единицы счёта</b>. Слово зависит не от фрукта, а от того, что вы берёте.</div>
  </div>

  <div class="shelf">
%(tags)s
  </div>

  <div class="note">У винограда сразу два слова: <b>一串</b> — это гроздь, <b>一颗</b> — одна ягода. Перепутать их значит получить не то, что просили</div>

  <div class="brand"><span class="bdot"></span><b>Kitai School</b><span>&middot; kitai-school.ru</span></div>
</div>
</body></html>""" % dict(fonts=FONTS, vars=VARS, tags=tags)

open(S + "frukt-hero.html", "w", encoding="utf-8").write(hero)

# ─────────── инфографика: уровни дробления ───────────
steps = ""
for i, (what, cl, ex, ru) in enumerate(LEVELS, start=1):
    steps += ('<div class="lv"><div class="n">%d</div>'
              '<div class="what">%s</div>'
              '<div class="cl">%s</div>'
              '<div class="ex"><b>%s</b><span>%s</span></div></div>' % (i, what, cl, ex, ru))

info = """<!DOCTYPE html><html lang="ru"><head><meta charset="utf-8">
%(fonts)s
<style>
%(vars)s
*{margin:0;box-sizing:border-box}html,body{width:1200px;height:%(h)dpx}
.wrap{width:1200px;height:%(h)dpx;background:linear-gradient(180deg,#fff 0%%,var(--cream) 42%%,var(--cream-2) 100%%);font-family:'Inter',sans-serif;padding:38px 48px 26px;display:flex;flex-direction:column;position:relative;overflow:hidden}
.wrap:before{content:"";position:absolute;left:0;right:0;top:0;height:9px;background:var(--brick)}
.top{display:flex;align-items:flex-end;justify-content:space-between;gap:34px;margin-bottom:24px}
.eyebrow{color:var(--brick);font-weight:700;font-size:15.5px;letter-spacing:.19em;text-transform:uppercase;margin-bottom:8px}
h2{font-family:'Cormorant Garamond',serif;font-weight:600;font-size:38px;line-height:1.07;color:var(--ink);max-width:22ch}
h2 i{font-style:italic;color:var(--brick)}
.hint{flex:0 0 388px;background:var(--surface);border:1px solid var(--hair);border-left:4px solid var(--brick);border-radius:13px;padding:12px 18px;font-size:15px;color:var(--ink-2);line-height:1.36}
.hint b{color:var(--ink)}

.body{display:flex;gap:24px;align-items:stretch}
.levels{flex:1 1 auto;display:flex;flex-direction:column;gap:12px}
.lv{display:flex;align-items:center;gap:16px;background:var(--surface);border:1px solid var(--hair);border-left:5px solid var(--brick);border-radius:13px;padding:14px 18px}
.lv .n{flex:0 0 auto;width:28px;height:28px;border-radius:50%%;background:var(--brick);color:#fff;font-size:14px;font-weight:700;display:flex;align-items:center;justify-content:center}
.lv .what{flex:0 0 212px;font-size:16px;font-weight:600;color:var(--ink)}
.lv .cl{flex:0 0 72px;font-family:'Noto Serif SC',serif;font-weight:700;font-size:38px;color:var(--brick);line-height:1;text-align:center}
.lv .ex{flex:1 1 auto}
.lv .ex b{display:block;font-family:'Noto Serif SC',serif;font-size:24px;color:var(--ink);line-height:1.15}
.lv .ex span{display:block;font-size:13.5px;color:var(--taupe);margin-top:2px}

.aside{flex:0 0 280px;background:var(--grey-soft);border:1px dashed var(--taupe);border-radius:14px;padding:16px 18px;display:flex;flex-direction:column;justify-content:center}
.aside .ttl{font-size:11.5px;font-weight:700;letter-spacing:.1em;text-transform:uppercase;color:var(--taupe);margin-bottom:9px}
.aside .zh{font-family:'Noto Serif SC',serif;font-weight:700;font-size:34px;color:var(--grey);line-height:1.1}
.aside .py{font-size:13px;color:var(--taupe);margin-top:2px}
.aside p{font-size:14px;color:var(--ink-2);line-height:1.34;margin-top:10px}

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
      <div class="eyebrow">Один продукт, три единицы</div>
      <h2>Слово меняется вместе с тем, <i>что вы берёте</i></h2>
    </div>
    <div class="hint">Виноград остаётся виноградом, а счётное слово — <b>нет</b>. Оно называет не продукт, а то, в каком виде его берут.</div>
  </div>

  <div class="body">
    <div class="levels">%(steps)s</div>
    <div class="aside">
      <div class="ttl">спорный случай</div>
      <div class="zh">%(dz)s</div>
      <div class="py">%(dpy)s — %(dru)s</div>
      <p>%(dnote)s. Выбирать за источники я не стала</p>
    </div>
  </div>

  <div class="foot">
    <div class="msg">Проверка простая: <b>спросите себя, что именно вы держите в руках</b> — плод, гроздь или тарелку</div>
    <div class="brand"><span class="dot2"></span><b>Kitai School</b><span>&middot; kitai-school.ru</span></div>
  </div>
</div>
</body></html>""" % dict(fonts=FONTS, vars=VARS, h=556, steps=steps,
                         dz=DISPUTED[0], dpy=DISPUTED[1], dru=DISPUTED[2], dnote=DISPUTED[3])

open(S + "frukt-info.html", "w", encoding="utf-8").write(info)

print("ok | способов счёта:", len(WAYS), "| уровней:", len(LEVELS),
      "| у винограда вариантов:", len(grape))
print("瓣 и 篮 в данных нет; спорный случай помечен")
