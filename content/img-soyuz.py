# -*- coding: utf-8 -*-
# Картинки к статье «Союз «и» в китайском»
# Обложка     — наборная строка с прорезью: один и тот же знак в одном и том же гнезде
# Инфографика — полоса регистра с засечками: пять слов от разговорного к книжному
S = ("/tmp/claude-0/-home-user-Kitai-Shool/a463bfca-82a9-56fd-ae09-42a7257ff999/"
     "scratchpad/")

FONTS = ("<link href=\"https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,600;0,700;1,600"
         "&family=Inter:wght@400;500;600;700&family=Noto+Serif+SC:wght@500;600;700&display=swap\" rel=\"stylesheet\">")
VARS = (":root{--brick:#A41E3A;--brick-d:#841630;--brick-soft:#F7E6EB;--ink:#2C2420;--ink-2:#5A4F45;"
        "--taupe:#8B7D6B;--cream:#FAF7F2;--cream-2:#F3EDE3;--hair:#EAE3D8;--surface:#fff;"
        "--good:#2F6F4F;--good-soft:#E8F3EC;--grey:#8A8178;--grey-soft:#EFEDE8}")

# ─────────── данные: пять слов со значением «и» ───────────
# знак, чтение, место на полосе регистра (0 — разговорное, 100 — книжное),
# что соединяет, где встречается
WORDS = [
    ("跟", "gēn", 8, "существительные и местоимения", "разговорная речь"),
    ("和", "hé", 32, "существительные и именные группы", "и в речи, и в письме"),
    ("及", "jí", 62, "однородные существительные", "книжные перечисления"),
    ("以及", "yǐjí", 78, "последний элемент перечисления", "письменный и официальный текст"),
    ("与", "yǔ", 93, "существительные и названия", "документы и названия"),
]

# ─────────── данные: две сборки для обложки ───────────
ROWS = [
    (True, "我", "他", "я и он", "两个名词 — связка на месте"),
    (False, "我毕业了", "我想继续读书", "я закончила — и хочу учиться дальше",
     "две части со своими сказуемыми — 和 здесь не ставится"),
]
FIXED = "我毕业了，想继续读书"

BAD = ["ужас", "страшн", "хорош", "плох", "правильн", "красив", "легк", "труд", "сложн"]

# ── проверки данных
assert len(WORDS) == 5, "слов должно быть пять"
pos = [w[2] for w in WORDS]
assert pos == sorted(pos), "места на полосе должны идти по возрастанию"
assert len(set(pos)) == 5, "места на полосе не должны совпадать"
assert min(pos) >= 5 and max(pos) <= 95, "засечки не должны упираться в края полосы"
for a, b in zip(pos, pos[1:]):
    assert b - a >= 12, "засечки %d и %d встанут слишком близко" % (a, b)
for zh, py, p, what, where in WORDS:
    assert zh and py and what and where, "у слова %s заполнены не все поля" % zh
    for v in (what, where):
        assert not any(x in v.lower() for x in BAD), "оценочное слово: %s" % v
assert len(ROWS) == 2 and ROWS[0][0] and not ROWS[1][0], "сборки: одна держится, одна нет"
assert "、" not in FIXED, "знак 、 разбирается у «Пунктуации»"

# ─────────── обложка: наборная строка с прорезью ───────────
def strip(ok, left, right, ru, note):
    cls = "ok" if ok else "no"
    mark = "сборка держится" if ok else "сборка не держится"
    return """  <div class="st %s">
    <div class="line">
      <span class="pl">%s</span>
      <span class="slot"><i>和</i></span>
      <span class="pl">%s</span>
    </div>
    <div class="meta"><b>%s</b><span>%s</span></div>
    <div class="ru">%s</div>
  </div>""" % (cls, left, right, mark, note, ru)


strips = "\n".join(strip(*r) for r in ROWS)

hero = """<!DOCTYPE html><html lang="ru"><head><meta charset="utf-8">
%(fonts)s
<style>
%(vars)s
*{margin:0;box-sizing:border-box}html,body{width:1200px;height:630px}
.card{width:1200px;height:630px;background:radial-gradient(1040px 700px at 10%% 6%%, #fff 0%%, var(--cream) 52%%, var(--cream-2) 100%%);position:relative;overflow:hidden;font-family:'Inter',sans-serif;padding:34px 56px 60px 72px;display:flex;flex-direction:column}
.card:before{content:"";position:absolute;left:0;top:0;bottom:0;width:12px;background:var(--brick)}
.head{display:flex;justify-content:space-between;align-items:flex-end;gap:34px;margin-bottom:20px}
.eyebrow{color:var(--brick);font-weight:700;font-size:18px;letter-spacing:.19em;text-transform:uppercase;margin-bottom:11px}
h1{font-family:'Cormorant Garamond',serif;font-weight:600;font-size:37px;line-height:1.07;color:var(--ink);letter-spacing:-.3px;max-width:25ch}
h1 i{font-style:italic;color:var(--brick)}
h1 i em{font-family:'Noto Serif SC',serif;font-style:normal;font-weight:600;font-size:.92em}
.tip{flex:0 0 362px;background:var(--surface);border:1px solid var(--hair);border-left:4px solid var(--brick);border-radius:13px;padding:13px 18px;font-size:15px;color:var(--ink-2);line-height:1.38}
.tip b{color:var(--ink)}

.strips{display:flex;flex-direction:column;gap:13px}
.st{background:var(--surface);border:1px solid var(--hair);border-radius:14px;padding:14px 20px 12px}
.st.ok{border-left:5px solid var(--good)}
.st.no{border-left:5px solid var(--brick)}
.line{display:flex;align-items:center;gap:13px}
.pl{background:var(--cream-2);border:1px solid var(--hair);border-radius:9px;padding:5px 13px;font-family:'Noto Serif SC',serif;font-weight:600;font-size:27px;color:var(--ink);line-height:1.22}
.slot{position:relative;width:66px;height:46px;border-radius:9px;border:2px dashed var(--taupe);background:repeating-linear-gradient(135deg,#fff 0 7px,var(--grey-soft) 7px 14px);display:flex;align-items:center;justify-content:center;flex:0 0 66px}
.slot i{font-family:'Noto Serif SC',serif;font-style:normal;font-weight:700;font-size:28px;color:var(--brick)}
.meta{display:flex;align-items:baseline;gap:12px;margin-top:9px;font-size:14px}
.st.ok .meta b{color:var(--good)}
.st.no .meta b{color:var(--brick)}
.meta span{color:var(--taupe)}
.ru{margin-top:4px;font-size:15px;color:var(--ink-2)}

.fix{margin-top:14px;display:flex;align-items:center;gap:14px;background:var(--good-soft);border:1px solid var(--good);border-radius:13px;padding:10px 18px}
.fix b{font-size:14.5px;color:var(--good);letter-spacing:.04em;text-transform:uppercase;flex:0 0 auto}
.fix .zh{font-family:'Noto Serif SC',serif;font-weight:600;font-size:23px;color:var(--ink)}
.fix span.ru2{font-size:14.5px;color:var(--ink-2)}

.brand{position:absolute;left:72px;bottom:20px;display:flex;align-items:center;gap:11px;color:var(--ink)}
.brand b{font-family:'Cormorant Garamond',serif;font-weight:700;font-size:26px}
.brand .bdot{width:10px;height:10px;border-radius:50%%;background:var(--brick)}
.brand span{color:var(--taupe);font-size:16px}
</style></head><body>
<div class="card">
  <div class="head">
    <div>
      <div class="eyebrow">Грамматика</div>
      <h1>Союз «и» в китайском: <i>почему <em>和</em> соединяет не всё подряд</i></h1>
    </div>
    <div class="tip">Одно и то же гнездо, один и тот же знак — и <b>разный результат</b>. Сверху два существительных, снизу две части со своими сказуемыми.</div>
  </div>

  <div class="strips">
%(strips)s
  </div>

  <div class="fix"><b>как надо</b><span class="zh">%(fixed)s</span><span class="ru2">— части разделяются, а не соединяются через 和</span></div>

  <div class="brand"><span class="bdot"></span><b>Kitai School</b><span>&middot; kitai-school.ru</span></div>
</div>
</body></html>""" % dict(fonts=FONTS, vars=VARS, strips=strips, fixed=FIXED)

open(S + "soyuz-hero.html", "w", encoding="utf-8").write(hero)

# ─────────── инфографика: полоса регистра с засечками ───────────
ticks = ""
for i, (zh, py, p, what, where) in enumerate(WORDS, start=1):
    ticks += ('<div class="tk" style="left:%.2f%%">'
              '<div class="zh">%s</div><div class="py">%s</div>'
              '<div class="st"></div><div class="num">%d</div></div>' % (p, zh, py, i))

cards = ""
for i, (zh, py, p, what, where) in enumerate(WORDS, start=1):
    cards += ('<div class="cd"><div class="cn">%d</div>'
              '<div class="cz">%s</div>'
              '<div class="cl">соединяет</div><div class="cv">%s</div>'
              '<div class="cl">встречается</div><div class="cv">%s</div></div>'
              % (i, zh, what, where))

info = """<!DOCTYPE html><html lang="ru"><head><meta charset="utf-8">
%(fonts)s
<style>
%(vars)s
*{margin:0;box-sizing:border-box}html,body{width:1200px;height:%(h)dpx}
.wrap{width:1200px;height:%(h)dpx;background:linear-gradient(180deg,#fff 0%%,var(--cream) 42%%,var(--cream-2) 100%%);font-family:'Inter',sans-serif;padding:38px 48px 28px;display:flex;flex-direction:column;position:relative;overflow:hidden}
.wrap:before{content:"";position:absolute;left:0;right:0;top:0;height:9px;background:var(--brick)}
.top{display:flex;align-items:flex-end;justify-content:space-between;gap:34px;margin-bottom:30px}
.eyebrow{color:var(--brick);font-weight:700;font-size:15.5px;letter-spacing:.19em;text-transform:uppercase;margin-bottom:8px}
h2{font-family:'Cormorant Garamond',serif;font-weight:600;font-size:38px;line-height:1.07;color:var(--ink);max-width:22ch}
h2 i{font-style:italic;color:var(--brick)}
.hint{flex:0 0 392px;background:var(--surface);border:1px solid var(--hair);border-left:4px solid var(--brick);border-radius:13px;padding:12px 18px;font-size:15px;color:var(--ink-2);line-height:1.36}
.hint b{color:var(--ink)}

.scale{position:relative;height:148px;margin:0 20px 10px}
.bar{position:absolute;left:0;right:0;top:104px;height:10px;border-radius:5px;background:linear-gradient(90deg,var(--grey-soft) 0%%,var(--cream-2) 45%%,var(--brick-soft) 100%%);border:1px solid var(--hair)}
.ends{position:absolute;left:0;right:0;top:124px;display:flex;justify-content:space-between;font-size:14px;font-weight:700;color:var(--taupe);letter-spacing:.06em;text-transform:uppercase}
.tk{position:absolute;top:0;transform:translateX(-50%%);display:flex;flex-direction:column;align-items:center}
.tk .zh{font-family:'Noto Serif SC',serif;font-weight:700;font-size:38px;color:var(--ink);line-height:1.05}
.tk .py{font-size:14px;color:var(--taupe);margin-top:1px}
.tk .st{width:3px;height:18px;background:var(--brick);margin-top:6px}
.tk .num{width:26px;height:26px;border-radius:50%%;background:var(--brick);color:#fff;font-size:14px;font-weight:700;display:flex;align-items:center;justify-content:center;margin-top:-1px}

.cards{display:flex;gap:12px;margin-top:4px}
.cd{flex:1 1 0;background:var(--surface);border:1px solid var(--hair);border-radius:12px;padding:13px 14px 14px;position:relative}
.cd .cn{position:absolute;top:-11px;left:13px;width:24px;height:24px;border-radius:50%%;background:var(--brick);color:#fff;font-size:13px;font-weight:700;display:flex;align-items:center;justify-content:center}
.cd .cz{font-family:'Noto Serif SC',serif;font-weight:700;font-size:25px;color:var(--brick);margin:9px 0 9px;line-height:1.1}
.cd .cl{font-size:11.5px;font-weight:700;letter-spacing:.11em;text-transform:uppercase;color:var(--taupe)}
.cd .cv{font-size:14px;color:var(--ink-2);line-height:1.32;margin:2px 0 9px}
.cd .cv:last-child{margin-bottom:0}

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
      <div class="eyebrow">Пять слов, одно значение</div>
      <h2>Выбирают не по смыслу, <i>а по тому, где это сказано</i></h2>
    </div>
    <div class="hint">Все пять соединяют существительные. Различаются они <b>речью, в которой встречаются</b>: слева — разговорное, справа — книжное.</div>
  </div>

  <div class="scale">
    <div class="bar"></div>
    %(ticks)s
    <div class="ends"><span>разговорная речь</span><span>книжный текст</span></div>
  </div>

  <div class="cards">%(cards)s</div>

  <div class="foot">
    <div class="msg">Частей фразы со своими сказуемыми <b>не соединяет ни одно из пяти</b> — для них нужны другие средства</div>
    <div class="brand"><span class="dot2"></span><b>Kitai School</b><span>&middot; kitai-school.ru</span></div>
  </div>
</div>
</body></html>""" % dict(fonts=FONTS, vars=VARS, h=620, ticks=ticks, cards=cards)

open(S + "soyuz-info.html", "w", encoding="utf-8").write(info)

print("ok | слов:", len(WORDS), "| места:", pos)
print("сборки:", len(ROWS), "| оценочных слов в данных нет")
