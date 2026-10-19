# -*- coding: utf-8 -*-
# Картинки к статье «Стоит ли учить китайский язык»
# Обложка    — монета на ребре: момент до решения
# Инфографика — две колонки: что язык решает и чего не решает
S = "/tmp/claude-0/-home-user-Kitai-Shool/a463bfca-82a9-56fd-ae09-42a7257ff999/scratchpad/"

FONTS = ("<link href=\"https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,600;0,700;1,600"
         "&family=Inter:wght@400;500;600;700&family=Noto+Serif+SC:wght@600;700&display=swap\" rel=\"stylesheet\">")
VARS = (":root{--brick:#A41E3A;--brick-d:#841630;--brick-soft:#F7E6EB;--ink:#2C2420;--ink-2:#5A4F45;"
        "--taupe:#8B7D6B;--cream:#FAF7F2;--cream-2:#F3EDE3;--hair:#EAE3D8;--surface:#fff;"
        "--green:#1E7A46;--green-s:#E3F6E9;--amber:#C08A2E;--blue:#2F5D8C;--blue-s:#E7EEF6;"
        "--coin:#E8C978;--coin-2:#C9A445;--coin-3:#A8842F}")

hero = """<!DOCTYPE html><html lang="ru"><head><meta charset="utf-8">
%s
<style>
%s
*{margin:0;box-sizing:border-box}html,body{width:1200px;height:630px}
.card{width:1200px;height:630px;background:radial-gradient(1050px 660px at 16%% 12%%, #fff 0%%, var(--cream) 52%%, var(--cream-2) 100%%);position:relative;overflow:hidden;font-family:'Inter',sans-serif;padding:52px 56px 0 72px;display:flex;justify-content:space-between}
.card:before{content:"";position:absolute;left:0;top:0;bottom:0;width:12px;background:var(--brick)}
.txt{flex:0 0 548px;padding-top:4px}
.eyebrow{color:var(--brick);font-weight:700;font-size:18px;letter-spacing:.19em;text-transform:uppercase;margin-bottom:13px}
h1{font-family:'Cormorant Garamond',serif;font-weight:600;font-size:47px;line-height:1.06;color:var(--ink);letter-spacing:-.4px}
h1 i{font-style:italic;color:var(--brick)}
.sub{font-size:18.5px;color:var(--ink-2);line-height:1.42;max-width:33ch;margin-top:16px}
.note{display:inline-block;margin-top:22px;background:var(--surface);border:1px solid var(--hair);border-left:4px solid var(--brick);border-radius:13px;padding:13px 19px;font-size:15.5px;color:var(--ink-2);line-height:1.36;max-width:35ch}
.note b{color:var(--ink)}

/* монета на ребре */
.scene{flex:0 0 476px;position:relative;height:452px;display:flex;align-items:center;justify-content:center}
.table-line{position:absolute;left:10px;right:10px;top:330px;height:2px;background:linear-gradient(90deg,rgba(234,227,216,0),var(--hair) 18%%,var(--hair) 82%%,rgba(234,227,216,0))}
.shadow{position:absolute;left:50%%;top:324px;width:210px;height:16px;margin-left:-105px;border-radius:50%%;background:rgba(44,36,32,.16);filter:blur(5px)}
.coin{position:absolute;top:80px;left:50%%;margin-left:-44px;width:88px;height:252px;border-radius:50%%;background:linear-gradient(90deg,#8A6A1E 0%%,var(--coin-2) 14%%,#FBF0CF 38%%,var(--coin) 56%%,var(--coin-2) 78%%,#8A6A1E 100%%);box-shadow:0 12px 26px rgba(44,36,32,.26);transform:rotate(7deg)}
.coin:before{content:"";position:absolute;left:9px;right:9px;top:14px;bottom:14px;border-radius:50%%;border:2px solid rgba(107,81,24,.35)}
.coin span{position:absolute;left:50%%;top:50%%;transform:translate(-50%%,-50%%);font-family:'Noto Serif SC',serif;font-weight:700;font-size:24px;color:#5E470F;z-index:2}
.side{position:absolute;top:168px;width:150px;text-align:center}
.side b{display:block;font-family:'Cormorant Garamond',serif;font-size:40px;line-height:1;color:var(--ink)}
.side i{display:block;font-style:normal;font-size:14.5px;color:var(--taupe);margin-top:7px;line-height:1.3}
.side.yes{left:6px}
.side.yes b{color:var(--green)}
.side.no{right:6px}
.side.no b{color:var(--brick)}
.cap{position:absolute;left:14px;right:14px;bottom:64px;text-align:center;font-size:15.5px;color:var(--ink-2);line-height:1.35}
.cap b{color:var(--ink)}
.brand{position:absolute;left:72px;bottom:28px;display:flex;align-items:center;gap:11px;color:var(--ink)}
.brand b{font-family:'Cormorant Garamond',serif;font-weight:700;font-size:26px}
.brand .bdot{width:10px;height:10px;border-radius:50%%;background:var(--brick)}
.brand span{color:var(--taupe);font-size:16px}
</style></head><body>
<div class="card">
  <div class="txt">
    <div class="eyebrow">Решение</div>
    <h1>Стоит ли учить <i>китайский язык</i></h1>
    <div class="sub">Вопрос задают про язык, а отвечать на него приходится про себя: про свою задачу, срок и запас времени</div>
    <div class="note"><b>У этого вопроса есть ответ «нет»</b> — и честнее услышать его до оплаты курса, а не через полгода</div>
  </div>
  <div class="scene">
    <div class="table-line"></div>
    <div class="shadow"></div>
    <div class="side yes"><b>Да</b><i>если задача совпала</i></div>
    <div class="coin"><span>汉</span></div>
    <div class="side no"><b>Нет</b><i>если задача другая</i></div>
    <div class="cap">Монета ещё не упала: <b>решение зависит от того, зачем вам язык</b></div>
  </div>
  <div class="brand"><span class="bdot"></span><b>Kitai School</b><span>&middot; kitai-school.ru</span></div>
</div>
</body></html>""" % (FONTS, VARS)

open(S + "st-hero.html", "w", encoding="utf-8").write(hero)

# -------------------------------------------------------------- инфографика
YES = [
    "Работать с китайскими поставщиками и партнёрами без посредника",
    "Учиться в китайском вузе и жить в стране",
    "Читать, смотреть и слушать то, что не переведено",
    "Понимать собеседника, а не только текст переписки",
    "Вести переговоры, где важны оттенки и вежливость",
]
NO = [
    "Гарантировать работу: язык — условие, а не причина найма",
    "Заменить профессию: китайский без специальности мало что даёт",
    "Окупиться быстро: первые месяцы отдачи не приносят",
    "Пригодиться в разовой поездке: там хватит переводчика в телефоне",
    "Сделать переписку мгновенной: машинный перевод её уже закрывает",
]

ylist = "\n".join('<li><i class="ok">✓</i><span>%s</span></li>' % t for t in YES)
nlist = "\n".join('<li><i class="no">✕</i><span>%s</span></li>' % t for t in NO)

info = """<!DOCTYPE html><html lang="ru"><head><meta charset="utf-8">
%s
<style>
%s
*{margin:0;box-sizing:border-box}html,body{width:1200px;height:HGTpx}
.wrap{width:1200px;height:HGTpx;background:linear-gradient(180deg,#fff 0%%,var(--cream) 46%%,var(--cream-2) 100%%);font-family:'Inter',sans-serif;padding:32px 46px 26px;display:flex;flex-direction:column}
.top{display:flex;align-items:flex-end;justify-content:space-between;gap:30px;margin-bottom:22px}
.eyebrow{color:var(--brick);font-weight:700;font-size:14.5px;letter-spacing:.17em;text-transform:uppercase;margin-bottom:7px}
h2{font-family:'Cormorant Garamond',serif;font-weight:600;font-size:40px;line-height:1.07;color:var(--ink);letter-spacing:-.3px}
h2 i{font-style:italic;color:var(--brick)}
.hint{flex:0 0 358px;background:var(--surface);border:1px solid var(--hair);border-left:4px solid var(--brick);border-radius:12px;padding:12px 17px;font-size:14.5px;color:var(--ink-2);line-height:1.36}
.hint b{color:var(--ink)}

.cols{display:flex;gap:22px;align-items:stretch}
.col{flex:1 1 0;background:var(--surface);border:1px solid var(--hair);border-radius:14px;padding:18px 22px 16px;box-shadow:0 5px 14px rgba(44,36,32,.05)}
.col.a{border-top:5px solid var(--green)}
.col.b{border-top:5px solid var(--brick)}
.ch{font-size:17px;font-weight:700;color:var(--ink);margin-bottom:14px;display:flex;align-items:center;gap:9px}
.ch em{font-style:normal;font-size:13px;font-weight:600;letter-spacing:.06em;text-transform:uppercase;padding:3px 9px;border-radius:7px}
.col.a .ch em{background:var(--green-s);color:var(--green)}
.col.b .ch em{background:var(--brick-soft);color:var(--brick)}
ul{list-style:none;display:flex;flex-direction:column;gap:11px}
li{display:flex;align-items:flex-start;gap:11px;font-size:15px;color:var(--ink-2);line-height:1.36}
li i{flex:0 0 22px;height:22px;border-radius:50%%;display:flex;align-items:center;justify-content:center;font-style:normal;font-size:13px;font-weight:700;margin-top:1px}
li .ok{background:var(--green-s);color:var(--green)}
li .no{background:var(--brick-soft);color:var(--brick)}

.foot{margin-top:auto;display:flex;align-items:center;gap:18px;padding-top:18px}
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
      <div class="eyebrow">До решения</div>
      <h2>Что язык решает — <i>и чего не решает</i></h2>
    </div>
    <div class="hint">Смотреть нужно не на правую колонку, а на левую: <b>есть ли там ваша задача</b>. Если нет — ответ, скорее всего, «не сейчас».</div>
  </div>

  <div class="cols">
    <div class="col a">
      <div class="ch"><em>Решает</em></div>
      <ul>
%s
      </ul>
    </div>
    <div class="col b">
      <div class="ch"><em>Не решает</em></div>
      <ul>
%s
      </ul>
    </div>
  </div>

  <div class="foot">
    <div class="msg">Главный признак хорошего решения: <b>вы можете назвать задачу, под которую берёте язык</b>, и она стоит в левой колонке</div>
    <div class="brand"><span class="dot2"></span><b>Kitai School</b><span>&middot; kitai-school.ru</span></div>
  </div>
</div>
</body></html>""" % (FONTS, VARS, ylist, nlist)

info = info.replace("HGT", "560")
open(S + "st-info.html", "w", encoding="utf-8").write(info)
print("ok")
