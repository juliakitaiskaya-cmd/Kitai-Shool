# -*- coding: utf-8 -*-
# Картинки к статье «Сколько ключей в китайском языке»
# Обложка     — словарная карточка ключа № 85
# Инфографика — столбики: сколько ключей в каждой группе по числу черт
import sys
sys.path.insert(0, "/home/user/Kitai-Shool/content")
from radicals import RADICALS, COUNTS, MAXG

S = ("/tmp/claude-0/-home-user-Kitai-Shool/a463bfca-82a9-56fd-ae09-42a7257ff999/"
     "scratchpad/")

FONTS = ("<link href=\"https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,600;0,700;1,600"
         "&family=Inter:wght@400;500;600;700&family=Noto+Serif+SC:wght@600;700&display=swap\" rel=\"stylesheet\">")
VARS = (":root{--brick:#A41E3A;--brick-d:#841630;--brick-soft:#F7E6EB;--ink:#2C2420;--ink-2:#5A4F45;"
        "--taupe:#8B7D6B;--cream:#FAF7F2;--cream-2:#F3EDE3;--hair:#EAE3D8;--surface:#fff;"
        "--paper:#FFFDF8;--good:#2F6F4F;--good-soft:#E8F3EC}")

TOTAL = len(RADICALS)
assert TOTAL == 214, "ключей должно быть 214"
CARD = RADICALS[84]          # ключ № 85
assert CARD[0] == 85 and CARD[3] == "вода", "на обложке ключ № 85 «вода»"
BIGGEST = max(COUNTS, key=lambda x: x[1])
assert BIGGEST == (4, 34), "самая большая группа — четыре черты"
FIRST_SIX = [r for r in RADICALS if r[2] <= 2]
assert len(FIRST_SIX) == 29, "в группах на одну и две черты 29 ключей"
# шесть известных ключей для нижнего ряда обложки
SHOW = [RADICALS[n - 1] for n in (1, 9, 30, 61, 75, 140)]
assert [r[0] for r in SHOW] == [1, 9, 30, 61, 75, 140], "номера нижнего ряда сбились"
assert SHOW[-1][3] == "трава", "ключ 140 — трава"

# ─────────── обложка: словарная карточка ───────────
hero = """<!DOCTYPE html><html lang="ru"><head><meta charset="utf-8">
%(fonts)s
<style>
%(vars)s
*{margin:0;box-sizing:border-box}html,body{width:1200px;height:630px}
.card{width:1200px;height:630px;background:radial-gradient(1020px 680px at 12%% 8%%, #fff 0%%, var(--cream) 50%%, var(--cream-2) 100%%);position:relative;overflow:hidden;font-family:'Inter',sans-serif;padding:52px 48px 0 72px;display:flex;justify-content:space-between}
.card:before{content:"";position:absolute;left:0;top:0;bottom:0;width:12px;background:var(--brick)}
.txt{flex:0 0 500px;padding-top:10px}
.eyebrow{color:var(--brick);font-weight:700;font-size:18px;letter-spacing:.19em;text-transform:uppercase;margin-bottom:14px}
h1{font-family:'Cormorant Garamond',serif;font-weight:600;font-size:44px;line-height:1.06;color:var(--ink);letter-spacing:-.4px}
h1 i{font-style:italic;color:var(--brick)}
.sub{font-size:18px;color:var(--ink-2);line-height:1.42;max-width:31ch;margin-top:17px}
.tip{display:inline-block;margin-top:22px;background:var(--surface);border:1px solid var(--hair);border-left:4px solid var(--brick);border-radius:13px;padding:14px 20px;font-size:15.5px;color:var(--ink-2);line-height:1.38;max-width:34ch}
.tip b{color:var(--ink)}

.scene{flex:0 0 480px;display:flex;flex-direction:column;align-items:center;padding-top:6px}
.dict{width:404px;background:var(--paper);border:1px solid var(--hair);border-radius:16px;box-shadow:0 16px 32px rgba(44,36,32,.17);padding:24px 26px 22px;position:relative}
.dict:before{content:"";position:absolute;left:26px;right:26px;top:0;height:6px;background:var(--brick);border-radius:0 0 4px 4px}
.no{position:absolute;right:22px;top:20px;background:var(--brick);color:#fff;border-radius:10px;padding:6px 12px;font-size:15px;font-weight:700}
.zh{font-family:'Noto Serif SC',serif;font-weight:700;font-size:150px;line-height:1;color:var(--ink);text-align:center;margin-top:22px}
.meta{display:flex;gap:10px;margin-top:20px}
.mt{flex:1 1 0;background:var(--cream);border:1px solid var(--hair);border-radius:11px;padding:10px 8px;text-align:center}
.mt .k{font-size:11.5px;letter-spacing:.11em;text-transform:uppercase;color:var(--taupe);font-weight:700}
.mt .v{font-size:17px;font-weight:700;color:var(--ink);margin-top:4px}
.mini{display:flex;gap:9px;margin-top:18px}
.mn{flex:1 1 0;background:var(--surface);border:1px solid var(--hair);border-radius:10px;padding:8px 4px;text-align:center}
.mn b{display:block;font-family:'Noto Serif SC',serif;font-weight:700;font-size:28px;color:var(--ink);line-height:1}
.mn i{display:block;font-style:normal;font-size:11px;color:var(--taupe);margin-top:4px;white-space:nowrap}
.under{margin-top:16px;text-align:center;font-size:16px;color:var(--ink-2);line-height:1.4;max-width:36ch}
.under b{color:var(--ink)}
.brand{position:absolute;left:72px;bottom:26px;display:flex;align-items:center;gap:11px;color:var(--ink)}
.brand b{font-family:'Cormorant Garamond',serif;font-weight:700;font-size:26px}
.brand .bdot{width:10px;height:10px;border-radius:50%%;background:var(--brick)}
.brand span{color:var(--taupe);font-size:16px}
</style></head><body>
<div class="card">
  <div class="txt">
    <div class="eyebrow">Иероглифика</div>
    <h1>Сколько ключей в китайском языке: <i>все 214 в одной таблице</i></h1>
    <div class="sub">У каждого ключа есть номер и число черт — по ним и ищут знак в словаре.</div>
    <div class="tip"><b>Таблица ключей — это указатель</b>, а не список для заучивания: она отвечает на вопрос «как найти», а не «что значит».</div>
    <div class="brand"><span class="bdot"></span><b>Kitai School</b><span>&middot; kitai-school.ru</span></div>
  </div>

  <div class="scene">
    <div class="dict">
      <span class="no">№ %(num)d</span>
      <div class="zh">%(zh)s</div>
      <div class="meta">
        <div class="mt"><div class="k">Черт</div><div class="v">%(str)d</div></div>
        <div class="mt"><div class="k">Значение</div><div class="v">%(ru)s</div></div>
        <div class="mt"><div class="k">Всего</div><div class="v">%(total)d</div></div>
      </div>
    </div>
    <div class="mini">%(mini)s</div>
    <div class="under">Такая строка есть у <b>каждого из %(total)d ключей</b></div>
  </div>
</div>
</body></html>""" % dict(fonts=FONTS, vars=VARS, num=CARD[0], zh=CARD[1], str=CARD[2],
                          ru=CARD[3], total=TOTAL,
                          mini="".join(
                              '<span class="mn"><b>%s</b><i>№ %d</i></span>' % (r[1], r[0])
                              for r in SHOW))

open(S + "kly-hero.html", "w", encoding="utf-8").write(hero)

# ─────────── инфографика: столбики по числу черт ───────────
HMAX = 250
bars = "".join(
    '<div class="bg"><div class="cnt">%d</div>'
    '<div class="bar" style="height:%.1fpx"></div><div class="st">%d</div></div>'
    % (n, max(10.0, HMAX * n / float(MAXG)), strokes)
    for strokes, n in COUNTS)

# примеры из самой большой группы
SAMPLE = [r for r in RADICALS if r[2] == BIGGEST[0]][:8]
assert len(SAMPLE) == 8, "нужно восемь примеров"
sample = "".join('<span class="sm"><b>%s</b><i>%s</i></span>' % (r[1], r[3]) for r in SAMPLE)

info = """<!DOCTYPE html><html lang="ru"><head><meta charset="utf-8">
%(fonts)s
<style>
%(vars)s
*{margin:0;box-sizing:border-box}html,body{width:1200px;height:%(h)dpx}
.wrap{width:1200px;height:%(h)dpx;background:linear-gradient(180deg,#fff 0%%,var(--cream) 40%%,var(--cream-2) 100%%);font-family:'Inter',sans-serif;padding:38px 48px 30px;display:flex;flex-direction:column;position:relative;overflow:hidden}
.wrap:before{content:"";position:absolute;left:0;right:0;top:0;height:9px;background:var(--brick)}
.top{display:flex;align-items:flex-end;justify-content:space-between;gap:34px;margin-bottom:26px}
.eyebrow{color:var(--brick);font-weight:700;font-size:15.5px;letter-spacing:.19em;text-transform:uppercase;margin-bottom:8px}
h2{font-family:'Cormorant Garamond',serif;font-weight:600;font-size:38px;line-height:1.07;color:var(--ink);max-width:21ch}
h2 i{font-style:italic;color:var(--brick)}
.hint{flex:0 0 404px;background:var(--surface);border:1px solid var(--hair);border-left:4px solid var(--brick);border-radius:13px;padding:12px 18px;font-size:15px;color:var(--ink-2);line-height:1.36}
.hint b{color:var(--ink)}

.chart{display:flex;align-items:flex-end;gap:8px;padding-left:4px}
.bg{flex:1 1 0;display:flex;flex-direction:column;align-items:center}
.cnt{font-family:'Cormorant Garamond',serif;font-weight:700;font-size:19px;color:var(--ink);line-height:1;margin-bottom:6px}
.bar{width:100%%;border-radius:7px 7px 0 0;background:linear-gradient(180deg,var(--brick) 0%%,var(--brick-d) 100%%)}
.st{font-size:13px;color:var(--taupe);margin-top:8px}
.axis{margin-top:6px;font-size:13.5px;color:var(--ink-2);text-align:center}

.sample{margin-top:24px;background:var(--surface);border:1px solid var(--hair);border-radius:14px;padding:14px 18px}
.sample .lb{font-size:12.5px;font-weight:700;letter-spacing:.12em;text-transform:uppercase;color:var(--taupe)}
.row{display:flex;gap:12px;margin-top:10px}
.sm{flex:1 1 0;text-align:center;background:var(--cream);border:1px solid var(--hair);border-radius:10px;padding:9px 4px}
.sm b{display:block;font-family:'Noto Serif SC',serif;font-weight:700;font-size:30px;color:var(--ink);line-height:1}
.sm i{display:block;font-style:normal;font-size:12px;color:var(--ink-2);margin-top:5px}

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
      <div class="eyebrow">214 ключей</div>
      <h2>Ключи разложены <i>по числу черт</i></h2>
    </div>
    <div class="hint">Столбик — это группа ключей с одинаковым числом черт. <b>Чем больше черт, тем меньше ключей</b>: в конце списка их по одному.</div>
  </div>

  <div class="chart">%(bars)s</div>
  <div class="axis">число черт в ключе — от одной до двадцати трёх</div>

  <div class="sample">
    <div class="lb">Из самой большой группы — четыре черты, %(big)d ключа</div>
    <div class="row">%(sample)s</div>
  </div>

  <div class="foot">
    <div class="msg">Порядок и номера — <b>по классическому списку словаря Канси</b>; тот же порядок закреплён в стандарте Юникода</div>
    <div class="brand"><span class="dot2"></span><b>Kitai School</b><span>&middot; kitai-school.ru</span></div>
  </div>
</div>
</body></html>""" % dict(fonts=FONTS, vars=VARS, h=744, bars=bars, sample=sample,
                          big=BIGGEST[1])

open(S + "kly-info.html", "w", encoding="utf-8").write(info)

print("ok | ключей:", TOTAL, "| групп:", len(COUNTS), "| самая большая:", BIGGEST)
print("на обложке:", CARD)
