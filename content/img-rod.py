# -*- coding: utf-8 -*-
# Картинки к статье «Родственники на китайском»
# Обложка     — дерево родства: от «я» вверх расходятся две линии, отцовская и материнская
# Инфографика — зеркальная таблица с центральной осью: один признак, два набора слов
S = ("/tmp/claude-0/-home-user-Kitai-Shool/a463bfca-82a9-56fd-ae09-42a7257ff999/"
     "scratchpad/")

FONTS = ("<link href=\"https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,600;0,700;1,600"
         "&family=Inter:wght@400;500;600;700&family=Noto+Serif+SC:wght@600;700&display=swap\" rel=\"stylesheet\">")
VARS = (":root{--brick:#A41E3A;--brick-d:#841630;--brick-soft:#F7E6EB;--ink:#2C2420;--ink-2:#5A4F45;"
        "--taupe:#8B7D6B;--cream:#FAF7F2;--cream-2:#F3EDE3;--hair:#EAE3D8;--surface:#fff;"
        "--pat:#39597F;--pat-soft:#E8EEF5;--mat:#8A6A3B;--mat-soft:#F5ECDC}")

# ─────────────────────────── данные обложки ───────────────────────────
# (иероглифы, пиньинь, кем является)
PAT_GP = [("爷爷", "yéye", "отец отца"), ("奶奶", "nǎinai", "мать отца")]
MAT_GP = [("外公", "wàigōng", "отец матери"), ("外婆", "wàipó", "мать матери")]

# геометрия дерева считается от чисел, а не набрана руками
GW = 238          # ширина группы прародителей
GAP = 82          # зазор между группами
BOXW = GW * 2 + GAP            # 558
LX = GW // 2                   # центр левой группы
RX = GW + GAP + GW // 2        # центр правой группы
CX = BOXW // 2                 # центр кадра
GH = 106          # высота группы
PY = 190          # верх ряда родителей
PH = 58           # высота плашки родителя
BUS = PY + PH + 48             # высота горизонтальной перекладины
MY = BUS + 50                  # верх плашки «я»
MH = 78
BOXH = MY + MH + 4

assert LX < CX < RX, "центры групп стоят не по порядку"
assert BUS > PY + PH, "перекладина попала внутрь плашки родителя"


def chip(z, p, r, cls):
    return ('<div class="chip %s"><b>%s</b><i>%s</i><span>%s</span></div>'
            % (cls, z, p, r))


pat_chips = "".join(chip(z, p, r, "pat") for z, p, r in PAT_GP)
mat_chips = "".join(chip(z, p, r, "mat") for z, p, r in MAT_GP)

hero = """<!DOCTYPE html><html lang="ru"><head><meta charset="utf-8">
%(fonts)s
<style>
%(vars)s
*{margin:0;box-sizing:border-box}html,body{width:1200px;height:630px}
.card{width:1200px;height:630px;background:radial-gradient(1020px 680px at 12%% 8%%, #fff 0%%, var(--cream) 50%%, var(--cream-2) 100%%);position:relative;overflow:hidden;font-family:'Inter',sans-serif;padding:52px 40px 0 72px;display:flex;justify-content:space-between}
.card:before{content:"";position:absolute;left:0;top:0;bottom:0;width:12px;background:var(--brick)}
.txt{flex:0 0 468px;padding-top:12px}
.eyebrow{color:var(--brick);font-weight:700;font-size:18px;letter-spacing:.19em;text-transform:uppercase;margin-bottom:14px}
h1{font-family:'Cormorant Garamond',serif;font-weight:600;font-size:46px;line-height:1.06;color:var(--ink);letter-spacing:-.4px}
h1 i{font-style:italic;color:var(--brick)}
.sub{font-size:18px;color:var(--ink-2);line-height:1.42;max-width:31ch;margin-top:17px}
.tip{display:inline-block;margin-top:24px;background:var(--surface);border:1px solid var(--hair);border-left:4px solid var(--brick);border-radius:13px;padding:14px 20px;font-size:16px;color:var(--ink-2);line-height:1.38;max-width:33ch}
.tip b{color:var(--ink)}
.tip em{font-family:'Noto Serif SC',serif;font-style:normal;font-weight:700;color:var(--brick)}

.scene{flex:0 0 %(boxw)dpx;display:flex;flex-direction:column;align-items:center;margin-top:10px}
.tree{position:relative;width:%(boxw)dpx;height:%(boxh)dpx}
.cap{margin-top:24px;background:var(--brick-soft);border:1px solid var(--brick);border-radius:13px;padding:13px 20px;font-size:15.5px;color:var(--ink);line-height:1.38;text-align:center}
.cap b{color:var(--brick-d)}
.grp{position:absolute;top:0;width:%(gw)dpx}
.grp.l{left:0}
.grp.r{left:%(rl)dpx}
.glbl{font-size:13px;font-weight:700;letter-spacing:.12em;text-transform:uppercase;text-align:center;margin-bottom:7px}
.grp.l .glbl{color:var(--pat)}
.grp.r .glbl{color:var(--mat)}
.row{display:flex;gap:10px;justify-content:center}
.chip{width:113px;background:var(--surface);border:1px solid var(--hair);border-radius:12px;padding:9px 6px 10px;text-align:center;box-shadow:0 5px 12px rgba(44,36,32,.07)}
.chip b{display:block;font-family:'Noto Serif SC',serif;font-weight:700;font-size:28px;line-height:1.1;color:var(--ink)}
.chip i{display:block;font-style:normal;font-size:12.5px;color:var(--taupe);margin-top:2px}
.chip span{display:block;font-size:11.5px;color:var(--ink-2);margin-top:4px;line-height:1.2}
.chip.pat{border-top:3px solid var(--pat);background:linear-gradient(180deg,var(--pat-soft) 0%%,#fff 46%%)}
.chip.mat{border-top:3px solid var(--mat);background:linear-gradient(180deg,var(--mat-soft) 0%%,#fff 46%%)}
.chip.mat b em{font-style:normal;color:var(--brick)}

.pr{position:absolute;top:%(py)dpx;height:%(ph)dpx;width:132px;border-radius:11px;display:flex;align-items:center;justify-content:center;gap:10px;color:#fff}
.pr b{font-family:'Noto Serif SC',serif;font-weight:700;font-size:24px}
.pr span{font-size:13px;opacity:.92}
.pr.l{left:%(prl)dpx;background:var(--pat)}
.pr.r{left:%(prr)dpx;background:var(--mat)}

.me{position:absolute;top:%(my)dpx;left:%(mel)dpx;width:152px;height:%(mh)dpx;border-radius:13px;background:var(--brick);color:#fff;display:flex;flex-direction:column;align-items:center;justify-content:center;box-shadow:0 10px 20px rgba(164,30,58,.26)}
.me b{font-family:'Noto Serif SC',serif;font-weight:700;font-size:34px;line-height:1.05}
.me span{font-size:13.5px;opacity:.93;margin-top:2px}

.v{position:absolute;width:2px;background:var(--hair)}
.h{position:absolute;height:2px;background:var(--hair)}

.brand{position:absolute;left:72px;bottom:28px;display:flex;align-items:center;gap:11px;color:var(--ink)}
.brand b{font-family:'Cormorant Garamond',serif;font-weight:700;font-size:26px}
.brand .bdot{width:10px;height:10px;border-radius:50%%;background:var(--brick)}
.brand span{color:var(--taupe);font-size:16px}
</style></head><body>
<div class="card">
  <div class="txt">
    <div class="eyebrow">Система родства</div>
    <h1>Родственники на китайском: <i>два слова там, где у нас одно</i></h1>
    <div class="sub">«Дедушка» по отцу и «дедушка» по матери — разные слова, и перепутать их нельзя.</div>
    <div class="tip">Материнскую линию помечает знак <em>外</em> — <b>«внешний»</b>: 外公 буквально «внешний дедушка».</div>
    <div class="brand"><span class="bdot"></span><b>Kitai School</b><span>&middot; kitai-school.ru</span></div>
  </div>

  <div class="scene">
    <div class="tree">
      <div class="grp l"><div class="glbl">по отцу</div><div class="row">%(pat)s</div></div>
      <div class="grp r"><div class="glbl">по матери</div><div class="row">%(mat)s</div></div>

      <div class="v" style="left:%(lv)dpx;top:%(gh)dpx;height:%(drop1)dpx"></div>
      <div class="v" style="left:%(rv)dpx;top:%(gh)dpx;height:%(drop1)dpx"></div>

      <div class="pr l"><b>爸爸</b><span>отец</span></div>
      <div class="pr r"><b>妈妈</b><span>мать</span></div>

      <div class="v" style="left:%(lv)dpx;top:%(pbot)dpx;height:%(drop2)dpx"></div>
      <div class="v" style="left:%(rv)dpx;top:%(pbot)dpx;height:%(drop2)dpx"></div>
      <div class="h" style="left:%(lx)dpx;top:%(bus)dpx;width:%(busw)dpx"></div>
      <div class="v" style="left:%(cv)dpx;top:%(bus)dpx;height:%(drop3)dpx"></div>

      <div class="me"><b>我</b><span>я</span></div>
    </div>
    <div class="cap">Два дедушки и две бабушки — <b>четыре слова вместо двух:</b> линия родства меняет само слово, а не добавляет к нему уточнение</div>
  </div>
</div>
</body></html>""" % dict(
    fonts=FONTS, vars=VARS, pat=pat_chips,
    mat=mat_chips.replace("外", "<em>外</em>"),
    boxw=BOXW, boxh=BOXH, gw=GW, rl=GW + GAP, gh=GH,
    py=PY, ph=PH, prl=LX - 66, prr=RX - 66,
    my=MY, mh=MH, mel=CX - 76,
    lv=LX - 1, rv=RX - 1, cv=CX - 1,
    drop1=PY - GH, pbot=PY + PH, drop2=BUS - (PY + PH),
    lx=LX, bus=BUS, busw=RX - LX, drop3=MY - BUS)

open(S + "rod-hero.html", "w", encoding="utf-8").write(hero)

# ─────────────────────────── данные инфографики ───────────────────────────
# (поколение, слова отцовской стороны, слова другой стороны, оговорка)
ROWS = [
    ("Дедушки и бабушки",
     [("爷爷", "yéye", "отец отца"), ("奶奶", "nǎinai", "мать отца")],
     [("外公", "wàigōng", "отец матери"), ("外婆", "wàipó", "мать матери")],
     "На севере вместо 外公 и 外婆 чаще говорят 姥爷 и 姥姥."),
    ("Дяди и тёти",
     [("伯伯", "bóbo", "старший брат отца"), ("叔叔", "shūshu", "младший брат отца"),
      ("姑姑", "gūgu", "сестра отца")],
     [("舅舅", "jiùjiu", "брат матери"), ("姨", "yí", "сестра матери")],
     "У братьев отца различают старшинство, у братьев матери — нет."),
    ("Двоюродные",
     [("堂哥", "tánggē", "сын брата отца"), ("堂妹", "tángmèi", "дочь брата отца")],
     [("表哥", "biǎogō", "сын сестры отца"), ("表姐", "biǎojiě", "дочь сестры отца")],
     "Здесь делят не по линии, а по фамилии: 堂 — своя фамилия, 表 — чужая, и под 表 попадает вся материнская родня."),
]

SIB = [("哥哥", "gēge", "старший брат"), ("弟弟", "dìdi", "младший брат"),
       ("姐姐", "jiějie", "старшая сестра"), ("妹妹", "mèimei", "младшая сестра")]

INLAW = [("公公", "gōnggong", "отец мужа"), ("婆婆", "pópo", "мать мужа"),
         ("岳父", "yuèfù", "отец жены"), ("岳母", "yuèmǔ", "мать жены")]

# ── проверки данных
ALL = [t[0] for r in ROWS for t in r[1] + r[2]] + [t[0] for t in SIB] + [t[0] for t in INLAW]
assert len(ALL) == len(set(ALL)), "один и тот же термин попал в картинку дважды"
assert len(ROWS) == 3, "поколений должно быть три"
for g, a, b, n in ROWS:
    assert a and b and n, "в строке %s пусто" % g
for z, p, r in [t for row in ROWS for t in row[1] + row[2]] + SIB + INLAW:
    assert z and p and r, "у термина %s не хватает части" % z
# материнскую сторону в первых двух поколениях помечает 外 или своё слово
assert all("外" in z for z, p, r in ROWS[0][2]), "в первом поколении потерялся знак 外"
MARK = sum(1 for z in ALL if "外" in z)
assert MARK == 2, "знак 外 ожидался ровно в двух терминах, найдено %d" % MARK


def cell(items, side):
    return "".join(
        '<div class="tm %s"><b>%s</b><i>%s</i><span>%s</span></div>' % (side, z, p, r)
        for z, p, r in items)


rows = "".join(
    '<div class="tr">'
    '<div class="side l">%s</div>'
    '<div class="axis"><span class="gen">%s</span><span class="note">%s</span></div>'
    '<div class="side r">%s</div>'
    '</div>' % (cell(a, "pat"), g, n, cell(b, "mat"))
    for g, a, b, n in ROWS)

sib = "".join('<div class="sm"><b>%s</b><i>%s</i><span>%s</span></div>' % t for t in SIB)
inlaw = "".join('<div class="sm il"><b>%s</b><i>%s</i><span>%s</span></div>' % t for t in INLAW)

info = """<!DOCTYPE html><html lang="ru"><head><meta charset="utf-8">
%(fonts)s
<style>
%(vars)s
*{margin:0;box-sizing:border-box}html,body{width:1200px;height:%(h)dpx}
.wrap{width:1200px;height:%(h)dpx;background:linear-gradient(180deg,#fff 0%%,var(--cream) 40%%,var(--cream-2) 100%%);font-family:'Inter',sans-serif;padding:38px 48px 30px;display:flex;flex-direction:column;position:relative;overflow:hidden}
.wrap:before{content:"";position:absolute;left:0;right:0;top:0;height:9px;background:var(--brick)}
.top{display:flex;align-items:flex-end;justify-content:space-between;gap:34px;margin-bottom:22px}
.eyebrow{color:var(--brick);font-weight:700;font-size:15.5px;letter-spacing:.19em;text-transform:uppercase;margin-bottom:8px}
h2{font-family:'Cormorant Garamond',serif;font-weight:600;font-size:37px;line-height:1.07;color:var(--ink);max-width:19ch}
h2 i{font-style:italic;color:var(--brick)}
.hint{flex:0 0 408px;background:var(--surface);border:1px solid var(--hair);border-left:4px solid var(--brick);border-radius:13px;padding:12px 18px;font-size:15px;color:var(--ink-2);line-height:1.36}
.hint b{color:var(--ink)}

.heads{display:grid;grid-template-columns:1fr 268px 1fr;gap:14px;margin-bottom:10px}
.hd{border-radius:11px;padding:9px 14px;font-size:15px;font-weight:700;letter-spacing:.04em;color:#fff;text-align:center}
.hd.l{background:var(--pat)}
.hd.r{background:var(--mat)}
.hd.c{font-family:'Cormorant Garamond',serif;font-weight:700;font-size:19px;color:var(--taupe);text-align:center;padding-top:11px;letter-spacing:0}

.tr{display:grid;grid-template-columns:1fr 268px 1fr;gap:14px;align-items:stretch;margin-bottom:12px}
.side{display:flex;gap:9px;align-items:stretch;border-radius:13px;padding:11px 12px}
.side.l{background:var(--pat-soft);justify-content:flex-end}
.side.r{background:var(--mat-soft)}
.tm{flex:0 0 auto;min-width:112px;background:var(--surface);border:1px solid var(--hair);border-radius:10px;padding:8px 9px 9px;text-align:center}
.tm b{display:block;font-family:'Noto Serif SC',serif;font-weight:700;font-size:24px;line-height:1.1;color:var(--ink)}
.tm i{display:block;font-style:normal;font-size:12px;color:var(--taupe);margin-top:1px}
.tm span{display:block;font-size:11.5px;color:var(--ink-2);margin-top:4px;line-height:1.22}
.tm.pat{border-bottom:3px solid var(--pat)}
.tm.mat{border-bottom:3px solid var(--mat)}
.axis{position:relative;display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center;padding:4px 10px}
.axis .gen{position:relative;background:var(--ink);color:#fff;border-radius:9px;padding:6px 14px;font-size:14.5px;font-weight:700;white-space:nowrap}
.axis .gen:before,.axis .gen:after{content:"";position:absolute;top:50%%;width:30px;height:1px;background:#D4C9B8}
.axis .gen:before{right:100%%;margin-right:7px}
.axis .gen:after{left:100%%;margin-left:7px}
.axis .note{position:relative;margin-top:7px;font-size:11.5px;color:var(--taupe);line-height:1.26}

.strip{display:flex;align-items:center;gap:16px;background:var(--surface);border:1px solid var(--hair);border-radius:14px;padding:12px 18px;margin-top:6px}
.strip .lb{flex:0 0 232px}
.strip .lb b{display:block;font-size:15px;color:var(--ink);font-weight:700}
.strip .lb span{display:block;font-size:12.5px;color:var(--taupe);line-height:1.3;margin-top:2px}
.strip .ln{flex:1 1 auto;display:flex;gap:9px}
.sm{flex:1 1 0;background:var(--cream);border:1px solid var(--hair);border-radius:10px;padding:7px 8px 8px;text-align:center}
.sm b{display:block;font-family:'Noto Serif SC',serif;font-weight:700;font-size:22px;line-height:1.1;color:var(--ink)}
.sm i{display:block;font-style:normal;font-size:11.5px;color:var(--taupe)}
.sm span{display:block;font-size:11.5px;color:var(--ink-2);margin-top:3px}
.sm.il b{color:var(--brick-d)}

.foot{margin-top:auto;display:flex;align-items:center;gap:18px;padding-top:16px}
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
      <div class="eyebrow">Ядро системы</div>
      <h2>Одна ступень родства — <i>и два набора слов</i></h2>
    </div>
    <div class="hint">Слово выбирают по трём признакам: <b>по какой линии родственник, старше или младше он вашего родителя и старше или младше вас самих.</b></div>
  </div>

  <div class="heads">
    <div class="hd l">Отцовская линия</div>
    <div class="hd c">признак различения</div>
    <div class="hd r">Материнская линия</div>
  </div>

  %(rows)s

  <div class="strip">
    <div class="lb"><b>Свои братья и сёстры</b><span>линия здесь ни при чём — различается только возраст</span></div>
    <div class="ln">%(sib)s</div>
  </div>

  <div class="strip">
    <div class="lb"><b>Родня супруга</b><span>у мужа и у жены свои слова для одной и той же роли</span></div>
    <div class="ln">%(inlaw)s</div>
  </div>

  <div class="foot">
    <div class="msg">Здесь только ядро системы: <b>полного списка терминов на одной картинке не бывает</b>, а север и юг Китая зовут одних и тех же родственников по-разному</div>
    <div class="brand"><span class="dot2"></span><b>Kitai School</b><span>&middot; kitai-school.ru</span></div>
  </div>
</div>
</body></html>""" % dict(fonts=FONTS, vars=VARS, h=872, rows=rows, sib=sib, inlaw=inlaw)

open(S + "rod-info.html", "w", encoding="utf-8").write(info)

print("ok | поколений:", len(ROWS),
      "| терминов всего:", len(ALL),
      "| знак 外 в:", MARK)
print("геометрия дерева: ширина", BOXW, "высота", BOXH,
      "| центры", LX, CX, RX, "| перекладина", BUS)
