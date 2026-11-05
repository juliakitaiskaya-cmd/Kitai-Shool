# -*- coding: utf-8 -*-
# Картинки к статье «Средняя зарплата в Китае»
# Обложка     — расчётный лист: 税前 сверху, удержания, 税后 внизу
# Инфографика — три столбца трёх официальных «средних»
S = ("/tmp/claude-0/-home-user-Kitai-Shool/a463bfca-82a9-56fd-ae09-42a7257ff999/"
     "scratchpad/")

FONTS = ("<link href=\"https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,600;0,700;1,600"
         "&family=Inter:wght@400;500;600;700&family=Noto+Serif+SC:wght@600;700&display=swap\" rel=\"stylesheet\">")
VARS = (":root{--brick:#A41E3A;--brick-d:#841630;--brick-soft:#F7E6EB;--ink:#2C2420;--ink-2:#5A4F45;"
        "--taupe:#8B7D6B;--cream:#FAF7F2;--cream-2:#F3EDE3;--hair:#EAE3D8;--surface:#fff;"
        "--paper:#FFFDF8;--good:#2F6F4F;--good-soft:#E8F3EC}")

# ─────────── данные: три официальные «средние», 2025 ───────────
# (годовая сумма в юанях, краткое имя, охват)
MEANS = [
    (129441, "Городские негосударственные единицы",
     "самый цитируемый показатель: его и называют «средней зарплатой в Китае»"),
    (106080, "Предприятия выше установленного размера",
     "только достаточно крупные предприятия"),
    (71590, "Городские частные единицы",
     "частный сектор в городах"),
]
GROWTH = 4.3            # рост первой цифры к прошлому году, номинально, %
MEDIAN_SHARE = 83.5     # медианный доход на душу от среднего, %

assert len(MEANS) == 3, "показателей должно быть три"
vals = [m[0] for m in MEANS]
assert vals == sorted(vals, reverse=True), "столбцы должны идти по убыванию"
assert vals[0] / float(vals[-1]) > 1.7, "разрыв между крайними — почти вдвое"
assert 0 < MEDIAN_SHARE < 100, "доля медианы меньше среднего"
MONTH = {v: int(round(v / 12.0)) for v in vals}
for v in vals:
    assert abs(MONTH[v] * 12 - v) <= 12, "месячное значение не сходится с годовым"
TOP = vals[0]


def ru(n):
    s = "%d" % n
    out = ""
    while len(s) > 3:
        out = " " + s[-3:] + out
        s = s[:-3]
    return s + out


# ─────────── обложка: расчётный лист ───────────
# строки удержаний: без сумм — только подписи, чужую платёжку не выдумываем
HOLD = [
    ("社保", "shèbǎo", "социальное страхование"),
    ("公积金", "gōngjījīn", "жилищный фонд"),
    ("个税", "gèshuì", "подоходный налог"),
]
assert len(HOLD) == 3, "строк удержаний должно быть три"
hold_rows = "".join(
    '<div class="hr"><span class="hz">%s</span><span class="hp">%s</span>'
    '<span class="hd">%s</span><span class="hm">&minus;</span></div>' % h for h in HOLD)

hero = """<!DOCTYPE html><html lang="ru"><head><meta charset="utf-8">
%(fonts)s
<style>
%(vars)s
*{margin:0;box-sizing:border-box}html,body{width:1200px;height:630px}
.card{width:1200px;height:630px;background:radial-gradient(1020px 680px at 12%% 8%%, #fff 0%%, var(--cream) 50%%, var(--cream-2) 100%%);position:relative;overflow:hidden;font-family:'Inter',sans-serif;padding:52px 48px 0 72px;display:flex;justify-content:space-between}
.card:before{content:"";position:absolute;left:0;top:0;bottom:0;width:12px;background:var(--brick)}
.txt{flex:0 0 486px;padding-top:10px}
.eyebrow{color:var(--brick);font-weight:700;font-size:18px;letter-spacing:.19em;text-transform:uppercase;margin-bottom:14px}
h1{font-family:'Cormorant Garamond',serif;font-weight:600;font-size:44px;line-height:1.06;color:var(--ink);letter-spacing:-.4px}
h1 i{font-style:italic;color:var(--brick)}
.sub{font-size:18px;color:var(--ink-2);line-height:1.42;max-width:31ch;margin-top:17px}
.tip{display:inline-block;margin-top:22px;background:var(--surface);border:1px solid var(--hair);border-left:4px solid var(--brick);border-radius:13px;padding:14px 20px;font-size:15.5px;color:var(--ink-2);line-height:1.38;max-width:34ch}
.tip b{color:var(--ink)}

.scene{flex:0 0 540px;display:flex;flex-direction:column;align-items:center;padding-top:2px}
.slip{width:466px;background:var(--paper);border:1px solid var(--hair);border-radius:14px;box-shadow:0 14px 30px rgba(44,36,32,.16);padding:20px 24px 22px;position:relative}
.slip:before{content:"";position:absolute;left:0;right:0;top:0;height:7px;border-radius:14px 14px 0 0;background:var(--brick)}
.slip .ttl{font-size:13px;font-weight:700;letter-spacing:.14em;text-transform:uppercase;color:var(--taupe);margin-top:8px}
.row{display:flex;align-items:baseline;gap:10px;margin-top:14px}
.row .z{font-family:'Noto Serif SC',serif;font-weight:700;font-size:30px;color:var(--ink);line-height:1}
.row .p{font-size:13px;color:var(--taupe)}
.row .d{margin-left:auto;font-size:14.5px;color:var(--ink-2);text-align:right;max-width:21ch;line-height:1.25}
.sep{height:1px;background:var(--hair);margin:16px 0 10px}
.holds{display:flex;flex-direction:column;gap:11px}
.hr{display:flex;align-items:center;gap:9px;font-size:14px;color:var(--ink-2)}
.hz{font-family:'Noto Serif SC',serif;font-weight:600;font-size:18px;color:var(--ink);min-width:56px}
.hp{font-size:12px;color:var(--taupe);min-width:62px}
.hd{flex:1 1 auto}
.hm{font-size:17px;color:var(--brick);font-weight:700;min-width:14px;text-align:center}
.hm.plus{color:var(--good)}
.outrow{display:flex;align-items:baseline;gap:10px;margin-top:14px;background:var(--good-soft);border:1px solid #BFD9C9;border-radius:11px;padding:12px 14px}
.outrow .z{font-family:'Noto Serif SC',serif;font-weight:700;font-size:30px;color:var(--good);line-height:1}
.outrow .p{font-size:13px;color:var(--taupe)}
.outrow .d{margin-left:auto;font-size:14.5px;color:var(--ink);font-weight:700;text-align:right}
.under{margin-top:18px;text-align:center;font-size:15.5px;color:var(--ink-2);line-height:1.4;max-width:40ch}
.under b{color:var(--ink)}
.brand{position:absolute;left:72px;bottom:26px;display:flex;align-items:center;gap:11px;color:var(--ink)}
.brand b{font-family:'Cormorant Garamond',serif;font-weight:700;font-size:26px}
.brand .bdot{width:10px;height:10px;border-radius:50%%;background:var(--brick)}
.brand span{color:var(--taupe);font-size:16px}
</style></head><body>
<div class="card">
  <div class="txt">
    <div class="eyebrow">Китай · работа</div>
    <h1>Средняя зарплата в Китае: <i>сколько реально платят</i></h1>
    <div class="sub">Официальных «средних» сразу три, и отличаются они почти вдвое — потому что считают разное.</div>
    <div class="tip"><b>Все публикуемые цифры — до вычетов.</b> На карту приходит меньше, и спрашивать об этом принято сразу.</div>
    <div class="brand"><span class="bdot"></span><b>Kitai School</b><span>&middot; kitai-school.ru</span></div>
  </div>

  <div class="scene">
    <div class="slip">
      <div class="ttl">Расчётный лист</div>
      <div class="row"><span class="z">税前</span><span class="p">shuìqián</span><span class="d">начислено до вычетов</span></div>
      <div class="sep"></div>
      <div class="holds"><div class="hr"><span class="hz">底薪</span><span class="hp">dǐxīn</span><span class="hd">оклад</span><span class="hm plus">+</span></div>
      <div class="hr"><span class="hz">奖金</span><span class="hp">jiǎngjīn</span><span class="hd">премия</span><span class="hm plus">+</span></div></div>
      <div class="sep"></div>
      <div class="holds">%(holds)s</div>
      <div class="outrow"><span class="z">税后</span><span class="p">shuìhòu</span><span class="d">на руки</span></div>
    </div>
    <div class="under">Сумм на листе нет намеренно: <b>удержания зависят от города и дохода</b></div>
  </div>
</div>
</body></html>""" % dict(fonts=FONTS, vars=VARS, holds=hold_rows)

open(S + "zp-hero.html", "w", encoding="utf-8").write(hero)

# ─────────── инфографика: три столбца ───────────
HMAX = 268  # пикселей на самый высокий столбец
bars = "".join(
    '<div class="col"><div class="val">%s <b>¥</b><i>в год</i></div>'
    '<div class="bar" style="height:%.1fpx"><span class="mo">%s ¥<i>в месяц</i></span></div></div>'
    % (ru(v), HMAX * v / float(TOP), ru(MONTH[v]))
    for v, name, scope in MEANS)
capts = "".join(
    '<div class="cp"><div class="nm">%s</div><div class="sc">%s</div></div>' % (name, scope)
    for v, name, scope in MEANS)

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
.hint{flex:0 0 404px;background:var(--surface);border:1px solid var(--hair);border-left:4px solid var(--brick);border-radius:13px;padding:12px 18px;font-size:15px;color:var(--ink-2);line-height:1.36}
.hint b{color:var(--ink)}

.body{display:flex;gap:30px;align-items:flex-end}
.charts{flex:1 1 auto;display:flex;flex-direction:column}
.cols{display:grid;grid-template-columns:repeat(3,1fr);gap:30px;align-items:end}
.capts{display:grid;grid-template-columns:repeat(3,1fr);gap:30px;margin-top:14px}
.cp{text-align:center}
.col{display:flex;flex-direction:column;align-items:center}
.val{font-family:'Cormorant Garamond',serif;font-weight:700;font-size:30px;color:var(--ink);line-height:1;margin-bottom:9px;white-space:nowrap}
.val b{font-family:'Inter',sans-serif;font-size:17px;color:var(--brick)}
.val i{font-style:normal;display:block;font-family:'Inter',sans-serif;font-size:12px;font-weight:500;color:var(--taupe);margin-top:4px;letter-spacing:.02em}
.bar{width:76%%;border-radius:10px 10px 0 0;background:linear-gradient(180deg,var(--brick) 0%%,var(--brick-d) 100%%);position:relative;display:flex;align-items:flex-end;justify-content:center;padding-bottom:12px}
.mo{font-size:15px;font-weight:700;color:#FFF0F3;text-align:center;line-height:1.2}
.mo i{font-style:normal;display:block;font-size:11.5px;font-weight:500;color:rgba(255,240,243,.8)}
.nm{font-size:14.5px;font-weight:700;color:var(--ink);line-height:1.26;padding:0 4px}
.sc{font-size:12.5px;color:var(--ink-2);margin-top:5px;line-height:1.3;padding:0 6px}

.side{flex:0 0 268px;background:var(--surface);border:1px solid var(--hair);border-radius:14px;padding:16px 18px;align-self:flex-end}
.side .lb{font-size:12.5px;font-weight:700;letter-spacing:.13em;text-transform:uppercase;color:var(--taupe)}
.side .big{font-family:'Cormorant Garamond',serif;font-weight:700;font-size:42px;color:var(--brick);line-height:1;margin-top:8px}
.side .tx{font-size:13.5px;color:var(--ink-2);line-height:1.34;margin-top:8px}
.side .tx b{color:var(--ink)}

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
      <div class="eyebrow">Данные за 2025 год</div>
      <h2>Три официальные «средние» — <i>и все три верные</i></h2>
    </div>
    <div class="hint">Разница не в ошибке, а в охвате: <b>каждый показатель считает свой круг работников</b>. Все суммы — до вычетов.</div>
  </div>

  <div class="body">
    <div class="charts"><div class="cols">%(bars)s</div><div class="capts">%(capts)s</div></div>
    <div class="side">
      <div class="lb">Медиана против среднего</div>
      <div class="big">%(med)s %%</div>
      <div class="tx">столько составляет <b>медианный доход на душу</b> от среднего. Половина получает меньше медианы — а значит, и меньше любой из цифр слева</div>
    </div>
  </div>

  <div class="foot">
    <div class="msg">Рост первого показателя к прошлому году — <b>%(gr)s %%</b> номинально. Источник — Национальное бюро статистики КНР</div>
    <div class="brand"><span class="dot2"></span><b>Kitai School</b><span>&middot; kitai-school.ru</span></div>
  </div>
</div>
</body></html>""" % dict(fonts=FONTS, vars=VARS, h=716, bars=bars, capts=capts,
                          med=("%.1f" % MEDIAN_SHARE).replace(".", ","),
                          gr=("%.1f" % GROWTH).replace(".", ","))

open(S + "zp-info.html", "w", encoding="utf-8").write(info)

print("ok | показателей:", len(MEANS), "| в месяц:", {ru(v): ru(MONTH[v]) for v in vals})
print("разрыв крайних: %.2f раза | медиана: %s %% | рост: %s %%"
      % (vals[0] / float(vals[-1]), MEDIAN_SHARE, GROWTH))
