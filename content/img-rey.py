# -*- coding: utf-8 -*-
# Картинки к статье «Социальный рейтинг в Китае»
# Обложка     — две колонки: как пересказывают и что по документам
# Инфографика — три системы по одинаковому набору признаков
S = ("/tmp/claude-0/-home-user-Kitai-Shool/a463bfca-82a9-56fd-ae09-42a7257ff999/"
     "scratchpad/")

FONTS = ("<link href=\"https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,600;0,700;1,600"
         "&family=Inter:wght@400;500;600;700&family=Noto+Serif+SC:wght@600;700&display=swap\" rel=\"stylesheet\">")
VARS = (":root{--brick:#A41E3A;--brick-d:#841630;--brick-soft:#F7E6EB;--ink:#2C2420;--ink-2:#5A4F45;"
        "--taupe:#8B7D6B;--cream:#FAF7F2;--cream-2:#F3EDE3;--hair:#EAE3D8;--surface:#fff;"
        "--paper:#FFFDF8;--good:#2F6F4F;--good-soft:#E8F3EC;--grey:#8A8178;--grey-soft:#EFEDE8}")

# ─────────── данные: пары «пересказ / устройство» ───────────
PAIRS = [
    ("Один общий балл у каждого жителя", "Единого балла нет: есть списки и реестры"),
    ("Баллы растут и падают за поступки", "Попадание в список — по решению суда, а не по сумме баллов"),
    ("Система касается всех и каждого", "Основная часть реестров относится к компаниям"),
    ("Рейтинг в приложении — часть системы", "Рейтинги платёжных сервисов коммерческие и добровольные"),
]

# ─────────── данные: три системы по признакам ───────────
ROWS = ["Кто ведёт", "Кого касается", "Есть ли баллы", "Участие", "Чем грозит"]
SYSTEMS = [
    ("Список должников", "失信被执行人", [
        "суды", "тех, кто не исполнил решение суда", "нет, есть факт в списке",
        "по решению суда", "ограничения на дорогие покупки и поездки"]),
    ("Корпоративный кредит", "企业信用", [
        "ведомства", "компании и их руководителей", "оценки и категории по отраслям",
        "обязательное для компаний", "проверки, допуск к закупкам, ограничения"]),
    ("Рейтинг в приложении", "芝麻信用", [
        "частные компании", "пользователей сервиса", "да, собственный балл сервиса",
        "добровольное", "условия сервиса: залог, рассрочка, лимиты"]),
]

BAD = ["ужас", "страшн", "антиутоп", "тоталитар", "хорош", "плох", "правильн", "свобод"]

# ── проверки данных
assert len(PAIRS) == 4, "пар должно быть четыре"
assert len(SYSTEMS) == 3, "систем должно быть три"
assert len(ROWS) == 5, "признаков должно быть пять"
for name, zh, vals in SYSTEMS:
    assert len(vals) == len(ROWS), "у системы «%s» не %d признаков" % (name, len(ROWS))
    for v in vals:
        low = v.lower()
        assert not any(b in low for b in BAD), "оценочное слово в признаке: %s" % v
for left, right in PAIRS:
    for v in (left, right):
        assert not any(b in v.lower() for b in BAD), "оценочное слово в паре: %s" % v
assert SYSTEMS[0][2][2].startswith("нет"), "в судебном списке баллов нет"
assert "добровольн" in SYSTEMS[2][2][3], "коммерческий рейтинг — добровольный"

pairs_html = "".join(
    '<div class="pr"><div class="lf">%s</div><div class="rg">%s</div></div>' % p
    for p in PAIRS)

hero = """<!DOCTYPE html><html lang="ru"><head><meta charset="utf-8">
%(fonts)s
<style>
%(vars)s
*{margin:0;box-sizing:border-box}html,body{width:1200px;height:630px}
.card{width:1200px;height:630px;background:radial-gradient(1020px 680px at 12%% 8%%, #fff 0%%, var(--cream) 50%%, var(--cream-2) 100%%);position:relative;overflow:hidden;font-family:'Inter',sans-serif;padding:46px 48px 0 72px;display:flex;flex-direction:column}
.card:before{content:"";position:absolute;left:0;top:0;bottom:0;width:12px;background:var(--brick)}
.head{display:flex;justify-content:space-between;align-items:flex-end;gap:30px;margin-bottom:22px}
.eyebrow{color:var(--brick);font-weight:700;font-size:18px;letter-spacing:.19em;text-transform:uppercase;margin-bottom:12px}
h1{font-family:'Cormorant Garamond',serif;font-weight:600;font-size:42px;line-height:1.07;color:var(--ink);letter-spacing:-.4px;max-width:19ch}
h1 i{font-style:italic;color:var(--brick)}
.tip{flex:0 0 376px;background:var(--surface);border:1px solid var(--hair);border-left:4px solid var(--brick);border-radius:13px;padding:13px 18px;font-size:15px;color:var(--ink-2);line-height:1.38}
.tip b{color:var(--ink)}

.cols{display:flex;gap:0;font-size:12.5px;font-weight:700;letter-spacing:.12em;text-transform:uppercase;color:var(--taupe);margin-bottom:8px}
.cols span:first-child{flex:1 1 0;padding-left:16px}
.cols span:last-child{flex:1 1 0;padding-left:30px;color:var(--brick)}
.pairs{display:flex;flex-direction:column;gap:11px}
.pr{display:flex;align-items:stretch;gap:14px}
.lf,.rg{flex:1 1 0;border-radius:11px;padding:15px 18px;font-size:15.5px;line-height:1.36}
.lf{background:var(--grey-soft);border:1px solid #E2DED6;color:var(--grey)}
.rg{background:var(--surface);border:1px solid var(--hair);border-left:4px solid var(--good);color:var(--ink)}
.note{margin-top:20px;font-size:15px;color:var(--ink-2);line-height:1.4;max-width:92ch}
.brand{position:absolute;left:72px;bottom:24px;display:flex;align-items:center;gap:11px;color:var(--ink)}
.brand b{font-family:'Cormorant Garamond',serif;font-weight:700;font-size:26px}
.brand .bdot{width:10px;height:10px;border-radius:50%%;background:var(--brick)}
.brand span{color:var(--taupe);font-size:16px}
</style></head><body>
<div class="card">
  <div class="head">
    <div>
      <div class="eyebrow">Как устроено</div>
      <h1>Социальный рейтинг в Китае: <i>что из этого правда</i></h1>
    </div>
    <div class="tip">Слева — <b>как тему обычно пересказывают</b>, справа — что удалось подтвердить по документам и разборам.</div>
  </div>

  <div class="cols"><span>Как пересказывают</span><span>Что по документам</span></div>
  <div class="pairs">%(pairs)s</div>

  <div class="note">Ни одна строка справа не выдумана: это то, что удалось найти в открытых разборах и юридических источниках. Там, где подтверждения нет, в статье так и написано</div>

  <div class="brand"><span class="bdot"></span><b>Kitai School</b><span>&middot; kitai-school.ru</span></div>
</div>
</body></html>""" % dict(fonts=FONTS, vars=VARS, pairs=pairs_html)

open(S + "rey-hero.html", "w", encoding="utf-8").write(hero)

# ─────────── инфографика: три системы по признакам ───────────
heads = "".join(
    '<div class="sy"><div class="nm">%s</div><div class="zh">%s</div></div>'
    % (name, zh) for name, zh, vals in SYSTEMS)

body_rows = ""
for i, label in enumerate(ROWS):
    cells = "".join('<div class="cl">%s</div>' % s[2][i] for s in SYSTEMS)
    body_rows += '<div class="rw"><div class="lb">%s</div>%s</div>' % (label, cells)

info = """<!DOCTYPE html><html lang="ru"><head><meta charset="utf-8">
%(fonts)s
<style>
%(vars)s
*{margin:0;box-sizing:border-box}html,body{width:1200px;height:%(h)dpx}
.wrap{width:1200px;height:%(h)dpx;background:linear-gradient(180deg,#fff 0%%,var(--cream) 40%%,var(--cream-2) 100%%);font-family:'Inter',sans-serif;padding:38px 48px 30px;display:flex;flex-direction:column;position:relative;overflow:hidden}
.wrap:before{content:"";position:absolute;left:0;right:0;top:0;height:9px;background:var(--brick)}
.top{display:flex;align-items:flex-end;justify-content:space-between;gap:34px;margin-bottom:26px}
.eyebrow{color:var(--brick);font-weight:700;font-size:15.5px;letter-spacing:.19em;text-transform:uppercase;margin-bottom:8px}
h2{font-family:'Cormorant Garamond',serif;font-weight:600;font-size:38px;line-height:1.07;color:var(--ink);max-width:21ch}
h2 i{font-style:italic;color:var(--brick)}
.hint{flex:0 0 404px;background:var(--surface);border:1px solid var(--hair);border-left:4px solid var(--brick);border-radius:13px;padding:12px 18px;font-size:15px;color:var(--ink-2);line-height:1.36}
.hint b{color:var(--ink)}

.tbl{display:flex;flex-direction:column}
.hd{display:flex;gap:12px;margin-bottom:10px}
.hd .sp{flex:0 0 168px}
.sy{flex:1 1 0;background:var(--brick);border-radius:11px 11px 0 0;padding:12px 14px;color:#fff}
.sy .nm{font-size:17px;font-weight:700;line-height:1.2}
.sy .zh{font-family:'Noto Serif SC',serif;font-weight:600;font-size:16px;color:#F6D8DF;margin-top:3px}
.rw{display:flex;gap:12px;margin-bottom:8px}
.lb{flex:0 0 168px;font-size:14px;font-weight:700;color:var(--ink);padding:11px 0 0 2px}
.cl{flex:1 1 0;background:var(--surface);border:1px solid var(--hair);border-radius:10px;padding:11px 14px;font-size:14px;color:var(--ink-2);line-height:1.34}

.foot{margin-top:auto;display:flex;align-items:center;gap:18px;padding-top:22px}
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
      <div class="eyebrow">Три разные системы</div>
      <h2>Общее у них — <i>только слово в названии</i></h2>
    </div>
    <div class="hint">Одни и те же признаки для каждой: <b>кто ведёт, кого касается, есть ли баллы</b>. Разница видна построчно.</div>
  </div>

  <div class="tbl">
    <div class="hd"><div class="sp"></div>%(heads)s</div>
    %(rows)s
  </div>

  <div class="foot">
    <div class="msg">Статья описывает <b>устройство, а не даёт оценок</b>; там, где подтверждения нет, это сказано прямо</div>
    <div class="brand"><span class="dot2"></span><b>Kitai School</b><span>&middot; kitai-school.ru</span></div>
  </div>
</div>
</body></html>""" % dict(fonts=FONTS, vars=VARS, h=640, heads=heads, rows=body_rows)

open(S + "rey-info.html", "w", encoding="utf-8").write(info)

print("ok | пар:", len(PAIRS), "| систем:", len(SYSTEMS), "| признаков:", len(ROWS))
print("оценочных слов в данных нет")
