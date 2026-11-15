# -*- coding: utf-8 -*-
# Картинки к статье «Баллы HSK»
# Обложка     — лесенка цены вопроса по шести уровням
# Инфографика — расчёт пробника в три шага с отметкой порога
import sys
sys.path.insert(0, "/home/user/Kitai-Shool/content")
from ball_hsk import (EXAMS, PRICE, MAXI, PASS, TOTAL_Q, SECTION_MAX,
                      EX_LEVEL, EX_STEPS, EX_TWO, EX_PASS, EX_NEED, EX_WRITE_MAX)

S = ("/tmp/claude-0/-home-user-Kitai-Shool/a463bfca-82a9-56fd-ae09-42a7257ff999/"
     "scratchpad/")

FONTS = ("<link href=\"https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,600;0,700;1,600"
         "&family=Inter:wght@400;500;600;700&display=swap\" rel=\"stylesheet\">")
VARS = (":root{--brick:#A41E3A;--brick-d:#841630;--brick-soft:#F7E6EB;--ink:#2C2420;--ink-2:#5A4F45;"
        "--taupe:#8B7D6B;--cream:#FAF7F2;--cream-2:#F3EDE3;--hair:#EAE3D8;--surface:#fff;"
        "--grey-soft:#EFEDE8;--grey:#9A9289}")

assert len(EXAMS) == 6

# ─────────── обложка: лесенка цены вопроса ───────────
LISTEN = [(lvl, PRICE[lvl]["аудирование"]) for lvl, a, r, w in EXAMS]
TOP = max(p for lvl, p in LISTEN)
MAXH = 248
assert LISTEN[0][1] == TOP, "самая высокая ступень — первый уровень"

steps = ""
for lvl, price in LISTEN:
    # шкала от нуля: высота прямо пропорциональна цене, без растяжки
    h = round(MAXH * price / TOP)
    first = lvl == LISTEN[0][0]
    steps += ("""<div class="st%(cls)s">
  <div class="val">%(price)s</div>
  <div class="bar" style="height:%(h)dpx"><span>%(q)d</span></div>
  <div class="lv">HSK %(lvl)d</div>
</div>""" % dict(cls=" top" if first else "", price=("%.1f" % price).replace(".", ","),
                 h=h, q=dict((e[0], e) for e in EXAMS)[lvl][1], lvl=lvl))
assert steps.count('class="st top"') == 1
assert steps.count('class="st"') == 5

hero = """<!DOCTYPE html><html lang="ru"><head><meta charset="utf-8">
%(fonts)s
<style>
%(vars)s
*{margin:0;box-sizing:border-box}html,body{width:1200px;height:630px}
.card{width:1200px;height:630px;background:radial-gradient(1040px 700px at 8%% 4%%, #fff 0%%, var(--cream) 54%%, var(--cream-2) 100%%);position:relative;overflow:hidden;font-family:'Inter',sans-serif;padding:28px 56px 50px 72px;display:flex;flex-direction:column}
.card:before{content:"";position:absolute;left:0;top:0;bottom:0;width:12px;background:var(--brick)}
.head{display:flex;justify-content:space-between;align-items:flex-end;gap:34px;margin-bottom:14px}
.eyebrow{color:var(--brick);font-weight:700;font-size:18px;letter-spacing:.19em;text-transform:uppercase;margin-bottom:8px}
h1{font-family:'Cormorant Garamond',serif;font-weight:600;font-size:37px;line-height:1.08;color:var(--ink);letter-spacing:-.3px;max-width:31ch}
h1 i{font-style:italic;color:var(--brick)}
.tip{flex:0 0 322px;background:var(--surface);border:1px solid var(--hair);border-left:4px solid var(--brick);border-radius:13px;padding:12px 18px;font-size:14.5px;color:var(--ink-2);line-height:1.38}
.tip b{color:var(--ink)}

.stage{flex:1 1 auto;min-height:0;display:flex;align-items:flex-end;gap:16px;padding:0 4px}
.st{flex:1 1 0;display:flex;flex-direction:column;align-items:center}
.val{font-family:'Cormorant Garamond',serif;font-weight:700;font-size:35px;color:var(--taupe);line-height:1;margin-bottom:9px}
.st.top .val{color:var(--brick);font-size:42px}
.bar{width:100%%;border-radius:10px 10px 0 0;background:var(--grey-soft);border:1px solid var(--hair);border-bottom:none;display:flex;align-items:flex-end;justify-content:center;padding-bottom:9px}
.st.top .bar{background:var(--brick-soft);border-color:var(--brick)}
.bar span{font-size:14px;font-weight:600;color:var(--taupe)}
.st.top .bar span{color:var(--brick-d)}
.lv{width:100%%;text-align:center;border-top:3px solid var(--taupe);padding-top:9px;font-size:17px;font-weight:700;color:var(--ink)}
.st.top .lv{border-top-color:var(--brick);color:var(--brick-d)}

.foot{margin-top:16px;display:flex;align-items:center;gap:18px;background:var(--surface);border:1px solid var(--hair);border-radius:13px;padding:11px 22px}
.foot b{font-size:12.5px;font-weight:700;letter-spacing:.11em;text-transform:uppercase;color:var(--brick);flex:0 0 auto}
.foot span{font-size:15px;color:var(--ink);line-height:1.36}

.brand{position:absolute;left:72px;bottom:16px;display:flex;align-items:center;gap:11px;color:var(--ink)}
.brand b{font-family:'Cormorant Garamond',serif;font-weight:700;font-size:24px}
.brand .bdot{width:10px;height:10px;border-radius:50%%;background:var(--brick)}
.brand span{color:var(--taupe);font-size:15px}
</style></head><body>
<div class="card">
  <div class="head">
    <div>
      <div class="eyebrow">Баллы HSK</div>
      <h1>Один вопрос: <i>чем выше уровень, тем дешевле ответ</i></h1>
    </div>
    <div class="tip">Раздел всегда стоит сто баллов, а вопросов в нём разное число. <b>Цифра над столбцом — цена одного ответа в аудировании, под ней число вопросов.</b></div>
  </div>

  <div class="stage">%(steps)s</div>

  <div class="foot"><b>что это значит</b><span>на первом уровне одна ошибка в аудировании стоит дороже, чем на шестом, — там вопросов вдвое больше</span></div>

  <div class="brand"><span class="bdot"></span><b>Kitai School</b><span>&middot; kitai-school.ru</span></div>
</div>
</body></html>""" % dict(fonts=FONTS, vars=VARS, steps=steps)

assert "%%" not in hero, "в разметке остались двойные проценты"
open(S + "ballhsk-hero.html", "w", encoding="utf-8").write(hero)

# ─────────── инфографика: расчёт в три шага ───────────
rows = ""
for name, ok, total, ball in EX_STEPS:
    rows += ("""<div class="rw">
  <div class="nm">%(name)s</div>
  <div class="eq"><b>%(ok)d</b> из %(total)d</div>
  <div class="sign">&times;</div>
  <div class="pr">%(price)s</div>
  <div class="sign">=</div>
  <div class="bl">%(ball)d</div>
</div>""" % dict(name=name, ok=ok, total=total, ball=ball,
                 price=("%.1f" % round(SECTION_MAX / total, 1)).replace(".", ",")))
assert rows.count('class="rw"') == 2

def ball_word(n):
    """Слово «балл» после «не хватает» — родительный падеж, считается по числу."""
    n = abs(n)
    if n % 100 // 10 != 1 and n % 10 == 1:
        return "балла"
    return "баллов"


assert (ball_word(1), ball_word(41), ball_word(11), ball_word(5), ball_word(42)) == \
    ("балла", "балла", "баллов", "баллов", "баллов"), "склонение считается верно"

SUM_PARTS = " + ".join(str(s3[3]) for s3 in EX_STEPS)
TWO_PCT = round(EX_TWO * 100.0 / MAXI[EX_LEVEL], 1)
NEED_PCT = round(EX_NEED * 100.0 / EX_WRITE_MAX, 1)
assert 0 < TWO_PCT < 100 and 0 < NEED_PCT < 100

info = """<!DOCTYPE html><html lang="ru"><head><meta charset="utf-8">
%(fonts)s
<style>
%(vars)s
*{margin:0;box-sizing:border-box}html,body{width:1200px;height:%(h)dpx}
.wrap{width:1200px;height:%(h)dpx;background:linear-gradient(180deg,#fff 0%%,var(--cream) 46%%,var(--cream-2) 100%%);font-family:'Inter',sans-serif;padding:30px 48px 26px;display:flex;flex-direction:column;position:relative;overflow:hidden}
.wrap:before{content:"";position:absolute;left:0;right:0;top:0;height:9px;background:var(--brick)}
.top{display:flex;align-items:flex-end;justify-content:space-between;gap:34px;margin-bottom:20px}
.eyebrow{color:var(--brick);font-weight:700;font-size:15.5px;letter-spacing:.19em;text-transform:uppercase;margin-bottom:7px}
h2{font-family:'Cormorant Garamond',serif;font-weight:600;font-size:34px;line-height:1.08;color:var(--ink);max-width:24ch}
h2 i{font-style:italic;color:var(--brick)}
.hint0{flex:0 0 340px;background:var(--surface);border:1px solid var(--hair);border-left:4px solid var(--brick);border-radius:13px;padding:11px 17px;font-size:14px;color:var(--ink-2);line-height:1.35}
.hint0 b{color:var(--ink)}

.steps{flex:1 1 auto;min-height:0;display:flex;gap:14px}
.sp{flex:1 1 0;background:var(--surface);border:1px solid var(--hair);border-radius:14px;padding:14px 18px 14px;display:flex;flex-direction:column}
.sp.last{border-color:var(--brick)}
.num{display:flex;align-items:center;gap:10px;margin-bottom:11px}
.num i{font-style:normal;width:28px;height:28px;border-radius:50%%;background:var(--brick);color:#fff;font-weight:700;font-size:15px;display:flex;align-items:center;justify-content:center;flex:0 0 auto}
.num span{font-size:13px;font-weight:700;letter-spacing:.1em;text-transform:uppercase;color:var(--brick)}
.ttl{font-size:16px;font-weight:600;color:var(--ink);line-height:1.3;margin-bottom:12px}

.rw{display:flex;align-items:center;gap:7px;margin-bottom:8px}
.rw .nm{flex:1 1 auto;font-size:13.5px;color:var(--ink-2)}
.rw .eq{font-size:13.5px;color:var(--ink)}
.rw .eq b{color:var(--brick-d)}
.rw .sign{color:var(--taupe);font-size:13px}
.rw .pr{font-size:13.5px;color:var(--ink-2)}
.rw .bl{min-width:38px;text-align:right;font-family:'Cormorant Garamond',serif;font-weight:700;font-size:25px;color:var(--ink);line-height:1}
.note{margin-top:auto;font-size:12.5px;color:var(--taupe);line-height:1.34}

.parts{font-size:19px;color:var(--taupe);margin-bottom:4px}
.sum{display:flex;align-items:baseline;gap:9px;margin-bottom:12px}
.sum b{font-family:'Cormorant Garamond',serif;font-weight:700;font-size:50px;color:var(--brick);line-height:1}
.sum span{font-size:14px;color:var(--ink-2)}

.scale{margin-bottom:11px}
.track{height:28px;border-radius:9px;background:var(--grey-soft);border:1px solid var(--hair);position:relative;overflow:hidden}
.fill{position:absolute;left:0;top:0;bottom:0;background:var(--brick);opacity:.78;border-radius:8px 0 0 8px}
.mark{position:absolute;top:-6px;bottom:-6px;width:3px;background:var(--ink)}
.lbl{position:relative;height:19px;margin-top:7px;font-size:12.5px;color:var(--taupe)}
.lbl .l0{position:absolute;left:0}
.lbl .l1{position:absolute;right:0}
.lbl b{position:absolute;transform:translateX(-50%%);white-space:nowrap;color:var(--ink)}
.need{background:var(--brick-soft);border-radius:10px;padding:10px 14px;font-size:14px;color:var(--ink);line-height:1.34}
.need b{color:var(--brick-d)}

.foot{margin-top:14px;flex:0 0 auto;display:flex;align-items:center;gap:18px}
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
      <div class="eyebrow">Пробник HSK %(lvl)d</div>
      <h2>Прикидка в три шага, <i>и честная остановка на письме</i></h2>
    </div>
    <div class="hint0">Аудирование и чтение можно посчитать самому. <b>Балл за письмо ставит проверяющий, поэтому в прикидке он остаётся пустым.</b></div>
  </div>

  <div class="steps">
    <div class="sp">
      <div class="num"><i>1</i><span>разделы</span></div>
      <div class="ttl">Верные ответы умножить на цену вопроса</div>
      %(rows)s
      <div class="note">Цена вопроса — сто баллов раздела, поделённые на число вопросов в нём</div>
    </div>

    <div class="sp">
      <div class="num"><i>2</i><span>сумма</span></div>
      <div class="ttl">Сложить то, что посчитано</div>
      <div class="parts">%(parts)s</div>
      <div class="sum"><b>%(two)d</b><span>из %(maxi)d возможных</span></div>
      <div class="note">Это сумма двух разделов из трёх. Письмо сюда ещё не входит, поэтому цифра неполная и сравнивать её с порогом рано</div>
    </div>

    <div class="sp last">
      <div class="num"><i>3</i><span>порог</span></div>
      <div class="ttl">Посмотреть, сколько осталось добрать</div>
      <div class="scale">
        <div class="track">
          <div class="fill" style="width:%(two_pct)s%%"></div>
          <div class="mark" style="left:%(pass_pct)s%%"></div>
        </div>
        <div class="lbl"><span class="l0">0</span><b style="left:%(pass_pct)s%%">порог %(pass)d</b><span class="l1">%(maxi)d</span></div>
      </div>
      <div class="need">До порога не хватает <b>%(need)d %(need_word)s</b> — столько нужно взять письмом из ста возможных</div>
      <div class="note">Прикидка показывает запас, а не результат: официальный балл считают по своей шкале</div>
    </div>
  </div>

  <div class="foot">
    <div class="msg">Считать стоит <b>до письма и отдельно</b>: так видно, какой раздел тянет вниз, и сколько остаётся на то, что оценивает не ученик</div>
    <div class="brand"><span class="dot2"></span><b>Kitai School</b><span>&middot; kitai-school.ru</span></div>
  </div>
</div>
</body></html>""" % dict(fonts=FONTS, vars=VARS, h=520, lvl=EX_LEVEL, rows=rows,
                         two=EX_TWO, maxi=MAXI[EX_LEVEL], pass_pct=round(EX_PASS * 100.0 / MAXI[EX_LEVEL], 1),
                         two_pct=TWO_PCT, need=EX_NEED, need_word=ball_word(EX_NEED), parts=SUM_PARTS, **{"pass": EX_PASS})

assert "%%" not in info, "в разметке остались двойные проценты"
open(S + "ballhsk-info.html", "w", encoding="utf-8").write(info)

print("ok | уровней:", len(EXAMS), "| цена аудирования:",
      [PRICE[l]["аудирование"] for l in range(1, 7)],
      "| два раздела:", EX_TWO, "| добрать:", EX_NEED)
