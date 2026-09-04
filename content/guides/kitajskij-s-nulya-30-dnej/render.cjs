/**
 * Печатает guide.html в PDF.
 *
 *   node render.cjs [--out kitajskij-s-nulya-30-dnej.pdf]
 *
 * Страницы свёрстаны фиксированными блоками 210×297 мм, поля заданы внутри них,
 * поэтому у @page поля нулевые: chromium печатает ровно то, что видно в браузере.
 * Нужен playwright с chromium.
 */
const path = require('path');
const { chromium } = require(process.env.PW_PATH || '/opt/node22/lib/node_modules/playwright');

const args = process.argv.slice(2);
const opt = (name, def) => {
  const i = args.indexOf('--' + name);
  return i === -1 ? def : args[i + 1];
};

const OUT = path.resolve(__dirname, opt('out', 'kitajskij-s-nulya-30-dnej.pdf'));
const PAGE = 'file://' + path.join(__dirname, 'guide.html');

(async () => {
  const browser = await chromium.launch({ args: ['--no-sandbox'] });
  const page = await browser.newPage();
  await page.goto(PAGE, { waitUntil: 'networkidle' });
  await page.evaluate(() => document.fonts.ready);
  await page.emulateMedia({ media: 'print' });
  await page.pdf({
    path: OUT,
    format: 'A4',
    printBackground: true,
    preferCSSPageSize: true,
    margin: { top: 0, right: 0, bottom: 0, left: 0 }
  });
  await browser.close();
  console.log('готово: ' + OUT);
})().catch(e => { console.error(e); process.exit(1); });
