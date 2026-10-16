# -*- coding: utf-8 -*-
# Картинки к статье «„Серый“ по-китайски»
# Обложка    — образец краски: выкраска с ярлыком и полоской оттенков
# Инфографика — картотечные вкладки: три слоя значений знака 灰
S = "/tmp/claude-0/-home-user-Kitai-Shool/a463bfca-82a9-56fd-ae09-42a7257ff999/scratchpad/"

FONTS = ("<link href=\"https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,600;0,700;1,600"
         "&family=Inter:wght@400;500;600;700&family=Noto+Serif+SC:wght@600;700&display=swap\" rel=\"stylesheet\">")
VARS = (":root{--brick:#A41E3A;--brick-d:#841630;--brick-soft:#F7E6EB;--ink:#2C2420;--ink-2:#5A4F45;"
        "--taupe:#8B7D6B;--cream:#FAF7F2;--cream-2:#F3EDE3;--hair:#EAE3D8;--surface:#fff;"
        "--green:#1E7A46;--green-soft:#E3F6E9;--amber:#C08A2E;--amber-s:#FBF2DF;--blue:#2F5D8C;--blue-s:#E7EEF6;"
        "--g-1:#CBC8C2;--g-2:#8E8B84;--g-3:#55534E}")

# ------------------------------------------------------------------ обложка
hero = """<!DOCTYPE html><html lang="ru"><head><meta charset="utf-8">
%s
<style>
%s
*{margin:0;box-sizing:border-box}html,body{width:1200px;height:630px}
.card{width:1200px;height:630px;background:radial-gradient(1100px 680px at 15%% 10%%, #fff 0%%, var(--cream) 55%%, var(--cream-2) 100%%);position:relative;overflow:hidden;font-family:'Inter',sans-serif;display:flex;align-items:center;justify-content:space-between;padding:0 72px}
.card:before{content:"";position:absolute;left:0;top:0;bottom:0;width:12px;background:var(--brick)}
.txt{flex:0 0 500px}
.eyebrow{color:var(--brick);font-weight:700;font-size:18px;letter-spacing:.19em;text-transform:uppercase;margin-bottom:12px}
h1{font-family:'Cormorant Garamond',serif;font-weight:600;font-size:50px;line-height:1.06;color:var(--ink);letter-spacing:-.4px;max-width:470px}
h1 i{font-style:italic;color:var(--brick)}
.sub{font-size:18px;color:var(--ink-2);line-height:1.42;max-width:31ch;margin-top:16px}
.brand{position:absolute;left:72px;bottom:32px;display:flex;align-items:center;gap:11px;color:var(--ink)}
.brand b{font-family:'Cormorant Garamond',serif;font-weight:700;font-size:26px}
.brand .bdot{width:10px;height:10px;border-radius:50%%;background:var(--brick)}
.brand span{color:var(--taupe);font-size:16px}

/* выкраска */
.art{flex:0 0 498px;display:flex;gap:18px;align-items:stretch}
.swatch{flex:1 1 auto;background:var(--surface);border:1px solid var(--hair);border-radius:16px;overflow:hidden;box-shadow:0 18px 40px rgba(44,36,32,.16)}
.swatch .fill{height:252px;background:linear-gradient(160deg,#9C9992 0%%,var(--g-2) 52%%,#7E7B75 100%%);display:flex;align-items:flex-start;justify-content:flex-end;padding:16px 18px}
.swatch .fill b{font-family:'Noto Serif SC',serif;font-weight:700;font-size:62px;color:rgba(255,255,255,.92);line-height:1}
.swatch .lab{padding:17px 20px 19px}
.lab .cn{font-family:'Noto Serif SC',serif;font-weight:700;font-size:34px;color:var(--ink);line-height:1}
.lab .py{font-size:20px;font-weight:600;color:var(--brick);margin-top:4px}
.lab .ru{font-size:15px;color:var(--ink-2);margin-top:9px;padding-top:9px;border-top:1px dotted var(--hair);line-height:1.38}
.lab .ru b{color:var(--ink)}
.strip{flex:0 0 116px;display:flex;flex-direction:column;border-radius:14px;overflow:hidden;border:1px solid var(--hair);box-shadow:0 10px 24px rgba(44,36,32,.12)}
.strip div{flex:1 1 0;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:3px;font-size:10.5px;letter-spacing:.02em;text-align:center}
.strip .h{font-family:'Noto Serif SC',serif;font-weight:700;font-size:17px;line-height:1}
.s1{background:var(--g-1);color:#3A3833}
.s2{background:var(--g-2);color:#fff}
.s3{background:var(--g-3);color:#fff}
</style></head><body>
<div class="card">
  <div class="txt">
    <div class="eyebrow">Цвет и слово</div>
    <h1>«Серый»<br><i>по-китайски</i></h1>
    <div class="sub">灰色 huīsè. Первый знак значит «пепел» — то, что остаётся от огня</div>
  </div>
  <div class="art">
    <div class="swatch">
      <div class="fill"><b>灰</b></div>
      <div class="lab">
        <div class="cn">灰色</div>
        <div class="py">huīsè &middot; хуэй-сэ</div>
        <div class="ru"><b>灰</b> — пепел, зола, известь; серый; подавленный</div>
      </div>
    </div>
    <div class="strip">
      <div class="s1"><span class="h">浅灰色</span><span>СВЕТЛО-СЕРЫЙ</span></div>
      <div class="s2"><span class="h">灰色</span><span>СЕРЫЙ</span></div>
      <div class="s3"><span class="h">深灰色</span><span>ТЁМНО-СЕРЫЙ</span></div>
    </div>
  </div>
  <div class="brand"><span class="bdot"></span><b>Kitai School</b><span>&middot; kitai-school.ru</span></div>
</div>
</body></html>""" % (FONTS, VARS)

open(S + "sr-hero.html", "w", encoding="utf-8").write(hero)

# -------------------------------------------------------------- инфографика
TABS = [
    ("tab-a", "1 &middot; ВЕЩЕСТВО", "То, что осталось от огня",
     [("灰", "huī", "пепел, зола"), ("灰尘", "huīchén", "пыль"), ("石灰", "shíhuī", "извёстка")],
     "Исходное значение знака: ключ 火 «огонь» и рука над ним"),
    ("tab-b", "2 &middot; ЦВЕТ", "Цвет, названный по веществу",
     [("灰色", "huīsè", "серый"), ("浅灰色", "qiǎn huīsè", "светло-серый"),
      ("银灰色", "yín huīsè", "серебристо-серый")],
     "Обычное, нейтральное слово: подходит почти любой вещи"),
    ("tab-c", "3 &middot; СОСТОЯНИЕ", "Когда цвет говорит о человеке и деле",
     [("灰心", "huīxīn", "упасть духом"), ("心灰意冷", "xīn huī yì lěng", "опустить руки"),
      ("灰色地带", "huīsè dìdài", "серая зона")],
     "Второй слой значения — неясность и упадок, как и в русском"),
]

cards = "\n".join(
    '<div class="tab %s">'
    '  <div class="tag">%s</div>'
    '  <div class="body">'
    '    <div class="ttl">%s</div>'
    '    <div class="rows">%s</div>'
    '    <div class="note">%s</div>'
    '  </div>'
    '</div>' % (
        cls, tag, ttl,
        "".join('<div class="wr"><span class="h">%s</span><span class="p">%s</span><span class="t">%s</span></div>'
                % w for w in words),
        note)
    for cls, tag, ttl, words, note in TABS)

info = """<!DOCTYPE html><html lang="ru"><head><meta charset="utf-8">
%s
<style>
%s
*{margin:0;box-sizing:border-box}html,body{width:1200px;height:HGTpx}
.wrap{width:1200px;height:HGTpx;background:linear-gradient(180deg,#fff 0%%,var(--cream) 46%%,var(--cream-2) 100%%);font-family:'Inter',sans-serif;padding:32px 46px 26px;display:flex;flex-direction:column}
.top{display:flex;align-items:flex-end;justify-content:space-between;gap:30px;margin-bottom:38px}
.eyebrow{color:var(--brick);font-weight:700;font-size:14.5px;letter-spacing:.17em;text-transform:uppercase;margin-bottom:7px}
h2{font-family:'Cormorant Garamond',serif;font-weight:600;font-size:40px;line-height:1.07;color:var(--ink);letter-spacing:-.3px}
h2 i{font-style:italic;color:var(--brick)}
.hint{flex:0 0 346px;background:var(--surface);border:1px solid var(--hair);border-left:4px solid var(--brick);border-radius:12px;padding:12px 17px;font-size:14.5px;color:var(--ink-2);line-height:1.36}
.hint b{color:var(--ink)}

.tabs{display:flex;gap:22px;align-items:stretch}
.tab{flex:1 1 0;position:relative;background:var(--surface);border:1px solid var(--hair);border-radius:4px 14px 14px 14px;box-shadow:0 10px 24px rgba(44,36,32,.10)}
.tab .tag{position:absolute;top:-30px;left:-1px;height:30px;padding:0 20px;display:flex;align-items:center;font-size:11.5px;font-weight:700;letter-spacing:.11em;border-radius:10px 10px 0 0;color:#fff}
.tab-a .tag{background:var(--g-1);color:#3A3833}
.tab-b .tag{background:var(--g-2)}
.tab-c .tag{background:var(--brick)}
.tab-c{border-color:var(--brick)}
.body{padding:16px 20px 18px}
.ttl{font-size:15.5px;font-weight:600;color:var(--ink);line-height:1.3;min-height:40px;border-bottom:1px solid var(--hair);padding-bottom:10px}
.rows{padding:4px 0 2px}
.wr{display:flex;align-items:baseline;gap:10px;padding:9px 0;border-bottom:1px dotted var(--hair)}
.wr:last-child{border-bottom:0}
.wr .h{flex:0 0 auto;font-family:'Noto Serif SC',serif;font-weight:700;font-size:23px;color:var(--ink);line-height:1.1}
.tab-c .wr .h{color:var(--brick)}
.wr .p{flex:0 0 auto;font-size:13px;color:var(--taupe)}
.wr .t{flex:1 1 auto;text-align:right;font-size:13.5px;color:var(--ink-2)}
.note{margin-top:10px;background:var(--cream);border-radius:10px;padding:10px 13px;font-size:13px;color:var(--ink-2);line-height:1.36}

.scale{margin-top:24px;display:flex;align-items:center;gap:0;border-radius:14px;overflow:hidden;border:1px solid var(--hair);box-shadow:0 6px 18px rgba(44,36,32,.07)}
.scale div{flex:1 1 0;padding:13px 20px;display:flex;align-items:baseline;gap:12px}
.scale .h{font-family:'Noto Serif SC',serif;font-weight:700;font-size:20px;line-height:1}
.scale .t{font-size:14px}
.w1{background:#fff;color:var(--ink)}
.w1 .t{color:var(--ink-2)}
.w2{background:var(--g-1);color:#2F2D29}
.w2 .t{color:#4A4843}
.w3{background:var(--g-3);color:#fff}
.w3 .t{color:#E2E0DC}

.foot{margin-top:auto;display:flex;align-items:center;gap:18px;padding-top:18px}
.foot .msg{flex:1 1 auto;background:var(--brick-soft);border:1px solid var(--brick);border-radius:14px;padding:12px 21px;font-size:16px;color:var(--ink);line-height:1.34}
.foot .msg b{color:var(--brick)}
.brand{display:flex;align-items:center;gap:10px;color:var(--ink);flex:0 0 auto}
.brand b{font-family:'Cormorant Garamond',serif;font-weight:700;font-size:23px}
.brand .dot2{width:9px;height:9px;border-radius:50%%;background:var(--brick)}
.brand span{color:var(--taupe);font-size:15px}
</style></head><body>
<div class="wrap">
  <div class="top">
    <div>
      <div class="eyebrow">Один знак — три слоя</div>
      <h2>От пепла к цвету, <i>от цвета к состоянию</i></h2>
    </div>
    <div class="hint">灰 — сначала вещество и только потом цвет. <b>Из одного знака выросли три группы слов</b>, и третья к цвету уже почти не относится.</div>
  </div>

  <div class="tabs">
%s
  </div>

  <div class="scale">
    <div class="w1"><span class="h">白色收入</span><span class="t">легальный доход</span></div>
    <div class="w2"><span class="h">灰色收入</span><span class="t">между законным и нет</span></div>
    <div class="w3"><span class="h">黑色收入</span><span class="t">незаконный доход</span></div>
  </div>

  <div class="foot">
    <div class="msg">Цветовая шкала работает <b>как в русском</b>: белое — чистое, чёрное — незаконное, серое — то, что посередине</div>
    <div class="brand"><span class="dot2"></span><b>Kitai School</b><span>&middot; kitai-school.ru</span></div>
  </div>
</div>
</body></html>""" % (FONTS, VARS, cards)

info = info.replace("HGT", "646")
open(S + "sr-info.html", "w", encoding="utf-8").write(info)
print("ok")
