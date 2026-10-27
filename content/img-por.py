# -*- coding: utf-8 -*-
# Картинки к статье «Порядковые числительные в китайском языке»
# Обложка    — номерок из гардероба: число отвечает «который», а не «сколько»
# Инфографика — конструкция из четырёх блоков и случаи, где первый блок снимается
S = ("/tmp/claude-0/-home-user-Kitai-Shool/a463bfca-82a9-56fd-ae09-42a7257ff999/"
     "scratchpad/")

FONTS = ("<link href=\"https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,600;0,700;1,600"
         "&family=Inter:wght@400;500;600;700&family=Noto+Serif+SC:wght@600;700&display=swap\" rel=\"stylesheet\">")
VARS = (":root{--brick:#A41E3A;--brick-d:#841630;--brick-soft:#F7E6EB;--ink:#2C2420;--ink-2:#5A4F45;"
        "--taupe:#8B7D6B;--cream:#FAF7F2;--cream-2:#F3EDE3;--hair:#EAE3D8;--surface:#fff;"
        "--steel:#C9CBCF;--steel-2:#A7ABB2;--steel-3:#83888F;--slate:#2F5D8C;--good:#1E7A46}")

hero = """<!DOCTYPE html><html lang="ru"><head><meta charset="utf-8">
%s
<style>
%s
*{margin:0;box-sizing:border-box}html,body{width:1200px;height:630px}
.card{width:1200px;height:630px;background:radial-gradient(1050px 660px at 14%% 12%%, #fff 0%%, var(--cream) 52%%, var(--cream-2) 100%%);position:relative;overflow:hidden;font-family:'Inter',sans-serif;padding:52px 46px 0 72px;display:flex;justify-content:space-between}
.card:before{content:"";position:absolute;left:0;top:0;bottom:0;width:12px;background:var(--brick)}
.txt{flex:0 0 500px;padding-top:6px}
.eyebrow{color:var(--brick);font-weight:700;font-size:18px;letter-spacing:.19em;text-transform:uppercase;margin-bottom:13px}
h1{font-family:'Cormorant Garamond',serif;font-weight:600;font-size:45px;line-height:1.07;color:var(--ink);letter-spacing:-.4px}
h1 i{font-style:italic;color:var(--brick)}
.sub{font-size:18px;color:var(--ink-2);line-height:1.42;max-width:31ch;margin-top:16px}
.tip{display:inline-block;margin-top:22px;background:var(--surface);border:1px solid var(--hair);border-left:4px solid var(--brick);border-radius:13px;padding:13px 19px;font-size:15.5px;color:var(--ink-2);line-height:1.36;max-width:35ch}
.tip b{color:var(--ink)}

/* номерок из гардероба */
.scene{flex:0 0 478px;padding-top:54px;display:flex;flex-direction:column;align-items:center}
.hook{width:2px;height:56px;background:linear-gradient(180deg,rgba(139,125,107,0),var(--taupe));margin-bottom:-6px}
.ring{width:34px;height:34px;border-radius:50%%;border:5px solid var(--steel-3);margin-bottom:-12px;box-shadow:0 2px 4px rgba(44,36,32,.18)}
.tag{position:relative;width:272px;height:272px;border-radius:50%%;background:radial-gradient(circle at 34%% 28%%, #F2F3F5 0%%, var(--steel) 46%%, var(--steel-2) 78%%, var(--steel-3) 100%%);box-shadow:0 18px 32px rgba(44,36,32,.26), inset 0 3px 7px rgba(255,255,255,.65), inset 0 -6px 12px rgba(0,0,0,.14);display:flex;flex-direction:column;align-items:center;justify-content:center}
.tag:before{content:"";position:absolute;inset:16px;border-radius:50%%;border:2px solid rgba(255,255,255,.5)}
.tag:after{content:"";position:absolute;left:50%%;top:13px;transform:translateX(-50%%);width:19px;height:19px;border-radius:50%%;background:var(--cream-2);box-shadow:inset 0 2px 4px rgba(0,0,0,.35)}
.tag .num{font-family:'Noto Serif SC',serif;font-size:104px;color:#4A4E54;line-height:1;text-shadow:0 2px 0 rgba(255,255,255,.55), 0 -1px 1px rgba(0,0,0,.3);margin-top:16px}
.tag .word{font-size:15px;letter-spacing:.2em;text-transform:uppercase;color:#6C7177;margin-top:8px}
.plate{margin-top:26px;background:var(--surface);border:1px solid var(--hair);border-radius:13px;padding:14px 20px;text-align:center;box-shadow:0 6px 14px rgba(44,36,32,.08)}
.plate .q{font-size:15px;color:var(--taupe)}
.plate .a{font-family:'Noto Serif SC',serif;font-size:30px;color:var(--brick);margin-top:4px}
.plate .p{font-size:14.5px;color:var(--ink-2);font-style:italic;margin-top:2px}
.brand{position:absolute;left:72px;bottom:28px;display:flex;align-items:center;gap:11px;color:var(--ink)}
.brand b{font-family:'Cormorant Garamond',serif;font-weight:700;font-size:26px}
.brand .bdot{width:10px;height:10px;border-radius:50%%;background:var(--brick)}
.brand span{color:var(--taupe);font-size:16px}
</style></head><body>
<div class="card">
  <div class="txt">
    <div class="eyebrow">Грамматика</div>
    <h1>Порядковые числительные <i>в китайском</i></h1>
    <div class="sub">«Третий» и «три» — это два разных слова, и собираются они по-разному</div>
    <div class="tip"><b>Число на номерке отвечает не «сколько», а «который».</b> По-китайски для этого перед числом ставят 第</div>
  </div>
  <div class="scene">
    <div class="hook"></div>
    <div class="ring"></div>
    <div class="tag">
      <div class="num">三</div>
      <div class="word">гардероб</div>
    </div>
    <div class="plate">
      <div class="q">который по счёту?</div>
      <div class="a">第三</div>
      <div class="p">dì-sān — третий</div>
    </div>
  </div>
  <div class="brand"><span class="bdot"></span><b>Kitai School</b><span>&middot; kitai-school.ru</span></div>
</div>
</body></html>""" % (FONTS, VARS)

open(S + "por-hero.html", "w", encoding="utf-8").write(hero)

# --------------------------------------------------------------- инфографика
BLOCKS = [
    ("第", "dì", "приставка порядка", True),
    ("三", "sān", "число", False),
    ("本", "běn", "счётное слово", False),
    ("书", "shū", "предмет", False),
]

blocks = ""
for i, (han, py, lab, mark) in enumerate(BLOCKS):
    if i:
        blocks += '<span class="plus">+</span>'
    blocks += ('<div class="bl%s"><div class="lb">%s</div><div class="hn">%s</div>'
               '<div class="py">%s</div></div>' % (" key" if mark else "", lab, han, py))

NOD = [
    ("三楼", "sān lóu", "третий этаж"),
    ("一月", "yī yuè", "январь"),
    ("星期一", "xīngqī yī", "понедельник"),
    ("三路车", "sān lù chē", "третий маршрут"),
]

nod = "".join(
    '<div class="nd"><div class="cross">第</div><div class="bd">'
    '<div class="nh">%s</div><div class="np">%s</div><div class="nr">%s</div></div></div>'
    % n for n in NOD)

info = """<!DOCTYPE html><html lang="ru"><head><meta charset="utf-8">
%(fonts)s
<style>
%(vars)s
*{margin:0;box-sizing:border-box}html,body{width:1200px;height:HGTpx}
.wrap{width:1200px;height:HGTpx;background:linear-gradient(180deg,#fff 0%%,var(--cream) 46%%,var(--cream-2) 100%%);font-family:'Inter',sans-serif;padding:32px 46px 28px;display:flex;flex-direction:column}
.top{display:flex;align-items:flex-end;justify-content:space-between;gap:30px;margin-bottom:22px}
.eyebrow{color:var(--brick);font-weight:700;font-size:14.5px;letter-spacing:.17em;text-transform:uppercase;margin-bottom:7px}
h2{font-family:'Cormorant Garamond',serif;font-weight:600;font-size:40px;line-height:1.07;color:var(--ink);letter-spacing:-.3px}
h2 i{font-style:italic;color:var(--brick)}
.hint{flex:0 0 368px;background:var(--surface);border:1px solid var(--hair);border-left:4px solid var(--brick);border-radius:12px;padding:12px 17px;font-size:14.5px;color:var(--ink-2);line-height:1.36}
.hint b{color:var(--ink)}

.row{display:flex;align-items:center;justify-content:center;gap:14px}
.bl{background:var(--surface);border:2px solid var(--hair);border-radius:15px;padding:13px 22px;text-align:center;min-width:150px;box-shadow:0 5px 13px rgba(44,36,32,.06)}
.bl .lb{font-size:12.5px;color:var(--taupe);letter-spacing:.04em}
.bl .hn{font-family:'Noto Serif SC',serif;font-size:40px;color:var(--ink);line-height:1.16;margin-top:2px}
.bl .py{font-size:13.5px;color:var(--ink-2);font-style:italic}
.bl.key{border-color:var(--brick);background:var(--brick-soft)}
.bl.key .hn{color:var(--brick)}
.bl.key .lb{color:var(--brick-d);font-weight:700}
.plus{font-size:24px;color:var(--taupe)}
.whole{text-align:center;margin-top:14px;font-size:16px;color:var(--ink-2)}
.whole b{font-family:'Noto Serif SC',serif;font-size:21px;color:var(--ink);vertical-align:-1px}

.sep{display:flex;align-items:center;gap:16px;margin:22px 0 16px}
.sep span{font-size:15px;font-weight:700;color:var(--brick-d);white-space:nowrap}
.sep i{flex:1 1 auto;height:1px;background:var(--hair)}

.nods{display:flex;gap:14px}
.nd{flex:1 1 0;background:var(--surface);border:1px solid var(--hair);border-radius:15px;padding:14px 16px;display:flex;align-items:center;gap:13px;box-shadow:0 4px 12px rgba(44,36,32,.05)}
.cross{position:relative;flex:0 0 42px;height:42px;border-radius:10px;background:var(--cream-2);color:var(--taupe);font-family:'Noto Serif SC',serif;font-size:24px;display:flex;align-items:center;justify-content:center}
.cross:after{content:"";position:absolute;left:5px;right:5px;top:50%%;height:2px;background:var(--brick);transform:rotate(-20deg)}
.nh{font-family:'Noto Serif SC',serif;font-size:25px;color:var(--ink);line-height:1.12}
.np{font-size:13px;color:var(--ink-2);font-style:italic}
.nr{font-size:13.5px;color:var(--taupe);margin-top:1px}

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
      <div class="eyebrow">Конструкция</div>
      <h2>Порядок собирается <i>из четырёх блоков</i></h2>
    </div>
    <div class="hint">Первый блок и делает число порядковым. <b>Но есть места, где его не ставят</b> — этажи, месяцы, дни недели и номера маршрутов.</div>
  </div>

  <div class="row">%(blocks)s</div>
  <div class="whole">вместе — <b>第三本书</b> dì-sān běn shū, «третья книга»</div>

  <div class="sep"><span>А здесь первый блок снимается</span><i></i></div>
  <div class="nods">%(nod)s</div>

  <div class="foot">
    <div class="msg">Порядок там и так понятен — <b>第 добавлять не нужно</b></div>
    <div class="brand"><span class="dot2"></span><b>Kitai School</b><span>&middot; kitai-school.ru</span></div>
  </div>
</div>
</body></html>""" % dict(fonts=FONTS, vars=VARS, blocks=blocks, nod=nod)

info = info.replace("HGT", "520")
open(S + "por-info.html", "w", encoding="utf-8").write(info)
assert len(BLOCKS) == 4 and sum(b[3] for b in BLOCKS) == 1, "блоков не четыре или выделен не один"
print("ok, блоков:", len(BLOCKS), "| случаев без 第:", len(NOD))
