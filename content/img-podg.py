# -*- coding: utf-8 -*-
# Картинки к статье «Подготовка к HSK: материалы, приложения и упражнения»
# Обложка     — четыре полосы покрытия: что часть набора закрывает и чего не закрывает
# Инфографика — лента из трёх проходов по одной записи, с отметкой, где расшифровка
import sys
sys.path.insert(0, "/home/user/Kitai-Shool/content")
from podg import KIT, PASSES

S = ("/tmp/claude-0/-home-user-Kitai-Shool/a463bfca-82a9-56fd-ae09-42a7257ff999/"
     "scratchpad/")

FONTS = ('<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,'
         'wght@0,600;0,700;1,600&family=Inter:wght@400;500;600;700&display=swap" '
         'rel="stylesheet">')
VARS = (":root{--brick:#A41E3A;--brick-d:#841630;--brick-soft:#F7E6EB;--ink:#2C2420;"
        "--ink-2:#5A4F45;--taupe:#8B7D6B;--cream:#FAF7F2;--cream-2:#F3EDE3;--hair:#EAE3D8;"
        "--surface:#fff;--grey-soft:#EFEDE8;--grey:#9A9289}")

BASE = """
*{margin:0;box-sizing:border-box}
.card{position:relative;overflow:hidden;font-family:'Inter',sans-serif;
 background:radial-gradient(1040px 700px at 6% 2%, #fff 0%, var(--cream) 56%, var(--cream-2) 100%);
 display:flex;flex-direction:column}
.card:before{content:"";position:absolute;left:0;top:0;bottom:0;width:12px;background:var(--brick)}
.eyebrow{color:var(--brick);font-weight:700;font-size:17px;letter-spacing:.19em;
 text-transform:uppercase;margin-bottom:7px}
h1{font-family:'Cormorant Garamond',serif;font-weight:600;line-height:1.06;
 color:var(--ink);letter-spacing:-.3px}
h1 i{font-style:italic;color:var(--brick)}
.tip{background:var(--surface);border:1px solid var(--hair);border-left:4px solid var(--brick);
 border-radius:13px;padding:12px 17px;font-size:14px;color:var(--ink-2);line-height:1.36}
.tip b{color:var(--ink)}
.foot{display:flex;align-items:center;gap:14px;margin-top:auto;border-top:1px solid var(--hair);
 padding-top:12px}
.foot .lb{font-size:12px;font-weight:700;letter-spacing:.11em;text-transform:uppercase;
 color:var(--taupe);flex:0 0 auto}
.foot .vl{font-size:14px;color:var(--ink-2)}
.foot .vl b{color:var(--ink)}
"""

# ───────────────────────── обложка: четыре полосы покрытия ─────────────────────────
bars = ""
for name, yes, no in KIT:
    bars += ('<div class="kr">'
             '<div class="nm">' + name + '</div>'
             '<div class="cov"><div class="yes"><s>закрывает</s>' + yes + '</div>'
             '<div class="no"><s>не закрывает</s>' + no + '</div></div>'
             '</div>')
assert bars.count('class="kr"') == 4
assert bars.count("закрывает") == 8, "у каждой части обе стороны"

HERO_CSS = BASE + """
html,body{width:1200px;height:630px}
.card{width:1200px;height:630px;padding:26px 48px 22px 64px}
.head{display:flex;justify-content:space-between;align-items:flex-end;gap:30px;margin-bottom:18px}
h1{font-size:40px;max-width:24ch}
.tip{flex:0 0 322px}
.bars{flex:1 1 auto;display:flex;flex-direction:column;justify-content:center;gap:16px}
.kr{display:flex;align-items:stretch;gap:14px}
.nm{flex:0 0 196px;display:flex;align-items:center;font-size:17px;font-weight:600;
 color:var(--ink);line-height:1.2;border-left:3px solid var(--brick);padding-left:12px}
.cov{flex:1 1 auto;display:flex;align-items:stretch;gap:10px}
.yes,.no{flex:1 1 0;border-radius:11px;padding:10px 15px;font-size:14.5px;line-height:1.3}
.yes{background:var(--brick-soft);border:1px solid var(--brick);color:var(--ink)}
.no{background:transparent;border:1px dashed var(--grey);color:var(--taupe)}
.yes s,.no s{display:block;text-decoration:none;font-size:11px;font-weight:700;
 letter-spacing:.11em;text-transform:uppercase;margin-bottom:4px}
.yes s{color:var(--brick)}
.no s{color:var(--grey)}
"""

hero = ('<!DOCTYPE html><html lang="ru"><head><meta charset="utf-8">' + FONTS
        + "<style>" + VARS + HERO_CSS + "</style></head><body><div class=\"card\">"
        + '<div class="head"><div>'
        + '<div class="eyebrow">Подготовка к экзамену</div>'
        + '<h1>Набор из четырёх частей: <i>у каждой своя работа</i></h1></div>'
        + '<div class="tip"><b>Правый столбец важнее левого.</b> Дыры в подготовке '
          'появляются там, где ни одна часть ничего не закрывает</div></div>'
        + '<div class="bars">' + bars + '</div>'
        + '<div class="foot"><span class="lb">Проверка набора</span>'
        + '<span class="vl">если две вещи делают одну работу, <b>одна лишняя</b></span>'
        + '<span class="lb">Чаще всего пусто</span>'
        + '<span class="vl">в слухе</span></div>'
        + "</div></body></html>")

# ───────────────────────── инфографика: три прохода ─────────────────────────
steps = ""
for i, (num, what, got) in enumerate(PASSES):
    tag = "без расшифровки"
    cls = "pa"
    if i == 1:
        tag = "с расшифровкой"
        cls = "pa mid"
    if i == 2:
        tag = "без расшифровки, через день"
    steps += ('<div class="' + cls + '">'
              '<div class="hd"><b>' + num + ' проход</b><s>' + tag + '</s></div>'
              '<div class="wt">' + what + '</div>'
              '<div class="gt"><i>что получаем</i>' + got + '</div>'
              '</div>')
    if i < 2:
        steps += '<div class="arw"></div>'
assert steps.count('class="pa') == 3 and steps.count('class="arw"') == 2
assert steps.count("<s>с расшифровкой</s>") == 1, "метка «с расшифровкой» только на втором проходе"
assert steps.count("<s>без расшифровки") == 2, "на первом и третьем проходе расшифровки нет"

FIG_CSS = BASE + """
html,body{width:1200px;height:450px}
.card{width:1200px;height:450px;padding:26px 48px 22px 64px}
.head{display:flex;justify-content:space-between;align-items:flex-end;gap:30px;margin-bottom:16px}
h1{font-size:34px;max-width:25ch}
.tip{flex:0 0 330px}
.flow{flex:1 1 auto;display:flex;align-items:center;gap:0;margin-bottom:14px}
.pa{flex:1 1 0;background:var(--surface);border:1px solid var(--hair);border-radius:15px;
 padding:16px 20px;display:flex;flex-direction:column;align-self:stretch}
.pa.mid{border:2px solid var(--brick);background:var(--brick-soft)}
.hd{margin-bottom:12px}
.hd b{display:block;font-size:21px;font-weight:600;color:var(--ink);margin-bottom:6px}
.hd s{display:inline-block;text-decoration:none;font-size:11.5px;font-weight:700;
 letter-spacing:.09em;text-transform:uppercase;color:var(--brick);background:var(--surface);
 border:1px solid var(--brick);border-radius:7px;padding:4px 10px}
.pa.mid .hd s{background:var(--brick);color:#fff;border-color:var(--brick)}
.wt{font-size:15.5px;color:var(--ink-2);line-height:1.42}
.gt{margin-top:16px;padding-top:12px;border-top:1px solid var(--hair);font-size:14.5px;
 color:var(--ink);line-height:1.38}
.gt i{display:block;font-style:normal;font-size:11px;font-weight:700;letter-spacing:.11em;
 text-transform:uppercase;color:var(--taupe);margin-bottom:5px}
.arw{flex:0 0 46px;align-self:center;height:2px;background:var(--brick);position:relative}
.arw:after{content:"";position:absolute;right:0;top:-5px;border-left:11px solid var(--brick);
 border-top:6px solid transparent;border-bottom:6px solid transparent}
"""

fig = ('<!DOCTYPE html><html lang="ru"><head><meta charset="utf-8">' + FONTS
       + "<style>" + VARS + FIG_CSS + "</style></head><body><div class=\"card\">"
       + '<div class="head"><div>'
       + '<div class="eyebrow">Аудирование самому</div>'
       + '<h1>Три прохода <i>по одной записи</i>, а не десять записей по разу</h1></div>'
       + '<div class="tip"><b>Расшифровка — только во втором проходе.</b> Именно поэтому '
         'третий проход работает как проверка</div></div>'
       + '<div class="flow">' + steps + '</div>'
       + '<div class="foot"><span class="lb">Счёт</span>'
       + '<span class="vl">в зачёт идут <b>разобранные</b> записи, а не прослушанные</span>'
       + '<span class="lb">Третий проход</span>'
       + '<span class="vl">делают через день, а не сразу</span></div>'
       + "</div></body></html>")

open(S + "podg-hero.html", "w", encoding="utf-8").write(hero)
open(S + "podg-info.html", "w", encoding="utf-8").write(fig)
print("готово: podg-hero.html, podg-info.html")
