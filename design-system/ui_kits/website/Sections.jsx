/* Sections.jsx — Kitai School marketing-site sections */

function Hero() {
  return (
    <div className="ks-wrap">
      <div className="hero">
        <div>
          <span className="badge">Лицензия Департамента образования · 20 лет опыта</span>
          <h1>Научим говорить по‑китайски <span className="italic">уверенно</span> и свободно</h1>
          <p>Проверенная методика, собственная платформа и контроль качества каждого урока. Для взрослых и детей от 6 лет.</p>
          <div className="hero-cta">
            <a className="btn btn-primary" href="#">Записаться на диагностический урок</a>
            <a className="btn btn-ghost" href="#">Узнать стоимость</a>
          </div>
          <div className="hero-also">Также: <a href="#">Поступление в Китай</a> · <a href="#">Лагерь летом 2026</a></div>
        </div>
        <div className="hero-photo">
          <img src="../../assets/founder-yulia.jpg" alt="Юлия Горяина — основатель Kitai School" />
          <div className="hero-cap"><b>Юлия Горяина</b><span>Основатель Kitai School · с 2005 года</span></div>
        </div>
      </div>
    </div>
  );
}

const METHOD = [
  { n: 'I',  t: 'Структура каждого урока', d: 'Разминка, повторение, новый материал, отработка, рефлексия. Никакой импровизации — только система.', m: '5 этапов · 55 минут' },
  { n: 'II', t: 'Тренажёр HSK на платформе', d: '2292 слова уровней HSK 1–4, шесть режимов, проверка произношения через AI и интервальные повторения.', m: '2292 слова · 6 режимов · SRS' },
  { n: 'III',t: 'Контроль качества каждого урока', d: 'Каждое занятие оценивается методистом по 11 критериям. Слабые места исправляются сразу.', m: '11 критериев · после каждого урока' },
  { n: 'IV', t: 'Обратная связь после урока', d: 'Развёрнутый комментарий: что получилось, над чем работаем, какое домашнее задание.', m: 'персонально каждому ученику' },
];

function Methodology() {
  return (
    <div className="ks-wrap">
      <div className="eyebrow">Почему у нас получается</div>
      <h2 className="sec-title">Методика — не слово на сайте, а <span className="italic">система</span> на каждый день</h2>
      <p className="sec-lead">Курс ОДиН М — единственная комплексная методика преподавания китайского в России. Каждый элемент работает на ученика и каждый элемент проверяем.</p>
      <div className="method-grid">
        {METHOD.map(x => (
          <div className="method" key={x.n}>
            <div className="num">{x.n}</div>
            <h3>{x.t}</h3>
            <p>{x.d}</p>
            <div className="meta">{x.m}</div>
          </div>
        ))}
      </div>
    </div>
  );
}

function Stats() {
  return (
    <div className="ks-wrap">
      <div className="stats">
        <div className="stat"><div className="big">100%</div><div className="lab">учеников сдают<br />HSK с первого раза</div></div>
        <div className="stat"><div className="big">80%</div><div className="lab">приходят к нам<br />по рекомендациям</div></div>
        <div className="stat"><div className="big">20</div><div className="lab">лет развиваем<br />методику преподавания</div></div>
      </div>
    </div>
  );
}

const FORMATS = [
  { t: 'Индивидуально', tag: 'Под ваш график и темп', why: 'Когда нужен фокус на личных целях — экзамене, поступлении, бизнес-задаче.', li: ['Подбор преподавателя под цель','Любой темп: 1–3+ занятий в неделю','Программа под ваши задачи'], price: 'от 2 100 ₽', per: 'за урок', cta: 'Узнать стоимость →' },
  { t: 'В паре', tag: 'Учиться вдвоём дешевле', why: 'С другом, супругом или коллегой — общий ритм, взаимная мотивация.', li: ['Дешевле индивидуальных','Общий план и расписание','Подбор пары к вашему уровню'], price: '2 200 ₽', per: 'за урок · с человека', cta: 'Записаться →' },
  { t: 'В мини-группе', tag: '3–4 человека, баланс цены и качества', why: 'Когда важна разговорная практика с учениками одного уровня.', li: ['Группы по уровням и целям','Фиксированное расписание','Не более 4 человек'], price: '1 800 ₽', per: 'за урок · с человека', cta: 'Записаться →' },
  { t: 'Гибридный формат', tag: 'Платформа + живые занятия', why: 'Для самостоятельных — экономия времени и денег без потери качества.', li: ['Полный курс на платформе','Куратор проверяет ДЗ','2 живых урока за 3 месяца'], price: 'от 12 000 ₽', per: 'за 3 месяца', cta: 'Записаться →' },
];

function Formats() {
  return (
    <div className="ks-wrap">
      <div className="eyebrow">Форматы</div>
      <h2 className="sec-title">Подберём программу под ваш <span className="italic">ритм</span></h2>
      <p className="sec-lead">Четыре формата обучения. Выберите тот, который соответствует вашим целям и графику.</p>
      <div className="formats">
        {FORMATS.map(f => (
          <div className="fmt" key={f.t}>
            <h3>{f.t}</h3>
            <div className="tagline">{f.tag}</div>
            <div className="why">{f.why}</div>
            <ul>{f.li.map((l,i) => <li key={i}>{l}</li>)}</ul>
            <div className="price">{f.price}</div>
            <div className="per">{f.per}</div>
            <a className="btn btn-primary" href="#">{f.cta}</a>
          </div>
        ))}
      </div>
    </div>
  );
}

const CMP = [
  ['Методика', 'Курс Т.В. Иоффе с 30-летней практикой — единый стандарт для всех преподавателей', 'Стандартный учебник + личные эксперименты преподавателя'],
  ['Контроль', 'Система видит отставание и сразу подключает методиста', 'Контроль раз в семестр на родительском собрании'],
  ['Разбор урока', 'Анализ по 11 критериям, преподавателю дают точки роста', 'Завуч заходит на 1 урок в год'],
  ['Темп прогресса', 'HSK3 за 8–12 месяцев', 'Часто 2–3 года — а нет даже уверенного HSK2'],
  ['Гарантия', 'Лицензия, договор, гарантия результата, вычет 13%', 'Услуги без юридических гарантий'],
];

function Comparison() {
  return (
    <div className="ks-wrap">
      <div className="eyebrow">Что отличает нас</div>
      <h2 className="sec-title">Что отличает <span className="italic">Kitai School</span></h2>
      <p className="sec-lead">Не просто уроки китайского. А система контроля, методика с 30-летней практикой и платформа, которой нет ни у репетиторов, ни у обычных школ.</p>
      <div className="cmp">
        <div className="cmp-col us">
          <div className="cmp-head us">Kitai School<small>EST · 2005</small></div>
          {CMP.map((r,i) => <div className="cmp-row" key={i}><span className="k">{r[0]}</span>{r[1]}</div>)}
        </div>
        <div className="cmp-col them">
          <div className="cmp-head them">Обычное обучение<small>репетитор или средняя школа</small></div>
          {CMP.map((r,i) => <div className="cmp-row" key={i}><span className="k">{r[0]}</span>{r[2]}</div>)}
        </div>
      </div>
    </div>
  );
}

const TEAM = [
  { img: 'team-yulia.webp',   role: 'Основатель школы', name: 'Юлия Горяина', who: 'Преподаватель МГУ, китаист с 20-летним стажем', p: 'Создала Kitai School в 2005 году. Отбирает лучшие методики и лично контролирует стандарты качества.' },
  { img: 'team-tatyana.webp', role: 'Главный методист', name: 'Татьяна Иоффе', who: 'Преподаватель ОмГУ, китаист с 30-летним стажем', p: 'Автор курса ОДиН М — единственной комплексной методики преподавания китайского в России.' },
  { img: 'team-jenny.webp',   role: 'Операционный директор', name: 'Женни Рэй', who: 'Технологии и качество процессов', p: 'Отвечает за то, чтобы платформа, расписания, оплаты и связь работали безупречно.' },
];

function Team() {
  return (
    <div className="ks-wrap">
      <div className="eyebrow">Наша команда</div>
      <h2 className="sec-title"><span className="italic">Кто</span> стоит за Kitai School</h2>
      <p className="sec-lead">Преподаватели с педагогическим образованием, методисты с многолетним опытом, операционная команда.</p>
      <div className="team">
        {TEAM.map(m => (
          <div className="member" key={m.name}>
            <img src={'../../assets/' + m.img} alt={m.name} />
            <div className="role">{m.role}</div>
            <h3>{m.name}</h3>
            <div className="who">{m.who}</div>
            <p>{m.p}</p>
          </div>
        ))}
      </div>
    </div>
  );
}

function Quote() {
  return (
    <div className="ks-wrap">
      <div className="quote">
        <blockquote>Мы учим быстро и <span className="italic">эффективно</span>, потому что следуем сильной проверенной методике.</blockquote>
        <div className="who">Татьяна Иоффе · главный методист · автор курса · 30 лет в профессии</div>
      </div>
    </div>
  );
}

function FinalCTA() {
  return (
    <div className="ks-wrap">
      <div className="final">
        <div className="han">启</div>
        <h2>Готовы начать?</h2>
        <p>Запишитесь на бесплатный пробный урок — за 30 минут пройдём диагностику текущего уровня и подберём программу под ваши цели.</p>
        <div className="cta-row">
          <a className="btn btn-primary" href="#">Записаться на диагностический урок →</a>
          <a className="btn btn-ghost" href="#">или узнать стоимость</a>
        </div>
        <div className="note">Без обязательств. Решение о продолжении — после урока.</div>
      </div>
    </div>
  );
}

Object.assign(window, { Hero, Methodology, Stats, Formats, Comparison, Team, Quote, FinalCTA });
