# -*- coding: utf-8 -*-
# Картинки к статье «Китайские пословицы и поговорки»
# Обложка    — парные надписи у двери: пословица состоит из двух половин
# Инфографика — карточки лицом и оборотом: дословно и по смыслу
S = "/tmp/claude-0/-home-user-Kitai-Shool/a463bfca-82a9-56fd-ae09-42a7257ff999/scratchpad/"

FONTS = ("<link href=\"https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,600;0,700;1,600"
         "&family=Inter:wght@400;500;600;700&family=Noto+Serif+SC:wght@600;700&display=swap\" rel=\"stylesheet\">")
VARS = (":root{--brick:#A41E3A;--brick-d:#841630;--brick-soft:#F7E6EB;--ink:#2C2420;--ink-2:#5A4F45;"
        "--taupe:#8B7D6B;--cream:#FAF7F2;--cream-2:#F3EDE3;--hair:#EAE3D8;--surface:#fff;"
        "--green:#1E7A46;--amber:#C08A2E;--blue:#2F5D8C;--blue-s:#E7EEF6;"
        "--door:#7C5A3A;--door-2:#654728;--red:#B3243F;--red-2:#8E1730;--gold:#F0D9A8}")

LEFT = "路遥知马力"
RIGHT = "日久见人心"


def vert(text):
    return "".join('<span>%s</span>' % ch for ch in text)


hero = """<!DOCTYPE html><html lang="ru"><head><meta charset="utf-8">
%s
<style>
%s
*{margin:0;box-sizing:border-box}html,body{width:1200px;height:630px}
.card{width:1200px;height:630px;background:radial-gradient(1050px 660px at 16%% 12%%, #fff 0%%, var(--cream) 52%%, var(--cream-2) 100%%);position:relative;overflow:hidden;font-family:'Inter',sans-serif;padding:50px 56px 0 72px;display:flex;justify-content:space-between}
.card:before{content:"";position:absolute;left:0;top:0;bottom:0;width:12px;background:var(--brick)}
.txt{flex:0 0 520px;padding-top:6px}
.eyebrow{color:var(--brick);font-weight:700;font-size:18px;letter-spacing:.19em;text-transform:uppercase;margin-bottom:13px}
h1{font-family:'Cormorant Garamond',serif;font-weight:600;font-size:48px;line-height:1.06;color:var(--ink);letter-spacing:-.4px}
h1 i{font-style:italic;color:var(--brick)}
.sub{font-size:18.5px;color:var(--ink-2);line-height:1.42;max-width:32ch;margin-top:16px}
.note{display:inline-block;margin-top:22px;background:var(--surface);border:1px solid var(--hair);border-left:4px solid var(--brick);border-radius:13px;padding:13px 19px;font-size:15.5px;color:var(--ink-2);line-height:1.36;max-width:34ch}
.note b{color:var(--ink)}

/* дверь с парными надписями */
.gate{flex:0 0 492px;position:relative;height:500px;display:flex;align-items:flex-start;justify-content:center;gap:176px}
.door{position:absolute;left:112px;right:112px;top:26px;bottom:0;background:linear-gradient(170deg,var(--door),var(--door-2));border-radius:6px 6px 0 0;box-shadow:inset 0 0 40px rgba(0,0,0,.25), 0 14px 28px rgba(44,36,32,.18)}
.door:before{content:"";position:absolute;left:50%%;top:0;bottom:0;width:3px;margin-left:-1.5px;background:rgba(0,0,0,.32)}
.knob{position:absolute;top:46%%;width:34px;height:34px;border-radius:50%%;background:radial-gradient(circle at 34%% 32%%, #F3DCA8, #C08A2E);box-shadow:0 3px 7px rgba(0,0,0,.3)}
.knob.a{left:calc(50%% - 46px)}
.knob.b{left:calc(50%% + 12px)}
.scroll{position:relative;z-index:2;width:78px;min-height:384px;margin-top:10px;background:linear-gradient(180deg,var(--red),var(--red-2));border-radius:5px;box-shadow:0 10px 22px rgba(44,36,32,.26);display:flex;flex-direction:column;align-items:center;padding:20px 0 16px;gap:9px;border:1px solid rgba(0,0,0,.14)}
.scroll span{font-family:'Noto Serif SC',serif;font-weight:700;font-size:40px;color:#FFF6E2;line-height:1}
.scroll:after{content:"";position:absolute;left:12px;right:12px;top:8px;height:2px;background:rgba(255,246,226,.28)}
.half{position:absolute;bottom:-34px;left:50%%;transform:translateX(-50%%);font-size:13px;font-weight:700;font-style:normal;color:var(--brick);letter-spacing:.03em;white-space:nowrap;background:#fff;border:1px solid var(--hair);border-radius:8px;padding:4px 11px;box-shadow:0 3px 8px rgba(44,36,32,.1)}
.cap{position:absolute;left:0;right:0;bottom:-6px;text-align:center;font-size:15px;color:var(--ink-2);line-height:1.34}
.cap b{color:var(--ink)}
.brand{position:absolute;left:72px;bottom:28px;display:flex;align-items:center;gap:11px;color:var(--ink)}
.brand b{font-family:'Cormorant Garamond',serif;font-weight:700;font-size:26px}
.brand .bdot{width:10px;height:10px;border-radius:50%%;background:var(--brick)}
.brand span{color:var(--taupe);font-size:16px}
</style></head><body>
<div class="card">
  <div class="txt">
    <div class="eyebrow">Поговорки</div>
    <h1>Китайские пословицы <i>и поговорки</i></h1>
    <div class="sub">Народная пословица почти всегда состоит из двух половин: первая даёт образ, вторая — вывод</div>
    <div class="note"><b>路遥知马力，日久见人心:</b> дальняя дорога покажет лошадь, долгое время — человека</div>
  </div>
  <div class="gate">
    <div class="door"><span class="knob a"></span><span class="knob b"></span></div>
    <div class="scroll l">%s<i class="half">первая половина</i></div>
    <div class="scroll r">%s<i class="half">вторая половина</i></div>
  </div>
  <div class="brand"><span class="bdot"></span><b>Kitai School</b><span>&middot; kitai-school.ru</span></div>
</div>
</body></html>""" % (FONTS, VARS, vert(LEFT), vert(RIGHT))

hero = hero.replace("#C9A košice", "#C08A2E")
open(S + "pg-hero.html", "w", encoding="utf-8").write(hero)

# -------------------------------------------------------------- инфографика
CARDS = [
    ("远亲不如近邻", "yuǎnqīn bùrú jìnlín",
     "дальняя родня хуже близкого соседа",
     "в беде поможет тот, кто рядом, а не тот, кто дорог", "#A41E3A", "#F7E6EB"),
    ("吃一堑，长一智", "chī yí qiàn, zhǎng yí zhì",
     "съел один ров — вырастил один ум",
     "каждая неудача чему-то учит", "#2F5D8C", "#E7EEF6"),
    ("活到老，学到老", "huó dào lǎo, xué dào lǎo",
     "живёшь до старости — учишься до старости",
     "учиться поздно не бывает", "#1E7A46", "#E3F6E9"),
    ("三个臭皮匠，顶个诸葛亮", "sān ge chòu píjiàng, dǐng ge Zhūgě Liàng",
     "три плохоньких кожевника заменят Чжугэ Ляна",
     "вместе придумают лучше, чем один умник", "#C08A2E", "#FBF2DF"),
]

cards = "\n".join(
    '<div class="cd" style="border-color:%s">'
    '  <div class="face">'
    '    <div class="han">%s</div>'
    '    <div class="py">%s</div>'
    '    <div class="lit"><b>Дословно:</b> %s</div>'
    '  </div>'
    '  <div class="back" style="background:%s;border-color:%s">'
    '    <div class="bl" style="color:%s">Смысл</div>'
    '    <div class="bt">%s</div>'
    '  </div>'
    '</div>' % (col, han, py, lit, soft, col, col, mean)
    for han, py, lit, mean, col, soft in CARDS)

info = """<!DOCTYPE html><html lang="ru"><head><meta charset="utf-8">
%s
<style>
%s
*{margin:0;box-sizing:border-box}html,body{width:1200px;height:HGTpx}
.wrap{width:1200px;height:HGTpx;background:linear-gradient(180deg,#fff 0%%,var(--cream) 46%%,var(--cream-2) 100%%);font-family:'Inter',sans-serif;padding:32px 46px 26px;display:flex;flex-direction:column}
.top{display:flex;align-items:flex-end;justify-content:space-between;gap:30px;margin-bottom:20px}
.eyebrow{color:var(--brick);font-weight:700;font-size:14.5px;letter-spacing:.17em;text-transform:uppercase;margin-bottom:7px}
h2{font-family:'Cormorant Garamond',serif;font-weight:600;font-size:40px;line-height:1.07;color:var(--ink);letter-spacing:-.3px}
h2 i{font-style:italic;color:var(--brick)}
.hint{flex:0 0 360px;background:var(--surface);border:1px solid var(--hair);border-left:4px solid var(--brick);border-radius:12px;padding:12px 17px;font-size:14.5px;color:var(--ink-2);line-height:1.36}
.hint b{color:var(--ink)}

.rows{display:flex;flex-direction:column;gap:12px}
.cd{display:flex;align-items:stretch;gap:0;background:var(--surface);border:1px solid var(--hair);border-left-width:5px;border-radius:12px;box-shadow:0 5px 13px rgba(44,36,32,.06);overflow:hidden}
.face{flex:1 1 auto;padding:12px 20px;display:flex;align-items:center;gap:20px}
.face .han{font-family:'Noto Serif SC',serif;font-weight:700;font-size:26px;color:var(--ink);flex:0 0 300px;line-height:1.2}
.face .py{font-size:14px;color:var(--taupe);flex:0 0 246px;line-height:1.3}
.face .lit{flex:1 1 auto;font-size:14.5px;color:var(--ink-2);line-height:1.34}
.face .lit b{color:var(--ink)}
.back{flex:0 0 322px;border-left:1px dashed;padding:12px 20px;display:flex;flex-direction:column;justify-content:center}
.bl{font-size:12.5px;font-weight:700;text-transform:uppercase;letter-spacing:.1em;margin-bottom:4px}
.bt{font-size:15px;color:var(--ink);line-height:1.32;font-weight:500}

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
      <div class="eyebrow">Лицевая сторона и оборот</div>
      <h2>Дословно — <i>и что это значит</i></h2>
    </div>
    <div class="hint">Пословицу <b>нельзя переводить по словам</b>: дословное прочтение даёт картинку, а смысл приходится знать отдельно.</div>
  </div>

  <div class="rows">
%s
  </div>

  <div class="foot">
    <div class="msg">Поэтому и учат их целиком: <b>по частям пословица не собирается</b>, как не собирается из слов русское «не всё коту масленица»</div>
    <div class="brand"><span class="dot2"></span><b>Kitai School</b><span>&middot; kitai-school.ru</span></div>
  </div>
</div>
</body></html>""" % (FONTS, VARS, cards)

info = info.replace("HGT", "628")
open(S + "pg-info.html", "w", encoding="utf-8").write(info)
print("ok")
