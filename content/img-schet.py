# -*- coding: utf-8 -*-
# Картинки к статье «Счётные слова в китайском языке»
# Обложка    — бумажный пакет с наклейкой заказа 两杯咖啡
# Инфографика — три паза формулы и пятнадцать классификаторов по группам
S = "/tmp/claude-0/-home-user-Kitai-Shool/a463bfca-82a9-56fd-ae09-42a7257ff999/scratchpad/"

FONTS = ("<link href=\"https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,600;0,700;1,600"
         "&family=Inter:wght@400;500;600;700&family=Noto+Serif+SC:wght@600;700&display=swap\" rel=\"stylesheet\">")
VARS = (":root{--brick:#A41E3A;--brick-d:#841630;--brick-soft:#F7E6EB;--ink:#2C2420;--ink-2:#5A4F45;"
        "--taupe:#8B7D6B;--cream:#FAF7F2;--cream-2:#F3EDE3;--hair:#EAE3D8;--surface:#fff;"
        "--kraft:#C89A68;--kraft-2:#A87C4E;--kraft-3:#8E6740;--label:#FBF8F1;"
        "--slot:#EFE9DD;--blue:#2F5D8C;--green:#1E7A46}")

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
.tip{display:inline-block;margin-top:22px;background:var(--surface);border:1px solid var(--hair);border-left:4px solid var(--brick);border-radius:13px;padding:13px 19px;font-size:15.5px;color:var(--ink-2);line-height:1.36;max-width:34ch}
.tip b{color:var(--ink)}

/* бумажный пакет */
.scene{flex:0 0 500px;padding-top:46px;display:flex;flex-direction:column;align-items:center}
.bag{position:relative;width:330px;height:360px;border-radius:6px 6px 10px 10px;background:linear-gradient(170deg,var(--kraft),var(--kraft-2) 58%%,var(--kraft-3));box-shadow:0 18px 32px rgba(44,36,32,.26), inset 0 2px 0 rgba(255,255,255,.2)}
.bag:before{content:"";position:absolute;left:0;right:0;top:0;height:44px;background:linear-gradient(180deg,#D9AE7D,#C89A68);border-radius:6px 6px 0 0;box-shadow:inset 0 -2px 4px rgba(0,0,0,.12)}
.bag:after{content:"";position:absolute;left:50%%;top:0;bottom:0;width:1px;background:rgba(0,0,0,.09)}
.handle{position:absolute;left:50%%;top:-34px;transform:translateX(-50%%);width:150px;height:46px;border:7px solid var(--kraft-3);border-bottom:none;border-radius:60px 60px 0 0}
.label{position:absolute;left:50%%;top:104px;transform:translateX(-50%%) rotate(-2deg);width:252px;background:var(--label);border-radius:10px;padding:18px 20px;box-shadow:0 7px 16px rgba(44,36,32,.22)}
.label .ttl{font-size:12.5px;letter-spacing:.14em;text-transform:uppercase;color:var(--taupe);margin-bottom:9px}
.label .han{font-family:'Noto Serif SC',serif;font-size:38px;color:var(--ink);line-height:1.15}
.label .han b{color:var(--brick)}
.label .py{font-size:15px;color:var(--ink-2);font-style:italic;margin-top:5px}
.label .ru{font-size:14.5px;color:var(--ink-2);margin-top:2px}
.cap{margin-top:24px;text-align:center;font-size:16.5px;color:var(--ink-2);line-height:1.42;max-width:36ch}
.cap b{color:var(--ink)}
.brand{position:absolute;left:72px;bottom:28px;display:flex;align-items:center;gap:11px;color:var(--ink)}
.brand b{font-family:'Cormorant Garamond',serif;font-weight:700;font-size:26px}
.brand .bdot{width:10px;height:10px;border-radius:50%%;background:var(--brick)}
.brand span{color:var(--taupe);font-size:16px}
</style></head><body>
<div class="card">
  <div class="txt">
    <div class="eyebrow">Грамматика</div>
    <h1>Счётные слова <i>в китайском</i></h1>
    <div class="sub">Между числом и предметом всегда стоит третье слово</div>
    <div class="tip"><b>«Два кофе» по-китайски — 两杯咖啡:</b> 杯 здесь не «чашка», а обязательная часть конструкции</div>
  </div>
  <div class="scene">
    <div class="bag">
      <div class="handle"></div>
      <div class="label">
        <div class="ttl">заказ</div>
        <div class="han">两<b>杯</b>咖啡</div>
        <div class="py">liǎng bēi kāfēi</div>
        <div class="ru">два стакана кофе</div>
      </div>
    </div>
    <div class="cap">Убрать 杯 нельзя — <b>конструкция не собирается</b></div>
  </div>
  <div class="brand"><span class="bdot"></span><b>Kitai School</b><span>&middot; kitai-school.ru</span></div>
</div>
</body></html>""" % (FONTS, VARS)

open(S + "sch-hero2.html", "w", encoding="utf-8").write(hero)

# -------------------------------------------------------------- инфографика
GROUPS = [
    ("Универсальные и люди", ["个 gè", "位 wèi"]),
    ("Форма и назначение", ["张 zhāng", "条 tiáo", "本 běn", "把 bǎ", "只 zhī",
                            "双 shuāng", "件 jiàn"]),
    ("Ёмкости, техника, заведения", ["杯 bēi", "瓶 píng", "碗 wǎn", "辆 liàng",
                                     "台 tái", "家 jiā"]),
]

groups = "\n".join(
    '<div class="grp"><div class="gh">%s</div><div class="ws">%s</div></div>'
    % (title, "".join('<span class="w">%s</span>' % w for w in words))
    for title, words in GROUPS)

TOTAL = sum(len(w) for _, w in GROUPS)

info = """<!DOCTYPE html><html lang="ru"><head><meta charset="utf-8">
%s
<style>
%s
*{margin:0;box-sizing:border-box}html,body{width:1200px;height:HGTpx}
.wrap{width:1200px;height:HGTpx;background:linear-gradient(180deg,#fff 0%%,var(--cream) 46%%,var(--cream-2) 100%%);font-family:'Inter',sans-serif;padding:32px 46px 30px;display:flex;flex-direction:column}
.top{display:flex;align-items:flex-end;justify-content:space-between;gap:30px;margin-bottom:20px}
.eyebrow{color:var(--brick);font-weight:700;font-size:14.5px;letter-spacing:.17em;text-transform:uppercase;margin-bottom:7px}
h2{font-family:'Cormorant Garamond',serif;font-weight:600;font-size:40px;line-height:1.07;color:var(--ink);letter-spacing:-.3px}
h2 i{font-style:italic;color:var(--brick)}
.hint{flex:0 0 360px;background:var(--surface);border:1px solid var(--hair);border-left:4px solid var(--brick);border-radius:12px;padding:12px 17px;font-size:14.5px;color:var(--ink-2);line-height:1.36}
.hint b{color:var(--ink)}

.formula{display:flex;align-items:center;justify-content:center;gap:16px;margin-bottom:22px}
.slot{background:var(--surface);border:2px solid var(--hair);border-radius:14px;padding:14px 24px;text-align:center;min-width:184px;box-shadow:0 5px 13px rgba(44,36,32,.06)}
.slot .lb{font-size:13px;color:var(--taupe);letter-spacing:.04em}
.slot .vl{font-family:'Noto Serif SC',serif;font-size:36px;color:var(--ink);line-height:1.2;margin-top:3px}
.slot.empty{border-style:dashed;border-color:var(--brick);background:var(--brick-soft)}
.slot.empty .vl{color:var(--brick)}
.slot.empty .lb{color:var(--brick-d);font-weight:600}
.plus{font-size:26px;color:var(--taupe)}

.grp{background:var(--surface);border:1px solid var(--hair);border-radius:15px;padding:14px 18px;box-shadow:0 4px 12px rgba(44,36,32,.05);margin-bottom:12px}
.gh{font-size:14.5px;font-weight:700;color:var(--brick-d);margin-bottom:9px}
.ws{display:flex;flex-wrap:wrap;gap:9px}
.w{background:var(--cream-2);border-radius:9px;padding:7px 13px;font-family:'Noto Serif SC',serif;font-size:19px;color:var(--ink)}

.foot{margin-top:auto;display:flex;align-items:center;gap:18px;padding-top:14px}
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
      <div class="eyebrow">Конструкция</div>
      <h2>Средний паз <i>пропустить нельзя</i></h2>
    </div>
    <div class="hint">Пятнадцать классификаторов закрывают почти весь быт. <b>Остальные добираются по ходу</b>, вместе со словами.</div>
  </div>

  <div class="formula">
    <div class="slot"><div class="lb">число</div><div class="vl">三</div></div>
    <div class="plus">+</div>
    <div class="slot empty"><div class="lb">счётное слово</div><div class="vl">本</div></div>
    <div class="plus">+</div>
    <div class="slot"><div class="lb">предмет</div><div class="vl">书</div></div>
  </div>

%s

  <div class="foot">
    <div class="msg">Новое существительное учат <b>сразу со своим классификатором</b> — одной карточкой</div>
    <div class="brand"><span class="dot2"></span><b>Kitai School</b><span>&middot; kitai-school.ru</span></div>
  </div>
</div>
</body></html>""" % (FONTS, VARS, groups)

info = info.replace("HGT", "690")
open(S + "sch-info2.html", "w", encoding="utf-8").write(info)
print("ok, классификаторов на инфографике:", TOTAL)
