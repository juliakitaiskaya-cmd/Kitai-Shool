# -*- coding: utf-8 -*-
# Картинки к статье «Почему Китай называют Поднебесной»
# Обложка     — бронзовый сосуд с надписью 中国
# Инфографика — небо, всё под небом и середина; плюс разведение трёх слов
S = ("/tmp/claude-0/-home-user-Kitai-Shool/a463bfca-82a9-56fd-ae09-42a7257ff999/"
     "scratchpad/")

FONTS = ("<link href=\"https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,600;0,700;1,600"
         "&family=Inter:wght@400;500;600;700&family=Noto+Serif+SC:wght@600;700&display=swap\" rel=\"stylesheet\">")
VARS = (":root{--brick:#A41E3A;--brick-d:#841630;--brick-soft:#F7E6EB;--ink:#2C2420;--ink-2:#5A4F45;"
        "--taupe:#8B7D6B;--cream:#FAF7F2;--cream-2:#F3EDE3;--hair:#EAE3D8;--surface:#fff;"
        "--bronze:#7A6A44;--bronze-l:#9C8A5E;--bronze-d:#4A3F28;--patina:#6E8F7A;"
        "--sky:#39597F;--sky-soft:#E7EDF4}")

hero = """<!DOCTYPE html><html lang="ru"><head><meta charset="utf-8">
%(fonts)s
<style>
%(vars)s
*{margin:0;box-sizing:border-box}html,body{width:1200px;height:630px}
.card{width:1200px;height:630px;background:radial-gradient(1050px 660px at 14%% 10%%, #fff 0%%, var(--cream) 52%%, var(--cream-2) 100%%);position:relative;overflow:hidden;font-family:'Inter',sans-serif;padding:80px 56px 0 72px;display:flex;justify-content:space-between}
.card:before{content:"";position:absolute;left:0;top:0;bottom:0;width:12px;background:var(--brick)}
.txt{flex:0 0 462px;padding-top:4px}
.eyebrow{color:var(--brick);font-weight:700;font-size:18px;letter-spacing:.19em;text-transform:uppercase;margin-bottom:13px}
h1{font-family:'Cormorant Garamond',serif;font-weight:600;font-size:45px;line-height:1.07;color:var(--ink);letter-spacing:-.4px}
h1 i{font-style:italic;color:var(--brick)}
.sub{font-size:18px;color:var(--ink-2);line-height:1.42;max-width:29ch;margin-top:16px}
.tip{display:inline-block;margin-top:22px;background:var(--surface);border:1px solid var(--hair);border-left:4px solid var(--brick);border-radius:13px;padding:13px 19px;font-size:15.5px;color:var(--ink-2);line-height:1.36;max-width:33ch}
.tip b{color:var(--ink)}

.scene{flex:0 0 530px;padding-top:6px;display:flex;flex-direction:column;align-items:center}
.stage{display:flex;align-items:center;gap:26px}
.vessel{position:relative;width:240px;height:300px;background:linear-gradient(100deg,var(--bronze-l) 0%%,var(--bronze) 38%%,var(--bronze-d) 100%%);clip-path:polygon(2%% 0%%,98%% 0%%,86%% 8%%,78%% 16%%,73%% 24%%,74%% 32%%,80%% 40%%,85%% 48%%,85%% 56%%,80%% 64%%,74%% 71%%,71%% 78%%,78%% 88%%,88%% 96%%,90%% 100%%,10%% 100%%,12%% 96%%,22%% 88%%,29%% 78%%,26%% 71%%,20%% 64%%,15%% 56%%,15%% 48%%,20%% 40%%,26%% 32%%,27%% 24%%,22%% 16%%,14%% 8%%);filter:drop-shadow(0 14px 22px rgba(44,36,32,.26))}
.vessel .rim{position:absolute;left:0;right:0;top:17%%;height:2px;background:rgba(255,255,255,.22)}
.vessel .foot{position:absolute;left:0;right:0;bottom:11%%;height:2px;background:rgba(255,255,255,.18)}
.vessel .pat{position:absolute;left:14%%;right:14%%;top:42%%;height:17%%;background:rgba(110,143,122,.3)}
.vessel .ins{position:absolute;left:0;right:0;top:44%%;text-align:center;font-family:'Noto Serif SC',serif;font-size:27px;color:#F2E8D4;letter-spacing:.04em}
.gloss{background:var(--surface);border:1px solid var(--hair);border-radius:16px;padding:18px 22px 19px;box-shadow:0 12px 24px rgba(44,36,32,.14);text-align:center}
.gloss .h{font-family:'Noto Serif SC',serif;font-size:46px;color:var(--ink);line-height:1.1}
.gloss .p{font-size:15px;color:var(--ink-2);font-style:italic;margin-top:5px}
.gloss .r{font-size:16px;color:var(--brick);font-weight:700;margin-top:3px}
.cap{margin-top:26px;text-align:center;font-size:16px;color:var(--ink-2);line-height:1.42;max-width:44ch}
.cap b{color:var(--ink)}
.note{margin-top:18px;background:var(--surface);border:1px solid var(--hair);border-radius:13px;padding:12px 20px;font-size:15px;color:var(--ink-2);line-height:1.4;text-align:center;max-width:460px}
.note b{color:var(--brick)}
.brand{position:absolute;left:72px;bottom:28px;display:flex;align-items:center;gap:11px;color:var(--ink)}
.brand b{font-family:'Cormorant Garamond',serif;font-weight:700;font-size:26px}
.brand .bdot{width:10px;height:10px;border-radius:50%%;background:var(--brick)}
.brand span{color:var(--taupe);font-size:16px}
</style></head><body>
<div class="card">
  <div class="txt">
    <div class="eyebrow">Культура</div>
    <h1>Почему Китай называют <i>Поднебесной</i></h1>
    <div class="sub">Страна зовётся 中国 — «срединное государство». Поднебесной её называем мы</div>
    <div class="tip"><b>天下 — не имя страны,</b> а картина мира: всё, что лежит под небом</div>
  </div>
  <div class="scene">
    <div class="stage">
      <div class="vessel"><div class="pat"></div><div class="rim"></div><div class="foot"></div><div class="ins">中国</div></div>
      <div class="gloss">
        <div class="h">中国</div>
        <div class="p">Zhōngguó</div>
        <div class="r">срединное государство</div>
      </div>
    </div>
    <div class="cap">Самое раннее известное написание 中国 <b>сохранилось на бронзе эпохи Западная Чжоу</b></div>
    <div class="note">Тогда это значило не «Китай», а <b>срединные владения</b> — земли вокруг столицы</div>
  </div>
  <div class="brand"><span class="bdot"></span><b>Kitai School</b><span>&middot; kitai-school.ru</span></div>
</div>
</body></html>""" % dict(fonts=FONTS, vars=VARS)

open(S + "pod-hero.html", "w", encoding="utf-8").write(hero)

# --------------------------------------------------------------- инфографика
WORDS = [
    ("中国", "Zhōngguó", "срединное государство",
     "название страны — официальное и живое",
     "我是中国人 — «я китаец»", "Так Китай называют китайцы", "cn"),
    ("天下", "tiānxià", "всё, что под небом",
     "понятие о мире, а не имя страны",
     "天下第一 — «первый в мире»", "Страной это слово не называют", "sky"),
    ("Поднебесная", "—", "калька с 天下",
     "русское книжное имя Китая",
     "«вести из Поднебесной» — газетная формула",
     "По-китайски так не говорят", "ru"),
]

assert len(WORDS) == 3, "слов не три"
assert WORDS[2][0] == "Поднебесная", "русское слово должно стоять последним"

cards = "".join(
    '<div class="wc %s"><div class="wh">%s</div><div class="wp">%s</div>'
    '<div class="wm">%s</div><div class="wu">%s</div><div class="we">%s</div>'
    '<div class="wn">%s</div></div>'
    % (cls, han, py, mean, use, ex, note) for han, py, mean, use, ex, note, cls in WORDS)

info = """<!DOCTYPE html><html lang="ru"><head><meta charset="utf-8">
%(fonts)s
<style>
%(vars)s
*{margin:0;box-sizing:border-box}html,body{width:1200px;height:700px}
.wrap{width:1200px;height:700px;background:linear-gradient(180deg,#fff 0%%,var(--cream) 46%%,var(--cream-2) 100%%);font-family:'Inter',sans-serif;padding:30px 46px 26px;display:flex;flex-direction:column}
.top{display:flex;align-items:flex-end;justify-content:space-between;gap:30px;margin-bottom:18px}
.eyebrow{color:var(--brick);font-weight:700;font-size:14.5px;letter-spacing:.17em;text-transform:uppercase;margin-bottom:7px}
h2{font-family:'Cormorant Garamond',serif;font-weight:600;font-size:39px;line-height:1.07;color:var(--ink);letter-spacing:-.3px}
h2 i{font-style:italic;color:var(--brick)}
.hint{flex:0 0 384px;background:var(--surface);border:1px solid var(--hair);border-left:4px solid var(--brick);border-radius:12px;padding:12px 17px;font-size:14.5px;color:var(--ink-2);line-height:1.36}
.hint b{color:var(--ink)}

.sky{position:relative;flex:0 0 222px;height:222px;border-radius:16px;background:linear-gradient(180deg,var(--sky-soft) 0%%,#fff 72%%);border:1px solid var(--hair);overflow:hidden}
.dome{position:absolute;left:50%%;transform:translateX(-50%%);top:14px;width:900px;height:280px;border-radius:50%% 50%% 0 0;border:2px solid var(--sky);border-bottom:none;background:rgba(57,89,127,.05)}
.tian{position:absolute;left:50%%;transform:translateX(-50%%);top:12px;font-family:'Noto Serif SC',serif;font-size:30px;color:var(--sky)}
.tian small{display:block;font-family:'Inter',sans-serif;font-size:13px;color:var(--sky);letter-spacing:.05em;text-align:center;margin-top:1px}
.under{position:absolute;left:50%%;transform:translateX(-50%%);top:74px;font-size:15px;color:var(--sky);letter-spacing:.06em}
.mid{position:absolute;left:50%%;transform:translateX(-50%%);bottom:16px;background:var(--brick);color:#fff;border-radius:13px;padding:11px 26px 13px;text-align:center;box-shadow:0 8px 18px rgba(164,30,58,.28)}
.mid .m1{font-family:'Noto Serif SC',serif;font-size:29px;line-height:1.15}
.mid .m2{font-size:13px;letter-spacing:.05em;opacity:.92;margin-top:1px}
.side{position:absolute;bottom:30px;font-size:14px;color:var(--taupe)}
.side.l{left:66px}.side.r{right:66px}

.sep{display:flex;align-items:center;gap:16px;margin:16px 0 11px}
.sep span{font-size:15px;font-weight:700;color:var(--brick-d);white-space:nowrap}
.sep i{flex:1 1 auto;height:1px;background:var(--hair)}
.cards{display:flex;gap:14px}
.wc{flex:1 1 0;background:var(--surface);border:1px solid var(--hair);border-radius:14px;padding:13px 18px 14px;border-top:4px solid var(--taupe)}
.wc.cn{border-top-color:var(--brick)}
.wc.sky{border-top-color:var(--sky)}
.wc.ru{border-top-color:var(--taupe)}
.wh{font-family:'Noto Serif SC',serif;font-size:26px;color:var(--ink);line-height:1.15}
.wc.ru .wh{font-family:'Cormorant Garamond',serif;font-weight:700;font-size:27px}
.wp{font-size:13px;color:var(--ink-2);font-style:italic}
.wm{font-size:14.5px;font-weight:700;color:var(--ink);margin-top:4px}
.wu{font-size:13.5px;color:var(--ink-2);margin-top:2px;line-height:1.3}
.we{font-size:13.5px;color:var(--ink);margin-top:7px;line-height:1.3;background:var(--cream-2);border-radius:8px;padding:7px 10px}
.wn{font-size:13.5px;color:var(--brick-d);font-weight:700;margin-top:6px}

.foot{margin-top:auto;display:flex;align-items:center;gap:18px;padding-top:14px}
.foot .msg{flex:1 1 auto;background:var(--brick-soft);border:1px solid var(--brick);border-radius:14px;padding:11px 21px;font-size:15px;color:var(--ink);line-height:1.34}
.foot .msg b{color:var(--brick)}
.brand{display:flex;align-items:center;gap:10px;color:var(--ink);flex:0 0 auto}
.brand b{font-family:'Cormorant Garamond',serif;font-weight:700;font-size:23px}
.brand .dot2{width:9px;height:9px;border-radius:50%%;background:var(--brick)}
.brand span{color:var(--taupe);font-size:15px}
</style></head><body>
<div class="wrap">
  <div class="top">
    <div>
      <div class="eyebrow">Картина мира</div>
      <h2>Небо сверху, <i>середина внизу</i></h2>
    </div>
    <div class="hint">天下 означает «под небом» — то есть весь обитаемый мир. <b>Середина этого мира и называлась 中国.</b></div>
  </div>

  <div class="sky">
    <div class="dome"></div>
    <div class="tian">天<small>небо</small></div>
    <div class="under">天下 — всё, что под ним</div>
    <div class="side l">окраины</div>
    <div class="side r">окраины</div>
    <div class="mid"><div class="m1">中国</div><div class="m2">СРЕДИННОЕ ГОСУДАРСТВО</div></div>
  </div>

  <div class="sep"><span>Три слова, которые часто путают</span><i></i></div>
  <div class="cards">%(cards)s</div>

  <div class="foot">
    <div class="msg">Китайцы не зовут свою страну Поднебесной — <b>так её называем мы</b></div>
    <div class="brand"><span class="dot2"></span><b>Kitai School</b><span>&middot; kitai-school.ru</span></div>
  </div>
</div>
</body></html>""" % dict(fonts=FONTS, vars=VARS, cards=cards)

open(S + "pod-info.html", "w", encoding="utf-8").write(info)
print("ok | карточек:", len(WORDS))
