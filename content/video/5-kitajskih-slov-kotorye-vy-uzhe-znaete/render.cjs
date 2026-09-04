/**
 * Рендер видео из video.html.
 *
 *   node render.cjs [--fps 30] [--out video.mp4] [--scale 1] [--frames-only]
 *
 * Сцена детерминированная: страница отдаёт window.setTime(t), скрипт
 * перематывает её кадр за кадром и отдаёт картинки прямо в ffmpeg.
 * Нужны playwright (chromium) и ffmpeg с libx264.
 */
const path = require('path');
const { spawn } = require('child_process');
const { chromium } = require(process.env.PW_PATH || '/opt/node22/lib/node_modules/playwright');

const args = process.argv.slice(2);
const opt = (name, def) => {
  const i = args.indexOf('--' + name);
  return i === -1 ? def : args[i + 1];
};

const FPS = parseInt(opt('fps', '30'), 10);
const SCALE = parseFloat(opt('scale', '1'));
const OUT = path.resolve(__dirname, opt('out', '5-kitajskih-slov-1080x1920.mp4'));
const PAGE = 'file://' + path.join(__dirname, 'video.html');
const W = 1080, H = 1920;

(async () => {
  const browser = await chromium.launch({
    args: ['--no-sandbox', '--font-render-hinting=none', '--force-color-profile=srgb']
  });
  const page = await browser.newPage({
    viewport: { width: W, height: H },
    deviceScaleFactor: SCALE
  });

  await page.goto(PAGE, { waitUntil: 'networkidle' });
  await page.evaluate(() => document.fonts.ready);
  await page.waitForTimeout(500);

  const duration = await page.evaluate(() => window.VIDEO_DURATION);
  const total = Math.round(duration * FPS);
  console.log(`длительность ${duration.toFixed(2)} c · ${total} кадров · ${FPS} fps`);

  const ff = spawn('ffmpeg', [
    '-y',
    '-f', 'image2pipe', '-framerate', String(FPS), '-i', '-',
    '-f', 'lavfi', '-i', 'anullsrc=channel_layout=stereo:sample_rate=44100',
    '-shortest',
    '-c:v', 'libx264', '-preset', 'slow', '-crf', '19',
    '-profile:v', 'high', '-level', '4.1', '-pix_fmt', 'yuv420p',
    '-r', String(FPS), '-movflags', '+faststart',
    '-c:a', 'aac', '-b:a', '96k',
    OUT
  ], { stdio: ['pipe', 'inherit', 'pipe'] });

  let ffErr = '';
  ff.stderr.on('data', d => { ffErr += d.toString(); });
  const done = new Promise((res, rej) => {
    ff.on('close', code => code === 0 ? res() : rej(new Error('ffmpeg ' + code + '\n' + ffErr.slice(-3000))));
  });

  const write = buf => new Promise(res => ff.stdin.write(buf) ? res() : ff.stdin.once('drain', res));

  for (let f = 0; f < total; f++) {
    const t = f / FPS;
    await page.evaluate(time => window.setTime(time), t);
    const buf = await page.screenshot({ type: 'jpeg', quality: 94 });
    await write(buf);
    if (f % 60 === 0) console.log(`  кадр ${f}/${total}  (${t.toFixed(1)} c)`);
  }

  ff.stdin.end();
  await done;
  await browser.close();
  console.log('готово: ' + OUT);
})().catch(e => { console.error(e); process.exit(1); });
