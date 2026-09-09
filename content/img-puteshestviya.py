# -*- coding: utf-8 -*-
S = "/tmp/claude-0/-home-user-Kitai-Shool/a463bfca-82a9-56fd-ae09-42a7257ff999/scratchpad/"

FONTS = ("<link href=\"https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,600;0,700;1,600"
         "&family=Inter:wght@400;500;600;700&family=Noto+Serif+SC:wght@600;700&display=swap\" rel=\"stylesheet\">")
VARS = (":root{--brick:#A41E3A;--brick-d:#841630;--brick-soft:#F7E6EB;--ink:#2C2420;--ink-2:#5A4F45;"
        "--taupe:#8B7D6B;--cream:#FAF7F2;--cream-2:#F3EDE3;--hair:#EAE3D8;--surface:#fff;"
        "--green:#1E7A46;--green-soft:#E3F6E9;--amber:#C08A2E;--amber-s:#FBF2DF;--blue:#2F5D8C;--blue-s:#E7EEF6}")

# ------------------------------------------------------------------ обложка: посадочный талон
hero = """<!DOCTYPE html><html lang="ru"><head><meta charset="utf-8">
FONTS
<style>
VARS
*{margin:0;box-sizing:border-box}html,body{width:1200px;height:630px}
.card{width:1200px;height:630px;background:radial-gradient(1100px 700px at 80PCT 18PCT, #fff 0PCT, var(--cream) 56PCT, var(--cream-2) 100PCT);display:flex;align-items:center;padding:0 54px 0 76px;position:relative;overflow:hidden;font-family:'Inter',sans-serif}
.card:before{content:"";position:absolute;left:0;top:0;bottom:0;width:12px;background:var(--brick)}
.seal{position:absolute;right:40px;top:26px;width:92px;height:92px;border:2.5px solid var(--brick);border-radius:14px;display:flex;align-items:center;justify-content:center;color:var(--brick);font-family:'Noto Serif SC',serif;font-weight:700;font-size:32px;opacity:.9}
.txt{flex:0 0 372px;max-width:372px}
.eyebrow{color:var(--brick);font-weight:700;font-size:19px;letter-spacing:.19em;text-transform:uppercase;margin-bottom:14px}
h1{font-family:'Cormorant Garamond',serif;font-weight:600;font-size:51px;line-height:1.04;color:var(--ink);letter-spacing:-.5px}
h1 i{font-style:italic;color:var(--brick)}
.sub{font-size:18.5px;color:var(--ink-2);line-height:1.42;max-width:22ch;margin-top:18px}
.brand{position:absolute;left:76px;bottom:34px;display:flex;align-items:center;gap:12px;color:var(--ink)}
.brand b{font-family:'Cormorant Garamond',serif;font-weight:700;font-size:28px}.brand .bdot{width:11px;height:11px;border-radius:50PCT;background:var(--brick)}.brand span{color:var(--taupe);font-size:17px}

.art{flex:1 1 auto;display:flex;align-items:center;justify-content:center}
.pass{display:flex;background:var(--surface);border:1px solid var(--hair);border-radius:20px;box-shadow:0 14px 34px rgba(44,36,32,.13);overflow:hidden;transform:rotate(-2deg)}
.main{width:432px;padding:20px 26px 22px}
.hdr{display:flex;align-items:center;justify-content:space-between;border-bottom:1px solid var(--hair);padding-bottom:10px}
.hdr .air{font-family:'Cormorant Garamond',serif;font-weight:700;font-size:20px;color:var(--brick)}
.hdr .kind{font-size:10.5px;font-weight:700;letter-spacing:.16em;text-transform:uppercase;color:var(--taupe)}
.route{display:flex;align-items:center;justify-content:space-between;margin-top:16px}
.route .pt{text-align:center}
.route .pt b{display:block;font-family:'Cormorant Garamond',serif;font-size:34px;font-weight:700;color:var(--ink);line-height:1}
.route .pt span{display:block;font-size:11px;font-weight:700;letter-spacing:.14em;text-transform:uppercase;color:var(--taupe);margin-top:5px}
.route .pt.cn b{font-family:'Noto Serif SC',serif;font-size:32px;color:var(--brick)}
.route .pl{flex:1 1 auto;color:var(--brick);font-size:22px;text-align:center;opacity:.75}
.fields{display:flex;gap:22px;margin-top:18px;padding-top:14px;border-top:1px dashed var(--hair)}
.fl span{display:block;font-size:10px;font-weight:700;letter-spacing:.14em;text-transform:uppercase;color:var(--taupe)}
.fl b{display:block;font-size:15px;color:var(--ink);margin-top:3px;font-weight:600}
.legs{margin-top:16px;font-size:13px;color:var(--ink-2);line-height:1.35}
.legs b{color:var(--ink)}
.stub{width:172px;border-left:2px dashed var(--hair);background:var(--brick-soft);display:flex;flex-direction:column;align-items:center;justify-content:center;padding:18px 12px;text-align:center}
.stub .n{font-family:'Cormorant Garamond',serif;font-size:66px;font-weight:700;color:var(--brick);line-height:1}
.stub .w{font-size:14px;font-weight:600;color:var(--ink);margin-top:4px}
.stub .d{font-size:11.5px;color:var(--taupe);margin-top:10px;line-height:1.3}
</style></head><body>
<div class="card"><div class="seal">旅行</div>
<div class="txt">
  <div class="eyebrow">В поездку</div>
  <h1>Китайский <i>для путешествий</i></h1>
  <div class="sub">Не курс, а готовые фразы под конкретные моменты</div>
</div>
<div class="art">
  <div class="pass">
    <div class="main">
      <div class="hdr"><span class="air">Kitai School</span><span class="kind">Разговорник</span></div>
      <div class="route">
        <div class="pt"><b>RUS</b><span>вылет</span></div>
        <div class="pl">&#9992;</div>
        <div class="pt cn"><b>中国</b><span>прилёт</span></div>
      </div>
      <div class="fields">
        <div class="fl"><span>Формат</span><b>фраза · пиньинь</b></div>
        <div class="fl"><span>Наизусть</span><b>5 фраз</b></div>
        <div class="fl"><span>В телефоне</span><b>остальные</b></div>
      </div>
      <div class="legs">Маршрут: <b>аэропорт → такси → отель → рынок → ресторан</b></div>
    </div>
    <div class="stub">
      <div class="n">50</div>
      <div class="w">фраз</div>
      <div class="d">с переводом и подсказкой, когда сказать</div>
    </div>
  </div>
</div>
<div class="brand"><span class="bdot"></span><b>Kitai School</b><span>&middot; kitai-school.ru</span></div></div>
</body></html>"""
hero = hero.replace("FONTS", FONTS).replace("VARS", VARS).replace("PCT", "%")
open(S + "put-hero.html", "w", encoding="utf-8").write(hero)

# ------------------------------------------------------------------ инфографика: экран телефона
STEPS = [
    ("1", "Показать адрес", "иероглифами, а не латиницей",
     "визитка отеля или скриншот — работает без единого слова"),
    ("2", "Показать на карте", "точку, а не название",
     "снимает вопрос, даже если топоним звучит непривычно"),
    ("3", "Попросить написать", "цену, время, номер",
     "услышать незнакомое трудно, прочитать цифру — легко"),
]
steps_html = "".join(
    '<div class="st"><span class="n">%s</span><div class="tx"><b>%s</b><span class="sub">%s</span>'
    '<div class="why">%s</div></div></div>' % (n, t, s, w) for n, t, s, w in STEPS)

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
.hint{flex:0 0 316px;font-size:13.5px;color:var(--ink-2);line-height:1.34;border-left:3px solid var(--brick);padding-left:14px}
.hint b{color:var(--brick)}

.body{display:flex;gap:26px;margin-top:18px;align-items:center}
.phone{flex:0 0 322px;height:452px;background:var(--ink);border-radius:36px;padding:12px;box-shadow:0 16px 38px rgba(44,36,32,.22);position:relative}
.notch{position:absolute;left:50PCT;transform:translateX(-50PCT);top:19px;width:104px;height:20px;border-radius:12px;background:#3C332C}
.scr{width:100PCT;height:100PCT;background:#fff;border-radius:26px;padding:44px 20px 20px;display:flex;flex-direction:column}
.scr .lbl{font-size:11px;font-weight:700;letter-spacing:.14em;text-transform:uppercase;color:var(--taupe);text-align:center}
.addr{margin-top:14px;background:var(--cream);border:1px solid var(--hair);border-radius:16px;padding:16px 14px;text-align:center}
.addr .hz{font-family:'Noto Serif SC',serif;font-weight:700;font-size:27px;color:var(--ink);line-height:1.4;letter-spacing:1px}
.addr .py{font-size:12.5px;color:var(--taupe);margin-top:9px;line-height:1.3}
.say{margin-top:14px;background:var(--brick-soft);border:1px solid var(--brick);border-radius:14px;padding:11px 13px;text-align:center}
.say .hz{font-family:'Noto Serif SC',serif;font-weight:700;font-size:19px;color:var(--brick);letter-spacing:1px}
.say .ru{font-size:12.5px;color:var(--ink-2);margin-top:5px;line-height:1.3}
.hand{margin-top:auto;text-align:center;font-size:12.5px;color:var(--taupe);line-height:1.3}

.right{flex:1 1 auto;display:flex;flex-direction:column;gap:12px}
.st{display:flex;gap:14px;background:#fff;border:1px solid var(--hair);border-radius:16px;padding:14px 20px 16px;box-shadow:0 4px 14px rgba(44,36,32,.05)}
.st .n{flex:0 0 30px;height:30px;border-radius:50PCT;background:var(--brick);color:#fff;font-family:'Cormorant Garamond',serif;font-weight:700;font-size:18px;display:flex;align-items:center;justify-content:center;margin-top:2px}
.st .tx b{font-family:'Cormorant Garamond',serif;font-size:23px;font-weight:700;color:var(--ink);line-height:1.1}
.st .tx .sub{font-size:13px;color:var(--brick);font-weight:600;margin-left:9px}
.st .why{font-size:13.5px;color:var(--ink-2);line-height:1.34;margin-top:6px}

.foot{margin-top:16px;display:flex;align-items:center;gap:16px}
.foot .msg{flex:1 1 auto;background:var(--green-soft);border:1px solid var(--green);border-radius:14px;padding:11px 20px;font-size:15.5px;color:var(--ink);line-height:1.34}
.foot .msg b{color:var(--green)}
.brand{display:flex;align-items:center;gap:10px;color:var(--ink);flex:0 0 auto}
.brand b{font-family:'Cormorant Garamond',serif;font-weight:700;font-size:23px}.brand .dot{width:9px;height:9px;border-radius:50PCT;background:var(--brick)}.brand span{color:var(--taupe);font-size:15px}
</style></head><body>
<div class="wrap">
  <div class="top">
    <div>
      <div class="eyebrow">Когда вас не поняли</div>
      <h2>Не произносить, <i>а показывать</i></h2>
    </div>
    <div class="hint">Тон может подвести, и слово услышат другим. А <b>написанное читается одинаково всеми</b> — и вами, и собеседником.</div>
  </div>

  <div class="body">
    <div class="phone"><div class="notch"></div>
      <div class="scr">
        <div class="lbl">Экран телефона</div>
        <div class="addr">
          <div class="hz">北京市<br>朝阳区</div>
          <div class="py">адрес жилья иероглифами — скриншот или визитка отеля</div>
        </div>
        <div class="say">
          <div class="hz">请送我去这个地址</div>
          <div class="ru">«Отвезите меня по этому адресу» — говорите и сразу показываете</div>
        </div>
        <div class="hand">Показать проще, чем повторить трижды</div>
      </div>
    </div>
    <div class="right">STEPS</div>
  </div>

  <div class="foot">
    <div class="msg">Тридцать секунд дома — сохранить адрес и скриншот карты — и <b>целой категории проблем не будет</b></div>
    <div class="brand"><span class="dot"></span><b>Kitai School</b><span>&middot; kitai-school.ru</span></div>
  </div>
</div>
</body></html>"""
info = (info.replace("FONTS", FONTS).replace("VARS", VARS).replace("PCT", "%")
            .replace("HGTpx", "665px").replace("STEPS", steps_html))
open(S + "put-info.html", "w", encoding="utf-8").write(info)
print("ok")
