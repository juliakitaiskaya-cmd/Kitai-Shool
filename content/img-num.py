# -*- coding: utf-8 -*-
# Картинки к статье «Китайская нумерология»
# Обложка    — латунный номер 888 на двери и созвучие 八 → 发
# Инфографика — девять цифр с созвучиями и цветовым статусом
S = ("/tmp/claude-0/-home-user-Kitai-Shool/a463bfca-82a9-56fd-ae09-42a7257ff999/"
     "scratchpad/")

FONTS = ("<link href=\"https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,600;0,700;1,600"
         "&family=Inter:wght@400;500;600;700&family=Noto+Serif+SC:wght@600;700&display=swap\" rel=\"stylesheet\">")
VARS = (":root{--brick:#A41E3A;--brick-d:#841630;--brick-soft:#F7E6EB;--ink:#2C2420;--ink-2:#5A4F45;"
        "--taupe:#8B7D6B;--cream:#FAF7F2;--cream-2:#F3EDE3;--hair:#EAE3D8;--surface:#fff;"
        "--brass:#D7B468;--brass-2:#B8933F;--brass-3:#8C6D27;--wood:#7A5B40;--wood-2:#5E4530;"
        "--good:#1E7A46;--good-s:#E6F4EA;--grey:#8A8E93;--grey-s:#EFEFF0}")

hero = """<!DOCTYPE html><html lang="ru"><head><meta charset="utf-8">
%s
<style>
%s
*{margin:0;box-sizing:border-box}html,body{width:1200px;height:630px}
.card{width:1200px;height:630px;background:radial-gradient(1050px 660px at 14%% 12%%, #fff 0%%, var(--cream) 52%%, var(--cream-2) 100%%);position:relative;overflow:hidden;font-family:'Inter',sans-serif;padding:52px 46px 0 72px;display:flex;justify-content:space-between}
.card:before{content:"";position:absolute;left:0;top:0;bottom:0;width:12px;background:var(--brick)}
.txt{flex:0 0 506px;padding-top:6px}
.eyebrow{color:var(--brick);font-weight:700;font-size:18px;letter-spacing:.19em;text-transform:uppercase;margin-bottom:13px}
h1{font-family:'Cormorant Garamond',serif;font-weight:600;font-size:45px;line-height:1.07;color:var(--ink);letter-spacing:-.4px}
h1 i{font-style:italic;color:var(--brick)}
.sub{font-size:18px;color:var(--ink-2);line-height:1.42;max-width:31ch;margin-top:16px}
.tip{display:inline-block;margin-top:22px;background:var(--surface);border:1px solid var(--hair);border-left:4px solid var(--brick);border-radius:13px;padding:13px 19px;font-size:15.5px;color:var(--ink-2);line-height:1.36;max-width:35ch}
.tip b{color:var(--ink)}

/* дверь с латунным номером */
.scene{flex:0 0 468px;padding-top:30px;display:flex;flex-direction:column;align-items:center}
.door{position:relative;width:286px;height:372px;border-radius:10px 10px 6px 6px;background:linear-gradient(160deg,#8D6B4C,var(--wood) 55%%,var(--wood-2));box-shadow:0 16px 30px rgba(44,36,32,.28), inset 0 2px 0 rgba(255,255,255,.14)}
.door:before{content:"";position:absolute;inset:18px;border-radius:6px;border:2px solid rgba(255,255,255,.1)}
.plate{position:absolute;left:50%%;top:62px;transform:translateX(-50%%);width:208px;border-radius:8px;background:linear-gradient(160deg,#F0DFAF,var(--brass) 48%%,var(--brass-2) 86%%,var(--brass-3));box-shadow:0 8px 16px rgba(44,36,32,.32), inset 0 2px 0 rgba(255,255,255,.55);padding:16px 0 18px;text-align:center}
.plate .n{font-family:'Inter',sans-serif;font-size:62px;font-weight:700;color:#4A3A12;line-height:1;letter-spacing:.06em;text-shadow:0 1px 0 rgba(255,255,255,.45)}
.screw{position:absolute;width:9px;height:9px;border-radius:50%%;background:var(--brass-3);box-shadow:inset 0 1px 1px rgba(255,255,255,.4)}
.s1{left:12px;top:10px}.s2{right:12px;top:10px}
.s3{left:12px;bottom:10px}.s4{right:12px;bottom:10px}
.knob{position:absolute;right:24px;top:188px;width:30px;height:30px;border-radius:50%%;background:radial-gradient(circle at 34%% 30%%, #F0DFAF, var(--brass) 55%%, var(--brass-3));box-shadow:0 3px 7px rgba(44,36,32,.35)}
.sound{position:absolute;right:-58px;bottom:12px;background:var(--surface);border:1px solid var(--hair);border-radius:14px;padding:12px 18px 14px;text-align:center;box-shadow:0 10px 20px rgba(44,36,32,.18)}
.sound .row{display:flex;align-items:center;gap:10px}
.sound .h{font-family:'Noto Serif SC',serif;font-size:34px;color:var(--ink);line-height:1}
.sound .h.b{color:var(--brick)}
.sound .ar{font-size:19px;color:var(--taupe)}
.sound .p{font-size:14px;color:var(--ink-2);font-style:italic;margin-top:5px}
.cap{margin-top:24px;text-align:center;font-size:16.5px;color:var(--ink-2);line-height:1.4;max-width:36ch}
.cap b{color:var(--ink)}
.brand{position:absolute;left:72px;bottom:28px;display:flex;align-items:center;gap:11px;color:var(--ink)}
.brand b{font-family:'Cormorant Garamond',serif;font-weight:700;font-size:26px}
.brand .bdot{width:10px;height:10px;border-radius:50%%;background:var(--brick)}
.brand span{color:var(--taupe);font-size:16px}
</style></head><body>
<div class="card">
  <div class="txt">
    <div class="eyebrow">Культура</div>
    <h1>Китайская <i>нумерология</i></h1>
    <div class="sub">Числа ценят не за величину, а за то, как они звучат</div>
    <div class="tip"><b>八 bā звучит почти как 发 fā — «богатеть».</b> Отсюда и цены, и номера, и этажи</div>
  </div>
  <div class="scene">
    <div class="door">
      <div class="plate">
        <span class="screw s1"></span><span class="screw s2"></span>
        <span class="screw s3"></span><span class="screw s4"></span>
        <div class="n">888</div>
      </div>
      <div class="knob"></div>
      <div class="sound">
        <div class="row"><span class="h b">八</span><span class="ar">&rarr;</span><span class="h">发</span></div>
        <div class="p">bā — fā, «богатеть»</div>
      </div>
    </div>
    <div class="cap">Номер выбирают <b>так же тщательно, как вывеску</b></div>
  </div>
  <div class="brand"><span class="bdot"></span><b>Kitai School</b><span>&middot; kitai-school.ru</span></div>
</div>
</body></html>""" % (FONTS, VARS)

open(S + "num-hero.html", "w", encoding="utf-8").write(hero)

# --------------------------------------------------------------- инфографика
# цифра, знак, пиньинь, созвучие, пояснение, статус
NUM = [
    ("1", "一", "yī", "—", "в номерах читают yāo", "neutral"),
    ("2", "二", "èr", "好事成双", "хорошее приходит парами", "good"),
    ("3", "三", "sān", "散 sàn", "«расставаться» — в подарках избегают", "mixed"),
    ("4", "四", "sì", "死 sǐ", "«смерть» — самое избегаемое", "bad"),
    ("5", "五", "wǔ", "无 wú", "и «без», и 五福 «пять благ»", "mixed"),
    ("6", "六", "liù", "六六大顺", "«всё идёт гладко»", "good"),
    ("7", "七", "qī", "—", "само по себе нейтрально", "neutral"),
    ("8", "八", "bā", "发 fā", "«богатеть» — главное счастливое", "good"),
    ("9", "九", "jiǔ", "久 jiǔ", "«долго» — о прочности и долголетии", "good"),
]

assert len(NUM) == 9, "цифр не девять"
assert sum(1 for n in NUM if n[5] == "bad") == 1, "избегаемая цифра отмечена не одна"

tiles = "".join(
    '<div class="tile %s"><div class="dg">%s</div><div class="hn">%s</div>'
    '<div class="py">%s</div><div class="so">%s</div><div class="ds">%s</div></div>'
    % (st, d, h, p, so, ds) for d, h, p, so, ds, st in NUM)

info = """<!DOCTYPE html><html lang="ru"><head><meta charset="utf-8">
%(fonts)s
<style>
%(vars)s
*{margin:0;box-sizing:border-box}html,body{width:1200px;height:HGTpx}
.wrap{width:1200px;height:HGTpx;background:linear-gradient(180deg,#fff 0%%,var(--cream) 46%%,var(--cream-2) 100%%);font-family:'Inter',sans-serif;padding:32px 46px 28px;display:flex;flex-direction:column}
.top{display:flex;align-items:flex-end;justify-content:space-between;gap:30px;margin-bottom:18px}
.eyebrow{color:var(--brick);font-weight:700;font-size:14.5px;letter-spacing:.17em;text-transform:uppercase;margin-bottom:7px}
h2{font-family:'Cormorant Garamond',serif;font-weight:600;font-size:40px;line-height:1.07;color:var(--ink);letter-spacing:-.3px}
h2 i{font-style:italic;color:var(--brick)}
.hint{flex:0 0 376px;background:var(--surface);border:1px solid var(--hair);border-left:4px solid var(--brick);border-radius:12px;padding:12px 17px;font-size:14.5px;color:var(--ink-2);line-height:1.36}
.hint b{color:var(--ink)}

.legend{display:flex;gap:18px;margin-bottom:14px;font-size:13.5px;color:var(--ink-2)}
.legend span{display:flex;align-items:center;gap:7px}
.legend i{width:13px;height:13px;border-radius:4px;display:inline-block}
.i-good{background:var(--good)}
.i-mixed{background:var(--brass-2)}
.i-bad{background:var(--brick)}
.i-neutral{background:var(--grey)}

.grid{display:grid;grid-template-columns:repeat(3,1fr);gap:12px}
.tile{background:var(--surface);border:1px solid var(--hair);border-radius:15px;padding:12px 16px 13px;box-shadow:0 4px 11px rgba(44,36,32,.05);position:relative;overflow:hidden}
.tile:before{content:"";position:absolute;left:0;top:0;bottom:0;width:5px}
.tile.good:before{background:var(--good)}
.tile.mixed:before{background:var(--brass-2)}
.tile.bad:before{background:var(--brick)}
.tile.neutral:before{background:var(--grey)}
.tile .dg{position:absolute;right:14px;top:10px;font-size:30px;font-weight:700;color:var(--hair)}
.tile .hn{font-family:'Noto Serif SC',serif;font-size:27px;color:var(--ink);line-height:1.1}
.tile .py{font-size:13px;color:var(--ink-2);font-style:italic}
.tile .so{font-family:'Noto Serif SC',serif;font-size:17px;color:var(--brick-d);margin-top:4px}
.tile .ds{font-size:13.5px;color:var(--ink-2);margin-top:2px;line-height:1.3}

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
      <div class="eyebrow">Девять цифр</div>
      <h2>Значение держится <i>на созвучии</i></h2>
    </div>
    <div class="hint">Цифра хороша не сама по себе, а потому что <b>напоминает по звучанию другое слово</b>. Отсюда и вся система, и её исключения.</div>
  </div>

  <div class="legend">
    <span><i class="i-good"></i>любят</span>
    <span><i class="i-mixed"></i>смотря где</span>
    <span><i class="i-bad"></i>избегают</span>
    <span><i class="i-neutral"></i>нейтрально</span>
  </div>

  <div class="grid">%(tiles)s</div>

  <div class="foot">
    <div class="msg">Это примета, а не правило — <b>но в ценах и номерах её видно каждый день</b></div>
    <div class="brand"><span class="dot2"></span><b>Kitai School</b><span>&middot; kitai-school.ru</span></div>
  </div>
</div>
</body></html>""" % dict(fonts=FONTS, vars=VARS, tiles=tiles)

info = info.replace("HGT", "660")
open(S + "num-info.html", "w", encoding="utf-8").write(info)
print("ok, цифр:", len(NUM))
