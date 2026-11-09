# -*- coding: utf-8 -*-
# Картинки к статье «Счастье на китайском»
# Обложка     — перекрёстная подстановка: две верные фразы и две перечёркнутые замены
# Инфографика — вложенные круги охвата: жизнь, событие, момент
S = ("/tmp/claude-0/-home-user-Kitai-Shool/a463bfca-82a9-56fd-ae09-42a7257ff999/"
     "scratchpad/")

FONTS = ("<link href=\"https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,600;0,700;1,600"
         "&family=Inter:wght@400;500;600;700&family=Noto+Serif+SC:wght@500;600;700&display=swap\" rel=\"stylesheet\">")
VARS = (":root{--brick:#A41E3A;--brick-d:#841630;--brick-soft:#F7E6EB;--ink:#2C2420;--ink-2:#5A4F45;"
        "--taupe:#8B7D6B;--cream:#FAF7F2;--cream-2:#F3EDE3;--hair:#EAE3D8;--surface:#fff;"
        "--good:#2F6F4F;--good-soft:#E8F3EC;--grey:#8A8178;--grey-soft:#EFEDE8}")

# ─────────── данные: слова о счастье ───────────
# знак, чтение, охват (3 — жизнь, 2 — событие, 1 — момент), о чём речь, пример, перевод примера
WORDS = [
    ("幸福", "xìngfú", 3, "о жизни целиком", "家庭幸福", "счастливая семья"),
    ("快乐", "kuàilè", 2, "о событии и поводе", "生日快乐", "с днём рождения"),
    ("开心", "kāixīn", 1, "о настроении сейчас", "我很开心", "мне радостно"),
    ("高兴", "gāoxìng", 1, "о реакции на случай", "很高兴认识你", "рад познакомиться"),
]
RINGS = [
    (3, "жизнь целиком", "幸福"),
    (2, "событие и повод", "快乐"),
    (1, "момент", "开心 и 高兴"),
]

# ─────────── данные: перекрёстная подстановка ───────────
# верная фраза, перевод, неверная замена
PAIRS = [
    ("家庭幸福", "счастливая семья", "家庭快乐"),
    ("生日快乐", "с днём рождения", "生日幸福"),
]

BAD = ["глубж", "сильн", "слаб", "красив", "лучш", "хуже", "правильн"]

# ── проверки данных
assert len(WORDS) == 4, "слов должно быть четыре"
assert all("福" != w[0] for w in WORDS), "знак 福 отдельно — он у «Удачи»"
assert "福" not in [r[2] for r in RINGS], "福 в кольца не ставится"
scopes = [r[0] for r in RINGS]
assert scopes == sorted(scopes, reverse=True), "охваты должны строго убывать"
assert len(set(scopes)) == len(scopes), "охваты не должны совпадать"
for zh, py, sc, about, ex, ru in WORDS:
    assert zh and py and about and ex and ru, "у слова %s заполнены не все поля" % zh
    assert sc in scopes, "охват слова %s не совпадает ни с одним кольцом" % zh
    for v in (about, ru):
        assert not any(b in v.lower() for b in BAD), "оценочное слово: %s" % v
assert len(PAIRS) == 2, "пар подстановки должно быть две"
assert PAIRS[0][2] != PAIRS[0][0] and PAIRS[1][2] != PAIRS[1][0], "замена должна отличаться"

# ─────────── обложка: перекрёстная подстановка ───────────
goods = "".join(
    '<div class="good"><div class="zh">%s</div><div class="ru">%s</div>'
    '<i class="mk">верно</i></div>' % (ok, ru) for ok, ru, bad in PAIRS)
bads = "".join(
    '<div class="bad"><div class="zh">%s</div><i class="mk">так не говорят</i></div>'
    % bad for ok, ru, bad in PAIRS)

hero = """<!DOCTYPE html><html lang="ru"><head><meta charset="utf-8">
%(fonts)s
<style>
%(vars)s
*{margin:0;box-sizing:border-box}html,body{width:1200px;height:630px}
.card{width:1200px;height:630px;background:radial-gradient(1040px 700px at 10%% 6%%, #fff 0%%, var(--cream) 52%%, var(--cream-2) 100%%);position:relative;overflow:hidden;font-family:'Inter',sans-serif;padding:34px 56px 58px 72px;display:flex;flex-direction:column}
.card:before{content:"";position:absolute;left:0;top:0;bottom:0;width:12px;background:var(--brick)}
.head{display:flex;justify-content:space-between;align-items:flex-end;gap:34px;margin-bottom:24px}
.eyebrow{color:var(--brick);font-weight:700;font-size:18px;letter-spacing:.19em;text-transform:uppercase;margin-bottom:11px}
h1{font-family:'Cormorant Garamond',serif;font-weight:600;font-size:36px;line-height:1.08;color:var(--ink);letter-spacing:-.3px;max-width:24ch}
h1 i{font-style:italic;color:var(--brick)}
h1 i em{font-family:'Noto Serif SC',serif;font-style:normal;font-weight:600;font-size:.94em;white-space:nowrap}
.tip{flex:0 0 346px;background:var(--surface);border:1px solid var(--hair);border-left:4px solid var(--brick);border-radius:13px;padding:13px 18px;font-size:15px;color:var(--ink-2);line-height:1.38}
.tip b{color:var(--ink)}

.pairs{display:flex;align-items:stretch;gap:0}
.col{display:flex;flex-direction:column;gap:14px;flex:0 0 384px}
.good,.bad{border-radius:14px;padding:14px 20px 12px;height:116px}
.good{background:var(--surface);border:1px solid var(--hair);border-left:5px solid var(--good)}
.bad{background:var(--grey-soft);border:1px dashed var(--taupe)}
.zh{font-family:'Noto Serif SC',serif;font-weight:600;font-size:34px;color:var(--ink);line-height:1.18}
.bad .zh{color:var(--grey);text-decoration:line-through;text-decoration-color:var(--brick);text-decoration-thickness:3px}
.ru{font-size:14.5px;color:var(--ink-2);margin-top:3px}
.mk{display:block;margin-top:6px;font-style:normal;font-size:12.5px;font-weight:700;letter-spacing:.1em;text-transform:uppercase}
.good .mk{color:var(--good)}
.bad .mk{color:var(--brick)}
.cross{flex:1 1 auto;position:relative;margin:0 16px}
.cross svg{position:absolute;inset:0;width:100%%;height:100%%}

.note{margin-top:18px;background:var(--brick-soft);border:1px solid var(--brick);border-radius:13px;padding:11px 20px;font-size:15px;color:var(--ink);line-height:1.36}
.note b{color:var(--brick)}

.brand{position:absolute;left:72px;bottom:20px;display:flex;align-items:center;gap:11px;color:var(--ink)}
.brand b{font-family:'Cormorant Garamond',serif;font-weight:700;font-size:26px}
.brand .bdot{width:10px;height:10px;border-radius:50%%;background:var(--brick)}
.brand span{color:var(--taupe);font-size:16px}
</style></head><body>
<div class="card">
  <div class="head">
    <div>
      <div class="eyebrow">Лексика</div>
      <h1>Счастье на китайском: <i><em>幸福</em> и <em>快乐</em> — почему это разные слова</i></h1>
    </div>
    <div class="tip">Поменять их местами <b>не получится</b>: одно говорят о жизни, другое — о поводе.</div>
  </div>

  <div class="pairs">
    <div class="col">%(goods)s</div>
    <div class="cross">
      <svg viewBox="0 0 100 246" preserveAspectRatio="none">
        <defs>
          <marker id="a" markerWidth="7" markerHeight="7" refX="6" refY="3.5" orient="auto">
            <path d="M0,0 L7,3.5 L0,7 Z" fill="#8B7D6B"></path>
          </marker>
        </defs>
        <line x1="2" y1="58" x2="96" y2="188" stroke="#8B7D6B" stroke-width="2"
              stroke-dasharray="7 6" marker-end="url(#a)" vector-effect="non-scaling-stroke"></line>
        <line x1="2" y1="188" x2="96" y2="58" stroke="#8B7D6B" stroke-width="2"
              stroke-dasharray="7 6" marker-end="url(#a)" vector-effect="non-scaling-stroke"></line>
      </svg>
    </div>
    <div class="col">%(bads)s</div>
  </div>

  <div class="note">Дело <b>не в силе чувства</b>, а в том, о каком отрезке жизни речь — о дне или обо всей жизни</div>

  <div class="brand"><span class="bdot"></span><b>Kitai School</b><span>&middot; kitai-school.ru</span></div>
</div>
</body></html>""" % dict(fonts=FONTS, vars=VARS, goods=goods, bads=bads)

open(S + "schastye-hero.html", "w", encoding="utf-8").write(hero)

# ─────────── инфографика: вложенные круги охвата ───────────
SIZE = {3: 336, 2: 228, 1: 128}
CY = 184          # центр колец по вертикали
circles = ""
for sc, label, zh in RINGS:
    d = SIZE[sc]
    circles += ('<div class="ci s%d" style="width:%dpx;height:%dpx;margin-left:%dpx;'
                'margin-top:%dpx"><span>%s</span></div>'
                % (sc, d, d, -d // 2, -d // 2, zh if sc == 1 else ""))

labels = ""
for i, (sc, label, zh) in enumerate(RINGS):
    d = SIZE[sc]
    labels += ('<div class="lb s%d" style="top:%dpx"><b>%s</b><span>%s</span></div>'
               % (sc, CY - d // 2 - 6, zh, label))

rowsi = ""
for zh, py, sc, about, ex, ru in WORDS:
    rowsi += ('<div class="wd s%d"><div class="w-zh">%s</div><div class="w-py">%s</div>'
              '<div class="w-ab">%s</div><div class="w-ex">%s</div>'
              '<div class="w-ru">%s</div></div>' % (sc, zh, py, about, ex, ru))

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

.body{display:flex;gap:24px;align-items:center}
.rings{flex:0 0 372px;position:relative;height:372px}
.ci{position:absolute;left:50%%;top:184px;border-radius:50%%;display:flex;align-items:center;justify-content:center}
.ci.s3{background:var(--brick-soft);border:2px solid var(--brick)}
.ci.s2{background:#F6EFE3;border:2px solid #C8A678}
.ci.s1{background:var(--good-soft);border:2px solid var(--good)}
.ci span{font-family:'Noto Serif SC',serif;font-weight:700;font-size:22px;color:var(--good)}
.lb{position:absolute;left:50%%;transform:translateX(-50%%);text-align:center;width:260px}
.lb b{display:block;font-family:'Noto Serif SC',serif;font-size:23px;line-height:1.1}
.lb span{display:block;font-size:13px;color:var(--taupe);margin-top:1px}
.lb.s3 b{color:var(--brick)}
.lb.s2 b{color:#9A7638}
.lb.s1{display:none}

.words{flex:1 1 auto;display:flex;flex-direction:column;gap:10px}
.wd{background:var(--surface);border:1px solid var(--hair);border-radius:12px;padding:10px 16px;display:grid;grid-template-columns:116px 1fr;grid-template-rows:auto auto;column-gap:14px;align-items:baseline}
.wd.s3{border-left:5px solid var(--brick)}
.wd.s2{border-left:5px solid #C8A678}
.wd.s1{border-left:5px solid var(--good)}
.w-zh{grid-row:1;grid-column:1;font-family:'Noto Serif SC',serif;font-weight:700;font-size:27px;color:var(--ink);line-height:1.1}
.w-py{grid-row:2;grid-column:1;font-size:12.5px;color:var(--taupe)}
.w-ab{grid-row:1;grid-column:2;font-size:14.5px;color:var(--ink);font-weight:600}
.w-ex{grid-row:2;grid-column:2;font-family:'Noto Serif SC',serif;font-size:17px;color:var(--brick-d);display:inline}
.w-ru{grid-row:2;grid-column:2;font-size:13px;color:var(--taupe);justify-self:end}

.foot{margin-top:auto;display:flex;align-items:center;gap:18px;padding-top:16px}
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
      <div class="eyebrow">Четыре слова о счастье</div>
      <h2>Различаются не силой, <i>а размером отрезка</i></h2>
    </div>
    <div class="hint">Внешнее кольцо — <b>жизнь целиком</b>, среднее — событие, внутреннее — момент. Чем меньше отрезок, тем будничнее слово.</div>
  </div>

  <div class="body">
    <div class="rings">%(circles)s%(labels)s</div>
    <div class="words">%(rowsi)s</div>
  </div>

  <div class="foot">
    <div class="msg">Знак <b>福</b> в этот ряд не встаёт: он не о чувстве, а о благополучии и пожелании</div>
    <div class="brand"><span class="dot2"></span><b>Kitai School</b><span>&middot; kitai-school.ru</span></div>
  </div>
</div>
</body></html>""" % dict(fonts=FONTS, vars=VARS, h=660, circles=circles, labels=labels, rowsi=rowsi)

open(S + "schastye-info.html", "w", encoding="utf-8").write(info)

print("ok | слов:", len(WORDS), "| колец:", len(RINGS), "| охваты:", scopes)
print("福 в ряду нет, оценочных слов нет")
