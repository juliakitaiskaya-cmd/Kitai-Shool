# -*- coding: utf-8 -*-
# Картинки к статье «Порядок определений в китайском»
# Обложка    — длинная именная группа со скобкой: всё до последнего знака — определения
# Инфографика — нарастающая строка: фраза растёт влево, справа отметка про 的
S = ("/tmp/claude-0/-home-user-Kitai-Shool/a463bfca-82a9-56fd-ae09-42a7257ff999/"
     "scratchpad/")

FONTS = ("<link href=\"https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,600;0,700;1,600"
         "&family=Inter:wght@400;500;600;700&family=Noto+Serif+SC:wght@600;700&display=swap\" rel=\"stylesheet\">")
VARS = (":root{--brick:#A41E3A;--brick-d:#841630;--brick-soft:#F7E6EB;--ink:#2C2420;--ink-2:#5A4F45;"
        "--taupe:#8B7D6B;--cream:#FAF7F2;--cream-2:#F3EDE3;--hair:#EAE3D8;--surface:#fff;"
        "--good:#1E7A46;--good-soft:#E8F3EC}")

HERO_HAN = [
    ("我的", "wǒ de", "mod"),
    ("那", "nà", "mod"),
    ("三本", "sān běn", "mod"),
    ("很有意思的", "hěn yǒu yìsi de", "mod"),
    ("中文", "Zhōngwén", "mod"),
    ("书", "shū", "head"),
]

assert sum(1 for h in HERO_HAN if h[2] == "head") == 1, "главное слово должно быть одно"
assert HERO_HAN[-1][2] == "head", "главное слово стоит не последним"

mods = "".join('<span class="ch">%s</span>' % han
               for han, py, cls in HERO_HAN if cls == "mod")
head = [h for h in HERO_HAN if h[2] == "head"][0][0]

hero = """<!DOCTYPE html><html lang="ru"><head><meta charset="utf-8">
%(fonts)s
<style>
%(vars)s
*{margin:0;box-sizing:border-box}html,body{width:1200px;height:630px}
.card{width:1200px;height:630px;background:radial-gradient(1050px 660px at 14%% 10%%, #fff 0%%, var(--cream) 52%%, var(--cream-2) 100%%);position:relative;overflow:hidden;font-family:'Inter',sans-serif;padding:78px 56px 0 72px;display:flex;justify-content:space-between}
.card:before{content:"";position:absolute;left:0;top:0;bottom:0;width:12px;background:var(--brick)}
.txt{flex:0 0 440px;padding-top:4px}
.eyebrow{color:var(--brick);font-weight:700;font-size:18px;letter-spacing:.19em;text-transform:uppercase;margin-bottom:13px}
h1{font-family:'Cormorant Garamond',serif;font-weight:600;font-size:45px;line-height:1.07;color:var(--ink);letter-spacing:-.4px}
h1 i{font-style:italic;color:var(--brick)}
.sub{font-size:18px;color:var(--ink-2);line-height:1.42;max-width:28ch;margin-top:16px}
.tip{display:inline-block;margin-top:22px;background:var(--surface);border:1px solid var(--hair);border-left:4px solid var(--brick);border-radius:13px;padding:13px 19px;font-size:15.5px;color:var(--ink-2);line-height:1.36;max-width:32ch}
.tip b{color:var(--ink)}

.scene{flex:0 0 560px;padding-top:34px;display:flex;flex-direction:column;align-items:center}
.plate{background:var(--surface);border:1px solid var(--hair);border-radius:18px;padding:30px 26px 26px;box-shadow:0 14px 30px rgba(44,36,32,.13);text-align:center}
.row{display:flex;align-items:flex-end;gap:10px;justify-content:center}
.grp{display:flex;flex-direction:column;align-items:center}
.ln{display:flex;white-space:nowrap}
.ch{font-family:'Noto Serif SC',serif;font-size:31px;color:var(--ink-2);line-height:1.15}
.hd{font-family:'Noto Serif SC',serif;font-size:39px;color:var(--brick);line-height:1.15}
.brk{height:13px;border:2px solid var(--taupe);border-top:none;border-radius:0 0 8px 8px;align-self:stretch;margin-top:8px}
.brk.one{border-color:var(--brick)}
.lb{margin-top:6px;font-size:14.5px;color:var(--taupe)}
.lb.one{color:var(--brick);font-weight:700}
.pin{margin-top:18px;font-size:15.5px;color:var(--ink-2);font-style:italic}
.tr{margin-top:3px;font-size:16px;color:var(--ink)}
.cap{margin-top:24px;text-align:center;font-size:16.5px;color:var(--ink-2);line-height:1.4;max-width:40ch}
.note{margin-top:22px;background:var(--surface);border:1px solid var(--hair);border-radius:13px;padding:12px 20px;font-size:15px;color:var(--ink-2);line-height:1.4;text-align:center;max-width:430px}
.note b{font-family:'Noto Serif SC',serif;font-size:19px;color:var(--ink);vertical-align:-1px}
.cap b{color:var(--ink)}
.brand{position:absolute;left:72px;bottom:28px;display:flex;align-items:center;gap:11px;color:var(--ink)}
.brand b{font-family:'Cormorant Garamond',serif;font-weight:700;font-size:26px}
.brand .bdot{width:10px;height:10px;border-radius:50%%;background:var(--brick)}
.brand span{color:var(--taupe);font-size:16px}
</style></head><body>
<div class="card">
  <div class="txt">
    <div class="eyebrow">Грамматика</div>
    <h1>Порядок определений <i>в китайском</i></h1>
    <div class="sub">Главное слово всегда последнее, а всё описание выстраивается слева от него</div>
    <div class="tip"><b>Порядок не свободный.</b> Чьё, какое, сколько, какого качества — у каждой подробности своё место</div>
  </div>
  <div class="scene">
    <div class="plate">
      <div class="row">
        <div class="grp"><div class="ln">%(mods)s</div><div class="brk"></div><div class="lb">пять определений</div></div>
        <div class="grp"><div class="ln"><span class="hd">%(head)s</span></div><div class="brk one"></div><div class="lb one">слово</div></div>
      </div>
      <div class="pin">wǒ de nà sān běn hěn yǒu yìsi de Zhōngwén shū</div>
      <div class="tr">те мои три очень интересные книги по китайскому</div>
    </div>
    <div class="cap">Читается справа налево: <b>сначала найдите последний знак</b> — это и есть то, о чём речь</div>
    <div class="note">А <b>书很有意思</b> — уже не словосочетание, а целое предложение: «книга интересная»</div>
  </div>
  <div class="brand"><span class="bdot"></span><b>Kitai School</b><span>&middot; kitai-school.ru</span></div>
</div>
</body></html>""" % dict(fonts=FONTS, vars=VARS, mods=mods, head=head)

open(S + "opr-hero.html", "w", encoding="utf-8").write(hero)

# --------------------------------------------------------------- инфографика
# (добавленный блок, вся фраза, перевод, нужна ли 的)
GROW = [
    ("书", "书", "книга", "—", "none"),
    ("中文", "中文书", "книга по китайскому", "без 的", "no"),
    ("很有意思的", "很有意思的中文书", "очень интересная книга по китайскому", "с 的", "yes"),
    ("三本", "三本很有意思的中文书", "три очень интересные книги по китайскому", "без 的", "no"),
    ("那", "那三本很有意思的中文书", "те три очень интересные книги по китайскому", "без 的", "no"),
    ("我的", "我的那三本很有意思的中文书", "те мои три очень интересные книги по китайскому",
     "с 的", "yes"),
]

assert len(GROW) == 6, "строк роста не шесть"
for i in range(1, len(GROW)):
    assert GROW[i][1].endswith(GROW[i - 1][1]), "строка %d не продолжает предыдущую" % i
    assert GROW[i][1] == GROW[i][0] + GROW[i - 1][1], "добавленный блок не совпадает со строкой"


def grow_row(i, g):
    add, whole, ru, de, cls = g
    pre = '<span class="add">%s</span>' % add if i else ""
    rest = whole[len(add):] if i else whole
    tail = '<span class="rest">%s</span>' % rest if rest else ""
    chip = {"none": '<span class="de none">—</span>',
            "no": '<span class="de no">%s</span>' % de,
            "yes": '<span class="de yes">%s</span>' % de}[cls]
    return ('<div class="gr"><div class="num">%d</div>'
            '<div class="phr">%s%s</div><div class="ru">%s</div>%s</div>'
            % (i + 1, pre, tail, ru, chip))


grow = "".join(grow_row(i, g) for i, g in enumerate(GROW))

SLOTS = ["чьё", "какое", "сколько", "какого качества", "что за", "СЛОВО"]
slot_line = "".join(
    '<span class="sl %s">%s</span>' % ("hd" if s == "СЛОВО" else "", s) for s in SLOTS)

info = """<!DOCTYPE html><html lang="ru"><head><meta charset="utf-8">
%(fonts)s
<style>
%(vars)s
*{margin:0;box-sizing:border-box}html,body{width:1200px;height:700px}
.wrap{width:1200px;height:700px;background:linear-gradient(180deg,#fff 0%%,var(--cream) 46%%,var(--cream-2) 100%%);font-family:'Inter',sans-serif;padding:30px 46px 26px;display:flex;flex-direction:column}
.top{display:flex;align-items:flex-end;justify-content:space-between;gap:30px;margin-bottom:16px}
.eyebrow{color:var(--brick);font-weight:700;font-size:14.5px;letter-spacing:.17em;text-transform:uppercase;margin-bottom:7px}
h2{font-family:'Cormorant Garamond',serif;font-weight:600;font-size:39px;line-height:1.07;color:var(--ink);letter-spacing:-.3px}
h2 i{font-style:italic;color:var(--brick)}
.hint{flex:0 0 372px;background:var(--surface);border:1px solid var(--hair);border-left:4px solid var(--brick);border-radius:12px;padding:12px 17px;font-size:14.5px;color:var(--ink-2);line-height:1.36}
.hint b{color:var(--ink)}

.gr{display:flex;align-items:center;gap:14px;background:var(--surface);border:1px solid var(--hair);border-radius:13px;padding:9px 16px;margin-bottom:8px;box-shadow:0 3px 9px rgba(44,36,32,.04)}
.num{flex:0 0 26px;height:26px;border-radius:50%%;background:var(--cream-2);color:var(--taupe);font-size:13.5px;font-weight:700;display:flex;align-items:center;justify-content:center}
.phr{flex:0 0 400px;font-family:'Noto Serif SC',serif;font-size:27px;line-height:1.25;white-space:nowrap}
.phr .add{color:var(--brick)}
.phr .rest{color:var(--ink-2)}
.ru{flex:1 1 auto;font-size:15px;color:var(--ink-2);line-height:1.3}
.de{flex:0 0 108px;text-align:center;font-size:14px;font-weight:700;border-radius:999px;padding:5px 0}
.de.none{background:var(--cream-2);color:var(--taupe)}
.de.no{background:var(--good-soft);color:var(--good)}
.de.yes{background:var(--brick-soft);color:var(--brick-d)}

.sep{display:flex;align-items:center;gap:16px;margin:14px 0 11px}
.sep span{font-size:15px;font-weight:700;color:var(--brick-d);white-space:nowrap}
.sep i{flex:1 1 auto;height:1px;background:var(--hair)}
.line{display:flex;align-items:center;gap:9px}
.sl{flex:1 1 0;text-align:center;background:var(--surface);border:1px solid var(--hair);border-radius:11px;padding:11px 4px;font-size:15px;color:var(--ink-2)}
.sl.hd{background:var(--brick);border-color:var(--brick);color:#fff;font-weight:700;letter-spacing:.06em}

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
      <div class="eyebrow">Именная группа</div>
      <h2>Фраза растёт <i>влево</i></h2>
    </div>
    <div class="hint">Каждый шаг добавляет одно определение — и всегда слева. <b>Существительное остаётся на последнем месте.</b></div>
  </div>

  %(grow)s

  <div class="sep"><span>Порядок слотов, который не меняется</span><i></i></div>
  <div class="line">%(slots)s</div>

  <div class="foot">
    <div class="msg">Так длинно не говорят — <b>но собрать фразу можно только в этом порядке</b></div>
    <div class="brand"><span class="dot2"></span><b>Kitai School</b><span>&middot; kitai-school.ru</span></div>
  </div>
</div>
</body></html>""" % dict(fonts=FONTS, vars=VARS, grow=grow, slots=slot_line)

open(S + "opr-info.html", "w", encoding="utf-8").write(info)
print("ok | строк роста:", len(GROW), "| слотов:", len(SLOTS))
