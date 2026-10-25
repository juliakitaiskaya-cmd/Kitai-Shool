# -*- coding: utf-8 -*-
# Картинки к статье «Китайские слова для начинающих»
# Обложка    — стикеры-заметки: наклейки внахлёст с иероглифами и пиньинем
# Инфографика — органайзер с кармашками: семь групп слов и итог 70
S = "/tmp/claude-0/-home-user-Kitai-Shool/a463bfca-82a9-56fd-ae09-42a7257ff999/scratchpad/"

FONTS = ("<link href=\"https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,600;0,700;1,600"
         "&family=Inter:wght@400;500;600;700&family=Noto+Serif+SC:wght@600;700&display=swap\" rel=\"stylesheet\">")
VARS = (":root{--brick:#A41E3A;--brick-d:#841630;--brick-soft:#F7E6EB;--ink:#2C2420;--ink-2:#5A4F45;"
        "--taupe:#8B7D6B;--cream:#FAF7F2;--cream-2:#F3EDE3;--hair:#EAE3D8;--surface:#fff;"
        "--n1:#FBE7A8;--n2:#CFE6D6;--n3:#F7D4D9;--n4:#D7E2F2;--pocket:#E7DCC8;--pocket-2:#DACDB4}")

NOTES = [
    ("你好", "nǐ hǎo", "здравствуйте", "n1", "-5deg", "16px", "8px"),
    ("谢谢", "xièxie", "спасибо", "n2", "4deg", "262px", "34px"),
    ("我", "wǒ", "я", "n3", "-3deg", "40px", "232px"),
    ("要", "yào", "хотеть, нужно", "n4", "6deg", "286px", "252px"),
]

notes = "\n".join(
    '<div class="note %s" style="transform:rotate(%s);left:%s;top:%s">'
    '<span class="han">%s</span><span class="py">%s</span><span class="ru">%s</span></div>'
    % (cls, rot, left, top, han, py, ru) for han, py, ru, cls, rot, left, top in NOTES)

hero = """<!DOCTYPE html><html lang="ru"><head><meta charset="utf-8">
%s
<style>
%s
*{margin:0;box-sizing:border-box}html,body{width:1200px;height:630px}
.card{width:1200px;height:630px;background:radial-gradient(1050px 660px at 14%% 12%%, #fff 0%%, var(--cream) 52%%, var(--cream-2) 100%%);position:relative;overflow:hidden;font-family:'Inter',sans-serif;padding:52px 46px 0 72px;display:flex;justify-content:space-between}
.card:before{content:"";position:absolute;left:0;top:0;bottom:0;width:12px;background:var(--brick)}
.txt{flex:0 0 486px;padding-top:4px}
.eyebrow{color:var(--brick);font-weight:700;font-size:18px;letter-spacing:.19em;text-transform:uppercase;margin-bottom:13px}
h1{font-family:'Cormorant Garamond',serif;font-weight:600;font-size:44px;line-height:1.08;color:var(--ink);letter-spacing:-.4px}
h1 i{font-style:italic;color:var(--brick)}
.sub{font-size:18px;color:var(--ink-2);line-height:1.42;max-width:31ch;margin-top:16px}
.tip{display:inline-block;margin-top:22px;background:var(--surface);border:1px solid var(--hair);border-left:4px solid var(--brick);border-radius:13px;padding:13px 19px;font-size:15.5px;color:var(--ink-2);line-height:1.36;max-width:33ch}
.tip b{color:var(--ink)}

/* стикеры */
.scene{flex:0 0 520px;position:relative;height:470px}
.note{position:absolute;width:196px;height:196px;border-radius:3px;padding:22px 18px;display:flex;flex-direction:column;justify-content:center;gap:6px;box-shadow:0 12px 22px rgba(44,36,32,.18)}
.note:after{content:"";position:absolute;left:50%%;top:-9px;transform:translateX(-50%%) rotate(-2deg);width:74px;height:20px;background:rgba(255,255,255,.55);border:1px solid rgba(44,36,32,.07)}
.note.n1{background:var(--n1)}.note.n2{background:var(--n2)}
.note.n3{background:var(--n3)}.note.n4{background:var(--n4)}
.note .han{font-family:'Noto Serif SC',serif;font-size:44px;color:var(--ink);line-height:1.06}
.note .py{font-size:17px;color:var(--ink-2);font-style:italic}
.note .ru{font-size:15px;color:var(--ink-2)}
.brand{position:absolute;left:72px;bottom:28px;display:flex;align-items:center;gap:11px;color:var(--ink)}
.brand b{font-family:'Cormorant Garamond',serif;font-weight:700;font-size:26px}
.brand .bdot{width:10px;height:10px;border-radius:50%%;background:var(--brick)}
.brand span{color:var(--taupe);font-size:16px}
</style></head><body>
<div class="card">
  <div class="txt">
    <div class="eyebrow">Словарь</div>
    <h1>Китайские слова <i>для начинающих</i></h1>
    <div class="sub">Семьдесят слов первого месяца — с иероглифом, пиньинем и переводом</div>
    <div class="tip"><b>Тон — часть слова:</b> выучили без него — выучили не слово, а его половину</div>
  </div>
  <div class="scene">
%s
  </div>
  <div class="brand"><span class="bdot"></span><b>Kitai School</b><span>&middot; kitai-school.ru</span></div>
</div>
</body></html>""" % (FONTS, VARS, notes)

open(S + "sl-hero.html", "w", encoding="utf-8").write(hero)

# -------------------------------------------------------------- инфографика
POCKETS = [
    ("Вежливость", "10", "你好 · 谢谢 · 请问"),
    ("Слова-опоры", "14", "是 · 有 · 不 · 很"),
    ("Местоимения", "6", "我 · 你 · 这个"),
    ("Вопросы", "6", "什么 · 谁 · 多少"),
    ("Люди и вещи", "12", "朋友 · 钱 · 手机"),
    ("Места и время", "12", "学校 · 今天 · 现在"),
    ("Глаголы", "10", "去 · 吃 · 买 · 学"),
]

pockets = "\n".join(
    '<div class="pk"><div class="num">%s</div><div class="nm">%s</div><div class="ex han">%s</div></div>'
    % (num, name, ex) for name, num, ex in POCKETS)

info = """<!DOCTYPE html><html lang="ru"><head><meta charset="utf-8">
%s
<style>
%s
*{margin:0;box-sizing:border-box}html,body{width:1200px;height:HGTpx}
.wrap{width:1200px;height:HGTpx;background:linear-gradient(180deg,#fff 0%%,var(--cream) 46%%,var(--cream-2) 100%%);font-family:'Inter',sans-serif;padding:32px 46px 30px;display:flex;flex-direction:column}
.top{display:flex;align-items:flex-end;justify-content:space-between;gap:30px;margin-bottom:24px}
.eyebrow{color:var(--brick);font-weight:700;font-size:14.5px;letter-spacing:.17em;text-transform:uppercase;margin-bottom:7px}
h2{font-family:'Cormorant Garamond',serif;font-weight:600;font-size:40px;line-height:1.07;color:var(--ink);letter-spacing:-.3px}
h2 i{font-style:italic;color:var(--brick)}
.hint{flex:0 0 372px;background:var(--surface);border:1px solid var(--hair);border-left:4px solid var(--brick);border-radius:12px;padding:12px 17px;font-size:14.5px;color:var(--ink-2);line-height:1.36}
.hint b{color:var(--ink)}

.rack{display:flex;gap:13px;align-items:flex-end}
.pk{flex:1 1 0;height:196px;border-radius:12px 12px 16px 16px;background:linear-gradient(180deg,#fff 0%%,#fff 34%%,var(--pocket) 34%%,var(--pocket-2) 100%%);border:1px solid var(--hair);box-shadow:0 7px 16px rgba(44,36,32,.09);display:flex;flex-direction:column;align-items:center;padding:16px 10px 14px;position:relative}
.pk:after{content:"";position:absolute;left:10px;right:10px;top:34%%;height:7px;border-radius:4px;background:rgba(44,36,32,.09)}
.pk .num{font-family:'Cormorant Garamond',serif;font-weight:700;font-size:40px;color:var(--brick);line-height:1}
.pk .nm{margin-top:4px;font-size:14.5px;font-weight:600;color:var(--ink);text-align:center;line-height:1.22}
.pk .ex{margin-top:16px;font-family:'Noto Serif SC',serif;font-size:15px;color:var(--ink-2);text-align:center;line-height:1.5}

.total{margin-top:20px;display:flex;align-items:center;gap:18px;background:var(--surface);border:1px solid var(--hair);border-radius:15px;padding:15px 24px;box-shadow:0 5px 14px rgba(44,36,32,.05)}
.total .big{font-family:'Cormorant Garamond',serif;font-weight:700;font-size:46px;color:var(--brick);line-height:1}
.total .t{font-size:15.5px;color:var(--ink-2);line-height:1.34}
.total .t b{color:var(--ink)}

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
      <div class="eyebrow">Первый месяц</div>
      <h2>Семь групп, <i>из которых собирается фраза</i></h2>
    </div>
    <div class="hint">Сначала берут <b>не красивые слова, а те, что держат предложение</b>: связки, вопросы, десяток глаголов.</div>
  </div>

  <div class="rack">
%s
  </div>

  <div class="total">
    <span class="big">70</span>
    <span class="t"><b>слов на месяц</b> — примерно по три в день, и это каркас, а не разговорник: темы по интересам добираются потом</span>
  </div>

  <div class="foot">
    <div class="msg">Каждое слово учится <b>вместе с тоном</b> — иначе его придётся учить заново</div>
    <div class="brand"><span class="dot2"></span><b>Kitai School</b><span>&middot; kitai-school.ru</span></div>
  </div>
</div>
</body></html>""" % (FONTS, VARS, pockets)

info = info.replace("HGT", "540")
open(S + "sl-info.html", "w", encoding="utf-8").write(info)
print("ok, сумма по кармашкам:", sum(int(n) for _, n, _ in POCKETS))
