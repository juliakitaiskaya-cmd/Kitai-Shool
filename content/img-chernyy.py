# -*- coding: utf-8 -*-
# Картинки к статье «Чёрный на китайском»
# Обложка    — брусок туши: чёрный как цвет копоти и туши
# Инфографика — пятно с тремя потёками: три группы значений
S = "/tmp/claude-0/-home-user-Kitai-Shool/a463bfca-82a9-56fd-ae09-42a7257ff999/scratchpad/"

FONTS = ("<link href=\"https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,600;0,700;1,600"
         "&family=Inter:wght@400;500;600;700&family=Noto+Serif+SC:wght@600;700&display=swap\" rel=\"stylesheet\">")
VARS = (":root{--brick:#A41E3A;--brick-d:#841630;--brick-soft:#F7E6EB;--ink:#2C2420;--ink-2:#5A4F45;"
        "--taupe:#8B7D6B;--cream:#FAF7F2;--cream-2:#F3EDE3;--hair:#EAE3D8;--surface:#fff;"
        "--green:#1E7A46;--green-s:#E3F6E9;--amber:#C08A2E;--amber-s:#FBF2DF;--blue:#2F5D8C;--blue-s:#E7EEF6;"
        "--ink-stick:#2A2724;--ink-stick-2:#15130F;--gold:#C9A961}")

hero = """<!DOCTYPE html><html lang="ru"><head><meta charset="utf-8">
%s
<style>
%s
*{margin:0;box-sizing:border-box}html,body{width:1200px;height:630px}
.card{width:1200px;height:630px;background:radial-gradient(1050px 660px at 14%% 12%%, #fff 0%%, var(--cream) 52%%, var(--cream-2) 100%%);position:relative;overflow:hidden;font-family:'Inter',sans-serif;padding:52px 46px 0 72px;display:flex;justify-content:space-between}
.card:before{content:"";position:absolute;left:0;top:0;bottom:0;width:12px;background:var(--brick)}
.txt{flex:0 0 512px;padding-top:4px}
.eyebrow{color:var(--brick);font-weight:700;font-size:18px;letter-spacing:.19em;text-transform:uppercase;margin-bottom:13px}
h1{font-family:'Cormorant Garamond',serif;font-weight:600;font-size:45px;line-height:1.07;color:var(--ink);letter-spacing:-.4px}
h1 i{font-style:italic;color:var(--brick)}
.sub{font-size:18px;color:var(--ink-2);line-height:1.42;max-width:32ch;margin-top:16px}
.note{display:inline-block;margin-top:22px;background:var(--surface);border:1px solid var(--hair);border-left:4px solid var(--brick);border-radius:13px;padding:13px 19px;font-size:15.5px;color:var(--ink-2);line-height:1.36;max-width:34ch}
.note b{color:var(--ink)}

/* брусок туши */
.scene{flex:0 0 500px;position:relative;height:482px;display:flex;flex-direction:column;align-items:center;justify-content:flex-start;padding-top:72px}
.stick{width:214px;height:300px;border-radius:12px;background:linear-gradient(152deg,#3A3732,var(--ink-stick) 36%%,var(--ink-stick-2));box-shadow:0 20px 38px rgba(20,18,15,.42), inset 0 1px 0 rgba(255,255,255,.14);display:flex;flex-direction:column;align-items:center;justify-content:center;gap:14px;position:relative;transform:rotate(-3deg)}
.stick:before{content:"";position:absolute;left:14px;right:14px;top:14px;bottom:14px;border:1px solid rgba(201,169,97,.4);border-radius:7px}
.stick .han{font-family:'Noto Serif SC',serif;font-size:104px;color:var(--gold);line-height:1;text-shadow:0 2px 3px rgba(0,0,0,.5)}
.stick .py{font-size:17px;color:#D9CBA6;letter-spacing:.14em}
.tray{width:268px;height:20px;margin-top:-6px;border-radius:0 0 14px 14px;background:linear-gradient(180deg,#C9BCA6,#A9977C);box-shadow:0 10px 18px rgba(44,36,32,.2)}
.cap{margin-top:30px;text-align:center;font-size:16.5px;color:var(--ink-2);line-height:1.42;max-width:36ch}
.cap b{color:var(--ink)}
.brand{position:absolute;left:72px;bottom:28px;display:flex;align-items:center;gap:11px;color:var(--ink)}
.brand b{font-family:'Cormorant Garamond',serif;font-weight:700;font-size:26px}
.brand .bdot{width:10px;height:10px;border-radius:50%%;background:var(--brick)}
.brand span{color:var(--taupe);font-size:16px}
</style></head><body>
<div class="card">
  <div class="txt">
    <div class="eyebrow">Лексика</div>
    <h1>Чёрный <i>на китайском</i></h1>
    <div class="sub">黑 (hēi) — знак, который в словаре «Шовэнь» объяснён как цвет копоти от огня</div>
    <div class="note"><b>В составе слова 黑 часто значит «незаконный»:</b> 黑市 — чёрный рынок, 黑车 — нелегальное такси</div>
  </div>
  <div class="scene">
    <div class="stick"><span class="han">黑</span><span class="py">hēi</span></div>
    <div class="tray"></div>
    <div class="cap">Тушь, копоть, темнота — и дальше <b>всё, что делается скрытно</b></div>
  </div>
  <div class="brand"><span class="bdot"></span><b>Kitai School</b><span>&middot; kitai-school.ru</span></div>
</div>
</body></html>""" % (FONTS, VARS)

open(S + "ch2-hero.html", "w", encoding="utf-8").write(hero)

# -------------------------------------------------------------- инфографика
GROUPS = [
    ("Просто цвет", "#2C2420", [("黑板", "классная доска"), ("黑夜", "тёмная ночь"),
                                ("黑眼睛", "чёрные глаза")]),
    ("Тайное и скрытое", "#4A4036", [("黑暗", "тьма, мрак"), ("黑名单", "чёрный список"),
                                     ("黑客", "хакер")]),
    ("Незаконное", "#8C2E3C", [("黑市", "чёрный рынок"), ("黑车", "нелегальное такси"),
                               ("黑中介", "недобросовестный посредник")]),
]

cards = "\n".join(
    '<div class="grp"><div class="ttl" style="background:%s">%s</div>%s</div>'
    % (color, title, "".join(
        '<div class="w"><span class="han">%s</span><span class="ru">%s</span></div>' % w
        for w in words))
    for title, color, words in GROUPS)

info = """<!DOCTYPE html><html lang="ru"><head><meta charset="utf-8">
%s
<style>
%s
*{margin:0;box-sizing:border-box}html,body{width:1200px;height:HGTpx}
.wrap{width:1200px;height:HGTpx;background:linear-gradient(180deg,#fff 0%%,var(--cream) 46%%,var(--cream-2) 100%%);font-family:'Inter',sans-serif;padding:32px 46px 30px;display:flex;flex-direction:column}
.top{display:flex;align-items:flex-end;justify-content:space-between;gap:30px;margin-bottom:18px}
.eyebrow{color:var(--brick);font-weight:700;font-size:14.5px;letter-spacing:.17em;text-transform:uppercase;margin-bottom:7px}
h2{font-family:'Cormorant Garamond',serif;font-weight:600;font-size:40px;line-height:1.07;color:var(--ink);letter-spacing:-.3px}
h2 i{font-style:italic;color:var(--brick)}
.hint{flex:0 0 378px;background:var(--surface);border:1px solid var(--hair);border-left:4px solid var(--brick);border-radius:12px;padding:12px 17px;font-size:14.5px;color:var(--ink-2);line-height:1.36}
.hint b{color:var(--ink)}

.main{display:flex;align-items:center;gap:26px}
.blot{flex:0 0 190px;height:190px;border-radius:50%% 46%% 52%% 48%%;background:radial-gradient(circle at 38%% 34%%, #3B3630, #15130F);box-shadow:0 14px 28px rgba(20,18,15,.35);display:flex;align-items:center;justify-content:center;position:relative}
.blot:before{content:"";position:absolute;right:-16px;top:40px;width:26px;height:16px;border-radius:50%%;background:#1B1814}
.blot:after{content:"";position:absolute;right:-28px;bottom:48px;width:14px;height:10px;border-radius:50%%;background:#241F1A}
.blot span{font-family:'Noto Serif SC',serif;font-size:84px;color:#F2EADB;line-height:1}
.groups{flex:1 1 auto;display:flex;gap:18px}
.grp{flex:1 1 0;background:var(--surface);border:1px solid var(--hair);border-radius:15px;overflow:hidden;box-shadow:0 5px 14px rgba(44,36,32,.06)}
.grp .ttl{color:#fff;font-size:15px;font-weight:600;padding:11px 16px;letter-spacing:.02em}
.grp .w{display:flex;align-items:baseline;gap:12px;padding:11px 16px;border-bottom:1px solid var(--hair)}
.grp .w:last-child{border-bottom:none}
.grp .w .han{font-family:'Noto Serif SC',serif;font-size:25px;color:var(--ink);flex:0 0 96px;line-height:1.15}
.grp .w .ru{font-size:14.5px;color:var(--ink-2);line-height:1.34}

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
      <div class="eyebrow">Три группы слов</div>
      <h2>Что значит 黑 <i>в разных словах</i></h2>
    </div>
    <div class="hint">Цепочка одна: <b>копоть → чёрный цвет → скрытое → незаконное</b>. Третья группа и делает знак предупреждением.</div>
  </div>

  <div class="main">
    <div class="blot"><span>黑</span></div>
    <div class="groups">
%s
    </div>
  </div>

  <div class="foot">
    <div class="msg">Увидели 黑 в незнакомом слове — <b>проверьте, не о нелегальном ли речь</b></div>
    <div class="brand"><span class="dot2"></span><b>Kitai School</b><span>&middot; kitai-school.ru</span></div>
  </div>
</div>
</body></html>""" % (FONTS, VARS, cards)

info = info.replace("HGT", "432")
open(S + "ch2-info.html", "w", encoding="utf-8").write(info)
print("ok")
