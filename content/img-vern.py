# -*- coding: utf-8 -*-
# Картинки к статье «Как вернуться к китайскому после перерыва»
# Обложка    — книга с закладкой: вы остановились здесь
# Инфографика — индикаторы заряда: что сохранилось, а что разрядилось
S = "/tmp/claude-0/-home-user-Kitai-Shool/a463bfca-82a9-56fd-ae09-42a7257ff999/scratchpad/"

FONTS = ("<link href=\"https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,600;0,700;1,600"
         "&family=Inter:wght@400;500;600;700&family=Noto+Serif+SC:wght@600;700&display=swap\" rel=\"stylesheet\">")
VARS = (":root{--brick:#A41E3A;--brick-d:#841630;--brick-soft:#F7E6EB;--ink:#2C2420;--ink-2:#5A4F45;"
        "--taupe:#8B7D6B;--cream:#FAF7F2;--cream-2:#F3EDE3;--hair:#EAE3D8;--surface:#fff;"
        "--green:#1E7A46;--green-soft:#E3F6E9;--amber:#C08A2E;--amber-s:#FBF2DF;--blue:#2F5D8C;--blue-s:#E7EEF6;"
        "--paper:#FDFBF5;--paper-2:#F5EFE3;--edge:#E2D8C6}")

# ------------------------------------------------------------------ обложка
hero = """<!DOCTYPE html><html lang="ru"><head><meta charset="utf-8">
%s
<style>
%s
*{margin:0;box-sizing:border-box}html,body{width:1200px;height:630px}
.card{width:1200px;height:630px;background:radial-gradient(1100px 680px at 15%% 10%%, #fff 0%%, var(--cream) 55%%, var(--cream-2) 100%%);position:relative;overflow:hidden;font-family:'Inter',sans-serif;display:flex;align-items:center;justify-content:space-between;padding:0 64px 0 72px}
.card:before{content:"";position:absolute;left:0;top:0;bottom:0;width:12px;background:var(--brick)}
.txt{flex:0 0 470px}
.eyebrow{color:var(--brick);font-weight:700;font-size:18px;letter-spacing:.19em;text-transform:uppercase;margin-bottom:12px}
h1{font-family:'Cormorant Garamond',serif;font-weight:600;font-size:50px;line-height:1.06;color:var(--ink);letter-spacing:-.4px}
h1 i{font-style:italic;color:var(--brick)}
.sub{font-size:18px;color:var(--ink-2);line-height:1.42;max-width:31ch;margin-top:16px}
.note{display:inline-block;margin-top:24px;background:var(--surface);border:1px solid var(--hair);border-left:4px solid var(--brick);border-radius:13px;padding:12px 18px;font-size:15.5px;color:var(--ink-2);line-height:1.36;max-width:34ch}
.note b{color:var(--ink)}
.brand{position:absolute;left:72px;bottom:32px;display:flex;align-items:center;gap:11px;color:var(--ink)}
.brand b{font-family:'Cormorant Garamond',serif;font-weight:700;font-size:26px}
.brand .bdot{width:10px;height:10px;border-radius:50%%;background:var(--brick)}
.brand span{color:var(--taupe);font-size:16px}

/* книга с закладкой */
.book{flex:0 0 520px;position:relative;height:392px;display:flex;filter:drop-shadow(0 18px 34px rgba(44,36,32,.2))}
.page{flex:1 1 0;background:linear-gradient(180deg,var(--paper),var(--paper-2));border:1px solid var(--edge);padding:30px 26px}
.page.l{border-radius:10px 2px 2px 10px;border-right:0}
.page.r{border-radius:2px 10px 10px 2px}
.spine{width:16px;background:linear-gradient(90deg,#E6DCCA,#D8CDB8,#E6DCCA);border-top:1px solid var(--edge);border-bottom:1px solid var(--edge)}
.ln{height:9px;border-radius:5px;background:#E8DFCF;margin-bottom:13px}
.ln.s{width:62%%}
.ln.m{width:84%%}
.han-row{display:flex;gap:10px;margin-bottom:16px}
.han-row span{font-family:'Noto Serif SC',serif;font-weight:700;font-size:30px;color:#4A4038;line-height:1}
.dim{opacity:.32}
.mark{position:absolute;right:52px;top:-22px;width:62px;height:220px;background:linear-gradient(180deg,#B32442,#8E1630);border-radius:3px 3px 0 0;box-shadow:0 8px 18px rgba(44,36,32,.26);display:flex;align-items:flex-end;justify-content:center;padding-bottom:28px}
.mark:after{content:"";position:absolute;left:0;right:0;bottom:0;height:22px;background:var(--cream);clip-path:polygon(0 0, 50%% 100%%, 100%% 0)}
.mark span{font-family:'Noto Serif SC',serif;font-weight:700;font-size:26px;color:#F7E3C0;line-height:1}
.here{position:absolute;right:36px;bottom:-16px;background:var(--surface);border:1px solid var(--hair);border-radius:11px;padding:9px 15px;font-size:14px;color:var(--ink);box-shadow:0 6px 16px rgba(44,36,32,.12)}
.here b{color:var(--brick)}
</style></head><body>
<div class="card">
  <div class="txt">
    <div class="eyebrow">Возвращение</div>
    <h1>Как вернуться к китайскому <i>после перерыва</i></h1>
    <div class="sub">Язык не стирается — он становится недоступен. Возвращать нужно доступ, а не учить заново</div>
    <div class="note"><b>Начинать с первой страницы не нужно:</b> место, где вы остановились, никуда не делось</div>
  </div>
  <div class="book">
    <div class="page l">
      <div class="ln m"></div><div class="ln"></div><div class="ln s"></div>
      <div class="han-row"><span>学</span><span>习</span><span>汉</span><span>语</span></div>
      <div class="ln"></div><div class="ln m"></div><div class="ln s"></div>
    </div>
    <div class="spine"></div>
    <div class="page r">
      <div class="ln s dim"></div><div class="ln m dim"></div>
      <div class="ln dim"></div>
      <div class="ln dim"></div><div class="ln s dim"></div><div class="ln m dim"></div>
    </div>
    <div class="mark"><span>复</span></div>
    <div class="here">Вы остановились <b>здесь</b></div>
  </div>
  <div class="brand"><span class="bdot"></span><b>Kitai School</b><span>&middot; kitai-school.ru</span></div>
</div>
</body></html>""" % (FONTS, VARS)

open(S + "vn-hero.html", "w", encoding="utf-8").write(hero)

# -------------------------------------------------------------- инфографика
CELLS = [
    ("Узнавание иероглифов", 8, "#1E7A46", "видите знак — вспоминаете значение",
     "почти полный", "держится дольше всего"),
    ("Грамматика", 6, "#2F5D8C", "порядок слов и конструкции",
     "больше половины", "правила вспоминаются с подсказки"),
    ("Активная лексика", 3, "#C08A2E", "слова, которые нужно достать из памяти сами",
     "низкий", "уходит заметно быстрее"),
    ("Тоны и говорение", 2, "#A41E3A", "произнести вслух без подготовки",
     "почти пустой", "страдает первым"),
]


def bar(filled, color):
    cells = "".join(
        '<i class="c%s" style="background:%s"></i>' % ("" if k < filled else " e", color if k < filled else "#EDE6DA")
        for k in range(10))
    return cells


rows = "\n".join(
    '<div class="row">'
    '  <div class="name">%s<span>%s</span></div>'
    '  <div class="batt"><div class="cells">%s</div><div class="cap"></div></div>'
    '  <div class="lvl" style="color:%s">%s</div>'
    '  <div class="what">%s</div>'
    '</div>' % (n, sub, bar(p, c), c, lvl, what)
    for n, p, c, sub, lvl, what in CELLS)

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
.hint{flex:0 0 352px;background:var(--surface);border:1px solid var(--hair);border-left:4px solid var(--brick);border-radius:12px;padding:12px 17px;font-size:14.5px;color:var(--ink-2);line-height:1.36}
.hint b{color:var(--ink)}

.rows{display:flex;flex-direction:column;gap:13px}
.row{display:flex;align-items:center;gap:20px;background:var(--surface);border:1px solid var(--hair);border-radius:14px;padding:13px 20px;box-shadow:0 5px 14px rgba(44,36,32,.05)}
.name{flex:0 0 250px;font-size:16px;font-weight:600;color:var(--ink);line-height:1.25}
.name span{display:block;font-size:12.5px;font-weight:400;color:var(--taupe);margin-top:3px;line-height:1.3}
.batt{flex:0 0 268px;display:flex;align-items:center}
.cells{display:flex;gap:3px;padding:5px;border:2px solid var(--ink);border-radius:7px;background:#fff}
.cells i{display:block;width:21px;height:26px;border-radius:2px}
.cap{width:6px;height:14px;background:var(--ink);border-radius:0 3px 3px 0}
.lvl{flex:0 0 128px;font-size:15px;font-weight:700;line-height:1.25;text-align:right}
.what{flex:1 1 auto;font-size:14.5px;color:var(--ink-2);line-height:1.34;border-left:1px solid var(--hair);padding-left:20px}

.foot{margin-top:auto;display:flex;align-items:center;gap:18px;padding-top:18px}
.foot .msg{flex:1 1 auto;background:var(--brick-soft);border:1px solid var(--brick);border-radius:14px;padding:12px 21px;font-size:15.5px;color:var(--ink);line-height:1.34}
.foot .msg b{color:var(--brick)}
.brand{display:flex;align-items:center;gap:10px;color:var(--ink);flex:0 0 auto}
.brand b{font-family:'Cormorant Garamond',serif;font-weight:700;font-size:23px}
.brand .dot2{width:9px;height:9px;border-radius:50%%;background:var(--brick)}
.brand span{color:var(--taupe);font-size:15px}
</style></head><body>
<div class="wrap">
  <div class="top">
    <div>
      <div class="eyebrow">После перерыва</div>
      <h2>Уходит <i>не всё и не равномерно</i></h2>
    </div>
    <div class="hint">Шкалы здесь условные — это не измерение, а порядок величин: <b>первым страдает то, что нужно доставать из памяти самому</b>.</div>
  </div>

  <div class="rows">
%s
  </div>

  <div class="foot">
    <div class="msg">Отсюда и знакомое чувство: <b>читаю и понимаю, а сказать не могу</b>. Это не «всё забыл» — это разряжено только говорение</div>
    <div class="brand"><span class="dot2"></span><b>Kitai School</b><span>&middot; kitai-school.ru</span></div>
  </div>
</div>
</body></html>""" % (FONTS, VARS, rows)

info = info.replace("HGT", "576")
open(S + "vn-info.html", "w", encoding="utf-8").write(info)
print("ok")
