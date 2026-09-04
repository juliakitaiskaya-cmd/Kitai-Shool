/**
 * Проверяет, помещается ли содержимое каждой страницы guide.html.
 *
 *   node check-fit.cjs
 *
 * Для каждой страницы печатает, сколько миллиметров свободно между последним
 * блоком и подвалом. Отрицательное значение — текст выехал за пределы полосы:
 * его надо сократить или перенести на соседнюю страницу.
 */
const path = require('path');
const { chromium } = require(process.env.PW_PATH || '/opt/node22/lib/node_modules/playwright');

(async () => {
  const browser = await chromium.launch({ args: ['--no-sandbox'] });
  const page = await browser.newPage();
  await page.goto('file://' + path.join(__dirname, 'guide.html'), { waitUntil: 'networkidle' });
  await page.evaluate(() => document.fonts.ready);

  const rows = await page.evaluate(() => {
    const mm = px => Math.round(px / (96 / 25.4));
    return [...document.querySelectorAll('.page')].map((pg, i) => {
      const foot = pg.querySelector('.runfoot');
      const blocks = [...pg.children].filter(c => !c.classList.contains('runfoot'));
      const last = blocks[blocks.length - 1].getBoundingClientRect();
      const limit = foot ? foot.getBoundingClientRect().top : pg.getBoundingClientRect().bottom;
      return { page: i + 1, free: mm(limit - last.bottom) };
    });
  });

  let bad = 0;
  for (const r of rows) {
    const ok = r.free >= 0;
    if (!ok) bad++;
    console.log(`  стр. ${String(r.page).padStart(2)} — ${ok ? 'свободно' : 'ПЕРЕПОЛНЕНИЕ'} ${r.free} мм`);
  }
  await browser.close();
  console.log(bad ? `\nстраниц с переполнением: ${bad}` : '\nвсё помещается');
  process.exit(bad ? 1 : 0);
})().catch(e => { console.error(e); process.exit(2); });
