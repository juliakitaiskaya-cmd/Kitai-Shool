# -*- coding: utf-8 -*-
# Картинки к статье «Сравнение в китайском»
# Обложка     — мерная рейка с двумя метками и подписанным промежутком
# Инфографика — сетка слотов: четыре конструкции по одинаковым колонкам
S = ("/tmp/claude-0/-home-user-Kitai-Shool/a463bfca-82a9-56fd-ae09-42a7257ff999/"
     "scratchpad/")

FONTS = ("<link href=\"https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,600;0,700;1,600"
         "&family=Inter:wght@400;500;600;700&family=Noto+Serif+SC:wght@500;600;700&display=swap\" rel=\"stylesheet\">")
VARS = (":root{--brick:#A41E3A;--brick-d:#841630;--brick-soft:#F7E6EB;--ink:#2C2420;--ink-2:#5A4F45;"
        "--taupe:#8B7D6B;--cream:#FAF7F2;--cream-2:#F3EDE3;--hair:#EAE3D8;--surface:#fff;"
        "--good:#2F6F4F;--good-soft:#E8F3EC;--grey:#8A8178;--grey-soft:#EFEDE8}")

# ─────────── данные: разбор фразы по частям (обложка) ───────────
# часть фразы, подпись по-русски
PARTS = [
    ("我", "кто"),
    ("比", "связка"),
    ("他", "с кем"),
    ("高", "качество"),
    ("两公分", "разница"),
]
TALL, SHORT = 178, 176
TOP_CM, PX_CM = 180, 24          # верх шкалы и пикселей на сантиметр
DIFF = "%d см" % (TALL - SHORT)

# ─────────── данные: четыре конструкции (инфографика) ───────────
# название, связка, качество, хвост, перевод
SLOTS = ["кто", "связка", "с кем", "качество", "хвост"]
# название, связка, с кем, качество, хвост, перевод; «—» значит, что ячейка пустует
CONSTR = [
    ("А больше Б", "比", "他", "高", "两公分", "я выше него на два сантиметра"),
    ("А меньше Б", "没有", "他", "高", "—", "я не такой высокий, как он"),
    ("А и Б наравне", "跟", "他", "一样高", "—", "мы с ним одного роста"),
    ("Сравнивать не с кем", "—", "—", "最高", "—", "я самый высокий"),
]
BAD = ["ужас", "страшн", "хорош", "плох", "правильн", "красив", "легк", "труд", "сложн"]

# ── проверки данных
assert len(PARTS) == 5, "частей фразы должно быть пять"
assert len(CONSTR) == 4 and len(SLOTS) == 5, "четыре конструкции и пять слотов"
for name, link, who, qual, tail, ru in CONSTR:
    assert name and link and who and qual and tail and ru, "у конструкции «%s» пустая ячейка" % name
    for v in (name, ru):
        assert not any(b in v.lower() for b in BAD), "оценочное слово: %s" % v
    assert "很" not in link + who + qual + tail, "很 в конструкцию с 比 не ставится"
assert CONSTR[-1][1] == "—" and CONSTR[-1][2] == "—", "у последней конструкции второго предмета нет"
assert CONSTR[2][3].startswith("一样"), "一样 входит в качество, а не в связку"
assert all("很" not in p[0] for p in PARTS), "很 в разборе фразы быть не должно"
assert TALL > SHORT, "первая метка должна быть выше второй"
assert TOP_CM >= TALL and TOP_CM - 10 <= SHORT, "обе метки должны попасть на шкалу"

def y(cm):
    return 16 + (TOP_CM - cm) * PX_CM


cms = "\n".join(
    '      <div class="cm%s" style="top:%dpx">%s</div>'
    % (" big" if c % 5 == 0 else "", y(c), ("<b>%d</b>" % c) if c % 5 == 0 else "")
    for c in range(TOP_CM - 10, TOP_CM + 1))

parts_html = "".join(
    '<div class="pt"><div class="zh">%s</div><div class="lb">%s</div></div>' % p
    for p in PARTS)

hero = """<!DOCTYPE html><html lang="ru"><head><meta charset="utf-8">
%(fonts)s
<style>
%(vars)s
*{margin:0;box-sizing:border-box}html,body{width:1200px;height:630px}
.card{width:1200px;height:630px;background:radial-gradient(1040px 700px at 10%% 6%%, #fff 0%%, var(--cream) 52%%, var(--cream-2) 100%%);position:relative;overflow:hidden;font-family:'Inter',sans-serif;padding:34px 56px 58px 72px;display:flex;flex-direction:column}
.card:before{content:"";position:absolute;left:0;top:0;bottom:0;width:12px;background:var(--brick)}
.head{display:flex;justify-content:space-between;align-items:flex-end;gap:34px;margin-bottom:22px}
.eyebrow{color:var(--brick);font-weight:700;font-size:18px;letter-spacing:.19em;text-transform:uppercase;margin-bottom:11px}
h1{font-family:'Cormorant Garamond',serif;font-weight:600;font-size:37px;line-height:1.07;color:var(--ink);letter-spacing:-.3px;max-width:24ch}
h1 i{font-style:italic;color:var(--brick)}
h1 i em{font-family:'Noto Serif SC',serif;font-style:normal;font-weight:600;font-size:.94em}
.tip{flex:0 0 352px;background:var(--surface);border:1px solid var(--hair);border-left:4px solid var(--brick);border-radius:13px;padding:13px 18px;font-size:15px;color:var(--ink-2);line-height:1.38}
.tip b{color:var(--ink)}

.body{display:flex;gap:40px;align-items:flex-start}

/* мерная рейка: фрагмент шкалы 170–180 см, 34px на сантиметр */
.rule{flex:0 0 320px;position:relative;height:330px;background:var(--surface);border:1px solid var(--hair);border-radius:14px;padding:16px}
.stick{position:absolute;left:30px;top:16px;height:240px;width:30px;background:linear-gradient(90deg,var(--cream-2),var(--grey-soft));border:1px solid var(--hair);border-radius:3px}
.cm{position:absolute;left:30px;width:12px;height:0;border-top:1px solid #C9BCA8}
.cm.big{width:30px;border-top-color:var(--taupe)}
.cm.big b{position:absolute;left:-28px;top:-8px;font-size:11px;font-weight:600;color:var(--taupe)}
.tick{position:absolute;left:30px;width:140px;height:0;border-top:2px solid var(--brick)}
.tick.b{border-top-color:var(--taupe);border-top-style:dashed}
.tick span{position:absolute;left:148px;top:-10px;font-size:14.5px;font-weight:700;color:var(--ink);white-space:nowrap}
.tick.b span{color:var(--taupe);font-weight:600}
.gap{position:absolute;left:140px;border-left:2px solid var(--brick)}
.gap b{position:absolute;left:9px;top:50%%;transform:translateY(-50%%);background:var(--brick);color:#fff;font-size:14px;padding:3px 10px;border-radius:7px;white-space:nowrap}
.cap{position:absolute;left:16px;right:16px;bottom:14px;font-size:13px;color:var(--taupe);line-height:1.3}

/* разбор фразы */
.phrase{flex:1 1 auto;display:flex;flex-direction:column;justify-content:center}
.ph-top{font-size:14px;font-weight:700;letter-spacing:.14em;text-transform:uppercase;color:var(--taupe);margin-bottom:12px}
.row{display:flex;gap:11px;align-items:flex-start}
.pt{background:var(--surface);border:1px solid var(--hair);border-radius:11px;padding:12px 14px 10px;text-align:center;flex:0 0 auto}
.pt .zh{font-family:'Noto Serif SC',serif;font-weight:600;font-size:34px;color:var(--ink);line-height:1.12}
.pt .lb{margin-top:7px;font-size:12.5px;font-weight:700;letter-spacing:.07em;text-transform:uppercase;color:var(--brick)}
.pt:nth-child(2){border-color:var(--brick);background:var(--brick-soft)}
.pt:nth-child(5){border-color:var(--good);background:var(--good-soft)}
.tr{margin-top:17px;font-size:17px;color:var(--ink-2)}
.warn{margin-top:16px;background:var(--surface);border:1px solid var(--hair);border-left:4px solid var(--brick);border-radius:12px;padding:11px 18px;font-size:15px;color:var(--ink-2);line-height:1.36}
.warn b{color:var(--brick)}
.warn s{color:var(--grey);text-decoration-color:var(--brick)}

.brand{position:absolute;left:72px;bottom:20px;display:flex;align-items:center;gap:11px;color:var(--ink)}
.brand b{font-family:'Cormorant Garamond',serif;font-weight:700;font-size:26px}
.brand .bdot{width:10px;height:10px;border-radius:50%%;background:var(--brick)}
.brand span{color:var(--taupe);font-size:16px}
</style></head><body>
<div class="card">
  <div class="head">
    <div>
      <div class="eyebrow">Грамматика</div>
      <h1>Сравнение в китайском: <i>конструкция с <em>比</em> и логика «А по сравнению с Б»</i></h1>
    </div>
    <div class="tip">Разница называется <b>в конце фразы</b>, а не перед качеством. Порядок частей менять нельзя.</div>
  </div>

  <div class="body">
    <div class="rule">
      <div class="stick"></div>
%(cms)s
      <div class="tick" style="top:%(ty)dpx"><span>я — %(tall)d см</span></div>
      <div class="tick b" style="top:%(tb)dpx"><span>он — %(short)d см</span></div>
      <div class="gap" style="top:%(ty)dpx;height:%(gh)dpx"><b>%(diff)s</b></div>
      <div class="cap">Промежуток между метками — это и есть то, что в китайской фразе стоит последним</div>
    </div>

    <div class="phrase">
      <div class="ph-top">та же мысль фразой</div>
      <div class="row">%(parts)s</div>
      <div class="tr">Я выше него на два сантиметра</div>
      <div class="warn"><b>Внутрь ставить нечего:</b> <s>我比他很高</s> — степень уже задана самим <b>比</b></div>
    </div>
  </div>

  <div class="brand"><span class="bdot"></span><b>Kitai School</b><span>&middot; kitai-school.ru</span></div>
</div>
</body></html>""" % dict(fonts=FONTS, vars=VARS, parts=parts_html, tall=TALL, short=SHORT, diff=DIFF,
         cms=cms, ty=y(TALL), tb=y(SHORT), gh=(TALL - SHORT) * PX_CM)

open(S + "sravn-hero.html", "w", encoding="utf-8").write(hero)

# ─────────── инфографика: сетка слотов ───────────
head_cells = "".join('<div class="hc">%s</div>' % s for s in SLOTS)

rows = ""
for name, link, who, qual, tail, ru in CONSTR:
    cells = [("我", ""), (link, "k"), (who, ""), (qual, "q"), (tail, "t")]
    inner = "".join('<div class="cl %s%s">%s</div>'
                    % (c, " e" if v == "—" else "", v) for v, c in cells)
    rows += ('<div class="rw"><div class="nm">%s</div><div class="cells">%s</div>'
             '<div class="ru">%s</div></div>' % (name, inner, ru))

info = """<!DOCTYPE html><html lang="ru"><head><meta charset="utf-8">
%(fonts)s
<style>
%(vars)s
*{margin:0;box-sizing:border-box}html,body{width:1200px;height:%(h)dpx}
.wrap{width:1200px;height:%(h)dpx;background:linear-gradient(180deg,#fff 0%%,var(--cream) 42%%,var(--cream-2) 100%%);font-family:'Inter',sans-serif;padding:38px 48px 28px;display:flex;flex-direction:column;position:relative;overflow:hidden}
.wrap:before{content:"";position:absolute;left:0;right:0;top:0;height:9px;background:var(--brick)}
.top{display:flex;align-items:flex-end;justify-content:space-between;gap:34px;margin-bottom:24px}
.eyebrow{color:var(--brick);font-weight:700;font-size:15.5px;letter-spacing:.19em;text-transform:uppercase;margin-bottom:8px}
h2{font-family:'Cormorant Garamond',serif;font-weight:600;font-size:38px;line-height:1.07;color:var(--ink);max-width:22ch}
h2 i{font-style:italic;color:var(--brick)}
.hint{flex:0 0 392px;background:var(--surface);border:1px solid var(--hair);border-left:4px solid var(--brick);border-radius:13px;padding:12px 18px;font-size:15px;color:var(--ink-2);line-height:1.36}
.hint b{color:var(--ink)}

.hd{display:flex;align-items:flex-end;gap:14px;margin-bottom:9px}
.hd .sp{flex:0 0 196px}
.hd .cells{flex:0 0 520px;display:flex;gap:9px}
.hd .hc{flex:1 1 0;text-align:center;font-size:11.5px;font-weight:700;letter-spacing:.11em;text-transform:uppercase;color:var(--taupe)}
.hd .sp2{flex:1 1 auto}

.rw{display:flex;align-items:center;gap:14px;margin-bottom:10px}
.nm{flex:0 0 196px;font-size:15px;font-weight:700;color:var(--ink);line-height:1.25}
.cells{flex:0 0 520px;display:flex;gap:9px}
.cl{flex:1 1 0;height:60px;display:flex;align-items:center;justify-content:center;background:var(--surface);border:1px solid var(--hair);border-radius:10px;font-family:'Noto Serif SC',serif;font-weight:600;font-size:23px;color:var(--ink);text-align:center;line-height:1.15;padding:0 4px}
.cl.k{background:var(--brick-soft);border-color:var(--brick);color:var(--brick-d);font-size:20px}
.cl.t{background:var(--good-soft);border-color:var(--good);color:var(--good);font-size:19px}
.cl.q{font-size:22px}
.cl.e{background:var(--grey-soft);border-style:dashed;color:var(--grey)}
.ru{flex:1 1 auto;font-size:14.5px;color:var(--ink-2);line-height:1.32}

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
      <div class="eyebrow">Четыре конструкции</div>
      <h2>Одна мысль, <i>четыре разные сборки</i></h2>
    </div>
    <div class="hint">Колонки у всех четырёх одинаковые. Прочерк значит, что <b>ячейка пустует</b>: в последней строке сравнивать не с кем.</div>
  </div>

  <div class="hd"><div class="sp"></div><div class="cells">%(heads)s</div><div class="sp2"></div></div>
  %(rows)s

  <div class="foot">
    <div class="msg">Ни в одну ячейку <b>не встаёт 很</b>: степень задаёт сама связка</div>
    <div class="brand"><span class="dot2"></span><b>Kitai School</b><span>&middot; kitai-school.ru</span></div>
  </div>
</div>
</body></html>""" % dict(fonts=FONTS, vars=VARS, h=556, heads=head_cells, rows=rows)

open(S + "sravn-info.html", "w", encoding="utf-8").write(info)

print("ok | частей фразы:", len(PARTS), "| конструкций:", len(CONSTR), "| слотов:", len(SLOTS))
print("很 в данных нет, оценочных слов нет")
