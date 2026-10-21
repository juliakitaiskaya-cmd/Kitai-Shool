# -*- coding: utf-8 -*-
# Картинки к статье «„Я тебя люблю“ по-китайски»
# Обложка    — почтовая открытка: фразу чаще пишут, чем произносят
# Инфографика — тоновые контуры трёх слогов
S = "/tmp/claude-0/-home-user-Kitai-Shool/a463bfca-82a9-56fd-ae09-42a7257ff999/scratchpad/"

FONTS = ("<link href=\"https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,600;0,700;1,600"
         "&family=Inter:wght@400;500;600;700&family=Noto+Serif+SC:wght@600;700&display=swap\" rel=\"stylesheet\">")
VARS = (":root{--brick:#A41E3A;--brick-d:#841630;--brick-soft:#F7E6EB;--ink:#2C2420;--ink-2:#5A4F45;"
        "--taupe:#8B7D6B;--cream:#FAF7F2;--cream-2:#F3EDE3;--hair:#EAE3D8;--surface:#fff;"
        "--green:#1E7A46;--green-s:#E3F6E9;--amber:#C08A2E;--amber-s:#FBF2DF;--blue:#2F5D8C;--blue-s:#E7EEF6;"
        "--card:#FFFDF8;--stamp:#C9A96B}")

hero = """<!DOCTYPE html><html lang="ru"><head><meta charset="utf-8">
%s
<style>
%s
*{margin:0;box-sizing:border-box}html,body{width:1200px;height:630px}
.card{width:1200px;height:630px;background:radial-gradient(1050px 660px at 14%% 12%%, #fff 0%%, var(--cream) 52%%, var(--cream-2) 100%%);position:relative;overflow:hidden;font-family:'Inter',sans-serif;padding:52px 46px 0 72px;display:flex;justify-content:space-between}
.card:before{content:"";position:absolute;left:0;top:0;bottom:0;width:12px;background:var(--brick)}
.txt{flex:0 0 492px;padding-top:4px}
.eyebrow{color:var(--brick);font-weight:700;font-size:18px;letter-spacing:.19em;text-transform:uppercase;margin-bottom:13px}
h1{font-family:'Cormorant Garamond',serif;font-weight:600;font-size:41px;line-height:1.07;color:var(--ink);letter-spacing:-.4px}
h1 i{font-style:italic;color:var(--brick)}
.sub{font-size:18px;color:var(--ink-2);line-height:1.42;max-width:30ch;margin-top:16px}
.note{display:inline-block;margin-top:20px;background:var(--surface);border:1px solid var(--hair);border-left:4px solid var(--brick);border-radius:13px;padding:13px 19px;font-size:15.5px;color:var(--ink-2);line-height:1.36;max-width:32ch}
.note b{color:var(--ink)}

/* открытка */
.scene{flex:0 0 560px;position:relative;height:482px;display:flex;align-items:flex-start;justify-content:center;padding-top:52px}
.post{width:470px;height:306px;background:var(--card);border:1px solid #E3DACA;border-radius:8px;box-shadow:0 18px 36px rgba(44,36,32,.18);transform:rotate(-2deg);padding:26px 30px;position:relative;display:flex;flex-direction:column;justify-content:center}
.stamp{position:absolute;right:26px;top:24px;width:84px;height:98px;border:2px dashed #D6C6A6;border-radius:5px;background:#FBF4E6;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:5px}
.stamp .h{font-family:'Noto Serif SC',serif;font-size:30px;color:var(--stamp)}
.stamp .n{font-size:12px;color:#A79468;letter-spacing:.1em}
.line{position:absolute;right:26px;top:140px;width:84px;border-top:1px solid #E3DACA}
.han{font-family:'Noto Serif SC',serif;font-size:76px;color:var(--ink);line-height:1.08;letter-spacing:4px}
.py{font-size:21px;color:var(--brick);font-style:italic;margin-top:10px}
.ru{font-size:18px;color:var(--ink-2);margin-top:7px}
.rules{position:absolute;left:30px;right:150px;bottom:26px;display:flex;flex-direction:column;gap:9px}
.rules i{display:block;border-top:1px solid #EDE4D4}
.cap{position:absolute;left:0;right:0;bottom:4px;text-align:center;font-size:15.5px;color:var(--ink-2)}
.cap b{color:var(--ink)}
.brand{position:absolute;left:72px;bottom:28px;display:flex;align-items:center;gap:11px;color:var(--ink)}
.brand b{font-family:'Cormorant Garamond',serif;font-weight:700;font-size:26px}
.brand .bdot{width:10px;height:10px;border-radius:50%%;background:var(--brick)}
.brand span{color:var(--taupe);font-size:16px}
</style></head><body>
<div class="card">
  <div class="txt">
    <div class="eyebrow">Фраза целиком</div>
    <h1>«Я тебя люблю» <i>по-китайски</i></h1>
    <div class="sub">Три знака, три слога и одно слово, которое в китайском весит больше, чем кажется</div>
    <div class="note"><b>Чаще эту фразу пишут, чем произносят</b> — в сообщении, в открытке, числом 520</div>
  </div>
  <div class="scene">
    <div class="post">
      <div class="stamp"><span class="h">爱</span><span class="n">520</span></div>
      <div class="line"></div>
      <div class="han">我爱你</div>
      <div class="py">wǒ ài nǐ</div>
      <div class="ru">я тебя люблю</div>
      <div class="rules"><i></i><i></i></div>
    </div>
    <div class="cap">Дословно — <b>«я люблю ты»</b>: порядок слов прямой, как в русском</div>
  </div>
  <div class="brand"><span class="bdot"></span><b>Kitai School</b><span>&middot; kitai-school.ru</span></div>
</div>
</body></html>""" % (FONTS, VARS)

open(S + "lv-hero.html", "w", encoding="utf-8").write(hero)

# -------------------------------------------------------------- инфографика
# третий тон — ныряющая линия, четвёртый — падающая
T3 = ('<svg viewBox="0 0 160 70" width="160" height="70">'
      '<path d="M8 16 C 44 16, 58 56, 80 56 C 102 56, 120 30, 152 12" fill="none" '
      'stroke="#A41E3A" stroke-width="5" stroke-linecap="round"/></svg>')
T4 = ('<svg viewBox="0 0 160 70" width="160" height="70">'
      '<path d="M12 12 L 148 58" fill="none" stroke="#2F5D8C" stroke-width="5" '
      'stroke-linecap="round"/></svg>')

SYL = [
    ("我", "wǒ", "третий тон", T3, "голос ныряет вниз и чуть поднимается"),
    ("爱", "ài", "четвёртый тон", T4, "резко вниз, будто отрубаете"),
    ("你", "nǐ", "третий тон", T3, "снова ныряет; в конце фразы звучит полностью"),
]

cards = "\n".join(
    '<div class="syl"><div class="h">%s</div><div class="p">%s</div>'
    '<div class="t">%s</div><div class="svg">%s</div><div class="d">%s</div></div>' % s
    for s in SYL)

info = """<!DOCTYPE html><html lang="ru"><head><meta charset="utf-8">
%s
<style>
%s
*{margin:0;box-sizing:border-box}html,body{width:1200px;height:HGTpx}
.wrap{width:1200px;height:HGTpx;background:linear-gradient(180deg,#fff 0%%,var(--cream) 46%%,var(--cream-2) 100%%);font-family:'Inter',sans-serif;padding:32px 46px 32px;display:flex;flex-direction:column}
.top{display:flex;align-items:flex-end;justify-content:space-between;gap:30px;margin-bottom:22px}
.eyebrow{color:var(--brick);font-weight:700;font-size:14.5px;letter-spacing:.17em;text-transform:uppercase;margin-bottom:7px}
h2{font-family:'Cormorant Garamond',serif;font-weight:600;font-size:40px;line-height:1.07;color:var(--ink);letter-spacing:-.3px}
h2 i{font-style:italic;color:var(--brick)}
.hint{flex:0 0 392px;background:var(--surface);border:1px solid var(--hair);border-left:4px solid var(--brick);border-radius:12px;padding:12px 17px;font-size:14.5px;color:var(--ink-2);line-height:1.36}
.hint b{color:var(--ink)}

.row{display:flex;gap:22px}
.syl{flex:1 1 0;background:var(--surface);border:1px solid var(--hair);border-radius:16px;padding:20px 18px 18px;box-shadow:0 5px 14px rgba(44,36,32,.05);display:flex;flex-direction:column;align-items:center;text-align:center}
.syl .h{font-family:'Noto Serif SC',serif;font-size:62px;color:var(--ink);line-height:1}
.syl .p{font-size:19px;color:var(--brick);font-style:italic;margin-top:6px}
.syl .t{font-size:14px;color:var(--taupe);margin-top:4px;letter-spacing:.04em}
.syl .svg{margin-top:10px}
.syl .d{font-size:14.5px;color:var(--ink-2);line-height:1.36;margin-top:8px;max-width:24ch}

.under{margin-top:18px;background:var(--blue-s);border:1px solid var(--blue);border-radius:14px;padding:13px 21px;font-size:15px;color:var(--ink);line-height:1.38}
.under b{color:var(--blue)}

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
      <div class="eyebrow">Три слога</div>
      <h2>Как звучит <i>我爱你</i></h2>
    </div>
    <div class="hint">Линии показывают <b>движение голоса</b>, а не громкость: тон — это высота, и меняется она внутри одного слога.</div>
  </div>

  <div class="row">
%s
  </div>

  <div class="under">Третий тон подряд два раза меняется на второй — но <b>здесь этого не происходит</b>: между 我 и 你 стоит 爱 четвёртого тона.</div>

  <div class="foot">
    <div class="msg">Проверить себя просто: <b>запишите фразу на диктофон</b> и сравните с речью носителя</div>
    <div class="brand"><span class="dot2"></span><b>Kitai School</b><span>&middot; kitai-school.ru</span></div>
  </div>
</div>
</body></html>""" % (FONTS, VARS, cards)

info = info.replace("HGT", "600")
open(S + "lv-info.html", "w", encoding="utf-8").write(info)
print("ok")
