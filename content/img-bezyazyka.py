# -*- coding: utf-8 -*-
# Картинки к статье «Китайские вузы для русских студентов без знания языка»
# Обложка    — студенческий бейдж на ленте: язык обучения English, но 汉语 в плане
# Инфографика — выписка из приказа про англоязычный клинический бакалавриат
S = "/tmp/claude-0/-home-user-Kitai-Shool/a463bfca-82a9-56fd-ae09-42a7257ff999/scratchpad/"

FONTS = ("<link href=\"https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,600;0,700;1,600"
         "&family=Inter:wght@400;500;600;700&family=Noto+Serif+SC:wght@600;700&display=swap\" rel=\"stylesheet\">")
VARS = (":root{--brick:#A41E3A;--brick-d:#841630;--brick-soft:#F7E6EB;--ink:#2C2420;--ink-2:#5A4F45;"
        "--taupe:#8B7D6B;--cream:#FAF7F2;--cream-2:#F3EDE3;--hair:#EAE3D8;--surface:#fff;"
        "--green:#1E7A46;--green-soft:#E3F6E9;--amber:#C08A2E;--amber-s:#FBF2DF;--blue:#2F5D8C;--blue-s:#E7EEF6}")

# ------------------------------------------------------------------ обложка
hero = """<!DOCTYPE html><html lang="ru"><head><meta charset="utf-8">
%s
<style>
%s
*{margin:0;box-sizing:border-box}html,body{width:1200px;height:630px}
.card{width:1200px;height:630px;background:radial-gradient(1100px 680px at 16%% 8%%, #fff 0%%, var(--cream) 54%%, var(--cream-2) 100%%);position:relative;overflow:hidden;font-family:'Inter',sans-serif;display:flex;align-items:center;justify-content:space-between;padding:0 92px 0 72px}
.card:before{content:"";position:absolute;left:0;top:0;bottom:0;width:12px;background:var(--brick)}
.txt{flex:0 0 560px}
.eyebrow{color:var(--brick);font-weight:700;font-size:18px;letter-spacing:.19em;text-transform:uppercase;margin-bottom:12px}
h1{font-family:'Cormorant Garamond',serif;font-weight:600;font-size:48px;line-height:1.07;color:var(--ink);letter-spacing:-.4px;max-width:545px}
h1 i{font-style:italic;color:var(--brick)}
.sub{font-size:18px;color:var(--ink-2);line-height:1.42;max-width:33ch;margin-top:16px}
.counts{display:flex;gap:12px;margin-top:25px}
.cnt{background:var(--surface);border:1px solid var(--hair);border-radius:14px;padding:11px 15px;text-align:center;box-shadow:0 4px 14px rgba(44,36,32,.05)}
.cnt b{display:block;font-family:'Cormorant Garamond',serif;font-size:26px;font-weight:700;color:var(--brick);line-height:1.1}
.cnt b.han{font-family:'Noto Serif SC',serif;font-size:23px}
.cnt span{font-size:11.5px;color:var(--taupe);letter-spacing:.04em}
.brand{position:absolute;left:72px;bottom:32px;display:flex;align-items:center;gap:11px;color:var(--ink)}
.brand b{font-family:'Cormorant Garamond',serif;font-weight:700;font-size:26px}
.brand .bdot{width:10px;height:10px;border-radius:50%%;background:var(--brick)}
.brand span{color:var(--taupe);font-size:16px}

/* бейдж на ленте */
.hold{flex:0 0 300px;position:relative;height:630px}
.strap{position:absolute;top:0;width:17px;height:146px;background:linear-gradient(180deg,#8F1631,var(--brick));border-radius:0 0 3px 3px}
.strap.a{left:122px;transform:rotate(15deg);transform-origin:top center}
.strap.b{left:162px;transform:rotate(-15deg);transform-origin:top center}
.clip{position:absolute;top:145px;left:122px;width:56px;height:21px;background:linear-gradient(180deg,#D6CCBE,#B6A897);border-radius:5px;border:1px solid #A5967F}
.clip:after{content:"";position:absolute;left:19px;top:7px;width:18px;height:7px;border-radius:3px;background:var(--cream-2)}
.badge{position:absolute;top:164px;left:0;width:300px;background:var(--surface);border:1px solid var(--hair);border-radius:16px;overflow:hidden;box-shadow:0 18px 40px rgba(44,36,32,.18)}
.bh{background:var(--brick);color:#fff;padding:11px 16px;display:flex;align-items:center;justify-content:space-between}
.bh .en{font-size:11.5px;font-weight:700;letter-spacing:.2em}
.bh .cn{font-family:'Noto Serif SC',serif;font-weight:700;font-size:15px}
.bb{padding:16px}
.prow{display:flex;gap:13px;margin-bottom:14px}
.ph{flex:0 0 72px;height:88px;border:1.5px solid #D9CFC0;border-radius:6px;background:repeating-linear-gradient(135deg,#EFE8DC 0 6px,#F6F1E8 6px 12px)}
.lines{flex:1 1 auto;padding-top:6px}
.ln{height:7px;background:#E2D8C8;border-radius:3px;margin-bottom:9px}
.ln.s{width:66%%}.ln.m{width:88%%}.ln.l{width:76%%}
.lang{background:var(--blue-s);border:1px solid #C9D8E8;border-radius:10px;padding:9px 13px;display:flex;align-items:center;justify-content:space-between;margin-bottom:12px}
.lang .k{font-size:10.5px;letter-spacing:.11em;color:var(--taupe);font-weight:700}
.lang .v{font-size:19px;font-weight:700;color:var(--blue);letter-spacing:.04em}
.must{background:var(--brick-soft);border:1px solid var(--brick);border-radius:10px;padding:9px 13px}
.must .k{font-size:10px;letter-spacing:.11em;color:var(--brick);font-weight:700;margin-bottom:4px}
.must .v{font-family:'Noto Serif SC',serif;font-weight:700;font-size:17px;color:var(--ink)}
</style></head><body>
<div class="card">
  <div class="txt">
    <div class="eyebrow">Поступление</div>
    <h1>Китайские вузы <i>без знания языка</i></h1>
    <div class="sub">Поступить без китайского можно. Проучиться четыре года, не зная ни слова, — нет: он стоит в учебном плане</div>
    <div class="counts">
      <div class="cnt"><b>IELTS</b><span>ВМЕСТО HSK</span></div>
      <div class="cnt"><b class="han">汉语</b><span>ВСЁ РАВНО В ПЛАНЕ</span></div>
      <div class="cnt"><b>уже</b><span>ВЫБОР НАПРАВЛЕНИЙ</span></div>
    </div>
  </div>
  <div class="hold">
    <div class="strap a"></div>
    <div class="strap b"></div>
    <div class="clip"></div>
    <div class="badge">
      <div class="bh"><span class="en">STUDENT</span><span class="cn">留学生</span></div>
      <div class="bb">
        <div class="prow">
          <div class="ph"></div>
          <div class="lines"><div class="ln m"></div><div class="ln s"></div><div class="ln l"></div></div>
        </div>
        <div class="lang"><span class="k">ЯЗЫК ОБУЧЕНИЯ</span><span class="v">ENGLISH</span></div>
        <div class="must"><div class="k">ОБЯЗАТЕЛЬНЫЕ ПРЕДМЕТЫ</div><div class="v">汉语 · 中国概况</div></div>
      </div>
    </div>
  </div>
  <div class="brand"><span class="bdot"></span><b>Kitai School</b><span>&middot; kitai-school.ru</span></div>
</div>
</body></html>""" % (FONTS, VARS)

open(S + "bz-hero.html", "w", encoding="utf-8").write(hero)

# -------------------------------------------------------------- инфографика
ITEMS = [
    ("Набирать могут <b>только вузы из списка</b>", "Список публикует Минобразования КНР, и пересматривается он ежегодно."),
    ("На 2023/24 учебный год — <b>44 вуза и 3048 мест</b>", "Квоты распределяет министерство, а не сами университеты."),
    ("Срок обучения — <b>шесть лет</b>", "Китайский язык и медицинский китайский входят в обязательные предметы."),
    ("Остальным вузам — <b>запрещено</b>", "Ни набирать таких студентов, ни выдавать диплом с обозначением MBBS. Обход через «двуязычное обучение» запрещён отдельным пунктом."),
]
items = "\n".join(
    '<div class="it"><span class="no">%d</span><div><div class="t">%s</div><div class="d">%s</div></div></div>'
    % (i, t, d) for i, (t, d) in enumerate(ITEMS, 1))

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
.hint{flex:0 0 352px;background:var(--surface);border:1px solid var(--hair);border-left:4px solid var(--brick);border-radius:12px;padding:12px 17px;font-size:14.5px;color:var(--ink-2);line-height:1.36}
.hint b{color:var(--ink)}

.mid{flex:1 1 auto;display:flex;justify-content:center;align-items:flex-start}
.doc{position:relative;width:840px;background:#fff;border:1px solid var(--hair);border-radius:6px;padding:24px 34px 26px;box-shadow:0 12px 28px rgba(44,36,32,.11)}
.doc:before{content:"";position:absolute;left:0;right:0;top:0;height:5px;background:var(--brick);border-radius:6px 6px 0 0}
.dh{border-bottom:1.5px solid var(--hair);padding-bottom:13px;margin-bottom:17px}
.dh .k{font-size:11.5px;font-weight:700;letter-spacing:.22em;color:var(--brick);margin-bottom:6px}
.dh .t{font-family:'Cormorant Garamond',serif;font-weight:700;font-size:24px;color:var(--ink);line-height:1.2;max-width:600px}
.dh .s{font-size:13.5px;color:var(--taupe);margin-top:5px}
.it{display:flex;gap:14px;align-items:flex-start;padding:8px 0;border-bottom:1px dotted var(--hair)}
.it:last-child{border-bottom:0}
.no{flex:0 0 26px;width:26px;height:26px;border-radius:50%%;border:1.5px solid var(--brick);color:var(--brick);font-size:13px;font-weight:700;display:flex;align-items:center;justify-content:center;margin-top:2px}
.it .t{font-size:16px;color:var(--ink);line-height:1.34}
.it .t b{color:var(--brick)}
.it .d{font-size:14px;color:var(--ink-2);line-height:1.4;margin-top:3px;max-width:62ch}
.osn{margin-top:16px;padding-top:12px;border-top:1.5px solid var(--hair);font-size:13px;color:var(--taupe);line-height:1.4}
.osn b{color:var(--ink-2)}
.stamp{position:absolute;right:28px;top:26px;width:96px;height:96px;border:2.5px solid var(--brick);border-radius:50%%;display:flex;align-items:center;justify-content:center;transform:rotate(-13deg);opacity:.5}
.stamp:after{content:"";position:absolute;left:7px;right:7px;top:7px;bottom:7px;border:1px solid var(--brick);border-radius:50%%}
.stamp span{font-family:'Noto Serif SC',serif;font-weight:700;font-size:21px;color:var(--brick);text-align:center;line-height:1.15}

.foot{display:flex;align-items:center;gap:18px;padding-top:16px}
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
      <div class="eyebrow">Медицина на английском</div>
      <h2>Единственное направление, где <i>«на английском» прописано приказом</i></h2>
    </div>
    <div class="hint">У остальных англоязычных программ правила ставит <b>сам вуз</b>. Здесь — список вузов, квоты и обязательные предметы задаются сверху.</div>
  </div>

  <div class="mid">
    <div class="doc">
      <div class="dh">
        <div class="k">ВЫПИСКА</div>
        <div class="t">Клинический бакалавриат на английском языке для иностранных студентов</div>
        <div class="s">что установлено нормативно</div>
      </div>
%s
      <div class="osn">Основание: <b>«Временные правила контроля качества медицинского бакалавриата для иностранных студентов (обучение на английском языке)»</b>, Минобразования КНР, 教外来〔2007〕39号. Списки и квоты публикуются ежегодно.</div>
      <div class="stamp"><span>教育部</span></div>
    </div>
  </div>

  <div class="foot">
    <div class="msg">Цифры <b>44 и 3048</b> — на 2023/24 учебный год. Это последние подтверждённые данные, и каждый год они другие</div>
    <div class="brand"><span class="dot2"></span><b>Kitai School</b><span>&middot; kitai-school.ru</span></div>
  </div>
</div>
</body></html>""" % (FONTS, VARS, items)

info = info.replace("HGT", "804")
open(S + "bz-info.html", "w", encoding="utf-8").write(info)
print("ok")
