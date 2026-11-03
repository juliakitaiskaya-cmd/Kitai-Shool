# -*- coding: utf-8 -*-
# Картинки к статье «Самые известные китайские писатели»
# Обложка     — разворот книги: слева старое письмо столбцами, справа новое строками
# Инфографика — лента времени тремя волнами, без единого года жизни
S = ("/tmp/claude-0/-home-user-Kitai-Shool/a463bfca-82a9-56fd-ae09-42a7257ff999/"
     "scratchpad/")

FONTS = ("<link href=\"https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,600;0,700;1,600"
         "&family=Inter:wght@400;500;600;700&family=Noto+Serif+SC:wght@600;700&display=swap\" rel=\"stylesheet\">")
VARS = (":root{--brick:#A41E3A;--brick-d:#841630;--brick-soft:#F7E6EB;--ink:#2C2420;--ink-2:#5A4F45;"
        "--taupe:#8B7D6B;--cream:#FAF7F2;--cream-2:#F3EDE3;--hair:#EAE3D8;--surface:#fff;"
        "--page:#FDFBF6;--page-2:#F6F0E4;--sky:#39597F;--sky-soft:#E8EEF5;--w1:#8C6A3F;--w2:#5F7A6A;--w3:#39597F}")

# ── обложка: одна мысль старым письменным языком и живым
# Начертания с обеих сторон одинаковые: разница только в языке, а не в упрощении знаков
OLD = ["有朋自远方来", "不亦乐乎"]          # столбцы, справа налево, без пунктуации
NEW = ["有朋友从远方来，", "不也很快乐吗？"]   # строки с пунктуацией

assert len(OLD) == 2 and len(NEW) == 2, "состав страниц изменился"
old_plain = "".join(OLD)
new_plain = "".join(ch for ch in "".join(NEW) if ch not in "，。？")
# живой язык многосложнее — это и есть содержание картинки
assert len(new_plain) > len(old_plain), "справа должно быть больше знаков, чем слева"
# пунктуация только справа
assert any(p in "".join(NEW) for p in "，。？"), "на правой странице нет пунктуации"
assert not any(p in old_plain for p in "，。？"), "на левой странице появилась пунктуация"
# традиционных начертаний нет ни с одной стороны: упрощение знаков — другая реформа, её не путаем
TRAD = "這樣寫對從爲說樂點讀書語長間們"
assert not any(c in old_plain + new_plain for c in TRAD), "в данные попали традиционные начертания"

cols = "".join('<div class="col">%s</div>' % "".join(
    '<span>%s</span>' % ch for ch in c) for c in OLD)
lines = "".join('<div class="ln">%s</div>' % l for l in NEW)

hero = """<!DOCTYPE html><html lang="ru"><head><meta charset="utf-8">
%(fonts)s
<style>
%(vars)s
*{margin:0;box-sizing:border-box}html,body{width:1200px;height:630px}
.card{width:1200px;height:630px;background:radial-gradient(1020px 680px at 12%% 8%%, #fff 0%%, var(--cream) 50%%, var(--cream-2) 100%%);position:relative;overflow:hidden;font-family:'Inter',sans-serif;padding:52px 44px 0 72px;display:flex;justify-content:space-between}
.card:before{content:"";position:absolute;left:0;top:0;bottom:0;width:12px;background:var(--brick)}
.txt{flex:0 0 470px;padding-top:12px}
.eyebrow{color:var(--brick);font-weight:700;font-size:18px;letter-spacing:.19em;text-transform:uppercase;margin-bottom:14px}
h1{font-family:'Cormorant Garamond',serif;font-weight:600;font-size:42px;line-height:1.06;color:var(--ink);letter-spacing:-.4px}
h1 i{font-style:italic;color:var(--brick)}
.sub{font-size:18px;color:var(--ink-2);line-height:1.42;max-width:31ch;margin-top:17px}
.tip{display:inline-block;margin-top:22px;background:var(--surface);border:1px solid var(--hair);border-left:4px solid var(--brick);border-radius:13px;padding:14px 20px;font-size:15.5px;color:var(--ink-2);line-height:1.38;max-width:34ch}
.tip b{color:var(--ink)}

.scene{flex:0 0 566px;display:flex;flex-direction:column;align-items:center;padding-top:34px}
.book{position:relative;width:566px;height:412px;display:flex;border-radius:9px;box-shadow:0 20px 40px rgba(44,36,32,.2)}
.pg{flex:1 1 0;background:linear-gradient(180deg,var(--page) 0%%,var(--page-2) 100%%);padding:26px 24px 20px;position:relative;overflow:hidden}
.pg.l{border-radius:9px 0 0 9px;border:1px solid var(--hair);border-right:none}
.pg.r{border-radius:0 9px 9px 0;border:1px solid var(--hair);border-left:none}
.spine{flex:0 0 16px;background:linear-gradient(90deg,#E3DACB 0%%,#CFC3B0 46%%,#E3DACB 100%%);box-shadow:inset 0 0 10px rgba(44,36,32,.22)}
.plbl{position:absolute;left:0;right:0;bottom:12px;text-align:center;font-size:12.5px;letter-spacing:.12em;text-transform:uppercase;font-weight:700}
.pg.l .plbl{color:var(--taupe)}
.pg.r .plbl{color:var(--brick)}

.vert{display:flex;flex-direction:row-reverse;justify-content:center;gap:24px;height:296px}
.col{display:flex;flex-direction:column;align-items:center;gap:3px}
.col span{font-family:'Noto Serif SC',serif;font-weight:600;font-size:31px;line-height:1.08;color:#4A4038}
.horiz{display:flex;flex-direction:column;gap:16px;padding-top:58px}
.ln{font-family:'Noto Serif SC',serif;font-weight:600;font-size:31px;line-height:1.3;color:var(--ink)}
.mark{position:absolute;right:22px;top:22px;width:9px;height:9px;border-radius:50%%;background:var(--brick)}

.cap{margin-top:20px;text-align:center;font-size:16.5px;color:var(--ink-2);line-height:1.4;max-width:42ch}
.cap b{color:var(--ink)}
.brand{position:absolute;left:72px;bottom:28px;display:flex;align-items:center;gap:11px;color:var(--ink)}
.brand b{font-family:'Cormorant Garamond',serif;font-weight:700;font-size:26px}
.brand .bdot{width:10px;height:10px;border-radius:50%%;background:var(--brick)}
.brand span{color:var(--taupe);font-size:16px}
</style></head><body>
<div class="card">
  <div class="txt">
    <div class="eyebrow">Литература</div>
    <h1>Самые известные китайские писатели: <i>от Лу Синя до нобелиата Мо Яня</i></h1>
    <div class="sub">Главный перелом случился не в сюжетах, а в том, на каком языке вообще пишут книги.</div>
    <div class="tip"><b>Одна и та же мысль</b> — слева книжным языком, на котором никто не говорил, справа — тем, как говорят.</div>
    <div class="brand"><span class="bdot"></span><b>Kitai School</b><span>&middot; kitai-school.ru</span></div>
  </div>

  <div class="scene">
    <div class="book">
      <div class="pg l">
        <div class="vert">%(cols)s</div>
        <div class="plbl">старый письменный язык</div>
      </div>
      <div class="spine"></div>
      <div class="pg r">
        <span class="mark"></span>
        <div class="horiz">%(lines)s</div>
        <div class="plbl">живой язык</div>
      </div>
    </div>
    <div class="cap">Начертания одинаковые — <b>разница только в языке</b></div>
  </div>
</div>
</body></html>""" % dict(fonts=FONTS, vars=VARS, cols=cols, lines=lines)

open(S + "pis-hero.html", "w", encoding="utf-8").write(hero)

# ─────────────────────────── инфографика ───────────────────────────
# (волна, подпись отрезка, цвет) и авторы в ней
WAVES = [
    ("w1", "Начало XX века", [
        ("鲁迅", "Лу Синь", "«Подлинная история А-Кью»", "перешёл на живой язык"),
    ]),
    ("w2", "Середина XX века", [
        ("老舍", "Лао Шэ", "«Рикша»", "город и маленький человек"),
        ("巴金", "Ба Цзинь", "«Семья»", "распад старого уклада"),
        ("张爱玲", "Чжан Айлин", "«Красная роза и белая роза»", "частная жизнь на фоне войны"),
    ]),
    ("w3", "Наши дни", [
        ("高行健", "Гао Синцзянь", "灵山", "премия 2000"),
        ("莫言", "Мо Янь", "«Красный гаолян»", "премия 2012"),
        ("余华", "Юй Хуа", "«Жить»", "короткая проза, простой язык"),
        ("刘慈欣", "Лю Цысинь", "«Задача трёх тел»", "премия 2015"),
    ]),
]

PRIZES = [("w3", "2000", "Нобелевская премия"), ("w3", "2012", "Нобелевская премия"),
          ("w3", "2015", "«Хьюго»")]

# ── проверки данных
authors = [a[0] for w in WAVES for a in w[2]]
assert len(authors) == len(set(authors)), "автор попал в две волны"
assert len(authors) == 8, "имён должно быть восемь, их %d" % len(authors)
assert len(WAVES) == 3, "волн должно быть три"
assert len(PRIZES) == 3, "меток премий должно быть ровно три"
# ни одной даты жизни: единственные четырёхзначные числа — годы премий
blob = " ".join(x for w in WAVES for a in w[2] for x in a) + " " + " ".join(w[1] for w in WAVES)
import re as _re
years = _re.findall(r"\b\d{4}\b", blob)
assert set(years) <= {"2000", "2012", "2015"}, "в данные просочился посторонний год: %s" % years
assert all(len(a) == 4 for w in WAVES for a in w[2]), "у автора не хватает поля"

waves = "".join(
    '<div class="wv %s"><div class="wh">%s</div><div class="cards">%s</div></div>'
    % (cls, label, "".join(
        '<div class="au"><b class="han">%s</b><span class="ru">%s</span>'
        '<span class="bk">%s</span><span class="wh2">%s</span></div>' % a for a in auths))
    for cls, label, auths in WAVES)

prizes = "".join('<div class="pz"><b>%s</b><span>%s</span></div>' % (y, t)
                 for _, y, t in PRIZES)

info = """<!DOCTYPE html><html lang="ru"><head><meta charset="utf-8">
%(fonts)s
<style>
%(vars)s
*{margin:0;box-sizing:border-box}html,body{width:1200px;height:%(h)dpx}
.wrap{width:1200px;height:%(h)dpx;background:linear-gradient(180deg,#fff 0%%,var(--cream) 40%%,var(--cream-2) 100%%);font-family:'Inter',sans-serif;padding:38px 48px 30px;display:flex;flex-direction:column;position:relative;overflow:hidden}
.wrap:before{content:"";position:absolute;left:0;right:0;top:0;height:9px;background:var(--brick)}
.top{display:flex;align-items:flex-end;justify-content:space-between;gap:34px;margin-bottom:20px}
.eyebrow{color:var(--brick);font-weight:700;font-size:15.5px;letter-spacing:.19em;text-transform:uppercase;margin-bottom:8px}
h2{font-family:'Cormorant Garamond',serif;font-weight:600;font-size:38px;line-height:1.07;color:var(--ink);max-width:19ch}
h2 i{font-style:italic;color:var(--brick)}
.hint{flex:0 0 400px;background:var(--surface);border:1px solid var(--hair);border-left:4px solid var(--brick);border-radius:13px;padding:12px 18px;font-size:15px;color:var(--ink-2);line-height:1.36}
.hint b{color:var(--ink)}

.prizes{display:flex;align-items:center;gap:12px;margin-bottom:12px;padding-right:4px;justify-content:flex-end}
.prizes .plead{margin-right:auto;font-size:13.5px;color:var(--taupe);line-height:1.3;max-width:34ch}
.pz{display:flex;align-items:baseline;gap:9px;background:var(--brick-soft);border:1px solid var(--brick);border-radius:11px;padding:8px 15px}
.pz b{font-family:'Cormorant Garamond',serif;font-weight:700;font-size:22px;color:var(--brick-d)}
.pz span{font-size:13.5px;color:var(--ink-2)}

.line{position:relative;padding-left:4px}
.line:before{content:"";position:absolute;left:4px;right:4px;top:13px;height:3px;background:linear-gradient(90deg,var(--w1) 0%%,var(--w2) 50%%,var(--w3) 100%%);border-radius:2px}
.waves{display:grid;grid-template-columns:1fr 2.4fr 3.1fr;gap:18px;position:relative}
.wv{padding-top:30px;position:relative}
.wv:before{content:"";position:absolute;left:0;top:7px;width:15px;height:15px;border-radius:50%%;background:#fff}
.wv.w1:before{border:4px solid var(--w1)}
.wv.w2:before{border:4px solid var(--w2)}
.wv.w3:before{border:4px solid var(--w3)}
.wh{font-size:14px;font-weight:700;letter-spacing:.04em;margin-bottom:12px;min-height:19px;white-space:nowrap}
.wv.w1 .wh{color:var(--w1)}
.wv.w2 .wh{color:var(--w2)}
.wv.w3 .wh{color:var(--w3)}
.cards{display:flex;gap:10px}
.au{flex:1 1 0;background:var(--surface);border:1px solid var(--hair);border-radius:13px;padding:13px 12px 14px;box-shadow:0 6px 14px rgba(44,36,32,.07)}
.wv.w1 .au{border-top:3px solid var(--w1)}
.wv.w2 .au{border-top:3px solid var(--w2)}
.wv.w3 .au{border-top:3px solid var(--w3)}
.au b{display:block;font-family:'Noto Serif SC',serif;font-weight:700;font-size:26px;line-height:1.1;color:var(--ink)}
.au .ru{display:block;font-size:14.5px;font-weight:700;color:var(--ink);margin-top:3px}
.au .bk{display:block;font-size:12.5px;color:var(--brick-d);line-height:1.26;margin-top:5px}
.au .wh2{display:block;font-size:12px;color:var(--taupe);line-height:1.26;margin-top:5px}

.foot{margin-top:auto;display:flex;align-items:center;gap:18px;padding-top:20px}
.foot .msg{flex:1 1 auto;background:var(--surface);border:1px solid var(--hair);border-left:4px solid var(--brick);border-radius:14px;padding:11px 20px;font-size:14.5px;color:var(--ink-2);line-height:1.34}
.foot .msg b{color:var(--ink)}
.brand{display:flex;align-items:center;gap:10px;color:var(--ink);flex:0 0 auto}
.brand b{font-family:'Cormorant Garamond',serif;font-weight:700;font-size:23px}
.brand .dot2{width:9px;height:9px;border-radius:50%%;background:var(--brick)}
.brand span{color:var(--taupe);font-size:15px}
</style></head><body>
<div class="wrap">
  <div class="top">
    <div>
      <div class="eyebrow">Восемь имён</div>
      <h2>Три поколения — <i>и восемь имён</i></h2>
    </div>
    <div class="hint">Читается слева направо: <b>от тех, с кого началась современная китайская проза, к тем, кого читают сейчас.</b></div>
  </div>

  <div class="prizes"><span class="plead">Три главные награды — и все три у авторов последнего поколения:</span>%(prizes)s</div>

  <div class="line">
    <div class="waves">%(waves)s</div>
  </div>

  <div class="foot">
    <div class="msg">У каждого названа <b>одна книга — та, с которой обычно начинают знакомство</b>, а не единственная важная</div>
    <div class="brand"><span class="dot2"></span><b>Kitai School</b><span>&middot; kitai-school.ru</span></div>
  </div>
</div>
</body></html>""" % dict(fonts=FONTS, vars=VARS, h=540, waves=waves, prizes=prizes)

open(S + "pis-info.html", "w", encoding="utf-8").write(info)

print("ok | волн:", len(WAVES), "| имён:", len(authors), "| меток премий:", len(PRIZES))
print("знаков: книжный язык", len(old_plain), "| живой", len(new_plain), "— живой длиннее, так и должно быть")
print("четырёхзначные числа в данных:", sorted(set(years)), "— только годы премий")
