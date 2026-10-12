# -*- coding: utf-8 -*-
# Картинки к статье «Как писать письмо на китайском»
# Обложка    — лист письма с загнутым углом: 见字如面
# Инфографика — клетчатый лист 稿纸: по клеткам видно, где начинается каждая часть
S = "/tmp/claude-0/-home-user-Kitai-Shool/a463bfca-82a9-56fd-ae09-42a7257ff999/scratchpad/"

FONTS = ("<link href=\"https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,600;0,700;1,600"
         "&family=Inter:wght@400;500;600;700&family=Noto+Serif+SC:wght@600;700&display=swap\" rel=\"stylesheet\">")
VARS = (":root{--brick:#A41E3A;--brick-d:#841630;--brick-soft:#F7E6EB;--ink:#2C2420;--ink-2:#5A4F45;"
        "--taupe:#8B7D6B;--cream:#FAF7F2;--cream-2:#F3EDE3;--hair:#EAE3D8;--surface:#fff;"
        "--green:#1E7A46;--green-soft:#E3F6E9;--amber:#C08A2E;--amber-s:#FBF2DF;--blue:#2F5D8C;--blue-s:#E7EEF6}")

# ------------------------------------------------------------------ обложка
hero = """<!DOCTYPE html><html lang="ru"><head><meta charset="utf-8">
%s
<style>
%s
*{margin:0;box-sizing:border-box}html,body{width:1200px;height:630px}
.card{width:1200px;height:630px;background:radial-gradient(1100px 680px at 16%% 8%%, #fff 0%%, var(--cream) 54%%, var(--cream-2) 100%%);position:relative;overflow:hidden;font-family:'Inter',sans-serif;display:flex;align-items:center;justify-content:space-between;padding:0 64px 0 72px}
.card:before{content:"";position:absolute;left:0;top:0;bottom:0;width:12px;background:var(--brick)}
.txt{flex:0 0 520px}
.eyebrow{color:var(--brick);font-weight:700;font-size:18px;letter-spacing:.19em;text-transform:uppercase;margin-bottom:12px}
h1{font-family:'Cormorant Garamond',serif;font-weight:600;font-size:52px;line-height:1.05;color:var(--ink);letter-spacing:-.5px;max-width:470px}
h1 i{font-style:italic;color:var(--brick)}
.sub{font-size:18.5px;color:var(--ink-2);line-height:1.42;max-width:31ch;margin-top:17px}
.counts{display:flex;gap:13px;margin-top:26px}
.cnt{background:var(--surface);border:1px solid var(--hair);border-radius:14px;padding:11px 16px;text-align:center;box-shadow:0 4px 14px rgba(44,36,32,.05)}
.cnt b{display:block;font-family:'Cormorant Garamond',serif;font-size:29px;font-weight:700;color:var(--brick);line-height:1.05}
.cnt span{font-size:12.5px;color:var(--taupe);letter-spacing:.04em}
.brand{position:absolute;left:72px;bottom:32px;display:flex;align-items:center;gap:11px;color:var(--ink)}
.brand b{font-family:'Cormorant Garamond',serif;font-weight:700;font-size:26px}
.brand .bdot{width:10px;height:10px;border-radius:50%%;background:var(--brick)}
.brand span{color:var(--taupe);font-size:16px}

/* лист с загнутым углом */
.sheetwrap{flex:0 0 404px;position:relative;filter:drop-shadow(0 16px 34px rgba(44,36,32,.16))}
.sheet{width:404px;height:446px;background:var(--surface);clip-path:polygon(0 0, calc(100%% - 72px) 0, 100%% 72px, 100%% 100%%, 0 100%%);padding:46px 38px 34px;display:flex;flex-direction:column;position:relative}
.fold{position:absolute;right:0;top:0;width:72px;height:72px;background:linear-gradient(225deg,var(--hair) 0%%,#D5CABB 100%%);clip-path:polygon(0 0, 100%% 100%%, 0 100%%)}
.rule{height:1px;background:var(--hair);margin:0 0 26px}
.big{font-family:'Noto Serif SC',serif;font-weight:700;font-size:62px;line-height:1.22;color:var(--ink);letter-spacing:.04em}
.tr{font-size:16px;color:var(--ink-2);line-height:1.45;margin-top:18px}
.tr b{color:var(--brick);font-weight:600}
.pin{font-size:15px;color:var(--taupe);letter-spacing:.09em;margin-top:9px}
.sig{margin-top:auto;text-align:right}
.sig .l{font-family:'Noto Serif SC',serif;font-weight:700;font-size:21px;color:var(--ink-2)}
.sig .d{font-size:14px;color:var(--taupe);margin-top:5px}
</style></head><body>
<div class="card">
  <div class="txt">
    <div class="eyebrow">Письмо</div>
    <h1>Как писать письмо <i>на китайском</i></h1>
    <div class="sub">Текст можно написать правильно и всё равно выдать себя тем, как он лежит на листе</div>
    <div class="counts">
      <div class="cnt"><b>6</b><span>ЧАСТЕЙ</span></div>
      <div class="cnt"><b>2</b><span>ЗНАКА ОТСТУПА</span></div>
      <div class="cnt"><b>в конце</b><span>ДАТА</span></div>
    </div>
  </div>
  <div class="sheetwrap">
    <div class="sheet">
      <div class="big">见字如面</div>
      <div class="tr"><b>«Увидеть эти строки</b> — всё равно что увидеть вас»</div>
      <div class="pin">jiàn zì rú miàn</div>
      <div class="sig"><div class="l">敬上</div><div class="d">с уважением</div></div>
    </div>
    <div class="fold"></div>
  </div>
  <div class="brand"><span class="bdot"></span><b>Kitai School</b><span>&middot; kitai-school.ru</span></div>
</div>
</body></html>""" % (FONTS, VARS)

open(S + "pis-hero.html", "w", encoding="utf-8").write(hero)

# -------------------------------------------------------------- инфографика
COLS = 12
# (знаки, отступ в клетках, выравнивание)  —  '' = пустая клетка
LINES = [
    ("亲爱的妈妈：", 0, "left",  "1"),
    ("您好！",       2, "left",  "2"),
    ("我在北京一切都好，", 2, "left", "3"),
    ("学习也很顺利。", 0, "left", ""),
    ("此致",         2, "left",  "4"),
    ("敬礼！",       0, "left",  ""),
    ("女儿小丽",     0, "right", "5"),
    ("十月十二日",   0, "right", "6"),
]

rows = []
for text, pad, align, badge in LINES:
    cells = []
    chars = list(text)
    if align == "right":
        lead = COLS - len(chars) - 1
        seq = [("", "e")] * lead + [(c, "f") for c in chars] + [("", "e")]
    else:
        seq = [("", "p")] * pad + [(c, "f") for c in chars]
        seq += [("", "e")] * (COLS - len(seq))
    for ch, kind in seq[:COLS]:
        cells.append('<span class="c %s">%s</span>' % (kind, ch))
    b = '<span class="bg">%s</span>' % badge if badge else '<span class="bg emptyb"></span>'
    rows.append('<div class="ln">%s<div class="cells">%s</div></div>' % (b, "".join(cells)))

grid = "\n".join(rows)

LEG = [
    ("1", "称呼", "обращение", "с первой клетки, заканчивается двоеточием"),
    ("2", "问候语", "приветствие", "с третьей клетки — отступ в два знака"),
    ("3", "正文", "основной текст", "каждый абзац тоже с третьей"),
    ("4", "祝颂语", "пожелание", "此致 с третьей, 敬礼 снова с первой"),
    ("5", "署名", "подпись", "справа внизу"),
    ("6", "日期", "дата", "под подписью, тоже справа"),
]
leg = "\n".join(
    '<div class="li"><span class="bg">%s</span><div><b class="han">%s</b> <span class="ru">%s</span>'
    '<div class="d">%s</div></div></div>' % (n, han, ru, d) for n, han, ru, d in LEG)

info = """<!DOCTYPE html><html lang="ru"><head><meta charset="utf-8">
%s
<style>
%s
*{margin:0;box-sizing:border-box}html,body{width:1200px;height:HGTpx}
.wrap{width:1200px;height:HGTpx;background:linear-gradient(180deg,#fff 0%%,var(--cream) 46%%,var(--cream-2) 100%%);font-family:'Inter',sans-serif;padding:32px 46px 26px;display:flex;flex-direction:column}
.top{display:flex;align-items:flex-end;justify-content:space-between;gap:30px;margin-bottom:22px}
.eyebrow{color:var(--brick);font-weight:700;font-size:14.5px;letter-spacing:.17em;text-transform:uppercase;margin-bottom:7px}
h2{font-family:'Cormorant Garamond',serif;font-weight:600;font-size:40px;line-height:1.07;color:var(--ink);letter-spacing:-.3px}
h2 i{font-style:italic;color:var(--brick)}
.hint{flex:0 0 352px;background:var(--surface);border:1px solid var(--hair);border-left:4px solid var(--brick);border-radius:12px;padding:12px 17px;font-size:14.5px;color:var(--ink-2);line-height:1.36}
.hint b{color:var(--ink)}

.main{display:flex;gap:34px;align-items:flex-start}

/* клетчатый лист */
.paper{flex:0 0 auto;background:var(--surface);border:1px solid var(--hair);border-radius:14px;padding:18px 20px;box-shadow:0 8px 24px rgba(44,36,32,.08)}
.ln{display:flex;align-items:center;gap:10px}
.bg{flex:0 0 22px;width:22px;height:22px;border-radius:50%%;background:var(--brick);color:#fff;font-size:12.5px;font-weight:700;display:flex;align-items:center;justify-content:center}
.bg.emptyb{background:transparent}
.cells{display:flex}
.c{width:42px;height:42px;border:1px solid #E2D9CC;margin:-0.5px 0 0 -0.5px;display:flex;align-items:center;justify-content:center;font-family:'Noto Serif SC',serif;font-weight:700;font-size:23px;color:var(--ink)}
.c.p{background:var(--brick-soft);border-color:#E7C9D2}
.c.e{background:#FDFCFA}

.leg{flex:1 1 auto;display:flex;flex-direction:column;gap:11px;padding-top:2px}
.li{display:flex;gap:11px;align-items:flex-start;background:var(--surface);border:1px solid var(--hair);border-radius:12px;padding:10px 14px}
.li .bg{margin-top:2px}
.li .han{font-family:'Noto Serif SC',serif;font-weight:700;font-size:18px;color:var(--ink)}
.li .ru{font-size:15px;color:var(--ink-2)}
.li .d{font-size:13.5px;color:var(--taupe);line-height:1.34;margin-top:2px}

.foot{margin-top:auto;display:flex;align-items:center;gap:18px;padding-top:18px}
.foot .msg{flex:1 1 auto;background:var(--brick-soft);border:1px solid var(--brick);border-radius:14px;padding:12px 21px;font-size:16px;color:var(--ink);line-height:1.34}
.foot .msg b{color:var(--brick)}
.brand{display:flex;align-items:center;gap:10px;color:var(--ink);flex:0 0 auto}
.brand b{font-family:'Cormorant Garamond',serif;font-weight:700;font-size:23px}
.brand .dot{width:9px;height:9px;border-radius:50%%;background:var(--brick)}
.brand span{color:var(--taupe);font-size:15px}
</style></head><body>
<div class="wrap">
  <div class="top">
    <div>
      <div class="eyebrow">Оформление</div>
      <h2>Где начинается каждая часть <i>письма</i></h2>
    </div>
    <div class="hint">Розовые клетки — <b>отступ</b>. Он не «на глаз»: ровно <b>два знака</b>, и на клетчатой бумаге это видно без линейки.</div>
  </div>

  <div class="main">
    <div class="paper">
%s
    </div>
    <div class="leg">
%s
    </div>
  </div>

  <div class="foot">
    <div class="msg">Обращение и <b>敬礼</b> идут от самого края. Отступ в две клетки — у первой строки каждого абзаца</div>
    <div class="brand"><span class="dot"></span><b>Kitai School</b><span>&middot; kitai-school.ru</span></div>
  </div>
</div>
</body></html>""" % (FONTS, VARS, grid, leg)

info = info.replace("HGT", "690")
open(S + "pis-info.html", "w", encoding="utf-8").write(info)
print("ok")
