# -*- coding: utf-8 -*-
# Картинки к статье «Ноль по-китайски»
# Обложка    — горсть монет и 零: ноль, который значит «мелочь»
# Инфографика — карта употреблений: где 零, где 〇, и слова с корнем 零
S = ("/tmp/claude-0/-home-user-Kitai-Shool/a463bfca-82a9-56fd-ae09-42a7257ff999/"
     "scratchpad/")

FONTS = ("<link href=\"https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,600;0,700;1,600"
         "&family=Inter:wght@400;500;600;700&family=Noto+Serif+SC:wght@600;700&display=swap\" rel=\"stylesheet\">")
VARS = (":root{--brick:#A41E3A;--brick-d:#841630;--brick-soft:#F7E6EB;--ink:#2C2420;--ink-2:#5A4F45;"
        "--taupe:#8B7D6B;--cream:#FAF7F2;--cream-2:#F3EDE3;--hair:#EAE3D8;--surface:#fff;"
        "--coin:#D9B96A;--coin-2:#B8914A;--coin-3:#8E6E34;--tray:#E7DECE;--slate:#2F5D8C}")

COINS = [(24, 132, -8), (100, 112, 6), (170, 142, -3), (58, 196, 10), (104, 58, 4)]

coins = "\n".join(
    '      <div class="coin" style="left:%dpx;top:%dpx;transform:rotate(%ddeg)">'
    '<span class="hole"></span></div>' % c for c in COINS)

hero = """<!DOCTYPE html><html lang="ru"><head><meta charset="utf-8">
%s
<style>
%s
*{margin:0;box-sizing:border-box}html,body{width:1200px;height:630px}
.card{width:1200px;height:630px;background:radial-gradient(1050px 660px at 14%% 12%%, #fff 0%%, var(--cream) 52%%, var(--cream-2) 100%%);position:relative;overflow:hidden;font-family:'Inter',sans-serif;padding:52px 46px 0 72px;display:flex;justify-content:space-between}
.card:before{content:"";position:absolute;left:0;top:0;bottom:0;width:12px;background:var(--brick)}
.txt{flex:0 0 498px;padding-top:6px}
.eyebrow{color:var(--brick);font-weight:700;font-size:18px;letter-spacing:.19em;text-transform:uppercase;margin-bottom:13px}
h1{font-family:'Cormorant Garamond',serif;font-weight:600;font-size:45px;line-height:1.07;color:var(--ink);letter-spacing:-.4px}
h1 i{font-style:italic;color:var(--brick)}
.sub{font-size:18px;color:var(--ink-2);line-height:1.42;max-width:31ch;margin-top:16px}
.tip{display:inline-block;margin-top:22px;background:var(--surface);border:1px solid var(--hair);border-left:4px solid var(--brick);border-radius:13px;padding:13px 19px;font-size:15.5px;color:var(--ink-2);line-height:1.36;max-width:35ch}
.tip b{color:var(--ink)}

/* монеты и знак */
.scene{flex:0 0 476px;padding-top:40px;display:flex;flex-direction:column;align-items:center}
.tray{position:relative;width:270px;height:280px;border-radius:20px;background:linear-gradient(170deg,#F3ECDF,var(--tray));box-shadow:inset 0 3px 10px rgba(44,36,32,.12), 0 12px 24px rgba(44,36,32,.14)}
.coin{position:absolute;width:74px;height:74px;border-radius:50%%;background:radial-gradient(circle at 34%% 30%%, #F0DCA8, var(--coin) 54%%, var(--coin-2) 86%%, var(--coin-3));box-shadow:0 4px 8px rgba(44,36,32,.26), inset 0 -3px 6px rgba(0,0,0,.18);display:flex;align-items:center;justify-content:center}
.coin .hole{width:21px;height:21px;border-radius:4px;background:var(--tray);box-shadow:inset 0 1px 3px rgba(0,0,0,.35)}
.sign{position:absolute;right:-86px;bottom:2px;background:var(--surface);border:1px solid var(--hair);border-radius:16px;padding:14px 22px 16px;text-align:center;box-shadow:0 10px 20px rgba(44,36,32,.16)}
.sign .h{font-family:'Noto Serif SC',serif;font-size:62px;line-height:1;color:var(--brick)}
.sign .p{font-size:15px;color:var(--ink-2);font-style:italic;margin-top:5px}
.sign .r{font-size:14px;color:var(--taupe);margin-top:1px}
.cap{margin-top:30px;text-align:center;font-size:16.5px;color:var(--ink-2);line-height:1.4;max-width:36ch}
.cap b{color:var(--ink)}
.brand{position:absolute;left:72px;bottom:28px;display:flex;align-items:center;gap:11px;color:var(--ink)}
.brand b{font-family:'Cormorant Garamond',serif;font-weight:700;font-size:26px}
.brand .bdot{width:10px;height:10px;border-radius:50%%;background:var(--brick)}
.brand span{color:var(--taupe);font-size:16px}
</style></head><body>
<div class="card">
  <div class="txt">
    <div class="eyebrow">Лексика</div>
    <h1>Ноль <i>по-китайски</i></h1>
    <div class="sub">零 — это не только цифра, но и «мелочь», и «остаток»</div>
    <div class="tip"><b>零钱 — мелкие деньги,</b> 零食 — перекус между делом. Один и тот же знак, и нуля в нём почти нет</div>
  </div>
  <div class="scene">
    <div class="tray">
COINS_HTML
      <div class="sign"><div class="h">零</div><div class="p">líng</div><div class="r">零钱 — мелочь</div></div>
    </div>
    <div class="cap">Знак для пустоты, <b>который означает мелкие деньги</b></div>
  </div>
  <div class="brand"><span class="bdot"></span><b>Kitai School</b><span>&middot; kitai-school.ru</span></div>
</div>
</body></html>""" % (FONTS, VARS)

hero = hero.replace("COINS_HTML", coins)
open(S + "nol-hero.html", "w", encoding="utf-8").write(hero)

# --------------------------------------------------------------- инфографика
USE = [
    ("Денежный документ", "零", "полная форма обязательна", True),
    ("Число с пропуском", "零", "一千零五 — тысяча пять", True),
    ("Дата", "〇 или 零", "二〇二六年 и 二零二六年", False),
    ("Номер телефона", "〇 или 零", "читается líng по цифрам", False),
]

assert len(USE) == 4, "контекстов не четыре"

use = "".join(
    '<div class="uc%s"><div class="ut">%s</div><div class="uh">%s</div>'
    '<div class="ud">%s</div></div>' % (" strict" if strict else "", t, h, d)
    for t, h, d, strict in USE)

WORDS = [
    ("零钱", "língqián", "мелочь"),
    ("零食", "língshí", "перекус"),
    ("零下", "língxià", "ниже нуля"),
    ("零件", "língjiàn", "деталь"),
    ("零售", "língshòu", "розница"),
]

assert len(WORDS) == 5, "слов с 零 не пять"

words = "".join(
    '<div class="wd"><span class="h">%s</span><span class="p">%s</span>'
    '<span class="r">%s</span></div>' % w for w in WORDS)

info = """<!DOCTYPE html><html lang="ru"><head><meta charset="utf-8">
%(fonts)s
<style>
%(vars)s
*{margin:0;box-sizing:border-box}html,body{width:1200px;height:HGTpx}
.wrap{width:1200px;height:HGTpx;background:linear-gradient(180deg,#fff 0%%,var(--cream) 46%%,var(--cream-2) 100%%);font-family:'Inter',sans-serif;padding:32px 46px 28px;display:flex;flex-direction:column}
.top{display:flex;align-items:flex-end;justify-content:space-between;gap:30px;margin-bottom:20px}
.eyebrow{color:var(--brick);font-weight:700;font-size:14.5px;letter-spacing:.17em;text-transform:uppercase;margin-bottom:7px}
h2{font-family:'Cormorant Garamond',serif;font-weight:600;font-size:40px;line-height:1.07;color:var(--ink);letter-spacing:-.3px}
h2 i{font-style:italic;color:var(--brick)}
.hint{flex:0 0 376px;background:var(--surface);border:1px solid var(--hair);border-left:4px solid var(--brick);border-radius:12px;padding:12px 17px;font-size:14.5px;color:var(--ink-2);line-height:1.36}
.hint b{color:var(--ink)}

.uses{display:flex;gap:13px}
.uc{flex:1 1 0;background:var(--surface);border:1px solid var(--hair);border-radius:15px;padding:14px 17px 15px;box-shadow:0 4px 11px rgba(44,36,32,.05)}
.uc.strict{border-color:var(--brick);background:var(--brick-soft)}
.ut{font-size:13px;color:var(--taupe);letter-spacing:.03em}
.uc.strict .ut{color:var(--brick-d);font-weight:700}
.uh{font-family:'Noto Serif SC',serif;font-size:32px;color:var(--ink);line-height:1.2;margin-top:3px}
.uc.strict .uh{color:var(--brick)}
.ud{font-size:14px;color:var(--ink-2);margin-top:3px;line-height:1.32}

.sep{display:flex;align-items:center;gap:16px;margin:20px 0 14px}
.sep span{font-size:15px;font-weight:700;color:var(--brick-d);white-space:nowrap}
.sep i{flex:1 1 auto;height:1px;background:var(--hair)}

.words{display:flex;gap:12px}
.wd{flex:1 1 0;background:var(--surface);border:1px solid var(--hair);border-radius:14px;padding:12px 14px;text-align:center;box-shadow:0 4px 10px rgba(44,36,32,.04)}
.wd .h{display:block;font-family:'Noto Serif SC',serif;font-size:25px;color:var(--ink);line-height:1.15}
.wd .p{display:block;font-size:13px;color:var(--brick-d);font-style:italic;margin-top:1px}
.wd .r{display:block;font-size:14px;color:var(--ink-2);margin-top:2px}

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
      <div class="eyebrow">Два облика нуля</div>
      <h2>Где 零, <i>а где хватит кружка</i></h2>
    </div>
    <div class="hint">Кружок 〇 удобен в датах и номерах. <b>А там, где важна подделка — в денежных документах, — пишут только 零</b>: его не дорисуешь.</div>
  </div>

  <div class="uses">%(use)s</div>

  <div class="sep"><span>零 без всякого нуля</span><i></i></div>
  <div class="words">%(words)s</div>

  <div class="foot">
    <div class="msg">В этих словах 零 значит <b>«мелкий, дробный», а не «пустой»</b></div>
    <div class="brand"><span class="dot2"></span><b>Kitai School</b><span>&middot; kitai-school.ru</span></div>
  </div>
</div>
</body></html>""" % dict(fonts=FONTS, vars=VARS, use=use, words=words)

info = info.replace("HGT", "462")
open(S + "nol-info.html", "w", encoding="utf-8").write(info)
assert len(COINS) == 5, "монет не пять"
print("ok, монет:", len(COINS), "| контекстов:", len(USE), "| слов:", len(WORDS))
