# -*- coding: utf-8 -*-
# Картинки к статье «Сколько иероглифов в китайском „алфавите“»
# Обложка     — карточка «вопрос — ответ»
# Инфографика — лестница словарей по эпохам
S = ("/tmp/claude-0/-home-user-Kitai-Shool/a463bfca-82a9-56fd-ae09-42a7257ff999/"
     "scratchpad/")

FONTS = ("<link href=\"https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,600;0,700;1,600"
         "&family=Inter:wght@400;500;600;700&family=Noto+Serif+SC:wght@600;700&display=swap\" rel=\"stylesheet\">")
VARS = (":root{--brick:#A41E3A;--brick-d:#841630;--brick-soft:#F7E6EB;--ink:#2C2420;--ink-2:#5A4F45;"
        "--taupe:#8B7D6B;--cream:#FAF7F2;--cream-2:#F3EDE3;--hair:#EAE3D8;--surface:#fff;"
        "--paper:#FFFDF8;--good:#2F6F4F;--good-soft:#E8F3EC;--step:#B8456040}")

# ─────────── данные: словари по эпохам ───────────
# (знак словаря, чтение, год, число знаков, подпись)
BOOKS = [
    ("说文解字", "Шовэнь цзецзы", 100, 9353, "первый разбор знаков по составу"),
    ("康熙字典", "Словарь Канси", 1716, 47035, "свод, собранный по указу императора"),
    ("中华字海", "Чжунхуа цзыхай", 1994, 85568, "самый полный современный свод"),
    ("異體字字典", "Словарь вариантов", 2004, 106230, "знаки вместе с вариантами написания"),
]
UNICODE = 97680     # ханьских знаков в Юникоде 16.0
READING = 3000      # сколько примерно нужно для чтения

# ── проверки данных
assert len(BOOKS) == 4, "словарей должно быть четыре"
years = [b[2] for b in BOOKS]
counts = [b[3] for b in BOOKS]
assert years == sorted(years), "годы должны идти по возрастанию"
assert counts == sorted(counts), "число знаков должно расти вместе с годами"
assert READING < min(counts), "отметка «для чтения» должна быть ниже самой низкой ступени"
assert counts[-1] > UNICODE > counts[-2], "кодировка лежит между двумя последними сводами"
TOP = counts[-1]


def ru(n):
    s, out = "%d" % n, ""
    while len(s) > 3:
        out = " " + s[-3:] + out
        s = s[:-3]
    return s + out


# ─────────── обложка: карточка «вопрос — ответ» ───────────
hero = """<!DOCTYPE html><html lang="ru"><head><meta charset="utf-8">
%(fonts)s
<style>
%(vars)s
*{margin:0;box-sizing:border-box}html,body{width:1200px;height:630px}
.card{width:1200px;height:630px;background:radial-gradient(1020px 680px at 12%% 8%%, #fff 0%%, var(--cream) 50%%, var(--cream-2) 100%%);position:relative;overflow:hidden;font-family:'Inter',sans-serif;padding:52px 48px 0 72px;display:flex;justify-content:space-between}
.card:before{content:"";position:absolute;left:0;top:0;bottom:0;width:12px;background:var(--brick)}
.txt{flex:0 0 470px;padding-top:10px}
.eyebrow{color:var(--brick);font-weight:700;font-size:18px;letter-spacing:.19em;text-transform:uppercase;margin-bottom:14px}
h1{font-family:'Cormorant Garamond',serif;font-weight:600;font-size:44px;line-height:1.06;color:var(--ink);letter-spacing:-.4px}
h1 i{font-style:italic;color:var(--brick)}
.sub{font-size:18px;color:var(--ink-2);line-height:1.42;max-width:30ch;margin-top:17px}
.tip{display:inline-block;margin-top:22px;background:var(--surface);border:1px solid var(--hair);border-left:4px solid var(--brick);border-radius:13px;padding:14px 20px;font-size:15.5px;color:var(--ink-2);line-height:1.38;max-width:33ch}
.tip b{color:var(--ink)}

.scene{flex:0 0 536px;display:flex;flex-direction:column;align-items:center;padding-top:14px}
.qa{width:488px;background:var(--surface);border:1px solid var(--hair);border-radius:18px;box-shadow:0 16px 34px rgba(44,36,32,.15);overflow:hidden}
.q{background:var(--cream-2);padding:18px 24px;border-bottom:1px solid var(--hair)}
.q .lb{font-size:12px;font-weight:700;letter-spacing:.16em;text-transform:uppercase;color:var(--taupe)}
.q .tx{font-family:'Cormorant Garamond',serif;font-size:27px;font-weight:600;color:var(--ink);line-height:1.2;margin-top:7px}
.a{padding:18px 24px 20px}
.a .lb{font-size:12px;font-weight:700;letter-spacing:.16em;text-transform:uppercase;color:var(--brick)}
.a .one{font-size:19px;font-weight:700;color:var(--ink);line-height:1.3;margin-top:8px}
.a .two{font-size:16px;color:var(--ink-2);line-height:1.4;margin-top:9px}
.a .two b{color:var(--ink)}
.nums{display:flex;gap:10px;margin-top:16px}
.nm{flex:1 1 0;background:var(--cream);border:1px solid var(--hair);border-radius:11px;padding:10px 8px;text-align:center}
.nm .v{font-family:'Cormorant Garamond',serif;font-weight:700;font-size:23px;color:var(--brick);line-height:1}
.nm .c{font-size:11.5px;color:var(--ink-2);line-height:1.26;margin-top:5px}
.under{margin-top:16px;text-align:center;font-size:15px;color:var(--ink-2);line-height:1.4;max-width:42ch}
.under b{color:var(--ink)}
.brand{position:absolute;left:72px;bottom:26px;display:flex;align-items:center;gap:11px;color:var(--ink)}
.brand b{font-family:'Cormorant Garamond',serif;font-weight:700;font-size:26px}
.brand .bdot{width:10px;height:10px;border-radius:50%%;background:var(--brick)}
.brand span{color:var(--taupe);font-size:16px}
</style></head><body>
<div class="card">
  <div class="txt">
    <div class="eyebrow">Письменность</div>
    <h1>Сколько иероглифов <i>в китайском «алфавите»</i></h1>
    <div class="sub">Ответ зависит от того, какой словарь открыть, — и это не уход от вопроса.</div>
    <div class="tip"><b>Алфавита у китайского нет.</b> Есть знаки, и их число в разных сводах отличается более чем в десять раз.</div>
    <div class="brand"><span class="bdot"></span><b>Kitai School</b><span>&middot; kitai-school.ru</span></div>
  </div>

  <div class="scene">
    <div class="qa">
      <div class="q">
        <div class="lb">Вопрос</div>
        <div class="tx">Сколько иероглифов в китайском алфавите?</div>
      </div>
      <div class="a">
        <div class="lb">Ответ</div>
        <div class="one">Алфавита нет, а точного числа знаков не существует.</div>
        <div class="two">Своды разных эпох насчитывают <b>от девяти тысяч до ста тысяч</b> — и каждый по-своему прав.</div>
        <div class="nums">
          <div class="nm"><div class="v">%(a)s</div><div class="c">в своде<br>100 года</div></div>
          <div class="nm"><div class="v">%(b)s</div><div class="c">в словаре<br>1716 года</div></div>
          <div class="nm"><div class="v">%(c)s</div><div class="c">в своде<br>2004 года</div></div>
        </div>
      </div>
    </div>
    <div class="under">Для чтения при этом хватает <b>около трёх тысяч</b></div>
  </div>
</div>
</body></html>""" % dict(fonts=FONTS, vars=VARS,
                          a=ru(counts[0]), b=ru(counts[1]), c=ru(counts[3]))

open(S + "alf-hero.html", "w", encoding="utf-8").write(hero)

# ─────────── инфографика: лестница по эпохам ───────────
HMAX = 318   # высота самой высокой ступени
HMIN = 56    # высота самой низкой, чтобы подпись помещалась
steps = "".join(
    '<div class="st"><div class="num">%s</div>'
    '<div class="col" style="height:%.1fpx"><span class="zh">%s</span></div>'
    '<div class="yr">%s</div><div class="nm">%s</div><div class="dsc">%s</div></div>'
    % (ru(cnt), HMIN + (HMAX - HMIN) * (cnt - counts[0]) / float(TOP - counts[0]),
       zh, ("%d год" % yr) if yr > 1000 else ("около %d года" % yr), ru_name, dsc)
    for zh, ru_name, yr, cnt, dsc in BOOKS)

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
.hint{flex:0 0 396px;background:var(--surface);border:1px solid var(--hair);border-left:4px solid var(--brick);border-radius:13px;padding:12px 18px;font-size:15px;color:var(--ink-2);line-height:1.36}
.hint b{color:var(--ink)}

.stage{display:flex;gap:22px;align-items:flex-end}
.steps{flex:1 1 auto;display:grid;grid-template-columns:repeat(4,1fr);gap:16px;align-items:end}
.st{display:flex;flex-direction:column;align-items:center}
.num{font-family:'Cormorant Garamond',serif;font-weight:700;font-size:28px;color:var(--ink);line-height:1;margin-bottom:8px;white-space:nowrap}
.col{width:100%%;border-radius:10px 10px 0 0;background:linear-gradient(180deg,var(--brick) 0%%,var(--brick-d) 100%%);display:flex;align-items:center;justify-content:center}
.zh{font-family:'Noto Serif SC',serif;font-weight:700;font-size:25px;color:#FFF0F3;letter-spacing:1px}
.yr{font-size:13px;color:var(--taupe);margin-top:10px}
.nm{font-size:15px;font-weight:700;color:var(--ink);margin-top:3px;text-align:center}
.dsc{font-size:12.5px;color:var(--ink-2);margin-top:4px;text-align:center;line-height:1.3;padding:0 4px}

.side{flex:0 0 250px;display:flex;flex-direction:column;gap:12px;margin-bottom:62px}
.box{background:var(--surface);border:1px solid var(--hair);border-radius:13px;padding:13px 16px}
.box .lb{font-size:11.5px;font-weight:700;letter-spacing:.13em;text-transform:uppercase;color:var(--taupe)}
.box .v{font-family:'Cormorant Garamond',serif;font-weight:700;font-size:30px;color:var(--brick);line-height:1;margin-top:6px}
.box .c{font-size:12.5px;color:var(--ink-2);line-height:1.3;margin-top:6px}
.box.green{background:var(--good-soft);border-color:#BFD9C9}
.box.green .v{color:var(--good)}

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
      <div class="eyebrow">Своды разных эпох</div>
      <h2>Чем позже словарь, <i>тем больше в нём знаков</i></h2>
    </div>
    <div class="hint">Своды считают <b>не одно и то же</b>: поздние включают древние, диалектные и вышедшие из употребления знаки вместе с вариантами написания.</div>
  </div>

  <div class="stage">
    <div class="steps">%(steps)s</div>
    <div class="side">
      <div class="box"><div class="lb">В компьютере</div><div class="v">%(uni)s</div>
        <div class="c">ханьских знаков закодировано в Юникоде 16.0</div></div>
      <div class="box green"><div class="lb">Для чтения</div><div class="v">около %(rd)s</div>
        <div class="c">столько знаков покрывает основную массу текста</div></div>
    </div>
  </div>

  <div class="foot">
    <div class="msg">Цифры <b>расходятся и внутри одного свода</b>: для словаря 1716 года встречаются и 47 035, и 46 933 — зависит от того, что считать отдельным знаком</div>
    <div class="brand"><span class="dot2"></span><b>Kitai School</b><span>&middot; kitai-school.ru</span></div>
  </div>
</div>
</body></html>""" % dict(fonts=FONTS, vars=VARS, h=742, steps=steps,
                          uni=ru(UNICODE), rd=ru(READING))

open(S + "alf-info.html", "w", encoding="utf-8").write(info)

print("ok | словарей:", len(BOOKS), "| ряд:", [ru(c) for c in counts])
print("кодировка:", ru(UNICODE), "| для чтения: около", ru(READING))
