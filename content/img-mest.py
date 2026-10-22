# -*- coding: utf-8 -*-
# Картинки к статье «Местоимения в китайском языке»
# Обложка    — три фигурки на поле: 我, 你, 他
# Инфографика — штамп 们: печать превращает местоимение в форму множественного числа
S = "/tmp/claude-0/-home-user-Kitai-Shool/a463bfca-82a9-56fd-ae09-42a7257ff999/scratchpad/"

FONTS = ("<link href=\"https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,600;0,700;1,600"
         "&family=Inter:wght@400;500;600;700&family=Noto+Serif+SC:wght@600;700&display=swap\" rel=\"stylesheet\">")
VARS = (":root{--brick:#A41E3A;--brick-d:#841630;--brick-soft:#F7E6EB;--ink:#2C2420;--ink-2:#5A4F45;"
        "--taupe:#8B7D6B;--cream:#FAF7F2;--cream-2:#F3EDE3;--hair:#EAE3D8;--surface:#fff;"
        "--p1:#A41E3A;--p1d:#7C1430;--p2:#2F5D8C;--p2d:#224566;--p3:#1E7A46;--p3d:#155936;"
        "--board:#EFE7D9;--stamp:#C3122F}")

PAWNS = [("我", "wǒ", "я", "p1"), ("你", "nǐ", "ты", "p2"), ("他", "tā", "он", "p3")]

pawns = "\n".join(
    '<div class="pawn %s"><div class="fig"><span class="head"></span><span class="body"></span></div>'
    '<div class="han">%s</div><div class="py">%s</div><div class="ru">%s</div></div>'
    % (cls, han, py, ru) for han, py, ru, cls in PAWNS)

hero = """<!DOCTYPE html><html lang="ru"><head><meta charset="utf-8">
%s
<style>
%s
*{margin:0;box-sizing:border-box}html,body{width:1200px;height:630px}
.card{width:1200px;height:630px;background:radial-gradient(1050px 660px at 14%% 12%%, #fff 0%%, var(--cream) 52%%, var(--cream-2) 100%%);position:relative;overflow:hidden;font-family:'Inter',sans-serif;padding:52px 46px 0 72px;display:flex;justify-content:space-between}
.card:before{content:"";position:absolute;left:0;top:0;bottom:0;width:12px;background:var(--brick)}
.txt{flex:0 0 470px;padding-top:4px}
.eyebrow{color:var(--brick);font-weight:700;font-size:18px;letter-spacing:.19em;text-transform:uppercase;margin-bottom:13px}
h1{font-family:'Cormorant Garamond',serif;font-weight:600;font-size:45px;line-height:1.07;color:var(--ink);letter-spacing:-.4px}
h1 i{font-style:italic;color:var(--brick)}
.sub{font-size:18px;color:var(--ink-2);line-height:1.42;max-width:30ch;margin-top:16px}
.note{display:inline-block;margin-top:22px;background:var(--surface);border:1px solid var(--hair);border-left:4px solid var(--brick);border-radius:13px;padding:13px 19px;font-size:15.5px;color:var(--ink-2);line-height:1.36;max-width:33ch}
.note b{color:var(--ink)}

/* три фигурки на поле */
.scene{flex:0 0 540px;position:relative;padding-top:60px;display:flex;flex-direction:column;align-items:center}
.board{width:510px;height:286px;border-radius:18px;background:linear-gradient(180deg,#fff,var(--board));border:1px solid var(--hair);box-shadow:0 16px 30px rgba(44,36,32,.12);display:flex;align-items:flex-end;justify-content:space-around;padding:0 24px 24px;position:relative;overflow:hidden}
.board:before{content:"";position:absolute;left:0;right:0;bottom:84px;height:1px;background:var(--hair)}
.pawn{display:flex;flex-direction:column;align-items:center;position:relative;z-index:1}
.fig{display:flex;flex-direction:column;align-items:center;margin-bottom:12px}
.head{display:block;width:34px;height:34px;border-radius:50%%;margin-bottom:-5px}
.body{display:block;width:0;height:0;border-left:30px solid transparent;border-right:30px solid transparent;border-bottom:62px solid #000}
.p1 .head{background:var(--p1)}.p1 .body{border-bottom-color:var(--p1)}
.p2 .head{background:var(--p2)}.p2 .body{border-bottom-color:var(--p2)}
.p3 .head{background:var(--p3)}.p3 .body{border-bottom-color:var(--p3)}
.pawn .han{font-family:'Noto Serif SC',serif;font-size:40px;color:var(--ink);line-height:1.1}
.pawn .py{font-size:16px;color:var(--ink-2);font-style:italic}
.pawn .ru{font-size:14.5px;color:var(--taupe)}
.cap{margin-top:24px;text-align:center;font-size:16.5px;color:var(--ink-2);line-height:1.42;max-width:40ch}
.cap b{color:var(--ink)}
.brand{position:absolute;left:72px;bottom:28px;display:flex;align-items:center;gap:11px;color:var(--ink)}
.brand b{font-family:'Cormorant Garamond',serif;font-weight:700;font-size:26px}
.brand .bdot{width:10px;height:10px;border-radius:50%%;background:var(--brick)}
.brand span{color:var(--taupe);font-size:16px}
</style></head><body>
<div class="card">
  <div class="txt">
    <div class="eyebrow">Грамматика</div>
    <h1>Местоимения <i>в китайском языке</i></h1>
    <div class="sub">Форма одна на все роли: падежей здесь нет</div>
    <div class="note"><b>Множественное число — один суффикс 们:</b> 我 → 我们, 你 → 你们, 他 → 他们</div>
  </div>
  <div class="scene">
    <div class="board">
%s
    </div>
    <div class="cap">Три стороны разговора — и <b>ни одна из них не меняет форму</b></div>
  </div>
  <div class="brand"><span class="bdot"></span><b>Kitai School</b><span>&middot; kitai-school.ru</span></div>
</div>
</body></html>""" % (FONTS, VARS, pawns)

open(S + "me-hero.html", "w", encoding="utf-8").write(hero)

# -------------------------------------------------------------- инфографика
ROWS = [
    ("我", "wǒ", "я", "我们", "wǒmen", "мы"),
    ("你", "nǐ", "ты", "你们", "nǐmen", "вы"),
    ("他", "tā", "он", "他们", "tāmen", "они"),
]

rows = "\n".join(
    '<div class="r"><div class="one"><span class="han">%s</span><span class="t"><i>%s</i>%s</span></div>'
    '<div class="stamp"><span class="han">们</span></div>'
    '<div class="one res"><span class="han">%s</span><span class="t"><i>%s</i>%s</span></div></div>'
    % r for r in ROWS)

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
.hint{flex:0 0 362px;background:var(--surface);border:1px solid var(--hair);border-left:4px solid var(--brick);border-radius:12px;padding:12px 17px;font-size:14.5px;color:var(--ink-2);line-height:1.36}
.hint b{color:var(--ink)}

.main{display:flex;gap:26px;align-items:stretch}
.rows{flex:1 1 auto;display:flex;flex-direction:column;gap:14px}
.r{display:flex;align-items:center;gap:20px;background:var(--surface);border:1px solid var(--hair);border-radius:15px;padding:12px 22px;box-shadow:0 4px 12px rgba(44,36,32,.05)}
.one{display:flex;align-items:baseline;gap:13px;flex:0 0 212px}
.one .han{font-family:'Noto Serif SC',serif;font-size:38px;color:var(--ink);line-height:1.1}
.one .t{font-size:14.5px;color:var(--ink-2);line-height:1.3}
.one .t i{display:block;color:var(--taupe);font-size:14px}
.one.res .han{color:var(--brick-d)}
.stamp{flex:0 0 86px;height:86px;border-radius:50%%;border:3px solid var(--stamp);display:flex;align-items:center;justify-content:center;transform:rotate(-8deg);box-shadow:0 3px 9px rgba(195,18,47,.17)}
.stamp .han{font-family:'Noto Serif SC',serif;font-size:42px;color:var(--stamp);line-height:1}

.side{flex:0 0 330px;background:var(--surface);border:1px solid var(--hair);border-radius:15px;padding:17px 20px;box-shadow:0 4px 12px rgba(44,36,32,.05)}
.side b.h{display:block;font-size:15.5px;color:var(--ink);margin-bottom:11px}
.side .no{display:flex;gap:11px;align-items:flex-start;margin-bottom:12px}
.side .x{flex:0 0 22px;height:22px;border-radius:50%%;background:var(--brick-soft);color:var(--brick-d);font-size:14px;font-weight:700;display:flex;align-items:center;justify-content:center;margin-top:2px}
.side .no div{font-size:14px;color:var(--ink-2);line-height:1.34}
.side .no div .han{font-family:'Noto Serif SC',serif;font-size:16px;color:var(--ink)}
.side .ok{background:var(--cream-2);border-radius:11px;padding:11px 13px;font-size:13.5px;color:var(--ink-2);line-height:1.34}

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
      <div class="eyebrow">Множественное число</div>
      <h2>Один суффикс <i>на все три формы</i></h2>
    </div>
    <div class="hint">Местоимение не меняется: <b>们 просто добавляется справа</b>. Никаких окончаний и чередований.</div>
  </div>

  <div class="main">
    <div class="rows">
%s
    </div>
    <div class="side">
      <b class="h">Куда 们 не ставят</b>
      <div class="no"><span class="x">×</span><div>После числительного: <span class="han">三个朋友</span>, а не 三个朋友们</div></div>
      <div class="no"><span class="x">×</span><div>К предметам: <span class="han">书</span> во множественном числе остаётся 书</div></div>
      <div class="no"><span class="x">×</span><div>Со словами количества: <span class="han">几个朋友</span>, а не 几个朋友们</div></div>
      <div class="ok">们 присоединяется к людям: 朋友们, 老师们, 同学们 — обращение к группе</div>
    </div>
  </div>

  <div class="foot">
    <div class="msg">Выучили три местоимения — <b>значит, выучили и шесть</b></div>
    <div class="brand"><span class="dot2"></span><b>Kitai School</b><span>&middot; kitai-school.ru</span></div>
  </div>
</div>
</body></html>""" % (FONTS, VARS, rows)

info = info.replace("HGT", "560")
open(S + "me-info.html", "w", encoding="utf-8").write(info)
print("ok")
