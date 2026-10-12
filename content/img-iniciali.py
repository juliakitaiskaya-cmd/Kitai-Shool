# -*- coding: utf-8 -*-
# Картинки к статье «Инициали в китайском языке»
# Обложка    — карточка элемента: слог 好 разложен на инициаль, финаль и тон
# Инфографика — костяшки домино: какие пары складываются, а какие не бывают
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
.card{width:1200px;height:630px;background:radial-gradient(1100px 680px at 16%% 8%%, #fff 0%%, var(--cream) 54%%, var(--cream-2) 100%%);position:relative;overflow:hidden;font-family:'Inter',sans-serif;display:flex;align-items:center;padding:0 60px 0 72px}
.card:before{content:"";position:absolute;left:0;top:0;bottom:0;width:12px;background:var(--brick)}
.txt{flex:1 1 auto;max-width:600px}
.eyebrow{color:var(--brick);font-weight:700;font-size:18px;letter-spacing:.19em;text-transform:uppercase;margin-bottom:12px}
h1{font-family:'Cormorant Garamond',serif;font-weight:600;font-size:60px;line-height:1.02;color:var(--ink);letter-spacing:-.6px}
h1 i{font-style:italic;color:var(--brick)}
.sub{font-size:19px;color:var(--ink-2);line-height:1.42;max-width:30ch;margin-top:18px}
.counts{display:flex;gap:14px;margin-top:26px}
.cnt{background:var(--surface);border:1px solid var(--hair);border-radius:14px;padding:11px 18px;text-align:center;box-shadow:0 4px 14px rgba(44,36,32,.05)}
.cnt b{display:block;font-family:'Cormorant Garamond',serif;font-size:32px;font-weight:700;color:var(--brick);line-height:1}
.cnt span{font-size:13px;color:var(--taupe);letter-spacing:.04em}
.brand{position:absolute;left:72px;bottom:34px;display:flex;align-items:center;gap:11px;color:var(--ink)}
.brand b{font-family:'Cormorant Garamond',serif;font-weight:700;font-size:27px}
.brand .bdot{width:10px;height:10px;border-radius:50%%;background:var(--brick)}
.brand span{color:var(--taupe);font-size:16px}

/* карточка элемента */
.el{flex:0 0 392px;background:var(--surface);border:2px solid var(--ink);border-radius:20px;padding:20px 24px 22px;position:relative;box-shadow:0 16px 40px rgba(44,36,32,.13)}
.el .no{position:absolute;left:22px;top:18px;font-size:15px;font-weight:700;color:var(--taupe);letter-spacing:.04em}
.el .tn{position:absolute;right:22px;top:16px;font-size:15px;color:var(--brick);font-weight:700}
.glyph{font-family:'Noto Serif SC',serif;font-weight:700;font-size:150px;line-height:1;color:var(--ink);text-align:center;margin:30px 0 6px}
.pin{text-align:center;font-size:34px;font-weight:600;color:var(--brick);letter-spacing:.04em;margin-bottom:20px}
.split{display:flex;gap:10px;border-top:1px solid var(--hair);padding-top:17px}
.part{flex:1 1 0;text-align:center}
.part .v{font-size:31px;font-weight:700;line-height:1;height:34px;margin-bottom:7px}
.part .k{font-size:12px;letter-spacing:.09em;text-transform:uppercase;color:var(--taupe)}
.part.a .v{color:var(--brick)}
.part.b .v{color:var(--blue)}
.part.c .v{color:var(--amber);font-size:50px;line-height:1}
</style></head><body>
<div class="card">
  <div class="txt">
    <div class="eyebrow">Фонетика</div>
    <h1>Инициали <i>в китайском языке</i></h1>
    <div class="sub">Слог здесь не набирается из букв. Он собирается из трёх позиций — и каждая занята строго одним элементом</div>
    <div class="counts">
      <div class="cnt"><b>21</b><span>ИНИЦИАЛЬ</span></div>
      <div class="cnt"><b>35</b><span>ФИНАЛЕЙ</span></div>
      <div class="cnt"><b>4+1</b><span>ТОНА</span></div>
    </div>
  </div>
  <div class="el">
    <div class="no">1 слог</div>
    <div class="tn">3-й тон</div>
    <div class="glyph">好</div>
    <div class="pin">hǎo</div>
    <div class="split">
      <div class="part a"><div class="v">h</div><div class="k">инициаль</div></div>
      <div class="part b"><div class="v">ao</div><div class="k">финаль</div></div>
      <div class="part c"><div class="v">ˇ</div><div class="k">тон</div></div>
    </div>
  </div>
  <div class="brand"><span class="bdot"></span><b>Kitai School</b><span>&middot; kitai-school.ru</span></div>
</div>
</body></html>""" % (FONTS, VARS)

open(S + "ini-hero.html", "w", encoding="utf-8").write(hero)


# -------------------------------------------------------------- инфографика
def tile(ini, fin, res, han, bad=False, why=""):
    if bad:
        return ('<div class="tl bad">'
                '<div class="dom"><span class="l">%s</span><span class="r">%s</span><span class="x"></span></div>'
                '<div class="res">не бывает</div><div class="why">%s</div>'
                '</div>') % (ini, fin, why)
    return ('<div class="tl">'
            '<div class="dom"><span class="l">%s</span><span class="r">%s</span></div>'
            '<div class="res">%s</div><div class="why"><span class="han">%s</span></div>'
            '</div>') % (ini, fin, res, han)


good = "".join([
    tile("j", "ü", "jū", "居"),
    tile("n", "iou", "niú", "牛"),
    tile("g", "uei", "guī", "归"),
])
bad = "".join([
    tile("j", "u", "", "", True, "ju — это j + ü, а не j + u"),
    tile("g", "i", "", "", True, "g, k, h не идут с i"),
    tile("zh", "ü", "", "", True, "zh, ch, sh, r не идут с ü"),
])

info = """<!DOCTYPE html><html lang="ru"><head><meta charset="utf-8">
%s
<style>
%s
*{margin:0;box-sizing:border-box}html,body{width:1200px;height:HGTpx}
.wrap{width:1200px;height:HGTpx;background:linear-gradient(180deg,#fff 0%%,var(--cream) 46%%,var(--cream-2) 100%%);font-family:'Inter',sans-serif;padding:32px 46px 26px;display:flex;flex-direction:column}
.top{display:flex;align-items:flex-end;justify-content:space-between;gap:30px;margin-bottom:22px}
.eyebrow{color:var(--brick);font-weight:700;font-size:14.5px;letter-spacing:.17em;text-transform:uppercase;margin-bottom:7px}
h2{font-family:'Cormorant Garamond',serif;font-weight:600;font-size:41px;line-height:1.06;color:var(--ink);letter-spacing:-.3px}
h2 i{font-style:italic;color:var(--brick)}
.hint{flex:0 0 376px;background:var(--surface);border:1px solid var(--hair);border-left:4px solid var(--brick);border-radius:12px;padding:12px 17px;font-size:14.5px;color:var(--ink-2);line-height:1.36}
.hint b{color:var(--ink)}

.band{margin-bottom:18px}
.bh{display:flex;align-items:center;gap:12px;margin-bottom:12px}
.bh .t{font-size:13px;font-weight:700;letter-spacing:.11em;text-transform:uppercase;color:var(--taupe)}
.bh .ln{flex:1 1 auto;height:1px;background:var(--hair)}
.row{display:flex;gap:20px}
.tl{flex:1 1 0;text-align:center}
.dom{position:relative;display:flex;height:92px;border-radius:14px;overflow:hidden;border:2px solid var(--ink);box-shadow:0 6px 18px rgba(44,36,32,.09)}
.dom .l,.dom .r{flex:1 1 0;display:flex;align-items:center;justify-content:center;font-size:36px;font-weight:700;letter-spacing:.01em}
.dom .l{background:var(--brick-soft);color:var(--brick);border-right:2px solid var(--ink)}
.dom .r{background:var(--blue-s);color:var(--blue)}
.tl.bad .dom{border-color:#C0B5A7;box-shadow:none}
.tl.bad .dom .l{background:var(--cream-2);color:#9A8E7F;border-right-color:#C0B5A7}
.tl.bad .dom .r{background:var(--cream-2);color:#9A8E7F}
.x{position:absolute;left:8px;right:8px;top:50%%;margin-top:-4px;height:8px;border-radius:4px;background:var(--brick);transform:rotate(-13deg);opacity:.95}
.res{margin-top:11px;font-size:25px;font-weight:700;color:var(--ink);line-height:1}
.tl.bad .res{color:var(--brick);font-size:19px;margin-top:13px}
.why{margin-top:5px;font-size:14px;color:var(--taupe);line-height:1.3}
.han{font-family:'Noto Serif SC',serif;font-weight:700;font-size:22px;color:var(--ink-2)}

.foot{margin-top:auto;display:flex;align-items:center;gap:18px}
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
      <div class="eyebrow">Сочетаемость</div>
      <h2>Слог складывается из двух половин — <i>но не любых</i></h2>
    </div>
    <div class="hint">Левая половина костяшки — <b>инициаль</b>, правая — <b>финаль</b>. Сложить можно далеко не всякую пару: часть сочетаний не встречается никогда.</div>
  </div>

  <div class="band">
    <div class="bh"><span class="t">Складываются</span><span class="ln"></span></div>
    <div class="row">%s</div>
  </div>

  <div class="band">
    <div class="bh"><span class="t">Не складываются никогда</span><span class="ln"></span></div>
    <div class="row">%s</div>
  </div>

  <div class="foot">
    <div class="msg">На бумаге пар <b>21 × 35 = 735</b>. Базовых слогов в путунхуа — <b>чуть больше четырёхсот</b></div>
    <div class="brand"><span class="dot"></span><b>Kitai School</b><span>&middot; kitai-school.ru</span></div>
  </div>
</div>
</body></html>""" % (FONTS, VARS, good, bad)

info = info.replace("HGT", "636")
open(S + "ini-info.html", "w", encoding="utf-8").write(info)
print("ok")
