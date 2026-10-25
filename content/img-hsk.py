# -*- coding: utf-8 -*-
# Картинки к статье «Сдать HSK: день экзамена»
# Обложка    — песочные часы и три части экзамена
# Инфографика — планшет с зажимом: чек-лист дня в три столбца
S = "/tmp/claude-0/-home-user-Kitai-Shool/a463bfca-82a9-56fd-ae09-42a7257ff999/scratchpad/"

FONTS = ("<link href=\"https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,600;0,700;1,600"
         "&family=Inter:wght@400;500;600;700&family=Noto+Serif+SC:wght@600;700&display=swap\" rel=\"stylesheet\">")
VARS = (":root{--brick:#A41E3A;--brick-d:#841630;--brick-soft:#F7E6EB;--ink:#2C2420;--ink-2:#5A4F45;"
        "--taupe:#8B7D6B;--cream:#FAF7F2;--cream-2:#F3EDE3;--hair:#EAE3D8;--surface:#fff;"
        "--sand:#D9A441;--sand-2:#C08A2E;--glass:#F4F1EA;--wood:#8B6F4E;--wood-2:#6E5539;"
        "--clip:#9AA3AD;--board:#C8B99D;--green:#1E7A46}")

PARTS = [("听力", "Аудирование", "звучит один раз"),
         ("阅读", "Чтение", "здесь кончается время"),
         ("书写", "Письмо", "бланк заполняют заранее")]

parts = "\n".join(
    '<div class="part"><span class="han">%s</span><span class="nm">%s</span>'
    '<span class="note">%s</span></div>' % p for p in PARTS)

hero = """<!DOCTYPE html><html lang="ru"><head><meta charset="utf-8">
%s
<style>
%s
*{margin:0;box-sizing:border-box}html,body{width:1200px;height:630px}
.card{width:1200px;height:630px;background:radial-gradient(1050px 660px at 14%% 12%%, #fff 0%%, var(--cream) 52%%, var(--cream-2) 100%%);position:relative;overflow:hidden;font-family:'Inter',sans-serif;padding:52px 46px 0 72px;display:flex;justify-content:space-between}
.card:before{content:"";position:absolute;left:0;top:0;bottom:0;width:12px;background:var(--brick)}
.txt{flex:0 0 500px;padding-top:4px}
.eyebrow{color:var(--brick);font-weight:700;font-size:18px;letter-spacing:.19em;text-transform:uppercase;margin-bottom:13px}
h1{font-family:'Cormorant Garamond',serif;font-weight:600;font-size:45px;line-height:1.07;color:var(--ink);letter-spacing:-.4px}
h1 i{font-style:italic;color:var(--brick)}
.sub{font-size:18px;color:var(--ink-2);line-height:1.42;max-width:31ch;margin-top:16px}
.note2{display:inline-block;margin-top:22px;background:var(--surface);border:1px solid var(--hair);border-left:4px solid var(--brick);border-radius:13px;padding:13px 19px;font-size:15.5px;color:var(--ink-2);line-height:1.36;max-width:34ch}
.note2 b{color:var(--ink)}

/* песочные часы */
.scene{flex:0 0 500px;position:relative;padding-top:52px;display:flex;align-items:flex-start;gap:34px}
.glasswrap{flex:0 0 190px;display:flex;flex-direction:column;align-items:center}
.cap{width:160px;height:16px;border-radius:5px;background:linear-gradient(180deg,var(--wood),var(--wood-2));box-shadow:0 3px 7px rgba(44,36,32,.25)}
.bulbs{position:relative;width:150px;height:252px}
.bulb{position:absolute;left:0;width:150px;height:124px;background:var(--glass);border:2px solid #E2DACB;overflow:hidden}
.bulb.top{top:0;border-radius:10px 10px 50%% 50%%}
.bulb.bot{bottom:0;border-radius:50%% 50%% 10px 10px}
.bulb .s{position:absolute;left:0;right:0;background:linear-gradient(180deg,var(--sand),var(--sand-2))}
.bulb.top .s{top:0;height:54px;border-radius:8px 8px 46%% 46%%}
.bulb.bot .s{bottom:0;height:66px;border-radius:46%% 46%% 8px 8px}
.neck{position:absolute;left:50%%;top:50%%;transform:translate(-50%%,-50%%);width:16px;height:14px;background:var(--glass);border-left:2px solid #E2DACB;border-right:2px solid #E2DACB;z-index:2}
.stream{position:absolute;left:50%%;top:122px;transform:translateX(-50%%);width:4px;height:36px;background:var(--sand);z-index:3;border-radius:2px}
.parts{flex:1 1 auto;display:flex;flex-direction:column;gap:14px;padding-top:16px}
.part{background:var(--surface);border:1px solid var(--hair);border-radius:13px;padding:12px 17px;box-shadow:0 4px 11px rgba(44,36,32,.05)}
.part .han{font-family:'Noto Serif SC',serif;font-size:25px;color:var(--ink);margin-right:10px}
.part .nm{font-size:16.5px;font-weight:600;color:var(--ink)}
.part .note{display:block;font-size:14px;color:var(--ink-2);margin-top:3px}
.brand{position:absolute;left:72px;bottom:28px;display:flex;align-items:center;gap:11px;color:var(--ink)}
.brand b{font-family:'Cormorant Garamond',serif;font-weight:700;font-size:26px}
.brand .bdot{width:10px;height:10px;border-radius:50%%;background:var(--brick)}
.brand span{color:var(--taupe);font-size:16px}
</style></head><body>
<div class="card">
  <div class="txt">
    <div class="eyebrow">Экзамен</div>
    <h1>Сдать HSK: <i>день экзамена</i></h1>
    <div class="sub">Три части подряд, и время у каждой своё</div>
    <div class="note2"><b>Баллы теряют на формате, а не на языке:</b> не дошёл до конца — задания остались неотвеченными</div>
  </div>
  <div class="scene">
    <div class="glasswrap">
      <div class="cap"></div>
      <div class="bulbs">
        <div class="bulb top"><span class="s"></span></div>
        <div class="stream"></div>
        <div class="neck"></div>
        <div class="bulb bot"><span class="s"></span></div>
      </div>
      <div class="cap"></div>
    </div>
    <div class="parts">
%s
    </div>
  </div>
  <div class="brand"><span class="bdot"></span><b>Kitai School</b><span>&middot; kitai-school.ru</span></div>
</div>
</body></html>""" % (FONTS, VARS, parts)

open(S + "hsk-hero.html", "w", encoding="utf-8").write(hero)

# -------------------------------------------------------------- инфографика
COLS = [
    ("До входа", ["Документ — тот же, что при регистрации",
                  "Телефон и умные часы — в сумку на хранение",
                  "Свои черновики и словари оставить дома",
                  "Найти свою аудиторию по спискам"]),
    ("В аудитории", ["Место по номеру, бланк заполняют до старта",
                     "Аудирование звучит один раз",
                     "Непонятное задание — пропустить и отметить",
                     "На бумажном формате ответы переносить по ходу"]),
    ("После", ["Бланк и задания остаются в аудитории",
               "Результат сначала в личном кабинете",
               "Бумажный сертификат идёт дольше",
               "Сроки уточняют в своём центре"]),
]

cols = "\n".join(
    '<div class="col"><div class="ch">%s</div>%s</div>'
    % (title, "".join('<div class="it"><span class="bx"></span><span>%s</span></div>' % i
                      for i in items))
    for title, items in COLS)

info = """<!DOCTYPE html><html lang="ru"><head><meta charset="utf-8">
%s
<style>
%s
*{margin:0;box-sizing:border-box}html,body{width:1200px;height:HGTpx}
.wrap{width:1200px;height:HGTpx;background:linear-gradient(180deg,#fff 0%%,var(--cream) 46%%,var(--cream-2) 100%%);font-family:'Inter',sans-serif;padding:32px 46px 30px;display:flex;flex-direction:column}
.top{display:flex;align-items:flex-end;justify-content:space-between;gap:30px;margin-bottom:20px}
.eyebrow{color:var(--brick);font-weight:700;font-size:14.5px;letter-spacing:.17em;text-transform:uppercase;margin-bottom:7px}
h2{font-family:'Cormorant Garamond',serif;font-weight:600;font-size:40px;line-height:1.07;color:var(--ink);letter-spacing:-.3px}
h2 i{font-style:italic;color:var(--brick)}
.hint{flex:0 0 360px;background:var(--surface);border:1px solid var(--hair);border-left:4px solid var(--brick);border-radius:12px;padding:12px 17px;font-size:14.5px;color:var(--ink-2);line-height:1.36}
.hint b{color:var(--ink)}

/* планшет с зажимом */
.board{position:relative;background:linear-gradient(180deg,#D7C9AC,var(--board));border-radius:14px;padding:40px 22px 22px;box-shadow:0 10px 24px rgba(44,36,32,.16)}
.clip{position:absolute;left:50%%;top:-14px;transform:translateX(-50%%);width:150px;height:34px;border-radius:7px;background:linear-gradient(180deg,#C2C9D1,var(--clip));box-shadow:0 4px 9px rgba(44,36,32,.22)}
.clip:after{content:"";position:absolute;left:50%%;top:9px;transform:translateX(-50%%);width:58px;height:13px;border-radius:4px;background:rgba(255,255,255,.45)}
.sheet{background:var(--surface);border-radius:10px;padding:18px 18px 16px;display:flex;gap:16px}
.col{flex:1 1 0}
.ch{font-size:16px;font-weight:700;color:var(--brick-d);border-bottom:2px solid var(--brick-soft);padding-bottom:7px;margin-bottom:11px}
.it{display:flex;gap:10px;align-items:flex-start;margin-bottom:10px;font-size:14.5px;color:var(--ink-2);line-height:1.33}
.bx{flex:0 0 16px;height:16px;border:2px solid var(--green);border-radius:4px;margin-top:2px;position:relative}
.bx:after{content:"";position:absolute;left:3px;top:0px;width:6px;height:10px;border:solid var(--green);border-width:0 2px 2px 0;transform:rotate(42deg)}

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
      <div class="eyebrow">День экзамена</div>
      <h2>Чек-лист <i>на три части дня</i></h2>
    </div>
    <div class="hint">Порядок в аудитории задаёт центр, <b>детали уточняйте у своего</b>. Общая схема везде одна.</div>
  </div>

  <div class="board">
    <div class="clip"></div>
    <div class="sheet">
%s
    </div>
  </div>

  <div class="foot">
    <div class="msg">Главное правило дня: <b>дойти до конца каждой части</b>, а не разобрать одно задание до дна</div>
    <div class="brand"><span class="dot2"></span><b>Kitai School</b><span>&middot; kitai-school.ru</span></div>
  </div>
</div>
</body></html>""" % (FONTS, VARS, cols)

info = info.replace("HGT", "500")
open(S + "hsk-info.html", "w", encoding="utf-8").write(info)
print("ok")
