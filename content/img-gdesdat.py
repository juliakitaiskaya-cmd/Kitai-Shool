# -*- coding: utf-8 -*-
# Картинки к статье «Где сдать HSK»
# Обложка     — три карточки: что из этого экзамен, а что нет
# Инфографика — развилка от одного вопроса: нужен сертификат или нет
import sys
sys.path.insert(0, "/home/user/Kitai-Shool/content")
from gde_sdat import (WAYS, NO_CENTER, IMPOSSIBLE, CONF, DESC, REAL, NOT_REAL,
                      CONFIRMED, UNCONFIRMED)

S = ("/tmp/claude-0/-home-user-Kitai-Shool/a463bfca-82a9-56fd-ae09-42a7257ff999/"
     "scratchpad/")

FONTS = ("<link href=\"https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,600;0,700;1,600"
         "&family=Inter:wght@400;500;600;700&display=swap\" rel=\"stylesheet\">")
VARS = (":root{--brick:#A41E3A;--brick-d:#841630;--brick-soft:#F7E6EB;--ink:#2C2420;--ink-2:#5A4F45;"
        "--taupe:#8B7D6B;--cream:#FAF7F2;--cream-2:#F3EDE3;--hair:#EAE3D8;--surface:#fff;"
        "--grey-soft:#EFEDE8;--grey:#9A9289}")

assert len(REAL) == 2 and len(NOT_REAL) == 1

# ─────────── обложка: три карточки ───────────
cards = ""
for name, where, what, st in WAYS:
    real = "настоящий экзамен" in what
    cards += ("""<div class="cd%(cls)s">
  <div class="badge">%(badge)s</div>
  <div class="nm">%(name)s</div>
  <div class="wh">%(where)s</div>
  <div class="wt">%(what)s</div>
  <div class="src">%(src)s</div>
</div>""" % dict(cls="" if real else " no", name=name, where=where.capitalize(), what=what,
                 badge="экзамен" if real else "не экзамен",
                 src="подтверждено" if st == CONF else "по описаниям"))
assert cards.count('class="cd"') == 2 and cards.count('class="cd no"') == 1

bans = "".join('<i>%s</i>' % a[0].upper() + a[1:] for a, b in IMPOSSIBLE)
bans = "".join('<i>%s</i>' % (a[0].upper() + a[1:]) for a, b in IMPOSSIBLE)
assert bans.count("<i>") == len(IMPOSSIBLE) == 3

hero = """<!DOCTYPE html><html lang="ru"><head><meta charset="utf-8">
%(fonts)s
<style>
%(vars)s
*{margin:0;box-sizing:border-box}html,body{width:1200px;height:630px}
.card{width:1200px;height:630px;background:radial-gradient(1040px 700px at 8%% 4%%, #fff 0%%, var(--cream) 54%%, var(--cream-2) 100%%);position:relative;overflow:hidden;font-family:'Inter',sans-serif;padding:28px 56px 50px 72px;display:flex;flex-direction:column}
.card:before{content:"";position:absolute;left:0;top:0;bottom:0;width:12px;background:var(--brick)}
.head{display:flex;justify-content:space-between;align-items:flex-end;gap:34px;margin-bottom:20px}
.eyebrow{color:var(--brick);font-weight:700;font-size:18px;letter-spacing:.19em;text-transform:uppercase;margin-bottom:8px}
h1{font-family:'Cormorant Garamond',serif;font-weight:600;font-size:38px;line-height:1.08;color:var(--ink);letter-spacing:-.3px;max-width:27ch}
h1 i{font-style:italic;color:var(--brick)}
.tip{flex:0 0 318px;background:var(--surface);border:1px solid var(--hair);border-left:4px solid var(--brick);border-radius:13px;padding:12px 18px;font-size:14.5px;color:var(--ink-2);line-height:1.38}
.tip b{color:var(--ink)}

.cards{flex:0 0 auto;display:flex;align-items:stretch;gap:18px}
.cd{flex:1 1 0;background:var(--surface);border:1px solid var(--brick);border-radius:15px;padding:18px 22px 16px;display:flex;flex-direction:column}
.cd.no{border-color:var(--hair);border-style:dashed;background:transparent}
.badge{align-self:flex-start;font-size:11.5px;font-weight:700;letter-spacing:.11em;text-transform:uppercase;color:#fff;background:var(--brick);border-radius:7px;padding:5px 12px;margin-bottom:14px}
.cd.no .badge{background:var(--grey-soft);color:var(--taupe)}
.nm{font-size:20px;font-weight:600;color:var(--ink);line-height:1.2;margin-bottom:8px}
.cd.no .nm{color:var(--taupe)}
.wh{font-size:14px;color:var(--brick-d);margin-bottom:12px}
.cd.no .wh{color:var(--taupe)}
.wt{font-size:15px;color:var(--ink-2);line-height:1.4}
.src{margin-top:16px;padding-top:0;font-size:12px;font-weight:700;letter-spacing:.07em;text-transform:uppercase;color:var(--taupe)}
.cd .src{color:var(--brick)}
.cd.no .src{color:var(--grey)}

.bans{margin-top:auto;display:flex;align-items:center;gap:12px;flex-wrap:nowrap}
.bans b{font-size:12.5px;font-weight:700;letter-spacing:.11em;text-transform:uppercase;color:var(--brick);flex:0 0 auto}
.bans i{flex:1 1 0;font-style:normal;background:var(--surface);border:1px dashed var(--grey);border-radius:11px;padding:9px 14px;font-size:13.5px;color:var(--ink-2);line-height:1.3}
.foot{margin-top:12px;display:flex;align-items:center;gap:18px;background:var(--surface);border:1px solid var(--hair);border-radius:13px;padding:11px 22px}
.foot b{font-size:12.5px;font-weight:700;letter-spacing:.11em;text-transform:uppercase;color:var(--brick);flex:0 0 auto}
.foot span{font-size:15px;color:var(--ink);line-height:1.36}

.brand{position:absolute;left:72px;bottom:16px;display:flex;align-items:center;gap:11px;color:var(--ink)}
.brand b{font-family:'Cormorant Garamond',serif;font-weight:700;font-size:24px}
.brand .bdot{width:10px;height:10px;border-radius:50%%;background:var(--brick)}
.brand span{color:var(--taupe);font-size:15px}
</style></head><body>
<div class="card">
  <div class="head">
    <div>
      <div class="eyebrow">Где сдать</div>
      <h1>Словом «онлайн» называют <i>три разные вещи</i></h1>
    </div>
    <div class="tip">Экзаменом из них являются два. <b>Третье — тренажёр: он показывает баллы, но сертификата не даёт.</b></div>
  </div>

  <div class="cards">%(cards)s</div>

  <div class="bans"><b>нельзя</b>%(bans)s</div>

  <div class="foot"><b>главное</b><span>компьютерный формат — это тоже «в центре»: из дома его не сдают, как бы ни называлось слово «онлайн» в объявлении</span></div>

  <div class="brand"><span class="bdot"></span><b>Kitai School</b><span>&middot; kitai-school.ru</span></div>
</div>
</body></html>""" % dict(fonts=FONTS, vars=VARS, cards=cards, bans=bans)

assert "%%" not in hero, "в разметке остались двойные проценты"
open(S + "gdesdat-hero.html", "w", encoding="utf-8").write(hero)

# ─────────── инфографика: развилка ───────────
yes_items = "".join(
    '<div class="it%s"><b>%s</b><span>%s</span><i>%s</i></div>'
    % ("" if st == CONF else " soft", name, where, "подтверждено" if st == CONF else "по описаниям")
    for name, where, what, st in REAL)
assert yes_items.count('class="it"') == 1 and yes_items.count('class="it soft"') == 1

no_item = ('<div class="it dim"><b>%s</b><span>%s</span><i>не экзамен</i></div>'
           % (NOT_REAL[0][0], NOT_REAL[0][1].capitalize()))

nc_items = "".join('<div class="nc"><b>%s</b><span>%s</span></div>'
                   % (a[0].upper() + a[1:], b) for a, b in NO_CENTER)
assert nc_items.count('class="nc"') == len(NO_CENTER) == 3

info = """<!DOCTYPE html><html lang="ru"><head><meta charset="utf-8">
%(fonts)s
<style>
%(vars)s
*{margin:0;box-sizing:border-box}html,body{width:1200px;height:%(h)dpx}
.wrap{width:1200px;height:%(h)dpx;background:linear-gradient(180deg,#fff 0%%,var(--cream) 46%%,var(--cream-2) 100%%);font-family:'Inter',sans-serif;padding:30px 48px 26px;display:flex;flex-direction:column;position:relative;overflow:hidden}
.wrap:before{content:"";position:absolute;left:0;right:0;top:0;height:9px;background:var(--brick)}
.top{display:flex;align-items:flex-end;justify-content:space-between;gap:34px;margin-bottom:20px}
.eyebrow{color:var(--brick);font-weight:700;font-size:15.5px;letter-spacing:.19em;text-transform:uppercase;margin-bottom:7px}
h2{font-family:'Cormorant Garamond',serif;font-weight:600;font-size:34px;line-height:1.08;color:var(--ink);max-width:24ch}
h2 i{font-style:italic;color:var(--brick)}
.hint0{flex:0 0 346px;background:var(--surface);border:1px solid var(--hair);border-left:4px solid var(--brick);border-radius:13px;padding:11px 17px;font-size:14px;color:var(--ink-2);line-height:1.35}
.hint0 b{color:var(--ink)}

.q{align-self:center;background:var(--brick);color:#fff;border-radius:12px;padding:12px 28px;font-size:19px;font-weight:600;margin-bottom:8px}
.stem{align-self:center;width:3px;height:18px;background:var(--brick)}

.forks{flex:1 1 auto;min-height:0;display:flex;gap:20px;margin-top:4px}
.fk{flex:1 1 0;background:var(--surface);border:1px solid var(--hair);border-radius:15px;padding:16px 20px;display:flex;flex-direction:column}
.fk.yes{border-color:var(--brick)}
.fh{display:flex;align-items:center;gap:10px;margin-bottom:12px}
.fh i{font-style:normal;width:30px;height:30px;border-radius:50%%;display:flex;align-items:center;justify-content:center;font-weight:700;font-size:16px;background:var(--brick);color:#fff}
.fk.no .fh i{background:var(--grey-soft);color:var(--taupe)}
.fh b{font-size:17px;color:var(--ink)}
.it{border-radius:11px;padding:11px 15px;margin-bottom:9px;background:var(--brick-soft);border:1px solid var(--brick)}
.it.soft{background:transparent;border-style:dashed;border-color:var(--grey)}
.it.dim{background:var(--grey-soft);border:1px solid var(--hair)}
.it b{display:block;font-size:16px;color:var(--ink);margin-bottom:3px}
.it.dim b{color:var(--taupe)}
.it span{font-size:13.5px;color:var(--ink-2)}
.it i{display:block;margin-top:6px;font-style:normal;font-size:11.5px;font-weight:700;letter-spacing:.07em;text-transform:uppercase;color:var(--brick)}
.it.soft i,.it.dim i{color:var(--grey)}
.fn{margin-top:auto;padding-top:10px;font-size:13px;color:var(--ink-2);line-height:1.35}

.ncs{margin-top:16px;flex:0 0 auto;display:flex;gap:11px}
.nc{flex:1 1 0;background:var(--surface);border:1px solid var(--hair);border-left:4px solid var(--brick);border-radius:12px;padding:10px 15px}
.nc b{display:block;font-size:14.5px;color:var(--ink);margin-bottom:2px}
.nc span{font-size:13px;color:var(--ink-2);line-height:1.3}

.foot{margin-top:14px;flex:0 0 auto;display:flex;align-items:center;gap:18px}
.foot .msg{flex:1 1 auto;background:var(--surface);border:1px solid var(--hair);border-radius:14px;padding:11px 20px;font-size:14.5px;color:var(--ink);line-height:1.34}
.foot .msg b{color:var(--brick)}
.brand{display:flex;align-items:center;gap:10px;color:var(--ink);flex:0 0 auto}
.brand b{font-family:'Cormorant Garamond',serif;font-weight:700;font-size:23px}
.brand .dot2{width:9px;height:9px;border-radius:50%%;background:var(--brick)}
.brand span{color:var(--taupe);font-size:15px}
</style></head><body>
<div class="wrap">
  <div class="top">
    <div>
      <div class="eyebrow">Развилка</div>
      <h2>Всё решает один вопрос: <i>нужен ли сертификат</i></h2>
    </div>
    <div class="hint0">Пунктиром отмечен домашний формат: он есть не везде и не на всех уровнях. <b>По России подтверждения я не нашла.</b></div>
  </div>

  <div class="q">Нужен официальный сертификат?</div>
  <div class="stem"></div>

  <div class="forks">
    <div class="fk yes">
      <div class="fh"><i>&#10003;</i><b>Да — только эти два пути</b></div>
      %(yes)s
      <div class="fn">Оба проводит центр тестирования: он проверяет документы и отвечает за результат</div>
    </div>
    <div class="fk no">
      <div class="fh"><i>&mdash;</i><b>Нет — хватит тренажёра</b></div>
      %(no)s
      <div class="fn">Подходит, чтобы измерить свой уровень перед записью или прикинуть, к чему готовиться</div>
    </div>
  </div>

  <div class="ncs">%(nc)s</div>

  <div class="foot">
    <div class="msg">Если центра в городе нет, <b>дата известна за месяцы</b> — поездку можно спланировать заранее</div>
    <div class="brand"><span class="dot2"></span><b>Kitai School</b><span>&middot; kitai-school.ru</span></div>
  </div>
</div>
</body></html>""" % dict(fonts=FONTS, vars=VARS, h=700, yes=yes_items, no=no_item, nc=nc_items)

assert "%%" not in info, "в разметке остались двойные проценты"
open(S + "gdesdat-info.html", "w", encoding="utf-8").write(info)

print("ok | экзамен:", [w[0] for w in REAL], "| не экзамен:", NOT_REAL[0][0],
      "| с оговоркой:", UNCONFIRMED[0][0])
