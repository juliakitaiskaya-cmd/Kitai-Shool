# -*- coding: utf-8 -*-
# Картинки к статье «Самое длинное слово в китайском языке»
# Обложка    — мерная лента под строкой знаков: измерять нечего, пока не решено, где границы
# Инфографика — составы из вагонов: четыре претендента, каждый вагон один знак
S = "/tmp/claude-0/-home-user-Kitai-Shool/a463bfca-82a9-56fd-ae09-42a7257ff999/scratchpad/"

FONTS = ("<link href=\"https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,600;0,700;1,600"
         "&family=Inter:wght@400;500;600;700&family=Noto+Serif+SC:wght@600;700&display=swap\" rel=\"stylesheet\">")
VARS = (":root{--brick:#A41E3A;--brick-d:#841630;--brick-soft:#F7E6EB;--ink:#2C2420;--ink-2:#5A4F45;"
        "--taupe:#8B7D6B;--cream:#FAF7F2;--cream-2:#F3EDE3;--hair:#EAE3D8;--surface:#fff;"
        "--green:#1E7A46;--green-soft:#E3F6E9;--amber:#C08A2E;--amber-s:#FBF2DF;--blue:#2F5D8C;--blue-s:#E7EEF6;"
        "--tape:#F0D79A;--tape-2:#E4C277;--tape-e:#C9A353}")

# ------------------------------------------------------------------ обложка
ticks = "".join(
    '<i class="%s"%s></i>' % ("big" if k % 5 == 0 else "", ' data-n="%d"' % (k // 5) if k % 5 == 0 else "")
    for k in range(46))

hero = """<!DOCTYPE html><html lang="ru"><head><meta charset="utf-8">
%s
<style>
%s
*{margin:0;box-sizing:border-box}html,body{width:1200px;height:630px}
.card{width:1200px;height:630px;background:radial-gradient(1150px 700px at 82%% 8%%, #fff 0%%, var(--cream) 52%%, var(--cream-2) 100%%);position:relative;overflow:hidden;font-family:'Inter',sans-serif;padding:52px 64px 0 72px}
.card:before{content:"";position:absolute;left:0;top:0;bottom:0;width:12px;background:var(--brick)}
.eyebrow{color:var(--brick);font-weight:700;font-size:18px;letter-spacing:.19em;text-transform:uppercase;margin-bottom:13px}
h1{font-family:'Cormorant Garamond',serif;font-weight:600;font-size:52px;line-height:1.05;color:var(--ink);letter-spacing:-.4px;max-width:21ch}
h1 i{font-style:italic;color:var(--brick)}
.sub{font-size:19px;color:var(--ink-2);line-height:1.4;max-width:46ch;margin-top:15px}

/* строка знаков с мерной лентой под ней */
.stage{position:absolute;left:72px;right:64px;top:330px}
.han{display:flex;gap:14px}
.han span{width:84px;height:84px;background:var(--surface);border:1px solid var(--hair);border-radius:11px;display:flex;align-items:center;justify-content:center;font-family:'Noto Serif SC',serif;font-weight:700;font-size:46px;color:var(--ink);box-shadow:0 5px 13px rgba(44,36,32,.07)}
.han span.on{border-color:var(--brick);background:var(--brick-soft)}

.tape{margin-top:16px;height:58px;background:linear-gradient(180deg,var(--tape),var(--tape-2));border:1px solid var(--tape-e);border-radius:6px;position:relative;display:flex;align-items:flex-start;padding:0 2px;box-shadow:0 7px 18px rgba(44,36,32,.14)}
.tape:before,.tape:after{content:"";position:absolute;top:-1px;bottom:-1px;width:16px;background:linear-gradient(90deg,rgba(44,36,32,.14),rgba(44,36,32,0))}
.tape:before{left:-1px;border-radius:6px 0 0 6px}
.tape:after{right:-1px;transform:scaleX(-1);border-radius:6px 0 0 6px}
.tape i{display:block;width:24px;height:15px;border-left:1px solid rgba(70,52,20,.5)}
.tape i.big{height:26px;border-left:2px solid rgba(70,52,20,.72);position:relative}
.tape i.big:after{content:attr(data-n);position:absolute;left:4px;top:28px;font-size:12.5px;font-weight:600;color:#6B5324}
.brace{position:absolute;left:0;top:186px;width:196px;height:15px;border:2px solid var(--brick);border-bottom:0;border-radius:9px 9px 0 0}
.brace:after{content:"слово? два слова?";position:absolute;left:0;right:0;top:19px;text-align:center;font-size:14.5px;font-weight:600;color:var(--brick);white-space:nowrap}
.pin{position:absolute;right:0;top:-148px;background:var(--surface);border:1px solid var(--hair);border-left:4px solid var(--brick);border-radius:13px;padding:13px 19px;font-size:16px;color:var(--ink-2);line-height:1.36;max-width:33ch;box-shadow:0 7px 18px rgba(44,36,32,.09)}
.pin b{color:var(--ink)}
.brand{position:absolute;right:64px;bottom:30px;display:flex;align-items:center;gap:11px;color:var(--ink)}
.brand b{font-family:'Cormorant Garamond',serif;font-weight:700;font-size:26px}
.brand .bdot{width:10px;height:10px;border-radius:50%%;background:var(--brick)}
.brand span{color:var(--taupe);font-size:16px}
</style></head><body>
<div class="card">
  <div class="eyebrow">Длина слова</div>
  <h1>Самое длинное слово<br><i>в китайском языке</i></h1>
  <div class="sub">В китайском письме нет пробелов. Длину измерить не получится, пока не решено, где слово начинается и где кончается</div>
  <div class="stage">
    <div class="han"><span class="on">脱</span><span class="on">氧</span><span>核</span><span>糖</span><span>核</span><span>酸</span></div>
    <div class="tape">%s</div>
    <div class="brace"></div>
    <div class="pin"><b>Шесть знаков — это длина?</b> Или это четыре части одного термина, записанные подряд</div>
  </div>
  <div class="brand"><span class="bdot"></span><b>Kitai School</b><span>&middot; kitai-school.ru</span></div>
</div>
</body></html>""" % (FONTS, VARS, ticks)

open(S + "dl-hero.html", "w", encoding="utf-8").write(hero)

# -------------------------------------------------------------- инфографика
TRAINS = [
    ("脱氧核糖核酸", "tuōyǎng hétáng hésuān", "ДНК", "Термин", "#2F5D8C", "#E7EEF6",
     "собран из названий частей молекулы"),
    ("中华人民共和国", "Zhōnghuá Rénmín Gònghéguó", "Полное название КНР", "Имя собственное", "#A41E3A",
     "#F7E6EB", "название, а не словарное слово"),
    ("歇斯底里", "xiēsīdǐlǐ", "hysteria", "Заимствование", "#C08A2E", "#FBF2DF",
     "знаки подобраны по звучанию, а не по смыслу"),
    ("总而言之", "zǒng'éryánzhī", "короче говоря", "Устойчивое выражение", "#1E7A46", "#E3F6E9",
     "четыре знака, по стандарту пишется слитно"),
]


def cars(word, color):
    return "".join('<i style="border-color:%s">%s</i>' % (color, ch) for ch in word)


rows = "\n".join(
    '<div class="row">'
    '  <div class="train">%s</div>'
    '  <div class="meta">'
    '    <div class="py">%s</div>'
    '    <div class="ru">%s</div>'
    '  </div>'
    '  <div class="verdict" style="background:%s;border-color:%s">'
    '    <b style="color:%s">%s</b><span>%s</span>'
    '  </div>'
    '</div>' % (cars(w, c), py, ru, soft, c, c, v, note)
    for w, py, ru, v, c, soft, note in TRAINS)

info = """<!DOCTYPE html><html lang="ru"><head><meta charset="utf-8">
%s
<style>
%s
*{margin:0;box-sizing:border-box}html,body{width:1200px;height:HGTpx}
.wrap{width:1200px;height:HGTpx;background:linear-gradient(180deg,#fff 0%%,var(--cream) 44%%,var(--cream-2) 100%%);font-family:'Inter',sans-serif;padding:32px 46px 26px;display:flex;flex-direction:column}
.top{display:flex;align-items:flex-end;justify-content:space-between;gap:30px;margin-bottom:20px}
.eyebrow{color:var(--brick);font-weight:700;font-size:14.5px;letter-spacing:.17em;text-transform:uppercase;margin-bottom:7px}
h2{font-family:'Cormorant Garamond',serif;font-weight:600;font-size:40px;line-height:1.07;color:var(--ink);letter-spacing:-.3px}
h2 i{font-style:italic;color:var(--brick)}
.hint{flex:0 0 358px;background:var(--surface);border:1px solid var(--hair);border-left:4px solid var(--brick);border-radius:12px;padding:12px 17px;font-size:14.5px;color:var(--ink-2);line-height:1.36}
.hint b{color:var(--ink)}

.rows{display:flex;flex-direction:column;gap:12px}
.row{display:flex;align-items:center;gap:18px;background:var(--surface);border:1px solid var(--hair);border-radius:14px;padding:12px 18px;box-shadow:0 5px 14px rgba(44,36,32,.05)}
.train{flex:0 0 408px;display:flex;align-items:center;gap:7px}
.train i{display:flex;align-items:center;justify-content:center;width:50px;height:50px;border:2px solid;border-radius:8px 8px 5px 5px;background:var(--cream);font-family:'Noto Serif SC',serif;font-weight:700;font-size:27px;font-style:normal;color:var(--ink);position:relative}
.train i:after{content:"";position:absolute;left:9px;right:9px;bottom:-7px;height:5px;border-radius:0 0 4px 4px;background:rgba(44,36,32,.16)}
.meta{flex:1 1 auto;min-width:0}
.meta .py{font-size:15px;font-weight:600;color:var(--ink);line-height:1.25}
.meta .ru{font-size:13.5px;color:var(--taupe);margin-top:3px;line-height:1.3}
.verdict{flex:0 0 298px;border:1px solid;border-radius:11px;padding:9px 14px}
.verdict b{display:block;font-size:14.5px;line-height:1.2}
.verdict span{display:block;font-size:13px;color:var(--ink-2);margin-top:4px;line-height:1.3}

.foot{margin-top:auto;display:flex;align-items:center;gap:18px;padding-top:16px}
.foot .msg{flex:1 1 auto;background:var(--brick-soft);border:1px solid var(--brick);border-radius:14px;padding:12px 21px;font-size:15.5px;color:var(--ink);line-height:1.34}
.foot .msg b{color:var(--brick)}
.brand{display:flex;align-items:center;gap:10px;color:var(--ink);flex:0 0 auto}
.brand b{font-family:'Cormorant Garamond',serif;font-weight:700;font-size:23px}
.brand .dot2{width:9px;height:9px;border-radius:50%%;background:var(--brick)}
.brand span{color:var(--taupe);font-size:15px}
</style></head><body>
<div class="wrap">
  <div class="top">
    <div>
      <div class="eyebrow">Претенденты на рекорд</div>
      <h2>Длина разная — <i>и каждый раз по своей причине</i></h2>
    </div>
    <div class="hint">Каждый вагон — один знак. <b>Чем длиннее состав, тем вероятнее, что перед вами название или термин</b>, собранный из нескольких частей.</div>
  </div>

  <div class="rows">
%s
  </div>

  <div class="foot">
    <div class="msg">Поэтому у вопроса нет победителя: <b>длина зависит от того, где провести границы</b>, а границы в китайском письме ничем не обозначены</div>
    <div class="brand"><span class="dot2"></span><b>Kitai School</b><span>&middot; kitai-school.ru</span></div>
  </div>
</div>
</body></html>""" % (FONTS, VARS, rows)

info = info.replace("HGT", "636")
open(S + "dl-info.html", "w", encoding="utf-8").write(info)
print("ok")
