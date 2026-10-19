# -*- coding: utf-8 -*-
# Картинки к статье «История китайской каллиграфии»
# Обложка    — кисть и след мазка: ценится движение, а не ровный контур
# Инфографика — музейные этикетки: пять стилей как экспонаты в экспозиции
S = "/tmp/claude-0/-home-user-Kitai-Shool/a463bfca-82a9-56fd-ae09-42a7257ff999/scratchpad/"

FONTS = ("<link href=\"https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,600;0,700;1,600"
         "&family=Inter:wght@400;500;600;700&family=Noto+Serif+SC:wght@600;700&display=swap\" rel=\"stylesheet\">")
VARS = (":root{--brick:#A41E3A;--brick-d:#841630;--brick-soft:#F7E6EB;--ink:#2C2420;--ink-2:#5A4F45;"
        "--taupe:#8B7D6B;--cream:#FAF7F2;--cream-2:#F3EDE3;--hair:#EAE3D8;--surface:#fff;"
        "--green:#1E7A46;--amber:#C08A2E;--blue:#2F5D8C;--blue-s:#E7EEF6;"
        "--wood:#9A6B3F;--wood-2:#7E5431;--hair-b:#3A3330;--ink-w:#1E1A18;--card:#F6F1E6}")

# ------------------------------------------------------------------ обложка
hero = """<!DOCTYPE html><html lang="ru"><head><meta charset="utf-8">
%s
<style>
%s
*{margin:0;box-sizing:border-box}html,body{width:1200px;height:630px}
.card{width:1200px;height:630px;background:radial-gradient(1050px 660px at 16%% 14%%, #fff 0%%, var(--cream) 52%%, var(--cream-2) 100%%);position:relative;overflow:hidden;font-family:'Inter',sans-serif;padding:54px 56px 0 72px;display:flex;justify-content:space-between}
.card:before{content:"";position:absolute;left:0;top:0;bottom:0;width:12px;background:var(--brick)}
.txt{flex:0 0 540px;padding-top:4px}
.eyebrow{color:var(--brick);font-weight:700;font-size:18px;letter-spacing:.19em;text-transform:uppercase;margin-bottom:13px}
h1{font-family:'Cormorant Garamond',serif;font-weight:600;font-size:47px;line-height:1.06;color:var(--ink);letter-spacing:-.4px}
h1 i{font-style:italic;color:var(--brick)}
.sub{font-size:18.5px;color:var(--ink-2);line-height:1.42;max-width:33ch;margin-top:16px}
.note{display:inline-block;margin-top:22px;background:var(--surface);border:1px solid var(--hair);border-left:4px solid var(--brick);border-radius:13px;padding:13px 19px;font-size:15.5px;color:var(--ink-2);line-height:1.36;max-width:35ch}
.note b{color:var(--ink)}

/* лист, мазок и кисть */
.sheet{flex:0 0 492px;position:relative;height:520px;background:#FFFDF8;border:1px solid var(--hair);border-radius:8px;box-shadow:0 14px 30px rgba(44,36,32,.12);overflow:hidden}
.sheet:before{content:"";position:absolute;left:50%%;top:0;bottom:0;width:1px;background:repeating-linear-gradient(180deg,var(--hair) 0 10px,transparent 10px 20px)}
.sheet:after{content:"";position:absolute;top:50%%;left:0;right:0;height:1px;background:repeating-linear-gradient(90deg,var(--hair) 0 10px,transparent 10px 20px)}
.stroke{position:absolute;left:66px;top:128px;width:322px;height:44px;background:linear-gradient(98deg,var(--ink-w) 0%%,#241F1C 46%%,#332C29 72%%,rgba(51,44,41,.5) 88%%,rgba(51,44,41,0) 100%%);border-radius:26px 6px 30px 8px / 22px 22px 22px 22px;transform:rotate(-5deg)}
.stroke2{position:absolute;left:92px;top:268px;width:206px;height:30px;background:linear-gradient(96deg,rgba(30,26,24,.94) 0%%,rgba(36,31,28,.88) 56%%,rgba(59,51,49,.34) 84%%,rgba(59,51,49,0) 100%%);border-radius:18px 5px 20px 6px / 15px 15px 15px 15px;transform:rotate(3deg)}
.seal{position:absolute;left:92px;top:340px;width:58px;height:58px;border-radius:6px;background:var(--brick);display:flex;align-items:center;justify-content:center;box-shadow:0 4px 10px rgba(164,30,58,.3)}
.seal span{font-family:'Noto Serif SC',serif;font-weight:700;font-size:30px;color:#fff;line-height:1}
.brush{position:absolute;right:46px;top:-28px;width:46px;height:430px;transform:rotate(14deg);transform-origin:50%% 0}
.handle{position:absolute;left:11px;top:0;width:24px;height:318px;border-radius:12px 12px 4px 4px;background:linear-gradient(90deg,var(--wood-2),var(--wood),var(--wood-2));box-shadow:0 10px 24px rgba(44,36,32,.22)}
.ferrule{position:absolute;left:8px;top:308px;width:30px;height:22px;border-radius:4px;background:linear-gradient(90deg,#C9B07A,#E7D6A8,#C9B07A)}
.tip{position:absolute;left:5px;top:326px;width:36px;height:116px;background:linear-gradient(180deg,#2C2622 0%%,#1E1A18 56%%,#1E1A18 78%%,rgba(30,26,24,.2) 100%%);clip-path:polygon(0 0, 100%% 0, 62%% 72%%, 50%% 100%%, 38%% 72%%)}
.cap{position:absolute;right:16px;bottom:22px;background:rgba(255,255,255,.95);border:1px solid var(--hair);border-radius:11px;padding:9px 15px;font-size:14px;color:var(--ink-2);line-height:1.3}
.cap b{color:var(--ink)}
.brand{position:absolute;left:72px;bottom:28px;display:flex;align-items:center;gap:11px;color:var(--ink)}
.brand b{font-family:'Cormorant Garamond',serif;font-weight:700;font-size:26px}
.brand .bdot{width:10px;height:10px;border-radius:50%%;background:var(--brick)}
.brand span{color:var(--taupe);font-size:16px}
</style></head><body>
<div class="card">
  <div class="txt">
    <div class="eyebrow">История</div>
    <h1>История китайской каллиграфии: <i>как письмо стало искусством</i></h1>
    <div class="sub">В каллиграфии оценивают не контур знака, а движение, которое его оставило: скорость, нажим, порядок черт</div>
    <div class="note"><b>书法 — «метод письма»:</b> отдельная дисциплина со своим каноном, а не просто красивый почерк</div>
  </div>
  <div class="sheet">
    <div class="stroke"></div>
    <div class="stroke2"></div>
    <div class="seal"><span>书</span></div>
    <div class="brush">
      <div class="handle"></div>
      <div class="ferrule"></div>
      <div class="tip"></div>
    </div>
    <div class="cap">Сухой хвост мазка — <b>след скорости</b></div>
  </div>
  <div class="brand"><span class="bdot"></span><b>Kitai School</b><span>&middot; kitai-school.ru</span></div>
</div>
</body></html>""" % (FONTS, VARS)

open(S + "kl-hero.html", "w", encoding="utf-8").write(hero)

# -------------------------------------------------------------- инфографика
STYLES = [
    ("篆书", "чжуаньшу", "Печатное письмо", "древнейший из пяти",
     "вытянутые округлые линии почти одной толщины, строгая симметрия",
     "печати, вывески, оттиски на картинах"),
    ("隶书", "лишу", "Деловое письмо", "ханьская канцелярия",
     "линии выпрямлены, широкие горизонтали с утолщением на конце",
     "заголовки, оформление, стилизация под старину"),
    ("草书", "цаошу", "Скоропись", "появилась при Хань",
     "знаки связаны в один росчерк, части сокращены до намёка",
     "художественные свитки; читается с трудом даже носителями"),
    ("行书", "синшу", "Полускоропись", "им написано «Предисловие»",
     "между уставом и скорописью: связность есть, читаемость сохраняется",
     "рукописный почерк, записки, подписи"),
    ("楷书", "кайшу", "Уставное письмо", "канон сложился при Тан",
     "каждая черта отдельно, пропорции выверены, образец для прописей",
     "печать, учебники, прописи, основа современного письма"),
]

cards = "\n".join(
    '<div class="lab">'
    '  <div class="han">%s</div>'
    '  <div class="body">'
    '    <div class="nm">%s <span>%s</span></div>'
    '    <div class="per">%s</div>'
    '    <div class="ds">%s</div>'
    '    <div class="now"><b>Сегодня:</b> %s</div>'
    '  </div>'
    '</div>' % (han, ru, name, per, ds, now)
    for han, ru, name, per, ds, now in STYLES)

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
.hint{flex:0 0 356px;background:var(--surface);border:1px solid var(--hair);border-left:4px solid var(--brick);border-radius:12px;padding:12px 17px;font-size:14.5px;color:var(--ink-2);line-height:1.36}
.hint b{color:var(--ink)}

.rows{display:flex;flex-direction:column;gap:11px}
.lab{display:flex;align-items:stretch;gap:18px;background:var(--card);border:1px solid var(--hair);border-radius:10px;padding:12px 18px;box-shadow:0 4px 11px rgba(44,36,32,.05);border-left:5px solid var(--brick)}
.lab .han{flex:0 0 76px;display:flex;align-items:center;justify-content:center;font-family:'Noto Serif SC',serif;font-weight:700;font-size:34px;color:var(--ink);background:#fff;border:1px solid var(--hair);border-radius:7px}
.body{flex:1 1 auto;display:flex;align-items:center;gap:18px}
.nm{flex:0 0 196px;font-size:16.5px;font-weight:700;color:var(--ink);line-height:1.2}
.nm span{display:block;font-size:13px;font-weight:500;color:var(--taupe);margin-top:4px}
.per{flex:0 0 176px;font-size:13.5px;color:var(--brick);font-weight:600;line-height:1.3}
.ds{flex:1 1 auto;font-size:14px;color:var(--ink-2);line-height:1.34;border-left:1px solid var(--hair);padding-left:18px}
.now{flex:0 0 268px;font-size:13.5px;color:var(--ink-2);line-height:1.32;background:#fff;border:1px solid var(--hair);border-radius:8px;padding:8px 12px}
.now b{color:var(--ink)}

.foot{margin-top:auto;display:flex;align-items:center;gap:18px;padding-top:16px}
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
      <div class="eyebrow">Пять стилей письма</div>
      <h2>Экспозиция: <i>чем они различаются</i></h2>
    </div>
    <div class="hint">Стили <b>не сменяли друг друга по очереди</b>: они сосуществуют, и каждый до сих пор занят своим делом. Начертания здесь описаны словами — передать их обычным шрифтом нельзя.</div>
  </div>

  <div class="rows">
%s
  </div>

  <div class="foot">
    <div class="msg">Различать их стоит до того, как браться за кисть: <b>образец задаёт и технику, и порядок черт</b></div>
    <div class="brand"><span class="dot2"></span><b>Kitai School</b><span>&middot; kitai-school.ru</span></div>
  </div>
</div>
</body></html>""" % (FONTS, VARS, cards)

info = info.replace("HGT", "690")
open(S + "kl-info.html", "w", encoding="utf-8").write(info)
print("ok")
