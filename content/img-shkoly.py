# -*- coding: utf-8 -*-
# Картинки к статье «Как учатся китайские школьники»
# Обложка    — школьная доска с расписанием на день
# Инфографика — стопка учебников: толщина равна доле учебных часов
S = "/tmp/claude-0/-home-user-Kitai-Shool/a463bfca-82a9-56fd-ae09-42a7257ff999/scratchpad/"

FONTS = ("<link href=\"https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,600;0,700;1,600"
         "&family=Inter:wght@400;500;600;700&family=Noto+Serif+SC:wght@600;700&display=swap\" rel=\"stylesheet\">")
VARS = (":root{--brick:#A41E3A;--brick-d:#841630;--brick-soft:#F7E6EB;--ink:#2C2420;--ink-2:#5A4F45;"
        "--taupe:#8B7D6B;--cream:#FAF7F2;--cream-2:#F3EDE3;--hair:#EAE3D8;--surface:#fff;"
        "--green:#1E7A46;--amber:#C08A2E;--blue:#2F5D8C;--blue-s:#E7EEF6;"
        "--board:#2F4A3C;--board-2:#27402F;--frame:#A8762F;--frame-2:#8A5F24;--chalk:#F2EEE2}")

LESSONS = [
    ("语文", "Китайский язык"),
    ("数学", "Математика"),
    ("英语", "Английский"),
    ("体育", "Физкультура"),
    ("科学", "Естествознание"),
    ("道德与法治", "Мораль и право"),
    ("音乐", "Музыка"),
]

rows = "\n".join(
    '<div class="ln"><span class="n">%d</span><span class="han">%s</span><span class="ru">%s</span></div>'
    % (i + 1, han, ru) for i, (han, ru) in enumerate(LESSONS))

hero = """<!DOCTYPE html><html lang="ru"><head><meta charset="utf-8">
%s
<style>
%s
*{margin:0;box-sizing:border-box}html,body{width:1200px;height:630px}
.card{width:1200px;height:630px;background:radial-gradient(1050px 660px at 14%% 12%%, #fff 0%%, var(--cream) 52%%, var(--cream-2) 100%%);position:relative;overflow:hidden;font-family:'Inter',sans-serif;padding:52px 56px 0 72px;display:flex;justify-content:space-between}
.card:before{content:"";position:absolute;left:0;top:0;bottom:0;width:12px;background:var(--brick)}
.txt{flex:0 0 536px;padding-top:4px}
.eyebrow{color:var(--brick);font-weight:700;font-size:18px;letter-spacing:.19em;text-transform:uppercase;margin-bottom:13px}
h1{font-family:'Cormorant Garamond',serif;font-weight:600;font-size:48px;line-height:1.06;color:var(--ink);letter-spacing:-.4px}
h1 i{font-style:italic;color:var(--brick)}
.sub{font-size:18.5px;color:var(--ink-2);line-height:1.42;max-width:33ch;margin-top:16px}
.note{display:inline-block;margin-top:22px;background:var(--surface);border:1px solid var(--hair);border-left:4px solid var(--brick);border-radius:13px;padding:13px 19px;font-size:15.5px;color:var(--ink-2);line-height:1.36;max-width:35ch}
.note b{color:var(--ink)}

/* доска */
.board{flex:0 0 498px;height:470px;background:linear-gradient(160deg,var(--board) 0%%,var(--board-2) 100%%);border:13px solid var(--frame);border-radius:7px;box-shadow:0 16px 32px rgba(44,36,32,.22), inset 0 0 60px rgba(0,0,0,.18);position:relative;padding:24px 28px 0}
.board:after{content:"";position:absolute;left:-13px;right:-13px;bottom:-26px;height:14px;background:linear-gradient(180deg,var(--frame),var(--frame-2));border-radius:0 0 5px 5px}
.btitle{font-family:'Noto Serif SC',serif;font-weight:700;font-size:26px;color:var(--chalk);letter-spacing:.04em;border-bottom:2px solid rgba(242,238,226,.42);padding-bottom:10px;margin-bottom:16px}
.btitle span{font-family:'Inter',sans-serif;font-weight:400;font-size:15px;color:rgba(242,238,226,.72);margin-left:10px}
.ln{display:flex;align-items:baseline;gap:12px;margin-bottom:12px;color:var(--chalk)}
.ln .n{width:22px;font-size:15px;color:rgba(242,238,226,.6)}
.ln .han{font-family:'Noto Serif SC',serif;font-weight:700;font-size:24px;min-width:142px;line-height:1.15}
.ln .ru{font-size:16px;color:rgba(242,238,226,.84)}
.chalk{position:absolute;right:34px;bottom:-24px;width:66px;height:12px;border-radius:3px;background:linear-gradient(180deg,#FFFDF6,#D9D2BF);box-shadow:0 3px 6px rgba(0,0,0,.35);z-index:2}
.brand{position:absolute;left:72px;bottom:28px;display:flex;align-items:center;gap:11px;color:var(--ink)}
.brand b{font-family:'Cormorant Garamond',serif;font-weight:700;font-size:26px}
.brand .bdot{width:10px;height:10px;border-radius:50%%;background:var(--brick)}
.brand span{color:var(--taupe);font-size:16px}
</style></head><body>
<div class="card">
  <div class="txt">
    <div class="eyebrow">Школа</div>
    <h1>Как учатся <i>китайские школьники</i></h1>
    <div class="sub">Чему и сколько учат в китайской школе: набор предметов, доля часов и место иностранного языка</div>
    <div class="note"><b>На родной язык и литературу</b> уходит втрое больше времени, чем на иностранный</div>
  </div>
  <div class="board">
    <div class="btitle">课程表<span>расписание на день</span></div>
%s
    <div class="chalk"></div>
  </div>
  <div class="brand"><span class="bdot"></span><b>Kitai School</b><span>&middot; kitai-school.ru</span></div>
</div>
</body></html>""" % (FONTS, VARS, rows)

open(S + "sh-hero.html", "w", encoding="utf-8").write(hero)

# -------------------------------------------------------------- инфографика
BOOKS = [
    ("语文", "Китайский язык и литература", "20–22 %", 76, "#A41E3A", "#F7E6EB"),
    ("数学", "Математика", "13–15 %", 56, "#2F5D8C", "#E7EEF6"),
    ("体育与健康", "Физкультура и здоровье", "10–11 %", 46, "#1E7A46", "#E3F6E9"),
    ("科学", "Естественные науки", "8–10 %", 40, "#C08A2E", "#FBF2DF"),
    ("外语", "Иностранный язык", "6–8 %", 32, "#5A4F45", "#EFE9DF"),
]

books = "\n".join(
    '<div class="bk" style="height:%dpx;background:%s;border-color:%s">'
    '  <span class="h">%s</span>'
    '  <span class="r">%s</span>'
    '  <span class="p" style="color:%s">%s</span>'
    '</div>' % (h, soft, col, han, ru, col, pct)
    for han, ru, pct, h, col, soft in BOOKS)

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
.hint{flex:0 0 372px;background:var(--surface);border:1px solid var(--hair);border-left:4px solid var(--brick);border-radius:12px;padding:12px 17px;font-size:14.5px;color:var(--ink-2);line-height:1.36}
.hint b{color:var(--ink)}

.stack{display:flex;flex-direction:column;gap:7px;align-items:center}
.bk{width:980px;border:1px solid;border-left-width:9px;border-radius:5px;display:flex;align-items:center;gap:20px;padding:0 26px;box-shadow:0 4px 10px rgba(44,36,32,.08)}
.bk .h{font-family:'Noto Serif SC',serif;font-weight:700;font-size:25px;color:var(--ink);flex:0 0 172px;line-height:1}
.bk .r{flex:1 1 auto;font-size:16.5px;color:var(--ink);font-weight:500}
.bk .p{flex:0 0 108px;text-align:right;font-size:19px;font-weight:700}

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
      <div class="eyebrow">Доля учебных часов</div>
      <h2>Толщина учебника — <i>это время</i></h2>
    </div>
    <div class="hint">Доли за девять лет обязательного образования, <b>по государственному стандарту 2022 года</b>. Провинции перераспределяют недельную нагрузку внутри этих рамок.</div>
  </div>

  <div class="stack">
%s
  </div>

  <div class="foot">
    <div class="msg">Главное, что видно сразу: <b>на родной язык и литературу уходит втрое больше времени, чем на иностранный</b></div>
    <div class="brand"><span class="dot2"></span><b>Kitai School</b><span>&middot; kitai-school.ru</span></div>
  </div>
</div>
</body></html>""" % (FONTS, VARS, books)

info = info.replace("HGT", "556")
open(S + "sh-info.html", "w", encoding="utf-8").write(info)
print("ok")
