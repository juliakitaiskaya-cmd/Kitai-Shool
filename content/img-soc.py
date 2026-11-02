# -*- coding: utf-8 -*-
# Картинки к статье «Самая популярная социальная сеть в Китае»
# Обложка     — экран телефона, где сетка из десяти иконок перекрыта одной
# Инфографика — стопка слоёв против рассыпанного набора отдельных приложений
S = ("/tmp/claude-0/-home-user-Kitai-Shool/a463bfca-82a9-56fd-ae09-42a7257ff999/"
     "scratchpad/")

FONTS = ("<link href=\"https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,600;0,700;1,600"
         "&family=Inter:wght@400;500;600;700&family=Noto+Serif+SC:wght@600;700&display=swap\" rel=\"stylesheet\">")
VARS = (":root{--brick:#A41E3A;--brick-d:#841630;--brick-soft:#F7E6EB;--ink:#2C2420;--ink-2:#5A4F45;"
        "--taupe:#8B7D6B;--cream:#FAF7F2;--cream-2:#F3EDE3;--hair:#EAE3D8;--surface:#fff;"
        "--sky:#39597F;--sky-soft:#E8EEF5;--grey:#B6ADA1}")

# ─────────────────────────── данные ───────────────────────────
# задачи, которые у нас решает отдельное приложение
TASKS = ["Переписка", "Лента друзей", "Оплата", "Переводы", "Доставка еды",
         "Запись к врачу", "Билеты", "Такси", "Документы", "Госуслуги"]

# слои одного приложения: (иероглифы, чтение, название, что делает, какие задачи закрывает)
LAYERS = [
    ("微信", "wēixìn", "Переписка", "личные и групповые чаты",
     ["Переписка"]),
    ("朋友圈", "péngyouquān", "Лента друзей", "видят только ваши контакты",
     ["Лента друзей"]),
    ("微信支付", "wēixìn zhīfù", "Кошелёк", "оплата по коду и переводы",
     ["Оплата", "Переводы"]),
    ("小程序", "xiǎochéngxù", "Мини-приложения", "запускаются внутри, не ставятся отдельно",
     ["Доставка еды", "Запись к врачу", "Билеты", "Такси"]),
    ("公众号", "gōngzhònghào", "Официальные аккаунты", "организации, школы, ведомства",
     ["Документы", "Госуслуги"]),
]

# ── проверки данных
covered = [t for l in LAYERS for t in l[4]]
assert len(covered) == len(set(covered)), "задача названа в двух слоях сразу"
assert sorted(covered) == sorted(TASKS), "состав задач слева и справа не совпал"
assert len(TASKS) == 10, "задач должно быть десять, их %d" % len(TASKS)
assert len(LAYERS) == 5, "слоёв должно быть пять, их %d" % len(LAYERS)
names = [l[0] for l in LAYERS]
assert len(names) == len(set(names)), "слой назван дважды"
# сетка обложки: десять задач раскладываются ровно по строкам
COLS = 2
assert len(TASKS) % COLS == 0, "сетка не делится на %d столбца" % COLS
ROWS = len(TASKS) // COLS

icons = "".join('<div class="ic"><span class="sq"></span><b>%s</b></div>' % t for t in TASKS)

hero = """<!DOCTYPE html><html lang="ru"><head><meta charset="utf-8">
%(fonts)s
<style>
%(vars)s
*{margin:0;box-sizing:border-box}html,body{width:1200px;height:630px}
.card{width:1200px;height:630px;background:radial-gradient(1020px 680px at 12%% 8%%, #fff 0%%, var(--cream) 50%%, var(--cream-2) 100%%);position:relative;overflow:hidden;font-family:'Inter',sans-serif;padding:56px 56px 0 72px;display:flex;justify-content:space-between}
.card:before{content:"";position:absolute;left:0;top:0;bottom:0;width:12px;background:var(--brick)}
.txt{flex:0 0 536px;padding-top:12px}
.eyebrow{color:var(--brick);font-weight:700;font-size:18px;letter-spacing:.19em;text-transform:uppercase;margin-bottom:14px}
h1{font-family:'Cormorant Garamond',serif;font-weight:600;font-size:46px;line-height:1.06;color:var(--ink);letter-spacing:-.4px}
h1 i{font-style:italic;color:var(--brick)}
.sub{font-size:18px;color:var(--ink-2);line-height:1.42;max-width:32ch;margin-top:17px}
.tip{display:inline-block;margin-top:24px;background:var(--surface);border:1px solid var(--hair);border-left:4px solid var(--brick);border-radius:13px;padding:14px 20px;font-size:16px;color:var(--ink-2);line-height:1.38;max-width:34ch}
.tip b{color:var(--ink)}
.tip em{font-family:'Noto Serif SC',serif;font-style:normal;font-weight:700;color:var(--brick)}

.scene{flex:0 0 400px;display:flex;flex-direction:column;align-items:center;padding-top:4px}
.phone{position:relative;width:334px;height:456px;border-radius:38px;background:#fff;border:9px solid #24201C;box-shadow:0 18px 38px rgba(44,36,32,.22);overflow:hidden}
.notch{position:absolute;left:50%%;transform:translateX(-50%%);top:0;width:108px;height:19px;background:#24201C;border-radius:0 0 13px 13px;z-index:4}
.grid{position:absolute;left:0;right:0;top:0;padding:38px 22px 0;display:grid;grid-template-columns:repeat(%(cols)d,1fr);gap:16px 14px;align-content:start}
.ic{display:flex;align-items:center;gap:8px;opacity:.42;height:33px}
.ic .sq{flex:0 0 auto;width:28px;height:28px;border-radius:9px;background:var(--grey);border:1px solid #A4998C}
.ic b{font-size:11.5px;font-weight:600;color:var(--ink-2);line-height:1.12;text-decoration:line-through;text-decoration-color:#8B7D6B}
.cover{position:absolute;left:20px;right:20px;bottom:18px;height:116px;border-radius:30px;background:linear-gradient(160deg,var(--brick) 0%%,var(--brick-d) 100%%);box-shadow:0 14px 28px rgba(164,30,58,.32);display:flex;align-items:center;gap:16px;padding:0 20px;z-index:3;color:#fff}
.cover b{flex:0 0 auto;white-space:nowrap;font-family:'Noto Serif SC',serif;font-weight:700;font-size:44px;line-height:1.02}
.cover .cl{display:flex;flex-direction:column}
.cover span{font-size:14px;opacity:.9;letter-spacing:.04em}
.cover em{font-style:normal;font-size:15px;font-weight:600;line-height:1.28;margin-top:4px}
.cap{margin-top:20px;text-align:center;font-size:16.5px;color:var(--ink-2);line-height:1.4;max-width:30ch}
.cap b{color:var(--ink)}
.brand{position:absolute;left:72px;bottom:28px;display:flex;align-items:center;gap:11px;color:var(--ink)}
.brand b{font-family:'Cormorant Garamond',serif;font-weight:700;font-size:26px}
.brand .bdot{width:10px;height:10px;border-radius:50%%;background:var(--brick)}
.brand span{color:var(--taupe);font-size:16px}
</style></head><body>
<div class="card">
  <div class="txt">
    <div class="eyebrow">Китайский интернет</div>
    <h1>Самая популярная социальная сеть в Китае: <i>одно приложение на месте десяти</i></h1>
    <div class="sub">Переписка, оплата, доставка, запись, билеты, документы — всё открывается там же, где чат.</div>
    <div class="tip"><em>微信</em> — <b>не просто мессенджер:</b> сервисы запускаются внутри него и не ставятся отдельно.</div>
    <div class="brand"><span class="bdot"></span><b>Kitai School</b><span>&middot; kitai-school.ru</span></div>
  </div>

  <div class="scene">
    <div class="phone">
      <div class="notch"></div>
      <div class="grid">%(icons)s</div>
      <div class="cover"><b>微信</b><div class="cl"><span>wēixìn</span><em>всё это &mdash; здесь</em></div></div>
    </div>
    <div class="cap">Десять отдельных значков <b>становятся не нужны</b></div>
  </div>
</div>
</body></html>""" % dict(fonts=FONTS, vars=VARS, icons=icons, cols=COLS)

open(S + "soc-hero.html", "w", encoding="utf-8").write(hero)

# ─────────────────────────── инфографика ───────────────────────────
layers = "".join(
    '<div class="ly"><div class="lh"><b class="han">%s</b><i>%s</i></div>'
    '<div class="lb"><span class="nm">%s</span><span class="ds">%s</span></div>'
    '<div class="cnt">%d</div></div>' % (z, p, nm, ds, len(tasks))
    for z, p, nm, ds, tasks in LAYERS)

cards = "".join('<div class="ap"><span class="sq"></span><b>%s</b></div>' % t for t in TASKS)

info = """<!DOCTYPE html><html lang="ru"><head><meta charset="utf-8">
%(fonts)s
<style>
%(vars)s
*{margin:0;box-sizing:border-box}html,body{width:1200px;height:%(h)dpx}
.wrap{width:1200px;height:%(h)dpx;background:linear-gradient(180deg,#fff 0%%,var(--cream) 40%%,var(--cream-2) 100%%);font-family:'Inter',sans-serif;padding:38px 48px 30px;display:flex;flex-direction:column;position:relative;overflow:hidden}
.wrap:before{content:"";position:absolute;left:0;right:0;top:0;height:9px;background:var(--brick)}
.top{display:flex;align-items:flex-end;justify-content:space-between;gap:34px;margin-bottom:24px}
.eyebrow{color:var(--brick);font-weight:700;font-size:15.5px;letter-spacing:.19em;text-transform:uppercase;margin-bottom:8px}
h2{font-family:'Cormorant Garamond',serif;font-weight:600;font-size:38px;line-height:1.07;color:var(--ink);max-width:20ch}
h2 i{font-style:italic;color:var(--brick)}
.hint{flex:0 0 404px;background:var(--surface);border:1px solid var(--hair);border-left:4px solid var(--brick);border-radius:13px;padding:12px 18px;font-size:15px;color:var(--ink-2);line-height:1.36}
.hint b{color:var(--ink)}

.cols{display:grid;grid-template-columns:1fr 92px 1fr;gap:0;align-items:start}
.side{display:flex;flex-direction:column}
.shd{font-size:14.5px;font-weight:700;letter-spacing:.05em;text-transform:uppercase;margin-bottom:11px}
.shd.l{color:var(--brick)}
.shd.r{color:var(--taupe)}

.stack{border-radius:16px;overflow:hidden;border:2px solid var(--brick);box-shadow:0 14px 28px rgba(44,36,32,.14)}
.ly{display:flex;align-items:center;gap:14px;padding:13px 16px;background:var(--surface);border-bottom:1px dashed #E2B9C5}
.ly:last-child{border-bottom:none}
.ly:nth-child(odd){background:var(--brick-soft)}
.lh{flex:0 0 132px;text-align:center}
.lh b{display:block;font-family:'Noto Serif SC',serif;font-weight:700;font-size:23px;line-height:1.1;color:var(--brick-d)}
.lh i{display:block;font-style:normal;font-size:11.5px;color:var(--taupe);margin-top:1px}
.lb{flex:1 1 auto}
.lb .nm{display:block;font-size:15.5px;font-weight:700;color:var(--ink)}
.lb .ds{display:block;font-size:13px;color:var(--ink-2);line-height:1.3;margin-top:2px}
.cnt{flex:0 0 auto;width:30px;height:30px;border-radius:50%%;background:var(--brick);color:#fff;font-size:14px;font-weight:700;display:flex;align-items:center;justify-content:center}

.mid{display:flex;flex-direction:column;align-items:center;padding-top:118px;gap:0}
.mid .vs{font-family:'Cormorant Garamond',serif;font-weight:700;font-size:25px;color:var(--taupe)}
.mid .ar{width:1px;height:132px;background:#D4C9B8;margin-top:10px}

.apps{display:grid;grid-template-columns:1fr 1fr;gap:11px}
.ap{display:flex;align-items:center;gap:10px;background:var(--surface);border:1px solid var(--hair);border-radius:12px;padding:11px 12px}
.ap .sq{flex:0 0 auto;width:26px;height:26px;border-radius:8px;background:var(--grey)}
.ap b{font-size:13px;font-weight:600;color:var(--ink-2);line-height:1.15}

.notes{display:grid;grid-template-columns:1fr 1fr;gap:16px;margin-top:18px}
.nt{background:var(--surface);border:1px solid var(--hair);border-radius:13px;padding:12px 17px;font-size:14.5px;color:var(--ink-2);line-height:1.36}
.nt b{color:var(--ink)}
.nt.l{border-left:4px solid var(--brick)}
.nt.r{border-left:4px solid var(--grey)}

.foot{margin-top:auto;display:flex;align-items:center;gap:18px;padding-top:18px}
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
      <div class="eyebrow">Устройство, а не рейтинг</div>
      <h2>Пять слоёв одного приложения — <i>или десять отдельных</i></h2>
    </div>
    <div class="hint">Слева и справа <b>один и тот же набор задач.</b> Разница в том, сколько всего нужно поставить и где это открывается.</div>
  </div>

  <div class="cols">
    <div class="side">
      <div class="shd l">Один <span class="han">微信</span>: пять слоёв</div>
      <div class="stack">%(layers)s</div>
    </div>
    <div class="mid"><div class="vs">против</div><div class="ar"></div></div>
    <div class="side">
      <div class="shd r">Те же задачи по отдельности</div>
      <div class="apps">%(cards)s</div>
    </div>
  </div>

  <div class="notes">
    <div class="nt l"><b>Главное отличие:</b> мини-приложения запускаются внутри и не ставятся отдельно — поэтому список значков не растёт.</div>
    <div class="nt r">Кружок у слоя показывает, <b>сколько задач он закрывает</b>: пять слоёв против десяти значков.</div>
  </div>

  <div class="foot">
    <div class="msg">Чисел аудитории и мест в рейтинге здесь нет намеренно: <b>проверить их по первоисточнику я не могу</b></div>
    <div class="brand"><span class="dot2"></span><b>Kitai School</b><span>&middot; kitai-school.ru</span></div>
  </div>
</div>
</body></html>""" % dict(fonts=FONTS, vars=VARS, h=752, layers=layers, cards=cards)

open(S + "soc-info.html", "w", encoding="utf-8").write(info)

print("ok | слоёв:", len(LAYERS), "| задач:", len(TASKS),
      "| сетка:", "%dx%d" % (COLS, ROWS))
print("состав задач слева и справа совпадает — проверено ассертом")
print("задач по слоям:", [len(l[4]) for l in LAYERS], "сумма", sum(len(l[4]) for l in LAYERS))
