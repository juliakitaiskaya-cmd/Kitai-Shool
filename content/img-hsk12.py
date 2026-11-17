# -*- coding: utf-8 -*-
# Новая обложка к статье «Как проходит экзамен HSK»
# Приём: четыре полосы длиной по времени экзамена. Внутри полосы — разделы,
# письмо выделено отдельным куском. Справа — вопросы, максимум и порог.
import sys
sys.path.insert(0, "/home/user/Kitai-Shool/content")
from hsk1 import STRUCT, WRITE_MIN, MINUTES, QUEST, SWITCH

S = ("/tmp/claude-0/-home-user-Kitai-Shool/a463bfca-82a9-56fd-ae09-42a7257ff999/"
     "scratchpad/")

FONTS = ('<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,'
         'wght@0,600;0,700;1,600&family=Inter:wght@400;500;600;700&display=swap" '
         'rel="stylesheet">')
VARS = (":root{--brick:#A41E3A;--brick-d:#841630;--brick-soft:#F7E6EB;--ink:#2C2420;"
        "--ink-2:#5A4F45;--taupe:#8B7D6B;--cream:#FAF7F2;--cream-2:#F3EDE3;--hair:#EAE3D8;"
        "--surface:#fff;--grey-soft:#EFEDE8;--grey:#9A9289}")

FULL = 570.0                      # пикселей на самый длинный экзамен
MAXM = max(MINUTES.values())
assert MAXM == 105, "самый длинный из четырёх — четвёртый уровень"

rows = ""
for lvl, sect, quest, mins, mx, thr, wr in STRUCT:
    w = int(round(FULL * mins / MAXM))
    wrw = int(round(FULL * wr / MAXM)) if wr else 0
    inner = ""
    if wr:
        inner = ('<span class="rest">аудирование и чтение</span>'
                 '<span class="wr" style="flex:0 0 ' + str(wrw) + 'px">письмо ' + str(wr)
                 + ' мин</span>')
    else:
        inner = '<span class="rest">аудирование и чтение</span>'
    rows += ('<div class="row">'
             '<div class="lv">HSK ' + str(lvl) + '</div>'
             '<div class="bar" style="width:' + str(w) + 'px">' + inner + '</div>'
             '<div class="mins">' + str(mins) + ' мин</div>'
             '<div class="qs"><b>' + str(quest) + '</b> вопросов · '
             + str(sect) + ' раздела</div>'
             '<div class="sc"><b>' + str(thr) + '</b> из ' + str(mx) + '</div>'
             '</div>')

assert rows.count('class="row"') == 4
assert rows.count('class="wr"') == len(WRITE_MIN) == 2, "письмо есть только на двух уровнях"
assert "раздела" in rows

CSS = """
*{margin:0;box-sizing:border-box}html,body{width:1200px;height:630px}
.card{width:1200px;height:630px;position:relative;overflow:hidden;font-family:'Inter',sans-serif;
 background:radial-gradient(1040px 700px at 6% 2%, #fff 0%, var(--cream) 56%, var(--cream-2) 100%);
 padding:28px 48px 24px 64px;display:flex;flex-direction:column}
.card:before{content:"";position:absolute;left:0;top:0;bottom:0;width:12px;background:var(--brick)}
.head{display:flex;justify-content:space-between;align-items:flex-end;gap:30px;margin-bottom:22px}
.eyebrow{color:var(--brick);font-weight:700;font-size:17px;letter-spacing:.19em;
 text-transform:uppercase;margin-bottom:7px}
h1{font-family:'Cormorant Garamond',serif;font-weight:600;font-size:42px;line-height:1.07;
 color:var(--ink);letter-spacing:-.3px;max-width:22ch}
h1 i{font-style:italic;color:var(--brick)}
.tip{flex:0 0 322px;background:var(--surface);border:1px solid var(--hair);
 border-left:4px solid var(--brick);border-radius:13px;padding:12px 17px;font-size:14px;
 color:var(--ink-2);line-height:1.36}
.tip b{color:var(--ink)}
.rows{flex:1 1 auto;display:flex;flex-direction:column;justify-content:center;gap:26px}
.row{display:flex;align-items:center;gap:12px}
.lv{flex:0 0 74px;font-size:19px;font-weight:700;color:var(--brick);letter-spacing:.02em}
.bar{height:58px;border-radius:11px;overflow:hidden;display:flex;align-items:stretch;
 border:1px solid var(--brick);background:var(--surface);flex:0 0 auto}
.rest{flex:1 1 auto;display:flex;align-items:center;padding-left:14px;font-size:13.5px;
 color:var(--ink-2);background:var(--brick-soft);white-space:nowrap;overflow:hidden}
.wr{display:flex;align-items:center;justify-content:center;background:var(--brick);color:#fff;
 font-size:12.5px;padding:0 6px;font-weight:600;white-space:nowrap}
.mins{flex:0 0 70px;font-size:17px;font-weight:700;color:var(--ink)}
.qs{flex:0 0 200px;font-size:14px;color:var(--ink-2)}
.qs b{color:var(--ink);font-size:16px}
.sc{flex:0 0 116px;font-size:14px;color:var(--taupe)}
.sc b{color:var(--brick);font-size:16px}
.foot{display:flex;align-items:center;gap:14px;margin-top:auto;border-top:1px solid var(--hair);
 padding-top:12px}
.foot .lb{font-size:12px;font-weight:700;letter-spacing:.11em;text-transform:uppercase;
 color:var(--taupe);flex:0 0 auto}
.foot .vl{font-size:14px;color:var(--ink-2)}
.foot .vl b{color:var(--ink)}
"""

hero = ('<!DOCTYPE html><html lang="ru"><head><meta charset="utf-8">' + FONTS
        + "<style>" + VARS + CSS + "</style></head><body><div class=\"card\">"
        + '<div class="head"><div>'
        + '<div class="eyebrow">Как проходит экзамен</div>'
        + '<h1>Разделы идут подряд: <i>от сорока минут</i> до ста пяти</h1></div>'
        + '<div class="tip"><b>Порог везде один</b> — три пятых от максимума, '
          'и отдельных порогов по разделам нет</div></div>'
        + '<div class="rows">' + rows + '</div>'
        + '<div class="foot"><span class="lb">Редакция</span>'
        + '<span class="vl">числа по действующей, время общее и примерное</span>'
        + '<span class="lb">Переход</span>'
        + '<span class="vl">с <b>' + SWITCH + '</b> сдают по новому стандарту</span></div>'
        + "</div></body></html>")

for lvl in (1, 2, 3, 4):
    assert "HSK " + str(lvl) in hero, "уровень %d на обложке" % lvl
assert SWITCH in hero and "три пятых" in hero

open(S + "hsk12-hero.html", "w", encoding="utf-8").write(hero)
print("готово: hsk12-hero.html")
