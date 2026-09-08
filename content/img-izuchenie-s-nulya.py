# -*- coding: utf-8 -*-
S = "/tmp/claude-0/-home-user-Kitai-Shool/a463bfca-82a9-56fd-ae09-42a7257ff999/scratchpad/"

FONTS = ("<link href=\"https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,600;0,700;1,600"
         "&family=Inter:wght@400;500;600;700&family=Noto+Serif+SC:wght@600;700&display=swap\" rel=\"stylesheet\">")
VARS = (":root{--brick:#A41E3A;--brick-d:#841630;--brick-soft:#F7E6EB;--ink:#2C2420;--ink-2:#5A4F45;"
        "--taupe:#8B7D6B;--cream:#FAF7F2;--cream-2:#F3EDE3;--hair:#EAE3D8;--surface:#fff;"
        "--green:#1E7A46;--green-soft:#E3F6E9;--amber:#C08A2E;--amber-s:#FBF2DF;--blue:#2F5D8C;--blue-s:#E7EEF6}")

# ------------------------------------------------------------------ обложка
hero = """<!DOCTYPE html><html lang="ru"><head><meta charset="utf-8">
FONTS
<style>
VARS
*{margin:0;box-sizing:border-box}html,body{width:1200px;height:630px}
.card{width:1200px;height:630px;background:radial-gradient(1100px 700px at 82pc 16pc, #fff 0pc, var(--cream) 56pc, var(--cream-2) 100pc);display:flex;align-items:center;padding:0 56px 0 76px;position:relative;overflow:hidden;font-family:'Inter',sans-serif}
.card:before{content:"";position:absolute;left:0;top:0;bottom:0;width:12px;background:var(--brick)}
.seal{position:absolute;right:40px;top:26px;width:92px;height:92px;border:2.5px solid var(--brick);border-radius:14px;display:flex;align-items:center;justify-content:center;color:var(--brick);font-family:'Noto Serif SC',serif;font-weight:700;font-size:36px;opacity:.9}
.txt{flex:0 0 386px;max-width:386px}
.eyebrow{color:var(--brick);font-weight:700;font-size:19px;letter-spacing:.19em;text-transform:uppercase;margin-bottom:14px}
h1{font-family:'Cormorant Garamond',serif;font-weight:600;font-size:53px;line-height:1.04;color:var(--ink);letter-spacing:-.5px}
h1 i{font-style:italic;color:var(--brick)}
.sub{font-size:18.5px;color:var(--ink-2);line-height:1.42;max-width:22ch;margin-top:18px}
.brand{position:absolute;left:76px;bottom:34px;display:flex;align-items:center;gap:12px;color:var(--ink)}
.brand b{font-family:'Cormorant Garamond',serif;font-weight:700;font-size:28px}.brand .bdot{width:11px;height:11px;border-radius:50pc;background:var(--brick)}.brand span{color:var(--taupe);font-size:17px}

.art{flex:1 1 auto;position:relative;height:470px;display:flex;align-items:center}
.zero{position:absolute;left:8px;top:50pc;transform:translateY(-50pc);width:130px;height:130px;border-radius:50pc;background:var(--brick);color:#fff;display:flex;align-items:center;justify-content:center;font-family:'Cormorant Garamond',serif;font-weight:700;font-size:74px;box-shadow:0 10px 30px rgba(164,30,58,.28)}
.zero span{margin-top:-6px}
.zlab{position:absolute;left:8px;top:calc(50pc + 78px);width:130px;text-align:center;font-size:12.5px;font-weight:700;letter-spacing:.14em;text-transform:uppercase;color:var(--taupe)}
svg.lines{position:absolute;left:0;top:0;width:100pc;height:100pc}
.node{position:absolute;left:330px;width:300px;background:var(--surface);border:1px solid var(--hair);border-radius:16px;padding:13px 18px 15px;box-shadow:0 6px 20px rgba(44,36,32,.09)}
.node .k{display:flex;align-items:baseline;gap:9px}
.node .k b{font-family:'Cormorant Garamond',serif;font-size:25px;font-weight:700;color:var(--ink)}
.node .k i{font-style:normal;font-family:'Noto Serif SC',serif;font-size:19px;color:var(--brick)}
.node .d{font-size:13.5px;color:var(--ink-2);line-height:1.32;margin-top:5px}
.n1{top:24px}.n2{top:180px}.n3{top:336px}
.num{position:absolute;left:-15px;top:16px;width:30px;height:30px;border-radius:50pc;background:var(--brick);color:#fff;font-family:'Cormorant Garamond',serif;font-weight:700;font-size:18px;display:flex;align-items:center;justify-content:center;box-shadow:0 3px 10px rgba(164,30,58,.28)}
.wk{position:absolute;left:648px;top:180px;width:150px;font-size:13px;color:var(--taupe);line-height:1.3}
</style></head><body>
<div class="card"><div class="seal">零</div>
<div class="txt">
  <div class="eyebrow">С чего начать</div>
  <h1>Китайский <i>с нуля</i></h1>
  <div class="sub">Первая неделя — это три дела, и ни одно из них не про иероглифы</div>
</div>
<div class="art">
  <svg class="lines" viewBox="0 0 700 470" preserveAspectRatio="none">
    <path d="M138 235 C 232 235, 244 74, 330 74"   fill="none" stroke="#A41E3A" stroke-width="2.6" opacity=".7"/>
    <path d="M138 235 L 330 232"                    fill="none" stroke="#A41E3A" stroke-width="2.6" opacity=".7"/>
    <path d="M138 235 C 232 235, 244 386, 330 386"  fill="none" stroke="#A41E3A" stroke-width="2.6" opacity=".7"/>
  </svg>
  <div class="zero"><span>0</span></div>
  <div class="zlab">старт</div>
  <div class="node n1"><span class="num">1</span><div class="k"><b>Звук</b><i>声</i></div><div class="d">четыре тона на слух и пиньинь как правила чтения</div></div>
  <div class="node n2"><span class="num">2</span><div class="k"><b>Знак</b><i>字</i></div><div class="d">иероглифы вторым шагом, когда слова уже звучат</div></div>
  <div class="node n3"><span class="num">3</span><div class="k"><b>Фраза</b><i>话</i></div><div class="d">говорить вслух с первой недели, а не «когда выучу»</div></div>
</div>
<div class="brand"><span class="bdot"></span><b>Kitai School</b><span>&middot; kitai-school.ru</span></div></div>
</body></html>"""
hero = hero.replace("FONTS", FONTS).replace("VARS", VARS).replace("pc", "%")
open(S + "nul-hero.html", "w", encoding="utf-8").write(hero)

# ------------------------------------------------------------------ инфографика
info = """<!DOCTYPE html><html lang="ru"><head><meta charset="utf-8">
FONTS
<style>
VARS
*{margin:0;box-sizing:border-box}html,body{width:1200px;height:HEIGHTpx}
.wrap{width:1200px;height:HEIGHTpx;background:var(--cream);position:relative;overflow:hidden;font-family:'Inter',sans-serif;padding:20px 58px 16px 72px}
.wrap:before{content:"";position:absolute;left:0;top:0;bottom:0;width:14px;background:var(--brick)}
.top{display:flex;align-items:flex-end;justify-content:space-between;gap:24px}
.eyebrow{color:var(--brick);font-weight:700;font-size:16px;letter-spacing:.2em;text-transform:uppercase;margin-bottom:5px}
h2{font-family:'Cormorant Garamond',serif;font-weight:700;font-size:39px;color:var(--ink);line-height:1.02;letter-spacing:-.5px}
h2 i{font-style:italic;color:var(--brick)}
.hint{flex:0 0 320px;font-size:13.5px;color:var(--ink-2);line-height:1.34;border-left:3px solid var(--brick);padding-left:14px}
.hint b{color:var(--brick)}

.pair{display:flex;gap:22px;margin-top:20px}
.side{flex:1 1 0;background:#fff;border:1px solid var(--hair);border-radius:20px;padding:16px 22px 20px;box-shadow:0 5px 16px rgba(44,36,32,.06);position:relative}
.side.ok{border-color:var(--green)}
.side.no{border-color:var(--brick)}
.cap{font-size:12.5px;font-weight:700;letter-spacing:.14em;text-transform:uppercase;margin-bottom:3px}
.side.ok .cap{color:var(--green)}.side.no .cap{color:var(--brick)}
.side h3{font-family:'Cormorant Garamond',serif;font-weight:700;font-size:27px;color:var(--ink);line-height:1.05;margin-bottom:12px}

.loop{position:relative;height:214px}
.loop svg{position:absolute;left:0;top:0;width:100pc;height:100pc}
.st{position:absolute;width:132px;background:var(--cream);border:1.5px solid var(--hair);border-radius:12px;padding:8px 10px;text-align:center;font-size:13.5px;font-weight:600;color:var(--ink);line-height:1.2}
.st .s{display:block;font-size:11.5px;font-weight:500;color:var(--taupe);margin-top:2px}
.s1{left:calc(50pc - 66px);top:0}
.s2{right:4px;top:88px}
.s3{left:4px;top:88px}
.s4{left:calc(50pc - 66px);top:170px}
.side.ok .st{border-color:var(--green);background:var(--green-soft)}
.side.no .st.dead{border-color:var(--brick);background:var(--brick-soft);color:var(--brick)}
.gap{position:absolute;right:4px;top:88px;width:132px;border:1.5px dashed var(--brick);border-radius:12px;padding:8px 10px;text-align:center;font-size:13.5px;font-weight:700;color:var(--brick);line-height:1.2;background:#fff}
.gap .s{display:block;font-size:11.5px;font-weight:500;color:var(--brick);opacity:.8;margin-top:2px}

.list{margin-top:14px;padding-top:12px;border-top:1px solid var(--hair);display:flex;flex-wrap:wrap;gap:7px}
.chip{font-size:13.5px;font-weight:600;border-radius:999px;padding:6px 13px;line-height:1.2}
.side.ok .chip{background:var(--green-soft);color:var(--green)}
.side.no .chip{background:var(--brick-soft);color:var(--brick)}
.why{margin-top:11px;font-size:13.5px;color:var(--ink-2);line-height:1.34}
.why b{color:var(--ink)}

.foot{margin-top:16px;display:flex;align-items:center;gap:16px}
.foot .msg{flex:1 1 auto;background:var(--amber-s);border:1px solid var(--amber);border-radius:14px;padding:11px 20px;font-size:15.5px;color:var(--ink);line-height:1.34}
.foot .msg b{color:var(--brick)}
.brand{display:flex;align-items:center;gap:10px;color:var(--ink);flex:0 0 auto}
.brand b{font-family:'Cormorant Garamond',serif;font-weight:700;font-size:23px}.brand .dot{width:9px;height:9px;border-radius:50pc;background:var(--brick)}.brand span{color:var(--taupe);font-size:15px}
</style></head><body>
<div class="wrap">
  <div class="top">
    <div>
      <div class="eyebrow">Почему одно учится самому, а другое нет</div>
      <h2>Замкнутая петля <i>и разорванная</i></h2>
    </div>
    <div class="hint">Навык растёт там, где круг замыкается: <b>сделал — проверил — исправил</b>. Если проверить нечем, повторяется ошибка.</div>
  </div>

  <div class="pair">
    <div class="side ok">
      <div class="cap">Круг замыкается</div>
      <h3>Можно выучить самому</h3>
      <div class="loop">
        <svg viewBox="0 0 470 214">
          <path d="M330 40 C 400 52, 410 120, 372 150" fill="none" stroke="#1E7A46" stroke-width="2.4"/>
          <path d="M300 196 C 210 210, 110 208, 96 176" fill="none" stroke="#1E7A46" stroke-width="2.4"/>
          <path d="M96 62 C 110 32, 180 24, 236 30" fill="none" stroke="#1E7A46" stroke-width="2.4"/>
          <path d="M232 26 l 10 4 -10 4" fill="none" stroke="#1E7A46" stroke-width="2.4"/>
          <path d="M370 146 l -2 10 8 -4" fill="none" stroke="#1E7A46" stroke-width="2.4"/>
          <path d="M100 180 l -4 -9 9 2" fill="none" stroke="#1E7A46" stroke-width="2.4"/>
        </svg>
        <div class="st s1">Сделал<span class="s">написал, сказал, ответил</span></div>
        <div class="st s2">Проверил<span class="s">карточка, ключ, пропись</span></div>
        <div class="st s4">Увидел ошибку<span class="s">сразу, а не через год</span></div>
        <div class="st s3">Исправил<span class="s">и повторил уже верно</span></div>
      </div>
      <div class="list">
        <span class="chip">Лексика</span><span class="chip">Чтение</span><span class="chip">Порядок слов</span><span class="chip">Написание знаков</span><span class="chip">Понимание на слух</span>
      </div>
      <div class="why">У каждого из них есть <b>эталон, с которым можно сверить себя</b>: обратная сторона карточки, перевод текста, ответы к упражнению, пропись с порядком черт.</div>
    </div>

    <div class="side no">
      <div class="cap">Круг разорван</div>
      <h3>Самому не выучить</h3>
      <div class="loop">
        <svg viewBox="0 0 470 214">
          <path d="M330 40 C 400 52, 410 120, 372 150" fill="none" stroke="#A41E3A" stroke-width="2.4" stroke-dasharray="7 7" opacity=".5"/>
          <path d="M300 196 C 210 210, 110 208, 96 176" fill="none" stroke="#A41E3A" stroke-width="2.4" stroke-dasharray="7 7" opacity=".5"/>
          <path d="M96 62 C 110 32, 180 24, 236 30" fill="none" stroke="#A41E3A" stroke-width="2.4"/>
          <path d="M232 26 l 10 4 -10 4" fill="none" stroke="#A41E3A" stroke-width="2.4"/>
        </svg>
        <div class="st s1">Сказал<span class="s">тон, звук, живая фраза</span></div>
        <div class="gap">Проверить нечем<span class="s">эталона нет</span></div>
        <div class="st s4">Ошибки не видно<span class="s">слышен замысел</span></div>
        <div class="st dead s3">Закрепил ошибку<span class="s">каждый повтор — глубже</span></div>
      </div>
      <div class="list">
        <span class="chip">Тоны</span><span class="chip">Собственная речь</span>
      </div>
      <div class="why">Сверить себя не с чем: <b>вы слышите свой замысел, а не своё произношение</b>. Диктофон помогает наполовину — запись вы слушаете тем же ухом.</div>
    </div>
  </div>

  <div class="foot">
    <div class="msg">Отсюда рабочая схема: <b>занимаемся сами, а звук показываем живому человеку в первый же месяц</b> — пока ошибка не стала привычкой</div>
    <div class="brand"><span class="dot"></span><b>Kitai School</b><span>&middot; kitai-school.ru</span></div>
  </div>
</div>
</body></html>"""
info = info.replace("FONTS", FONTS).replace("VARS", VARS).replace("pc", "%").replace("HEIGHT", "700")
open(S + "nul-info.html", "w", encoding="utf-8").write(info)
print("ok")
