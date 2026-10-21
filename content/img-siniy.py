# -*- coding: utf-8 -*-
# Картинки к статье «Синий на китайском»
# Обложка    — бирка на ткани: 蓝 начиналось как название краски
# Инфографика — лист синьки: слова с 蓝, где цвет уже не про цвет
S = "/tmp/claude-0/-home-user-Kitai-Shool/a463bfca-82a9-56fd-ae09-42a7257ff999/scratchpad/"

FONTS = ("<link href=\"https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,600;0,700;1,600"
         "&family=Inter:wght@400;500;600;700&family=Noto+Serif+SC:wght@600;700&display=swap\" rel=\"stylesheet\">")
VARS = (":root{--brick:#A41E3A;--brick-d:#841630;--brick-soft:#F7E6EB;--ink:#2C2420;--ink-2:#5A4F45;"
        "--taupe:#8B7D6B;--cream:#FAF7F2;--cream-2:#F3EDE3;--hair:#EAE3D8;--surface:#fff;"
        "--green:#1E7A46;--green-s:#E3F6E9;--amber:#C08A2E;--amber-s:#FBF2DF;--blue:#2F5D8C;--blue-s:#E7EEF6;"
        "--indigo:#28457A;--indigo-2:#1B3157;--cloth:#35558C;--cloth-2:#27416E;--tag:#F6F1E6}")

hero = """<!DOCTYPE html><html lang="ru"><head><meta charset="utf-8">
%s
<style>
%s
*{margin:0;box-sizing:border-box}html,body{width:1200px;height:630px}
.card{width:1200px;height:630px;background:radial-gradient(1050px 660px at 14%% 12%%, #fff 0%%, var(--cream) 52%%, var(--cream-2) 100%%);position:relative;overflow:hidden;font-family:'Inter',sans-serif;padding:52px 46px 0 72px;display:flex;justify-content:space-between}
.card:before{content:"";position:absolute;left:0;top:0;bottom:0;width:12px;background:var(--brick)}
.txt{flex:0 0 506px;padding-top:4px}
.eyebrow{color:var(--brick);font-weight:700;font-size:18px;letter-spacing:.19em;text-transform:uppercase;margin-bottom:13px}
h1{font-family:'Cormorant Garamond',serif;font-weight:600;font-size:45px;line-height:1.07;color:var(--ink);letter-spacing:-.4px}
h1 i{font-style:italic;color:var(--brick)}
.sub{font-size:18px;color:var(--ink-2);line-height:1.42;max-width:32ch;margin-top:16px}
.note{display:inline-block;margin-top:22px;background:var(--surface);border:1px solid var(--hair);border-left:4px solid var(--brick);border-radius:13px;padding:13px 19px;font-size:15.5px;color:var(--ink-2);line-height:1.36;max-width:34ch}
.note b{color:var(--ink)}

/* ткань с биркой */
.scene{flex:0 0 520px;position:relative;height:482px;display:flex;align-items:flex-start;justify-content:center;padding-top:40px}
.cloth{width:398px;height:324px;border-radius:10px;background:linear-gradient(150deg,var(--cloth),var(--cloth-2));box-shadow:0 18px 34px rgba(26,40,70,.3);position:relative;overflow:hidden;transform:rotate(-1.5deg)}
.cloth:before{content:"";position:absolute;inset:0;background:repeating-linear-gradient(90deg,rgba(255,255,255,.05) 0 2px,transparent 2px 6px),repeating-linear-gradient(0deg,rgba(0,0,0,.07) 0 2px,transparent 2px 6px)}
.cloth:after{content:"";position:absolute;left:0;right:0;bottom:0;height:16px;background:repeating-linear-gradient(90deg,var(--cloth-2) 0 7px,transparent 7px 14px)}
.tag{position:absolute;right:16px;top:104px;width:186px;background:var(--tag);border:1px solid #E0D6C2;border-radius:10px;padding:18px 16px 16px;box-shadow:0 10px 22px rgba(44,36,32,.22);text-align:center;transform:rotate(4deg)}
.tag:before{content:"";position:absolute;left:50%%;top:-15px;margin-left:-7px;width:14px;height:14px;border-radius:50%%;border:2px solid #C9BCA2;background:#fff}
.tag .han{font-family:'Noto Serif SC',serif;font-size:62px;color:var(--indigo);line-height:1}
.tag .py{font-size:17px;color:var(--brick);font-style:italic;margin-top:5px}
.tag .ru{font-size:15px;color:var(--ink-2);margin-top:3px}
.tag .line{margin:11px 6px 0;border-top:1px dashed #D8CCB4}
.tag .add{font-size:13px;color:var(--taupe);margin-top:9px;line-height:1.35}
.cap{position:absolute;left:0;right:0;bottom:22px;text-align:center;font-size:16px;color:var(--ink-2);line-height:1.4}
.cap b{color:var(--ink)}
.brand{position:absolute;left:72px;bottom:28px;display:flex;align-items:center;gap:11px;color:var(--ink)}
.brand b{font-family:'Cormorant Garamond',serif;font-weight:700;font-size:26px}
.brand .bdot{width:10px;height:10px;border-radius:50%%;background:var(--brick)}
.brand span{color:var(--taupe);font-size:16px}
</style></head><body>
<div class="card">
  <div class="txt">
    <div class="eyebrow">Лексика</div>
    <h1>Синий <i>на китайском</i></h1>
    <div class="sub">Слов с 蓝 больше, чем кажется, и во многих цвет уже не главное</div>
    <div class="note"><b>蓝 начиналось не с цвета, а с краски:</b> так называли растение, которым красили ткань</div>
  </div>
  <div class="scene">
    <div class="cloth">
      <div class="tag">
        <div class="han">蓝</div>
        <div class="py">lán</div>
        <div class="ru">синий</div>
        <div class="line"></div>
        <div class="add">в речи чаще 蓝色 lánsè</div>
      </div>
    </div>
    <div class="cap">蓝图 — чертёж и <b>план</b>, 蓝领 — <b>рабочие профессии</b></div>
  </div>
  <div class="brand"><span class="bdot"></span><b>Kitai School</b><span>&middot; kitai-school.ru</span></div>
</div>
</body></html>""" % (FONTS, VARS)

open(S + "sn-hero.html", "w", encoding="utf-8").write(hero)

# -------------------------------------------------------------- инфографика
WORDS = [
    ("蓝图", "lántú", "чертёж; план действий", "белые линии по синему — так печатали чертежи"),
    ("蓝领", "lánlǐng", "рабочие специальности", "калька с английского blue collar"),
    ("蓝牙", "lányá", "Bluetooth", "название перенесено из английского целиком"),
    ("蓝海", "lánhǎi", "рынок без конкурентов", "из делового языка"),
]

rows = "\n".join(
    '<div class="row"><div class="w">%s</div><div class="p">%s</div>'
    '<div class="ru">%s</div><div class="nt">%s</div></div>' % w for w in WORDS)

info = """<!DOCTYPE html><html lang="ru"><head><meta charset="utf-8">
%s
<style>
%s
*{margin:0;box-sizing:border-box}html,body{width:1200px;height:HGTpx}
.wrap{width:1200px;height:HGTpx;background:linear-gradient(165deg,var(--indigo),var(--indigo-2));font-family:'Inter',sans-serif;padding:32px 46px 30px;display:flex;flex-direction:column;position:relative;overflow:hidden}
.grid{position:absolute;inset:0;background:repeating-linear-gradient(90deg,rgba(255,255,255,.07) 0 1px,transparent 1px 48px),repeating-linear-gradient(0deg,rgba(255,255,255,.07) 0 1px,transparent 1px 48px)}
.frame{position:absolute;left:22px;right:22px;top:20px;bottom:20px;border:1px solid rgba(255,255,255,.3);border-radius:6px}
.top{position:relative;display:flex;align-items:flex-end;justify-content:space-between;gap:30px;margin-bottom:20px}
.eyebrow{color:#BFD2F0;font-weight:700;font-size:14.5px;letter-spacing:.17em;text-transform:uppercase;margin-bottom:7px}
h2{font-family:'Cormorant Garamond',serif;font-weight:600;font-size:40px;line-height:1.07;color:#fff;letter-spacing:-.3px}
h2 i{font-style:italic;color:#F2C9D5}
.hint{flex:0 0 372px;background:rgba(255,255,255,.1);border:1px solid rgba(255,255,255,.35);border-radius:12px;padding:12px 17px;font-size:14.5px;color:#E8EFFA;line-height:1.36}
.hint b{color:#fff}

.rows{position:relative;display:flex;flex-direction:column;gap:12px}
.row{display:flex;align-items:center;gap:20px;border:1px solid rgba(255,255,255,.34);border-radius:12px;padding:14px 20px;background:rgba(255,255,255,.06)}
.row .w{flex:0 0 132px;font-family:'Noto Serif SC',serif;font-size:36px;color:#fff;line-height:1.1;letter-spacing:2px}
.row .p{flex:0 0 118px;font-size:16px;color:#BFD2F0;font-style:italic}
.row .ru{flex:0 0 250px;font-size:17px;font-weight:600;color:#fff}
.row .nt{flex:1 1 auto;font-size:14.5px;color:#D9E4F5;line-height:1.36}

.foot{position:relative;margin-top:auto;display:flex;align-items:center;gap:18px;padding-top:18px}
.foot .msg{flex:1 1 auto;background:rgba(255,255,255,.93);border-radius:13px;padding:12px 21px;font-size:15px;color:var(--ink);line-height:1.34}
.foot .msg b{color:var(--brick)}
.brand{display:flex;align-items:center;gap:10px;color:#fff;flex:0 0 auto}
.brand b{font-family:'Cormorant Garamond',serif;font-weight:700;font-size:23px}
.brand .dot2{width:9px;height:9px;border-radius:50%%;background:#F2C9D5}
.brand span{color:#BFD2F0;font-size:15px}
</style></head><body>
<div class="wrap">
  <div class="grid"></div>
  <div class="frame"></div>
  <div class="top">
    <div>
      <div class="eyebrow">Слова с 蓝</div>
      <h2>Где синий <i>уже не про цвет</i></h2>
    </div>
    <div class="hint">Фон этой картинки — <b>та самая синька</b>: чертежи печатали белыми линиями по синему, отсюда и 蓝图.</div>
  </div>

  <div class="rows">
%s
  </div>

  <div class="foot">
    <div class="msg">Проверяйте такие слова <b>целиком, а не по знакам</b>: 蓝图 это не «синий рисунок»</div>
    <div class="brand"><span class="dot2"></span><b>Kitai School</b><span>&middot; kitai-school.ru</span></div>
  </div>
</div>
</body></html>""" % (FONTS, VARS, rows)

info = info.replace("HGT", "540")
open(S + "sn-info.html", "w", encoding="utf-8").write(info)
print("ok")
