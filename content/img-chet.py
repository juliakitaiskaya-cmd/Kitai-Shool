# -*- coding: utf-8 -*-
# Картинки к статье «В каких странах цифра 4 означает смерть»
# Обложка     — карточки стран: слова «четыре» и «смерть» с чтениями и сила поверья
# Инфографика — звуковые пары: насколько близки чтения в каждом языке
import sys
sys.path.insert(0, "/home/user/Kitai-Shool/content")
from chetyre import LANGS, STRENGTH, KOREA_F, JAPAN_49

S = ("/tmp/claude-0/-home-user-Kitai-Shool/a463bfca-82a9-56fd-ae09-42a7257ff999/"
     "scratchpad/")

FONTS = ("<link href=\"https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,600;0,700;1,600"
         "&family=Inter:wght@400;500;600;700&family=Noto+Serif+SC:wght@600;700&display=swap\" rel=\"stylesheet\">")
VARS = (":root{--brick:#A41E3A;--brick-d:#841630;--brick-soft:#F7E6EB;--ink:#2C2420;--ink-2:#5A4F45;"
        "--taupe:#8B7D6B;--cream:#FAF7F2;--cream-2:#F3EDE3;--hair:#EAE3D8;--surface:#fff;"
        "--paper:#FFFDF8;--good:#2F6F4F;--good-soft:#E8F3EC;--grey:#8A8178;--grey-soft:#EFEDE8}")

assert len(LANGS) == 4
LEVELS = {"сильное": 3, "заметное": 2, "умеренное": 2, "спорное": 1}
assert set(LEVELS) >= set(STRENGTH), "у каждой степени задана высота полосы"

# ─────────── обложка: карточки стран ───────────
cards = ""
for country, four, four_rd, death, death_rd, power, where, note in LANGS:
    bars = ""
    for i in range(3):
        on = " on" if i < LEVELS[power] else ""
        bars += '<i class="b%s"></i>' % on
    cards += ("""<div class="cc">
  <div class="cn">%(country)s</div>
  <div class="pair">
    <div class="w"><span class="zh">%(four)s</span><span class="rd">%(four_rd)s</span><span class="lb">четыре</span></div>
    <div class="eq">≈</div>
    <div class="w d"><span class="zh">%(death)s</span><span class="rd">%(death_rd)s</span><span class="lb">смерть</span></div>
  </div>
  <div class="where"><span class="wl">где заметнее</span><span class="wt">%(where)s</span>%(note)s</div>
  <div class="pw"><span class="pl">поверье</span><div class="bars">%(bars)s</div><span class="pv">%(power)s</span></div>
</div>""" % dict(country=country, four=four, four_rd=four_rd, death=death,
                 death_rd=death_rd, bars=bars, power=power, where=where,
                 note=('<span class="wn">%s</span>' % note) if note else ""))
assert cards.count('class="cc"') == 4

hero = """<!DOCTYPE html><html lang="ru"><head><meta charset="utf-8">
%(fonts)s
<style>
%(vars)s
*{margin:0;box-sizing:border-box}html,body{width:1200px;height:630px}
.card{width:1200px;height:630px;background:radial-gradient(1040px 700px at 12%% 4%%, #fff 0%%, var(--cream) 54%%, var(--cream-2) 100%%);position:relative;overflow:hidden;font-family:'Inter',sans-serif;padding:28px 56px 50px 72px;display:flex;flex-direction:column}
.card:before{content:"";position:absolute;left:0;top:0;bottom:0;width:12px;background:var(--brick)}
.head{display:flex;justify-content:space-between;align-items:flex-end;gap:34px;margin-bottom:18px}
.eyebrow{color:var(--brick);font-weight:700;font-size:18px;letter-spacing:.19em;text-transform:uppercase;margin-bottom:8px}
h1{font-family:'Cormorant Garamond',serif;font-weight:600;font-size:36px;line-height:1.07;color:var(--ink);letter-spacing:-.3px;max-width:22ch}
h1 i{font-style:italic;color:var(--brick)}
.tip{flex:0 0 324px;background:var(--surface);border:1px solid var(--hair);border-left:4px solid var(--brick);border-radius:13px;padding:12px 18px;font-size:14.5px;color:var(--ink-2);line-height:1.38}
.tip b{color:var(--ink)}

.cards{flex:1 1 auto;display:flex;gap:16px}
.cc{flex:1 1 0;background:var(--surface);border:1px solid var(--hair);border-radius:15px;padding:14px 16px 13px;display:flex;flex-direction:column}
.cn{font-size:18px;font-weight:700;color:var(--ink);padding-bottom:10px;border-bottom:1px solid var(--hair);margin-bottom:12px}
.pair{display:flex;align-items:center;gap:10px}
.w{flex:1 1 0;text-align:center;background:var(--grey-soft);border-radius:11px;padding:18px 6px}
.w.d{background:var(--brick-soft)}
.w .zh{display:block;font-family:'Noto Serif SC',serif;font-weight:700;font-size:38px;color:var(--ink);line-height:1.15}
.w.d .zh{color:var(--brick-d)}
.w .rd{display:block;font-size:14px;font-weight:600;color:var(--ink-2);margin-top:2px}
.w .lb{display:block;font-size:11.5px;color:var(--taupe);margin-top:4px}
.eq{flex:0 0 auto;font-size:20px;color:var(--taupe);font-weight:700}
.where{margin-top:14px;flex:1 1 auto;border-top:1px dashed var(--hair);padding-top:11px}
.where .wl{display:block;font-size:11px;letter-spacing:.1em;text-transform:uppercase;color:var(--taupe);margin-bottom:5px}
.where .wt{display:block;font-size:14.5px;color:var(--ink);line-height:1.34}
.where .wn{display:block;margin-top:7px;font-size:12.5px;color:var(--ink-2);line-height:1.32;background:var(--cream-2);border-radius:8px;padding:7px 9px}
.pw{margin-top:auto;padding-top:12px;display:flex;align-items:center;gap:9px}
.pl{font-size:11.5px;color:var(--taupe);flex:0 0 auto}
.bars{display:flex;gap:4px;flex:1 1 auto}
.bars .b{flex:1 1 0;height:9px;border-radius:3px;background:var(--grey-soft);display:block}
.bars .b.on{background:var(--brick)}
.pv{font-size:12.5px;font-weight:600;color:var(--brick);flex:0 0 auto}

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
      <div class="eyebrow">Культура</div>
      <h1>Цифра 4 и смерть: <i>одно созвучие на четыре страны</i></h1>
    </div>
    <div class="tip">Поверье держится на звучании слов, поэтому <b>оно переехало вместе с лексикой</b>, а не с границами.</div>
  </div>

  <div class="cards">%(cards)s</div>

  <div class="foot"><b>и подробности</b><span>в Японии неудачным считают ещё и число %(n49)s, а в корейских лифтах на месте четвёртого этажа ставят букву %(kf)s</span></div>

  <div class="brand"><span class="bdot"></span><b>Kitai School</b><span>&middot; kitai-school.ru</span></div>
</div>
</body></html>""" % dict(fonts=FONTS, vars=VARS, cards=cards, n49=JAPAN_49[0], kf=KOREA_F[0])

open(S + "chet-hero.html", "w", encoding="utf-8").write(hero)

# ─────────── инфографика: звуковые пары ───────────
rows = ""
for country, four, four_rd, death, death_rd, power, where, note in LANGS:
    same = four_rd == death_rd and not note
    if note:
        verdict = "близки, но источники расходятся"
    elif same:
        verdict = "совпадают полностью"
    else:
        verdict = "различаются тоном"
    cls = " full" if same else ""
    rows += ("""<div class="sr%(cls)s">
  <div class="sc">%(country)s</div>
  <div class="sw">%(four_rd)s</div>
  <div class="sm">%(verdict)s</div>
  <div class="sw d">%(death_rd)s</div>
  <div class="sn">%(where)s</div>
</div>""" % dict(cls=cls, country=country, four_rd=four_rd, death_rd=death_rd,
                 verdict=verdict, where=where))
assert rows.count('class="sr') == 4
FULL = rows.count('class="sr full"')
assert FULL == 2, "полное совпадение без оговорок — у японского и корейского"
assert rows.count("источники расходятся") == 1, "оговорка стоит у единственной спорной страны"

info = """<!DOCTYPE html><html lang="ru"><head><meta charset="utf-8">
%(fonts)s
<style>
%(vars)s
*{margin:0;box-sizing:border-box}html,body{width:1200px;height:%(h)dpx}
.wrap{width:1200px;height:%(h)dpx;background:linear-gradient(180deg,#fff 0%%,var(--cream) 44%%,var(--cream-2) 100%%);font-family:'Inter',sans-serif;padding:30px 48px 26px;display:flex;flex-direction:column;position:relative;overflow:hidden}
.wrap:before{content:"";position:absolute;left:0;right:0;top:0;height:9px;background:var(--brick)}
.top{display:flex;align-items:flex-end;justify-content:space-between;gap:34px;margin-bottom:18px}
.eyebrow{color:var(--brick);font-weight:700;font-size:15.5px;letter-spacing:.19em;text-transform:uppercase;margin-bottom:7px}
h2{font-family:'Cormorant Garamond',serif;font-weight:600;font-size:34px;line-height:1.08;color:var(--ink);max-width:24ch}
h2 i{font-style:italic;color:var(--brick)}
.hint{flex:0 0 350px;background:var(--surface);border:1px solid var(--hair);border-left:4px solid var(--brick);border-radius:13px;padding:11px 17px;font-size:14px;color:var(--ink-2);line-height:1.35}
.hint b{color:var(--ink)}

.rows{flex:1 1 auto;min-height:0;display:flex;flex-direction:column;gap:12px}
.sr{flex:1 1 0;background:var(--surface);border:1px solid var(--hair);border-radius:14px;display:flex;align-items:center;gap:16px;padding:12px 20px}
.sr.full{border-color:var(--brick);background:var(--brick-soft)}
.sc{flex:0 0 120px;font-size:17px;font-weight:700;color:var(--ink)}
.sw{flex:0 0 150px;text-align:center;background:var(--grey-soft);border-radius:10px;padding:10px 6px;font-size:22px;font-weight:700;color:var(--ink)}
.sw.d{background:#fff;border:1px solid var(--brick);color:var(--brick-d)}
.sr.full .sw{background:#fff;border:1px solid var(--hair)}
.sm{flex:0 0 215px;text-align:center;font-size:13.5px;color:var(--ink-2);line-height:1.3}
.sr.full .sm{color:var(--brick-d);font-weight:600}
.sn{flex:1 1 auto;font-size:13.5px;color:var(--ink-2);line-height:1.35;padding-left:6px}

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
      <div class="eyebrow">Звуковые пары</div>
      <h2>Чем ближе чтения, <i>тем крепче поверье</i></h2>
    </div>
    <div class="hint">Слева чтение слова «четыре», справа — слова «смерть». <b>В японском и корейском они совпадают полностью.</b></div>
  </div>

  <div class="rows">%(rows)s</div>

  <div class="foot">
    <div class="msg">Китайский здесь мягче остальных: <b>четвёрку и смерть различает только тон</b></div>
    <div class="brand"><span class="dot2"></span><b>Kitai School</b><span>&middot; kitai-school.ru</span></div>
  </div>
</div>
</body></html>""" % dict(fonts=FONTS, vars=VARS, h=620, rows=rows)

open(S + "chet-info.html", "w", encoding="utf-8").write(info)

print("ok | стран:", len(LANGS), "| полных совпадений:", FULL)
