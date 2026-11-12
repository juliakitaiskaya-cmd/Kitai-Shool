# -*- coding: utf-8 -*-
# Картинки к статье «Как подготовить ребёнка к YCT 1»
# Обложка     — дорожка из двенадцати недель: три блока по четыре недели
# Инфографика — экзамен в числах: задания, время и шкала баллов
import sys
sys.path.insert(0, "/home/user/Kitai-Shool/content")
from yct1 import (PARTS, PLAN, WEEKS, TOTAL_TASKS, TOTAL_MINUTES, MAX_SCORE,
                  PASS_SCORE, SECTION_MAX, WORDS, WITH_TASKS)

S = ("/tmp/claude-0/-home-user-Kitai-Shool/a463bfca-82a9-56fd-ae09-42a7257ff999/"
     "scratchpad/")

FONTS = ("<link href=\"https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,600;0,700;1,600"
         "&family=Inter:wght@400;500;600;700&family=Noto+Serif+SC:wght@600;700&display=swap\" rel=\"stylesheet\">")
VARS = (":root{--brick:#A41E3A;--brick-d:#841630;--brick-soft:#F7E6EB;--ink:#2C2420;--ink-2:#5A4F45;"
        "--taupe:#8B7D6B;--cream:#FAF7F2;--cream-2:#F3EDE3;--hair:#EAE3D8;--surface:#fff;"
        "--grey-soft:#EFEDE8}")

assert len(PLAN) == 3 and WEEKS == list(range(1, 13))

# ─────────── обложка: дорожка недель ───────────
blocks = ""
for i, (block, weeks, task, ready, doing) in enumerate(PLAN, start=1):
    a, b = weeks.replace(" недели", "").split("–")
    dots = "".join('<i></i>' for _ in range(int(a), int(b) + 1))
    blocks += ("""<div class="bl">
  <div class="bhead"><span class="num">%(i)d</span><b>%(block)s</b><span class="wk">%(weeks)s недели</span></div>
  <div class="dots">%(dots)s</div>
  <div class="task">%(task)s</div>
  <ul class="doing">%(doing)s</ul>
  <div class="ready"><span>готов дальше, когда</span>%(ready)s</div>
</div>""" % dict(i=i, block=block, weeks=weeks.replace(" недели", ""),
                 dots=dots, task=task, ready=ready,
                 doing="".join("<li>%s</li>" % d for d in doing)))
assert blocks.count('class="bl"') == 3
assert blocks.count("<i></i>") == len(WEEKS) == 12

hero = """<!DOCTYPE html><html lang="ru"><head><meta charset="utf-8">
%(fonts)s
<style>
%(vars)s
*{margin:0;box-sizing:border-box}html,body{width:1200px;height:630px}
.card{width:1200px;height:630px;background:radial-gradient(1040px 700px at 10%% 4%%, #fff 0%%, var(--cream) 54%%, var(--cream-2) 100%%);position:relative;overflow:hidden;font-family:'Inter',sans-serif;padding:28px 56px 50px 72px;display:flex;flex-direction:column}
.card:before{content:"";position:absolute;left:0;top:0;bottom:0;width:12px;background:var(--brick)}
.head{display:flex;justify-content:space-between;align-items:flex-end;gap:34px;margin-bottom:18px}
.eyebrow{color:var(--brick);font-weight:700;font-size:18px;letter-spacing:.19em;text-transform:uppercase;margin-bottom:8px}
h1{font-family:'Cormorant Garamond',serif;font-weight:600;font-size:38px;line-height:1.07;color:var(--ink);letter-spacing:-.3px;max-width:30ch}
h1 i{font-style:italic;color:var(--brick)}
.tip{flex:0 0 322px;background:var(--surface);border:1px solid var(--hair);border-left:4px solid var(--brick);border-radius:13px;padding:12px 18px;font-size:14.5px;color:var(--ink-2);line-height:1.38}
.tip b{color:var(--ink)}

.track{position:relative;flex:1 1 auto;display:flex;gap:16px;padding-top:12px}
.track:before{content:"";position:absolute;left:24px;right:24px;top:0;height:3px;background:var(--hair);border-radius:2px}
.bl{flex:1 1 0;background:var(--surface);border:1px solid var(--hair);border-radius:15px;padding:14px 20px 14px;display:flex;flex-direction:column}
.bhead{display:flex;align-items:center;gap:10px}
.num{width:26px;height:26px;border-radius:50%%;background:var(--brick);color:#fff;font-size:14px;font-weight:700;display:flex;align-items:center;justify-content:center;flex:0 0 auto}
.bhead b{font-size:17px;color:var(--ink)}
.wk{margin-left:auto;font-size:13px;color:var(--taupe)}
.dots{display:flex;gap:6px;margin:13px 0 0}
.dots i{display:block;width:100%%;height:10px;border-radius:5px;background:var(--brick);opacity:.78}
.task{margin-top:14px;font-size:17px;font-weight:600;color:var(--brick-d);line-height:1.3}
.doing{list-style:none;margin:11px 0 0;padding:0}
.doing li{position:relative;padding-left:16px;font-size:14px;color:var(--ink-2);line-height:1.34;margin-bottom:5px}
.doing li:before{content:"";position:absolute;left:0;top:8px;width:6px;height:6px;border-radius:50%%;background:var(--brick);opacity:.55}
.ready{margin-top:auto;padding-top:13px;background:none;font-size:14px;color:var(--ink-2);line-height:1.35}
.ready span{display:block;font-size:10.5px;letter-spacing:.1em;text-transform:uppercase;color:var(--taupe);margin-bottom:4px}

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
      <div class="eyebrow">Экзамены для детей</div>
      <h1>Подготовка к YCT 1: <i>двенадцать недель, три задачи</i></h1>
    </div>
    <div class="tip">Двигаться дальше стоит по признаку готовности, <b>а не по календарю.</b></div>
  </div>

  <div class="track">%(blocks)s</div>

  <div class="foot"><b>моя раскладка</b><span>это рабочая схема занятий, а не чьё-то требование: ребёнок с опытом пройдёт её быстрее</span></div>

  <div class="brand"><span class="bdot"></span><b>Kitai School</b><span>&middot; kitai-school.ru</span></div>
</div>
</body></html>""" % dict(fonts=FONTS, vars=VARS, blocks=blocks)

assert "%%" not in hero, "в разметке остались двойные проценты"
open(S + "yct1-hero.html", "w", encoding="utf-8").write(hero)

# ─────────── инфографика: экзамен в числах ───────────
PCT = 100.0 * PASS_SCORE / MAX_SCORE
cells = ""
for name, n, mins, what in PARTS:
    if n:
        sq = "".join('<i></i>' for _ in range(n))
        cells += ('<div class="pt"><div class="phead"><b>%s</b><span>%d</span></div>'
                  '<div class="sq">%s</div><div class="pm">около %d мин</div></div>'
                  % (name, n, sq, mins))
    else:
        cells += ('<div class="pt none"><div class="phead"><b>%s</b></div>'
                  '<div class="pw">%s</div><div class="pm">около %d мин</div></div>'
                  % (name, what, mins))
assert cells.count('class="pt"') == 2 and cells.count('class="pt none"') == 1
assert cells.count("<i></i>") == sum(n for _, n, _, _ in PARTS) == TOTAL_TASKS

info = """<!DOCTYPE html><html lang="ru"><head><meta charset="utf-8">
%(fonts)s
<style>
%(vars)s
*{margin:0;box-sizing:border-box}html,body{width:1200px;height:%(h)dpx}
.wrap{width:1200px;height:%(h)dpx;background:linear-gradient(180deg,#fff 0%%,var(--cream) 46%%,var(--cream-2) 100%%);font-family:'Inter',sans-serif;padding:30px 48px 26px;display:flex;flex-direction:column;position:relative;overflow:hidden}
.wrap:before{content:"";position:absolute;left:0;right:0;top:0;height:9px;background:var(--brick)}
.top{display:flex;align-items:flex-end;justify-content:space-between;gap:34px;margin-bottom:20px}
.eyebrow{color:var(--brick);font-weight:700;font-size:15.5px;letter-spacing:.19em;text-transform:uppercase;margin-bottom:7px}
h2{font-family:'Cormorant Garamond',serif;font-weight:600;font-size:34px;line-height:1.08;color:var(--ink);max-width:22ch}
h2 i{font-style:italic;color:var(--brick)}
.hint0{flex:0 0 340px;background:var(--surface);border:1px solid var(--hair);border-left:4px solid var(--brick);border-radius:13px;padding:11px 17px;font-size:14px;color:var(--ink-2);line-height:1.35}
.hint0 b{color:var(--ink)}

.parts{display:flex;gap:16px;margin-bottom:16px}
.pt{flex:1 1 0;background:var(--surface);border:1px solid var(--hair);border-radius:15px;padding:13px 18px 12px}
.pt.none{background:var(--grey-soft);border-style:dashed}
.phead{display:flex;align-items:baseline;justify-content:space-between;padding-bottom:9px;border-bottom:1px solid var(--hair)}
.phead b{font-size:17px;color:var(--ink)}
.phead span{font-family:'Cormorant Garamond',serif;font-size:28px;color:var(--brick-d);line-height:1}
.sq{display:flex;flex-wrap:wrap;gap:5px;margin-top:11px}
.sq i{display:block;width:16px;height:16px;border-radius:4px;background:var(--brick);opacity:.82}
.pw{margin-top:11px;font-size:14px;color:var(--ink-2);line-height:1.35}
.pm{margin-top:11px;font-size:14px;font-weight:600;color:var(--taupe)}

.scorebox{flex:1 1 auto;background:var(--surface);border:1px solid var(--hair);border-radius:15px;padding:18px 24px 16px;display:flex;flex-direction:column;justify-content:center}
.sctitle{font-size:12.5px;letter-spacing:.11em;text-transform:uppercase;color:var(--taupe);margin-bottom:14px}
.scale{position:relative;height:50px}
.bar{position:absolute;left:0;right:0;top:0;height:16px;border-radius:8px;background:var(--grey-soft);overflow:hidden}
.fill{position:absolute;left:0;top:0;bottom:0;width:%(pct).4f%%;background:var(--brick-soft);border-right:3px solid var(--brick)}
.ends{position:absolute;left:0;right:0;top:22px;display:flex;justify-content:space-between;font-size:13.5px;font-weight:700;color:var(--ink)}
.pin{position:absolute;left:%(pct).4f%%;top:20px;transform:translateX(-50%%);text-align:center;white-space:nowrap}
.pin b{display:inline-block;background:var(--brick);color:#fff;font-size:13.5px;font-weight:700;border-radius:8px;padding:4px 12px}
.halves{display:flex;gap:14px;margin-top:16px}
.half{flex:1 1 0;background:var(--cream-2);border-radius:10px;padding:9px 14px;font-size:14px;color:var(--ink-2)}
.half b{color:var(--ink)}

.foot{margin-top:16px;flex:0 0 auto;display:flex;align-items:center;gap:18px}
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
      <div class="eyebrow">Экзамен в числах</div>
      <h2>%(tasks)d заданий <i>примерно за %(minutes)d минут</i></h2>
    </div>
    <div class="hint0">Один квадрат — одно задание. <b>Работа с бланком входит в экзаменационное время, а не идёт до него.</b></div>
  </div>

  <div class="parts">%(cells)s</div>

  <div class="scorebox">
    <div class="sctitle">баллы</div>
    <div class="scale">
      <div class="bar"><span class="fill"></span></div>
      <div class="ends"><span>0</span><span>%(max)d</span></div>
      <div class="pin"><b>%(pass)d — порог</b></div>
    </div>
    <div class="halves">
      <div class="half">аудирование — до <b>%(sect)d</b></div>
      <div class="half">чтение — до <b>%(sect)d</b></div>
      <div class="half">лексика ступени — около <b>%(words)d слов</b></div>
    </div>
  </div>

  <div class="foot">
    <div class="msg">Порог — чуть больше половины: <b>одна-две потерянные позиции результата не решают</b></div>
    <div class="brand"><span class="dot2"></span><b>Kitai School</b><span>&middot; kitai-school.ru</span></div>
  </div>
</div>
</body></html>""" % dict(fonts=FONTS, vars=VARS, h=575, cells=cells, pct=PCT,
                         tasks=TOTAL_TASKS, minutes=TOTAL_MINUTES, words=WORDS,
                         sect=SECTION_MAX, **{"max": MAX_SCORE, "pass": PASS_SCORE})

assert "%%" not in info, "в разметке остались двойные проценты"
open(S + "yct1-info.html", "w", encoding="utf-8").write(info)

print("ok | недель:", len(WEEKS), "| заданий:", TOTAL_TASKS, "| порог:", PASS_SCORE)
