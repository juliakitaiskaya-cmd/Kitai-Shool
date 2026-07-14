/* Chrome.jsx — Kitai School marketing site header + footer */
function SiteHeader() {
  return (
    <header className="site-header">
      <div className="ks-wrap">
        <a href="#"><img src="../../assets/kitai-logo.svg" alt="Kitai School" /></a>
        <nav className="site-nav">
          <a href="#">Индивидуально</a>
          <a href="#">Группы</a>
          <a href="#">Бизнес-китайский</a>
          <a href="#">Подготовка к HSK</a>
          <a href="#">Поступление в Китай</a>
        </nav>
        <a className="tg-btn" href="#">Написать в Telegram</a>
      </div>
    </header>
  );
}

function SiteFooter() {
  return (
    <footer className="site-footer">
      <div className="ks-wrap">
        <div className="foot-brand">
          <div className="name">Kitai School</div>
          <div className="sub">Школа китайского языка<br />с 2005 года · EST · 2005 · MOSCOW</div>
        </div>
        <div>
          <h4>Контакты</h4>
          <a href="#">+7 (958) 538-70-80</a>
          <a href="#">info@kitai-school.ru</a>
          <a href="#">Telegram · @kitai_school</a>
          <a href="#">VK · vk.com/kitai_school</a>
        </div>
        <div>
          <h4>Лицензия</h4>
          <a href="#">№ Л035-01298-77/02285772</a>
          <a href="#">Департамент образования Москвы</a>
          <a href="#">Скачать PDF →</a>
        </div>
        <div className="foot-copy">© 2005–2026 Kitai School. Все права защищены. · Налоговый вычет 13% · Договор-оферта</div>
      </div>
    </footer>
  );
}

Object.assign(window, { SiteHeader, SiteFooter });
