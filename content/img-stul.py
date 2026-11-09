# -*- coding: utf-8 -*-
# Картинки к статье «Счётное слово для стульев»
# Обложка     — один знак в трёх работах
# Инфографика — граница применимости: где 把 работает, где уже нет
S = ("/tmp/claude-0/-home-user-Kitai-Shool/a463bfca-82a9-56fd-ae09-42a7257ff999/"
     "scratchpad/")

FONTS = ("<link href=\"https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,600;0,700;1,600"
         "&family=Inter:wght@400;500;600;700&family=Noto+Serif+SC:wght@500;600;700&display=swap\" rel=\"stylesheet\">")
VARS = (":root{--brick:#A41E3A;--brick-d:#841630;--brick-soft:#F7E6EB;--ink:#2C2420;--ink-2:#5A4F45;"
        "--taupe:#8B7D6B;--cream:#FAF7F2;--cream-2:#F3EDE3;--hair:#EAE3D8;--surface:#fff;"
        "--good:#2F6F4F;--good-soft:#E8F3EC;--grey:#8A8178;--grey-soft:#EFEDE8}")

# ─────────── данные: работы знака 把 ───────────
# роль, пример, перевод, пояснение, разобрано ли у нас отдельно
JOBS = [
    ("счётное слово", "一把伞", "один зонт", "предметы, которые берут за ручку", False),
    ("мера «горсть»", "一把米", "горсть риса", "сыпучее, что помещается в ладони", False),
    ("часть слова", "把手", "ручка", "то самое, за что берутся", False),
    ("грамматическая конструкция", "把门关上", "закрой дверь", "разобрана у нас отдельно", True),
]

# ─────────── данные: предметы и граница ───────────
# знак, чтение, перевод, есть ли за что взяться, классификатор, пограничный ли
THINGS = [
    ("椅子", "yǐzi", "стул", True, "把", False),
    ("伞", "sǎn", "зонт", True, "把", False),
    ("刀", "dāo", "нож", True, "把", False),
    ("钥匙", "yàoshi", "ключ", True, "把", False),
    ("梳子", "shūzi", "расчёска", True, "把", False),
    ("扇子", "shànzi", "веер", True, "把", False),
    ("凳子", "dèngzi", "табурет без спинки", False, "个", True),
    ("杯子", "bēizi", "стакан", False, "个", False),
    ("盘子", "pánzi", "тарелка", False, "个", False),
    ("苹果", "píngguǒ", "яблоко", False, "个", False),
]
BAD = ["лучш", "хуже", "сложн", "легк", "красив", "правильн"]

# ── проверки данных
assert len(JOBS) == 4, "работ у знака должно быть четыре"
assert sum(1 for j in JOBS if j[4]) == 1, "отдельно разобрана ровно одна работа — конструкция"
for role, ex, ru, note, apart in JOBS:
    assert role and ex and ru and note, "у работы «%s» заполнены не все поля" % role
for zh, py, ru, grip, cl, edge in THINGS:
    assert zh and py and ru and cl, "у %s заполнены не все поля" % zh
    assert (cl == "把") == grip, "классификатор у %s не согласован с признаком" % zh
    for v in (ru,):
        assert not any(b in v.lower() for b in BAD), "оценочное слово: %s" % v
assert sum(1 for t in THINGS if t[5]) == 1, "пограничный случай должен быть один"
assert [t[0] for t in THINGS if t[5]] == ["凳子"], "пограничный случай — табурет"
assert all(t[4] == "把" for t in THINGS if t[3]), "слева только 把"
assert all(t[4] == "个" for t in THINGS if not t[3]), "справа только 个"

# ─────────── обложка: один знак в трёх работах ───────────
jobs_html = ""
for role, ex, ru, note, apart in JOBS:
    cls = " apart" if apart else ""
    jobs_html += ('<div class="jb%s"><div class="role">%s</div>'
                  '<div class="ex">%s</div><div class="ru">%s</div>'
                  '<div class="note">%s</div></div>' % (cls, role, ex, ru, note))

hero = """<!DOCTYPE html><html lang="ru"><head><meta charset="utf-8">
%(fonts)s
<style>
%(vars)s
*{margin:0;box-sizing:border-box}html,body{width:1200px;height:630px}
.card{width:1200px;height:630px;background:radial-gradient(1040px 700px at 10%% 6%%, #fff 0%%, var(--cream) 52%%, var(--cream-2) 100%%);position:relative;overflow:hidden;font-family:'Inter',sans-serif;padding:32px 56px 54px 72px;display:flex;flex-direction:column}
.card:before{content:"";position:absolute;left:0;top:0;bottom:0;width:12px;background:var(--brick)}
.head{display:flex;justify-content:space-between;align-items:flex-end;gap:34px;margin-bottom:22px}
.eyebrow{color:var(--brick);font-weight:700;font-size:18px;letter-spacing:.19em;text-transform:uppercase;margin-bottom:10px}
h1{font-family:'Cormorant Garamond',serif;font-weight:600;font-size:37px;line-height:1.07;color:var(--ink);letter-spacing:-.3px;max-width:24ch}
h1 i{font-style:italic;color:var(--brick)}
h1 i em{font-family:'Noto Serif SC',serif;font-style:normal;font-weight:600;font-size:.94em;white-space:nowrap}
.tip{flex:0 0 336px;background:var(--surface);border:1px solid var(--hair);border-left:4px solid var(--brick);border-radius:13px;padding:13px 18px;font-size:15px;color:var(--ink-2);line-height:1.38}
.tip b{color:var(--ink)}

.body{display:flex;align-items:center;gap:26px}
.core{flex:0 0 190px;height:252px;background:var(--brick);border-radius:18px;display:flex;flex-direction:column;align-items:center;justify-content:center;color:#fff}
.core b{font-family:'Noto Serif SC',serif;font-size:96px;line-height:1}
.core span{font-size:16px;margin-top:6px;letter-spacing:.04em}
.core i{font-style:normal;font-size:12.5px;font-weight:700;letter-spacing:.11em;text-transform:uppercase;color:#F6D8DF;margin-top:12px}
.jobs{flex:1 1 auto;display:grid;grid-template-columns:1fr 1fr;gap:12px}
.jb{background:var(--surface);border:1px solid var(--hair);border-left:5px solid var(--brick);border-radius:13px;padding:14px 16px 15px}
.jb.apart{border-left-color:var(--taupe);border-style:dashed;background:var(--grey-soft)}
.jb .role{font-size:12px;font-weight:700;letter-spacing:.1em;text-transform:uppercase;color:var(--brick)}
.jb.apart .role{color:var(--taupe)}
.jb .ex{font-family:'Noto Serif SC',serif;font-size:28px;color:var(--ink);margin-top:5px;line-height:1.15}
.jb .ru{font-size:14px;color:var(--ink-2);margin-top:2px}
.jb .note{font-size:12.5px;color:var(--taupe);margin-top:5px;line-height:1.3}

.rootline{margin-top:16px;display:flex;align-items:baseline;gap:16px;background:var(--brick-soft);border:1px solid var(--brick);border-radius:13px;padding:12px 22px}
.rootline b{font-size:12.5px;font-weight:700;letter-spacing:.11em;text-transform:uppercase;color:var(--brick);flex:0 0 auto}
.rootline span{font-size:15.5px;color:var(--ink);line-height:1.36}
.brand{position:absolute;left:72px;bottom:19px;display:flex;align-items:center;gap:11px;color:var(--ink)}
.brand b{font-family:'Cormorant Garamond',serif;font-weight:700;font-size:26px}
.brand .bdot{width:10px;height:10px;border-radius:50%%;background:var(--brick)}
.brand span{color:var(--taupe);font-size:16px}
</style></head><body>
<div class="card">
  <div class="head">
    <div>
      <div class="eyebrow">Грамматика</div>
      <h1>Счётное слово для стульев: <i><em>把</em> и неожиданная связь с «рукоятью»</i></h1>
    </div>
    <div class="tip">Один знак — <b>несколько работ</b>. Счётное слово, мера и часть слова «ручка» связаны общим смыслом.</div>
  </div>

  <div class="body">
    <div class="core"><b>把</b><span>bǎ</span><i>один знак</i></div>
    <div class="jobs">%(jobs)s</div>
  </div>

  <div class="rootline"><b>общий смысл</b><span>знак восходит к глаголу «схватить» — отсюда и ручка, и горсть, и счётное слово для того, что берут в руку</span></div>

  <div class="brand"><span class="bdot"></span><b>Kitai School</b><span>&middot; kitai-school.ru</span></div>
</div>
</body></html>""" % dict(fonts=FONTS, vars=VARS, jobs=jobs_html)

open(S + "stul-hero.html", "w", encoding="utf-8").write(hero)

# ─────────── инфографика: граница применимости ───────────
def side(grip):
    out = ""
    for zh, py, ru, g, cl, edge in THINGS:
        if g != grip or edge:
            continue
        out += ('<div class="th"><div class="zh">%s</div><div class="py">%s</div>'
                '<div class="ru">%s</div></div>' % (zh, py, ru))
    return out


edge_item = [t for t in THINGS if t[5]][0]

info = """<!DOCTYPE html><html lang="ru"><head><meta charset="utf-8">
%(fonts)s
<style>
%(vars)s
*{margin:0;box-sizing:border-box}html,body{width:1200px;height:%(h)dpx}
.wrap{width:1200px;height:%(h)dpx;background:linear-gradient(180deg,#fff 0%%,var(--cream) 42%%,var(--cream-2) 100%%);font-family:'Inter',sans-serif;padding:38px 48px 26px;display:flex;flex-direction:column;position:relative;overflow:hidden}
.wrap:before{content:"";position:absolute;left:0;right:0;top:0;height:9px;background:var(--brick)}
.top{display:flex;align-items:flex-end;justify-content:space-between;gap:34px;margin-bottom:22px}
.eyebrow{color:var(--brick);font-weight:700;font-size:15.5px;letter-spacing:.19em;text-transform:uppercase;margin-bottom:8px}
h2{font-family:'Cormorant Garamond',serif;font-weight:600;font-size:38px;line-height:1.07;color:var(--ink);max-width:22ch}
h2 i{font-style:italic;color:var(--brick)}
.hint{flex:0 0 388px;background:var(--surface);border:1px solid var(--hair);border-left:4px solid var(--brick);border-radius:13px;padding:12px 18px;font-size:15px;color:var(--ink-2);line-height:1.36}
.hint b{color:var(--ink)}

.cols{display:flex;align-items:stretch;gap:0}
.col{flex:1 1 0;border-radius:16px;padding:16px 18px 18px}
.col.yes{background:var(--good-soft);border:1px solid var(--good)}
.col.no{background:var(--grey-soft);border:1px dashed var(--taupe)}
.ch{display:flex;align-items:baseline;gap:12px;margin-bottom:13px}
.ch b{font-family:'Noto Serif SC',serif;font-size:36px;line-height:1}
.col.yes .ch b{color:var(--good)}
.col.no .ch b{color:var(--grey)}
.ch span{font-size:14px;font-weight:600;color:var(--ink);line-height:1.25}
.items{display:flex;flex-wrap:wrap;gap:10px}
.th{background:var(--surface);border:1px solid var(--hair);border-radius:11px;padding:9px 14px 10px;text-align:center;min-width:104px}
.th .zh{font-family:'Noto Serif SC',serif;font-weight:600;font-size:24px;color:var(--ink);line-height:1.1}
.th .py{font-size:11.5px;color:var(--taupe);margin-top:1px}
.th .ru{font-size:13px;color:var(--ink-2);margin-top:3px}

.edge{flex:0 0 232px;margin:0 16px;background:var(--brick-soft);border:1px solid var(--brick);border-radius:16px;padding:16px 18px;display:flex;flex-direction:column;justify-content:center;text-align:center}
.edge .ttl{font-size:11.5px;font-weight:700;letter-spacing:.1em;text-transform:uppercase;color:var(--brick);margin-bottom:8px}
.edge .zh{font-family:'Noto Serif SC',serif;font-weight:700;font-size:34px;color:var(--brick-d);line-height:1.1}
.edge .py{font-size:12.5px;color:var(--taupe);margin-top:2px}
.edge p{font-size:13.5px;color:var(--ink-2);line-height:1.34;margin-top:9px}
.edge p b{color:var(--ink)}

.foot{margin-top:auto;display:flex;align-items:center;gap:18px;padding-top:18px}
.foot .msg{flex:1 1 auto;background:var(--surface);border:1px solid var(--hair);border-radius:14px;padding:11px 20px;font-size:14.5px;color:var(--ink);line-height:1.34}
.foot .msg b{color:var(--brick)}
.brand{display:flex;align-items:center;gap:10px;color:var(--ink);flex:0 0 auto}
.brand b{font-family:'Cormorant Garamond',serif;font-weight:700;font-size:23px}
.brand .dot2{width:9px;height:9px;border-radius:50%%;background:var(--brick)}
.brand span{color:var(--taupe);font-size:15px}
</style></head><body>
<div class="wrap">
  <div class="top">
    <div>
      <div class="eyebrow">Где правило кончается</div>
      <h2>Есть за что взяться — <i>есть и 把</i></h2>
    </div>
    <div class="hint">Слева предметы с ручкой или рукоятью, справа — те, у которых её нет. Посередине <b>пограничный случай</b>.</div>
  </div>

  <div class="cols">
    <div class="col yes">
      <div class="ch"><b>把</b><span>есть ручка, дужка или рукоять</span></div>
      <div class="items">%(yes)s</div>
    </div>
    <div class="edge">
      <div class="ttl">на границе</div>
      <div class="zh">%(ez)s</div>
      <div class="py">%(epy)s</div>
      <p>%(eru)s: браться не за что, поэтому <b>个</b>, а не 把</p>
    </div>
    <div class="col no">
      <div class="ch"><b>个</b><span>взяться не за что</span></div>
      <div class="items">%(no)s</div>
    </div>
  </div>

  <div class="foot">
    <div class="msg">Проверка простая: <b>спросите себя, за что вы возьмёте предмет</b> — ответ подскажет слово</div>
    <div class="brand"><span class="dot2"></span><b>Kitai School</b><span>&middot; kitai-school.ru</span></div>
  </div>
</div>
</body></html>""" % dict(fonts=FONTS, vars=VARS, h=556, yes=side(True), no=side(False),
                         ez=edge_item[0], epy=edge_item[1], eru=edge_item[2].capitalize())

open(S + "stul-info.html", "w", encoding="utf-8").write(info)

print("ok | работ знака:", len(JOBS), "| предметов:", len(THINGS),
      "| с 把:", sum(1 for t in THINGS if t[3]), "| пограничный:", edge_item[0])
