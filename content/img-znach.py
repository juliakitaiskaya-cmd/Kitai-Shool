# -*- coding: utf-8 -*-
# Картинки к статье «Что означают китайские иероглифы»
# Обложка    — рукописный ввод на экране: так сегодня узнают значение знака
# Инфографика — один знак в трёх контекстах
S = "/tmp/claude-0/-home-user-Kitai-Shool/a463bfca-82a9-56fd-ae09-42a7257ff999/scratchpad/"

FONTS = ("<link href=\"https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,600;0,700;1,600"
         "&family=Inter:wght@400;500;600;700&family=Noto+Serif+SC:wght@600;700&display=swap\" rel=\"stylesheet\">")
VARS = (":root{--brick:#A41E3A;--brick-d:#841630;--brick-soft:#F7E6EB;--ink:#2C2420;--ink-2:#5A4F45;"
        "--taupe:#8B7D6B;--cream:#FAF7F2;--cream-2:#F3EDE3;--hair:#EAE3D8;--surface:#fff;"
        "--green:#1E7A46;--green-s:#E3F6E9;--amber:#C08A2E;--amber-s:#FBF2DF;--blue:#2F5D8C;--blue-s:#E7EEF6;"
        "--screen:#F7F4EE;--frame:#2E2A26;--frame-2:#1E1B18;--grid:#E2D9C9}")

HINTS = ["生", "牛", "主", "丰"]
hint_html = "\n".join('<div class="hint %s">%s</div>' % ("on" if h == "生" else "", h)
                      for h in HINTS)

hero = """<!DOCTYPE html><html lang="ru"><head><meta charset="utf-8">
%s
<style>
%s
*{margin:0;box-sizing:border-box}html,body{width:1200px;height:630px}
.card{width:1200px;height:630px;background:radial-gradient(1050px 660px at 14%% 12%%, #fff 0%%, var(--cream) 52%%, var(--cream-2) 100%%);position:relative;overflow:hidden;font-family:'Inter',sans-serif;padding:52px 46px 0 72px;display:flex;justify-content:space-between}
.card:before{content:"";position:absolute;left:0;top:0;bottom:0;width:12px;background:var(--brick)}
.txt{flex:0 0 520px;padding-top:4px}
.eyebrow{color:var(--brick);font-weight:700;font-size:18px;letter-spacing:.19em;text-transform:uppercase;margin-bottom:13px}
h1{font-family:'Cormorant Garamond',serif;font-weight:600;font-size:45px;line-height:1.07;color:var(--ink);letter-spacing:-.4px}
h1 i{font-style:italic;color:var(--brick)}
.sub{font-size:18px;color:var(--ink-2);line-height:1.42;max-width:32ch;margin-top:16px}
.note{display:inline-block;margin-top:22px;background:var(--surface);border:1px solid var(--hair);border-left:4px solid var(--brick);border-radius:13px;padding:13px 19px;font-size:15.5px;color:var(--ink-2);line-height:1.36;max-width:34ch}
.note b{color:var(--ink)}

/* экран с рукописным вводом */
.scene{flex:0 0 500px;position:relative;height:482px;display:flex;flex-direction:column;align-items:center;padding-top:26px}
.phone{width:306px;height:418px;border-radius:30px;background:linear-gradient(170deg,var(--frame),var(--frame-2));padding:14px;box-shadow:0 18px 36px rgba(44,36,32,.3)}
.screen{width:100%%;height:100%%;border-radius:20px;background:var(--screen);display:flex;flex-direction:column;padding:16px 14px;gap:12px}
.hints{display:flex;gap:8px}
.hint{flex:1 1 0;height:48px;border-radius:9px;background:#fff;border:1px solid var(--hair);display:flex;align-items:center;justify-content:center;font-family:'Noto Serif SC',serif;font-size:25px;color:var(--ink-2)}
.hint.on{background:var(--brick-soft);border-color:var(--brick);color:var(--brick)}
.pad{flex:1 1 auto;border-radius:12px;background:#fff;border:1px dashed var(--grid);position:relative;display:flex;align-items:center;justify-content:center}
.pad:before{content:"";position:absolute;left:12px;right:12px;top:50%%;border-top:1px dashed var(--grid)}
.pad:after{content:"";position:absolute;top:12px;bottom:12px;left:50%%;border-left:1px dashed var(--grid)}
.pad .draw{font-family:'Noto Serif SC',serif;font-size:132px;color:var(--ink);position:relative;z-index:2;line-height:1}
.panel{height:42px;border-radius:9px;background:#fff;border:1px solid var(--hair);display:flex;align-items:center;justify-content:space-between;padding:0 14px;font-size:13.5px;color:var(--taupe)}
.panel b{color:var(--brick);font-weight:600}
.cap{margin-top:22px;text-align:center;font-size:16px;color:var(--ink-2);line-height:1.4;max-width:40ch}
.cap b{color:var(--ink)}
.brand{position:absolute;left:72px;bottom:28px;display:flex;align-items:center;gap:11px;color:var(--ink)}
.brand b{font-family:'Cormorant Garamond',serif;font-weight:700;font-size:26px}
.brand .bdot{width:10px;height:10px;border-radius:50%%;background:var(--brick)}
.brand span{color:var(--taupe);font-size:16px}
</style></head><body>
<div class="card">
  <div class="txt">
    <div class="eyebrow">Иероглифы</div>
    <h1>Что означают <i>китайские иероглифы</i></h1>
    <div class="sub">У вопроса о значении знака редко бывает один ответ: выбирает контекст</div>
    <div class="note"><b>Незнакомый знак сегодня ищут пальцем:</b> рисуют на экране и смотрят, что предложит словарь</div>
  </div>
  <div class="scene">
    <div class="phone">
      <div class="screen">
        <div class="hints">
%s
        </div>
        <div class="pad"><span class="draw">生</span></div>
        <div class="panel"><span>рукописный ввод</span><b>生 shēng</b></div>
      </div>
    </div>
    <div class="cap">Словарь покажет <b>список значений</b>, а не одно</div>
  </div>
  <div class="brand"><span class="bdot"></span><b>Kitai School</b><span>&middot; kitai-school.ru</span></div>
</div>
</body></html>""" % (FONTS, VARS, hint_html)

open(S + "zn-hero.html", "w", encoding="utf-8").write(hero)

# -------------------------------------------------------------- инфографика
ROWS = [
    ("生日", "shēngrì", "生", "день рождения", "здесь 生 — «рождаться»"),
    ("学生", "xuéshēng", "生", "ученик, студент", "здесь 生 — «учащийся»"),
    ("生肉", "shēngròu", "生", "сырое мясо", "здесь 生 — «сырой, необработанный»"),
    ("陌生", "mòshēng", "生", "незнакомый", "здесь 生 — «чужой, непривычный»"),
]


def word_html(word, hl):
    return "".join(
        '<span class="%s">%s</span>' % ("hl" if ch == hl else "", ch) for ch in word)


rows = "\n".join(
    '<div class="row"><div class="w">%s</div><div class="p">%s</div>'
    '<div class="ru">%s</div><div class="note">%s</div></div>'
    % (word_html(w, h), p, ru, note) for w, p, h, ru, note in ROWS)

info = """<!DOCTYPE html><html lang="ru"><head><meta charset="utf-8">
%s
<style>
%s
*{margin:0;box-sizing:border-box}html,body{width:1200px;height:HGTpx}
.wrap{width:1200px;height:HGTpx;background:linear-gradient(180deg,#fff 0%%,var(--cream) 46%%,var(--cream-2) 100%%);font-family:'Inter',sans-serif;padding:32px 46px 32px;display:flex;flex-direction:column}
.top{display:flex;align-items:flex-end;justify-content:space-between;gap:30px;margin-bottom:20px}
.eyebrow{color:var(--brick);font-weight:700;font-size:14.5px;letter-spacing:.17em;text-transform:uppercase;margin-bottom:7px}
h2{font-family:'Cormorant Garamond',serif;font-weight:600;font-size:40px;line-height:1.07;color:var(--ink);letter-spacing:-.3px}
h2 i{font-style:italic;color:var(--brick)}
.hint{flex:0 0 390px;background:var(--surface);border:1px solid var(--hair);border-left:4px solid var(--brick);border-radius:12px;padding:12px 17px;font-size:14.5px;color:var(--ink-2);line-height:1.36}
.hint b{color:var(--ink)}

.rows{display:flex;flex-direction:column;gap:13px}
.row{display:flex;align-items:center;gap:22px;background:var(--surface);border:1px solid var(--hair);border-radius:14px;padding:14px 22px;box-shadow:0 4px 12px rgba(44,36,32,.05)}
.row .w{flex:0 0 150px;font-family:'Noto Serif SC',serif;font-size:40px;color:var(--ink);line-height:1.1;letter-spacing:2px}
.row .w .hl{color:var(--brick)}
.row .p{flex:0 0 136px;font-size:16px;color:var(--taupe);font-style:italic}
.row .ru{flex:0 0 212px;font-size:17px;font-weight:600;color:var(--ink)}
.row .note{flex:1 1 auto;font-size:15px;color:var(--ink-2)}

.foot{margin-top:auto;display:flex;align-items:center;gap:18px;padding-top:20px}
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
      <div class="eyebrow">Один знак, четыре слова</div>
      <h2>Что значит <i>生</i></h2>
    </div>
    <div class="hint">Значение знака <b>выбирает соседнее слово</b>, а не словарь: в отрыве от контекста у 生 нет одного перевода.</div>
  </div>

  <div class="rows">
%s
  </div>

  <div class="foot">
    <div class="msg">Поэтому вопрос <b>«что значит этот знак»</b> почти всегда требует второго вопроса: а где вы его встретили</div>
    <div class="brand"><span class="dot2"></span><b>Kitai School</b><span>&middot; kitai-school.ru</span></div>
  </div>
</div>
</body></html>""" % (FONTS, VARS, rows)

info = info.replace("HGT", "548")
open(S + "zn-info.html", "w", encoding="utf-8").write(info)
print("ok")
