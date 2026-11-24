# -*- coding: utf-8 -*-
# Картинки к статье «Какой уровень HSK нужен для поступления»
# Обложка     — пять ступеней лестницей, у каждой свой экзамен
# Инфографика — две полосы в масштабе словника: путь до четвёртого и прибавка до пятого
import sys
sys.path.insert(0, "/home/user/Kitai-Shool/content")
from postup import (STAGES, HSK, ENG, NONE, WORDS, WORDS_LOW, WORDS_HIGH,
                    STEP_UP, SHARE, FREE_LEVEL, FREE_STEP, HSK_STAGES, NO_HSK)

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
.foot{display:flex;align-items:center;gap:14px;margin-top:auto;border-top:1px solid var(--hair);
 padding-top:12px}
.foot .lb{font-size:12px;font-weight:700;letter-spacing:.11em;text-transform:uppercase;
 color:var(--taupe);flex:0 0 auto}
.foot .vl{font-size:14px;color:var(--ink-2)}
.foot .vl b{color:var(--ink)}
"""

# ───────────────────── обложка: пять ступеней ─────────────────────
SHORT = {
    "Языковой год и курсы": "Языковой год",
    "Бакалавриат на китайском": "Бакалавриат на китайском",
    "Более требовательные программы": "Более требовательные программы",
    "Магистратура на китайском": "Магистратура на китайском",
    "Программы на английском": "Программы на английском",
}
assert set(SHORT) == {s[0] for s in STAGES}

# снизу вверх: языковой год, бакалавриат, сильные вузы, магистратура,
# а программы на английском стоят сбоку — они не на этой лестнице
STAIRS = [s for s in STAGES if s[1] != ENG]
ASIDE = [s for s in STAGES if s[1] == ENG]
assert len(STAIRS) == 4 and len(ASIDE) == 1

# высота ступени задаётся уровнем, а не порядком: у двух ступеней с пятым
# уровнем высота одинаковая, иначе картинка говорила бы не то, что текст
H_BY_LVL = {None: 150, 4: 238, 5: 326}
assert len({H_BY_LVL[s[2]] for s in STAIRS}) == 3, "три разные высоты на четыре ступени"

steps_html = ""
for name, exam, lvl, note in STAIRS:
    h = H_BY_LVL[lvl]
    if exam == NONE:
        tag, cls = "экзамен не нужен", "none"
    else:
        tag, cls = "HSK %d" % lvl, "hsk"
    steps_html += ('<div class="st ' + cls + '" style="height:' + str(h) + 'px">'
                   '<div class="tag">' + tag + '</div>'
                   '<div class="nm">' + SHORT[name] + "</div></div>")
assert steps_html.count('class="st ') == 4

HERO_CSS = BASE + """
html,body{width:1200px;height:630px}
.card{width:1200px;height:630px;padding:28px 48px 20px 64px}
h1{font-size:42px;max-width:31ch;margin-bottom:6px}
.sub{font-size:17px;color:var(--ink-2);margin-bottom:16px}
.row{flex:1 1 auto;display:flex;align-items:flex-end;gap:26px}
.stairs{flex:1 1 auto;display:flex;align-items:flex-end;gap:12px}
.st{flex:1 1 0;border-radius:12px 12px 0 0;padding:14px 12px 0;display:flex;
 flex-direction:column;align-items:center;text-align:center}
.st.none{background:var(--grey-soft);border:1px solid var(--hair);border-bottom:none}
.st.hsk{background:var(--brick-soft);border:1px solid #E8C3CF;border-bottom:none}
.tag{font-size:17px;font-weight:700;color:var(--brick-d)}
.st.none .tag{color:var(--taupe);font-size:14px}
.nm{font-size:13.5px;color:var(--ink-2);line-height:1.25;margin-top:8px}
.aside{flex:0 0 268px;background:var(--surface);border:1px solid var(--hair);
 border-left:4px solid var(--grey);border-radius:14px;padding:16px 18px}
.aside .at{font-size:13px;font-weight:700;letter-spacing:.06em;text-transform:uppercase;
 color:var(--taupe)}
.aside .an{font-size:19px;font-weight:700;color:var(--ink);margin-top:6px;line-height:1.2}
.aside .ad{font-size:14px;color:var(--ink-2);line-height:1.35;margin-top:9px}
"""

hero = ('<!DOCTYPE html><html lang="ru"><head><meta charset="utf-8">' + FONTS
        + "<style>" + VARS + HERO_CSS + "</style></head><body><div class=\"card\">"
        + '<div class="eyebrow">Уровень HSK для поступления</div>'
        + '<h1>Экзамен выбирает <i>язык программы, а не страна</i></h1>'
        + '<div class="sub">Ступени обучения на китайском — и те, где HSK '
          'не спрашивают вовсе</div>'
        + '<div class="row"><div class="stairs">' + steps_html + '</div>'
        + '<div class="aside"><div class="at">Отдельно</div>'
          '<div class="an">Программы на английском</div>'
          '<div class="ad">HSK не нужен: язык программы подтверждают международным '
          'сертификатом по английскому</div></div></div>'
        + '<div class="foot"><span class="lb">Порог ставит</span>'
        + '<span class="vl"><b>конкретная программа</b>, а не страна и не центр '
          'тестирования</span>'
        + '<span class="lb">Сводка</span>'
        + '<span class="vl">по нашим разборам поступления</span></div>'
        + "</div></body></html>")

# ───────────────────── инфографика: две полосы ─────────────────────
BAR_MAX = 880.0
w_low = int(round(BAR_MAX * WORDS_LOW / float(WORDS_HIGH)))
w_up = int(round(BAR_MAX * STEP_UP / float(WORDS_HIGH)))
assert w_low + w_up == BAR_MAX or abs(w_low + w_up - BAR_MAX) <= 1

FIG_CSS = BASE + """
html,body{width:1200px;height:520px}
.card{width:1200px;height:520px;padding:22px 48px 14px 64px}
.head{display:flex;justify-content:space-between;align-items:flex-start;gap:34px;
 margin-bottom:18px}
h1{font-size:30px;max-width:31ch}
.tip{background:var(--surface);border:1px solid var(--hair);border-left:4px solid var(--brick);
 border-radius:13px;padding:10px 15px;font-size:13px;color:var(--ink-2);line-height:1.33;
 flex:0 0 300px}
.tip b{color:var(--ink)}
.bars{flex:1 1 auto;display:flex;flex-direction:column;justify-content:center;gap:46px}
.br{display:flex;align-items:center;gap:20px}
.bl{flex:0 0 232px;font-size:14px;color:var(--ink-2);line-height:1.3}
.bl b{display:block;font-size:19px;color:var(--ink);margin-bottom:4px}
.bar{height:88px;border-radius:13px;display:flex;align-items:center;padding:0 24px;
 font-size:28px;font-weight:700;color:#fff}
.bar.a{background:linear-gradient(90deg,#B8304B 0%,var(--brick) 100%)}
.bar.b{background:linear-gradient(90deg,#C9637A 0%,#B8304B 100%)}
.note{font-size:15px;color:var(--ink-2);margin-left:20px;line-height:1.3}
.note b{color:var(--brick-d);font-size:24px}
"""

fig = ('<!DOCTYPE html><html lang="ru"><head><meta charset="utf-8">' + FONTS
       + "<style>" + VARS + FIG_CSS + "</style></head><body><div class=\"card\">"
       + '<div class="head"><div>'
       + '<div class="eyebrow">Что стоит за «уровнем выше»</div>'
       + '<h1>Один шаг по названию — <i>восемьдесят процентов по работе</i></h1></div>'
       + '<div class="tip"><b>Полосы в одном масштабе.</b> Длина — число слов '
         'по словнику действующего стандарта</div></div>'
       + '<div class="bars">'
       + '<div class="br"><div class="bl"><b>С нуля до HSK 4</b>'
         'весь путь до требования большинства программ</div>'
       + '<div class="bar a" style="width:' + str(w_low) + 'px">'
       + str(WORDS_LOW) + ' слов</div></div>'
       + '<div class="br"><div class="bl"><b>С HSK 4 до HSK 5</b>'
         'то, что добавляется, когда программа просит на уровень выше</div>'
       + '<div class="bar b" style="width:' + str(w_up) + 'px">'
       + str(STEP_UP) + ' слов</div>'
       + '<div class="note"><b>' + str(SHARE) + '&nbsp;%</b><br>от первой полосы</div>'
         '</div>'
       + '</div>'
       + '<div class="foot"><span class="lb">Дальше</span>'
       + '<span class="vl">от пятого уровня до шестого — ещё <b>' + str(FREE_STEP)
       + '</b> слов</span>'
       + '<span class="lb">Расчёт</span>'
       + '<span class="vl">вычитанием по словнику, это не опубликованная величина</span>'
         '</div>'
       + "</div></body></html>")

open(S + "pst-hero.html", "w", encoding="utf-8").write(hero)
open(S + "pst-info.html", "w", encoding="utf-8").write(fig)
print("готово: pst-hero.html, pst-info.html")
