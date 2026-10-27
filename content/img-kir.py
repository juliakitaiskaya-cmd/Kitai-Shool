# -*- coding: utf-8 -*-
# Картинки к статье «Китайские слова русскими буквами»
# Обложка    — чёткое и размытое: пиньинь против кириллицы
# Инфографика — воронка: что не проходит в русскую запись
S = "/tmp/claude-0/-home-user-Kitai-Shool/a463bfca-82a9-56fd-ae09-42a7257ff999/scratchpad/"

FONTS = ("<link href=\"https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,600;0,700;1,600"
         "&family=Inter:wght@400;500;600;700&family=Noto+Serif+SC:wght@600;700&display=swap\" rel=\"stylesheet\">")
VARS = (":root{--brick:#A41E3A;--brick-d:#841630;--brick-soft:#F7E6EB;--ink:#2C2420;--ink-2:#5A4F45;"
        "--taupe:#8B7D6B;--cream:#FAF7F2;--cream-2:#F3EDE3;--hair:#EAE3D8;--surface:#fff;"
        "--good:#1E7A46;--good-s:#E3F6E9;--warn:#C08A2E;--warn-s:#FBF2DF;--funnel:#E5DED1}")

hero = """<!DOCTYPE html><html lang="ru"><head><meta charset="utf-8">
%s
<style>
%s
*{margin:0;box-sizing:border-box}html,body{width:1200px;height:630px}
.card{width:1200px;height:630px;background:radial-gradient(1050px 660px at 14%% 12%%, #fff 0%%, var(--cream) 52%%, var(--cream-2) 100%%);position:relative;overflow:hidden;font-family:'Inter',sans-serif;padding:52px 46px 0 72px;display:flex;justify-content:space-between}
.card:before{content:"";position:absolute;left:0;top:0;bottom:0;width:12px;background:var(--brick)}
.txt{flex:0 0 480px;padding-top:4px}
.eyebrow{color:var(--brick);font-weight:700;font-size:18px;letter-spacing:.19em;text-transform:uppercase;margin-bottom:13px}
h1{font-family:'Cormorant Garamond',serif;font-weight:600;font-size:44px;line-height:1.08;color:var(--ink);letter-spacing:-.4px}
h1 i{font-style:italic;color:var(--brick)}
.sub{font-size:18px;color:var(--ink-2);line-height:1.42;max-width:31ch;margin-top:16px}
.tip{display:inline-block;margin-top:22px;background:var(--surface);border:1px solid var(--hair);border-left:4px solid var(--brick);border-radius:13px;padding:13px 19px;font-size:15.5px;color:var(--ink-2);line-height:1.36;max-width:34ch}
.tip b{color:var(--ink)}

/* чёткое и размытое */
.scene{flex:0 0 530px;padding-top:62px;display:flex;flex-direction:column;gap:20px}
.box{background:var(--surface);border:1px solid var(--hair);border-radius:16px;padding:22px 26px;box-shadow:0 8px 18px rgba(44,36,32,.07);position:relative}
.box .lbl{position:absolute;right:20px;top:-11px;font-size:12.5px;font-weight:700;letter-spacing:.1em;text-transform:uppercase;padding:4px 11px;border-radius:20px}
.box.ok .lbl{background:var(--good-s);color:var(--good);border:1px solid var(--good)}
.box.no .lbl{background:var(--warn-s);color:var(--warn);border:1px solid var(--warn)}
.han{font-family:'Noto Serif SC',serif;font-size:46px;color:var(--ink);line-height:1.1}
.py{font-size:30px;color:var(--brick-d);font-weight:600;margin-top:6px;letter-spacing:.01em}
.cyr{font-size:30px;color:var(--ink);font-weight:600;margin-top:6px;filter:blur(2.4px)}
.note{font-size:14.5px;color:var(--ink-2);margin-top:10px;line-height:1.34}
.note b{color:var(--ink)}
.brand{position:absolute;left:72px;bottom:28px;display:flex;align-items:center;gap:11px;color:var(--ink)}
.brand b{font-family:'Cormorant Garamond',serif;font-weight:700;font-size:26px}
.brand .bdot{width:10px;height:10px;border-radius:50%%;background:var(--brick)}
.brand span{color:var(--taupe);font-size:16px}
</style></head><body>
<div class="card">
  <div class="txt">
    <div class="eyebrow">Произношение</div>
    <h1>Китайские слова <i>русскими буквами</i></h1>
    <div class="sub">Запись удобная, но часть звуков в неё просто не помещается</div>
    <div class="tip"><b>Тоны кириллица не передаёт вовсе,</b> а «цз» и «чж» читатель произносит по-русски</div>
  </div>
  <div class="scene">
    <div class="box ok">
      <span class="lbl">точно</span>
      <div class="han">谢谢</div>
      <div class="py">xièxie</div>
      <div class="note">Пиньинь — <b>система правил</b>: один слог читается одним способом</div>
    </div>
    <div class="box no">
      <span class="lbl">приблизительно</span>
      <div class="han">谢谢</div>
      <div class="cyr">сесе</div>
      <div class="note">Русская запись — <b>подсказка на глаз</b>: тон потерян, согласный не тот</div>
    </div>
  </div>
  <div class="brand"><span class="bdot"></span><b>Kitai School</b><span>&middot; kitai-school.ru</span></div>
</div>
</body></html>""" % (FONTS, VARS)

open(S + "kir-hero.html", "w", encoding="utf-8").write(hero)

# -------------------------------------------------------------- инфографика
TOP = [("zhōng", "中"), ("jiā", "家"), ("zì", "字"), ("qī", "七"), ("chī", "吃")]
BOT = [("чжун", ""), ("цзя", ""), ("цзы", ""), ("ци", ""), ("чи", "")]

top = "".join('<div class="s"><span class="p">%s</span><span class="h">%s</span></div>' % t
              for t in TOP)
bot = "".join('<div class="s c"><span class="p">%s</span></div>' % b[0] for b in BOT)

LOST = [
    ("Тоны", "их нет вовсе: «ма» — это и 妈, и 马, и ещё два слова"),
    ("Качество согласных", "«цз», «чж», «ж» читаются по-русски и звучат не как j, zh, r"),
    ("Звук ü", "записывается как «юй», но это другой звук"),
]

lost = "".join('<div class="l"><span class="x">—</span><div><b>%s</b>%s</div></div>' % l
               for l in LOST)

info = """<!DOCTYPE html><html lang="ru"><head><meta charset="utf-8">
%s
<style>
%s
*{margin:0;box-sizing:border-box}html,body{width:1200px;height:HGTpx}
.wrap{width:1200px;height:HGTpx;background:linear-gradient(180deg,#fff 0%%,var(--cream) 46%%,var(--cream-2) 100%%);font-family:'Inter',sans-serif;padding:32px 46px 30px;display:flex;flex-direction:column}
.top{display:flex;align-items:flex-end;justify-content:space-between;gap:30px;margin-bottom:18px}
.eyebrow{color:var(--brick);font-weight:700;font-size:14.5px;letter-spacing:.17em;text-transform:uppercase;margin-bottom:7px}
h2{font-family:'Cormorant Garamond',serif;font-weight:600;font-size:40px;line-height:1.07;color:var(--ink);letter-spacing:-.3px}
h2 i{font-style:italic;color:var(--brick)}
.hint{flex:0 0 364px;background:var(--surface);border:1px solid var(--hair);border-left:4px solid var(--brick);border-radius:12px;padding:12px 17px;font-size:14.5px;color:var(--ink-2);line-height:1.36}
.hint b{color:var(--ink)}

.main{display:flex;gap:28px;align-items:center}
.col{flex:1 1 auto;display:flex;flex-direction:column;align-items:center}
.row{display:flex;gap:11px}
.s{background:var(--surface);border:1px solid var(--hair);border-radius:12px;padding:10px 14px;text-align:center;min-width:104px;box-shadow:0 4px 10px rgba(44,36,32,.05)}
.s .p{display:block;font-size:21px;font-weight:600;color:var(--brick-d)}
.s .h{display:block;font-family:'Noto Serif SC',serif;font-size:17px;color:var(--ink-2);margin-top:2px}
.s.c .p{color:var(--ink)}
.funnel{width:430px;height:112px;background:linear-gradient(180deg,var(--funnel),#D5CCBB);clip-path:polygon(0 0, 100%% 0, 63%% 100%%, 37%% 100%%);margin:12px 0;position:relative}
.funnel span{position:absolute;left:0;right:0;top:34px;text-align:center;font-size:14.5px;color:var(--ink-2)}
.arrow{width:0;height:0;border-left:13px solid transparent;border-right:13px solid transparent;border-top:16px solid var(--taupe);margin:8px 0 12px}
.side{flex:0 0 358px;background:var(--surface);border:1px solid var(--hair);border-radius:15px;padding:17px 20px;box-shadow:0 5px 14px rgba(44,36,32,.06)}
.side b.h{display:block;font-size:15.5px;color:var(--ink);margin-bottom:12px}
.l{display:flex;gap:11px;align-items:flex-start;margin-bottom:12px}
.l .x{flex:0 0 22px;height:22px;border-radius:50%%;background:var(--brick-soft);color:var(--brick-d);font-size:15px;font-weight:700;display:flex;align-items:center;justify-content:center;margin-top:2px}
.l div{font-size:14px;color:var(--ink-2);line-height:1.33}
.l div b{display:block;color:var(--ink);font-size:14.5px}

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
      <div class="eyebrow">Что теряется</div>
      <h2>Через русскую запись <i>проходит не всё</i></h2>
    </div>
    <div class="hint">Кириллица решает свою задачу — <b>записать слово в русском тексте</b>. Произносить по ней — другая задача, и для неё она не предназначена.</div>
  </div>

  <div class="main">
    <div class="col">
      <div class="row">%s</div>
      <div class="funnel"><span>русская запись</span></div>
      <div class="arrow"></div>
      <div class="row">%s</div>
    </div>
    <div class="side">
      <b class="h">Застряло в горловине</b>
%s
    </div>
  </div>

  <div class="foot">
    <div class="msg">Пользоваться можно — <b>но как подсказкой, а не как образцом</b></div>
    <div class="brand"><span class="dot2"></span><b>Kitai School</b><span>&middot; kitai-school.ru</span></div>
  </div>
</div>
</body></html>""" % (FONTS, VARS, top, bot, lost)

info = info.replace("HGT", "600")
open(S + "kir-info.html", "w", encoding="utf-8").write(info)
print("ok")
