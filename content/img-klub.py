# -*- coding: utf-8 -*-
# Картинки к статье «Разговорный клуб с носителем языка»
# Обложка    — микрофон, который передают: слово переходит, а не достаётся одному
# Инфографика — круглый стол сверху: как устроена встреча
S = "/tmp/claude-0/-home-user-Kitai-Shool/a463bfca-82a9-56fd-ae09-42a7257ff999/scratchpad/"

FONTS = ("<link href=\"https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,600;0,700;1,600"
         "&family=Inter:wght@400;500;600;700&family=Noto+Serif+SC:wght@600;700&display=swap\" rel=\"stylesheet\">")
VARS = (":root{--brick:#A41E3A;--brick-d:#841630;--brick-soft:#F7E6EB;--ink:#2C2420;--ink-2:#5A4F45;"
        "--taupe:#8B7D6B;--cream:#FAF7F2;--cream-2:#F3EDE3;--hair:#EAE3D8;--surface:#fff;"
        "--green:#1E7A46;--green-s:#E3F6E9;--amber:#C08A2E;--amber-s:#FBF2DF;--blue:#2F5D8C;--blue-s:#E7EEF6;"
        "--mic:#4A4541;--mic-2:#332F2C;--mesh:#9A938A;--skin:#E8C9A8;--skin-2:#D4AE86}")

hero = """<!DOCTYPE html><html lang="ru"><head><meta charset="utf-8">
%s
<style>
%s
*{margin:0;box-sizing:border-box}html,body{width:1200px;height:630px}
.card{width:1200px;height:630px;background:radial-gradient(1050px 660px at 14%% 12%%, #fff 0%%, var(--cream) 52%%, var(--cream-2) 100%%);position:relative;overflow:hidden;font-family:'Inter',sans-serif;padding:50px 46px 0 72px;display:flex;justify-content:space-between}
.card:before{content:"";position:absolute;left:0;top:0;bottom:0;width:12px;background:var(--brick)}
.txt{flex:0 0 520px;padding-top:4px}
.eyebrow{color:var(--brick);font-weight:700;font-size:18px;letter-spacing:.19em;text-transform:uppercase;margin-bottom:13px}
h1{font-family:'Cormorant Garamond',serif;font-weight:600;font-size:46px;line-height:1.06;color:var(--ink);letter-spacing:-.4px}
h1 i{font-style:italic;color:var(--brick)}
.sub{font-size:18px;color:var(--ink-2);line-height:1.42;max-width:32ch;margin-top:16px}
.note{display:inline-block;margin-top:22px;background:var(--surface);border:1px solid var(--hair);border-left:4px solid var(--brick);border-radius:13px;padding:13px 19px;font-size:15.5px;color:var(--ink-2);line-height:1.36;max-width:34ch}
.note b{color:var(--ink)}

/* микрофон между двумя руками */
.scene{flex:0 0 536px;position:relative;height:482px}
.ring{position:absolute;left:92px;top:72px;width:352px;height:352px;border-radius:50%%;border:3px dashed rgba(164,30,58,.5)}
.ring:after{content:"";position:absolute;right:-9px;top:160px;border-left:16px solid var(--brick);border-top:9px solid transparent;border-bottom:9px solid transparent}
.mic{position:absolute;left:224px;top:112px;width:88px;height:250px;transform:rotate(-13deg)}
.head{position:absolute;left:0;top:0;width:88px;height:88px;border-radius:50%%;background:radial-gradient(circle at 34%% 30%%, #B8B1A7, var(--mesh));box-shadow:inset 0 -6px 14px rgba(0,0,0,.26), 0 6px 14px rgba(44,36,32,.2)}
.head:after{content:"";position:absolute;left:12px;top:12px;right:12px;bottom:12px;border-radius:50%%;background:repeating-radial-gradient(circle at 50%% 50%%, rgba(0,0,0,.22) 0 2px, rgba(255,255,255,.12) 2px 4px)}
.body{position:absolute;left:26px;top:78px;width:36px;height:168px;border-radius:9px;background:linear-gradient(90deg,var(--mic-2),var(--mic),var(--mic-2));box-shadow:0 8px 18px rgba(44,36,32,.24)}
.body:after{content:"";position:absolute;left:7px;right:7px;top:34px;height:3px;background:rgba(255,255,255,.22);border-radius:2px}
.tag{position:absolute;left:52px;top:48px;background:var(--surface);border:1px solid var(--hair);border-radius:11px;padding:9px 15px;font-size:14.5px;color:var(--ink-2);line-height:1.3}
.tag b{color:var(--ink)}
.cap{position:absolute;left:0;right:0;bottom:16px;text-align:center;font-size:15.5px;color:var(--ink-2);line-height:1.34}
.cap b{color:var(--ink)}
.brand{position:absolute;left:72px;bottom:28px;display:flex;align-items:center;gap:11px;color:var(--ink)}
.brand b{font-family:'Cormorant Garamond',serif;font-weight:700;font-size:26px}
.brand .bdot{width:10px;height:10px;border-radius:50%%;background:var(--brick)}
.brand span{color:var(--taupe);font-size:16px}
</style></head><body>
<div class="card">
  <div class="txt">
    <div class="eyebrow">Формат</div>
    <h1>Разговорный клуб <i>с носителем языка</i></h1>
    <div class="sub">Клуб не даёт говорения сам по себе: он даёт возможность, которой нужно воспользоваться</div>
    <div class="note"><b>Разница между «ходил» и «говорил»</b> решает всё: три реплики за встречу — это присутствие, а не практика</div>
  </div>
  <div class="scene">
    <div class="ring"></div>
    <div class="mic"><div class="head"></div><div class="body"></div></div>
    <div class="tag"><b>Слово переходит</b> по кругу</div>
    <div class="cap">Берите его сами — <b>ждать вопроса ведущего необязательно</b></div>
  </div>
  <div class="brand"><span class="bdot"></span><b>Kitai School</b><span>&middot; kitai-school.ru</span></div>
</div>
</body></html>""" % (FONTS, VARS)

open(S + "kb-hero.html", "w", encoding="utf-8").write(hero)

# -------------------------------------------------------------- инфографика
SEATS = [
    (0, "Ведущий", "var(--brick)"),
    (51, "Участник", "var(--blue)"),
    (103, "Участник", "var(--blue)"),
    (154, "Участник", "var(--blue)"),
    (206, "Участник", "var(--blue)"),
    (257, "Участник", "var(--blue)"),
    (309, "Участник", "var(--blue)"),
]

seats = "\n".join(
    '<div class="seat" style="transform:rotate(%ddeg) translate(0,-176px) rotate(%ddeg)">'
    '<span style="background:%s"></span></div>' % (a, -a, c) for a, t, c in SEATS)

STAGES = [
    ("0–10 мин", "Разминка", "короткий круг: как прошла неделя, одна фраза от каждого"),
    ("10–25 мин", "Тема", "ведущий вводит вопрос и ключевые слова, которые пригодятся"),
    ("25–60 мин", "Обсуждение", "основная часть: мнения, возражения, уточнения"),
    ("60–75 мин", "Пары", "разговор по двое, чтобы говорили все, а не самые смелые"),
    ("75–90 мин", "Итог", "ведущий возвращает ошибки и выражения, которых не хватало"),
]

stages = "\n".join(
    '<div class="st"><div class="t">%s</div><div class="n">%s</div><div class="d">%s</div></div>'
    % s for s in STAGES)

info = """<!DOCTYPE html><html lang="ru"><head><meta charset="utf-8">
%s
<style>
%s
*{margin:0;box-sizing:border-box}html,body{width:1200px;height:HGTpx}
.wrap{width:1200px;height:HGTpx;background:linear-gradient(180deg,#fff 0%%,var(--cream) 46%%,var(--cream-2) 100%%);font-family:'Inter',sans-serif;padding:32px 46px 32px;display:flex;flex-direction:column}
.top{display:flex;align-items:flex-end;justify-content:space-between;gap:30px;margin-bottom:18px}
.eyebrow{color:var(--brick);font-weight:700;font-size:14.5px;letter-spacing:.17em;text-transform:uppercase;margin-bottom:7px}
h2{font-family:'Cormorant Garamond',serif;font-weight:600;font-size:40px;line-height:1.07;color:var(--ink);letter-spacing:-.3px}
h2 i{font-style:italic;color:var(--brick)}
.hint{flex:0 0 366px;background:var(--surface);border:1px solid var(--hair);border-left:4px solid var(--brick);border-radius:12px;padding:12px 17px;font-size:14.5px;color:var(--ink-2);line-height:1.36}
.hint b{color:var(--ink)}

.main{display:flex;gap:30px;align-items:center}
.round{flex:0 0 424px;height:452px;position:relative;display:flex;align-items:center;justify-content:center;padding-bottom:24px}
.legend{position:absolute;left:0;right:0;bottom:0;display:flex;justify-content:center;gap:24px;font-size:14px;color:var(--ink-2)}
.legend span{display:flex;align-items:center;gap:8px}
.legend i{width:14px;height:14px;border-radius:50%%;display:block}
.table{width:214px;height:214px;border-radius:50%%;background:var(--surface);border:2px solid var(--hair);box-shadow:0 8px 20px rgba(44,36,32,.08);display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center;padding:0 24px}
.table b{font-family:'Cormorant Garamond',serif;font-size:26px;color:var(--ink);line-height:1.15}
.table span{font-size:14px;color:var(--taupe);margin-top:7px;line-height:1.3}
.seat{position:absolute;left:50%%;top:calc(50%% - 23px);width:0;height:0}
.seat span{position:absolute;left:-23px;top:-23px;width:46px;height:46px;border-radius:50%%;box-shadow:0 5px 12px rgba(44,36,32,.2)}

.stages{flex:1 1 auto;display:flex;flex-direction:column;gap:9px}
.st{display:flex;align-items:baseline;gap:16px;background:var(--surface);border:1px solid var(--hair);border-radius:12px;padding:11px 18px;box-shadow:0 4px 11px rgba(44,36,32,.05)}
.st .t{flex:0 0 108px;font-size:14px;font-weight:700;color:var(--brick)}
.st .n{flex:0 0 132px;font-size:16px;font-weight:600;color:var(--ink)}
.st .d{flex:1 1 auto;font-size:14.5px;color:var(--ink-2);line-height:1.34}

.foot{margin-top:auto;display:flex;align-items:center;gap:18px;padding-top:16px}
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
      <div class="eyebrow">Как проходит встреча</div>
      <h2>Полтора часа <i>по кругу</i></h2>
    </div>
    <div class="hint">Это <b>наш формат, а не общий стандарт</b>: у разных школ этапы и тайминг свои. Сверяйте с тем, что вам предлагают.</div>
  </div>

  <div class="main">
    <div class="round">
%s
      <div class="table"><b>Тема встречи</b><span>известна заранее, слова даны до начала</span></div>
      <div class="legend"><span><i style="background:var(--brick)"></i>ведущий</span><span><i style="background:var(--blue)"></i>участники</span></div>
    </div>
    <div class="stages">
%s
    </div>
  </div>

  <div class="foot">
    <div class="msg">Главное на что смотреть при выборе: <b>есть ли часть в парах</b> — без неё говорят только самые смелые</div>
    <div class="brand"><span class="dot2"></span><b>Kitai School</b><span>&middot; kitai-school.ru</span></div>
  </div>
</div>
</body></html>""" % (FONTS, VARS, seats, stages)

info = info.replace("HGT", "672")
open(S + "kb-info.html", "w", encoding="utf-8").write(info)
print("ok")
