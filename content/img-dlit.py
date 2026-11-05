# -*- coding: utf-8 -*-
# Картинки к статье «Сколько длится экзамен HSK»
# Обложка     — два циферблата: сорок минут против ста двадцати пяти
# Инфографика — пять составных полос, по строке на уровень
S = ("/tmp/claude-0/-home-user-Kitai-Shool/a463bfca-82a9-56fd-ae09-42a7257ff999/"
     "scratchpad/")

FONTS = ("<link href=\"https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,600;0,700;1,600"
         "&family=Inter:wght@400;500;600;700&family=Noto+Serif+SC:wght@600;700&display=swap\" rel=\"stylesheet\">")
VARS = (":root{--brick:#A41E3A;--brick-d:#841630;--brick-soft:#F7E6EB;--ink:#2C2420;--ink-2:#5A4F45;"
        "--taupe:#8B7D6B;--cream:#FAF7F2;--cream-2:#F3EDE3;--hair:#EAE3D8;--surface:#fff;"
        "--aud:#A41E3A;--chi:#2F6F4F;--pis:#B5873A;--rest:#D8CFBF}")

# ─────────── данные: одна таблица на текст и обе картинки ───────────
# (уровень, вопросов, аудирование, чтение, письмо, итого с анкетой)
LEVELS = [
    ("HSK 1", 40, 15, 17, 0, 40),
    ("HSK 2", 60, 25, 22, 0, 55),
    ("HSK 3", 80, 35, 30, 15, 90),
    ("HSK 4", 100, 30, 40, 25, 105),
    ("HSK 5", 100, 30, 40, 40, 125),
]

# ── проверки данных
assert len(LEVELS) == 5, "уровней должно быть пять, их %d" % len(LEVELS)
tot_prev = 0
for name, q, aud, chi, pis, tot in LEVELS:
    assert aud + chi + pis <= tot, "%s: сумма разделов больше общего времени" % name
    assert tot > tot_prev, "%s: время должно расти от уровня к уровню" % name
    tot_prev = tot
assert all(l[4] == 0 for l in LEVELS[:2]), "письма на первых двух уровнях нет"
assert all(l[4] > 0 for l in LEVELS[2:]), "письмо есть начиная с третьего уровня"
MAXT = max(l[5] for l in LEVELS)
assert MAXT == 125, "самый длинный экзамен в таблице — сто двадцать пять минут"
SHORT = LEVELS[0][5]
assert SHORT == 40, "самый короткий — сорок минут"
# секунды на один вопрос: время заданий без анкеты, делённое на число вопросов
PER_Q = {l[0]: round((l[2] + l[3] + l[4]) * 60.0 / l[1]) for l in LEVELS}
assert all(40 <= v <= 75 for v in PER_Q.values()), "счёт на вопрос вышел за ожидаемое: %s" % PER_Q
assert PER_Q["HSK 5"] != 53, "53 секунды — счёт соседа по чтению HSK 5, у нас другой счёт"

# ─────────── обложка: два циферблата ───────────
# ВАЖНО: полный круг у обоих — самый длинный экзамен из пяти (125 минут),
# иначе короткий экзамен занимал бы больший сектор, чем длинный.
DIAL_FULL = MAXT
assert DIAL_FULL == 125, "полный круг — сто двадцать пять минут"


def dial(minutes, cap, note, accent):
    deg = 360.0 * minutes / DIAL_FULL
    assert 0 < deg <= 360, "сектор вышел за круг"
    wedge = ('background:conic-gradient(%s 0deg, %s %.2fdeg, #EFE8DC %.2fdeg, #EFE8DC 360deg)'
             % (accent, accent, deg, deg))
    ticks = "".join('<i style="transform:rotate(%.1fdeg)"></i>' % (k * 72.0) for k in range(5))
    return ('<div class="dl"><div class="face" style="%s">%s<div class="hub"></div></div>'
            '<div class="mins">%d <b>мин</b></div><div class="cap">%s</div>'
            '<div class="note">%s</div></div>' % (wedge, ticks, minutes, cap, note))


left = dial(SHORT, "HSK 1", "два раздела, письма нет", "var(--brick)")
right = dial(MAXT, "HSK 5", "три раздела, письмо сорок минут", "var(--chi)")

hero = """<!DOCTYPE html><html lang="ru"><head><meta charset="utf-8">
%(fonts)s
<style>
%(vars)s
*{margin:0;box-sizing:border-box}html,body{width:1200px;height:630px}
.card{width:1200px;height:630px;background:radial-gradient(1020px 680px at 12%% 8%%, #fff 0%%, var(--cream) 50%%, var(--cream-2) 100%%);position:relative;overflow:hidden;font-family:'Inter',sans-serif;padding:54px 48px 0 72px;display:flex;justify-content:space-between}
.card:before{content:"";position:absolute;left:0;top:0;bottom:0;width:12px;background:var(--brick)}
.txt{flex:0 0 470px;padding-top:10px}
.eyebrow{color:var(--brick);font-weight:700;font-size:18px;letter-spacing:.19em;text-transform:uppercase;margin-bottom:14px}
h1{font-family:'Cormorant Garamond',serif;font-weight:600;font-size:44px;line-height:1.06;color:var(--ink);letter-spacing:-.4px}
h1 i{font-style:italic;color:var(--brick)}
.sub{font-size:18px;color:var(--ink-2);line-height:1.42;max-width:30ch;margin-top:17px}
.tip{display:inline-block;margin-top:22px;background:var(--surface);border:1px solid var(--hair);border-left:4px solid var(--brick);border-radius:13px;padding:14px 20px;font-size:15.5px;color:var(--ink-2);line-height:1.38;max-width:33ch}
.tip b{color:var(--ink)}

.scene{flex:0 0 556px;display:flex;flex-direction:column;align-items:center;padding-top:6px}
.dials{display:flex;gap:40px;align-items:flex-start;margin-top:14px}
.dl{width:250px;text-align:center}
.face{width:244px;height:244px;border-radius:50%%;margin:0 auto;position:relative;border:3px solid var(--ink);box-shadow:0 12px 26px rgba(44,36,32,.18)}
.face i{position:absolute;left:50%%;top:-17px;width:3px;height:13px;background:var(--taupe);transform-origin:50%% 139px;margin-left:-1.5px;border-radius:2px}
.hub{position:absolute;left:50%%;top:50%%;width:16px;height:16px;border-radius:50%%;background:var(--ink);transform:translate(-50%%,-50%%)}
.mins{font-family:'Cormorant Garamond',serif;font-weight:700;font-size:34px;color:var(--ink);margin-top:18px;line-height:1}
.mins b{font-family:'Inter',sans-serif;font-size:16px;font-weight:600;color:var(--taupe)}
.cap{font-size:17px;font-weight:700;color:var(--ink);margin-top:6px}
.note{font-size:13.5px;color:var(--ink-2);line-height:1.3;margin-top:3px;padding:0 6px}
.under{margin-top:26px;text-align:center;font-size:16px;color:var(--ink-2);line-height:1.4;max-width:42ch}
.under b{color:var(--ink)}
.brand{position:absolute;left:72px;bottom:28px;display:flex;align-items:center;gap:11px;color:var(--ink)}
.brand b{font-family:'Cormorant Garamond',serif;font-weight:700;font-size:26px}
.brand .bdot{width:10px;height:10px;border-radius:50%%;background:var(--brick)}
.brand span{color:var(--taupe);font-size:16px}
</style></head><body>
<div class="card">
  <div class="txt">
    <div class="eyebrow">Экзамены</div>
    <h1>Сколько длится экзамен HSK: <i>тайминг по уровням</i></h1>
    <div class="sub">От сорока минут на первом уровне до двух часов на пятом — и дело не только в длине.</div>
    <div class="tip"><b>Полный круг на обоих циферблатах</b> — сто двадцать пять минут, то есть всё время самого длинного экзамена из пяти.</div>
    <div class="brand"><span class="bdot"></span><b>Kitai School</b><span>&middot; kitai-school.ru</span></div>
  </div>

  <div class="scene">
    <div class="dials">%(left)s%(right)s</div>
    <div class="under">Между HSK 1 и HSK 5 разница втрое, а число разделов вырастает с двух до трёх.<br>Время по разделам примерное, <b>по действующей редакции HSK 2.0</b></div>
  </div>
</div>
</body></html>""" % dict(fonts=FONTS, vars=VARS, left=left, right=right)

open(S + "dlit-hero.html", "w", encoding="utf-8").write(hero)

# ─────────── инфографика: пять составных полос ───────────
rows = []
for name, q, aud, chi, pis, tot in LEVELS:
    rest = tot - aud - chi - pis
    segs = [("aud", aud, "听力"), ("chi", chi, "阅读"), ("pis", pis, "书写"), ("rest", rest, "")]
    inner = "".join(
        '<span class="sg %s" style="width:%.3f%%">%s</span>'
        % (cls, 100.0 * val / tot, ('<i>%d</i>' % val) if val >= 14 else "")
        for cls, val, lab in segs if val > 0)
    rows.append(
        '<div class="rw"><span class="nm">%s</span>'
        '<span class="barwrap"><span class="track" style="width:%.3f%%">%s</span></span>'
        '<span class="tot">%d <b>мин</b></span>'
        '<span class="pq">%d с<i>на вопрос</i></span></div>'
        % (name, 100.0 * tot / MAXT, inner, tot, PER_Q[name]))
bars = "\n".join(rows)

info = """<!DOCTYPE html><html lang="ru"><head><meta charset="utf-8">
%(fonts)s
<style>
%(vars)s
*{margin:0;box-sizing:border-box}html,body{width:1200px;height:%(h)dpx}
.wrap{width:1200px;height:%(h)dpx;background:linear-gradient(180deg,#fff 0%%,var(--cream) 40%%,var(--cream-2) 100%%);font-family:'Inter',sans-serif;padding:38px 48px 30px;display:flex;flex-direction:column;position:relative;overflow:hidden}
.wrap:before{content:"";position:absolute;left:0;right:0;top:0;height:9px;background:var(--brick)}
.top{display:flex;align-items:flex-end;justify-content:space-between;gap:34px;margin-bottom:24px}
.eyebrow{color:var(--brick);font-weight:700;font-size:15.5px;letter-spacing:.19em;text-transform:uppercase;margin-bottom:8px}
h2{font-family:'Cormorant Garamond',serif;font-weight:600;font-size:38px;line-height:1.07;color:var(--ink);max-width:20ch}
h2 i{font-style:italic;color:var(--brick)}
.hint{flex:0 0 416px;background:var(--surface);border:1px solid var(--hair);border-left:4px solid var(--brick);border-radius:13px;padding:12px 18px;font-size:15px;color:var(--ink-2);line-height:1.36}
.hint b{color:var(--ink)}

.chart{display:flex;flex-direction:column;gap:15px;padding-left:4px}
.rw{display:flex;align-items:center;gap:0}
.nm{flex:0 0 78px;font-size:17px;font-weight:700;color:var(--ink)}
.barwrap{flex:1 1 auto;display:flex}
.track{height:42px;border-radius:7px;overflow:hidden;display:flex;box-shadow:0 2px 0 rgba(44,36,32,.05)}
.sg{height:42px;display:flex;align-items:center;justify-content:center;position:relative}
.sg i{font-style:normal;font-size:13.5px;font-weight:700;color:#fff}
.sg.aud{background:var(--aud)}
.sg.chi{background:var(--chi)}
.sg.pis{background:var(--pis)}
.sg.rest{background:var(--rest)}
.sg.rest i{color:var(--ink-2)}
.tot{flex:0 0 104px;padding-left:16px;text-align:right;font-size:17px;font-weight:700;color:var(--ink);white-space:nowrap}
.tot b{font-size:13px;font-weight:600;color:var(--taupe)}
.pq{flex:0 0 116px;padding-left:18px;font-size:15px;font-weight:700;color:var(--ink-2);white-space:nowrap}
.pq i{display:block;font-style:normal;font-size:11.5px;font-weight:500;color:var(--taupe);letter-spacing:.02em}

.legend{display:flex;gap:24px;margin-top:24px;padding-left:82px;flex-wrap:wrap}
.lg{display:flex;align-items:center;gap:9px;font-size:14.5px;color:var(--ink-2)}
.lg i{width:24px;height:14px;border-radius:4px;display:block}
.lg.a i{background:var(--aud)}
.lg.b i{background:var(--chi)}
.lg.c i{background:var(--pis)}
.lg.d i{background:var(--rest)}

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
      <div class="eyebrow">Пять уровней подряд</div>
      <h2>Время растёт, <i>а минута на вопрос — почти нет</i></h2>
    </div>
    <div class="hint">Длина полосы — всё время экзамена. Справа — <b>сколько секунд приходится на один вопрос</b>: разница между уровнями меньше, чем кажется.</div>
  </div>

  <div class="chart">
%(bars)s
  </div>

  <div class="legend">
    <span class="lg a"><i></i>听力 — аудирование</span>
    <span class="lg b"><i></i>阅读 — чтение</span>
    <span class="lg c"><i></i>书写 — письмо</span>
    <span class="lg d"><i></i>анкета и бланк</span>
  </div>

  <div class="foot">
    <div class="msg">Время по разделам примерное, <b>по действующей редакции HSK 2.0</b>: порядок частей зависит от центра и уровня</div>
    <div class="brand"><span class="dot2"></span><b>Kitai School</b><span>&middot; kitai-school.ru</span></div>
  </div>
</div>
</body></html>""" % dict(fonts=FONTS, vars=VARS, h=640, bars=bars)

open(S + "dlit-info.html", "w", encoding="utf-8").write(info)

print("ok | уровней:", len(LEVELS), "| самый короткий:", SHORT, "| самый длинный:", MAXT)
print("секунд на вопрос:", PER_Q)
