# -*- coding: utf-8 -*-
# Картинки к статье «Медицинское образование в Китае»
# Обложка    — формула срока: 5 + 3, и отдельно 6 для иностранцев
# Инфографика — три корочки: какие документы получают и что каждый даёт
S = "/tmp/claude-0/-home-user-Kitai-Shool/a463bfca-82a9-56fd-ae09-42a7257ff999/scratchpad/"

FONTS = ("<link href=\"https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,600;0,700;1,600"
         "&family=Inter:wght@400;500;600;700&family=Noto+Serif+SC:wght@600;700&display=swap\" rel=\"stylesheet\">")
VARS = (":root{--brick:#A41E3A;--brick-d:#841630;--brick-soft:#F7E6EB;--ink:#2C2420;--ink-2:#5A4F45;"
        "--taupe:#8B7D6B;--cream:#FAF7F2;--cream-2:#F3EDE3;--hair:#EAE3D8;--surface:#fff;"
        "--green:#1E7A46;--green-soft:#E3F6E9;--amber:#C08A2E;--amber-s:#FBF2DF;--blue:#2F5D8C;--blue-s:#E7EEF6}")

# ------------------------------------------------------------------ обложка
hero = """<!DOCTYPE html><html lang="ru"><head><meta charset="utf-8">
%s
<style>
%s
*{margin:0;box-sizing:border-box}html,body{width:1200px;height:630px}
.card{width:1200px;height:630px;background:radial-gradient(1100px 680px at 16%% 8%%, #fff 0%%, var(--cream) 54%%, var(--cream-2) 100%%);position:relative;overflow:hidden;font-family:'Inter',sans-serif;display:flex;align-items:center;justify-content:space-between;padding:0 64px 0 72px}
.card:before{content:"";position:absolute;left:0;top:0;bottom:0;width:12px;background:var(--brick)}
.txt{flex:0 0 490px}
.eyebrow{color:var(--brick);font-weight:700;font-size:18px;letter-spacing:.19em;text-transform:uppercase;margin-bottom:12px}
h1{font-family:'Cormorant Garamond',serif;font-weight:600;font-size:50px;line-height:1.06;color:var(--ink);letter-spacing:-.4px;max-width:470px}
h1 i{font-style:italic;color:var(--brick)}
.sub{font-size:18px;color:var(--ink-2);line-height:1.42;max-width:31ch;margin-top:17px}
.brand{position:absolute;left:72px;bottom:32px;display:flex;align-items:center;gap:11px;color:var(--ink)}
.brand b{font-family:'Cormorant Garamond',serif;font-weight:700;font-size:26px}
.brand .bdot{width:10px;height:10px;border-radius:50%%;background:var(--brick)}
.brand span{color:var(--taupe);font-size:16px}

/* формула срока */
.art{flex:0 0 536px;background:var(--surface);border:1px solid var(--hair);border-radius:22px;padding:30px 34px 26px;box-shadow:0 16px 38px rgba(44,36,32,.12)}
.form{display:flex;align-items:flex-start;justify-content:center;gap:16px}
.term{flex:0 0 auto;text-align:center;width:196px}
.term .n{font-family:'Cormorant Garamond',serif;font-weight:700;font-size:112px;line-height:.92;color:var(--brick)}
.term .k{font-size:13px;font-weight:700;letter-spacing:.1em;text-transform:uppercase;color:var(--ink);margin-top:8px;min-height:34px}
.term .h{font-family:'Noto Serif SC',serif;font-weight:700;font-size:16px;color:var(--taupe);margin-top:3px}
.plus{font-family:'Cormorant Garamond',serif;font-weight:600;font-size:62px;color:var(--taupe);line-height:1;padding-top:26px}
.rule{height:1px;background:var(--hair);margin:20px 0 16px}
.alt{display:flex;align-items:center;gap:14px;background:var(--blue-s);border:1px solid #C9D8E8;border-radius:14px;padding:12px 18px}
.alt .n{font-family:'Cormorant Garamond',serif;font-weight:700;font-size:44px;color:var(--blue);line-height:1}
.alt .t{font-size:15px;color:var(--ink-2);line-height:1.34}
.alt .t b{color:var(--ink)}
</style></head><body>
<div class="card">
  <div class="txt">
    <div class="eyebrow">Медицина</div>
    <h1>Медицинское образование <i>в Китае</i></h1>
    <div class="sub">Срок здесь считают не годами, а ступенями — и диплом в конце пятого года ещё не даёт права лечить</div>
  </div>
  <div class="art">
    <div class="form">
      <div class="term"><div class="n">5</div><div class="k">БАКАЛАВРИАТ</div><div class="h">本科</div></div>
      <div class="plus">+</div>
      <div class="term"><div class="n">3</div><div class="k">МАГИСТРАТУРА<br>И ОРДИНАТУРА</div><div class="h">规培</div></div>
    </div>
    <div class="rule"></div>
    <div class="alt">
      <span class="n">6</span>
      <span class="t">столько длится <b>англоязычная программа</b> для иностранцев</span>
    </div>
  </div>
  <div class="brand"><span class="bdot"></span><b>Kitai School</b><span>&middot; kitai-school.ru</span></div>
</div>
</body></html>""" % (FONTS, VARS)

open(S + "md-hero.html", "w", encoding="utf-8").write(hero)

# -------------------------------------------------------------- инфографика
DOCS = [
    ("a", "毕业证 + 学位证", "Диплом бакалавра", "после пятого года",
     "законченное высшее по клинической медицине", "права лечить"),
    ("b", "规培合格证", "Сертификат об ординатуре", "после трёх лет 规培",
     "пройденную клиническую подготовку", "сам по себе — допуска к практике"),
    ("c", "医师资格证", "Квалификационный документ врача", "после сдачи 医师资格考试",
     "квалификацию врача — то, ради чего весь путь", None),
]

cards = "\n".join(
    '<div class="doc %s">'
    '<div class="dh"><span class="cn">%s</span></div>'
    '<div class="db">'
    '<div class="ru">%s</div>'
    '<div class="fld"><span class="k">КОГДА</span><span class="v">%s</span></div>'
    '<div class="fld"><span class="k">ПОДТВЕРЖДАЕТ</span><span class="v">%s</span></div>'
    '%s'
    '</div></div>' % (
        c, cn, ru, when, what,
        ('<div class="fld no"><span class="k">НЕ ДАЁТ</span><span class="v">%s</span></div>' % nope)
        if nope else '<div class="fld fin"><span class="k">ЧТО ДАЛЬШЕ</span><span class="v">с него начинается допуск к работе</span></div>')
    for c, cn, ru, when, what, nope in DOCS)

info = """<!DOCTYPE html><html lang="ru"><head><meta charset="utf-8">
%s
<style>
%s
*{margin:0;box-sizing:border-box}html,body{width:1200px;height:HGTpx}
.wrap{width:1200px;height:HGTpx;background:linear-gradient(180deg,#fff 0%%,var(--cream) 46%%,var(--cream-2) 100%%);font-family:'Inter',sans-serif;padding:32px 46px 26px;display:flex;flex-direction:column}
.top{display:flex;align-items:flex-end;justify-content:space-between;gap:30px;margin-bottom:26px}
.eyebrow{color:var(--brick);font-weight:700;font-size:14.5px;letter-spacing:.17em;text-transform:uppercase;margin-bottom:7px}
h2{font-family:'Cormorant Garamond',serif;font-weight:600;font-size:40px;line-height:1.07;color:var(--ink);letter-spacing:-.3px}
h2 i{font-style:italic;color:var(--brick)}
.hint{flex:0 0 348px;background:var(--surface);border:1px solid var(--hair);border-left:4px solid var(--brick);border-radius:12px;padding:12px 17px;font-size:14.5px;color:var(--ink-2);line-height:1.36}
.hint b{color:var(--ink)}

.row{display:flex;gap:22px;align-items:stretch;justify-content:center;padding:6px 0 10px}
.doc{flex:1 1 0;background:var(--surface);border:1px solid var(--hair);border-radius:14px;overflow:hidden;box-shadow:0 12px 26px rgba(44,36,32,.12)}
.doc.a{transform:rotate(-2.2deg)}
.doc.b{transform:rotate(.8deg)}
.doc.c{transform:rotate(2.4deg);border-color:var(--brick)}
.dh{padding:13px 16px;background:var(--cream-2);border-bottom:1px solid var(--hair)}
.doc.c .dh{background:var(--brick);border-bottom-color:var(--brick)}
.dh .cn{font-family:'Noto Serif SC',serif;font-weight:700;font-size:21px;color:var(--ink)}
.doc.c .dh .cn{color:#fff}
.db{padding:14px 16px 16px}
.ru{font-size:17px;font-weight:600;color:var(--ink);line-height:1.25;margin-bottom:12px;min-height:42px}
.fld{border-top:1px dotted var(--hair);padding:8px 0 0;margin-top:8px}
.fld:first-of-type{border-top:0;padding-top:0;margin-top:0}
.fld .k{display:block;font-size:10.5px;font-weight:700;letter-spacing:.11em;color:var(--taupe)}
.fld .v{display:block;font-size:14.5px;color:var(--ink-2);line-height:1.36;margin-top:3px}
.fld.no .k{color:var(--brick)}
.fld.no .v{color:var(--ink)}
.fld.fin .k{color:var(--green)}
.fld.fin .v{color:var(--ink)}

.foot{margin-top:auto;display:flex;align-items:center;gap:18px;padding-top:16px}
.foot .msg{flex:1 1 auto;background:var(--brick-soft);border:1px solid var(--brick);border-radius:14px;padding:12px 21px;font-size:16px;color:var(--ink);line-height:1.34}
.foot .msg b{color:var(--brick)}
.brand{display:flex;align-items:center;gap:10px;color:var(--ink);flex:0 0 auto}
.brand b{font-family:'Cormorant Garamond',serif;font-weight:700;font-size:23px}
.brand .dot2{width:9px;height:9px;border-radius:50%%;background:var(--brick)}
.brand span{color:var(--taupe);font-size:15px}
</style></head><body>
<div class="wrap">
  <div class="top">
    <div>
      <div class="eyebrow">Что получают на выходе</div>
      <h2>Путь считают <i>не годами, а корочками</i></h2>
    </div>
    <div class="hint">Документов три, и они приходят в разное время. <b>Наличие первого не означает двух остальных</b> — именно здесь чаще всего ломаются расчёты.</div>
  </div>

  <div class="row">
%s
  </div>

  <div class="foot">
    <div class="msg">Считать стоит <b>не до выпуска, а до третьего документа</b>: именно он открывает практику</div>
    <div class="brand"><span class="dot2"></span><b>Kitai School</b><span>&middot; kitai-school.ru</span></div>
  </div>
</div>
</body></html>""" % (FONTS, VARS, cards)

info = info.replace("HGT", "632")
open(S + "md-info.html", "w", encoding="utf-8").write(info)
print("ok")
