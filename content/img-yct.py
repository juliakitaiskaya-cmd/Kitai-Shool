# -*- coding: utf-8 -*-
# Картинки к статье «Сдать YCT: лексика и задания»
# Обложка    — магнитная доска: магниты-слова, один упал
# Инфографика — пары знаков «найди отличие»
S = "/tmp/claude-0/-home-user-Kitai-Shool/a463bfca-82a9-56fd-ae09-42a7257ff999/scratchpad/"

FONTS = ("<link href=\"https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,600;0,700;1,600"
         "&family=Inter:wght@400;500;600;700&family=Noto+Serif+SC:wght@600;700&display=swap\" rel=\"stylesheet\">")
VARS = (":root{--brick:#A41E3A;--brick-d:#841630;--brick-soft:#F7E6EB;--ink:#2C2420;--ink-2:#5A4F45;"
        "--taupe:#8B7D6B;--cream:#FAF7F2;--cream-2:#F3EDE3;--hair:#EAE3D8;--surface:#fff;"
        "--steel:#E8EBEE;--steel-2:#D3D9DF;--m1:#F2C14E;--m2:#6FB98F;--m3:#E98074;--m4:#7FA7D4;"
        "--green:#1E7A46}")

MAGS = [("我", "wǒ", "я", "m1", "-4deg", "26px", "26px"),
        ("你", "nǐ", "ты", "m2", "3deg", "214px", "16px"),
        ("好", "hǎo", "хорошо", "m3", "-2deg", "40px", "168px"),
        ("不", "bù", "не", "m4", "14deg", "236px", "186px")]

mags = "\n".join(
    '<div class="mag %s" style="transform:rotate(%s);left:%s;top:%s">'
    '<span class="han">%s</span><span class="py">%s</span><span class="ru">%s</span></div>'
    % (cls, rot, left, top, han, py, ru) for han, py, ru, cls, rot, left, top in MAGS)

hero = """<!DOCTYPE html><html lang="ru"><head><meta charset="utf-8">
%s
<style>
%s
*{margin:0;box-sizing:border-box}html,body{width:1200px;height:630px}
.card{width:1200px;height:630px;background:radial-gradient(1050px 660px at 14%% 12%%, #fff 0%%, var(--cream) 52%%, var(--cream-2) 100%%);position:relative;overflow:hidden;font-family:'Inter',sans-serif;padding:52px 46px 0 72px;display:flex;justify-content:space-between}
.card:before{content:"";position:absolute;left:0;top:0;bottom:0;width:12px;background:var(--brick)}
.txt{flex:0 0 486px;padding-top:4px}
.eyebrow{color:var(--brick);font-weight:700;font-size:18px;letter-spacing:.19em;text-transform:uppercase;margin-bottom:13px}
h1{font-family:'Cormorant Garamond',serif;font-weight:600;font-size:45px;line-height:1.07;color:var(--ink);letter-spacing:-.4px}
h1 i{font-style:italic;color:var(--brick)}
.sub{font-size:18px;color:var(--ink-2);line-height:1.42;max-width:31ch;margin-top:16px}
.tip{display:inline-block;margin-top:22px;background:var(--surface);border:1px solid var(--hair);border-left:4px solid var(--brick);border-radius:13px;padding:13px 19px;font-size:15.5px;color:var(--ink-2);line-height:1.36;max-width:34ch}
.tip b{color:var(--ink)}

/* магнитная доска */
.scene{flex:0 0 520px;padding-top:40px}
.board{position:relative;width:470px;height:390px;border-radius:16px;background:linear-gradient(160deg,var(--steel),var(--steel-2));box-shadow:inset 0 1px 0 rgba(255,255,255,.7), 0 14px 28px rgba(44,36,32,.16);border:1px solid #CBD2D9}
.mag{position:absolute;width:184px;height:150px;border-radius:10px;padding:16px 16px 14px;display:flex;flex-direction:column;justify-content:center;gap:3px;box-shadow:0 6px 13px rgba(44,36,32,.2), inset 0 1px 0 rgba(255,255,255,.5)}
.mag.m1{background:var(--m1)}.mag.m2{background:var(--m2)}
.mag.m3{background:var(--m3)}.mag.m4{background:var(--m4)}
.mag .han{font-family:'Noto Serif SC',serif;font-size:46px;color:#2C2420;line-height:1.05}
.mag .py{font-size:16px;color:#3B332C;font-style:italic}
.mag .ru{font-size:14.5px;color:#3B332C}
.cap{margin-top:18px;width:470px;text-align:center;font-size:16.5px;color:var(--ink-2);line-height:1.42}
.cap b{color:var(--ink)}
.brand{position:absolute;left:72px;bottom:28px;display:flex;align-items:center;gap:11px;color:var(--ink)}
.brand b{font-family:'Cormorant Garamond',serif;font-weight:700;font-size:26px}
.brand .bdot{width:10px;height:10px;border-radius:50%%;background:var(--brick)}
.brand span{color:var(--taupe);font-size:16px}
</style></head><body>
<div class="card">
  <div class="txt">
    <div class="eyebrow">Детский экзамен</div>
    <h1>Сдать YCT: <i>лексика и задания</i></h1>
    <div class="sub">Экзамен проверяет не объём словаря, а умение узнать знакомое слово</div>
    <div class="tip"><b>Дети путают не слова, а начертания:</b> 日 и 目, 千 и 干 различаются одной чертой</div>
  </div>
  <div class="scene">
    <div class="board">
%s
    </div>
    <div class="cap">Слова, которые ребёнок <b>узнаёт сразу</b>, — основа всего экзамена</div>
  </div>
  <div class="brand"><span class="bdot"></span><b>Kitai School</b><span>&middot; kitai-school.ru</span></div>
</div>
</body></html>""" % (FONTS, VARS, mags)

open(S + "yc-hero.html", "w", encoding="utf-8").write(hero)

# -------------------------------------------------------------- инфографика
PAIRS = [
    ("日", "rì", "солнце, день", "目", "mù", "глаз", "внутри одна черта против двух"),
    ("人", "rén", "человек", "入", "rù", "входить", "у 人 верх сходится в точку"),
    ("千", "qiān", "тысяча", "干", "gān", "сухой", "сверху откидная против прямой"),
    ("木", "mù", "дерево", "本", "běn", "корень, книга", "у 本 добавлена черта внизу"),
    ("大", "dà", "большой", "太", "tài", "слишком", "у 太 добавлена точка"),
]

pairs = "\n".join(
    '<div class="pair">'
    '<div class="one"><span class="han">%s</span><span class="py">%s</span><span class="ru">%s</span></div>'
    '<div class="vs">≠</div>'
    '<div class="one"><span class="han">%s</span><span class="py">%s</span><span class="ru">%s</span></div>'
    '<div class="diff">%s</div></div>' % p for p in PAIRS)

info = """<!DOCTYPE html><html lang="ru"><head><meta charset="utf-8">
%s
<style>
%s
*{margin:0;box-sizing:border-box}html,body{width:1200px;height:HGTpx}
.wrap{width:1200px;height:HGTpx;background:linear-gradient(180deg,#fff 0%%,var(--cream) 46%%,var(--cream-2) 100%%);font-family:'Inter',sans-serif;padding:32px 46px 30px;display:flex;flex-direction:column}
.top{display:flex;align-items:flex-end;justify-content:space-between;gap:30px;margin-bottom:22px}
.eyebrow{color:var(--brick);font-weight:700;font-size:14.5px;letter-spacing:.17em;text-transform:uppercase;margin-bottom:7px}
h2{font-family:'Cormorant Garamond',serif;font-weight:600;font-size:40px;line-height:1.07;color:var(--ink);letter-spacing:-.3px}
h2 i{font-style:italic;color:var(--brick)}
.hint{flex:0 0 366px;background:var(--surface);border:1px solid var(--hair);border-left:4px solid var(--brick);border-radius:12px;padding:12px 17px;font-size:14.5px;color:var(--ink-2);line-height:1.36}
.hint b{color:var(--ink)}

.rows{display:flex;gap:13px}
.pair{flex:1 1 0;background:var(--surface);border:1px solid var(--hair);border-radius:15px;padding:16px 12px 14px;box-shadow:0 5px 14px rgba(44,36,32,.06);display:flex;flex-direction:column;align-items:center;gap:6px}
.one{display:flex;flex-direction:column;align-items:center;line-height:1.1}
.one .han{font-family:'Noto Serif SC',serif;font-size:52px;color:var(--ink)}
.one .py{font-size:14.5px;color:var(--taupe);font-style:italic;margin-top:2px}
.one .ru{font-size:13.5px;color:var(--ink-2)}
.vs{font-size:19px;color:var(--brick);font-weight:700;margin:2px 0}
.diff{margin-top:9px;background:var(--brick-soft);border-radius:9px;padding:8px 10px;font-size:13px;color:var(--brick-d);text-align:center;line-height:1.3;width:100%%}

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
      <div class="eyebrow">Похожие знаки</div>
      <h2>Пять пар, <i>которые путают чаще всего</i></h2>
    </div>
    <div class="hint">В каждой паре разница — <b>одна черта</b>. Ребёнок путает не слова, а начертания: показывать нужно отличие.</div>
  </div>

  <div class="rows">
%s
  </div>

  <div class="foot">
    <div class="msg">Приём на каждый день: <b>писать пару рядом</b> и вслух называть, чем они различаются</div>
    <div class="brand"><span class="dot2"></span><b>Kitai School</b><span>&middot; kitai-school.ru</span></div>
  </div>
</div>
</body></html>""" % (FONTS, VARS, pairs)

info = info.replace("HGT", "520")
open(S + "yc-info.html", "w", encoding="utf-8").write(info)
print("ok, пар:", len(PAIRS))
