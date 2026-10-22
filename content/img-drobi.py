# -*- coding: utf-8 -*-
# Картинки к статье «Дроби в китайском языке»
# Обложка    — плитка шоколада: три дольки, одна отломана, над ней 三分之一
# Инфографика — зеркальный порядок чтения: числитель и знаменатель меняются местами
S = "/tmp/claude-0/-home-user-Kitai-Shool/a463bfca-82a9-56fd-ae09-42a7257ff999/scratchpad/"

FONTS = ("<link href=\"https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,600;0,700;1,600"
         "&family=Inter:wght@400;500;600;700&family=Noto+Serif+SC:wght@600;700&display=swap\" rel=\"stylesheet\">")
VARS = (":root{--brick:#A41E3A;--brick-d:#841630;--brick-soft:#F7E6EB;--ink:#2C2420;--ink-2:#5A4F45;"
        "--taupe:#8B7D6B;--cream:#FAF7F2;--cream-2:#F3EDE3;--hair:#EAE3D8;--surface:#fff;"
        "--choc:#5B3A26;--choc-2:#3E2619;--choc-l:#6E4832;--blue:#2F5D8C;--blue-s:#E7EEF6;"
        "--foil:#D9CFBC}")

# ------------------------------------------------------------------ обложка
hero = """<!DOCTYPE html><html lang="ru"><head><meta charset="utf-8">
%s
<style>
%s
*{margin:0;box-sizing:border-box}html,body{width:1200px;height:630px}
.card{width:1200px;height:630px;background:radial-gradient(1050px 660px at 14%% 12%%, #fff 0%%, var(--cream) 52%%, var(--cream-2) 100%%);position:relative;overflow:hidden;font-family:'Inter',sans-serif;padding:52px 46px 0 72px;display:flex;justify-content:space-between}
.card:before{content:"";position:absolute;left:0;top:0;bottom:0;width:12px;background:var(--brick)}
.txt{flex:0 0 492px;padding-top:4px}
.eyebrow{color:var(--brick);font-weight:700;font-size:18px;letter-spacing:.19em;text-transform:uppercase;margin-bottom:13px}
h1{font-family:'Cormorant Garamond',serif;font-weight:600;font-size:45px;line-height:1.07;color:var(--ink);letter-spacing:-.4px}
h1 i{font-style:italic;color:var(--brick)}
.sub{font-size:18px;color:var(--ink-2);line-height:1.42;max-width:31ch;margin-top:16px}
.note{display:inline-block;margin-top:22px;background:var(--surface);border:1px solid var(--hair);border-left:4px solid var(--brick);border-radius:13px;padding:13px 19px;font-size:15.5px;color:var(--ink-2);line-height:1.36;max-width:33ch}
.note b{color:var(--ink)}

/* плитка шоколада */
.scene{flex:0 0 520px;position:relative;padding-top:78px;display:flex;flex-direction:column;align-items:center}
.bar{display:flex;gap:7px;align-items:flex-start}
.pair{display:flex;gap:7px;padding:11px;border-radius:14px;background:linear-gradient(180deg,rgba(217,207,188,.55),rgba(217,207,188,.25));box-shadow:0 14px 26px rgba(44,36,32,.14)}
.sq{width:104px;height:124px;border-radius:9px;background:linear-gradient(150deg,var(--choc-l),var(--choc) 46%%,var(--choc-2));box-shadow:inset 0 2px 0 rgba(255,255,255,.14), inset 0 -3px 6px rgba(0,0,0,.35), 0 6px 12px rgba(44,36,32,.2);position:relative}
.sq:after{content:"";position:absolute;left:12px;right:12px;top:12px;bottom:12px;border:1px solid rgba(0,0,0,.22);border-radius:5px}
.one{margin-left:40px;transform:rotate(7deg)}
.one .sq{box-shadow:inset 0 2px 0 rgba(255,255,255,.16), inset 0 -3px 6px rgba(0,0,0,.35), 0 12px 20px rgba(44,36,32,.28)}
.tag{margin-top:26px;display:flex;align-items:center;gap:14px}
.tag .han{font-family:'Noto Serif SC',serif;font-size:42px;color:var(--ink);line-height:1}
.tag .eq{font-size:30px;color:var(--taupe)}
.tag .fr{display:flex;flex-direction:column;align-items:center;line-height:1;font-size:27px;color:var(--brick);font-weight:600}
.tag .fr span:first-child{padding-bottom:4px;border-bottom:2px solid var(--brick)}
.tag .fr span:last-child{padding-top:4px}
.cap{margin-top:18px;text-align:center;font-size:16.5px;color:var(--ink-2);line-height:1.42}
.cap b{color:var(--ink)}
.brand{position:absolute;left:72px;bottom:28px;display:flex;align-items:center;gap:11px;color:var(--ink)}
.brand b{font-family:'Cormorant Garamond',serif;font-weight:700;font-size:26px}
.brand .bdot{width:10px;height:10px;border-radius:50%%;background:var(--brick)}
.brand span{color:var(--taupe);font-size:16px}
</style></head><body>
<div class="card">
  <div class="txt">
    <div class="eyebrow">Числа</div>
    <h1>Дроби <i>в китайском языке</i></h1>
    <div class="sub">Сначала называют знаменатель, и только потом числитель</div>
    <div class="note"><b>三分之一 — дословно «из трёх частей одна».</b> На той же формуле строятся и проценты</div>
  </div>
  <div class="scene">
    <div class="bar">
      <div class="pair"><div class="sq"></div><div class="sq"></div></div>
      <div class="pair one"><div class="sq"></div></div>
    </div>
    <div class="tag">
      <span class="han">三分之一</span>
      <span class="eq">=</span>
      <span class="fr"><span>1</span><span>3</span></span>
    </div>
    <div class="cap">Три части, из них <b>одна</b> — порядок слов идёт от целого к части</div>
  </div>
  <div class="brand"><span class="bdot"></span><b>Kitai School</b><span>&middot; kitai-school.ru</span></div>
</div>
</body></html>""" % (FONTS, VARS)

open(S + "dr-hero.html", "w", encoding="utf-8").write(hero)

# -------------------------------------------------------------- инфографика
EX = [
    ("1/2", "二分之一", "èr fēn zhī yī"),
    ("1/4", "四分之一", "sì fēn zhī yī"),
    ("3/4", "四分之三", "sì fēn zhī sān"),
    ("50 %", "百分之五十", "bǎi fēn zhī wǔshí"),
]

ex_cards = "\n".join(
    '<div class="ex"><div class="ru">%s</div><div class="han">%s</div><div class="py">%s</div></div>'
    % e for e in EX)

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
.hint{flex:0 0 368px;background:var(--surface);border:1px solid var(--hair);border-left:4px solid var(--brick);border-radius:12px;padding:12px 17px;font-size:14.5px;color:var(--ink-2);line-height:1.36}
.hint b{color:var(--ink)}

.swap{background:var(--surface);border:1px solid var(--hair);border-radius:16px;padding:20px 26px 22px;box-shadow:0 6px 16px rgba(44,36,32,.06)}
.line{display:flex;align-items:center;gap:16px}
.who{flex:0 0 168px;font-size:15px;color:var(--taupe)}
.tok{display:flex;align-items:baseline;gap:12px}
.w{padding:8px 16px;border-radius:11px;font-size:27px;font-weight:600;line-height:1.15}
.w.num{background:var(--brick-soft);border:1px solid var(--brick);color:var(--brick-d)}
.w.den{background:var(--blue-s);border:1px solid var(--blue);color:var(--blue)}
.w.mid{background:var(--cream-2);border:1px solid var(--hair);color:var(--ink-2);font-size:24px}
.w .role{display:block;font-size:12.5px;font-weight:500;letter-spacing:.02em;opacity:.85;margin-top:3px}
.han{font-family:'Noto Serif SC',serif}
.cross{height:46px;position:relative;margin:4px 0 4px 184px;width:436px}
.cross i{position:absolute;height:2px;background:var(--taupe);opacity:.55;border-radius:2px}
.cross i.a{left:8px;top:22px;width:300px;transform:rotate(11deg)}
.cross i.b{left:108px;top:22px;width:300px;transform:rotate(-11deg)}
.cross b{position:absolute;right:-6px;top:7px;font-size:13px;color:var(--taupe);font-weight:500}

.swapin{display:flex;gap:26px;align-items:center}
.swapleft{flex:1 1 auto}
.gloss{flex:0 0 322px;display:flex;flex-direction:column;gap:11px;border-left:1px solid var(--hair);padding-left:24px}
.gloss .g{display:flex;align-items:center;gap:13px}
.gloss .gh{font-size:31px;color:var(--ink);line-height:1}
.gloss .gt{font-size:14px;color:var(--ink-2);line-height:1.3}
.gloss .gt b{display:block;color:var(--ink);font-size:14.5px}
.gloss .note2{display:block;background:var(--cream-2);border-radius:10px;padding:10px 13px;font-size:13.5px;color:var(--ink-2);line-height:1.33}
.exs{margin-top:20px;display:flex;gap:14px}
.ex{flex:1 1 0;background:var(--surface);border:1px solid var(--hair);border-radius:14px;padding:13px 16px;text-align:center;box-shadow:0 4px 11px rgba(44,36,32,.05)}
.ex .ru{font-size:19px;font-weight:600;color:var(--brick);margin-bottom:5px}
.ex .han{font-size:23px;color:var(--ink);line-height:1.2}
.ex .py{font-size:13.5px;color:var(--ink-2);margin-top:4px}

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
      <div class="eyebrow">Порядок слов</div>
      <h2>Числитель и знаменатель <i>меняются местами</i></h2>
    </div>
    <div class="hint">В русском дробь начинается с части, в китайском — <b>с целого</b>: сначала на сколько делим, потом сколько берём.</div>
  </div>

  <div class="swap">
    <div class="swapin">
    <div class="swapleft">
    <div class="line">
      <div class="who">Мы говорим</div>
      <div class="tok">
        <span class="w num">одна<span class="role">числитель</span></span>
        <span class="w den">третья<span class="role">знаменатель</span></span>
      </div>
    </div>
    <div class="cross"><i class="a"></i><i class="b"></i><b>порядок обратный</b></div>
    <div class="line">
      <div class="who">Китайцы говорят</div>
      <div class="tok">
        <span class="w den han">三<span class="role">знаменатель</span></span>
        <span class="w mid han">分之<span class="role">частей, из них</span></span>
        <span class="w num han">一<span class="role">числитель</span></span>
      </div>
    </div>
    </div>
    <div class="gloss">
      <div class="g"><span class="gh han">分</span><span class="gt"><b>fēn</b>делить, часть</span></div>
      <div class="g"><span class="gh han">之</span><span class="gt"><b>zhī</b>показатель «из», связывает целое и часть</span></div>
      <div class="g note2">Та же формула и у процентов: 百分之 — «из ста частей»</div>
    </div>
    </div>
  </div>

  <div class="exs">
%s
  </div>

  <div class="foot">
    <div class="msg">Читайте дробь с конца: <b>сначала нижнее число, потом верхнее</b></div>
    <div class="brand"><span class="dot2"></span><b>Kitai School</b><span>&middot; kitai-school.ru</span></div>
  </div>
</div>
</body></html>""" % (FONTS, VARS, ex_cards)

info = info.replace("HGT", "600")
open(S + "dr-info.html", "w", encoding="utf-8").write(info)
print("ok")
