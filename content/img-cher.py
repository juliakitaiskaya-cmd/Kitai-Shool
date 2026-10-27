# -*- coding: utf-8 -*-
# Картинки к статье «Порядок черт в китайских иероглифах»
# Обложка    — знак на полпути: 十, вторая черта показана пунктиром
# Инфографика — пошаговая сборка 国: восемь кадров, в каждом на черту больше
S = ("/tmp/claude-0/-home-user-Kitai-Shool/a463bfca-82a9-56fd-ae09-42a7257ff999/"
     "scratchpad/")

FONTS = ("<link href=\"https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,600;0,700;1,600"
         "&family=Inter:wght@400;500;600;700&family=Noto+Serif+SC:wght@600;700&display=swap\" rel=\"stylesheet\">")
VARS = (":root{--brick:#A41E3A;--brick-d:#841630;--brick-soft:#F7E6EB;--ink:#2C2420;--ink-2:#5A4F45;"
        "--taupe:#8B7D6B;--cream:#FAF7F2;--cream-2:#F3EDE3;--hair:#EAE3D8;--surface:#fff;"
        "--pencil:#3A332D;--ghost:#C6BCAE}")

hero = """<!DOCTYPE html><html lang="ru"><head><meta charset="utf-8">
%s
<style>
%s
*{margin:0;box-sizing:border-box}html,body{width:1200px;height:630px}
.card{width:1200px;height:630px;background:radial-gradient(1050px 660px at 14%% 12%%, #fff 0%%, var(--cream) 52%%, var(--cream-2) 100%%);position:relative;overflow:hidden;font-family:'Inter',sans-serif;padding:52px 46px 0 72px;display:flex;justify-content:space-between}
.card:before{content:"";position:absolute;left:0;top:0;bottom:0;width:12px;background:var(--brick)}
.txt{flex:0 0 496px;padding-top:6px}
.eyebrow{color:var(--brick);font-weight:700;font-size:18px;letter-spacing:.19em;text-transform:uppercase;margin-bottom:13px}
h1{font-family:'Cormorant Garamond',serif;font-weight:600;font-size:45px;line-height:1.07;color:var(--ink);letter-spacing:-.4px}
h1 i{font-style:italic;color:var(--brick)}
.sub{font-size:18px;color:var(--ink-2);line-height:1.42;max-width:31ch;margin-top:16px}
.tip{display:inline-block;margin-top:22px;background:var(--surface);border:1px solid var(--hair);border-left:4px solid var(--brick);border-radius:13px;padding:13px 19px;font-size:15.5px;color:var(--ink-2);line-height:1.36;max-width:35ch}
.tip b{color:var(--ink)}

/* знак на полпути */
.scene{flex:0 0 470px;padding-top:36px;display:flex;flex-direction:column;align-items:center}
.sheetp{position:relative;width:360px;height:360px;background:var(--surface);border:1px solid var(--hair);border-radius:18px;box-shadow:0 16px 30px rgba(44,36,32,.14)}
.hz{position:absolute;left:58px;top:168px;width:244px;height:15px;border-radius:8px;background:var(--pencil)}
.hz .n{position:absolute;left:-34px;top:-11px;width:26px;height:26px;border-radius:50%%;background:var(--pencil);color:#fff;font-size:14px;font-weight:700;display:flex;align-items:center;justify-content:center}
.vt{position:absolute;left:172px;top:52px;width:15px;height:258px;border-radius:8px;border:3px dashed var(--brick);background:var(--brick-soft)}
.vt .n{position:absolute;left:28px;top:-13px;width:26px;height:26px;border-radius:50%%;background:var(--brick);color:#fff;font-size:14px;font-weight:700;display:flex;align-items:center;justify-content:center}
.arw{position:absolute;left:172px;top:306px;width:0;height:0;border-left:13px solid transparent;border-right:13px solid transparent;border-top:20px solid var(--brick);transform:translateX(-5px)}
.cap{margin-top:22px;text-align:center;font-size:16.5px;color:var(--ink-2);line-height:1.4;max-width:42ch}
.cap b{color:var(--ink)}
.brand{position:absolute;left:72px;bottom:28px;display:flex;align-items:center;gap:11px;color:var(--ink)}
.brand b{font-family:'Cormorant Garamond',serif;font-weight:700;font-size:26px}
.brand .bdot{width:10px;height:10px;border-radius:50%%;background:var(--brick)}
.brand span{color:var(--taupe);font-size:16px}
</style></head><body>
<div class="card">
  <div class="txt">
    <div class="eyebrow">Иероглифика</div>
    <h1>Порядок черт <i>в китайских иероглифах</i></h1>
    <div class="sub">Знак пишется не как получится, а в заданной последовательности</div>
    <div class="tip"><b>Сначала горизонталь, потом вертикаль.</b> У 十 всего две черты — и порядок у них уже есть</div>
  </div>
  <div class="scene">
    <div class="sheetp">
      <div class="hz"><span class="n">1</span></div>
      <div class="vt"><span class="n">2</span></div>
      <div class="arw"></div>
    </div>
    <div class="cap">Написанное — сплошным, <b>следующее — пунктиром</b></div>
  </div>
  <div class="brand"><span class="bdot"></span><b>Kitai School</b><span>&middot; kitai-school.ru</span></div>
</div>
</body></html>""" % (FONTS, VARS)

open(S + "cher-hero.html", "w", encoding="utf-8").write(hero)

# --------------------------------------------------------------- инфографика
# Восемь шагов знака 国. Каждый шаг — набор уже написанных элементов.
# Элементы заданы как прямоугольники в координатах кадра 100x100.
PARTS = {
    "left":   (16, 14, 7, 72),      # левая вертикаль рамки
    "top":    (16, 14, 68, 7),      # верхняя горизонталь
    "right":  (77, 14, 7, 72),      # правая вертикаль рамки
    "w1":     (32, 32, 36, 6),      # верхняя горизонталь 王
    "wv":     (47, 32, 6, 30),      # вертикаль 王
    "w2":     (32, 56, 36, 6),      # средняя горизонталь
    "w3":     (30, 70, 40, 6),      # нижняя горизонталь 玉
    "dot":    (66, 60, 9, 9),       # точка 玉
    "bottom": (16, 79, 68, 7),      # нижняя закрывающая черта
}

STEPS = [
    (1, ["left"], "丨"),
    (2, ["left", "top", "right"], "𠃌"),
    (3, ["left", "top", "right", "w1"], "一"),
    (4, ["left", "top", "right", "w1", "wv"], "丨"),
    (5, ["left", "top", "right", "w1", "wv", "w2"], "一"),
    (6, ["left", "top", "right", "w1", "wv", "w2", "w3"], "一"),
    (7, ["left", "top", "right", "w1", "wv", "w2", "w3", "dot"], "丶"),
    (8, ["left", "top", "right", "w1", "wv", "w2", "w3", "dot", "bottom"], "一"),
]

assert len(STEPS) == 8, "шагов не восемь, а %d" % len(STEPS)
assert STEPS[-1][1][-1] == "bottom", "последней пишется не закрывающая черта"


def frame(no, parts, stroke, prev):
    inner = ""
    for key in PARTS:
        x, y, w, h = PARTS[key]
        fresh = key not in prev
        cls = "pc new" if fresh else "pc"
        if key in parts:
            if key == "dot":
                cls += " dt"
            inner += ('<i class="%s" style="left:%d%%;top:%d%%;width:%d%%;height:%d%%"></i>'
                      % (cls, x, y, w, h))
    return ('<div class="fr"><div class="no">%d</div><div class="box">%s</div>'
            '<div class="st">%s</div></div>' % (no, inner, stroke))


frames = "\n".join("      " + frame(no, parts, st, STEPS[i - 1][1] if i else [])
                   for i, (no, parts, st) in enumerate(STEPS))

RULES = [
    ("先外后内", "сначала внешнее, потом внутреннее", "шаги 1—2: рамка открывается первой"),
    ("先里头后封口", "внутреннее раньше закрывающей черты", "шаг 8: низ рамки — последний"),
]

rules = "".join(
    '<div class="rl"><div class="rh">%s</div><div class="rt">%s</div><div class="rw">%s</div></div>'
    % r for r in RULES)

info = """<!DOCTYPE html><html lang="ru"><head><meta charset="utf-8">
%(fonts)s
<style>
%(vars)s
*{margin:0;box-sizing:border-box}html,body{width:1200px;height:HGTpx}
.wrap{width:1200px;height:HGTpx;background:linear-gradient(180deg,#fff 0%%,var(--cream) 46%%,var(--cream-2) 100%%);font-family:'Inter',sans-serif;padding:32px 46px 28px;display:flex;flex-direction:column}
.top{display:flex;align-items:flex-end;justify-content:space-between;gap:30px;margin-bottom:22px}
.eyebrow{color:var(--brick);font-weight:700;font-size:14.5px;letter-spacing:.17em;text-transform:uppercase;margin-bottom:7px}
h2{font-family:'Cormorant Garamond',serif;font-weight:600;font-size:40px;line-height:1.07;color:var(--ink);letter-spacing:-.3px}
h2 i{font-style:italic;color:var(--brick)}
.hint{flex:0 0 376px;background:var(--surface);border:1px solid var(--hair);border-left:4px solid var(--brick);border-radius:12px;padding:12px 17px;font-size:14.5px;color:var(--ink-2);line-height:1.36}
.hint b{color:var(--ink)}

.frames{display:flex;gap:12px}
.fr{flex:1 1 0;background:var(--surface);border:1px solid var(--hair);border-radius:14px;padding:10px 10px 8px;box-shadow:0 4px 11px rgba(44,36,32,.05);text-align:center}
.no{font-size:12px;color:var(--taupe);font-weight:600;letter-spacing:.06em}
.box{position:relative;width:100%%;padding-top:100%%;margin-top:5px;background:var(--cream);border-radius:9px}
.pc{position:absolute;background:var(--ghost);border-radius:2px}
.pc.dt{border-radius:50%% 2px 50%% 50%%;transform:rotate(12deg)}
.pc.new{background:var(--brick);box-shadow:0 0 0 3px var(--brick-soft)}
.st{font-family:'Noto Serif SC',serif;font-size:19px;color:var(--ink);margin-top:6px;line-height:1.1}

.rules{display:flex;gap:14px;margin-top:20px}
.rl{flex:1 1 0;background:var(--surface);border:1px solid var(--hair);border-left:4px solid var(--brick);border-radius:13px;padding:12px 17px}
.rh{font-family:'Noto Serif SC',serif;font-size:21px;color:var(--brick-d)}
.rt{font-size:14.5px;color:var(--ink);margin-top:3px;font-weight:600}
.rw{font-size:13.5px;color:var(--ink-2);margin-top:2px}

.foot{margin-top:auto;display:flex;align-items:center;gap:18px;padding-top:18px}
.foot .msg{flex:1 1 auto;background:var(--brick-soft);border:1px solid var(--brick);border-radius:14px;padding:12px 21px;font-size:15px;color:var(--ink);line-height:1.34}
.foot .msg b{color:var(--brick)}
.brand{display:flex;align-items:center;gap:10px;color:var(--ink);flex:0 0 auto}
.brand b{font-family:'Cormorant Garamond',serif;font-weight:700;font-size:23px}
.brand .dot2{width:9px;height:9px;border-radius:50%%;background:var(--brick)}
.brand span{color:var(--taupe);font-size:15px}
</style></head><body>
<div class="wrap">
  <div class="top">
    <div>
      <div class="eyebrow">Сборка знака</div>
      <h2>国 за восемь шагов: <i>рамка закрывается последней</i></h2>
    </div>
    <div class="hint">Красным — черта, которая добавилась на этом шаге. <b>Нижняя черта рамки пишется в самом конце</b>, когда внутренняя часть уже на месте.</div>
  </div>

  <div class="frames">
%(frames)s
  </div>

  <div class="rules">%(rules)s</div>

  <div class="foot">
    <div class="msg">Порядок держится на правилах — <b>запоминать каждый знак отдельно не нужно</b></div>
    <div class="brand"><span class="dot2"></span><b>Kitai School</b><span>&middot; kitai-school.ru</span></div>
  </div>
</div>
</body></html>""" % dict(fonts=FONTS, vars=VARS, frames=frames, rules=rules)

info = info.replace("HGT", "545")
open(S + "cher-info.html", "w", encoding="utf-8").write(info)
print("ok, шагов:", len(STEPS), "| правил рядом:", len(RULES))
