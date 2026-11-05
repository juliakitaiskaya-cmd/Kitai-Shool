# -*- coding: utf-8 -*-
# Картинки к статье «Сколько зарабатывают переводчики в Китае»
# Обложка     — три бирки форматов перевода, без сумм
# Инфографика — пять карточек источников и причина, почему цифре нельзя верить
S = ("/tmp/claude-0/-home-user-Kitai-Shool/a463bfca-82a9-56fd-ae09-42a7257ff999/"
     "scratchpad/")

FONTS = ("<link href=\"https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,600;0,700;1,600"
         "&family=Inter:wght@400;500;600;700&family=Noto+Serif+SC:wght@600;700&display=swap\" rel=\"stylesheet\">")
VARS = (":root{--brick:#A41E3A;--brick-d:#841630;--brick-soft:#F7E6EB;--ink:#2C2420;--ink-2:#5A4F45;"
        "--taupe:#8B7D6B;--cream:#FAF7F2;--cream-2:#F3EDE3;--hair:#EAE3D8;--surface:#fff;"
        "--paper:#FFFDF8;--gold:#B5873A;--gold-soft:#F6EEDF;--good:#2F6F4F}")

# ─────────── данные: три формата ───────────
# (знак, чтение, название, что меняется, насколько выше по прайсам)
FORMATS = [
    ("笔译", "bǐyì", "Письменный перевод",
     "работа со временем на обдумывание и правку", "основание"),
    ("交替传译", "jiāotì chuányì", "Последовательный перевод",
     "говорящий делает паузы, переводчик работает на месте", "выше письменного"),
    ("同声传译", "tóngshēng chuányì", "Синхронный перевод",
     "перевод идёт одновременно с речью, работают в паре", "выше последовательного"),
]

# ─────────── данные: источники и почему цифре нельзя верить ───────────
# (что за источник, что говорит, почему нельзя брать как есть)
SOURCES = [
    ("Зарплатный агрегатор", "медиана 12 000 ¥ в год", "выборка — 45 анонимных анкет"),
    ("Он же, устные переводчики", "около 8 000 ¥ в месяц", "выборка — 5 анкет"),
    ("Другой агрегатор", "3 740–12 978 ¥ в месяц", "в одной категории штатные и фрилансеры"),
    ("Оценка по модели", "около 205 000 ¥ в год", "не собранные данные, а расчёт"),
    ("Прайс бюро переводов", "синхрон 6 000–20 000 ¥ за день", "это цена для заказчика"),
]

# ── проверки данных
assert len(FORMATS) == 3, "форматов должно быть три"
assert len(SOURCES) == 5, "источников должно быть пять"
for t in SOURCES:
    assert all(x.strip() for x in t), "у источника не заполнено поле"
    assert len(t[2]) > 10, "у источника «%s» нет внятной оговорки" % t[0]
for zh, py, name, what, rel in FORMATS:
    assert not any(ch.isdigit() for ch in what), "на бирке не должно быть сумм: %s" % name
assert FORMATS[0][4] == "основание", "письменный перевод — точка отсчёта"
assert all("¥" in s[1] for s in SOURCES), "у источника должна стоять валюта"

tags = "".join(
    '<div class="tag%s"><div class="zh">%s</div><div class="py">%s</div>'
    '<div class="nm">%s</div><div class="wh">%s</div><div class="rel">%s</div>'
    '<span class="hole"></span></div>'
    % (" t%d" % i, zh, py, name, what, rel)
    for i, (zh, py, name, what, rel) in enumerate(FORMATS))

hero = """<!DOCTYPE html><html lang="ru"><head><meta charset="utf-8">
%(fonts)s
<style>
%(vars)s
*{margin:0;box-sizing:border-box}html,body{width:1200px;height:630px}
.card{width:1200px;height:630px;background:radial-gradient(1020px 680px at 12%% 8%%, #fff 0%%, var(--cream) 50%%, var(--cream-2) 100%%);position:relative;overflow:hidden;font-family:'Inter',sans-serif;padding:50px 52px 0 72px;display:flex;justify-content:space-between}
.card:before{content:"";position:absolute;left:0;top:0;bottom:0;width:12px;background:var(--brick)}
.txt{flex:0 0 452px;padding-top:10px}
.eyebrow{color:var(--brick);font-weight:700;font-size:18px;letter-spacing:.19em;text-transform:uppercase;margin-bottom:14px}
h1{font-family:'Cormorant Garamond',serif;font-weight:600;font-size:43px;line-height:1.06;color:var(--ink);letter-spacing:-.4px}
h1 i{font-style:italic;color:var(--brick)}
.sub{font-size:18px;color:var(--ink-2);line-height:1.42;max-width:29ch;margin-top:16px}
.tip{display:inline-block;margin-top:20px;background:var(--surface);border:1px solid var(--hair);border-left:4px solid var(--brick);border-radius:13px;padding:13px 18px;font-size:15.5px;color:var(--ink-2);line-height:1.38;max-width:32ch}
.tip b{color:var(--ink)}

.scene{flex:0 0 556px;display:flex;flex-direction:column;align-items:center;padding-top:4px}
.tags{display:flex;flex-direction:column;gap:12px;width:100%%}
.tag{position:relative;background:var(--paper);border:1px solid var(--hair);border-left:5px solid var(--brick);border-radius:12px;padding:13px 18px 13px 54px;box-shadow:0 8px 18px rgba(44,36,32,.1)}
.tag.t1{border-left-color:var(--gold)}
.tag.t2{border-left-color:var(--good)}
.hole{position:absolute;left:24px;top:50%%;width:13px;height:13px;border-radius:50%%;border:2px solid var(--hair);background:var(--cream-2);transform:translateY(-50%%)}
.zh{font-family:'Noto Serif SC',serif;font-weight:700;font-size:25px;color:var(--ink);line-height:1.1;display:inline-block}
.py{display:inline-block;font-size:12.5px;color:var(--taupe);margin-left:9px}
.nm{font-size:16.5px;font-weight:700;color:var(--ink);margin-top:4px}
.wh{font-size:14px;color:var(--ink-2);margin-top:3px;line-height:1.32}
.rel{display:inline-block;margin-top:7px;font-size:12px;font-weight:700;letter-spacing:.05em;text-transform:uppercase;color:var(--brick);background:var(--brick-soft);border-radius:7px;padding:3px 9px}
.under{margin-top:18px;text-align:center;font-size:15.5px;color:var(--ink-2);line-height:1.4;max-width:44ch}
.under b{color:var(--ink)}
.brand{position:absolute;left:72px;bottom:26px;display:flex;align-items:center;gap:11px;color:var(--ink)}
.brand b{font-family:'Cormorant Garamond',serif;font-weight:700;font-size:26px}
.brand .bdot{width:10px;height:10px;border-radius:50%%;background:var(--brick)}
.brand span{color:var(--taupe);font-size:16px}
</style></head><body>
<div class="card">
  <div class="txt">
    <div class="eyebrow">Работа с языком</div>
    <h1>Сколько зарабатывают переводчики в Китае: <i>единой цифры нет</i></h1>
    <div class="sub">Оплата зависит от формата работы, и разница между форматами больше, чем кажется.</div>
    <div class="tip"><b>Сумм на бирках нет намеренно:</b> цена агентства и гонорар переводчика — разные деньги.</div>
    <div class="brand"><span class="bdot"></span><b>Kitai School</b><span>&middot; kitai-school.ru</span></div>
  </div>

  <div class="scene">
    <div class="tags">%(tags)s</div>
    <div class="under">Чем меньше у переводчика времени на обдумывание, <b>тем дороже работа</b></div>
  </div>
</div>
</body></html>""" % dict(fonts=FONTS, vars=VARS, tags=tags)

open(S + "per-hero.html", "w", encoding="utf-8").write(hero)

# ─────────── инфографика: карточки источников ───────────
cards = "".join(
    '<div class="src"><div class="who">%s</div><div class="val">%s</div>'
    '<div class="why"><b>Почему нельзя брать как есть:</b> %s</div></div>'
    % t for t in SOURCES)

info = """<!DOCTYPE html><html lang="ru"><head><meta charset="utf-8">
%(fonts)s
<style>
%(vars)s
*{margin:0;box-sizing:border-box}html,body{width:1200px;height:%(h)dpx}
.wrap{width:1200px;height:%(h)dpx;background:linear-gradient(180deg,#fff 0%%,var(--cream) 40%%,var(--cream-2) 100%%);font-family:'Inter',sans-serif;padding:38px 48px 30px;display:flex;flex-direction:column;position:relative;overflow:hidden}
.wrap:before{content:"";position:absolute;left:0;right:0;top:0;height:9px;background:var(--brick)}
.top{display:flex;align-items:flex-end;justify-content:space-between;gap:34px;margin-bottom:26px}
.eyebrow{color:var(--brick);font-weight:700;font-size:15.5px;letter-spacing:.19em;text-transform:uppercase;margin-bottom:8px}
h2{font-family:'Cormorant Garamond',serif;font-weight:600;font-size:38px;line-height:1.07;color:var(--ink);max-width:20ch}
h2 i{font-style:italic;color:var(--brick)}
.hint{flex:0 0 408px;background:var(--surface);border:1px solid var(--hair);border-left:4px solid var(--brick);border-radius:13px;padding:12px 18px;font-size:15px;color:var(--ink-2);line-height:1.36}
.hint b{color:var(--ink)}

.grid{display:grid;grid-template-columns:repeat(5,1fr);gap:14px}
.src{background:var(--surface);border:1px solid var(--hair);border-top:5px solid var(--brick);border-radius:13px;padding:15px 15px 14px;display:flex;flex-direction:column}
.who{font-size:13px;font-weight:700;color:var(--taupe);letter-spacing:.04em;text-transform:uppercase;line-height:1.25;min-height:46px}
.val{font-family:'Cormorant Garamond',serif;font-weight:700;font-size:23px;color:var(--ink);line-height:1.18;margin-top:4px;min-height:84px}
.why{font-size:13px;color:var(--ink-2);line-height:1.34;border-top:1px solid var(--hair);padding-top:10px;margin-top:auto}
.why b{color:var(--brick);display:block;font-size:11.5px;letter-spacing:.06em;text-transform:uppercase;margin-bottom:4px}

.note{margin-top:24px;display:flex;gap:16px;align-items:stretch}
.nb{flex:1 1 0;background:var(--gold-soft);border:1px solid #E3D2B4;border-radius:14px;padding:14px 18px;font-size:15px;color:var(--ink);line-height:1.38}
.nb b{color:var(--gold)}

.foot{margin-top:auto;display:flex;align-items:center;gap:18px;padding-top:20px}
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
      <div class="eyebrow">Пять источников</div>
      <h2>Цифры есть — <i>но верить им как есть нельзя</i></h2>
    </div>
    <div class="hint">Это не разные профессии и не разные годы. Это <b>разные способы счёта</b>: у кого-то пять анкет, у кого-то расчёт по модели, а у кого-то вообще цена для заказчика.</div>
  </div>

  <div class="grid">%(cards)s</div>

  <div class="note">
    <div class="nb"><b>Главная путаница темы:</b> прайс бюро переводов — это то, что платит заказчик. Переводчику достаётся часть, и сколько именно, зависит от договора</div>
  </div>

  <div class="foot">
    <div class="msg">Поэтому в статье <b>нет вилок дохода</b>: привести их честно по таким источникам невозможно</div>
    <div class="brand"><span class="dot2"></span><b>Kitai School</b><span>&middot; kitai-school.ru</span></div>
  </div>
</div>
</body></html>""" % dict(fonts=FONTS, vars=VARS, h=640, cards=cards)

open(S + "per-info.html", "w", encoding="utf-8").write(info)

print("ok | форматов:", len(FORMATS), "| источников:", len(SOURCES))
print("на бирках сумм нет; у каждого источника есть оговорка")
