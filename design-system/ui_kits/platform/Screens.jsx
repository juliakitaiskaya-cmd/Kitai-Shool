/* Screens.jsx — Kitai School platform screens: Header, Dashboard, Learn hub, Flashcard. */
const { useState: useStateS } = React;

/* ---------- shared greeting header ---------- */
function Header() {
  return (
    <div className="ks-header">
      <div>
        <h1 className="ks-greet">Привет, Анна!</h1>
        <div className="ks-greet-sub">Путь к HSK3</div>
      </div>
      <div className="ks-header-right">
        <button className="ks-support"><Icon name="help" size={16} /> Поддержка</button>
        <span className="ks-streak"><Icon name="flame" size={16} /> 1</span>
      </div>
    </div>
  );
}

/* ---------- DASHBOARD (Главная) ---------- */
function Dashboard() {
  return (
    <div className="ks-screen">
      <Header />

      <div className="ks-card ks-pad">
        <div className="ks-card-title"><Icon name="family" size={19} style={{color:'var(--brick)'}} /> Доступ для родителей</div>
        <p className="ks-card-text">Сгенерируйте ссылку для родителей. Они увидят расписание, прогресс и ДЗ — но не чат и не тренажёр.</p>
        <button className="ks-btn ks-btn-soft">Создать ссылку</button>
      </div>

      <div className="ks-card ks-pad">
        <div className="ks-card-title"><Icon name="bell" size={19} style={{color:'var(--brick)'}} /> Telegram-уведомления</div>
        <p className="ks-card-text">Получайте напоминания об уроках, ДЗ и сообщениях в чате прямо в Telegram.</p>
        <button className="ks-btn ks-btn-soft">Подключить Telegram</button>
      </div>

      <div className="ks-goal">
        <div className="ks-goal-ring">4/5</div>
        <div>
          <div className="ks-goal-title">Ежедневная цель</div>
          <div className="ks-goal-sub">Выучи ещё 1 слово</div>
        </div>
      </div>

      <div className="ks-tiles">
        <div className="ks-tile"><div className="ks-tile-ico"><Icon name="book" size={22} /></div><div className="ks-tile-num">612 / 1289</div><div className="ks-tile-cap">слова</div></div>
        <div className="ks-tile"><div className="ks-tile-ico"><Icon name="layers" size={22} /></div><div className="ks-tile-num">38 / 102</div><div className="ks-tile-cap">уроки</div></div>
        <div className="ks-tile"><div className="ks-tile-ico"><Icon name="target" size={22} /></div><div className="ks-tile-num">78%</div><div className="ks-tile-cap">точность</div></div>
      </div>

      <div className="ks-eyebrow ks-section-label">Ближайший урок</div>
      <div className="ks-card ks-pad ks-lesson-row">
        <div>
          <div className="ks-card-title" style={{marginBottom:4}}>HSK3 · Урок 39</div>
          <div className="ks-card-text" style={{margin:0}}>Завтra, 18:00 · Конструкция 把</div>
        </div>
        <button className="ks-btn ks-btn-primary">К уроку</button>
      </div>
    </div>
  );
}

/* ---------- LEARN hub (Учить) ---------- */
const KS_MODES = [
  { icon: 'cards',   title: 'Карточки',     hint: 'ПОМНЮ / НЕ ПОМНЮ',     opens: true },
  { icon: 'edit',    title: 'Заполни\nпропуск', hint: 'ВЫБЕРИ СЛОВО' },
  { icon: 'shuffle', title: 'Порядок\nслов',  hint: 'СОБЕРИ ПРЕДЛОЖЕНИЕ' },
  { icon: 'message', title: 'Диалог',        hint: 'КОНТЕКСТ' },
  { icon: 'brush',   title: 'Написание',     hint: 'ПОРЯДОК ЧЕРТ' },
];

function Learn({ onOpenCard }) {
  return (
    <div className="ks-screen">
      <Header />

      <div className="ks-card ks-pad ks-progress">
        <div className="ks-progress-bar"><span style={{width:'47%'}}></span></div>
        <div className="ks-progress-row">
          <div><b className="ks-progress-num">612</b> <span className="ks-muted">/ 1289 слов</span></div>
          <b className="ks-progress-pct">47%</b>
        </div>
        <div className="ks-legend">
          <span><i className="d g"></i>выучено 612</span>
          <span><i className="d y"></i>повторяю 187</span>
          <span><i className="d r"></i>учу 64</span>
          <span><i className="d n"></i>новые 426</span>
        </div>
      </div>

      <div className="ks-chip-row">
        <span className="ks-chip"><i className="ks-chip-dot"></i>Пиньинь</span>
        <span className="ks-chip"><i className="ks-chip-dot"></i>Перевод</span>
      </div>

      <div className="ks-search"><span className="ks-search-ico"><Icon name="search" size={18} /></span> Поиск слова: <span className="ks-han">汉字</span>, pinyin или перевод…</div>

      <div className="ks-modes">
        {KS_MODES.map((m,i) => (
          <button key={i} className="ks-mode" onClick={() => m.opens && onOpenCard()}>
            <span className="ks-mode-ico"><Icon name={m.icon} size={24} /></span>
            <span className="ks-mode-title">{m.title}</span>
            <span className="ks-mode-hint">{m.hint}</span>
          </button>
        ))}
      </div>

      <button className="ks-accordion">▸ Карта прогресса (все слова)</button>
    </div>
  );
}

/* ---------- FLASHCARD / pronunciation ---------- */
function Flashcard({ onBack }) {
  const [graded, setGraded] = useStateS(false);
  return (
    <div className="ks-screen ks-flash-screen">
      <div className="ks-flash-top">
        <button className="ks-round" onClick={onBack}><Icon name="arrow-left" size={17} /></button>
        <button className="ks-round"><Icon name="home" size={17} /></button>
        <span className="ks-counter">4<br/>/<br/>10</span>
        <span className="ks-flash-mode"><Icon name="cards" size={15} style={{display:'inline-block',verticalAlign:'-2px',marginRight:5}} /> Карточки</span>
      </div>

      <div className="ks-flash-card">
        <button className="ks-round ks-audio"><Icon name="volume" size={16} /></button>
        <div className="ks-flash-han">或者</div>
        <div className="ks-flash-pin">huò zhě</div>
        <div className="ks-flash-mean">или, возможно, или (в утвердительных предложениях)</div>
        <div className="ks-flash-tag">HSK3 · Урок 3</div>

        {graded && (
          <div className="ks-flash-grade">
            <div className="ks-tone-row">
              <span className="ks-tone">或者<sub>或 78%</sub></span>
              <span className="ks-tone">或者<sub>者 72%</sub></span>
            </div>
            <div className="ks-tone-score">Общая оценка: 75/100</div>
            <div className="ks-highlight">Хорошо! Тон в первом слоге 或 уже близок — попробуйте ещё резче, как команда «Стоп!». Во втором слоге 者 — голос ныряет вниз и снова вверх.</div>
            <button className="ks-btn ks-btn-soft ks-again"><Icon name="mic" size={15} /> Ещё раз</button>
          </div>
        )}

        <div className="ks-flash-example">
          苹果或者橘子 <button className="ks-round ks-sm"><Icon name="volume" size={13} /></button>
          <div className="ks-muted">Яблоки или апельсины</div>
        </div>
      </div>

      <div className="ks-flash-actions">
        <button className="ks-btn ks-btn-soft" onClick={onBack}>Сложно</button>
        <button className="ks-btn ks-btn-ghost" onClick={() => setGraded(true)}>Повтор</button>
        <button className="ks-btn ks-btn-success" onClick={onBack}>Знаю</button>
      </div>
    </div>
  );
}

Object.assign(window, { Header, Dashboard, Learn, Flashcard });
