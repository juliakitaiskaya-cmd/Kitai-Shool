# -*- coding: utf-8 -*-
# Картинки к статье «Предлоги в китайском»
# Обложка     — кадр видоискателя: обстоятельство слева, действие справа
# Инфографика — схема позиции и четыре знака в двух ролях
S = ("/tmp/claude-0/-home-user-Kitai-Shool/a463bfca-82a9-56fd-ae09-42a7257ff999/"
     "scratchpad/")

FONTS = ("<link href=\"https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,600;0,700;1,600"
         "&family=Inter:wght@400;500;600;700&family=Noto+Serif+SC:wght@600;700&display=swap\" rel=\"stylesheet\">")
VARS = (":root{--brick:#A41E3A;--brick-d:#841630;--brick-soft:#F7E6EB;--ink:#2C2420;--ink-2:#5A4F45;"
        "--taupe:#8B7D6B;--cream:#FAF7F2;--cream-2:#F3EDE3;--hair:#EAE3D8;--surface:#fff;"
        "--sky:#39597F;--sky-soft:#E7EDF4;--good:#1E7A46;--good-soft:#E8F3EC}")

hero = """<!DOCTYPE html><html lang="ru"><head><meta charset="utf-8">
%(fonts)s
<style>
%(vars)s
*{margin:0;box-sizing:border-box}html,body{width:1200px;height:630px}
.card{width:1200px;height:630px;background:radial-gradient(1050px 660px at 14%% 10%%, #fff 0%%, var(--cream) 52%%, var(--cream-2) 100%%);position:relative;overflow:hidden;font-family:'Inter',sans-serif;padding:78px 56px 0 72px;display:flex;justify-content:space-between}
.card:before{content:"";position:absolute;left:0;top:0;bottom:0;width:12px;background:var(--brick)}
.txt{flex:0 0 452px;padding-top:4px}
.eyebrow{color:var(--brick);font-weight:700;font-size:18px;letter-spacing:.19em;text-transform:uppercase;margin-bottom:13px}
h1{font-family:'Cormorant Garamond',serif;font-weight:600;font-size:45px;line-height:1.07;color:var(--ink);letter-spacing:-.4px}
h1 i{font-style:italic;color:var(--brick)}
.sub{font-size:18px;color:var(--ink-2);line-height:1.42;max-width:29ch;margin-top:16px}
.tip{display:inline-block;margin-top:22px;background:var(--surface);border:1px solid var(--hair);border-left:4px solid var(--brick);border-radius:13px;padding:13px 19px;font-size:15.5px;color:var(--ink-2);line-height:1.36;max-width:33ch}
.tip b{color:var(--ink)}

.scene{flex:0 0 540px;padding-top:22px;display:flex;flex-direction:column;align-items:center}
.view{position:relative;width:500px;padding:34px 30px 30px;background:var(--surface);border-radius:18px;box-shadow:0 14px 30px rgba(44,36,32,.13)}
.view .c{position:absolute;width:34px;height:34px;border:4px solid var(--brick)}
.view .tl{left:14px;top:14px;border-right:none;border-bottom:none;border-radius:8px 0 0 0}
.view .tr{right:14px;top:14px;border-left:none;border-bottom:none;border-radius:0 8px 0 0}
.view .bl{left:14px;bottom:14px;border-right:none;border-top:none;border-radius:0 0 0 8px}
.view .br{right:14px;bottom:14px;border-left:none;border-top:none;border-radius:0 0 8px 0}
.line{display:flex;align-items:flex-end;justify-content:center;gap:3px;font-family:'Noto Serif SC',serif;font-size:38px;color:var(--ink-2);line-height:1.15}
.line b{color:var(--brick);font-weight:700}
.marks{display:flex;justify-content:center;gap:3px;margin-top:9px}
.marks span{font-size:13px;letter-spacing:.02em;text-align:center}
.marks .a{color:var(--brick);font-weight:700}
.marks .b{color:var(--taupe)}
.pin{margin-top:15px;text-align:center;font-size:15.5px;color:var(--ink-2);font-style:italic}
.tr2{margin-top:3px;text-align:center;font-size:16px;color:var(--ink)}
.cap{margin-top:24px;text-align:center;font-size:16.5px;color:var(--ink-2);line-height:1.42;max-width:42ch}
.cap b{color:var(--ink)}
.note{margin-top:18px;background:var(--surface);border:1px solid var(--hair);border-radius:13px;padding:12px 20px;font-size:15px;color:var(--ink-2);line-height:1.4;text-align:center;max-width:470px}
.note b{color:var(--brick)}
.brand{position:absolute;left:72px;bottom:28px;display:flex;align-items:center;gap:11px;color:var(--ink)}
.brand b{font-family:'Cormorant Garamond',serif;font-weight:700;font-size:26px}
.brand .bdot{width:10px;height:10px;border-radius:50%%;background:var(--brick)}
.brand span{color:var(--taupe);font-size:16px}
</style></head><body>
<div class="card">
  <div class="txt">
    <div class="eyebrow">Грамматика</div>
    <h1>Предлоги <i>в китайском</i></h1>
    <div class="sub">Кому, где, чем и откуда — всё это называется до глагола, а не после</div>
    <div class="tip"><b>Многие предлоги — бывшие глаголы,</b> и след прежнего значения в них виден до сих пор</div>
  </div>
  <div class="scene">
    <div class="view">
      <span class="c tl"></span><span class="c tr"></span>
      <span class="c bl"></span><span class="c br"></span>
      <div class="line">我<b>给妈妈</b>打电话</div>
      <div class="marks">
        <span class="b" style="width:38px">кто</span>
        <span class="a" style="width:114px">кому</span>
        <span class="b" style="width:114px">что делает</span>
      </div>
      <div class="pin">wǒ gěi māma dǎ diànhuà</div>
      <div class="tr2">я звоню маме</div>
    </div>
    <div class="cap">Адресат стоит <b>перед глаголом</b> — переставить его назад нельзя</div>
    <div class="note">А само 给 умеет быть и глаголом: <b>给我一本书</b> — «дай мне книгу»</div>
  </div>
  <div class="brand"><span class="bdot"></span><b>Kitai School</b><span>&middot; kitai-school.ru</span></div>
</div>
</body></html>""" % dict(fonts=FONTS, vars=VARS)

open(S + "prd-hero.html", "w", encoding="utf-8").write(hero)

# --------------------------------------------------------------- инфографика
SLOT = [
    ("кто", "我", "sub"),
    ("предлог + слово", "给妈妈", "key"),
    ("глагол", "打", "verb"),
    ("дополнение", "电话", "obj"),
]

assert sum(1 for s in SLOT if s[2] == "key") == 1, "предложная группа отмечена не один раз"
assert [s[1] for s in SLOT] == ["我", "给妈妈", "打", "电话"], "порядок частей сбит"

slots = "".join(
    '<div class="sl %s"><div class="lb">%s</div><div class="vv">%s</div></div>'
    % (cls, lab, han) for lab, han, cls in SLOT)

PAIR = [
    ("在", "zài", "находиться", "他在家", "он дома", "в, на", "他在家吃饭", "он ест дома"),
    ("给", "gěi", "дать", "给我一本书", "дай мне книгу", "кому", "给我打电话",
     "позвони мне"),
    ("到", "dào", "прибыть", "我到了", "я на месте", "до", "从一点到三点", "с часа до трёх"),
    ("跟", "gēn", "следовать", "跟我来", "идите за мной", "с", "跟他说", "сказать ему"),
]

assert len(PAIR) == 4, "пар не четыре"
for p in PAIR:
    assert len(p) == 8, "в паре не восемь полей: %s" % p[0]

pairs = "".join(
    '<div class="pc"><div class="ph">%s <small>%s</small></div>'
    '<div class="role v"><span class="rl">глагол</span><b>%s</b>'
    '<div class="ex"><span class="han">%s</span> — %s</div></div>'
    '<div class="role p"><span class="rl">предлог</span><b>%s</b>'
    '<div class="ex"><span class="han">%s</span> — %s</div></div></div>'
    % (han, py, vmean, vex, vtr, pmean, pex, ptr)
    for han, py, vmean, vex, vtr, pmean, pex, ptr in PAIR)

info = """<!DOCTYPE html><html lang="ru"><head><meta charset="utf-8">
%(fonts)s
<style>
%(vars)s
*{margin:0;box-sizing:border-box}html,body{width:1200px;height:600px}
.wrap{width:1200px;height:600px;background:linear-gradient(180deg,#fff 0%%,var(--cream) 46%%,var(--cream-2) 100%%);font-family:'Inter',sans-serif;padding:30px 46px 26px;display:flex;flex-direction:column}
.top{display:flex;align-items:flex-end;justify-content:space-between;gap:30px;margin-bottom:18px}
.eyebrow{color:var(--brick);font-weight:700;font-size:14.5px;letter-spacing:.17em;text-transform:uppercase;margin-bottom:7px}
h2{font-family:'Cormorant Garamond',serif;font-weight:600;font-size:38px;line-height:1.07;color:var(--ink);letter-spacing:-.3px}
h2 i{font-style:italic;color:var(--brick)}
.hint{flex:0 0 392px;background:var(--surface);border:1px solid var(--hair);border-left:4px solid var(--brick);border-radius:12px;padding:12px 17px;font-size:14.5px;color:var(--ink-2);line-height:1.36}
.hint b{color:var(--ink)}

.line{display:flex;gap:11px;align-items:stretch;flex:0 0 auto}
.sl{flex:1 1 0;background:var(--surface);border:2px solid var(--hair);border-radius:14px;padding:11px 10px 12px;text-align:center;box-shadow:0 4px 11px rgba(44,36,32,.05)}
.sl .lb{font-size:12.5px;color:var(--taupe);letter-spacing:.03em}
.sl .vv{font-family:'Noto Serif SC',serif;font-size:29px;color:var(--ink);line-height:1.2;margin-top:3px}
.sl.key{border-color:var(--brick);background:var(--brick-soft)}
.sl.key .lb{color:var(--brick-d);font-weight:700}
.sl.key .vv{color:var(--brick)}
.whole{text-align:center;margin-top:11px;font-size:15.5px;color:var(--ink-2)}
.whole b{font-family:'Noto Serif SC',serif;font-size:20px;color:var(--ink);vertical-align:-1px}

.sep{display:flex;align-items:center;gap:16px;margin:17px 0 12px}
.sep span{font-size:15px;font-weight:700;color:var(--brick-d);white-space:nowrap}
.sep i{flex:1 1 auto;height:1px;background:var(--hair)}
.pairs{display:flex;gap:13px}
.pc{flex:1 1 0;background:var(--surface);border:1px solid var(--hair);border-radius:14px;padding:12px 15px 13px}
.ph{font-family:'Noto Serif SC',serif;font-size:30px;color:var(--brick);line-height:1.1;text-align:center;margin-bottom:9px}
.ph small{font-family:'Inter',sans-serif;font-size:12.5px;color:var(--ink-2);font-style:italic}
.role{border-radius:10px;padding:8px 11px 9px}
.role.v{background:var(--sky-soft)}
.role.p{background:var(--good-soft);margin-top:7px}
.rl{display:block;font-size:11px;font-weight:700;letter-spacing:.08em;text-transform:uppercase}
.role.v .rl{color:var(--sky)}
.role.p .rl{color:var(--good)}
.role b{font-size:14px;color:var(--ink)}
.ex{font-size:13px;color:var(--ink-2);margin-top:3px;line-height:1.3}
.ex .han{font-family:'Noto Serif SC',serif;font-size:16px;color:var(--ink)}

.foot{margin-top:auto;display:flex;align-items:center;gap:18px;padding-top:14px}
.foot .msg{flex:1 1 auto;background:var(--brick-soft);border:1px solid var(--brick);border-radius:14px;padding:11px 21px;font-size:15px;color:var(--ink);line-height:1.34}
.foot .msg b{color:var(--brick)}
.brand{display:flex;align-items:center;gap:10px;color:var(--ink);flex:0 0 auto}
.brand b{font-family:'Cormorant Garamond',serif;font-weight:700;font-size:23px}
.brand .dot2{width:9px;height:9px;border-radius:50%%;background:var(--brick)}
.brand span{color:var(--taupe);font-size:15px}
</style></head><body>
<div class="wrap">
  <div class="top">
    <div>
      <div class="eyebrow">介词</div>
      <h2>Один знак — <i>две работы</i></h2>
    </div>
    <div class="hint">Предложная группа стоит между подлежащим и глаголом. <b>Справа от глагола ей места нет.</b></div>
  </div>

  <div class="line">%(slots)s</div>
  <div class="whole">целиком — <b>我给妈妈打电话</b>, «я звоню маме»</div>

  <div class="sep"><span>Те же знаки в роли глагола и в роли предлога</span><i></i></div>
  <div class="pairs">%(pairs)s</div>

  <div class="foot">
    <div class="msg">Отличить просто: <b>если в предложении есть другой глагол — перед вами предлог</b></div>
    <div class="brand"><span class="dot2"></span><b>Kitai School</b><span>&middot; kitai-school.ru</span></div>
  </div>
</div>
</body></html>""" % dict(fonts=FONTS, vars=VARS, slots=slots, pairs=pairs)

open(S + "prd-info.html", "w", encoding="utf-8").write(info)
print("ok | блоков:", len(SLOT), "| пар:", len(PAIR))
