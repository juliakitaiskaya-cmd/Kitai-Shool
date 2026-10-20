# -*- coding: utf-8 -*-
# Картинки к статье «Напитки на китайском»
# Обложка    — меню-табло чайной: так названия и встречаются в жизни
# Инфографика — стакан с двумя шкалами: сладость и лёд
S = "/tmp/claude-0/-home-user-Kitai-Shool/a463bfca-82a9-56fd-ae09-42a7257ff999/scratchpad/"

FONTS = ("<link href=\"https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,600;0,700;1,600"
         "&family=Inter:wght@400;500;600;700&family=Noto+Serif+SC:wght@600;700&display=swap\" rel=\"stylesheet\">")
VARS = (":root{--brick:#A41E3A;--brick-d:#841630;--brick-soft:#F7E6EB;--ink:#2C2420;--ink-2:#5A4F45;"
        "--taupe:#8B7D6B;--cream:#FAF7F2;--cream-2:#F3EDE3;--hair:#EAE3D8;--surface:#fff;"
        "--green:#1E7A46;--green-s:#E3F6E9;--amber:#C08A2E;--amber-s:#FBF2DF;--blue:#2F5D8C;--blue-s:#E7EEF6;"
        "--board:#2E3A33;--board-2:#232C27;--milk:#D9B48A;--milk-2:#C79C6E;--pearl:#3A2E26}")

MENU = [
    ("水", "shuǐ", "вода"),
    ("茶", "chá", "чай"),
    ("奶茶", "nǎichá", "молочный чай"),
    ("咖啡", "kāfēi", "кофе"),
    ("果汁", "guǒzhī", "сок"),
    ("牛奶", "niúnǎi", "молоко"),
]

menu_rows = "\n".join(
    '<div class="mrow"><span class="han">%s</span><span class="py">%s</span>'
    '<span class="ru">%s</span></div>' % m for m in MENU)

hero = """<!DOCTYPE html><html lang="ru"><head><meta charset="utf-8">
%s
<style>
%s
*{margin:0;box-sizing:border-box}html,body{width:1200px;height:630px}
.card{width:1200px;height:630px;background:radial-gradient(1050px 660px at 14%% 12%%, #fff 0%%, var(--cream) 52%%, var(--cream-2) 100%%);position:relative;overflow:hidden;font-family:'Inter',sans-serif;padding:52px 46px 0 72px;display:flex;justify-content:space-between}
.card:before{content:"";position:absolute;left:0;top:0;bottom:0;width:12px;background:var(--brick)}
.txt{flex:0 0 500px;padding-top:4px}
.eyebrow{color:var(--brick);font-weight:700;font-size:18px;letter-spacing:.19em;text-transform:uppercase;margin-bottom:13px}
h1{font-family:'Cormorant Garamond',serif;font-weight:600;font-size:46px;line-height:1.06;color:var(--ink);letter-spacing:-.4px}
h1 i{font-style:italic;color:var(--brick)}
.sub{font-size:18px;color:var(--ink-2);line-height:1.42;max-width:31ch;margin-top:16px}
.note{display:inline-block;margin-top:22px;background:var(--surface);border:1px solid var(--hair);border-left:4px solid var(--brick);border-radius:13px;padding:13px 19px;font-size:15.5px;color:var(--ink-2);line-height:1.36;max-width:33ch}
.note b{color:var(--ink)}

/* меню-табло */
.board{flex:0 0 500px;margin-top:12px;height:452px;background:linear-gradient(168deg,var(--board),var(--board-2));border-radius:18px;box-shadow:0 16px 34px rgba(30,40,34,.3);padding:26px 30px;display:flex;flex-direction:column}
.bhead{color:#D8CFC2;font-size:13.5px;letter-spacing:.2em;text-transform:uppercase;padding-bottom:13px;border-bottom:1px solid rgba(255,255,255,.16);margin-bottom:6px}
.mrow{display:flex;align-items:baseline;gap:14px;padding:13px 0;border-bottom:1px dashed rgba(255,255,255,.14)}
.mrow:last-child{border-bottom:none}
.mrow .han{font-family:'Noto Serif SC',serif;font-size:30px;color:#fff;flex:0 0 108px;line-height:1}
.mrow .py{font-size:16px;color:#C9BFB2;flex:0 0 118px;font-style:italic}
.mrow .ru{font-size:17px;color:#EFE9E0}
.brand{position:absolute;left:72px;bottom:28px;display:flex;align-items:center;gap:11px;color:var(--ink)}
.brand b{font-family:'Cormorant Garamond',serif;font-weight:700;font-size:26px}
.brand .bdot{width:10px;height:10px;border-radius:50%%;background:var(--brick)}
.brand span{color:var(--taupe);font-size:16px}
</style></head><body>
<div class="card">
  <div class="txt">
    <div class="eyebrow">Лексика</div>
    <h1>Напитки <i>на китайском</i></h1>
    <div class="sub">Названия — половина дела: напиток ещё нужно заказать горячим, со льдом или без сахара</div>
    <div class="note"><b>Самая частая путаница:</b> 红茶 — это тот самый чай, который по-русски называют чёрным</div>
  </div>
  <div class="board">
    <div class="bhead">Меню</div>
%s
  </div>
  <div class="brand"><span class="bdot"></span><b>Kitai School</b><span>&middot; kitai-school.ru</span></div>
</div>
</body></html>""" % (FONTS, VARS, menu_rows)

open(S + "np-hero.html", "w", encoding="utf-8").write(hero)

# -------------------------------------------------------------- инфографика
SUGAR = [
    ("正常糖", "zhèngcháng táng", "как обычно"),
    ("少糖", "shǎo táng", "поменьше"),
    ("半糖", "bàn táng", "наполовину"),
    ("微糖", "wēi táng", "совсем чуть-чуть"),
    ("无糖", "wú táng", "без сахара"),
]

ICE = [
    ("正常冰", "zhèngcháng bīng", "как обычно"),
    ("少冰", "shǎo bīng", "поменьше льда"),
    ("去冰", "qù bīng", "безо льда"),
    ("常温", "chángwēn", "комнатной температуры"),
    ("热的", "rè de", "горячий"),
]


def scale(items, side):
    return "\n".join(
        '<div class="step"><span class="han">%s</span><span class="py">%s</span>'
        '<span class="ru">%s</span></div>' % i for i in items)


info = """<!DOCTYPE html><html lang="ru"><head><meta charset="utf-8">
%s
<style>
%s
*{margin:0;box-sizing:border-box}html,body{width:1200px;height:HGTpx}
.wrap{width:1200px;height:HGTpx;background:linear-gradient(180deg,#fff 0%%,var(--cream) 46%%,var(--cream-2) 100%%);font-family:'Inter',sans-serif;padding:32px 46px 32px;display:flex;flex-direction:column}
.top{display:flex;align-items:flex-end;justify-content:space-between;gap:30px;margin-bottom:20px}
.eyebrow{color:var(--brick);font-weight:700;font-size:14.5px;letter-spacing:.17em;text-transform:uppercase;margin-bottom:7px}
h2{font-family:'Cormorant Garamond',serif;font-weight:600;font-size:40px;line-height:1.07;color:var(--ink);letter-spacing:-.3px}
h2 i{font-style:italic;color:var(--brick)}
.hint{flex:0 0 392px;background:var(--surface);border:1px solid var(--hair);border-left:4px solid var(--brick);border-radius:12px;padding:12px 17px;font-size:14.5px;color:var(--ink-2);line-height:1.36}
.hint b{color:var(--ink)}

.main{display:flex;gap:28px;align-items:center}
.col{flex:1 1 0;display:flex;flex-direction:column;gap:9px}
.coltitle{font-size:15px;font-weight:700;color:var(--brick);letter-spacing:.04em;margin-bottom:3px}
.step{display:flex;align-items:baseline;gap:12px;background:var(--surface);border:1px solid var(--hair);border-radius:12px;padding:10px 16px;box-shadow:0 4px 11px rgba(44,36,32,.05)}
.step .han{font-family:'Noto Serif SC',serif;font-size:20px;color:var(--ink);flex:0 0 92px;line-height:1.2}
.step .py{font-size:13.5px;color:var(--taupe);font-style:italic;flex:0 0 126px}
.step .ru{font-size:14.5px;color:var(--ink-2)}

/* стакан */
.cup{flex:0 0 206px;display:flex;flex-direction:column;align-items:center}
.lid{width:170px;height:15px;border-radius:8px 8px 3px 3px;background:#CFC6BA;box-shadow:0 3px 7px rgba(44,36,32,.18);position:relative;z-index:2}
.glass{position:relative;width:156px;height:216px;margin-top:-2px;background:linear-gradient(180deg,rgba(255,255,255,.9),rgba(255,255,255,.55));border:2px solid #D7CFC3;border-radius:10px 10px 22px 22px;overflow:hidden;clip-path:polygon(0 0,100%% 0,88%% 100%%,12%% 100%%)}
.tea{position:absolute;left:0;right:0;bottom:0;height:176px;background:linear-gradient(180deg,var(--milk),var(--milk-2))}
.pearls{position:absolute;left:0;right:0;bottom:6px;height:46px;display:flex;align-items:flex-end;justify-content:center;gap:7px;flex-wrap:wrap;padding:0 26px}
.pearls span{width:17px;height:17px;border-radius:50%%;background:var(--pearl);box-shadow:inset 0 -3px 4px rgba(0,0,0,.3)}
.straw{position:absolute;left:52%%;top:-10px;width:13px;height:150px;background:linear-gradient(90deg,#B03147,#8E2339);transform:rotate(9deg);border-radius:7px}
.cupcap{margin-top:14px;font-size:14px;color:var(--ink-2);text-align:center;line-height:1.36;max-width:21ch}
.cupcap b{color:var(--ink)}

.foot{margin-top:auto;display:flex;align-items:center;gap:18px;padding-top:20px}
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
      <div class="eyebrow">Как заказывают</div>
      <h2>Две шкалы, <i>которые спросят на кассе</i></h2>
    </div>
    <div class="hint">Порядок уровней общий, а <b>доли у каждой сети свои</b>: одно и то же слово в двух кофейнях может означать разную сладость.</div>
  </div>

  <div class="main">
    <div class="col">
      <div class="coltitle">Сладость — 甜度</div>
%s
    </div>
    <div class="cup">
      <div class="lid"></div>
      <div class="glass">
        <div class="tea"></div>
        <div class="pearls"><span></span><span></span><span></span><span></span><span></span><span></span></div>
        <div class="straw"></div>
      </div>
      <div class="cupcap"><b>Спрашивают почти всегда</b> — ответ готовьте заранее</div>
    </div>
    <div class="col">
      <div class="coltitle">Лёд и температура — 冰度</div>
%s
    </div>
  </div>

  <div class="foot">
    <div class="msg">Если сомневаетесь, скажите <b>少糖、少冰</b> — это понятный и безопасный заказ</div>
    <div class="brand"><span class="dot2"></span><b>Kitai School</b><span>&middot; kitai-school.ru</span></div>
  </div>
</div>
</body></html>""" % (FONTS, VARS, scale(SUGAR, "l"), scale(ICE, "r"))

info = info.replace("HGT", "524")
open(S + "np-info.html", "w", encoding="utf-8").write(info)
print("ok")
