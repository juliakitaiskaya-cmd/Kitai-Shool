# -*- coding: utf-8 -*-
# Картинки к статье «Простые предложения на китайском»
# Обложка     — пустая ячейка там, где русский требует глагола
# Инфографика — шесть моделей простого предложения с цветовой разметкой
S = ("/tmp/claude-0/-home-user-Kitai-Shool/a463bfca-82a9-56fd-ae09-42a7257ff999/"
     "scratchpad/")

FONTS = ("<link href=\"https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,600;0,700;1,600"
         "&family=Inter:wght@400;500;600;700&family=Noto+Serif+SC:wght@600;700&display=swap\" rel=\"stylesheet\">")
VARS = (":root{--brick:#A41E3A;--brick-d:#841630;--brick-soft:#F7E6EB;--ink:#2C2420;--ink-2:#5A4F45;"
        "--taupe:#8B7D6B;--cream:#FAF7F2;--cream-2:#F3EDE3;--hair:#EAE3D8;--surface:#fff;"
        "--sky:#39597F;--sky-soft:#E7EDF4;--good:#1E7A46;--good-soft:#E8F3EC}")

hero = """<!DOCTYPE html><html lang="ru"><head><meta charset="utf-8">
%(fonts)s
<style>
%(vars)s
*{margin:0;box-sizing:border-box}html,body{width:1200px;height:630px}
.card{width:1200px;height:630px;background:radial-gradient(1050px 660px at 14%% 10%%, #fff 0%%, var(--cream) 52%%, var(--cream-2) 100%%);position:relative;overflow:hidden;font-family:'Inter',sans-serif;padding:80px 56px 0 72px;display:flex;justify-content:space-between}
.card:before{content:"";position:absolute;left:0;top:0;bottom:0;width:12px;background:var(--brick)}
.txt{flex:0 0 448px;padding-top:4px}
.eyebrow{color:var(--brick);font-weight:700;font-size:18px;letter-spacing:.19em;text-transform:uppercase;margin-bottom:13px}
h1{font-family:'Cormorant Garamond',serif;font-weight:600;font-size:45px;line-height:1.07;color:var(--ink);letter-spacing:-.4px}
h1 i{font-style:italic;color:var(--brick)}
.sub{font-size:18px;color:var(--ink-2);line-height:1.42;max-width:29ch;margin-top:16px}
.tip{display:inline-block;margin-top:22px;background:var(--surface);border:1px solid var(--hair);border-left:4px solid var(--brick);border-radius:13px;padding:13px 19px;font-size:15.5px;color:var(--ink-2);line-height:1.36;max-width:33ch}
.tip b{color:var(--ink)}

.scene{flex:0 0 536px;padding-top:12px;display:flex;flex-direction:column;align-items:center}
.plate{background:var(--surface);border:1px solid var(--hair);border-radius:18px;padding:30px 30px 26px;box-shadow:0 14px 30px rgba(44,36,32,.13);text-align:center}
.row{display:flex;align-items:center;justify-content:center;gap:10px}
.han{font-family:'Noto Serif SC',serif;font-size:42px;color:var(--ink);line-height:1.15}
.gap{width:74px;height:54px;border:3px dashed var(--brick);border-radius:11px;background:var(--brick-soft);display:flex;align-items:center;justify-content:center;color:var(--brick);font-size:26px;font-weight:700}
.gaplb{margin-top:10px;font-size:13.5px;color:var(--brick);font-weight:700;letter-spacing:.02em}
.pin{margin-top:16px;font-size:15.5px;color:var(--ink-2);font-style:italic}
.tr{margin-top:3px;font-size:17px;color:var(--ink)}
.ru{margin-top:18px;padding-top:15px;border-top:1px solid var(--hair);font-size:16px;color:var(--ink-2)}
.ru b{color:var(--ink)}
.ru u{text-decoration:none;color:var(--brick);font-weight:700}
.cap{margin-top:24px;text-align:center;font-size:16.5px;color:var(--ink-2);line-height:1.42;max-width:42ch}
.cap b{color:var(--ink)}
.brand{position:absolute;left:72px;bottom:28px;display:flex;align-items:center;gap:11px;color:var(--ink)}
.brand b{font-family:'Cormorant Garamond',serif;font-weight:700;font-size:26px}
.brand .bdot{width:10px;height:10px;border-radius:50%%;background:var(--brick)}
.brand span{color:var(--taupe);font-size:16px}
</style></head><body>
<div class="card">
  <div class="txt">
    <div class="eyebrow">Грамматика</div>
    <h1>Простые предложения <i>на китайском</i></h1>
    <div class="sub">Сказуемым бывает не только глагол: ещё признак и даже существительное</div>
    <div class="tip"><b>Шесть моделей —</b> и почти вся бытовая речь складывается из них</div>
  </div>
  <div class="scene">
    <div class="plate">
      <div class="row">
        <span class="han">这个</span>
        <span class="gap"></span>
        <span class="han">五块钱</span>
      </div>
      <div class="gaplb">глагол сюда не ставится</div>
      <div class="pin">zhège wǔ kuài qián</div>
      <div class="tr">это пять юаней</div>
      <div class="ru">По-русски без глагола не обойтись: <b>это <u>стоит</u> пять юаней</b></div>
    </div>
    <div class="cap">Там, где русский требует сказуемого, <b>китайский обходится двумя существительными</b></div>
  </div>
  <div class="brand"><span class="bdot"></span><b>Kitai School</b><span>&middot; kitai-school.ru</span></div>
</div>
</body></html>""" % dict(fonts=FONTS, vars=VARS)

open(S + "prst-hero.html", "w", encoding="utf-8").write(hero)

# --------------------------------------------------------------- инфографика
# (название, схема как список (текст, роль), пример, перевод)
MODEL = [
    ("С 是", [("кто", "t"), ("是", "k"), ("кто или что", "x")],
     "他是学生", "он студент"),
    ("Качественное", [("кто", "t"), ("很", "k"), ("какой", "x")],
     "她很忙", "она занята"),
    ("Глагольное", [("кто", "t"), ("глагол", "k"), ("что", "x")],
     "我吃饭", "я ем"),
    ("С 有", [("у кого", "t"), ("有", "k"), ("что", "x")],
     "我有两个哥哥", "у меня два брата"),
    ("С 在", [("кто или что", "t"), ("在", "k"), ("где", "x")],
     "妈妈在厨房", "мама на кухне"),
    ("Без глагола", [("что", "t"), ("", "n"), ("признак", "x")],
     "这个五块钱", "это пять юаней"),
]

assert len(MODEL) == 6, "моделей не шесть"
assert sum(1 for m in MODEL if any(r == "n" for _, r in m[1])) == 1, \
    "модель без сказуемого должна быть одна"

ROLE = {"t": "тема", "k": "ядро сказуемого", "x": "остальное", "n": "пусто"}

rows = "".join(
    '<div class="mr"><div class="nm">%s</div>'
    '<div class="sch">%s</div>'
    '<div class="ex"><span class="hn">%s</span></div>'
    '<div class="tr">%s</div></div>'
    % (name,
       "".join('<span class="bk %s">%s</span>' % (r, t) for t, r in sch),
       ex, tr)
    for name, sch, ex, tr in MODEL)

legend = "".join('<span class="lg"><i class="bk %s"></i>%s</span>' % (k, v)
                 for k, v in (("t", ROLE["t"]), ("k", ROLE["k"]), ("x", ROLE["x"])))

info = """<!DOCTYPE html><html lang="ru"><head><meta charset="utf-8">
%(fonts)s
<style>
%(vars)s
*{margin:0;box-sizing:border-box}html,body{width:1200px;height:640px}
.wrap{width:1200px;height:640px;background:linear-gradient(180deg,#fff 0%%,var(--cream) 46%%,var(--cream-2) 100%%);font-family:'Inter',sans-serif;padding:30px 46px 26px;display:flex;flex-direction:column}
.top{display:flex;align-items:flex-end;justify-content:space-between;gap:30px;margin-bottom:14px}
.eyebrow{color:var(--brick);font-weight:700;font-size:14.5px;letter-spacing:.17em;text-transform:uppercase;margin-bottom:7px}
h2{font-family:'Cormorant Garamond',serif;font-weight:600;font-size:38px;line-height:1.07;color:var(--ink);letter-spacing:-.3px}
h2 i{font-style:italic;color:var(--brick)}
.hint{flex:0 0 392px;background:var(--surface);border:1px solid var(--hair);border-left:4px solid var(--brick);border-radius:12px;padding:12px 17px;font-size:14.5px;color:var(--ink-2);line-height:1.36}
.hint b{color:var(--ink)}

.leg{display:flex;gap:18px;margin-bottom:11px;padding-left:2px}
.lg{display:flex;align-items:center;gap:7px;font-size:13px;color:var(--ink-2)}
.lg .bk{width:22px;height:13px;padding:0;border-radius:4px}

.mr{display:flex;align-items:center;gap:14px;background:var(--surface);border:1px solid var(--hair);border-radius:13px;padding:10px 16px;margin-bottom:8px;box-shadow:0 3px 9px rgba(44,36,32,.04)}
.nm{flex:0 0 132px;font-size:14.5px;font-weight:700;color:var(--ink)}
.sch{flex:0 0 352px;display:flex;gap:5px}
.bk{display:inline-flex;align-items:center;justify-content:center;font-size:12.5px;border-radius:6px;padding:7px 9px;white-space:nowrap}
.bk.t{background:var(--cream-2);color:var(--ink-2)}
.bk.k{background:var(--brick);color:#fff;font-weight:700;font-family:'Noto Serif SC',serif;font-size:15px}
.bk.x{background:var(--sky-soft);color:var(--sky)}
.bk.n{background:#fff;border:2px dashed var(--taupe);min-width:40px}
.ex{flex:0 0 196px}
.ex .hn{font-family:'Noto Serif SC',serif;font-size:24px;color:var(--ink);line-height:1.15}
.mr .tr{flex:1 1 auto;font-size:14.5px;color:var(--ink-2)}

.foot{margin-top:auto;display:flex;align-items:center;gap:18px;padding-top:12px}
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
      <div class="eyebrow">Простое предложение</div>
      <h2>Шесть моделей, <i>и ни одной лишней</i></h2>
    </div>
    <div class="hint">Кирпичным отмечено ядро сказуемого. <b>В последней модели его нет вовсе — и предложение всё равно целое.</b></div>
  </div>

  <div class="leg">%(legend)s</div>
  %(rows)s

  <div class="foot">
    <div class="msg">Деление рабочее, а не единственно возможное — <b>в разных описаниях моделей насчитывают по-своему</b></div>
    <div class="brand"><span class="dot2"></span><b>Kitai School</b><span>&middot; kitai-school.ru</span></div>
  </div>
</div>
</body></html>""" % dict(fonts=FONTS, vars=VARS, legend=legend, rows=rows)

open(S + "prst-info.html", "w", encoding="utf-8").write(info)
print("ok | моделей:", len(MODEL))

# примеры не должны совпадать с примерами статьи-родителя
PARENT = ["我是老师", "我喝茶", "他很高", "我学汉语", "他学汉语", "你学汉语", "我找他",
          "他找我", "书放在桌子上", "我在家学汉语", "他住在北京", "我的中文书"]
mine = [m[2] for m in MODEL] + ["这个五块钱"]
for p in PARENT:
    for x in mine:
        assert p not in x and x not in p, "пример пересекается с родителем: %s / %s" % (p, x)
print("пересечений примеров с «Как составлять предложения»: нет")
