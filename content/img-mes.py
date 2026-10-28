# -*- coding: utf-8 -*-
# Картинки к статье «Месяцы на китайском»
# Обложка    — нумератор со сменной цифрой: меняется число, 月 остаётся
# Инфографика — сетка из двенадцати плиток и врезка 几月 против 几个月
S = ("/tmp/claude-0/-home-user-Kitai-Shool/a463bfca-82a9-56fd-ae09-42a7257ff999/"
     "scratchpad/")

FONTS = ("<link href=\"https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,600;0,700;1,600"
         "&family=Inter:wght@400;500;600;700&family=Noto+Serif+SC:wght@600;700&display=swap\" rel=\"stylesheet\">")
VARS = (":root{--brick:#A41E3A;--brick-d:#841630;--brick-soft:#F7E6EB;--ink:#2C2420;--ink-2:#5A4F45;"
        "--taupe:#8B7D6B;--cream:#FAF7F2;--cream-2:#F3EDE3;--hair:#EAE3D8;--surface:#fff;"
        "--steel:#D4D7DB;--steel-2:#AFB4BA;--steel-3:#7E858D;--ink-dark:#1F1B18;--slate:#2F5D8C}")

hero = """<!DOCTYPE html><html lang="ru"><head><meta charset="utf-8">
%s
<style>
%s
*{margin:0;box-sizing:border-box}html,body{width:1200px;height:630px}
.card{width:1200px;height:630px;background:radial-gradient(1050px 660px at 14%% 12%%, #fff 0%%, var(--cream) 52%%, var(--cream-2) 100%%);position:relative;overflow:hidden;font-family:'Inter',sans-serif;padding:52px 46px 0 72px;display:flex;justify-content:space-between}
.card:before{content:"";position:absolute;left:0;top:0;bottom:0;width:12px;background:var(--brick)}
.txt{flex:0 0 498px;padding-top:6px}
.eyebrow{color:var(--brick);font-weight:700;font-size:18px;letter-spacing:.19em;text-transform:uppercase;margin-bottom:13px}
h1{font-family:'Cormorant Garamond',serif;font-weight:600;font-size:45px;line-height:1.07;color:var(--ink);letter-spacing:-.4px}
h1 i{font-style:italic;color:var(--brick)}
.sub{font-size:18px;color:var(--ink-2);line-height:1.42;max-width:31ch;margin-top:16px}
.tip{display:inline-block;margin-top:22px;background:var(--surface);border:1px solid var(--hair);border-left:4px solid var(--brick);border-radius:13px;padding:13px 19px;font-size:15.5px;color:var(--ink-2);line-height:1.36;max-width:35ch}
.tip b{color:var(--ink)}

/* нумератор */
.scene{flex:0 0 470px;padding-top:48px;display:flex;flex-direction:column;align-items:center}
.stamp{position:relative;width:360px;background:linear-gradient(170deg,#F4F5F7,var(--steel) 60%%,var(--steel-2));border-radius:18px;padding:22px 24px 26px;box-shadow:0 16px 30px rgba(44,36,32,.24), inset 0 2px 0 rgba(255,255,255,.75)}
.handle{position:absolute;left:50%%;top:-30px;transform:translateX(-50%%);width:118px;height:34px;border-radius:12px 12px 4px 4px;background:linear-gradient(180deg,var(--steel-2),var(--steel-3));box-shadow:0 4px 8px rgba(44,36,32,.22)}
.rows{display:flex;gap:12px;align-items:stretch;justify-content:center}
.drum{position:relative;flex:0 0 112px;background:var(--ink-dark);border-radius:12px;padding:10px 0;overflow:hidden;box-shadow:inset 0 0 0 2px rgba(255,255,255,.12)}
.drum .v{font-family:'Noto Serif SC',serif;font-size:50px;line-height:1.16;color:#F2EDE4;text-align:center}
.drum .v.dim{color:rgba(242,237,228,.28);font-size:34px;line-height:1.1}
.drum:before,.drum:after{content:"";position:absolute;left:0;right:0;height:26px;pointer-events:none}
.drum:before{top:0;background:linear-gradient(180deg,rgba(31,27,24,.95),rgba(31,27,24,0))}
.drum:after{bottom:0;background:linear-gradient(0deg,rgba(31,27,24,.95),rgba(31,27,24,0))}
.fixed{flex:0 0 112px;background:var(--brick);border-radius:12px;display:flex;align-items:center;justify-content:center;box-shadow:inset 0 0 0 2px rgba(255,255,255,.18)}
.fixed .v{font-family:'Noto Serif SC',serif;font-size:60px;color:#FDF6EC;line-height:1}
.labels{display:flex;gap:12px;justify-content:center;margin-top:12px}
.labels span{flex:0 0 112px;text-align:center;font-size:13px;color:#4C5158;letter-spacing:.04em}
.labels span.b{color:var(--brick-d);font-weight:700}
.cap{margin-top:24px;text-align:center;font-size:16.5px;color:var(--ink-2);line-height:1.4;max-width:38ch}
.cap b{color:var(--ink)}
.brand{position:absolute;left:72px;bottom:28px;display:flex;align-items:center;gap:11px;color:var(--ink)}
.brand b{font-family:'Cormorant Garamond',serif;font-weight:700;font-size:26px}
.brand .bdot{width:10px;height:10px;border-radius:50%%;background:var(--brick)}
.brand span{color:var(--taupe);font-size:16px}
</style></head><body>
<div class="card">
  <div class="txt">
    <div class="eyebrow">Лексика</div>
    <h1>Месяцы <i>на китайском</i></h1>
    <div class="sub">Двенадцать названий, которые не нужно учить по отдельности</div>
    <div class="tip"><b>Название месяца — это число и 月.</b> Меняется только цифра, второе слово остаётся тем же</div>
  </div>
  <div class="scene">
    <div class="stamp">
      <div class="handle"></div>
      <div class="rows">
        <div class="drum">
          <div class="v dim">二</div>
          <div class="v">三</div>
          <div class="v dim">四</div>
        </div>
        <div class="fixed"><div class="v">月</div></div>
      </div>
      <div class="labels"><span>меняется</span><span class="b">не меняется</span></div>
    </div>
    <div class="cap">三月 — март. <b>Крутим барабан — получаем любой месяц</b></div>
  </div>
  <div class="brand"><span class="bdot"></span><b>Kitai School</b><span>&middot; kitai-school.ru</span></div>
</div>
</body></html>""" % (FONTS, VARS)

open(S + "mes-hero.html", "w", encoding="utf-8").write(hero)

# --------------------------------------------------------------- инфографика
MONTHS = [
    ("一月", "yīyuè", "январь"), ("二月", "èryuè", "февраль"), ("三月", "sānyuè", "март"),
    ("四月", "sìyuè", "апрель"), ("五月", "wǔyuè", "май"), ("六月", "liùyuè", "июнь"),
    ("七月", "qīyuè", "июль"), ("八月", "bāyuè", "август"), ("九月", "jiǔyuè", "сентябрь"),
    ("十月", "shíyuè", "октябрь"), ("十一月", "shíyīyuè", "ноябрь"),
    ("十二月", "shí'èryuè", "декабрь"),
]

assert len(MONTHS) == 12, "месяцев не 12, а %d" % len(MONTHS)
assert all(m[0].endswith("月") for m in MONTHS), "в сетке есть не месяц"
assert all(m[1] for m in MONTHS), "у месяца нет пиньиня"

tiles = "".join(
    '<div class="tile"><div class="no">%d</div><div class="hn">%s</div>'
    '<div class="py">%s</div><div class="ru">%s</div></div>'
    % (i + 1, han, py, ru) for i, (han, py, ru) in enumerate(MONTHS))

info = """<!DOCTYPE html><html lang="ru"><head><meta charset="utf-8">
%(fonts)s
<style>
%(vars)s
*{margin:0;box-sizing:border-box}html,body{width:1200px;height:HGTpx}
.wrap{width:1200px;height:HGTpx;background:linear-gradient(180deg,#fff 0%%,var(--cream) 46%%,var(--cream-2) 100%%);font-family:'Inter',sans-serif;padding:32px 46px 28px;display:flex;flex-direction:column}
.top{display:flex;align-items:flex-end;justify-content:space-between;gap:30px;margin-bottom:20px}
.eyebrow{color:var(--brick);font-weight:700;font-size:14.5px;letter-spacing:.17em;text-transform:uppercase;margin-bottom:7px}
h2{font-family:'Cormorant Garamond',serif;font-weight:600;font-size:40px;line-height:1.07;color:var(--ink);letter-spacing:-.3px}
h2 i{font-style:italic;color:var(--brick)}
.hint{flex:0 0 372px;background:var(--surface);border:1px solid var(--hair);border-left:4px solid var(--brick);border-radius:12px;padding:12px 17px;font-size:14.5px;color:var(--ink-2);line-height:1.36}
.hint b{color:var(--ink)}

.grid{display:grid;grid-template-columns:repeat(4,1fr);gap:12px}
.tile{background:var(--surface);border:1px solid var(--hair);border-radius:14px;padding:11px 14px 12px;box-shadow:0 4px 11px rgba(44,36,32,.05);position:relative}
.tile .no{position:absolute;right:12px;top:9px;font-size:12px;color:var(--taupe);font-weight:600}
.tile .hn{font-family:'Noto Serif SC',serif;font-size:27px;color:var(--ink);line-height:1.12}
.tile .py{font-size:13.5px;color:var(--brick-d);font-style:italic;margin-top:1px}
.tile .ru{font-size:14px;color:var(--ink-2);margin-top:2px}

.pair{display:flex;gap:14px;margin-top:16px}
.pc{flex:1 1 0;background:var(--surface);border:1px solid var(--hair);border-left:4px solid var(--brick);border-radius:14px;padding:13px 19px;display:flex;align-items:center;gap:16px}
.pc .q{font-family:'Noto Serif SC',serif;font-size:28px;color:var(--brick-d);flex:0 0 auto}
.pc .t{font-size:15px;color:var(--ink);font-weight:700}
.pc .d{font-size:14px;color:var(--ink-2);margin-top:2px;line-height:1.32}

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
      <div class="eyebrow">Двенадцать месяцев</div>
      <h2>Одно правило <i>на весь год</i></h2>
    </div>
    <div class="hint">Запоминать нужно только 月 и счёт до двенадцати. <b>Ноябрь и декабрь</b> строятся так же: 十一月 и 十二月.</div>
  </div>

  <div class="grid">%(tiles)s</div>

  <div class="pair">
    <div class="pc"><div class="q">几月</div><div><div class="t">какой месяц</div>
      <div class="d">你的生日是几月？ — в каком месяце день рождения</div></div></div>
    <div class="pc"><div class="q">几个月</div><div><div class="t">сколько месяцев</div>
      <div class="d">你学了几个月？ — сколько месяцев вы учитесь</div></div></div>
  </div>

  <div class="foot">
    <div class="msg">Разница в одном слоге — <b>个 превращает название в длительность</b></div>
    <div class="brand"><span class="dot2"></span><b>Kitai School</b><span>&middot; kitai-school.ru</span></div>
  </div>
</div>
</body></html>""" % dict(fonts=FONTS, vars=VARS, tiles=tiles)

info = info.replace("HGT", "600")
open(S + "mes-info.html", "w", encoding="utf-8").write(info)
print("ok, месяцев в сетке:", len(MONTHS))
