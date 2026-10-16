# -*- coding: utf-8 -*-
# Картинки к статье «„Удача“ по-китайски»
# Обложка    — каллиграфический лист с красной печатью
# Инфографика — разрез дома: где 福 вешают прямо, а где вверх ногами
S = "/tmp/claude-0/-home-user-Kitai-Shool/a463bfca-82a9-56fd-ae09-42a7257ff999/scratchpad/"

FONTS = ("<link href=\"https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,600;0,700;1,600"
         "&family=Inter:wght@400;500;600;700&family=Noto+Serif+SC:wght@600;700&display=swap\" rel=\"stylesheet\">")
VARS = (":root{--brick:#A41E3A;--brick-d:#841630;--brick-soft:#F7E6EB;--ink:#2C2420;--ink-2:#5A4F45;"
        "--taupe:#8B7D6B;--cream:#FAF7F2;--cream-2:#F3EDE3;--hair:#EAE3D8;--surface:#fff;"
        "--green:#1E7A46;--green-soft:#E3F6E9;--amber:#C08A2E;--amber-s:#FBF2DF;--blue:#2F5D8C;--blue-s:#E7EEF6;"
        "--paper:#FDFBF6;--wall:#EFE7DA;--wood:#B99ركА}")
VARS = VARS.replace("#B99ركА", "#B49A78")

# ------------------------------------------------------------------ обложка
hero = """<!DOCTYPE html><html lang="ru"><head><meta charset="utf-8">
%s
<style>
%s
*{margin:0;box-sizing:border-box}html,body{width:1200px;height:630px}
.card{width:1200px;height:630px;background:radial-gradient(1100px 680px at 15%% 10%%, #fff 0%%, var(--cream) 55%%, var(--cream-2) 100%%);position:relative;overflow:hidden;font-family:'Inter',sans-serif;display:flex;align-items:center;justify-content:space-between;padding:0 72px}
.card:before{content:"";position:absolute;left:0;top:0;bottom:0;width:12px;background:var(--brick)}
.txt{flex:0 0 480px}
.eyebrow{color:var(--brick);font-weight:700;font-size:18px;letter-spacing:.19em;text-transform:uppercase;margin-bottom:12px}
h1{font-family:'Cormorant Garamond',serif;font-weight:600;font-size:52px;line-height:1.05;color:var(--ink);letter-spacing:-.4px}
h1 i{font-style:italic;color:var(--brick)}
.sub{font-size:18px;color:var(--ink-2);line-height:1.42;max-width:30ch;margin-top:16px}
.row{display:flex;gap:10px;margin-top:24px}
.chip{background:var(--surface);border:1px solid var(--hair);border-radius:12px;padding:9px 14px;text-align:center;box-shadow:0 4px 12px rgba(44,36,32,.05)}
.chip b{display:block;font-family:'Noto Serif SC',serif;font-weight:700;font-size:20px;color:var(--ink);line-height:1.1}
.chip span{display:block;font-size:11.5px;color:var(--taupe);margin-top:2px}
.brand{position:absolute;left:72px;bottom:32px;display:flex;align-items:center;gap:11px;color:var(--ink)}
.brand b{font-family:'Cormorant Garamond',serif;font-weight:700;font-size:26px}
.brand .bdot{width:10px;height:10px;border-radius:50%%;background:var(--brick)}
.brand span{color:var(--taupe);font-size:16px}

/* каллиграфический лист */
.sheet{flex:0 0 470px;height:446px;position:relative;background:linear-gradient(180deg,var(--paper) 0%%,#F7F2E8 100%%);border:1px solid #E3D9C8;border-radius:10px;box-shadow:0 18px 40px rgba(44,36,32,.18);display:flex;align-items:center;justify-content:center}
.sheet:before{content:"";position:absolute;inset:16px;border:1px solid #E8DFCF;border-radius:6px}
.glyphs{display:flex;align-items:center;gap:18px}
.gl{font-family:'Noto Serif SC',serif;font-weight:700;font-size:108px;line-height:1;color:#241E19}
.side{display:flex;flex-direction:column;align-items:flex-start;gap:4px;border-left:1px solid #E3D9C8;padding-left:18px}
.side .py{font-size:23px;font-weight:600;color:var(--brick);letter-spacing:.01em}
.side .ru{font-size:16px;color:var(--ink-2)}
.side .note{font-size:13px;color:var(--taupe);margin-top:8px;line-height:1.35;max-width:14ch}
.seal{position:absolute;right:30px;bottom:30px;width:62px;height:62px;border-radius:7px;background:var(--brick);display:flex;align-items:center;justify-content:center;box-shadow:0 6px 16px rgba(164,30,58,.3)}
.seal span{font-family:'Noto Serif SC',serif;font-weight:700;font-size:34px;color:#FDEBEF;line-height:1.05;text-align:center}
</style></head><body>
<div class="card">
  <div class="txt">
    <div class="eyebrow">Слова и знаки</div>
    <h1>«Удача»<br><i>по-китайски</i></h1>
    <div class="sub">Главное слово — 好运. Но рядом стоят ещё три, и работают они по-разному</div>
    <div class="row">
      <div class="chip"><b>运气</b><span>ВЕЗЕНИЕ</span></div>
      <div class="chip"><b>幸运</b><span>УДАЧЛИВЫЙ</span></div>
      <div class="chip"><b>吉祥</b><span>БЛАГОПРИЯТНЫЙ</span></div>
    </div>
  </div>
  <div class="sheet">
    <div class="glyphs">
      <span class="gl">好运</span>
      <div class="side">
        <span class="py">hǎoyùn</span>
        <span class="ru">удача</span>
        <span class="note">运 — «судьба, ход вещей»</span>
      </div>
    </div>
    <div class="seal"><span>吉</span></div>
  </div>
  <div class="brand"><span class="bdot"></span><b>Kitai School</b><span>&middot; kitai-school.ru</span></div>
</div>
</body></html>""" % (FONTS, VARS)

open(S + "ud-hero.html", "w", encoding="utf-8").write(hero)

# -------------------------------------------------------------- инфографика
info = """<!DOCTYPE html><html lang="ru"><head><meta charset="utf-8">
%s
<style>
%s
*{margin:0;box-sizing:border-box}html,body{width:1200px;height:HGTpx}
.wrap{width:1200px;height:HGTpx;background:linear-gradient(180deg,#fff 0%%,var(--cream) 46%%,var(--cream-2) 100%%);font-family:'Inter',sans-serif;padding:32px 46px 26px;display:flex;flex-direction:column}
.top{display:flex;align-items:flex-end;justify-content:space-between;gap:30px;margin-bottom:22px}
.eyebrow{color:var(--brick);font-weight:700;font-size:14.5px;letter-spacing:.17em;text-transform:uppercase;margin-bottom:7px}
h2{font-family:'Cormorant Garamond',serif;font-weight:600;font-size:40px;line-height:1.07;color:var(--ink);letter-spacing:-.3px}
h2 i{font-style:italic;color:var(--brick)}
.hint{flex:0 0 352px;background:var(--surface);border:1px solid var(--hair);border-left:4px solid var(--brick);border-radius:12px;padding:12px 17px;font-size:14.5px;color:var(--ink-2);line-height:1.36}
.hint b{color:var(--ink)}

.house{display:flex;gap:26px;align-items:flex-start}

/* снаружи: дверь */
.out{flex:0 0 332px;background:linear-gradient(180deg,#F6F0E5,#EFE7DA);border:1px solid var(--hair);border-radius:16px;padding:16px 18px 18px;display:flex;flex-direction:column;align-items:center;box-shadow:0 10px 24px rgba(44,36,32,.08)}
.lab{font-size:11.5px;font-weight:700;letter-spacing:.13em;color:var(--taupe);align-self:flex-start}
.door{margin-top:10px;width:176px;height:196px;background:linear-gradient(180deg,#C8A882,var(--wood));border:3px solid #9A7F5F;border-radius:8px 8px 4px 4px;position:relative;display:flex;align-items:flex-start;justify-content:center;padding-top:30px;box-shadow:inset 0 0 0 6px rgba(255,255,255,.12)}
.door:after{content:"";position:absolute;left:50%%;top:0;bottom:0;width:2px;background:rgba(0,0,0,.18)}
.fu{width:84px;height:84px;background:linear-gradient(145deg,#B32442,#8E1630);border:2px solid #D9A94E;border-radius:6px;display:flex;align-items:center;justify-content:center;position:relative;z-index:1;box-shadow:0 8px 18px rgba(44,36,32,.25)}
.fu span{font-family:'Noto Serif SC',serif;font-weight:700;font-size:50px;color:#F7E3C0;line-height:1}
.fu.up span{transform:rotate(180deg)}
.verdict{margin-top:14px;text-align:center}
.verdict .v{font-size:17px;font-weight:700;color:var(--green)}
.verdict .v.bad{color:var(--brick)}
.verdict .d{font-size:13.5px;color:var(--ink-2);line-height:1.38;margin-top:5px;max-width:30ch}

/* внутри: предметы */
.in{flex:1 1 auto;background:var(--surface);border:1px solid var(--hair);border-radius:16px;padding:16px 20px 18px;box-shadow:0 10px 24px rgba(44,36,32,.08)}
.items{display:flex;gap:14px;margin-top:10px}
.item{flex:1 1 0;background:var(--cream);border:1px solid var(--hair);border-radius:13px;padding:13px 14px 15px;text-align:center}
.item .box{width:68px;height:68px;margin:0 auto 9px;border-radius:8px;background:linear-gradient(145deg,#B32442,#8E1630);border:2px solid #D9A94E;display:flex;align-items:center;justify-content:center}
.item .box span{font-family:'Noto Serif SC',serif;font-weight:700;font-size:42px;color:#F7E3C0;line-height:1;transform:rotate(180deg)}
.item .n{font-size:15px;font-weight:600;color:var(--ink)}
.item .w{font-size:13px;color:var(--ink-2);line-height:1.36;margin-top:5px}
.inverdict{margin-top:14px;background:var(--brick-soft);border:1px solid var(--brick);border-radius:12px;padding:11px 16px;font-size:14.5px;color:var(--ink);line-height:1.36}
.inverdict b{color:var(--brick)}

.foot{margin-top:auto;display:flex;align-items:center;gap:18px;padding-top:16px}
.foot .msg{flex:1 1 auto;background:var(--surface);border:1px solid var(--hair);border-left:4px solid var(--brick);border-radius:14px;padding:12px 21px;font-size:15.5px;color:var(--ink-2);line-height:1.34}
.foot .msg b{color:var(--ink)}
.brand{display:flex;align-items:center;gap:10px;color:var(--ink);flex:0 0 auto}
.brand b{font-family:'Cormorant Garamond',serif;font-weight:700;font-size:23px}
.brand .dot2{width:9px;height:9px;border-radius:50%%;background:var(--brick)}
.brand span{color:var(--taupe);font-size:15px}
</style></head><body>
<div class="wrap">
  <div class="top">
    <div>
      <div class="eyebrow">Где прямо, а где вверх ногами</div>
      <h2>На дверь — <i>только прямо</i></h2>
    </div>
    <div class="hint">Перевёрнутый знак на входной двери означал бы, что счастье дошло до порога <b>и внутрь не попало</b>. Переворачивают его в доме, а не на входе.</div>
  </div>

  <div class="house">
    <div class="out">
      <div class="lab">СНАРУЖИ · ВХОДНАЯ ДВЕРЬ</div>
      <div class="door"><div class="fu"><span>福</span></div></div>
      <div class="verdict">
        <div class="v">Прямо</div>
        <div class="d">Чтобы счастье вошло в дом, а не остановилось у порога</div>
      </div>
    </div>

    <div class="in">
      <div class="lab">ВНУТРИ ДОМА</div>
      <div class="items">
        <div class="item">
          <div class="box"><span>福</span></div>
          <div class="n">Шкаф, сундук</div>
          <div class="w">там хранят ценное — пусть прибывает</div>
        </div>
        <div class="item">
          <div class="box"><span>福</span></div>
          <div class="n">Сосуд для воды</div>
          <div class="w">воду выливают, и знак это возмещает</div>
        </div>
        <div class="item">
          <div class="box"><span>福</span></div>
          <div class="n">Мусорное ведро</div>
          <div class="w">содержимое выносят — счастье остаётся</div>
        </div>
      </div>
      <div class="inverdict">Здесь знак вешают <b>вверх ногами</b>: 倒 «перевёрнутый» звучит как 到 «прийти», и получается «счастье пришло»</div>
    </div>
  </div>

  <div class="foot">
    <div class="msg">Клеят обычно <b>до заката в канун Нового года</b>, в порядке снаружи внутрь</div>
    <div class="brand"><span class="dot2"></span><b>Kitai School</b><span>&middot; kitai-school.ru</span></div>
  </div>
</div>
</body></html>""" % (FONTS, VARS)

info = info.replace("HGT", "596")
open(S + "ud-info.html", "w", encoding="utf-8").write(info)
print("ok")
