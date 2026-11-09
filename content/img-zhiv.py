# -*- coding: utf-8 -*-
# Картинки к статье «Счётное слово для животных»
# Обложка     — определитель-цепочка: три вопроса и ответ по умолчанию
# Инфографика — матрица по двум признакам: размер и форма, плюс выноска для 匹
S = ("/tmp/claude-0/-home-user-Kitai-Shool/a463bfca-82a9-56fd-ae09-42a7257ff999/"
     "scratchpad/")

FONTS = ("<link href=\"https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,600;0,700;1,600"
         "&family=Inter:wght@400;500;600;700&family=Noto+Serif+SC:wght@500;600;700&display=swap\" rel=\"stylesheet\">")
VARS = (":root{--brick:#A41E3A;--brick-d:#841630;--brick-soft:#F7E6EB;--ink:#2C2420;--ink-2:#5A4F45;"
        "--taupe:#8B7D6B;--cream:#FAF7F2;--cream-2:#F3EDE3;--hair:#EAE3D8;--surface:#fff;"
        "--good:#2F6F4F;--good-soft:#E8F3EC;--grey:#8A8178;--grey-soft:#EFEDE8}")

# ─────────── данные: классификаторы и животные ───────────
# знак, чтение, признак группы, примеры животных
CLS = [
    ("只", "zhī", "почти все остальные", "猫 鸟 鸡 老虎"),
    ("匹", "pǐ", "лошади", "马"),
    ("头", "tóu", "крупный скот", "牛 猪 大象"),
    ("条", "tiáo", "длинное и гибкое", "鱼 蛇"),
]
# животное, чтение, перевод, классификатор, скот ли (сюда же слон), длинное ли, пометка
ANIMALS = [
    ("猫", "māo", "кошка", "只", False, False, ""),
    ("鸟", "niǎo", "птица", "只", False, False, ""),
    ("鸡", "jī", "курица", "只", False, False, ""),
    ("老虎", "lǎohǔ", "тигр", "只", False, False, ""),
    ("狗", "gǒu", "собака", "只", False, False, "встречается и 条"),
    ("牛", "niú", "корова", "头", True, False, ""),
    ("猪", "zhū", "свинья", "头", True, False, ""),
    ("大象", "dàxiàng", "слон", "头", True, False, ""),
    ("鱼", "yú", "рыба", "条", False, True, ""),
    ("蛇", "shé", "змея", "条", False, True, ""),
    ("马", "mǎ", "лошадь", "匹", True, False, "исключение"),
]
# определитель: вопрос, ответ
CHAIN = [
    ("Это лошадь?", "匹"),
    ("Длинное и гибкое тело?", "条"),
    ("Крупный скот?", "头"),
]
DEFAULT = "只"

# ── проверки данных
assert len(CLS) == 4, "классификаторов должно быть четыре"
known = [c[0] for c in CLS]
assert DEFAULT in known, "ответ по умолчанию должен быть среди классификаторов"
assert all(q and a in known for q, a in CHAIN), "каждый вопрос цепочки ведёт к классификатору"
assert len(CHAIN) == len(known) - 1, "вопросов на один меньше, чем ответов"
for zh, py, ru, cl, big, long_, note in ANIMALS:
    assert cl in known, "у %s неизвестный классификатор %s" % (zh, cl)
    assert zh and py and ru, "у %s заполнены не все поля" % zh
assert [a for a in ANIMALS if a[3] == "匹"] == [a for a in ANIMALS if a[6] == "исключение"], \
    "匹 — единственное исключение, оно должно быть отмечено"
assert all("峰" not in a[3] for a in ANIMALS), "峰 не подтвердилось, в данные не берём"
assert sum(1 for a in ANIMALS if a[3] == "只") >= 4, "只 должен покрывать большинство"
for herd in (False, True):
    for long_ in (False, True):
        box = [a for a in ANIMALS if a[4] == herd and a[5] == long_ and a[6] != "исключение"]
        assert len(set(a[3] for a in box)) <= 1, \
            "в одной клетке матрицы оказались разные классификаторы: %s" % [a[0] for a in box]

# ─────────── обложка: определитель-цепочка ───────────
steps = ""
for i, (q, ans) in enumerate(CHAIN, start=1):
    ex = next(a[0] for a in ANIMALS if a[3] == ans)
    steps += """  <div class="st">
    <div class="q"><i>%d</i><span>%s</span></div>
    <div class="yes"><b>да</b><div class="cl">%s</div><div class="ex">一%s%s</div></div>
  </div>""" % (i, q, ans, ans, ex)

hero = """<!DOCTYPE html><html lang="ru"><head><meta charset="utf-8">
%(fonts)s
<style>
%(vars)s
*{margin:0;box-sizing:border-box}html,body{width:1200px;height:630px}
.card{width:1200px;height:630px;background:radial-gradient(1040px 700px at 10%% 6%%, #fff 0%%, var(--cream) 52%%, var(--cream-2) 100%%);position:relative;overflow:hidden;font-family:'Inter',sans-serif;padding:32px 56px 56px 72px;display:flex;flex-direction:column}
.card:before{content:"";position:absolute;left:0;top:0;bottom:0;width:12px;background:var(--brick)}
.head{display:flex;justify-content:space-between;align-items:flex-end;gap:34px;margin-bottom:20px}
.eyebrow{color:var(--brick);font-weight:700;font-size:18px;letter-spacing:.19em;text-transform:uppercase;margin-bottom:10px}
h1{font-family:'Cormorant Garamond',serif;font-weight:600;font-size:37px;line-height:1.07;color:var(--ink);letter-spacing:-.3px;max-width:24ch}
h1 i{font-style:italic;color:var(--brick)}
h1 i em{font-family:'Noto Serif SC',serif;font-style:normal;font-weight:600;font-size:.94em;white-space:nowrap}
.tip{flex:0 0 344px;background:var(--surface);border:1px solid var(--hair);border-left:4px solid var(--brick);border-radius:13px;padding:13px 18px;font-size:15px;color:var(--ink-2);line-height:1.38}
.tip b{color:var(--ink)}

.chain{display:flex;flex-direction:column;gap:11px}
.st{display:flex;align-items:stretch;gap:0}
.q{flex:1 1 auto;background:var(--surface);border:1px solid var(--hair);border-radius:12px 0 0 12px;border-right:0;padding:14px 20px;display:flex;align-items:center;gap:14px;font-size:19px;color:var(--ink)}
.q i{font-style:normal;flex:0 0 auto;width:28px;height:28px;border-radius:50%%;background:var(--cream-2);border:1px solid var(--hair);color:var(--taupe);font-size:14px;font-weight:700;display:flex;align-items:center;justify-content:center}
.yes{flex:0 0 310px;background:var(--brick-soft);border:1px solid var(--brick);border-radius:0 12px 12px 0;padding:9px 20px;display:flex;align-items:center;gap:16px}
.yes b{font-size:12.5px;font-weight:700;letter-spacing:.12em;text-transform:uppercase;color:var(--brick);flex:0 0 auto}
.yes .cl{font-family:'Noto Serif SC',serif;font-weight:700;font-size:34px;color:var(--brick-d);line-height:1}
.yes .ex{font-family:'Noto Serif SC',serif;font-size:21px;color:var(--ink-2)}

.def{margin-top:13px;display:flex;align-items:center;gap:18px;background:var(--good-soft);border:1px solid var(--good);border-radius:13px;padding:13px 22px}
.def b{font-size:12.5px;font-weight:700;letter-spacing:.12em;text-transform:uppercase;color:var(--good);flex:0 0 auto}
.def .cl{font-family:'Noto Serif SC',serif;font-weight:700;font-size:36px;color:var(--good);line-height:1}
.def span{font-size:16px;color:var(--ink-2)}

.brand{position:absolute;left:72px;bottom:19px;display:flex;align-items:center;gap:11px;color:var(--ink)}
.brand b{font-family:'Cormorant Garamond',serif;font-weight:700;font-size:26px}
.brand .bdot{width:10px;height:10px;border-radius:50%%;background:var(--brick)}
.brand span{color:var(--taupe);font-size:16px}
</style></head><body>
<div class="card">
  <div class="head">
    <div>
      <div class="eyebrow">Грамматика</div>
      <h1>Счётное слово для животных: <i>почему <em>只</em> подходит кошке, но не лошади</i></h1>
    </div>
    <div class="tip">Три вопроса подряд — и слово найдено. <b>只 стоит последним</b>: это вариант по умолчанию.</div>
  </div>

  <div class="chain">
%(steps)s
  </div>

  <div class="def"><b>ни одно не подошло</b><span class="cl">%(def)s</span><span>猫, 鸟, 鸡, 老虎 — и почти все остальные</span></div>

  <div class="brand"><span class="bdot"></span><b>Kitai School</b><span>&middot; kitai-school.ru</span></div>
</div>
</body></html>""" % dict(fonts=FONTS, vars=VARS, steps=steps, **{"def": DEFAULT})

open(S + "zhiv-hero.html", "w", encoding="utf-8").write(hero)

# ─────────── инфографика: матрица по двум признакам ───────────
def cell(big, long_):
    inside = [a for a in ANIMALS if a[4] == big and a[5] == long_ and a[6] != "исключение"]
    if not inside:
        return None, []
    return inside[0][3], inside


grid = ""
for big, rowname in [(False, "остальные"), (True, "скот и слон")]:
    cells = ""
    for long_, colname in [(False, "обычная форма"), (True, "длинное и гибкое")]:
        cl, inside = cell(big, long_)
        if cl is None:
            cells += '<div class="cl empty"><span>—</span></div>'
            continue
        names = " ".join("%s" % a[0] for a in inside)
        ru = ", ".join(a[2] for a in inside)
        cells += ('<div class="cl"><div class="zh">%s</div><div class="an">%s</div>'
                  '<div class="ru">%s</div></div>' % (cl, names, ru))
    grid += '<div class="rw"><div class="rn">%s</div>%s</div>' % (rowname, cells)

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

.body{display:flex;gap:26px;align-items:flex-start}
.mx{flex:1 1 auto}
.hd{display:flex;gap:12px;margin-bottom:9px}
.hd .sp{flex:0 0 118px}
.hd .cn{flex:1 1 0;text-align:center;font-size:12px;font-weight:700;letter-spacing:.11em;text-transform:uppercase;color:var(--taupe)}
.rw{display:flex;gap:12px;margin-bottom:12px;align-items:stretch}
.rn{flex:0 0 118px;display:flex;align-items:center;font-size:14.5px;font-weight:700;color:var(--ink);line-height:1.25}
.cl{flex:1 1 0;background:var(--surface);border:1px solid var(--hair);border-left:5px solid var(--brick);border-radius:12px;padding:13px 16px 14px;min-height:124px}
.cl.empty{border-left-color:var(--taupe);border-style:dashed;display:flex;align-items:center;justify-content:center;color:var(--grey)}
.cl .zh{font-family:'Noto Serif SC',serif;font-weight:700;font-size:34px;color:var(--brick);line-height:1.05}
.cl .an{font-family:'Noto Serif SC',serif;font-size:24px;color:var(--ink);margin-top:6px;letter-spacing:.06em}
.cl .ru{font-size:13.5px;color:var(--taupe);margin-top:4px;line-height:1.3}

.side{flex:0 0 262px;background:var(--good-soft);border:1px solid var(--good);border-radius:14px;padding:16px 18px}
.side .ttl{font-size:12px;font-weight:700;letter-spacing:.11em;text-transform:uppercase;color:var(--good);margin-bottom:10px}
.side .zh{font-family:'Noto Serif SC',serif;font-weight:700;font-size:40px;color:var(--good);line-height:1}
.side .an{font-family:'Noto Serif SC',serif;font-size:26px;color:var(--ink);margin-top:8px}
.side p{font-size:14px;color:var(--ink-2);line-height:1.36;margin-top:10px}

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
      <div class="eyebrow">Два признака, которые работают</div>
      <h2>Хозяйство и форма — <i>а размер подводит</i></h2>
    </div>
    <div class="hint">Строки — <b>хозяйственные животные и все остальные</b>, столбцы — форма тела. Размер сам по себе не решает.</div>
  </div>

  <div class="body">
    <div class="mx">
      <div class="hd"><div class="sp"></div><div class="cn">обычная форма</div><div class="cn">длинное и гибкое</div></div>
      %(grid)s
    </div>
    <div class="side">
      <div class="ttl">вне матрицы</div>
      <div class="zh">匹</div>
      <div class="an">一匹马</div>
      <p>Лошадь — хозяйственное животное, но 头 к ней не ставят: у неё своё слово, и его просто запоминают.</p>
    </div>
  </div>

  <div class="foot">
    <div class="msg">Размер обманчив: 老虎 крупнее свиньи, но идёт с <b>只</b>, а 猪 — с 头</div>
    <div class="brand"><span class="dot2"></span><b>Kitai School</b><span>&middot; kitai-school.ru</span></div>
  </div>
</div>
</body></html>""" % dict(fonts=FONTS, vars=VARS, h=600, grid=grid)

open(S + "zhiv-info.html", "w", encoding="utf-8").write(info)

print("ok | классификаторов:", len(CLS), "| животных:", len(ANIMALS),
      "| вопросов в цепочке:", len(CHAIN))
print("峰 в данных нет, 匹 отмечено исключением")
