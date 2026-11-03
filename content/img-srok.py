# -*- coding: utf-8 -*-
# Картинки к статье «Сколько действует сертификат HSK»
# Обложка     — два бланка рядом: на одном стоит срок, на другом нет
# Инфографика — полоса в двадцать четыре месяца с окном подачи и подвижной меткой
S = ("/tmp/claude-0/-home-user-Kitai-Shool/a463bfca-82a9-56fd-ae09-42a7257ff999/"
     "scratchpad/")

FONTS = ("<link href=\"https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,600;0,700;1,600"
         "&family=Inter:wght@400;500;600;700&family=Noto+Serif+SC:wght@600;700&display=swap\" rel=\"stylesheet\">")
VARS = (":root{--brick:#A41E3A;--brick-d:#841630;--brick-soft:#F7E6EB;--ink:#2C2420;--ink-2:#5A4F45;"
        "--taupe:#8B7D6B;--cream:#FAF7F2;--cream-2:#F3EDE3;--hair:#EAE3D8;--surface:#fff;"
        "--paper:#FDFBF6;--good:#1E7A46;--good-soft:#E8F3EC;--wait:#C9BFAE}")

# ─────────── вся геометрия шкалы считается из одного числа ───────────
MONTHS = 24          # срок действия результата
WAIT = 2             # месяцев, пока результат идёт (подаём как «несколько недель»)
DEADLINE = 19        # месяц, на который приходится дедлайн подачи в примере

assert MONTHS == 24, "срок должен быть двадцать четыре месяца"
assert 0 < WAIT < MONTHS, "ожидание результата должно лежать внутри срока"
assert WAIT < DEADLINE < MONTHS, "дедлайн должен лежать внутри окна подачи"
PCT_WAIT = WAIT * 100 // MONTHS
PCT_DL = DEADLINE * 100 // MONTHS
assert PCT_WAIT < PCT_DL < 100, "отметки на шкале встали не по порядку"

ticks = "".join(
    '<div class="tk%s" style="left:%.4f%%"><i></i>%s</div>'
    % ("" if m % 6 else " big", m * 100.0 / MONTHS,
       '<span>%d</span>' % m if m in (6, 12, 18) else "")
    for m in range(MONTHS + 1))

# ─────────── обложка ───────────
hero = """<!DOCTYPE html><html lang="ru"><head><meta charset="utf-8">
%(fonts)s
<style>
%(vars)s
*{margin:0;box-sizing:border-box}html,body{width:1200px;height:630px}
.card{width:1200px;height:630px;background:radial-gradient(1020px 680px at 12%% 8%%, #fff 0%%, var(--cream) 50%%, var(--cream-2) 100%%);position:relative;overflow:hidden;font-family:'Inter',sans-serif;padding:54px 48px 0 72px;display:flex;justify-content:space-between}
.card:before{content:"";position:absolute;left:0;top:0;bottom:0;width:12px;background:var(--brick)}
.txt{flex:0 0 478px;padding-top:10px}
.eyebrow{color:var(--brick);font-weight:700;font-size:18px;letter-spacing:.19em;text-transform:uppercase;margin-bottom:14px}
h1{font-family:'Cormorant Garamond',serif;font-weight:600;font-size:44px;line-height:1.06;color:var(--ink);letter-spacing:-.4px}
h1 i{font-style:italic;color:var(--brick)}
.sub{font-size:18px;color:var(--ink-2);line-height:1.42;max-width:31ch;margin-top:17px}
.tip{display:inline-block;margin-top:22px;background:var(--surface);border:1px solid var(--hair);border-left:4px solid var(--brick);border-radius:13px;padding:14px 20px;font-size:15.5px;color:var(--ink-2);line-height:1.38;max-width:34ch}
.tip b{color:var(--ink)}

.scene{flex:0 0 530px;display:flex;flex-direction:column;align-items:center;padding-top:6px}
.sheets{display:flex;gap:22px}
.sh{width:238px;height:390px;background:var(--paper);border:1px solid var(--hair);border-radius:11px;box-shadow:0 12px 26px rgba(44,36,32,.15);padding:20px 18px;position:relative;display:flex;flex-direction:column}
.sh .kind{font-size:12.5px;font-weight:700;letter-spacing:.12em;text-transform:uppercase;color:var(--taupe)}
.sh .ttl{font-size:17px;font-weight:700;color:var(--ink);line-height:1.22;margin-top:8px}
.sh .lines{margin-top:14px;display:flex;flex-direction:column;gap:9px}
.sh .ln{height:7px;border-radius:4px;background:#E7E0D4}
.sh .ln.s{width:62%%}
.sh .ln.m{width:84%%}
.stamp{position:absolute;left:18px;right:18px;bottom:20px;border:2px solid var(--brick);color:var(--brick-d);border-radius:9px;padding:9px 6px;text-align:center;font-size:15px;font-weight:700;line-height:1.24;transform:rotate(-3deg);background:rgba(247,230,235,.72)}
.stamp.grey{border-color:var(--good);color:var(--good);background:rgba(232,243,236,.72);transform:rotate(2deg)}
.cap{margin-top:22px;text-align:center;font-size:16.5px;color:var(--ink-2);line-height:1.42;max-width:40ch}
.cap b{color:var(--ink)}
.brand{position:absolute;left:72px;bottom:28px;display:flex;align-items:center;gap:11px;color:var(--ink)}
.brand b{font-family:'Cormorant Garamond',serif;font-weight:700;font-size:26px}
.brand .bdot{width:10px;height:10px;border-radius:50%%;background:var(--brick)}
.brand span{color:var(--taupe);font-size:16px}
</style></head><body>
<div class="card">
  <div class="txt">
    <div class="eyebrow">Экзамены</div>
    <h1>Сколько действует сертификат HSK: <i>срок годности и что он значит на практике</i></h1>
    <div class="sub">Два года — и считаются они не с того дня, с которого обычно думают.</div>
    <div class="tip"><b>Срок стоит на результате, а не на самом документе:</b> в приёмную комиссию несут первое, в резюме — второе.</div>
    <div class="brand"><span class="bdot"></span><b>Kitai School</b><span>&middot; kitai-school.ru</span></div>
  </div>

  <div class="scene">
    <div class="sheets">
      <div class="sh">
        <div class="kind">Результат</div>
        <div class="ttl">Отчёт с баллами по разделам</div>
        <div class="lines"><span class="ln m"></span><span class="ln"></span><span class="ln s"></span><span class="ln m"></span><span class="ln s"></span></div>
        <div class="stamp">действителен<br>два года</div>
      </div>
      <div class="sh">
        <div class="kind">Документ</div>
        <div class="ttl">Подтверждение факта сдачи</div>
        <div class="lines"><span class="ln m"></span><span class="ln s"></span><span class="ln"></span><span class="ln s"></span><span class="ln m"></span></div>
        <div class="stamp grey">остаётся<br>у вас</div>
      </div>
    </div>
    <div class="cap">Это один и тот же лист — <b>но в приёмной комиссии и в резюме от него нужно разное</b></div>
  </div>
</div>
</body></html>""" % dict(fonts=FONTS, vars=VARS)

open(S + "srok-hero.html", "w", encoding="utf-8").write(hero)

# ─────────── инфографика ───────────
info = """<!DOCTYPE html><html lang="ru"><head><meta charset="utf-8">
%(fonts)s
<style>
%(vars)s
*{margin:0;box-sizing:border-box}html,body{width:1200px;height:%(h)dpx}
.wrap{width:1200px;height:%(h)dpx;background:linear-gradient(180deg,#fff 0%%,var(--cream) 40%%,var(--cream-2) 100%%);font-family:'Inter',sans-serif;padding:38px 48px 30px;display:flex;flex-direction:column;position:relative;overflow:hidden}
.wrap:before{content:"";position:absolute;left:0;right:0;top:0;height:9px;background:var(--brick)}
.top{display:flex;align-items:flex-end;justify-content:space-between;gap:34px;margin-bottom:22px}
.eyebrow{color:var(--brick);font-weight:700;font-size:15.5px;letter-spacing:.19em;text-transform:uppercase;margin-bottom:8px}
h2{font-family:'Cormorant Garamond',serif;font-weight:600;font-size:38px;line-height:1.07;color:var(--ink);max-width:20ch}
h2 i{font-style:italic;color:var(--brick)}
.hint{flex:0 0 412px;background:var(--surface);border:1px solid var(--hair);border-left:4px solid var(--brick);border-radius:13px;padding:12px 18px;font-size:15px;color:var(--ink-2);line-height:1.36}
.hint b{color:var(--ink)}

.scale{position:relative;height:252px;margin:0 14px}
.bar{position:absolute;left:0;right:0;top:112px;height:44px;border-radius:7px;background:var(--good-soft);border:1px solid #BFD9C9}
.wait{position:absolute;left:0;top:112px;height:44px;width:%(pwait)s%%;border-radius:7px 0 0 7px;background:repeating-linear-gradient(135deg,var(--wait) 0 7px,#D9D1C2 7px 14px);border:1px solid #B5AB99}
.tk{position:absolute;top:156px;transform:translateX(-50%%);color:var(--taupe);font-size:12px}
.tk i{display:block;width:1px;height:7px;background:#CFC5B4;margin:0 auto 3px}
.tk.big i{height:13px;background:var(--taupe)}
.tk span{display:block;white-space:nowrap}

.ans{position:absolute;left:0;top:4px;width:360px;display:flex;align-items:center;gap:16px;background:var(--surface);border:1px solid var(--hair);border-radius:14px;padding:14px 18px}
.ans .num{font-family:'Cormorant Garamond',serif;font-weight:700;font-size:46px;line-height:1;color:var(--brick)}
.ans .tx{font-size:14.5px;color:var(--ink-2);line-height:1.34}
.ans .tx b{color:var(--ink)}

.pin{position:absolute;top:0;transform:translateX(-50%%);text-align:center;width:210px}
.pin .lbl{display:inline-block;background:var(--brick);color:#fff;border-radius:9px;padding:7px 13px;font-size:14px;font-weight:700;white-space:nowrap}
.pin .note{font-size:12.5px;color:var(--ink-2);line-height:1.3;margin-top:5px}
.pin .stick{position:absolute;left:50%%;top:62px;width:2px;height:50px;background:var(--brick);transform:translateX(-50%%)}

.edge{position:absolute;top:196px;transform:translateX(-50%%);text-align:center;width:168px}
.edge .t{font-size:13px;font-weight:700;color:var(--ink)}
.edge .d{font-size:12px;color:var(--taupe);margin-top:1px}
.edge .v{position:absolute;left:50%%;top:-38px;width:2px;height:34px;background:var(--taupe);transform:translateX(-50%%)}

.legend{display:flex;gap:26px;margin-top:26px;padding-left:14px}
.lg{display:flex;align-items:center;gap:9px;font-size:14px;color:var(--ink-2)}
.lg i{width:26px;height:14px;border-radius:4px;display:block}
.lg.a i{background:repeating-linear-gradient(135deg,var(--wait) 0 6px,#D9D1C2 6px 12px);border:1px solid #B5AB99}
.lg.b i{background:var(--good-soft);border:1px solid #BFD9C9}

.foot{margin-top:auto;display:flex;align-items:center;gap:18px;padding-top:20px}
.foot .msg{flex:1 1 auto;background:var(--brick-soft);border:1px solid var(--brick);border-radius:14px;padding:11px 20px;font-size:14.5px;color:var(--ink);line-height:1.34}
.foot .msg b{color:var(--brick)}
.brand{display:flex;align-items:center;gap:10px;color:var(--ink);flex:0 0 auto}
.brand b{font-family:'Cormorant Garamond',serif;font-weight:700;font-size:23px}
.brand .dot2{width:9px;height:9px;border-radius:50%%;background:var(--brick)}
.brand span{color:var(--taupe);font-size:15px}
</style></head><body>
<div class="wrap">
  <div class="top">
    <div>
      <div class="eyebrow">Двадцать четыре месяца</div>
      <h2>Считать нужно <i>назад от дедлайна</i></h2>
    </div>
    <div class="hint">Срок идёт <b>с дня экзамена</b>, а не с того дня, когда вы получили результат на руки.</div>
  </div>

  <div class="scale">
    <div class="ans"><span class="num">%(months)d</span><span class="tx"><b>месяца — весь срок результата.</b> Вся полоса ниже и есть эти два года</span></div>
    <div class="bar"></div>
    <div class="wait"></div>
    %(ticks)s
    <div class="edge" style="left:0%%"><div class="t">День экзамена</div><div class="d">отсчёт пошёл</div><span class="v"></span></div>
    <div class="edge" style="left:100%%"><div class="t">Срок вышел</div><div class="d">подать уже нельзя</div><span class="v"></span></div>
    <div class="pin" style="left:%(pdl)s%%"><span class="lbl">Ваш дедлайн подачи</span><div class="note">от него и отсчитывайте назад, выбирая дату экзамена</div><span class="stick"></span></div>
  </div>

  <div class="legend">
    <span class="lg a"><i></i>результат ещё идёт — несколько недель</span>
    <span class="lg b"><i></i>результат принимают</span>
  </div>

  <div class="foot">
    <div class="msg">Месяцы на шкале — <b>для наглядности, а не норматив</b>: сроки получения результата зависят от сессии и центра</div>
    <div class="brand"><span class="dot2"></span><b>Kitai School</b><span>&middot; kitai-school.ru</span></div>
  </div>
</div>
</body></html>""" % dict(fonts=FONTS, vars=VARS, h=568, ticks=ticks,
                          pwait=PCT_WAIT, pdl=PCT_DL, months=MONTHS)

open(S + "srok-info.html", "w", encoding="utf-8").write(info)

print("ok | срок:", MONTHS, "мес | ожидание:", WAIT, "| дедлайн на", DEADLINE)
print("отметки: ожидание %d %%, дедлайн %d %% — по порядку" % (PCT_WAIT, PCT_DL))
