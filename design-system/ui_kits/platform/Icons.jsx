/* Icons.jsx — Kitai School platform outline icon set.
   Linear SVGs (Lucide-style, stroke=currentColor 1.75) replacing the old emoji.
   Usage: <Icon name="home" /> — size via CSS on the wrapping element's font-size? no:
   each svg is 1em-agnostic; we size with width/height props (default 20). */

function Icon({ name, size = 20, stroke = 1.75, style }) {
  const p = {
    width: size, height: size, viewBox: '0 0 24 24', fill: 'none',
    stroke: 'currentColor', strokeWidth: stroke, strokeLinecap: 'round',
    strokeLinejoin: 'round', style: { display: 'block', ...style },
  };
  switch (name) {
    case 'home':    return <svg {...p}><path d="M3 10.5 12 3l9 7.5"/><path d="M5 9.5V20a1 1 0 0 0 1 1h12a1 1 0 0 0 1-1V9.5"/><path d="M9.5 21v-6h5v6"/></svg>;
    case 'layers':  return <svg {...p}><path d="m12 3 9 4.5-9 4.5-9-4.5L12 3Z"/><path d="m3 12 9 4.5L21 12"/><path d="m3 16.5 9 4.5 9-4.5"/></svg>;
    case 'book-open': return <svg {...p}><path d="M12 6.5C10.5 5 8 4.5 4 4.8V18c4-.3 6.5.2 8 1.7 1.5-1.5 4-2 8-1.7V4.8c-4-.3-6.5.2-8 1.7Z"/><path d="M12 6.5v13.2"/></svg>;
    case 'book':    return <svg {...p}><path d="M6 3h11a1 1 0 0 1 1 1v15.5a.5.5 0 0 1-.5.5H7a2 2 0 0 1-2-2V4a1 1 0 0 1 1-1Z"/><path d="M5 17.5A2 2 0 0 1 7 16h11"/></svg>;
    case 'route':   return <svg {...p}><circle cx="6" cy="19" r="2.5"/><circle cx="18" cy="5" r="2.5"/><path d="M8.5 19H14a3.5 3.5 0 0 0 0-7h-4a3.5 3.5 0 0 1 0-7h5.5"/></svg>;
    case 'trend':   return <svg {...p}><path d="M3 17l6-6 4 4 8-8"/><path d="M17 7h4v4"/></svg>;
    case 'chat':    return <svg {...p}><path d="M20 12a7.5 7.5 0 0 1-10.8 6.7L4 20l1.3-5.2A7.5 7.5 0 1 1 20 12Z"/></svg>;
    case 'target':  return <svg {...p}><circle cx="12" cy="12" r="8.5"/><circle cx="12" cy="12" r="4.5"/><circle cx="12" cy="12" r="1"/></svg>;
    case 'cards':   return <svg {...p}><rect x="3" y="7" width="13" height="13" rx="2"/><path d="M8 4h9a2 2 0 0 1 2 2v9"/></svg>;
    case 'edit':    return <svg {...p}><path d="M4 20h4l10-10a2 2 0 0 0-3-3L5 17v3Z"/><path d="M13.5 6.5l3 3"/></svg>;
    case 'shuffle': return <svg {...p}><path d="M16 4h4v4"/><path d="M20 4 4 20"/><path d="M16 20h4v-4"/><path d="m15 15 5 5"/><path d="M4 4l5 5"/></svg>;
    case 'message': return <svg {...p}><path d="M5 5h14a1 1 0 0 1 1 1v9a1 1 0 0 1-1 1H9l-4 4V6a1 1 0 0 1 1-1Z"/></svg>;
    case 'brush':   return <svg {...p}><path d="M15 4 8.5 10.5a3 3 0 0 0 0 4.2L13 19l5-5a3 3 0 0 0 0-4.2L15 4Z" transform="rotate(45 13 12)"/><path d="M6 16c-2 .5-3 2-3 4 2 0 3.5-1 4-3"/></svg>;
    case 'family':  return <svg {...p}><circle cx="8" cy="8" r="3"/><circle cx="16.5" cy="9" r="2.5"/><path d="M2.5 20c0-3 2.5-5 5.5-5s5.5 2 5.5 5"/><path d="M15 15c2.8 0 5 1.8 5 5"/></svg>;
    case 'bell':    return <svg {...p}><path d="M6 9a6 6 0 0 1 12 0c0 5 2 6 2 6H4s2-1 2-6Z"/><path d="M10 19a2 2 0 0 0 4 0"/></svg>;
    case 'flame':   return <svg {...p}><path d="M12 3c1 3-1.5 4-1.5 6.5a1.5 1.5 0 0 0 3 0c0-.5 0-1-.3-1.5 2 1.3 3.3 3.4 3.3 5.8a6.5 6.5 0 0 1-13 0C3.5 10 7 7 8 4.5c.7 1.5 2 2 2.5 3 .8-1.6.8-3 1.5-4.5Z"/></svg>;
    case 'help':    return <svg {...p}><circle cx="12" cy="12" r="9"/><path d="M9.3 9.3a2.7 2.7 0 0 1 5.2 1c0 1.8-2.7 2.3-2.7 4"/><path d="M12 17.5v.01"/></svg>;
    case 'search':  return <svg {...p}><circle cx="11" cy="11" r="7"/><path d="m20 20-3.5-3.5"/></svg>;
    case 'volume':  return <svg {...p}><path d="M4 9.5h3L12 5v14l-5-4.5H4Z"/><path d="M16 9a4 4 0 0 1 0 6"/><path d="M18.5 6.5a7 7 0 0 1 0 11"/></svg>;
    case 'mic':     return <svg {...p}><rect x="9" y="3" width="6" height="11" rx="3"/><path d="M5 11a7 7 0 0 0 14 0"/><path d="M12 18v3"/></svg>;
    case 'arrow-left': return <svg {...p}><path d="M19 12H5"/><path d="m11 6-6 6 6 6"/></svg>;
    default: return <svg {...p}><circle cx="12" cy="12" r="9"/></svg>;
  }
}

Object.assign(window, { Icon });
