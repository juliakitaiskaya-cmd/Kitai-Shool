# -*- coding: utf-8 -*-
# Картинки к статье «Речевой этикет в Китае»
# Обложка    — раскрытый веер: формулы по ситуациям
# Инфографика — три гири: вес извинения
S = "/tmp/claude-0/-home-user-Kitai-Shool/a463bfca-82a9-56fd-ae09-42a7257ff999/scratchpad/"

FONTS = ("<link href=\"https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,600;0,700;1,600"
         "&family=Inter:wght@400;500;600;700&family=Noto+Serif+SC:wght@600;700&display=swap\" rel=\"stylesheet\">")
VARS = (":root{--brick:#A41E3A;--brick-d:#841630;--brick-soft:#F7E6EB;--ink:#2C2420;--ink-2:#5A4F45;"
        "--taupe:#8B7D6B;--cream:#FAF7F2;--cream-2:#F3EDE3;--hair:#EAE3D8;--surface:#fff;"
        "--green:#1E7A46;--green-s:#E3F6E9;--amber:#C08A2E;--amber-s:#FBF2DF;--blue:#2F5D8C;--blue-s:#E7EEF6;"
        "--fan:#FDF8EC;--fan-2:#F2E7CE;--rib:#B98A4B;--iron:#4A4440;--iron-2:#332E2B}")

BLADES = [
    (-52, "谢谢", "спасибо"),
    (-26, "不好意思", "извините"),
    (0, "请", "пожалуйста"),
    (26, "麻烦您", "побеспокою"),
    (52, "不客气", "не за что"),
]

blades = "\n".join(
    '<div class="bl" style="transform:rotate(%ddeg)">'
    '  <div class="ribtop"><div class="inner" style="transform:rotate(%ddeg)">'
    '<span class="h">%s</span><span class="r">%s</span></div></div>'
    '</div>' % (a, -a, han, ru) for a, han, ru in BLADES)

hero = """<!DOCTYPE html><html lang="ru"><head><meta charset="utf-8">
%s
<style>
%s
*{margin:0;box-sizing:border-box}html,body{width:1200px;height:630px}
.card{width:1200px;height:630px;background:radial-gradient(1050px 660px at 14%% 12%%, #fff 0%%, var(--cream) 52%%, var(--cream-2) 100%%);position:relative;overflow:hidden;font-family:'Inter',sans-serif;padding:52px 40px 0 72px;display:flex;justify-content:space-between}
.card:before{content:"";position:absolute;left:0;top:0;bottom:0;width:12px;background:var(--brick)}
.txt{flex:0 0 520px;padding-top:4px}
.eyebrow{color:var(--brick);font-weight:700;font-size:18px;letter-spacing:.19em;text-transform:uppercase;margin-bottom:13px}
h1{font-family:'Cormorant Garamond',serif;font-weight:600;font-size:47px;line-height:1.06;color:var(--ink);letter-spacing:-.4px}
h1 i{font-style:italic;color:var(--brick)}
.sub{font-size:18.5px;color:var(--ink-2);line-height:1.42;max-width:32ch;margin-top:16px}
.note{display:inline-block;margin-top:22px;background:var(--surface);border:1px solid var(--hair);border-left:4px solid var(--brick);border-radius:13px;padding:13px 19px;font-size:15.5px;color:var(--ink-2);line-height:1.36;max-width:34ch}
.note b{color:var(--ink)}

/* веер */
.fan{flex:0 0 540px;position:relative;height:500px}
.pivot{position:absolute;left:50%%;bottom:52px;width:26px;height:26px;margin-left:-13px;border-radius:50%%;background:radial-gradient(circle at 36%% 32%%, #E8CFA0, var(--rib));box-shadow:0 3px 8px rgba(44,36,32,.3);z-index:5}
.bl{position:absolute;left:50%%;bottom:62px;width:96px;height:312px;margin-left:-48px;transform-origin:50%% 100%%}
.ribtop{position:absolute;left:0;right:0;top:0;height:300px;border-radius:48px 48px 10px 10px;background:linear-gradient(180deg,var(--fan),var(--fan-2));border:1px solid var(--hair);box-shadow:0 6px 16px rgba(44,36,32,.1);display:flex;align-items:flex-start;justify-content:center;padding-top:30px}
.inner{display:flex;flex-direction:column;align-items:center;gap:7px;width:104px}
.ribtop .h{font-family:'Noto Serif SC',serif;font-weight:700;font-size:23px;color:var(--ink);line-height:1.15;text-align:center;padding:0 6px}
.ribtop .r{font-size:12.5px;color:var(--taupe);text-align:center;line-height:1.25;padding:0 6px}
.cap{position:absolute;left:0;right:0;bottom:16px;text-align:center;font-size:15px;color:var(--ink-2);line-height:1.34}
.cap b{color:var(--ink)}
.brand{position:absolute;left:72px;bottom:28px;display:flex;align-items:center;gap:11px;color:var(--ink)}
.brand b{font-family:'Cormorant Garamond',serif;font-weight:700;font-size:26px}
.brand .bdot{width:10px;height:10px;border-radius:50%%;background:var(--brick)}
.brand span{color:var(--taupe);font-size:16px}
</style></head><body>
<div class="card">
  <div class="txt">
    <div class="eyebrow">Этикет</div>
    <h1>Речевой этикет <i>в Китае</i></h1>
    <div class="sub">Вежливость здесь измеряется не количеством вежливых слов, а их уместностью</div>
    <div class="note"><b>Избыток формул читается как неловкость:</b> иностранцы чаще ошибаются в сторону «слишком», а не «мало»</div>
  </div>
  <div class="fan">
%s
    <div class="pivot"></div>
    <div class="cap">У каждой формулы <b>своя ситуация</b>, а не своя степень вежливости</div>
  </div>
  <div class="brand"><span class="bdot"></span><b>Kitai School</b><span>&middot; kitai-school.ru</span></div>
</div>
</body></html>""" % (FONTS, VARS, blades)

open(S + "et-hero.html", "w", encoding="utf-8").write(hero)

# -------------------------------------------------------------- инфографика
WEIGHTS = [
    ("不好意思", "bù hǎoyìsi", "лёгкая", 74, "#1E7A46", "#E3F6E9",
     "Неудобства ещё нет, вы его предупреждаете",
     "просьба, отказ, привлечь внимание, вклиниться в разговор"),
    ("抱歉", "bàoqiàn", "средняя", 104, "#C08A2E", "#FBF2DF",
     "Промежуточный вес: сожаление без тяжёлой вины",
     "опоздание, сорванная договорённость, деловая переписка"),
    ("对不起", "duìbuqǐ", "тяжёлая", 140, "#A41E3A", "#F7E6EB",
     "Нарушение уже произошло, и вы его признаёте",
     "реальный проступок, причинённый ущерб, обида"),
]

cells = "\n".join(
    '<div class="wcell">'
    '  <div class="wtop">'
    '    <div class="weight" style="width:%dpx;height:%dpx;background:%s;border-color:%s">'
    '      <span class="handle" style="border-color:%s"></span>'
    '      <span class="mass" style="color:%s">%s</span>'
    '    </div>'
    '  </div>'
    '  <div class="wname"><span class="han">%s</span><span class="py">%s</span></div>'
    '  <div class="wwhen" style="border-color:%s"><b>%s</b><span>%s</span></div>'
    '</div>' % (w, int(w * 0.8), soft, col, col, col, mass, han, py, col, when, where)
    for han, py, mass, w, col, soft, when, where in WEIGHTS)

info = """<!DOCTYPE html><html lang="ru"><head><meta charset="utf-8">
%s
<style>
%s
*{margin:0;box-sizing:border-box}html,body{width:1200px;height:HGTpx}
.wrap{width:1200px;height:HGTpx;background:linear-gradient(180deg,#fff 0%%,var(--cream) 46%%,var(--cream-2) 100%%);font-family:'Inter',sans-serif;padding:32px 46px 26px;display:flex;flex-direction:column}
.top{display:flex;align-items:flex-end;justify-content:space-between;gap:30px;margin-bottom:18px}
.eyebrow{color:var(--brick);font-weight:700;font-size:14.5px;letter-spacing:.17em;text-transform:uppercase;margin-bottom:7px}
h2{font-family:'Cormorant Garamond',serif;font-weight:600;font-size:40px;line-height:1.07;color:var(--ink);letter-spacing:-.3px}
h2 i{font-style:italic;color:var(--brick)}
.hint{flex:0 0 362px;background:var(--surface);border:1px solid var(--hair);border-left:4px solid var(--brick);border-radius:12px;padding:12px 17px;font-size:14.5px;color:var(--ink-2);line-height:1.36}
.hint b{color:var(--ink)}

.cells{display:flex;gap:20px;align-items:stretch}
.wcell{flex:1 1 0;background:var(--surface);border:1px solid var(--hair);border-radius:14px;padding:16px 18px 16px;box-shadow:0 5px 14px rgba(44,36,32,.05);display:flex;flex-direction:column}
.wtop{height:134px;display:flex;align-items:flex-end;justify-content:center}
.weight{position:relative;border:2px solid;border-radius:7px 7px 11px 11px;clip-path:polygon(16%% 0, 84%% 0, 100%% 100%%, 0 100%%)}
.weight .handle{position:absolute;left:50%%;top:-17px;width:30px;height:20px;margin-left:-15px;border:3px solid;border-bottom:0;border-radius:15px 15px 0 0;background:transparent}
.weight .mass{position:absolute;left:0;right:0;bottom:9px;text-align:center;font-size:13.5px;font-weight:700;text-transform:uppercase;letter-spacing:.05em}
.wname{text-align:center;margin-top:14px}
.wname .han{display:block;font-family:'Noto Serif SC',serif;font-weight:700;font-size:28px;color:var(--ink);line-height:1.2}
.wname .py{display:block;font-size:13.5px;color:var(--taupe);margin-top:4px}
.wwhen{margin-top:13px;border-top:3px solid;padding-top:11px}
.wwhen b{display:block;font-size:14.5px;color:var(--ink);line-height:1.32}
.wwhen span{display:block;font-size:13.5px;color:var(--ink-2);line-height:1.32;margin-top:6px}

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
      <div class="eyebrow">Извинения</div>
      <h2>Три формулы — <i>три разных веса</i></h2>
    </div>
    <div class="hint">Выбор между ними — <b>не вопрос степени вежливости</b>, а вопрос того, что именно произошло: неудобство ещё предстоит или нарушение уже случилось.</div>
  </div>

  <div class="cells">
%s
  </div>

  <div class="foot">
    <div class="msg">Самое частое в речи — лёгкое: <b>不好意思 звучит чаще и в более разных ситуациях</b>, чем 对不起</div>
    <div class="brand"><span class="dot2"></span><b>Kitai School</b><span>&middot; kitai-school.ru</span></div>
  </div>
</div>
</body></html>""" % (FONTS, VARS, cells)

info = info.replace("HGT", "560")
open(S + "et-info.html", "w", encoding="utf-8").write(info)
print("ok")
