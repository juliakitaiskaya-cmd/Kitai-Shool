# -*- coding: utf-8 -*-
# Картинки к статье «Китайская система счисления»
# Обложка    — счётные палочки: число 2016, выложенное палочками, пустое место на месте нуля
# Инфографика — одно число с двумя разметками: по три разряда и по четыре
S = "/tmp/claude-0/-home-user-Kitai-Shool/a463bfca-82a9-56fd-ae09-42a7257ff999/scratchpad/"

FONTS = ("<link href=\"https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,600;0,700;1,600"
         "&family=Inter:wght@400;500;600;700&family=Noto+Serif+SC:wght@600;700&display=swap\" rel=\"stylesheet\">")
VARS = (":root{--brick:#A41E3A;--brick-d:#841630;--brick-soft:#F7E6EB;--ink:#2C2420;--ink-2:#5A4F45;"
        "--taupe:#8B7D6B;--cream:#FAF7F2;--cream-2:#F3EDE3;--hair:#EAE3D8;--surface:#fff;"
        "--board:#3B332C;--board-2:#241E19;--rod:#E8DCC4;--rod-d:#C9B48A;--gold:#C9A961}")

# ------------------------------------------------------------------ обложка
# 2016: тысячи 2 — горизонтальные, сотни 0 — пусто, десятки 1 — горизонтальная,
# единицы 6 — верхняя горизонталь (пятёрка) и одна вертикальная палочка
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
.sub{font-size:18px;color:var(--ink-2);line-height:1.42;max-width:30ch;margin-top:16px}
.note{display:inline-block;margin-top:22px;background:var(--surface);border:1px solid var(--hair);border-left:4px solid var(--brick);border-radius:13px;padding:13px 19px;font-size:15.5px;color:var(--ink-2);line-height:1.36;max-width:32ch}
.note b{color:var(--ink)}

/* доска со счётными палочками */
.scene{flex:0 0 530px;position:relative;padding-top:66px}
.board{width:530px;height:300px;border-radius:16px;background:linear-gradient(160deg,var(--board),var(--board-2));box-shadow:0 20px 38px rgba(20,18,15,.38), inset 0 1px 0 rgba(255,255,255,.1);padding:26px 22px 18px;display:flex;align-items:flex-end;justify-content:space-around}
.col{flex:0 0 102px;height:208px;display:flex;flex-direction:column;align-items:center;justify-content:flex-end;gap:12px;position:relative}
.col+.col:before{content:"";position:absolute;left:-2px;top:14px;bottom:30px;width:1px;background:rgba(232,220,196,.14)}
.rods{height:150px;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:11px}
.rods.vert{flex-direction:row;align-items:flex-end;gap:10px}
.h{width:66px;height:9px;border-radius:5px;background:linear-gradient(180deg,var(--rod),var(--rod-d));box-shadow:0 2px 3px rgba(0,0,0,.4)}
.v{width:9px;height:66px;border-radius:5px;background:linear-gradient(90deg,var(--rod),var(--rod-d));box-shadow:0 2px 3px rgba(0,0,0,.4)}
.six{display:flex;flex-direction:column;align-items:center;gap:11px}
.empty{width:66px;height:66px;border:2px dashed rgba(232,220,196,.3);border-radius:9px}
.dig{color:var(--gold);font-size:19px;font-weight:600;letter-spacing:.04em}
.lab{color:#9E9284;font-size:13.5px;letter-spacing:.04em}
.cap{margin-top:22px;text-align:center;font-size:16.5px;color:var(--ink-2);line-height:1.42}
.cap b{color:var(--ink)}
.brand{position:absolute;left:72px;bottom:28px;display:flex;align-items:center;gap:11px;color:var(--ink)}
.brand b{font-family:'Cormorant Garamond',serif;font-weight:700;font-size:26px}
.brand .bdot{width:10px;height:10px;border-radius:50%%;background:var(--brick)}
.brand span{color:var(--taupe);font-size:16px}
</style></head><body>
<div class="card">
  <div class="txt">
    <div class="eyebrow">Числа</div>
    <h1>Китайская <i>система счисления</i></h1>
    <div class="sub">Десятичная и позиционная — такой же она была и до арабских цифр</div>
    <div class="note"><b>Счётными палочками выкладывали разряды:</b> соседние шли поперёк друг другу, а пустое место означало ноль</div>
  </div>
  <div class="scene">
    <div class="board">
      <div class="col"><div class="rods"><div class="h"></div><div class="h"></div></div><div class="dig">2</div><div class="lab">тысячи</div></div>
      <div class="col"><div class="rods"><div class="empty"></div></div><div class="dig">0</div><div class="lab">сотни</div></div>
      <div class="col"><div class="rods"><div class="h"></div></div><div class="dig">1</div><div class="lab">десятки</div></div>
      <div class="col"><div class="rods"><div class="six"><div class="h"></div><div class="v"></div></div></div><div class="dig">6</div><div class="lab">единицы</div></div>
    </div>
    <div class="cap">Так выглядит <b>2016</b>: верхняя палочка в последнем разряде означает пять</div>
  </div>
  <div class="brand"><span class="bdot"></span><b>Kitai School</b><span>&middot; kitai-school.ru</span></div>
</div>
</body></html>""" % (FONTS, VARS)

open(S + "sch-hero.html", "w", encoding="utf-8").write(hero)

# -------------------------------------------------------------- инфографика
DIGITS = "1234567890"

cells = "".join('<div class="d">%s</div>' % d for d in DIGITS)

info = """<!DOCTYPE html><html lang="ru"><head><meta charset="utf-8">
%s
<style>
%s
*{margin:0;box-sizing:border-box}html,body{width:1200px;height:HGTpx}
.wrap{width:1200px;height:HGTpx;background:linear-gradient(180deg,#fff 0%%,var(--cream) 46%%,var(--cream-2) 100%%);font-family:'Inter',sans-serif;padding:32px 46px 30px;display:flex;flex-direction:column}
.top{display:flex;align-items:flex-end;justify-content:space-between;gap:30px;margin-bottom:26px}
.eyebrow{color:var(--brick);font-weight:700;font-size:14.5px;letter-spacing:.17em;text-transform:uppercase;margin-bottom:7px}
h2{font-family:'Cormorant Garamond',serif;font-weight:600;font-size:40px;line-height:1.07;color:var(--ink);letter-spacing:-.3px}
h2 i{font-style:italic;color:var(--brick)}
.hint{flex:0 0 372px;background:var(--surface);border:1px solid var(--hair);border-left:4px solid var(--brick);border-radius:12px;padding:12px 17px;font-size:14.5px;color:var(--ink-2);line-height:1.36}
.hint b{color:var(--ink)}

.stage{position:relative;display:flex;flex-direction:column;align-items:center;gap:0}
.row{display:flex;gap:6px}
.d{width:84px;height:92px;display:flex;align-items:center;justify-content:center;background:var(--surface);border:1px solid var(--hair);border-radius:11px;font-size:44px;font-weight:600;color:var(--ink);box-shadow:0 4px 11px rgba(44,36,32,.06)}
.marks{display:flex;gap:6px;width:100%%;justify-content:center}
.g{border-radius:9px;padding:9px 0;text-align:center;font-size:14.5px;line-height:1.2}
.g b{display:block;font-size:16px}
.up .g{background:#EEF2F7;border:1px solid #D4DEEA;color:#3C5572;margin-bottom:12px}
.dn .g{background:var(--brick-soft);border:1px solid var(--brick);color:var(--brick-d);margin-top:12px}
.w1{width:84px}.w3{width:264px}.w4{width:354px}.w2{width:174px}

.read{margin-top:24px;background:var(--surface);border:1px solid var(--hair);border-radius:14px;padding:15px 22px;text-align:center}
.read .han{font-family:'Noto Serif SC',serif;font-size:27px;color:var(--ink);line-height:1.3}
.read .ru{font-size:15px;color:var(--ink-2);margin-top:5px}

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
      <div class="eyebrow">Разряды</div>
      <h2>Одно число, <i>две разметки</i></h2>
    </div>
    <div class="hint">Мы делим число <b>по три разряда</b>, китайская запись — <b>по четыре</b>. Отсюда и расхождение в переводе.</div>
  </div>

  <div class="stage">
    <div class="marks up">
      <div class="g w1"><b>1</b>млрд</div>
      <div class="g w3"><b>234</b>миллионы</div>
      <div class="g w3"><b>567</b>тысячи</div>
      <div class="g w3"><b>890</b>единицы</div>
    </div>
    <div class="row">%s</div>
    <div class="marks dn">
      <div class="g w2"><b>12 亿</b>亿 — сто миллионов</div>
      <div class="g w4"><b>3456 万</b>万 — десять тысяч</div>
      <div class="g w4"><b>7890</b>единицы</div>
    </div>
  </div>

  <div class="read">
    <div class="han">十二亿 三千四百五十六万 七千八百九十</div>
    <div class="ru">То же число по-китайски: 12 亿, 3456 万 и 7890</div>
  </div>

  <div class="foot">
    <div class="msg">Увидели 万 — <b>умножайте на десять тысяч</b>, и только потом переводите в привычные разряды</div>
    <div class="brand"><span class="dot2"></span><b>Kitai School</b><span>&middot; kitai-school.ru</span></div>
  </div>
</div>
</body></html>""" % (FONTS, VARS, cells)

info = info.replace("HGT", "560")
open(S + "sch-info.html", "w", encoding="utf-8").write(info)
print("ok")
