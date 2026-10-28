# -*- coding: utf-8 -*-
# Картинки к статье «Пассивный залог в китайском»
# Обложка    — след от предмета на столе: 手机被偷了
# Инфографика — скелет конструкции с необязательным блоком и три альтернативы
S = ("/tmp/claude-0/-home-user-Kitai-Shool/a463bfca-82a9-56fd-ae09-42a7257ff999/"
     "scratchpad/")

FONTS = ("<link href=\"https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,600;0,700;1,600"
         "&family=Inter:wght@400;500;600;700&family=Noto+Serif+SC:wght@600;700&display=swap\" rel=\"stylesheet\">")
VARS = (":root{--brick:#A41E3A;--brick-d:#841630;--brick-soft:#F7E6EB;--ink:#2C2420;--ink-2:#5A4F45;"
        "--taupe:#8B7D6B;--cream:#FAF7F2;--cream-2:#F3EDE3;--hair:#EAE3D8;--surface:#fff;"
        "--desk:#C9A981;--desk-2:#AD8B63;--dust:#DCC6A6;--slate:#2F5D8C;--good:#1E7A46}")

hero = """<!DOCTYPE html><html lang="ru"><head><meta charset="utf-8">
%s
<style>
%s
*{margin:0;box-sizing:border-box}html,body{width:1200px;height:630px}
.card{width:1200px;height:630px;background:radial-gradient(1050px 660px at 14%% 12%%, #fff 0%%, var(--cream) 52%%, var(--cream-2) 100%%);position:relative;overflow:hidden;font-family:'Inter',sans-serif;padding:84px 46px 0 72px;display:flex;justify-content:space-between}
.card:before{content:"";position:absolute;left:0;top:0;bottom:0;width:12px;background:var(--brick)}
.txt{flex:0 0 506px;padding-top:6px}
.eyebrow{color:var(--brick);font-weight:700;font-size:18px;letter-spacing:.19em;text-transform:uppercase;margin-bottom:13px}
h1{font-family:'Cormorant Garamond',serif;font-weight:600;font-size:45px;line-height:1.07;color:var(--ink);letter-spacing:-.4px}
h1 i{font-style:italic;color:var(--brick)}
.sub{font-size:18px;color:var(--ink-2);line-height:1.42;max-width:31ch;margin-top:16px}
.tip{display:inline-block;margin-top:22px;background:var(--surface);border:1px solid var(--hair);border-left:4px solid var(--brick);border-radius:13px;padding:13px 19px;font-size:15.5px;color:var(--ink-2);line-height:1.36;max-width:35ch}
.tip b{color:var(--ink)}

/* след от предмета на столе */
.scene{flex:0 0 468px;padding-top:28px;display:flex;flex-direction:column;align-items:center}
.desk{position:relative;width:372px;height:306px;border-radius:14px;background:linear-gradient(165deg,#D8BC97,var(--desk) 55%%,var(--desk-2));box-shadow:0 16px 30px rgba(44,36,32,.24), inset 0 2px 0 rgba(255,255,255,.22);overflow:hidden}
.desk:before{content:"";position:absolute;left:-30px;top:92px;right:-30px;height:1px;background:rgba(80,58,36,.16)}
.desk:after{content:"";position:absolute;left:-30px;top:186px;right:-30px;height:1px;background:rgba(80,58,36,.12)}
.trace{position:absolute;left:62px;top:58px;width:124px;height:200px;border-radius:14px;border:3px dashed rgba(255,255,255,.72);background:rgba(255,255,255,.18)}
.trace span{position:absolute;left:0;right:0;top:50%%;transform:translateY(-50%%);text-align:center;font-size:15px;color:#6B4F32;letter-spacing:.04em}
.plate{position:absolute;right:-18px;bottom:20px;background:var(--surface);border:1px solid var(--hair);border-radius:15px;padding:13px 20px 15px;box-shadow:0 10px 20px rgba(44,36,32,.2);text-align:center}
.plate .h{font-family:'Noto Serif SC',serif;font-size:30px;color:var(--ink);line-height:1.2}
.plate .h b{color:var(--brick)}
.plate .p{font-size:14px;color:var(--ink-2);font-style:italic;margin-top:4px}
.plate .r{font-size:14.5px;color:var(--taupe);margin-top:1px}
.cap{margin-top:24px;text-align:center;font-size:16.5px;color:var(--ink-2);line-height:1.4;max-width:37ch}
.cap b{color:var(--ink)}
.brand{position:absolute;left:72px;bottom:28px;display:flex;align-items:center;gap:11px;color:var(--ink)}
.brand b{font-family:'Cormorant Garamond',serif;font-weight:700;font-size:26px}
.brand .bdot{width:10px;height:10px;border-radius:50%%;background:var(--brick)}
.brand span{color:var(--taupe);font-size:16px}
</style></head><body>
<div class="card">
  <div class="txt">
    <div class="eyebrow">Грамматика</div>
    <h1>Пассивный залог <i>в китайском</i></h1>
    <div class="sub">被 ставят там, где с предметом что-то случилось — чаще неприятное</div>
    <div class="tip"><b>Кто именно это сделал — можно не называть.</b> В конструкции с 被 деятель необязателен</div>
  </div>
  <div class="scene">
    <div class="desk">
      <div class="trace"><span>было здесь</span></div>
      <div class="plate">
        <div class="h">手机<b>被</b>偷了</div>
        <div class="p">shǒujī bèi tōu le</div>
        <div class="r">телефон украли</div>
      </div>
    </div>
    <div class="cap">Объект на первом месте, <b>а виновник может и не появиться</b></div>
  </div>
  <div class="brand"><span class="bdot"></span><b>Kitai School</b><span>&middot; kitai-school.ru</span></div>
</div>
</body></html>""" % (FONTS, VARS)

open(S + "bei-hero.html", "w", encoding="utf-8").write(hero)

# --------------------------------------------------------------- инфографика
SLOTS = [
    ("手机", "объект", "req"),
    ("被", "показатель", "key"),
    ("小偷", "деятель", "opt"),
    ("偷", "глагол", "req"),
    ("了", "результат", "req"),
]

assert sum(1 for s in SLOTS if s[2] == "opt") == 1, "необязательный блок не один"
assert sum(1 for s in SLOTS if s[2] == "key") == 1, "показатель отмечен не один раз"

slots = "".join(
    '<div class="sl %s"><div class="lb">%s</div><div class="vv">%s</div>%s</div>'
    % (cls, lab, han, '<div class="opt">можно убрать</div>' if cls == "opt" else "")
    for han, lab, cls in SLOTS)

ALT = [
    ("叫 / 让", "jiào / ràng", "разговорная замена 被",
     "我的车叫人撞了 — мою машину задели"),
    ("без показателя", "—", "форма активная, смысл пассивный",
     "饭做好了 — еда готова"),
    ("是…的", "shì… de", "когда важно, кем и когда",
     "这本书是他写的 — эту книгу написал он"),
]

alt = "".join(
    '<div class="al"><div class="ah">%s</div><div class="ap">%s</div>'
    '<div class="at">%s</div><div class="ad">%s</div></div>' % a for a in ALT)

info = """<!DOCTYPE html><html lang="ru"><head><meta charset="utf-8">
%(fonts)s
<style>
%(vars)s
*{margin:0;box-sizing:border-box}html,body{width:1200px;height:HGTpx}
.wrap{width:1200px;height:HGTpx;background:linear-gradient(180deg,#fff 0%%,var(--cream) 46%%,var(--cream-2) 100%%);font-family:'Inter',sans-serif;padding:32px 46px 28px;display:flex;flex-direction:column}
.top{display:flex;align-items:flex-end;justify-content:space-between;gap:30px;margin-bottom:20px}
.eyebrow{color:var(--brick);font-weight:700;font-size:14.5px;letter-spacing:.17em;text-transform:uppercase;margin-bottom:7px}
h2{font-family:'Cormorant Garamond',serif;font-weight:600;font-size:40px;line-height:1.07;color:var(--ink);letter-spacing:-.3px}
h2 i{font-style:italic;color:var(--brick)}
.hint{flex:0 0 378px;background:var(--surface);border:1px solid var(--hair);border-left:4px solid var(--brick);border-radius:12px;padding:12px 17px;font-size:14.5px;color:var(--ink-2);line-height:1.36}
.hint b{color:var(--ink)}

.line{display:flex;gap:11px;align-items:stretch}
.sl{flex:1 1 0;background:var(--surface);border:2px solid var(--hair);border-radius:14px;padding:12px 10px 13px;text-align:center;box-shadow:0 4px 11px rgba(44,36,32,.05);position:relative}
.sl .lb{font-size:12.5px;color:var(--taupe);letter-spacing:.03em}
.sl .vv{font-family:'Noto Serif SC',serif;font-size:31px;color:var(--ink);line-height:1.2;margin-top:3px}
.sl.key{border-color:var(--brick);background:var(--brick-soft)}
.sl.key .lb{color:var(--brick-d);font-weight:700}
.sl.key .vv{color:var(--brick)}
.sl.opt{border-style:dashed;border-color:var(--taupe);background:#FBF9F5}
.sl.opt .vv{color:var(--taupe)}
.sl .opt{font-size:11.5px;color:var(--taupe);margin-top:3px;font-weight:600;letter-spacing:.02em}
.whole{text-align:center;margin-top:13px;font-size:16px;color:var(--ink-2)}
.whole b{font-family:'Noto Serif SC',serif;font-size:21px;color:var(--ink);vertical-align:-1px}

.sep{display:flex;align-items:center;gap:16px;margin:20px 0 14px}
.sep span{font-size:15px;font-weight:700;color:var(--brick-d);white-space:nowrap}
.sep i{flex:1 1 auto;height:1px;background:var(--hair)}

.alts{display:flex;gap:13px}
.al{flex:1 1 0;background:var(--surface);border:1px solid var(--hair);border-left:4px solid var(--good);border-radius:14px;padding:13px 17px}
.ah{font-family:'Noto Serif SC',serif;font-size:23px;color:var(--ink);line-height:1.15}
.ap{font-size:13px;color:var(--ink-2);font-style:italic}
.at{font-size:14px;font-weight:700;color:var(--ink);margin-top:4px}
.ad{font-size:13.5px;color:var(--ink-2);margin-top:2px;line-height:1.3}

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
      <div class="eyebrow">Конструкция с 被</div>
      <h2>Деятеля можно <i>не называть</i></h2>
    </div>
    <div class="hint">После глагола обязательно что-то стоит — 了, результат или дополнение. <b>Пустым глагол в этой конструкции не остаётся.</b></div>
  </div>

  <div class="line">%(slots)s</div>
  <div class="whole">целиком — <b>手机被小偷偷了</b>, а короче — <b>手机被偷了</b></div>

  <div class="sep"><span>Чаще, чем 被, говорят иначе</span><i></i></div>
  <div class="alts">%(alt)s</div>

  <div class="foot">
    <div class="msg">被 звучит тяжеловато — <b>в живой речи его берегут для неприятного</b></div>
    <div class="brand"><span class="dot2"></span><b>Kitai School</b><span>&middot; kitai-school.ru</span></div>
  </div>
</div>
</body></html>""" % dict(fonts=FONTS, vars=VARS, slots=slots, alt=alt)

info = info.replace("HGT", "560")
open(S + "bei-info.html", "w", encoding="utf-8").write(info)
print("ok, блоков:", len(SLOTS), "| альтернатив:", len(ALT))
