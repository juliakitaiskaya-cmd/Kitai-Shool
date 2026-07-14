/* Sidebar.jsx — fixed left icon navigation for the Kitai School learning platform.
   Outline icons (see Icons.jsx) per design-system update. */
const { useState } = React;

const KS_NAV = [
  { id: 'home',    icon: 'home',      label: 'Главная' },
  { id: 'lessons', icon: 'layers',    label: 'Уроки'   },
  { id: 'learn',   icon: 'book-open', label: 'Учить'   },
  { id: 'words',   icon: 'book',      label: 'Слова'   },
  { id: 'path',    icon: 'route',     label: 'Путь'    },
  { id: 'growth',  icon: 'trend',     label: 'Рост'    },
  { id: 'chat',    icon: 'chat',      label: 'Чат'     },
];

function Sidebar({ active, onNavigate }) {
  return (
    <nav className="ks-sidebar">
      <div className="ks-side-logo">启</div>
      <div className="ks-side-items">
        {KS_NAV.map(item => (
          <button
            key={item.id}
            className={'ks-side-item' + (active === item.id ? ' on' : '')}
            onClick={() => onNavigate(item.id)}
          >
            <span className="ks-side-ico"><Icon name={item.icon} size={20} /></span>
            <span className="ks-side-label">{item.label}</span>
          </button>
        ))}
      </div>
    </nav>
  );
}

Object.assign(window, { Sidebar, KS_NAV });
