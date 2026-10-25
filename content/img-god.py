# -*- coding: utf-8 -*-
# Картинки к статье «Языковой год в Китае: лексика кампуса»
# Обложка    — чемодан с биркой и наклейками
# Инфографика — поднос в столовой: секции с лексикой
S = "/tmp/claude-0/-home-user-Kitai-Shool/a463bfca-82a9-56fd-ae09-42a7257ff999/scratchpad/"

FONTS = ("<link href=\"https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,600;0,700;1,600"
         "&family=Inter:wght@400;500;600;700&family=Noto+Serif+SC:wght@600;700&display=swap\" rel=\"stylesheet\">")
VARS = (":root{--brick:#A41E3A;--brick-d:#841630;--brick-soft:#F7E6EB;--ink:#2C2420;--ink-2:#5A4F45;"
        "--taupe:#8B7D6B;--cream:#FAF7F2;--cream-2:#F3EDE3;--hair:#EAE3D8;--surface:#fff;"
        "--case:#8C5A3C;--case-2:#6E4530;--strap:#5A3A28;--tag:#F6F1E6;--tray:#D8DEE4;"
        "--tray-2:#C3CBD3;--green:#1E7A46;--blue:#2F5D8C}")

STICK = [("留学", "-7deg", "#E6CB7A", "22px", "30px"),
         ("HSK", "6deg", "#CBDCC9", "132px", "22px"),
         ("语言生", "-3deg", "#EFC7C4", "60px", "116px")]

sticks = "\n".join(
    '<div class="st" style="transform:rotate(%s);background:%s;left:%s;top:%s">%s</div>'
    % (rot, bg, left, top, txt) for txt, rot, bg, left, top in STICK)

hero = """<!DOCTYPE html><html lang="ru"><head><meta charset="utf-8">
%s
<style>
%s
*{margin:0;box-sizing:border-box}html,body{width:1200px;height:630px}
.card{width:1200px;height:630px;background:radial-gradient(1050px 660px at 14%% 12%%, #fff 0%%, var(--cream) 52%%, var(--cream-2) 100%%);position:relative;overflow:hidden;font-family:'Inter',sans-serif;padding:52px 46px 0 72px;display:flex;justify-content:space-between}
.card:before{content:"";position:absolute;left:0;top:0;bottom:0;width:12px;background:var(--brick)}
.txt{flex:0 0 500px;padding-top:4px}
.eyebrow{color:var(--brick);font-weight:700;font-size:18px;letter-spacing:.19em;text-transform:uppercase;margin-bottom:13px}
h1{font-family:'Cormorant Garamond',serif;font-weight:600;font-size:45px;line-height:1.07;color:var(--ink);letter-spacing:-.4px}
h1 i{font-style:italic;color:var(--brick)}
.sub{font-size:18px;color:var(--ink-2);line-height:1.42;max-width:31ch;margin-top:16px}
.tip{display:inline-block;margin-top:22px;background:var(--surface);border:1px solid var(--hair);border-left:4px solid var(--brick);border-radius:13px;padding:13px 19px;font-size:15.5px;color:var(--ink-2);line-height:1.36;max-width:34ch}
.tip b{color:var(--ink)}

/* чемодан */
.scene{flex:0 0 500px;padding-top:56px;display:flex;flex-direction:column;align-items:center}
.handle{width:96px;height:34px;border:7px solid var(--strap);border-bottom:none;border-radius:14px 14px 0 0}
.case{position:relative;width:360px;height:280px;border-radius:20px;background:linear-gradient(160deg,var(--case),var(--case-2));box-shadow:0 18px 32px rgba(44,36,32,.3), inset 0 2px 0 rgba(255,255,255,.14);padding:18px}
.case:before,.case:after{content:"";position:absolute;left:0;right:0;height:22px;background:var(--strap)}
.case:before{top:62px}.case:after{top:186px}
.st{position:absolute;padding:9px 13px;border-radius:7px;font-family:'Noto Serif SC',serif;font-size:21px;color:#2C2420;box-shadow:0 3px 7px rgba(0,0,0,.2);z-index:2}
.tag{position:absolute;right:-26px;top:40px;width:104px;height:70px;background:var(--tag);border:1px solid #E0D6C4;border-radius:7px;transform:rotate(8deg);box-shadow:0 5px 11px rgba(44,36,32,.22);display:flex;flex-direction:column;align-items:center;justify-content:center;gap:2px;z-index:3}
.tag b{font-family:'Noto Serif SC',serif;font-size:22px;color:var(--ink)}
.tag span{font-size:11.5px;color:var(--ink-2)}
.tag:before{content:"";position:absolute;left:50%%;top:-13px;transform:translateX(-50%%);width:2px;height:14px;background:#B9AD96}
.cap{margin-top:26px;text-align:center;font-size:16.5px;color:var(--ink-2);line-height:1.42;max-width:38ch}
.cap b{color:var(--ink)}
.brand{position:absolute;left:72px;bottom:28px;display:flex;align-items:center;gap:11px;color:var(--ink)}
.brand b{font-family:'Cormorant Garamond',serif;font-weight:700;font-size:26px}
.brand .bdot{width:10px;height:10px;border-radius:50%%;background:var(--brick)}
.brand span{color:var(--taupe);font-size:16px}
</style></head><body>
<div class="card">
  <div class="txt">
    <div class="eyebrow">Учёба в Китае</div>
    <h1>Языковой год: <i>лексика кампуса</i></h1>
    <div class="sub">В столовой и общежитии говорят не так, как в учебнике</div>
    <div class="tip"><b>Непонимание — не провал, а начало разговора:</b> переспросить выгоднее, чем кивнуть</div>
  </div>
  <div class="scene">
    <div class="handle"></div>
    <div class="case">
%s
      <div class="tag"><b>北京</b><span>языковой год</span></div>
    </div>
    <div class="cap">Первые недели решает не словарь, а <b>готовность переспрашивать</b></div>
  </div>
  <div class="brand"><span class="bdot"></span><b>Kitai School</b><span>&middot; kitai-school.ru</span></div>
</div>
</body></html>""" % (FONTS, VARS, sticks)

open(S + "god-hero.html", "w", encoding="utf-8").write(hero)

# -------------------------------------------------------------- инфографика
CELLS = [
    ("Что берут", [("米饭", "mǐfàn", "рис"), ("面条", "miàntiáo", "лапша"),
                   ("青菜", "qīngcài", "овощи")]),
    ("Как платят", [("一卡通", "yīkǎtōng", "кампусная карта"), ("扫码", "sǎomǎ", "сканировать код"),
                    ("多少钱", "duōshao qián", "сколько")]),
    ("Как просят", [("少放辣", "shǎo fàng là", "поменьше острого"),
                    ("打包", "dǎbāo", "с собой"), ("再来一个", "zài lái yí ge", "ещё одну порцию")]),
]

cells = "\n".join(
    '<div class="cell"><div class="ch">%s</div>%s</div>'
    % (title, "".join('<div class="w"><span class="han">%s</span>'
                      '<span class="t"><i>%s</i>%s</span></div>' % w for w in words))
    for title, words in CELLS)

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
.hint{flex:0 0 362px;background:var(--surface);border:1px solid var(--hair);border-left:4px solid var(--brick);border-radius:12px;padding:12px 17px;font-size:14.5px;color:var(--ink-2);line-height:1.36}
.hint b{color:var(--ink)}

/* поднос */
.tray{background:linear-gradient(180deg,var(--tray),var(--tray-2));border-radius:20px;padding:18px;box-shadow:0 12px 24px rgba(44,36,32,.16), inset 0 2px 0 rgba(255,255,255,.6);display:flex;gap:16px}
.cell{flex:1 1 0;background:var(--surface);border-radius:14px;padding:15px 17px;box-shadow:inset 0 0 0 1px var(--hair)}
.ch{font-size:15.5px;font-weight:700;color:var(--brick-d);margin-bottom:11px;border-bottom:2px solid var(--brick-soft);padding-bottom:7px}
.w{display:flex;align-items:baseline;gap:11px;margin-bottom:9px}
.w .han{font-family:'Noto Serif SC',serif;font-size:24px;color:var(--ink);flex:0 0 110px;line-height:1.2}
.w .t{font-size:14px;color:var(--ink-2);line-height:1.3}
.w .t i{display:block;color:var(--taupe);font-size:13.5px}

.note{margin-top:18px;background:var(--surface);border:1px solid var(--hair);border-radius:14px;padding:13px 20px;font-size:15px;color:var(--ink-2);line-height:1.36}
.note b{color:var(--ink)}

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
      <div class="eyebrow">Столовая 食堂</div>
      <h2>Три группы слов, <i>которые нужны сразу</i></h2>
    </div>
    <div class="hint">Здесь вы окажетесь в первый же день — и здесь <b>проще всего начать говорить</b>: реплики короткие и повторяются.</div>
  </div>

  <div class="tray">
%s
  </div>

  <div class="note"><b>一卡通</b> (yīkǎtōng) — студенческая карта: ею платят в столовой, проходят в общежитие и берут кипяток. Потерять её неприятнее, чем кажется.</div>

  <div class="foot">
    <div class="msg">Не расслышали цену — <b>покажите карту и спросите 多少钱</b>, это нормальная реплика</div>
    <div class="brand"><span class="dot2"></span><b>Kitai School</b><span>&middot; kitai-school.ru</span></div>
  </div>
</div>
</body></html>""" % (FONTS, VARS, cells)

info = info.replace("HGT", "560")
open(S + "god-info.html", "w", encoding="utf-8").write(info)
print("ok")
