# -*- coding: utf-8 -*-
# Картинки к статье «Проходные баллы HSK»
# Обложка     — столбик из трёх разделов и черта порога на 180
# Инфографика — две структуры теста и общий порог в 60 % от суммы
S = ("/tmp/claude-0/-home-user-Kitai-Shool/a463bfca-82a9-56fd-ae09-42a7257ff999/"
     "scratchpad/")

FONTS = ("<link href=\"https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,600;0,700;1,600"
         "&family=Inter:wght@400;500;600;700&family=Noto+Serif+SC:wght@600;700&display=swap\" rel=\"stylesheet\">")
VARS = (":root{--brick:#A41E3A;--brick-d:#841630;--brick-soft:#F7E6EB;--ink:#2C2420;--ink-2:#5A4F45;"
        "--taupe:#8B7D6B;--cream:#FAF7F2;--cream-2:#F3EDE3;--hair:#EAE3D8;--surface:#fff;"
        "--sky:#39597F;--sky-soft:#E7EDF4;--good:#1E7A46;--good-soft:#E8F3EC;"
        "--s1:#B9C7D8;--s2:#9FB3C9;--s3:#8098B4}")

# разделы HSK 3–6, снизу вверх
PART = [("Аудирование", 100, "s1"), ("Чтение", 100, "s2"), ("Письмо", 100, "s3")]
TOTAL = sum(p[1] for p in PART)
PASS = 180
assert TOTAL == 300, "сумма разделов не 300"
assert PASS * 100 // TOTAL == 60, "порог не равен 60 %% от суммы"

BARH = 420  # высота столбика в пикселях
seg = "".join(
    '<div class="sg %s" style="height:%dpx"><span>%s</span><b>%d</b></div>'
    % (cls, BARH * val // TOTAL, name, val) for name, val, cls in reversed(PART))

hero = """<!DOCTYPE html><html lang="ru"><head><meta charset="utf-8">
%(fonts)s
<style>
%(vars)s
*{margin:0;box-sizing:border-box}html,body{width:1200px;height:630px}
.card{width:1200px;height:630px;background:radial-gradient(1050px 660px at 14%% 10%%, #fff 0%%, var(--cream) 52%%, var(--cream-2) 100%%);position:relative;overflow:hidden;font-family:'Inter',sans-serif;padding:66px 56px 0 72px;display:flex;justify-content:space-between}
.card:before{content:"";position:absolute;left:0;top:0;bottom:0;width:12px;background:var(--brick)}
.txt{flex:0 0 468px;padding-top:4px}
.eyebrow{color:var(--brick);font-weight:700;font-size:18px;letter-spacing:.19em;text-transform:uppercase;margin-bottom:13px}
h1{font-family:'Cormorant Garamond',serif;font-weight:600;font-size:45px;line-height:1.07;color:var(--ink);letter-spacing:-.4px}
h1 i{font-style:italic;color:var(--brick)}
.sub{font-size:18px;color:var(--ink-2);line-height:1.42;max-width:30ch;margin-top:16px}
.tip{display:inline-block;margin-top:22px;background:var(--surface);border:1px solid var(--hair);border-left:4px solid var(--brick);border-radius:13px;padding:13px 19px;font-size:15.5px;color:var(--ink-2);line-height:1.36;max-width:34ch}
.tip b{color:var(--ink)}
.warn{display:inline-block;margin-top:14px;font-size:14px;color:var(--taupe);line-height:1.4;max-width:36ch}

.scene{flex:0 0 480px;display:flex;flex-direction:column;align-items:center;padding-top:4px}
.barwrap{position:relative;width:470px;padding-left:54px}
.bar{width:196px;height:%(barh)dpx;display:flex;flex-direction:column;border-radius:12px;overflow:hidden;box-shadow:0 12px 24px rgba(44,36,32,.16)}
.sg{display:flex;align-items:center;justify-content:space-between;gap:8px;padding:0 13px;color:#fff}
.sg span{font-size:13.5px;letter-spacing:-.01em}
.sg b{font-size:18px}
.sg.s1{background:var(--s1);color:#2C3A4A}
.sg.s2{background:var(--s2);color:#22303F}
.sg.s3{background:var(--s3)}
.line{position:absolute;left:44px;width:216px;border-top:3px dashed var(--brick)}
.lbl{position:absolute;left:268px;transform:translateY(-50%%);background:var(--brick);color:#fff;border-radius:9px;padding:6px 12px;font-size:15px;font-weight:700;white-space:nowrap}
.tot{position:absolute;left:44px;transform:translate(-100%%,-50%%);font-size:15px;color:var(--taupe);white-space:nowrap;padding-right:9px}
.cap{margin-top:20px;text-align:center;font-size:16.5px;color:var(--ink-2);line-height:1.42;max-width:38ch}
.cap b{color:var(--ink)}
.brand{position:absolute;left:72px;bottom:28px;display:flex;align-items:center;gap:11px;color:var(--ink)}
.brand b{font-family:'Cormorant Garamond',serif;font-weight:700;font-size:26px}
.brand .bdot{width:10px;height:10px;border-radius:50%%;background:var(--brick)}
.brand span{color:var(--taupe);font-size:16px}
</style></head><body>
<div class="card">
  <div class="txt">
    <div class="eyebrow">Экзамены</div>
    <h1>Проходные баллы <i>HSK</i></h1>
    <div class="sub">На HSK 3–6 это 180 из 300 — и считается по сумме, а не по разделам</div>
    <div class="tip"><b>Провалить один раздел и всё равно сдать — можно.</b> Отдельного порога по разделам нет</div>
    <div class="warn">Экзамен переходит на новый стандарт HSK 3.0: перед регистрацией цифры стоит сверить в своём центре.</div>
  </div>
  <div class="scene">
    <div class="barwrap">
      <div class="bar">%(seg)s</div>
      <div class="tot" style="top:0">300</div>
      <div class="line" style="top:%(pass)dpx"></div>
      <div class="lbl" style="top:%(pass)dpx">180 — порог</div>
      <div class="tot" style="top:%(barh)dpx">0</div>
    </div>
    <div class="cap">Три раздела по сто баллов, <b>а зачёт идёт от общей суммы</b></div>
  </div>
  <div class="brand"><span class="bdot"></span><b>Kitai School</b><span>&middot; kitai-school.ru</span></div>
</div>
</body></html>""" % dict(fonts=FONTS, vars=VARS, seg=seg, barh=BARH,
                         pass_=0, **{"pass": BARH - BARH * PASS // TOTAL})

open(S + "ball-hero.html", "w", encoding="utf-8").write(hero)

# --------------------------------------------------------------- инфографика
GROUP = [
    ("HSK 1 и HSK 2", ["Аудирование", "Чтение"], 200, 120, "две части по 100"),
    ("HSK 3 — HSK 6", ["Аудирование", "Чтение", "Письмо"], 300, 180, "три части по 100"),
]

for g in GROUP:
    assert g[2] == len(g[1]) * 100, "сумма не складывается из разделов: %s" % g[0]
    assert g[3] * 100 // g[2] == 60, "порог не 60 %% от суммы: %s" % g[0]

groups = "".join(
    '<div class="gc"><div class="gh">%s</div><div class="gs">%s</div>'
    '<div class="parts">%s</div>'
    '<div class="scale"><div class="fill" style="width:%d%%"></div>'
    '<div class="mark" style="left:%d%%"></div></div>'
    '<div class="nums"><span>0</span><span class="p">%d — порог</span>'
    '<span>%d</span></div></div>'
    % (name, note,
       "".join('<span class="pt">%s</span>' % p for p in parts),
       60, 60, pas, tot)
    for name, parts, tot, pas, note in GROUP)

LEVELS = [("HSK 1", 200, 120), ("HSK 2", 200, 120), ("HSK 3", 300, 180),
          ("HSK 4", 300, 180), ("HSK 5", 300, 180), ("HSK 6", 300, 180)]

assert len(LEVELS) == 6, "уровней не шесть"

levels = "".join(
    '<div class="lv"><div class="ln">%s</div><div class="lp">%d</div>'
    '<div class="lt">из %d</div></div>' % (n, p, t) for n, t, p in LEVELS)

info = """<!DOCTYPE html><html lang="ru"><head><meta charset="utf-8">
%(fonts)s
<style>
%(vars)s
*{margin:0;box-sizing:border-box}html,body{width:1200px;height:548px}
.wrap{width:1200px;height:548px;background:linear-gradient(180deg,#fff 0%%,var(--cream) 46%%,var(--cream-2) 100%%);font-family:'Inter',sans-serif;padding:30px 46px 26px;display:flex;flex-direction:column}
.top{display:flex;align-items:flex-end;justify-content:space-between;gap:30px;margin-bottom:18px}
.eyebrow{color:var(--brick);font-weight:700;font-size:14.5px;letter-spacing:.17em;text-transform:uppercase;margin-bottom:7px}
h2{font-family:'Cormorant Garamond',serif;font-weight:600;font-size:38px;line-height:1.07;color:var(--ink);letter-spacing:-.3px}
h2 i{font-style:italic;color:var(--brick)}
.hint{flex:0 0 392px;background:var(--surface);border:1px solid var(--hair);border-left:4px solid var(--brick);border-radius:12px;padding:12px 17px;font-size:14.5px;color:var(--ink-2);line-height:1.36}
.hint b{color:var(--ink)}

.groups{display:flex;gap:18px}
.gc{flex:1 1 0;background:var(--surface);border:1px solid var(--hair);border-radius:15px;padding:16px 20px 18px;box-shadow:0 4px 12px rgba(44,36,32,.05)}
.gh{font-family:'Cormorant Garamond',serif;font-weight:700;font-size:26px;color:var(--ink);line-height:1.1}
.gs{font-size:13.5px;color:var(--taupe);margin-top:2px}
.parts{display:flex;gap:7px;margin-top:11px}
.pt{flex:1 1 0;text-align:center;background:var(--sky-soft);color:var(--sky);border-radius:8px;padding:7px 4px;font-size:13px;font-weight:600}
.scale{position:relative;height:22px;background:var(--cream-2);border-radius:7px;margin-top:14px;overflow:hidden}
.fill{position:absolute;left:0;top:0;bottom:0;background:var(--brick-soft)}
.mark{position:absolute;top:-3px;bottom:-3px;width:3px;background:var(--brick)}
.nums{display:flex;justify-content:space-between;margin-top:6px;font-size:13px;color:var(--taupe)}
.nums .p{color:var(--brick);font-weight:700}

.sep{display:flex;align-items:center;gap:16px;margin:18px 0 12px}
.sep span{font-size:15px;font-weight:700;color:var(--brick-d);white-space:nowrap}
.sep i{flex:1 1 auto;height:1px;background:var(--hair)}
.levels{display:flex;gap:11px}
.lv{flex:1 1 0;background:var(--surface);border:1px solid var(--hair);border-radius:13px;padding:11px 6px 12px;text-align:center}
.ln{font-size:13.5px;color:var(--ink-2);font-weight:600}
.lp{font-family:'Cormorant Garamond',serif;font-weight:700;font-size:30px;color:var(--brick);line-height:1.05;margin-top:2px}
.lt{font-size:12.5px;color:var(--taupe)}

.foot{margin-top:auto;display:flex;align-items:center;gap:18px;padding-top:14px}
.foot .msg{flex:1 1 auto;background:var(--brick-soft);border:1px solid var(--brick);border-radius:14px;padding:11px 21px;font-size:15px;color:var(--ink);line-height:1.34}
.foot .msg b{color:var(--brick)}
.brand{display:flex;align-items:center;gap:10px;color:var(--ink);flex:0 0 auto}
.brand b{font-family:'Cormorant Garamond',serif;font-weight:700;font-size:23px}
.brand .dot2{width:9px;height:9px;border-radius:50%%;background:var(--brick)}
.brand span{color:var(--taupe);font-size:15px}
</style></head><body>
<div class="wrap">
  <div class="top">
    <div>
      <div class="eyebrow">Порог сдачи</div>
      <h2>Две структуры — <i>и один и тот же порог</i></h2>
    </div>
    <div class="hint">Число баллов разное, а доля одна: <b>сдать — значит набрать 60 %% от суммы.</b></div>
  </div>

  <div class="groups">%(groups)s</div>

  <div class="sep"><span>Сколько нужно на каждом уровне</span><i></i></div>
  <div class="levels">%(levels)s</div>

  <div class="foot">
    <div class="msg">Экзамен переходит на HSK 3.0 — <b>перед регистрацией цифры сверяйте в своём центре</b></div>
    <div class="brand"><span class="dot2"></span><b>Kitai School</b><span>&middot; kitai-school.ru</span></div>
  </div>
</div>
</body></html>""" % dict(fonts=FONTS, vars=VARS, groups=groups, levels=levels)

open(S + "ball-info.html", "w", encoding="utf-8").write(info)
print("ok | разделов:", len(PART), "| групп:", len(GROUP), "| уровней:", len(LEVELS))
print("порог везде 60 % от суммы — проверено ассертами")
