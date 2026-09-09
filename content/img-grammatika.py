# -*- coding: utf-8 -*-
S = "/tmp/claude-0/-home-user-Kitai-Shool/a463bfca-82a9-56fd-ae09-42a7257ff999/scratchpad/"

FONTS = ("<link href=\"https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,600;0,700;1,600"
         "&family=Inter:wght@400;500;600;700&family=Noto+Serif+SC:wght@600;700&display=swap\" rel=\"stylesheet\">")
VARS = (":root{--brick:#A41E3A;--brick-d:#841630;--brick-soft:#F7E6EB;--ink:#2C2420;--ink-2:#5A4F45;"
        "--taupe:#8B7D6B;--cream:#FAF7F2;--cream-2:#F3EDE3;--hair:#EAE3D8;--surface:#fff;"
        "--green:#1E7A46;--green-soft:#E3F6E9;--amber:#C08A2E;--amber-s:#FBF2DF;--blue:#2F5D8C;--blue-s:#E7EEF6}")

# ------------------------------------------------------------------ обложка: блоки-конструктор
BLOCKS = [("Кто", "#A41E3A"), ("Когда", "#C08A2E"), ("Где", "#2F5D8C"), ("Что делает", "#1E7A46")]
blocks_html = "".join(
    '<div class="bl" style="background:%s"><span>%s</span></div>' % (c, t) for t, c in BLOCKS)

hero = """<!DOCTYPE html><html lang="ru"><head><meta charset="utf-8">
FONTS
<style>
VARS
*{margin:0;box-sizing:border-box}html,body{width:1200px;height:630px}
.card{width:1200px;height:630px;background:radial-gradient(1100px 700px at 80PCT 20PCT, #fff 0PCT, var(--cream) 56PCT, var(--cream-2) 100PCT);display:flex;align-items:center;padding:0 60px 0 76px;position:relative;overflow:hidden;font-family:'Inter',sans-serif}
.card:before{content:"";position:absolute;left:0;top:0;bottom:0;width:12px;background:var(--brick)}
.seal{position:absolute;right:40px;top:26px;width:92px;height:92px;border:2.5px solid var(--brick);border-radius:14px;display:flex;align-items:center;justify-content:center;color:var(--brick);font-family:'Noto Serif SC',serif;font-weight:700;font-size:34px;opacity:.9}
.txt{flex:0 0 386px;max-width:386px}
.eyebrow{color:var(--brick);font-weight:700;font-size:19px;letter-spacing:.19em;text-transform:uppercase;margin-bottom:14px}
h1{font-family:'Cormorant Garamond',serif;font-weight:600;font-size:51px;line-height:1.04;color:var(--ink);letter-spacing:-.5px}
h1 i{font-style:italic;color:var(--brick)}
.sub{font-size:18.5px;color:var(--ink-2);line-height:1.42;max-width:22ch;margin-top:18px}
.brand{position:absolute;left:76px;bottom:34px;display:flex;align-items:center;gap:12px;color:var(--ink)}
.brand b{font-family:'Cormorant Garamond',serif;font-weight:700;font-size:28px}.brand .bdot{width:11px;height:11px;border-radius:50PCT;background:var(--brick)}.brand span{color:var(--taupe);font-size:17px}

.art{flex:1 1 auto;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:26px}
.chain{display:flex;align-items:center}
.bl{position:relative;height:104px;display:flex;align-items:center;justify-content:center;padding:0 26px;color:#fff;font-weight:700;font-size:19px;box-shadow:0 8px 22px rgba(44,36,32,.16)}
.bl:first-child{border-radius:16px 0 0 16px}
.bl:last-child{border-radius:0 16px 16px 0}
.bl:after{content:"";position:absolute;right:-13px;top:50PCT;transform:translateY(-50PCT);width:26px;height:26px;border-radius:50PCT;background:inherit;z-index:2}
.bl:last-child:after{display:none}
.bl span{position:relative;z-index:3}
.plate{background:var(--surface);border:1px solid var(--hair);border-radius:16px;padding:14px 26px;box-shadow:0 6px 18px rgba(44,36,32,.07);text-align:center;max-width:520px}
.plate b{display:block;font-family:'Cormorant Garamond',serif;font-size:24px;font-weight:700;color:var(--ink);line-height:1.15}
.plate span{display:block;font-size:14px;color:var(--taupe);margin-top:5px;line-height:1.3}
</style></head><body>
<div class="card"><div class="seal">语法</div>
<div class="txt">
  <div class="eyebrow">Грамматика</div>
  <h1>Грамматика <i>китайского</i></h1>
  <div class="sub">Слова не меняются — роль задаёт место в предложении</div>
</div>
<div class="art">
  <div class="chain">BLOCKS</div>
  <div class="plate"><b>Порядок и есть грамматика</b><span>сдвиньте блок — получится другое предложение</span></div>
</div>
<div class="brand"><span class="bdot"></span><b>Kitai School</b><span>&middot; kitai-school.ru</span></div></div>
</body></html>"""
hero = hero.replace("FONTS", FONTS).replace("VARS", VARS).replace("PCT", "%").replace("BLOCKS", blocks_html)
open(S + "gram-hero.html", "w", encoding="utf-8").write(hero)

# ------------------------------------------------------------------ инфографика: рамка предложения
SLOTS = [
    ("Кто",        "我",        "wǒ",          "я",            "#A41E3A"),
    ("Когда",      "昨天",      "zuótiān",     "вчера",        "#C08A2E"),
    ("Где",        "在咖啡馆",  "zài kāfēiguǎn", "в кафе",     "#2F5D8C"),
    ("С кем",      "跟朋友",    "gēn péngyou", "с другом",     "#7A4E8C"),
    ("Что делает", "吃了",      "chī le",      "поужинал",     "#1E7A46"),
    ("Что именно", "晚饭",      "wǎnfàn",      "ужин",         "#B4552F"),
]
slots_html = "".join(
    '<div class="sl"><div class="role" style="background:%s">%s</div>'
    '<div class="cell"><div class="hz">%s</div><div class="py">%s</div><div class="ru">%s</div></div></div>'
    % (c, role, hz, py, ru) for role, hz, py, ru, c in SLOTS)

hero_ru = ["Я вчера в кафе с другом ужинал", "Вчера я ужинал в кафе с другом", "С другом я вчера в кафе ужинал"]
ru_html = "".join('<div class="v ok"><span>&#10003;</span>%s</div>' % v for v in hero_ru)

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
.hint{flex:0 0 312px;font-size:13.5px;color:var(--ink-2);line-height:1.34;border-left:3px solid var(--brick);padding-left:14px}
.hint b{color:var(--brick)}

.frame{margin-top:18px;background:#fff;border:1px solid var(--hair);border-radius:20px;padding:18px 22px 20px;box-shadow:0 5px 16px rgba(44,36,32,.06)}
.slots{display:flex;gap:10px}
.sl{flex:1 1 0}
.role{border-radius:10px 10px 0 0;color:#fff;font-size:12.5px;font-weight:700;letter-spacing:.08em;text-transform:uppercase;text-align:center;padding:7px 4px}
.cell{border:1.5px solid var(--hair);border-top:none;border-radius:0 0 12px 12px;padding:13px 8px 14px;text-align:center;background:var(--cream)}
.hz{font-family:'Noto Serif SC',serif;font-weight:700;font-size:27px;color:var(--ink);line-height:1.15;letter-spacing:1px}
.py{font-size:12.5px;color:var(--brick);font-weight:600;margin-top:6px}
.ru{font-size:13px;color:var(--ink-2);margin-top:5px}
.full{margin-top:16px;padding-top:14px;border-top:1px dashed var(--hair);text-align:center}
.full .l{font-size:11.5px;font-weight:700;letter-spacing:.14em;text-transform:uppercase;color:var(--taupe)}
.full .s{font-size:16px;color:var(--ink);margin-top:6px}
.full .s b{color:var(--brick)}

.cmp{display:flex;gap:20px;margin-top:16px}
.col{flex:1 1 0;background:#fff;border:1px solid var(--hair);border-radius:18px;padding:14px 20px 16px;box-shadow:0 4px 14px rgba(44,36,32,.05)}
.col.no{border-color:var(--brick)}
.col h3{font-family:'Cormorant Garamond',serif;font-size:23px;font-weight:700;color:var(--ink);margin-bottom:4px}
.col .cap{font-size:12px;font-weight:700;letter-spacing:.13em;text-transform:uppercase;color:var(--taupe);margin-bottom:9px}
.v{display:flex;align-items:flex-start;gap:9px;font-size:14px;line-height:1.4;color:var(--ink-2);padding:4px 0}
.v span{flex:0 0 18px;font-weight:700}
.v.ok span{color:var(--green)}
.v.bad span{color:var(--brick)}
.v.bad{color:var(--ink-2)}
.v .hz{font-family:'Noto Serif SC',serif;font-size:16px;font-weight:700;color:var(--ink);letter-spacing:.5px}
.v .note{display:block;font-size:12.5px;color:var(--taupe);margin-top:2px}

.foot{margin-top:16px;display:flex;align-items:center;gap:16px}
.foot .msg{flex:1 1 auto;background:var(--amber-s);border:1px solid var(--amber);border-radius:14px;padding:11px 20px;font-size:15px;color:var(--ink);line-height:1.34}
.foot .msg b{color:var(--brick)}
.brand{display:flex;align-items:center;gap:10px;color:var(--ink);flex:0 0 auto}
.brand b{font-family:'Cormorant Garamond',serif;font-weight:700;font-size:23px}.brand .dot{width:9px;height:9px;border-radius:50PCT;background:var(--brick)}.brand span{color:var(--taupe);font-size:15px}
</style></head><body>
<div class="wrap">
  <div class="top">
    <div>
      <div class="eyebrow">Рамка предложения</div>
      <h2>Каждый блок <i>на своём месте</i></h2>
    </div>
    <div class="hint">В китайском слово не меняется. Роль ему задаёт <b>только позиция</b> — поэтому порядок и есть грамматика.</div>
  </div>

  <div class="frame">
    <div class="slots">SLOTS</div>
    <div class="full">
      <div class="l">Целиком</div>
      <div class="s"><b class="hz">我昨天在咖啡馆跟朋友吃了晚饭。</b> — «Я вчера в кафе с другом поужинал»</div>
    </div>
  </div>

  <div class="cmp">
    <div class="col">
      <div class="cap">По-русски</div>
      <h3>Переставить можно</h3>
      RU
      <div class="v ok"><span>&#10003;</span><div><span class="note" style="margin-top:0">Роль слова показывает окончание, поэтому смысл не теряется при любом порядке</span></div></div>
    </div>
    <div class="col no">
      <div class="cap">По-китайски</div>
      <h3>Переставить нельзя</h3>
      <div class="v bad"><span>&#10007;</span><div><span class="hz">我在咖啡馆昨天…</span><span class="note">время после места — так не говорят</span></div></div>
      <div class="v bad"><span>&#10007;</span><div><span class="hz">我吃了晚饭跟朋友…</span><span class="note">«с кем» после сказуемого — предложение рассыпается</span></div></div>
      <div class="v ok"><span>&#10003;</span><div><span class="note" style="margin-top:0">Время — единственный блок, который может стоять и до подлежащего: 昨天我在咖啡馆…</span></div></div>
    </div>
  </div>

  <div class="foot">
    <div class="msg">Поэтому грамматику проверяют <b>переводом с русского</b>: в обратную сторону ошибка не видна</div>
    <div class="brand"><span class="dot"></span><b>Kitai School</b><span>&middot; kitai-school.ru</span></div>
  </div>
</div>
</body></html>"""
info = (info.replace("FONTS", FONTS).replace("VARS", VARS).replace("PCT", "%")
            .replace("HGTpx", "700px").replace("SLOTS", slots_html).replace("RU", ru_html))
open(S + "gram-info.html", "w", encoding="utf-8").write(info)
print("ok")
