# -*- coding: utf-8 -*-
# Новая обложка к статье «Где сдать HSK в России»
# Приём: лестница часовых поясов с запада на восток. Каждая ступень опускается,
# города с несколькими центрами помечены, города без объявленных дат — пунктиром.
import sys
sys.path.insert(0, "/home/user/Kitai-Shool/content")
from gde_sdat import ZONES, CITIES, CITIES_SOON, MULTI, CHECKED

S = ("/tmp/claude-0/-home-user-Kitai-Shool/a463bfca-82a9-56fd-ae09-42a7257ff999/"
     "scratchpad/")

FONTS = ('<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,'
         'wght@0,600;0,700;1,600&family=Inter:wght@400;500;600;700&display=swap" '
         'rel="stylesheet">')
VARS = (":root{--brick:#A41E3A;--brick-d:#841630;--brick-soft:#F7E6EB;--ink:#2C2420;"
        "--ink-2:#5A4F45;--taupe:#8B7D6B;--cream:#FAF7F2;--cream-2:#F3EDE3;--hair:#EAE3D8;"
        "--surface:#fff;--grey-soft:#EFEDE8;--grey:#9A9289}")

# ───────────────────────────────── ступени
steps = ""
for n, (zone, cities) in enumerate(ZONES):
    chips = ""
    for c in cities:
        cls = "ct"
        mark = ""
        if c in CITIES_SOON:
            cls += " soon"
            mark = '<s>даты уточняются</s>'
        elif c in MULTI:
            cls += " multi"
            mark = '<s>центров несколько</s>'
        chips += '<div class="' + cls + '"><b>' + c + '</b>' + mark + '</div>'
    steps += ('<div class="step" style="margin-left:' + str(n * 112) + 'px">'
              '<div class="zn">' + zone + '</div>'
              '<div class="chips">' + chips + '</div></div>')

assert steps.count('class="ct') == 12, "двенадцать городов"
assert steps.count("soon") == len(CITIES_SOON) == 3
assert steps.count("multi") == len(MULTI) == 2

CSS = """
*{margin:0;box-sizing:border-box}html,body{width:1200px;height:630px}
.card{width:1200px;height:630px;position:relative;overflow:hidden;font-family:'Inter',sans-serif;
 background:radial-gradient(1040px 700px at 6% 2%, #fff 0%, var(--cream) 56%, var(--cream-2) 100%);
 padding:26px 48px 26px 64px;display:flex;flex-direction:column}
.card:before{content:"";position:absolute;left:0;top:0;bottom:0;width:12px;background:var(--brick)}
.head{display:flex;justify-content:space-between;align-items:flex-end;gap:30px;margin-bottom:14px}
.eyebrow{color:var(--brick);font-weight:700;font-size:17px;letter-spacing:.19em;
 text-transform:uppercase;margin-bottom:7px}
h1{font-family:'Cormorant Garamond',serif;font-weight:600;font-size:41px;line-height:1.06;
 color:var(--ink);letter-spacing:-.3px;max-width:30ch}
h1 i{font-style:italic;color:var(--brick)}
.tip{flex:0 0 330px;background:var(--surface);border:1px solid var(--hair);
 border-left:4px solid var(--brick);border-radius:13px;padding:11px 16px;font-size:14px;
 color:var(--ink-2);line-height:1.36}
.tip b{color:var(--ink)}
.stage{flex:1 1 auto;position:relative;margin-top:2px}
.axis{position:absolute;left:0;right:0;top:16px;height:2px;background:var(--hair)}
.wnames{display:flex;justify-content:space-between;font-size:12px;font-weight:700;
 letter-spacing:.14em;text-transform:uppercase;color:var(--taupe);margin-bottom:6px}
.step{display:flex;align-items:center;gap:12px;margin-top:8px}
.zn{flex:0 0 140px;font-size:13px;font-weight:700;letter-spacing:.09em;text-transform:uppercase;
 color:var(--brick);border-left:3px solid var(--brick);padding-left:9px;line-height:1.15}
.chips{display:flex;gap:9px}
.ct{background:var(--surface);border:1px solid var(--brick);border-radius:11px;
 padding:9px 18px 8px;line-height:1.1}
.ct b{display:block;font-size:18px;font-weight:600;color:var(--ink)}
.ct s{display:block;text-decoration:none;font-size:11px;letter-spacing:.05em;
 text-transform:uppercase;color:var(--brick);margin-top:3px;font-weight:700}
.ct.multi{background:var(--brick-soft)}
.ct.soon{border:1px dashed var(--grey);background:transparent}
.ct.soon b{color:var(--taupe)}
.ct.soon s{color:var(--grey)}
.foot{display:flex;align-items:center;gap:14px;margin-top:10px;border-top:1px solid var(--hair);
 padding-top:11px}
.foot .lb{font-size:12px;font-weight:700;letter-spacing:.11em;text-transform:uppercase;
 color:var(--taupe)}
.foot .vl{font-size:14px;color:var(--ink-2)}
.foot .vl b{color:var(--ink)}
"""
# CSS собирается склейкой, без форматирования через %, поэтому проценты тут настоящие

hero = ("<!DOCTYPE html><html lang=\"ru\"><head><meta charset=\"utf-8\">" + FONTS
        + "<style>" + VARS + CSS + "</style></head><body><div class=\"card\">"
        + '<div class="head"><div>'
        + '<div class="eyebrow">Где сдать</div>'
        + '<h1>Экзамен принимают <i>в двенадцати городах</i> — от Петербурга '
          'до Владивостока</h1></div>'
        + '<div class="tip"><b>Это не все центры страны.</b> Это города, чьи центры '
          'объявили даты на осень к моменту нашей сверки</div></div>'
        + '<div class="stage">'
        + '<div class="wnames"><span>запад</span><span>восток</span></div>'
        + steps
        + '</div>'
        + '<div class="foot"><span class="lb">Сверка</span>'
        + '<span class="vl">расписание центров по состоянию на <b>' + CHECKED + '</b></span>'
        + '<span class="lb">Адресов нет</span>'
        + '<span class="vl">список площадок устаревает за сезон</span></div>'
        + "</div></body></html>")

for city in [c for z, cs in ZONES for c in cs]:
    assert city in hero, "город %s попал на обложку" % city
assert CHECKED in hero, "дата сверки на обложке"

open(S + "gdesdat2-hero.html", "w", encoding="utf-8").write(hero)
print("готово: gdesdat2-hero.html")
