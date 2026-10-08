# -*- coding: utf-8 -*-
# Картинки к статье «Как здороваются китайцы: жесты»
# Обложка    — три кадра киноплёнки: 拱 → 鞠 → 握
# Инфографика — три круглых окна со схемой рук: мужской, женский, перепутанный
S = "/tmp/claude-0/-home-user-Kitai-Shool/a463bfca-82a9-56fd-ae09-42a7257ff999/scratchpad/"

FONTS = ("<link href=\"https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,600;0,700;1,600"
         "&family=Inter:wght@400;500;600;700&family=Noto+Serif+SC:wght@600;700&display=swap\" rel=\"stylesheet\">")
VARS = (":root{--brick:#A41E3A;--brick-d:#841630;--brick-soft:#F7E6EB;--ink:#2C2420;--ink-2:#5A4F45;"
        "--taupe:#8B7D6B;--cream:#FAF7F2;--cream-2:#F3EDE3;--hair:#EAE3D8;--surface:#fff;"
        "--green:#1E7A46;--green-soft:#E3F6E9;--amber:#C08A2E;--amber-s:#FBF2DF;--blue:#2F5D8C;--blue-s:#E7EEF6}")

# ------------------------------------------------------------------ обложка
def frame(glyph, era, title, line, tone):
    return ('<div class="fr %s">'
            '<div class="era">%s</div>'
            '<div class="win"><span class="gl">%s</span></div>'
            '<div class="nm">%s</div>'
            '<div class="ln">%s</div>'
            '</div>') % (tone, era, glyph, title, line)

frames = "".join([
    frame("拱", "до XX века", "拱手", "кулак, накрытый ладонью", "a"),
    frame("鞠", "начало Республики", "鞠躬", "поклон и снятая шляпа", "b"),
    frame("握", "сегодня", "握手", "рукопожатие — мягче и короче", "c"),
])

hero = """<!DOCTYPE html><html lang="ru"><head><meta charset="utf-8">
%s
<style>
%s
*{margin:0;box-sizing:border-box}html,body{width:1200px;height:630px}
.card{width:1200px;height:630px;background:radial-gradient(1100px 680px at 18%% 10%%, #fff 0%%, var(--cream) 52%%, var(--cream-2) 100%%);position:relative;overflow:hidden;font-family:'Inter',sans-serif;padding:42px 56px 0 72px;display:flex;flex-direction:column}
.card:before{content:"";position:absolute;left:0;top:0;bottom:0;width:12px;background:var(--brick)}
.seal{position:absolute;right:44px;top:34px;width:88px;height:88px;border:2.5px solid var(--brick);border-radius:14px;display:flex;align-items:center;justify-content:center;color:var(--brick);font-family:'Noto Serif SC',serif;font-weight:700;font-size:32px;opacity:.92}
.eyebrow{color:var(--brick);font-weight:700;font-size:18px;letter-spacing:.19em;text-transform:uppercase;margin-bottom:11px}
h1{font-family:'Cormorant Garamond',serif;font-weight:600;font-size:58px;line-height:1.02;color:var(--ink);letter-spacing:-.6px;max-width:22ch}
h1 i{font-style:italic;color:var(--brick)}
.sub{font-size:18.5px;color:var(--ink-2);line-height:1.4;max-width:50ch;margin-top:13px}

.mid{margin-top:auto;display:flex;align-items:center;gap:22px;padding-bottom:20px}
.mid .cap{font-size:16px;color:var(--taupe);letter-spacing:.02em;white-space:nowrap}
.mid .cap b{color:var(--ink);font-weight:600}
.mid .rule{flex:1 1 auto;height:1px;background:var(--hair)}

.film{position:relative;background:#241D19;border-radius:16px 16px 0 0;padding:13px 20px 0;box-shadow:0 -6px 26px rgba(44,36,32,.17)}
.perf{display:flex;justify-content:space-between;padding:0 6px 10px}
.perf i{display:block;width:26px;height:12px;border-radius:3px;background:#4A3F38}
.strip{display:flex;gap:16px;padding-bottom:20px}
.fr{flex:1 1 0;background:var(--surface);border-radius:10px;padding:15px 19px 17px;position:relative}
.era{font-size:12px;font-weight:700;letter-spacing:.1em;text-transform:uppercase;color:var(--taupe);margin-bottom:10px}
.win{height:118px;border-radius:8px;display:flex;align-items:center;justify-content:center;margin-bottom:11px;border:1px solid var(--hair)}
.gl{font-family:'Noto Serif SC',serif;font-weight:700;font-size:84px;line-height:1}
.fr.a .win{background:var(--cream-2)}.fr.a .gl{color:var(--taupe)}
.fr.b .win{background:var(--amber-s)}.fr.b .gl{color:var(--amber)}
.fr.c .win{background:var(--brick-soft);border-color:var(--brick)}.fr.c .gl{color:var(--brick)}
.nm{font-family:'Noto Serif SC',serif;font-weight:700;font-size:20px;color:var(--ink);margin-bottom:3px}
.ln{font-size:13.5px;color:var(--ink-2);line-height:1.3}

.brand{display:flex;align-items:center;gap:11px;color:var(--ink);flex:0 0 auto}
.brand b{font-family:'Cormorant Garamond',serif;font-weight:700;font-size:26px}
.brand .bdot{width:10px;height:10px;border-radius:50%%;background:var(--brick)}
.brand span{color:var(--taupe);font-size:16px}
</style></head><body>
<div class="card">
  <div class="seal">礼</div>
  <div class="eyebrow">Этикет</div>
  <h1>Как здороваются <i>китайцы</i></h1>
  <div class="sub">Жесту 拱手 больше двух тысяч лет. Рукопожатию в Китае — около ста</div>
  <div class="mid">
    <div class="cap"><b>Три эпохи</b> одного приветствия</div>
    <div class="rule"></div>
    <div class="brand"><span class="bdot"></span><b>Kitai School</b><span>&middot; kitai-school.ru</span></div>
  </div>
  <div class="film">
    <div class="perf">%s</div>
    <div class="strip">%s</div>
  </div>
</div>
</body></html>""" % (FONTS, VARS, "<i></i>" * 16, frames)

open(S + "zd-hero.html", "w", encoding="utf-8").write(hero)

# -------------------------------------------------------------- инфографика
info = """<!DOCTYPE html><html lang="ru"><head><meta charset="utf-8">
%s
<style>
%s
*{margin:0;box-sizing:border-box}html,body{width:1200px;height:HGTpx}
.wrap{width:1200px;height:HGTpx;background:linear-gradient(180deg,#fff 0%%,var(--cream) 46%%,var(--cream-2) 100%%);font-family:'Inter',sans-serif;padding:32px 46px 26px;display:flex;flex-direction:column}
.top{display:flex;align-items:flex-end;justify-content:space-between;gap:30px;margin-bottom:20px}
.eyebrow{color:var(--brick);font-weight:700;font-size:14.5px;letter-spacing:.17em;text-transform:uppercase;margin-bottom:7px}
h2{font-family:'Cormorant Garamond',serif;font-weight:600;font-size:41px;line-height:1.06;color:var(--ink);letter-spacing:-.3px}
h2 i{font-style:italic;color:var(--brick)}
.hint{flex:0 0 384px;background:var(--surface);border:1px solid var(--hair);border-left:4px solid var(--brick);border-radius:12px;padding:12px 17px;font-size:14.5px;color:var(--ink-2);line-height:1.36}
.hint b{color:var(--ink)}

.row{display:flex;gap:22px;align-items:stretch}
.cl{flex:1 1 0;background:var(--surface);border:1px solid var(--hair);border-radius:20px;padding:18px 20px 18px;box-shadow:0 8px 24px rgba(44,36,32,.07);display:flex;flex-direction:column;align-items:center;text-align:center}
.cl.bad{border-color:var(--brick);background:#FFFBFC}
.cap{font-size:12.5px;font-weight:700;letter-spacing:.11em;text-transform:uppercase;color:var(--taupe);margin-bottom:14px}
.cl.bad .cap{color:var(--brick)}

.dial{position:relative;width:218px;height:218px;border-radius:50%%;background:var(--cream);border:1px solid var(--hair);display:flex;align-items:center;justify-content:center;margin-bottom:15px}
.cl.bad .dial{background:var(--brick-soft);border-color:var(--brick)}
.palm{position:absolute;width:178px;height:178px;border-radius:50%%;border:18px solid var(--blue);border-right-color:transparent}
.cl.ok .palm{transform:rotate(-42deg)}
.cl.ok2 .palm,.cl.bad .palm{transform:rotate(222deg)}
.plab{position:absolute;top:84px;width:50px;height:50px;border-radius:50%%;background:#fff;border:2px solid var(--blue);display:flex;align-items:center;justify-content:center;font-family:'Noto Serif SC',serif;font-weight:700;font-size:25px;color:var(--blue)}
.cl.ok .plab{left:4px}
.cl.ok2 .plab,.cl.bad .plab{right:4px}
.fist{position:absolute;width:106px;height:106px;border-radius:50%%;background:var(--brick);display:flex;align-items:center;justify-content:center;box-shadow:0 0 0 7px #fff}
.fist b{font-family:'Noto Serif SC',serif;font-weight:700;font-size:40px;color:#fff}
.x{position:absolute;right:-8px;top:-8px;width:60px;height:60px;border-radius:50%%;background:#fff;border:6px solid var(--brick);box-shadow:0 0 0 5px #FFFBFC}
.x:after{content:"";position:absolute;left:3px;right:3px;top:50%%;margin-top:-3px;height:6px;border-radius:3px;background:var(--brick);transform:rotate(-45deg)}
.nt{font-size:15px;color:var(--ink-2);line-height:1.38;max-width:28ch}
.nt b{color:var(--ink)}
.cl.bad .nt b{color:var(--brick)}

.lgnd{display:flex;gap:30px;justify-content:center;margin-top:16px;font-size:14px;color:var(--ink-2)}
.lgnd i{display:inline-block;width:14px;height:14px;border-radius:50%%;margin-right:8px;vertical-align:-2px}
.lgnd .i1{background:var(--brick)}.lgnd .i2{background:var(--blue)}

.foot{margin-top:auto;display:flex;align-items:center;gap:18px}
.foot .msg{flex:1 1 auto;background:var(--brick-soft);border:1px solid var(--brick);border-radius:14px;padding:12px 21px;font-size:16px;color:var(--ink);line-height:1.34}
.foot .msg b{color:var(--brick)}
.brand{display:flex;align-items:center;gap:10px;color:var(--ink);flex:0 0 auto}
.brand b{font-family:'Cormorant Garamond',serif;font-weight:700;font-size:23px}
.brand .dot{width:9px;height:9px;border-radius:50%%;background:var(--brick)}
.brand span{color:var(--taupe);font-size:15px}
</style></head><body>
<div class="wrap">
  <div class="top">
    <div>
      <div class="eyebrow">拱手 — порядок рук</div>
      <h2>Один жест, два смысла: <i>приветствие или соболезнование</i></h2>
    </div>
    <div class="hint">Красный круг — <b>кулак</b>, синяя дуга — <b>ладонь, которая его накрывает</b>. Всё решает то, какая рука оказалась снаружи.</div>
  </div>

  <div class="row">
    <div class="cl ok">
      <div class="cap">Мужчина — приветствие</div>
      <div class="dial"><span class="palm"></span><span class="plab">左</span><span class="fist"><b>右</b></span></div>
      <div class="nt">Снаружи <b>левая</b> ладонь, правая сжата в кулак внутри</div>
    </div>
    <div class="cl ok2">
      <div class="cap">Женщина — приветствие</div>
      <div class="dial"><span class="palm"></span><span class="plab">右</span><span class="fist"><b>左</b></span></div>
      <div class="nt">Зеркально: снаружи <b>правая</b> ладонь, в кулаке левая</div>
    </div>
    <div class="cl bad">
      <div class="cap">Мужчина перепутал</div>
      <div class="dial"><span class="palm"></span><span class="plab">右</span><span class="fist"><b>左</b></span><span class="x"></span></div>
      <div class="nt">Тот же рисунок, что в женском приветствии, но у мужчины это <b>凶拜 — соболезнование</b></div>
    </div>
  </div>

  <div class="lgnd"><span><i class="i1"></i>рука в кулаке, внутри</span><span><i class="i2"></i>рука-ладонь, снаружи</span></div>

  <div class="foot">
    <div class="msg">Сомневаетесь в руках — сделайте <b>кивок</b>. Он уместен всегда и ничего не перепутает</div>
    <div class="brand"><span class="dot"></span><b>Kitai School</b><span>&middot; kitai-school.ru</span></div>
  </div>
</div>
</body></html>""" % (FONTS, VARS)

info = info.replace("HGT", "646")
open(S + "zd-info.html", "w", encoding="utf-8").write(info)
print("ok")
