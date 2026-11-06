# -*- coding: utf-8 -*-
# Картинки к статье «Образование в России и Китае»
# Обложка     — две траектории на общей оси лет с отметками границ и экзаменов
# Инфографика — три корзины сопоставления: совпадает, расходится, сравнить не удалось
S = ("/tmp/claude-0/-home-user-Kitai-Shool/a463bfca-82a9-56fd-ae09-42a7257ff999/"
     "scratchpad/")

FONTS = ("<link href=\"https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,600;0,700;1,600"
         "&family=Inter:wght@400;500;600;700&family=Noto+Serif+SC:wght@500;600;700&display=swap\" rel=\"stylesheet\">")
VARS = (":root{--brick:#A41E3A;--brick-d:#841630;--brick-soft:#F7E6EB;--ink:#2C2420;--ink-2:#5A4F45;"
        "--taupe:#8B7D6B;--cream:#FAF7F2;--cream-2:#F3EDE3;--hair:#EAE3D8;--surface:#fff;"
        "--good:#2F6F4F;--good-soft:#E8F3EC;--grey:#8A8178;--grey-soft:#EFEDE8;--navy:#2F4F6F;"
        "--navy-soft:#E7EEF5}")

YEARS = 12

# ─────────── данные: две траектории ───────────
# страна, сколько лет школа, граница обязательной части, экзамен после девятого, выпускной экзамен
TRACKS = [
    ("Россия", 11, 9, "ОГЭ", "ЕГЭ", "navy"),
    ("Китай", 12, 9, "中考", "高考", "brick"),
]

# ─────────── данные: параметры сопоставления ───────────
# параметр, Россия, Китай, корзина, причина (для корзины «не удалось»)
FACTS = [
    ("Обязательная часть", "9 классов", "9 лет 义务教育", "same", ""),
    ("Экзамен после девятого", "ОГЭ", "中考", "same", ""),
    ("Время выпускного экзамена", "конец мая — июнь", "обычно начало июня", "same", ""),
    ("Длина школы", "11 лет: 4+5+2", "12 лет: 6+3+3", "diff", ""),
    ("Что решает экзамен после девятого", "аттестует за основную школу",
     "распределяет в старшую школу или училище", "diff", ""),
    ("Выпускной экзамен", "2 обязательных предмета плюс выбор, 100 баллов",
     "750 баллов, модель 3+1+2", "diff", ""),
    ("Возраст приёма", "6 лет 6 месяцев — 8 лет", "6 полных лет к 1 сентября", "diff", ""),
    ("Школьная шкала оценок", "пятибалльная практика", "стобалльная, порог 60", "diff", ""),
    ("Годовая нагрузка в часах", "сопоставимых цифр не нашла", "910 и 1050 часов", "none",
     "нет российских данных в том же виде"),
    ("Публикация результатов", "правил не нашла", "запрет на рейтинги с 2021 года", "none",
     "сравнение вышло бы односторонним"),
]
BASKETS = [("same", "Совпадает"), ("diff", "Расходится"), ("none", "Сравнить не удалось")]
BAD = ["лучш", "хуже", "сильн", "слаб", "гуманн", "жёстч", "эффективн", "отстал", "передов"]

# ── проверки данных
assert len(TRACKS) == 2, "траекторий должно быть две"
for c, total, must, mid, fin, col in TRACKS:
    assert 0 < must < total <= YEARS, "границы у «%s» не укладываются в ось" % c
    assert mid and fin, "у «%s» не названы экзамены" % c
assert TRACKS[0][2] == TRACKS[1][2], "обязательная часть совпадает — на этом держится картинка"
keys = [b[0] for b in BASKETS]
for p, ru, cn, bask, why in FACTS:
    assert bask in keys, "неизвестная корзина: %s" % bask
    assert p and ru and cn, "у параметра «%s» пустая сторона" % p
    assert (bask == "none") == bool(why), "причина нужна только у несопоставимых: %s" % p
    for v in (p, ru, cn, why):
        assert not any(b in v.lower() for b in BAD), "оценочное слово: %s" % v
for k, title in BASKETS:
    assert any(f[3] == k for f in FACTS), "корзина «%s» пуста" % title

# ─────────── обложка: две траектории на общей оси лет ───────────
STEP = 72          # пикселей на год
LEFT = 124         # отступ оси слева внутри карточки


def x(year):
    return LEFT + (year - 1) * STEP + STEP // 2


ticks = "".join('<div class="yr" style="left:%dpx">%d</div>' % (x(y), y)
                for y in range(1, YEARS + 1))

lines = ""
for c, total, must, mid, fin, col in TRACKS:
    x0, xm, xe = x(1) - 13, x(must) + STEP // 2, x(total) + 13
    lines += """<div class="tr %s">
      <div class="lbl">%s</div>
      <div class="ln must" style="left:%dpx;width:%dpx"></div>
      <div class="ln free" style="left:%dpx;width:%dpx"></div>
      <div class="seg" style="left:%dpx;width:%dpx"><span>обязательная</span></div>
      <div class="seg f" style="left:%dpx;width:%dpx"><span>по выбору</span></div>
      <div class="ev must" style="left:%dpx"><b>%s</b><span>конец обязательной части</span></div>
      <div class="ev fin" style="left:%dpx"><b>%s</b><span>%d лет школы</span></div>
    </div>""" % (col, c, x0, xm - x0, xm, xe - xm, x0, xm - x0, xm, xe - xm,
                 xm, mid, x(total), fin, total)

hero = """<!DOCTYPE html><html lang="ru"><head><meta charset="utf-8">
%(fonts)s
<style>
%(vars)s
*{margin:0;box-sizing:border-box}html,body{width:1200px;height:630px}
.card{width:1200px;height:630px;background:radial-gradient(1040px 700px at 10%% 6%%, #fff 0%%, var(--cream) 52%%, var(--cream-2) 100%%);position:relative;overflow:hidden;font-family:'Inter',sans-serif;padding:34px 48px 58px 60px;display:flex;flex-direction:column}
.card:before{content:"";position:absolute;left:0;top:0;bottom:0;width:12px;background:var(--brick)}
.head{display:flex;justify-content:space-between;align-items:flex-end;gap:30px;margin-bottom:26px}
.eyebrow{color:var(--brick);font-weight:700;font-size:18px;letter-spacing:.19em;text-transform:uppercase;margin-bottom:11px}
h1{font-family:'Cormorant Garamond',serif;font-weight:600;font-size:37px;line-height:1.07;color:var(--ink);letter-spacing:-.3px;max-width:24ch}
h1 i{font-style:italic;color:var(--brick)}
.tip{flex:0 0 340px;background:var(--surface);border:1px solid var(--hair);border-left:4px solid var(--brick);border-radius:13px;padding:13px 18px;font-size:15px;color:var(--ink-2);line-height:1.38}
.tip b{color:var(--ink)}

.chart{position:relative;background:var(--surface);border:1px solid var(--hair);border-radius:14px;padding:18px 18px 14px;height:322px}
.axis{position:absolute;left:0;right:18px;top:40px;height:22px}
.yr{position:absolute;transform:translateX(-50%%);font-size:12.5px;font-weight:600;color:var(--taupe)}
.grid{position:absolute;top:62px;bottom:52px;width:1px;background:#F0EAE0}
.axname{position:absolute;left:18px;top:16px;font-size:12px;font-weight:700;letter-spacing:.12em;text-transform:uppercase;color:var(--taupe)}

.tr{position:absolute;left:0;right:0;height:96px}
.tr.navy{top:76px}
.tr.brick{top:196px}
.lbl{position:absolute;left:18px;top:32px;font-size:16px;font-weight:700;color:var(--ink)}
.ln{position:absolute;top:40px;height:12px}
.ln.must{border-radius:6px 0 0 6px}
.ln.free{border-radius:0 6px 6px 0}
.tr.navy .ln.must{background:#8FA8BF;border:1px solid #7C96AE}
.tr.navy .ln.free{background:var(--navy-soft);border:1px solid #C3D2DF}
.tr.brick .ln.must{background:#D79AAA;border:1px solid #C9869A}
.tr.brick .ln.free{background:var(--brick-soft);border:1px solid #E6C3CD}
.seg{position:absolute;top:56px;text-align:center}
.seg span{font-size:11.5px;font-weight:600;letter-spacing:.06em;color:var(--taupe)}
.ev{position:absolute;transform:translateX(-50%%);text-align:center;width:168px}
.ev:before{content:"";position:absolute;left:50%%;width:2px;height:15px;transform:translateX(-50%%)}
.ev.must{top:-22px}
.ev.must:before{bottom:-17px}
.ev.fin{top:76px}
.ev.fin:before{top:-15px}
.tr.navy .ev:before{background:var(--navy)}
.tr.brick .ev:before{background:var(--brick)}
.ev b{display:block;font-size:17px;line-height:1.15;font-family:'Noto Serif SC',serif}
.tr.navy .ev b{color:var(--navy)}
.tr.brick .ev b{color:var(--brick)}
.ev span{display:block;font-size:12px;color:var(--taupe);margin-top:1px;line-height:1.2}

.brand{position:absolute;left:60px;bottom:20px;display:flex;align-items:center;gap:11px;color:var(--ink)}
.brand b{font-family:'Cormorant Garamond',serif;font-weight:700;font-size:26px}
.brand .bdot{width:10px;height:10px;border-radius:50%%;background:var(--brick)}
.brand span{color:var(--taupe);font-size:16px}
</style></head><body>
<div class="card">
  <div class="head">
    <div>
      <div class="eyebrow">Школа</div>
      <h1>Образование в России и Китае: <i>чем системы похожи и где расходятся</i></h1>
    </div>
    <div class="tip">Обязательная часть кончается <b>на одном и том же году</b>. Дальше пути расходятся — и по длине, и по тому, что решает экзамен.</div>
  </div>

  <div class="chart">
    <div class="axname">год обучения</div>
    <div class="axis">%(ticks)s</div>
    %(lines)s
  </div>

  <div class="brand"><span class="bdot"></span><b>Kitai School</b><span>&middot; kitai-school.ru</span></div>
</div>
</body></html>""" % dict(fonts=FONTS, vars=VARS, ticks=ticks, lines=lines)

open(S + "obr-hero.html", "w", encoding="utf-8").write(hero)

# ─────────── инфографика: три корзины ───────────
cols = ""
for key, title in BASKETS:
    items = ""
    for p, ru, cn, bask, why in FACTS:
        if bask != key:
            continue
        tail = '<div class="why">%s</div>' % why if why else ""
        items += ('<div class="it"><div class="pm">%s</div>'
                  '<div class="sd"><span>РФ</span>%s</div>'
                  '<div class="sd"><span>КНР</span>%s</div>%s</div>' % (p, ru, cn, tail))
    n = sum(1 for f in FACTS if f[3] == key)
    cols += ('<div class="bk %s"><div class="bh">%s<i>%d</i></div>%s</div>' % (key, title, n, items))

info = """<!DOCTYPE html><html lang="ru"><head><meta charset="utf-8">
%(fonts)s
<style>
%(vars)s
*{margin:0;box-sizing:border-box}html,body{width:1200px;height:%(h)dpx}
.wrap{width:1200px;height:%(h)dpx;background:linear-gradient(180deg,#fff 0%%,var(--cream) 42%%,var(--cream-2) 100%%);font-family:'Inter',sans-serif;padding:38px 48px 26px;display:flex;flex-direction:column;position:relative;overflow:hidden}
.wrap:before{content:"";position:absolute;left:0;right:0;top:0;height:9px;background:var(--brick)}
.top{display:flex;align-items:flex-end;justify-content:space-between;gap:34px;margin-bottom:24px}
.eyebrow{color:var(--brick);font-weight:700;font-size:15.5px;letter-spacing:.19em;text-transform:uppercase;margin-bottom:8px}
h2{font-family:'Cormorant Garamond',serif;font-weight:600;font-size:38px;line-height:1.07;color:var(--ink);max-width:23ch}
h2 i{font-style:italic;color:var(--brick)}
.hint{flex:0 0 392px;background:var(--surface);border:1px solid var(--hair);border-left:4px solid var(--brick);border-radius:13px;padding:12px 18px;font-size:15px;color:var(--ink-2);line-height:1.36}
.hint b{color:var(--ink)}

.cols{display:flex;gap:14px;align-items:stretch}
.bk{flex:1 1 0;border-radius:14px;padding:12px;border:1px solid var(--hair);background:var(--surface)}
.bk.same{border-color:var(--good);background:var(--good-soft)}
.bk.diff{border-color:var(--brick);background:var(--brick-soft)}
.bk.none{border-color:var(--taupe);background:var(--grey-soft);border-style:dashed}
.bh{font-size:14px;font-weight:700;letter-spacing:.1em;text-transform:uppercase;margin-bottom:10px;display:flex;align-items:center;gap:8px}
.bk.same .bh{color:var(--good)}
.bk.diff .bh{color:var(--brick)}
.bk.none .bh{color:var(--taupe)}
.bh i{font-style:normal;font-size:12px;width:21px;height:21px;border-radius:50%%;display:flex;align-items:center;justify-content:center;color:#fff}
.bk.same .bh i{background:var(--good)}
.bk.diff .bh i{background:var(--brick)}
.bk.none .bh i{background:var(--taupe)}
.it{background:var(--surface);border:1px solid var(--hair);border-radius:10px;padding:9px 12px 10px;margin-bottom:9px}
.it:last-child{margin-bottom:0}
.pm{font-size:14px;font-weight:700;color:var(--ink);line-height:1.22;margin-bottom:5px}
.sd{font-size:13px;color:var(--ink-2);line-height:1.3;display:flex;gap:7px;margin-top:2px}
.sd span{flex:0 0 30px;font-size:10.5px;font-weight:700;letter-spacing:.07em;color:var(--taupe);padding-top:2px}
.why{margin-top:6px;font-size:12px;color:var(--taupe);line-height:1.28;border-top:1px dashed var(--hair);padding-top:5px}

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
      <div class="eyebrow">Сопоставление по параметрам</div>
      <h2>Третья колонка — <i>тоже результат</i></h2>
    </div>
    <div class="hint">Параметры разложены на три группы. В последней — то, что <b>сопоставить не удалось</b>, и причина у каждого пункта.</div>
  </div>

  <div class="cols">%(cols)s</div>

  <div class="foot">
    <div class="msg">Оценок «лучше» и «хуже» здесь нет: <b>только числа и то, чего в числах не нашлось</b></div>
    <div class="brand"><span class="dot2"></span><b>Kitai School</b><span>&middot; kitai-school.ru</span></div>
  </div>
</div>
</body></html>""" % dict(fonts=FONTS, vars=VARS, h=800, cols=cols)

open(S + "obr-info.html", "w", encoding="utf-8").write(info)

print("ok | параметров:", len(FACTS), "| корзины:",
      {t: sum(1 for f in FACTS if f[3] == k) for k, t in BASKETS})
print("оценочных слов в данных нет")
