# -*- coding: utf-8 -*-
S = "/tmp/claude-0/-home-user-Kitai-Shool/a463bfca-82a9-56fd-ae09-42a7257ff999/scratchpad/"

FONTS = ("<link href=\"https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,600;0,700;1,600"
         "&family=Inter:wght@400;500;600;700&family=Noto+Serif+SC:wght@600;700&display=swap\" rel=\"stylesheet\">")
VARS = (":root{--brick:#A41E3A;--brick-d:#841630;--brick-soft:#F7E6EB;--ink:#2C2420;--ink-2:#5A4F45;"
        "--taupe:#8B7D6B;--cream:#FAF7F2;--cream-2:#F3EDE3;--hair:#EAE3D8;--surface:#fff;"
        "--green:#1E7A46;--green-soft:#E3F6E9;--amber:#C08A2E;--amber-s:#FBF2DF;--blue:#2F5D8C;--blue-s:#E7EEF6}")

# ------------------------------------------------------------------ обложка: 3 → 17
hero = """<!DOCTYPE html><html lang="ru"><head><meta charset="utf-8">
FONTS
<style>
VARS
*{margin:0;box-sizing:border-box}html,body{width:1200px;height:630px}
.card{width:1200px;height:630px;background:radial-gradient(1100px 700px at 78PCT 20PCT, #fff 0PCT, var(--cream) 56PCT, var(--cream-2) 100PCT);display:flex;align-items:center;padding:0 60px 0 76px;position:relative;overflow:hidden;font-family:'Inter',sans-serif}
.card:before{content:"";position:absolute;left:0;top:0;bottom:0;width:12px;background:var(--brick)}
.seal{position:absolute;right:40px;top:26px;width:92px;height:92px;border:2.5px solid var(--brick);border-radius:14px;display:flex;align-items:center;justify-content:center;color:var(--brick);font-family:'Noto Serif SC',serif;font-weight:700;font-size:36px;opacity:.9}
.txt{flex:0 0 392px;max-width:392px}
.eyebrow{color:var(--brick);font-weight:700;font-size:19px;letter-spacing:.19em;text-transform:uppercase;margin-bottom:14px}
h1{font-family:'Cormorant Garamond',serif;font-weight:600;font-size:52px;line-height:1.04;color:var(--ink);letter-spacing:-.5px}
h1 i{font-style:italic;color:var(--brick)}
.sub{font-size:18.5px;color:var(--ink-2);line-height:1.42;max-width:22ch;margin-top:18px}
.brand{position:absolute;left:76px;bottom:34px;display:flex;align-items:center;gap:12px;color:var(--ink)}
.brand b{font-family:'Cormorant Garamond',serif;font-weight:700;font-size:28px}.brand .bdot{width:11px;height:11px;border-radius:50PCT;background:var(--brick)}.brand span{color:var(--taupe);font-size:17px}

.art{flex:1 1 auto;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:22px}
.range{display:flex;align-items:baseline;gap:20px;font-family:'Cormorant Garamond',serif;color:var(--ink);line-height:1}
.range .n{font-size:132px;font-weight:700}
.range .n.b{color:var(--brick)}
.range .ar{font-size:64px;color:var(--taupe);font-family:'Inter',sans-serif;font-weight:400;position:relative;top:-14px}
.range .un{font-size:34px;color:var(--taupe);font-weight:600;margin-left:4px}
.marks{display:flex;gap:12px}
.mk{background:var(--surface);border:1px solid var(--hair);border-radius:14px;padding:11px 17px 13px;box-shadow:0 5px 16px rgba(44,36,32,.07);text-align:center;min-width:150px}
.mk b{display:block;font-family:'Cormorant Garamond',serif;font-size:21px;font-weight:700;color:var(--ink);line-height:1.1}
.mk span{display:block;font-size:12.5px;color:var(--taupe);margin-top:4px;line-height:1.25}
.mk.c1{border-color:var(--green)}.mk.c1 b{color:var(--green)}
.mk.c2{border-color:var(--amber)}.mk.c2 b{color:var(--amber)}
.mk.c3{border-color:var(--brick)}.mk.c3 b{color:var(--brick)}
</style></head><body>
<div class="card"><div class="seal">儿童</div>
<div class="txt">
  <div class="eyebrow">Детям</div>
  <h1>Китайский <i>для детей</i></h1>
  <div class="sub">Не один курс, а маршрут длиной больше десяти лет</div>
</div>
<div class="art">
  <div class="range"><span class="n">3</span><span class="ar">&rarr;</span><span class="n b">17</span><span class="un">лет</span></div>
  <div class="marks">
    <div class="mk c1"><b>Игра</b><span>слух, песни, первые фразы</span></div>
    <div class="mk c2"><b>Экзамен</b><span>YCT, потом HSK</span></div>
    <div class="mk c3"><b>Поступление</b><span>ЕГЭ и олимпиады</span></div>
  </div>
</div>
<div class="brand"><span class="bdot"></span><b>Kitai School</b><span>&middot; kitai-school.ru</span></div></div>
</body></html>"""
hero = hero.replace("FONTS", FONTS).replace("VARS", VARS).replace("PCT", "%")
open(S + "det-hero.html", "w", encoding="utf-8").write(hero)

# ------------------------------------------------------------------ инфографика: кривая интереса
# точки кривой: (возраст, уровень интереса 0..100)
CURVE = [(3, 78), (5, 88), (6.5, 84), (7.5, 40), (9, 72), (11, 66),
         (12, 34), (13.5, 70), (14.5, 64), (15.5, 30), (16.5, 68), (17, 76)]
X0, X1 = 3.0, 17.0
W, H = 700.0, 300.0
def px(a): return (a - X0) / (X1 - X0) * W
def py(v): return H - (v - 25.0) / 67.0 * (H - 60) - 22

pts = [(px(a), py(v)) for a, v in CURVE]
d = "M %.1f %.1f " % pts[0]
for i in range(1, len(pts)):
    x0, y0 = pts[i - 1]; x1, y1 = pts[i]
    d += "C %.1f %.1f, %.1f %.1f, %.1f %.1f " % (x0 + (x1 - x0) * .45, y0, x1 - (x1 - x0) * .45, y1, x1, y1)

DIPS = [(7.5, 40, "1"), (12, 34, "2"), (15.5, 30, "3")]
dips_svg = "".join(
    '<line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f" stroke="#A41E3A" stroke-width="1.6" stroke-dasharray="4 5" opacity=".55"/>'
    '<circle cx="%.1f" cy="%.1f" r="16" fill="#A41E3A"/>'
    '<text x="%.1f" y="%.1f" text-anchor="middle" font-family="Cormorant Garamond,serif" font-size="19" font-weight="700" fill="#fff">%s</text>'
    % (px(a), py(v), px(a), H, px(a), py(v), px(a), py(v) + 6.5, n) for a, v, n in DIPS)

ticks = "".join(
    '<text x="%.1f" y="%.1f" text-anchor="middle" font-family="Inter,sans-serif" font-size="14" fill="#8B7D6B">%d</text>'
    % (px(a), H + 22, a) for a in (3, 6, 9, 12, 15, 17))

CARDS = [
    ("1", "около 7 лет", "Появились иероглифы", "было весело и на слух — стало трудно и в тетради",
     "разбирать знак на части, а не прописывать по сто раз"),
    ("2", "около 11–12 лет", "Плато", "слов уже много, а говорить всё ещё не получается",
     "живая задача: переписка, ролевая игра, YCT как цель"),
    ("3", "около 15 лет", "Другие предметы", "«зачем мне китайский, когда впереди профильные экзамены»",
     "перевести язык в инструмент: ЕГЭ, олимпиада, поступление"),
]
cards = "".join(
    '<div class="cd"><div class="hd"><span class="nn">%s</span><div><b>%s</b><span class="age">%s</span></div></div>'
    '<div class="what">%s</div><div class="fix"><span>Что помогает</span>%s</div></div>'
    % (n, title, age, what, fix) for n, age, title, what, fix in CARDS)

info = """<!DOCTYPE html><html lang="ru"><head><meta charset="utf-8">
FONTS
<style>
VARS
*{margin:0;box-sizing:border-box}html,body{width:1200px;height:HGTpx}
.wrap{width:1200px;height:HGTpx;background:var(--cream);position:relative;overflow:hidden;font-family:'Inter',sans-serif;padding:20px 58px 16px 72px}
.wrap:before{content:"";position:absolute;left:0;top:0;bottom:0;width:14px;background:var(--brick)}
.top{display:flex;align-items:flex-end;justify-content:space-between;gap:24px}
.eyebrow{color:var(--brick);font-weight:700;font-size:16px;letter-spacing:.2em;text-transform:uppercase;margin-bottom:5px}
h2{font-family:'Cormorant Garamond',serif;font-weight:700;font-size:37px;color:var(--ink);line-height:1.02;letter-spacing:-.5px}
h2 i{font-style:italic;color:var(--brick)}
.hint{flex:0 0 300px;font-size:13.5px;color:var(--ink-2);line-height:1.34;border-left:3px solid var(--brick);padding-left:14px}
.hint b{color:var(--brick)}

.chart{margin-top:14px;background:#fff;border:1px solid var(--hair);border-radius:20px;padding:16px 26px 10px;box-shadow:0 5px 16px rgba(44,36,32,.06);position:relative}
.chart .yl{position:absolute;left:14px;top:50PCT;transform:translateY(-50PCT) rotate(-90deg);font-size:11.5px;font-weight:700;letter-spacing:.13em;text-transform:uppercase;color:var(--taupe);white-space:nowrap}
.chart .xl{text-align:center;font-size:11.5px;font-weight:700;letter-spacing:.13em;text-transform:uppercase;color:var(--taupe);margin-top:2px}
svg{display:block;margin:0 auto}

.cards{display:flex;gap:14px;margin-top:14px}
.cd{flex:1 1 0;background:#fff;border:1px solid var(--hair);border-radius:16px;padding:13px 18px 15px;box-shadow:0 4px 14px rgba(44,36,32,.05)}
.cd .hd{display:flex;align-items:flex-start;gap:11px}
.cd .nn{flex:0 0 28px;height:28px;border-radius:50PCT;background:var(--brick);color:#fff;font-family:'Cormorant Garamond',serif;font-weight:700;font-size:17px;display:flex;align-items:center;justify-content:center}
.cd .hd b{display:block;font-family:'Cormorant Garamond',serif;font-size:21px;font-weight:700;color:var(--ink);line-height:1.1}
.cd .age{display:block;font-size:12.5px;color:var(--taupe);margin-top:2px}
.cd .what{font-size:13.5px;color:var(--ink-2);line-height:1.34;margin-top:9px}
.cd .fix{margin-top:10px;padding-top:9px;border-top:1px solid var(--hair);font-size:13.5px;color:var(--ink);line-height:1.32}
.cd .fix span{display:block;font-size:11px;font-weight:700;letter-spacing:.13em;text-transform:uppercase;color:var(--green);margin-bottom:3px}

.foot{margin-top:14px;display:flex;align-items:center;gap:16px}
.foot .msg{flex:1 1 auto;background:var(--green-soft);border:1px solid var(--green);border-radius:14px;padding:11px 20px;font-size:15.5px;color:var(--ink);line-height:1.34}
.foot .msg b{color:var(--green)}
.brand{display:flex;align-items:center;gap:10px;color:var(--ink);flex:0 0 auto}
.brand b{font-family:'Cormorant Garamond',serif;font-weight:700;font-size:23px}.brand .dot{width:9px;height:9px;border-radius:50PCT;background:var(--brick)}.brand span{color:var(--taupe);font-size:15px}
</style></head><body>
<div class="wrap">
  <div class="top">
    <div>
      <div class="eyebrow">Где дети бросают китайский</div>
      <h2>Три провала, <i>и все три предсказуемы</i></h2>
    </div>
    <div class="hint">Интерес падает не из-за характера ребёнка, а в <b>одних и тех же местах</b>. Если знать заранее, каждое проходят спокойно.</div>
  </div>

  <div class="chart">
    <div class="yl">Интерес</div>
    <svg width="820" height="352" viewBox="0 0 700 340">
      <line x1="0" y1="300" x2="700" y2="300" stroke="#EAE3D8" stroke-width="1.5"/>
      <path d="DPATH" fill="none" stroke="#2F5D8C" stroke-width="3.4" stroke-linecap="round"/>
      DIPS
      TICKS
    </svg>
    <div class="xl">Возраст, лет</div>
  </div>

  <div class="cards">CARDS</div>

  <div class="foot">
    <div class="msg">После каждого провала интерес возвращается <b>выше прежнего</b> — если провал прошли, а не переждали</div>
    <div class="brand"><span class="dot"></span><b>Kitai School</b><span>&middot; kitai-school.ru</span></div>
  </div>
</div>
</body></html>"""
info = (info.replace("FONTS", FONTS).replace("VARS", VARS).replace("PCT", "%")
            .replace("HGTpx", "790px").replace("DPATH", d.strip())
            .replace("DIPS", dips_svg).replace("TICKS", ticks).replace("CARDS", cards))
open(S + "det-info.html", "w", encoding="utf-8").write(info)
print("ok")
