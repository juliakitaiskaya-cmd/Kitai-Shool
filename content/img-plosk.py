# -*- coding: utf-8 -*-
# Картинки к статье «Счётное слово для плоских предметов»
# Обложка     — силуэты пяти предметов с их классификаторами
# Инфографика — знак и его собственное значение: почему он закреплён за этой группой
S = ("/tmp/claude-0/-home-user-Kitai-Shool/a463bfca-82a9-56fd-ae09-42a7257ff999/"
     "scratchpad/")

FONTS = ("<link href=\"https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,600;0,700;1,600"
         "&family=Inter:wght@400;500;600;700&family=Noto+Serif+SC:wght@500;600;700&display=swap\" rel=\"stylesheet\">")
VARS = (":root{--brick:#A41E3A;--brick-d:#841630;--brick-soft:#F7E6EB;--ink:#2C2420;--ink-2:#5A4F45;"
        "--taupe:#8B7D6B;--cream:#FAF7F2;--cream-2:#F3EDE3;--hair:#EAE3D8;--surface:#fff;"
        "--good:#2F6F4F;--good-soft:#E8F3EC;--grey:#8A8178;--grey-soft:#EFEDE8}")

# ─────────── данные: пять классификаторов ───────────
# знак, чтение, что считает, собственное значение знака, пример, перевод примера, форма силуэта
CLS = [
    ("张", "zhāng", "лист, билет, стол", "", "一张纸", "лист бумаги", "sheet"),
    ("面", "miàn", "зеркало, флаг", "поверхность, сторона", "一面镜子", "зеркало", "mirror"),
    ("幅", "fú", "картина, свиток", "ширина полотна", "一幅画", "картина", "frame"),
    ("片", "piàn", "ломтик, пластинка", "тонкий ломтик", "一片面包", "ломтик хлеба", "slice"),
    ("枚", "méi", "монета, марка, значок", "", "一枚硬币", "монета", "coin"),
]
EXTRA = ("门", "mén", "язык, учебный курс", "дверь", "一门外语", "иностранный язык")
BAD = ["лучш", "хуже", "сложн", "легк", "красив", "правильн"]

# ── проверки данных
assert len(CLS) == 5, "классификаторов должно быть пять"
assert CLS[0][0] == "张", "张 стоит первым как общий случай"
repl = CLS[1:]
assert all(c[0] != "张" for c in repl), "в заменах самого 张 быть не должно"
assert EXTRA[0] == "门" and EXTRA[3], "у 门 должно стоять собственное значение"
for zh, py, what, mean, ex, ru, shape in CLS:
    assert zh and py and what and ex and ru and shape, "у %s заполнены не все поля" % zh
    for v in (what, ru):
        assert not any(b in v.lower() for b in BAD), "оценочное слово: %s" % v
no_mean = [c[0] for c in CLS if not c[3]]
assert "枚" in no_mean, "у 枚 ходового самостоятельного значения нет — так и помечаем"
assert len(set(c[6] for c in CLS)) == len(CLS), "силуэты не должны повторяться"

SHAPES = {
    "sheet": '<div class="sh sheet"></div>',
    "mirror": '<div class="sh mirror"></div>',
    "frame": '<div class="sh frame"><i></i></div>',
    "slice": '<div class="sh slice"></div>',
    "coin": '<div class="sh coin"></div>',
}

# ─────────── обложка: силуэты предметов ───────────
cards = ""
for zh, py, what, mean, ex, ru, shape in CLS:
    cls = " base" if zh == "张" else ""
    tag = "<i class=\"tag\">у соседей</i>" if zh == "张" else ""
    cards += ('<div class="cd%s"><div class="shbox">%s</div><div class="zh">%s</div><div class="py">%s</div>'
              '<div class="ex">%s</div><div class="ru">%s</div>%s</div>'
              % (cls, SHAPES[shape], zh, py, ex, ru, tag))

hero = """<!DOCTYPE html><html lang="ru"><head><meta charset="utf-8">
%(fonts)s
<style>
%(vars)s
*{margin:0;box-sizing:border-box}html,body{width:1200px;height:630px}
.card{width:1200px;height:630px;background:radial-gradient(1040px 700px at 10%% 6%%, #fff 0%%, var(--cream) 52%%, var(--cream-2) 100%%);position:relative;overflow:hidden;font-family:'Inter',sans-serif;padding:32px 56px 54px 72px;display:flex;flex-direction:column}
.card:before{content:"";position:absolute;left:0;top:0;bottom:0;width:12px;background:var(--brick)}
.head{display:flex;justify-content:space-between;align-items:flex-end;gap:34px;margin-bottom:24px}
.eyebrow{color:var(--brick);font-weight:700;font-size:18px;letter-spacing:.19em;text-transform:uppercase;margin-bottom:10px}
h1{font-family:'Cormorant Garamond',serif;font-weight:600;font-size:36px;line-height:1.07;color:var(--ink);letter-spacing:-.3px;max-width:25ch}
h1 i{font-style:italic;color:var(--brick)}
h1 i em{font-family:'Noto Serif SC',serif;font-style:normal;font-weight:600;font-size:.94em;white-space:nowrap}
.tip{flex:0 0 330px;background:var(--surface);border:1px solid var(--hair);border-left:4px solid var(--brick);border-radius:13px;padding:13px 18px;font-size:15px;color:var(--ink-2);line-height:1.38}
.tip b{color:var(--ink)}

.row{display:flex;gap:14px}
.cd{flex:1 1 0;background:var(--surface);border:1px solid var(--hair);border-radius:14px;padding:18px 14px 16px;text-align:center;position:relative}
.cd.base{background:var(--grey-soft);border-style:dashed}
.shbox{height:104px;display:flex;align-items:flex-end;justify-content:center}
.cd .zh{font-family:'Noto Serif SC',serif;font-weight:700;font-size:42px;color:var(--brick);line-height:1.05;margin-top:12px}
.cd.base .zh{color:var(--grey)}
.cd .py{font-size:13px;color:var(--taupe);margin-top:1px}
.cd .ex{font-family:'Noto Serif SC',serif;font-size:22px;color:var(--ink);margin-top:10px}
.cd .ru{font-size:13px;color:var(--taupe);margin-top:2px;line-height:1.25}
.cd .tag{position:absolute;top:-10px;left:50%%;transform:translateX(-50%%);font-style:normal;font-size:10.5px;font-weight:700;letter-spacing:.08em;text-transform:uppercase;background:var(--grey);color:#fff;border-radius:6px;padding:2px 8px;white-space:nowrap}

/* силуэты предметов */
.sh{margin:0 auto;position:relative}
.sheet{width:66px;height:86px;background:#fff;border:2px solid var(--taupe);border-radius:3px}
.sheet:after{content:"";position:absolute;right:-2px;top:-2px;border:10px solid transparent;border-top-color:var(--cream-2);border-right-color:var(--cream-2)}
.mirror{width:62px;height:86px;background:linear-gradient(145deg,#EDF2F5,#D7E2E9);border:3px solid var(--taupe);border-radius:31px 31px 26px 26px}
.frame{width:92px;height:76px;background:#fff;border:5px solid #B08A52;border-radius:3px;display:flex;align-items:center;justify-content:center}
.frame i{display:block;width:56px;height:40px;background:linear-gradient(160deg,#E8D9C3,#CBB79A);border-radius:2px}
.slice{width:84px;height:54px;background:#F0DCB8;border:2px solid #C9A86A;border-radius:10px 10px 6px 6px}
.coin{width:68px;height:68px;border-radius:50%%;background:radial-gradient(circle at 36%% 32%%, #F4E3B6, #D8B87A);border:3px solid #B08A52}

.extra{margin-top:14px;display:flex;align-items:baseline;gap:14px;background:var(--brick-soft);border:1px solid var(--brick);border-radius:13px;padding:11px 22px}
.extra b{font-family:'Noto Serif SC',serif;font-size:30px;color:var(--brick-d);line-height:1}
.extra .epy{font-size:13px;color:var(--taupe)}
.extra .ewhat{font-size:15.5px;color:var(--ink);font-weight:600}
.extra .eex{font-family:'Noto Serif SC',serif;font-size:21px;color:var(--ink);margin-left:auto}
.extra .eru{font-size:14px;color:var(--ink-2)}
.brand{position:absolute;left:72px;bottom:19px;display:flex;align-items:center;gap:11px;color:var(--ink)}
.brand b{font-family:'Cormorant Garamond',serif;font-weight:700;font-size:26px}
.brand .bdot{width:10px;height:10px;border-radius:50%%;background:var(--brick)}
.brand span{color:var(--taupe);font-size:16px}
</style></head><body>
<div class="card">
  <div class="head">
    <div>
      <div class="eyebrow">Грамматика</div>
      <h1>Счётное слово для плоских предметов: <i>когда <em>张</em> не подходит и чем его заменить</i></h1>
    </div>
    <div class="tip">Все пять предметов плоские, а слова у них <b>разные</b>. Первое знакомо, остальные четыре — нет.</div>
  </div>

  <div class="row">%(cards)s</div>

  <div class="extra"><b>%(ez)s</b><span class="epy">%(epy)s</span><span class="ewhat">%(ewhat)s</span><span class="eex">%(eex)s</span><span class="eru">— %(eru)s</span></div>

  <div class="brand"><span class="bdot"></span><b>Kitai School</b><span>&middot; kitai-school.ru</span></div>
</div>
</body></html>""" % dict(fonts=FONTS, vars=VARS, cards=cards, ez=EXTRA[0], epy=EXTRA[1],
         ewhat='и ещё один случай, не плоский: ' + EXTRA[2], eex=EXTRA[4], eru=EXTRA[5])

open(S + "plosk-hero.html", "w", encoding="utf-8").write(hero)

# ─────────── инфографика: знак и его собственное значение ───────────
rows = ""
for zh, py, what, mean, ex, ru, shape in CLS[1:] + [EXTRA + ("",)]:
    if mean:
        mid = '<div class="mean"><span>знак сам значит</span><b>%s</b></div>' % mean
    else:
        mid = ('<div class="mean none"><span>ходового значения нет</span>'
               '<b>просто запоминают</b></div>')
    rows += ('<div class="rw"><div class="zh">%s<i>%s</i></div>%s'
             '<div class="what">%s</div>'
             '<div class="ex"><b>%s</b><span>%s</span></div></div>'
             % (zh, py, mid, what, ex, ru))

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
.hint{flex:0 0 392px;background:var(--surface);border:1px solid var(--hair);border-left:4px solid var(--brick);border-radius:13px;padding:12px 18px;font-size:15px;color:var(--ink-2);line-height:1.36}
.hint b{color:var(--ink)}

.rw{display:flex;align-items:stretch;gap:14px;margin-bottom:11px}
.rw .zh{flex:0 0 120px;background:var(--surface);border:1px solid var(--hair);border-left:5px solid var(--brick);border-radius:12px;display:flex;flex-direction:column;align-items:center;justify-content:center;font-family:'Noto Serif SC',serif;font-weight:700;font-size:40px;color:var(--brick);line-height:1}
.rw .zh i{font-family:'Inter',sans-serif;font-style:normal;font-size:12.5px;font-weight:600;color:var(--taupe);margin-top:4px}
.mean{flex:0 0 266px;background:var(--good-soft);border:1px solid var(--good);border-radius:12px;padding:13px 16px;display:flex;flex-direction:column;justify-content:center}
.mean span{font-size:11.5px;font-weight:700;letter-spacing:.1em;text-transform:uppercase;color:var(--good)}
.mean b{font-size:17px;color:var(--ink);margin-top:3px;line-height:1.25}
.mean.none{background:var(--grey-soft);border-color:var(--taupe);border-style:dashed}
.mean.none span,.mean.none b{color:var(--taupe)}
.mean.none b{color:var(--grey)}
.what{flex:1 1 auto;background:var(--surface);border:1px solid var(--hair);border-radius:12px;padding:13px 16px;display:flex;align-items:center;font-size:16px;color:var(--ink);line-height:1.3}
.ex{flex:0 0 232px;background:var(--brick-soft);border:1px solid var(--brick);border-radius:12px;padding:11px 16px;display:flex;flex-direction:column;justify-content:center}
.ex b{font-family:'Noto Serif SC',serif;font-size:22px;color:var(--brick-d);line-height:1.15}
.ex span{font-size:13px;color:var(--ink-2);margin-top:2px}

.foot{margin-top:auto;display:flex;align-items:center;gap:18px;padding-top:16px}
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
      <div class="eyebrow">Почему именно это слово</div>
      <h2>Знак подсказывает сам — <i>если знать, что он значит</i></h2>
    </div>
    <div class="hint">У большинства классификаторов есть <b>собственное значение</b>, и оно объясняет, что они считают. Исключение одно.</div>
  </div>

  %(rows)s

  <div class="foot">
    <div class="msg">В разговорной речи вместо специального слова часто ставят <b>个</b> — вас поймут, но прозвучит это небрежно</div>
    <div class="brand"><span class="dot2"></span><b>Kitai School</b><span>&middot; kitai-school.ru</span></div>
  </div>
</div>
</body></html>""" % dict(fonts=FONTS, vars=VARS, h=640, rows=rows)

open(S + "plosk-info.html", "w", encoding="utf-8").write(info)

print("ok | классификаторов:", len(CLS), "| замен:", len(CLS) - 1, "| плюс 门")
print("张 помечен как разобранный у соседей; у 枚 стоит пометка")
