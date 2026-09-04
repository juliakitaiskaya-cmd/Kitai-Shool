/**
 * Собирает презентацию «Китайский с нуля: план на первые 30 дней».
 *
 *   node build.cjs [--out kitajskij-s-nulya-30-dnej.pptx]
 *
 * Материал тот же, что в гайде content/guides/kitajskij-s-nulya-30-dnej,
 * разложенный на 15 слайдов 16:9. Шрифты взяты те, что есть в PowerPoint
 * у всех: Cambria в заголовках, Calibri в тексте.
 */
const path = require('path');
const PptxGenJS = require(process.env.PPTX_PATH ||
  '/tmp/claude-0/-home-user-Kitai-Shool/363ce274-d622-5f34-acb0-c9405171414d/scratchpad/node_modules/pptxgenjs');

const args = process.argv.slice(2);
const opt = (n, d) => { const i = args.indexOf('--' + n); return i === -1 ? d : args[i + 1]; };
const OUT = path.resolve(__dirname, opt('out', 'kitajskij-s-nulya-30-dnej.pptx'));

/* ---------- фирменные цвета и шрифты ---------- */
const INK = '2C2420', INK2 = '5A4F45', BRICK = 'A41E3A', TAUPE = '8B7D6B';
const CREAM = 'FAF7F2', WHITE = 'FFFFFF', HL = 'FCF6E2', PINK = 'F7E6EB';
const LINE = 'EAE3D8', SOFT = 'B8AC9C', GHOST = 'F1EAE0', INK_SOFT = '3B322C';
const HEAD = 'Cambria', BODY = 'Calibri';

const W = 13.33, H = 7.5, M = 0.75, CW = W - M * 2;

const pres = new PptxGenJS();
pres.layout = 'LAYOUT_WIDE';
pres.author = 'Kitai School';
pres.company = 'Kitai School';
pres.title = 'Китайский с нуля: план на первые 30 дней';

const shadow = () => ({ type: 'outer', color: INK, opacity: 0.07, blur: 14, offset: 0.05, angle: 90 });

/** белая карточка со скруглением */
function card(slide, x, y, w, h, fill = WHITE, border = LINE) {
  slide.addShape(pres.ShapeType.roundRect, {
    x, y, w, h, fill: { color: fill }, line: { color: border, width: 0.75 },
    rectRadius: 0.14, shadow: shadow()
  });
}

/** надпись-рубрика над содержимым карточки */
function eyebrow(slide, text, x, y, w, color = TAUPE) {
  slide.addText(text.toUpperCase(), {
    x, y, w, h: 0.26, isTextBox: true, margin: 0,
    fontFace: BODY, fontSize: 10, bold: true, charSpacing: 2, color
  });
}

/** сквозная нижняя строка */
function footer(slide, num) {
  slide.addText('Kitai School · kitai-school.ru', {
    x: M, y: 6.92, w: 6, h: 0.3, isTextBox: true, margin: 0,
    fontFace: BODY, fontSize: 10, color: SOFT
  });
  slide.addText(String(num), {
    x: W - M - 1, y: 6.92, w: 1, h: 0.3, isTextBox: true, margin: 0,
    fontFace: BODY, fontSize: 10, color: SOFT, align: 'right'
  });
}

/** светлый слайд с фоном и подвалом */
function page(num) {
  const s = pres.addSlide();
  s.background = { color: CREAM };
  if (num) footer(s, num);
  return s;
}

/** большой бледный иероглиф в углу */
function watermark(slide, ch) {
  slide.addText(ch, {
    x: 8.9, y: 1.1, w: 4.4, h: 5.2, isTextBox: true, margin: 0,
    fontFace: BODY, fontSize: 200, color: GHOST, align: 'center', valign: 'middle'
  });
}

/** шапка слайда-шага: номер, дни, заголовок */
function stephead(slide, n, days, title) {
  slide.addText(String(n), {
    x: M, y: 0.42, w: 1.1, h: 1.1, isTextBox: true, margin: 0,
    fontFace: HEAD, fontSize: 54, bold: true, italic: true, color: BRICK, valign: 'middle'
  });
  slide.addText(days.toUpperCase(), {
    x: M + 1.05, y: 0.5, w: 5, h: 0.28, isTextBox: true, margin: 0,
    fontFace: BODY, fontSize: 10.5, bold: true, charSpacing: 2, color: TAUPE
  });
  slide.addText(title, {
    x: M + 1.02, y: 0.74, w: 9.5, h: 0.75, isTextBox: true, margin: 0,
    fontFace: HEAD, fontSize: 30, bold: true, color: INK, valign: 'middle'
  });
}

/** ячейка таблицы с тонкой линией снизу */
const cell = (text, o = {}) => ({
  text,
  options: Object.assign({
    border: [{ type: 'none' }, { type: 'none' }, { type: 'solid', color: LINE, pt: 0.75 }, { type: 'none' }]
  }, o)
});
const headCell = text => ({
  text: text.toUpperCase(),
  options: {
    fontSize: 10, bold: true, charSpacing: 1.5, color: TAUPE,
    border: [{ type: 'none' }, { type: 'none' }, { type: 'solid', color: '#DED5C6'.slice(1), pt: 1 }, { type: 'none' }]
  }
});
const tableOpts = extra => Object.assign({
  fontFace: BODY, fontSize: 13.5, color: INK2, valign: 'middle',
  margin: [0.05, 0.12, 0.05, 0], border: { type: 'none' }
}, extra);

/* =======================================================================
   1. Титул
   ======================================================================= */
{
  const s = pres.addSlide();
  s.background = { color: INK };
  s.addText('汉语', {
    x: 8.6, y: 0.6, w: 4.6, h: 6.2, isTextBox: true, margin: 0,
    fontFace: BODY, fontSize: 190, color: INK_SOFT, align: 'center', valign: 'middle'
  });
  s.addImage({ path: path.join(__dirname, 'logo-light.png'), x: M, y: 0.62, w: 1.9, h: 0.76 });
  s.addText('Китайский с нуля:\nплан на первые 30 дней', {
    x: M, y: 2.25, w: 8.4, h: 2.1, isTextBox: true, margin: 0,
    fontFace: HEAD, fontSize: 42, bold: true, color: CREAM, lineSpacingMultiple: 1.06
  });
  s.addText('Семь шагов, задания на каждый день и понятная цель в конце месяца', {
    x: M, y: 4.45, w: 7.8, h: 0.6, isTextBox: true, margin: 0,
    fontFace: BODY, fontSize: 16, color: SOFT
  });
  s.addText([
    { text: 'Юлия Горяина', options: { bold: true, color: CREAM } },
    { text: '  ·  китаист, докторант Шаньдунского университета, основатель Kitai School', options: { color: TAUPE } }
  ], { x: M, y: 6.15, w: 10.5, h: 0.4, isTextBox: true, margin: 0, fontFace: BODY, fontSize: 12 });
  s.addNotes('Знакомство: кто я и о чём этот план. Главная мысль — за месяц язык не выучить, но можно перестать его бояться.');
}

/* =======================================================================
   2. Что будет через 30 дней
   ======================================================================= */
{
  const s = page(2);
  s.addText('Что будет через тридцать дней', {
    x: M, y: 0.55, w: 11, h: 0.8, isTextBox: true, margin: 0,
    fontFace: HEAD, fontSize: 34, bold: true, color: INK
  });

  const items = [
    ['Читаете', 'Прочитаете вслух любое китайское слово, записанное латинскими буквами.'],
    ['Слышите', 'Отличите слова, которые звучат одинаково, но сказаны с разной мелодией.'],
    ['Пишете и говорите', 'Напишете десять иероглифов от руки и расскажете о себе шестью фразами.']
  ];
  const cw = 3.72, gap = 0.34;
  items.forEach(([h, t], i) => {
    const x = M + i * (cw + gap);
    card(s, x, 1.65, cw, 2.5);
    s.addText(String(i + 1), {
      x: x + 0.32, y: 1.85, w: 0.8, h: 0.7, isTextBox: true, margin: 0,
      fontFace: HEAD, fontSize: 34, bold: true, italic: true, color: BRICK
    });
    s.addText(h, {
      x: x + 0.32, y: 2.6, w: cw - 0.64, h: 0.4, isTextBox: true, margin: 0,
      fontFace: BODY, fontSize: 15, bold: true, color: INK
    });
    s.addText(t, {
      x: x + 0.32, y: 3.0, w: cw - 0.64, h: 1.0, isTextBox: true, margin: 0,
      fontFace: BODY, fontSize: 13, color: INK2, lineSpacingMultiple: 1.15
    });
  });

  card(s, M, 4.45, CW, 2.1, PINK, 'EFD3DB');
  eyebrow(s, 'Чего честно ждать', M + 0.4, 4.72, 6);
  s.addText('Свободно вы не заговорите: за тридцать дней так не бывает ни в одном языке. Зато будет то, с чем можно спокойно идти дальше. Следующая понятная ступенька — первый уровень HSK, международного экзамена по китайскому. До него обычно доходят за несколько месяцев спокойных занятий.', {
    x: M + 0.4, y: 5.05, w: CW - 0.8, h: 1.3, isTextBox: true, margin: 0,
    fontFace: BODY, fontSize: 14, color: INK2, lineSpacingMultiple: 1.2
  });
  s.addNotes('Сразу снимаем завышенные ожидания: месяц даёт основу, а не свободную речь. И сразу показываем следующую цель, чтобы план не выглядел тупиковым.');
}

/* =======================================================================
   3. Как заниматься
   ======================================================================= */
{
  const s = page(3);
  s.addText('Как заниматься', {
    x: M, y: 0.55, w: 11, h: 0.8, isTextBox: true, margin: 0,
    fontFace: HEAD, fontSize: 34, bold: true, color: INK
  });

  card(s, M, 1.65, 5.75, 2.55);
  s.addText('30 минут', {
    x: M + 0.45, y: 1.95, w: 4.8, h: 0.9, isTextBox: true, margin: 0,
    fontFace: HEAD, fontSize: 44, bold: true, color: INK
  });
  s.addText('в день, шесть дней в неделю. Седьмой день — только повторяем, ничего нового.', {
    x: M + 0.45, y: 2.85, w: 4.85, h: 0.6, isTextBox: true, margin: 0,
    fontFace: BODY, fontSize: 14, color: INK2
  });
  s.addText('Двадцать минут каждый день дают больше, чем три часа в воскресенье.', {
    x: M + 0.45, y: 3.5, w: 4.85, h: 0.5, isTextBox: true, margin: 0,
    fontFace: BODY, fontSize: 14, bold: true, color: BRICK
  });

  card(s, M + 6.08, 1.65, 5.75, 2.55);
  eyebrow(s, 'Что приготовить', M + 6.5, 1.92, 4);
  s.addText([
    { text: 'тетрадь в клетку и карандаш', options: { bullet: true, breakLine: true } },
    { text: 'словарь в телефоне: Pleco или БКРС', options: { bullet: true, breakLine: true } },
    { text: 'стопку карточек или пачку стикеров', options: { bullet: true, breakLine: true } },
    { text: 'наушники и телефон — записывать свой голос', options: { bullet: true } }
  ], {
    x: M + 6.5, y: 2.3, w: 4.9, h: 1.7, isTextBox: true, margin: 0,
    fontFace: BODY, fontSize: 14, color: INK2, paraSpaceAfter: 8
  });

  card(s, M, 4.5, CW, 2.05, HL, 'EFE3C2');
  eyebrow(s, 'Правило седьмого дня', M + 0.4, 4.78, 6);
  s.addText('Достаёте карточки за неделю, вслух перечитываете свои фразы, переписываете два иероглифа, которые держатся хуже всех. Кажется, что день потрачен зря, но именно он и закрепляет выученное.', {
    x: M + 0.4, y: 5.12, w: CW - 0.8, h: 1.1, isTextBox: true, margin: 0,
    fontFace: BODY, fontSize: 14, color: INK2, lineSpacingMultiple: 1.2
  });
  s.addNotes('Главный аргумент занятия: регулярность важнее объёма. Седьмой день не пропускать — он держит всё остальное.');
}

/* =======================================================================
   4. Что за чем
   ======================================================================= */
{
  const s = page(4);
  s.addText('Что за чем', {
    x: M, y: 0.45, w: 11.5, h: 0.9, isTextBox: true, margin: 0,
    fontFace: HEAD, fontSize: 32, bold: true, color: INK, valign: 'middle'
  });
  s.addText('Семь шагов по дням. Каждый следующий опирается на предыдущий, поэтому порядок лучше не менять.', {
    x: M, y: 1.42, w: 9.5, h: 0.4, isTextBox: true, margin: 0,
    fontFace: BODY, fontSize: 14, color: INK2
  });

  const rows = [
    [headCell('Дни'), headCell('Чем занимаемся'), headCell('Что появится в итоге')],
    ...[
      ['1–3', 'Учимся читать латиницей', 'прочитаете вслух любое слово'],
      ['4–6', 'Слышим мелодию слова', 'отличите «маму» от «лошади»'],
      ['7–10', 'Первые 20 слов', 'слова, которые не забываются'],
      ['11–15', 'Как устроен иероглиф', 'напишете десять знаков от руки'],
      ['16–20', 'Первые фразы', 'скажете, спросите и возразите'],
      ['21–25', 'Слушаем и повторяем', 'поймёте короткий разговор на слух'],
      ['26–30', 'Собираем всё вместе', 'расскажете о себе шестью фразами']
    ].map(r => [cell(r[0], { bold: true, color: INK }), cell(r[1], { color: INK }), cell(r[2])])
  ];
  s.addTable(rows, tableOpts({ x: M, y: 1.85, w: CW, colW: [1.6, 4.6, 5.63], rowH: 0.58 }));
  s.addNotes('Показываем маршрут целиком, чтобы у слушателя была карта. Дальше идём по шагам.');
}

/* =======================================================================
   5. Шаг 1 — читаем латиницей
   ======================================================================= */
{
  const s = page(5);
  watermark(s, '汉');
  stephead(s, 1, 'Дни 1–3', 'Сначала научимся читать');

  s.addText('Китайские слова записывают не только иероглифами. Есть официальная запись латинскими буквами — пиньинь, с неё начинают все, включая китайских первоклассников.\n\nСлог устроен просто: начало, хвост и мелодия. Всего слогов чуть больше четырёхсот.', {
    x: M, y: 1.85, w: 4.9, h: 2.5, isTextBox: true, margin: 0,
    fontFace: BODY, fontSize: 14, color: INK2, lineSpacingMultiple: 1.2
  });

  card(s, M, 4.5, 4.9, 2.05, HL, 'EFE3C2');
  eyebrow(s, 'Задание', M + 0.35, 4.72, 3);
  s.addText('Прочитайте вслух двадцать слогов и запишите себя на телефон. Послушайте запись через день: звуки, которые вчера казались одинаковыми, станут разными.', {
    x: M + 0.35, y: 5.02, w: 4.2, h: 1.4, isTextBox: true, margin: 0,
    fontFace: BODY, fontSize: 13, color: INK2, lineSpacingMultiple: 1.15
  });

  card(s, 6.1, 1.75, 6.48, 4.8);
  eyebrow(s, 'Пять букв, которые чаще всего читают неверно', 6.5, 2.0, 5.8);
  const rows = [
    [headCell('Пишется'), headCell('Звучит как'), headCell('Не читается')],
    ...[
      ['qi', 'ци, мягко', '«ки»'],
      ['xie', 'сье', '«ксие»'],
      ['zhi', 'чжи, язык назад', '«зи»'],
      ['ri', 'жи с загнутым языком', '«ри»'],
      ['nü', 'нюй, губы трубочкой', '«ну»']
    ].map(r => [
      cell(r[0], { fontFace: HEAD, italic: true, bold: true, fontSize: 16, color: BRICK }),
      cell(r[1], { color: INK }),
      cell(r[2])
    ])
  ];
  s.addTable(rows, tableOpts({ x: 6.5, y: 2.4, w: 5.7, colW: [1.5, 2.5, 1.7], rowH: 0.62, fontSize: 13 }));
  s.addNotes('Разбираем звуки, которые русскому уху непривычны. Просим повторять вслух прямо на занятии.');
}

/* =======================================================================
   6. Шаг 2 — мелодия слова
   ======================================================================= */
{
  const s = page(6);
  stephead(s, 2, 'Дни 4–6', 'У каждого слова своя мелодия');

  s.addText('Одни и те же звуки, сказанные с разной мелодией, — это разные слова.', {
    x: M, y: 1.6, w: 9, h: 0.35, isTextBox: true, margin: 0,
    fontFace: BODY, fontSize: 15, color: INK2
  });

  const rows = [
    [headCell('Знак'), headCell('Читается'), headCell('Что делает голос'), headCell('Значение')],
    ...[
      ['妈', 'mā', 'ровно и высоко', 'мама'],
      ['麻', 'má', 'идёт вверх', 'конопля'],
      ['马', 'mǎ', 'вниз и обратно вверх', 'лошадь'],
      ['骂', 'mà', 'резко падает вниз', 'ругать']
    ].map(r => [
      cell(r[0], { fontSize: 20, color: INK }),
      cell(r[1], { fontFace: HEAD, italic: true, bold: true, fontSize: 17, color: BRICK }),
      cell(r[2], { color: INK }),
      cell(r[3])
    ])
  ];
  s.addTable(rows, tableOpts({ x: M, y: 1.95, w: CW, colW: [1.5, 2.0, 4.5, 3.83], rowH: 0.46 }));

  card(s, M, 5.0, 5.75, 1.6);
  eyebrow(s, 'На что это похоже', M + 0.35, 5.2, 4);
  s.addText([
    { text: 'ровно и высоко — как тянут «а-а-а» у врача;', options: { bullet: true, breakLine: true } },
    { text: 'вверх — как русское вопросительное «да?»;', options: { bullet: true, breakLine: true } },
    { text: 'вниз — как короткое «стой!».', options: { bullet: true } }
  ], {
    x: M + 0.35, y: 5.5, w: 5.1, h: 1.0, isTextBox: true, margin: 0,
    fontFace: BODY, fontSize: 12.5, color: INK2, paraSpaceAfter: 3
  });

  card(s, M + 6.08, 5.0, 5.75, 1.6, PINK, 'EFD3DB');
  eyebrow(s, 'Частая ошибка', M + 6.43, 5.2, 4);
  s.addText('Отложить мелодию на потом. Она не украшение, а часть слова: без неё вас не поймут, а переучиваться дольше, чем выучить сразу.', {
    x: M + 6.43, y: 5.5, w: 5.1, h: 1.0, isTextBox: true, margin: 0,
    fontFace: BODY, fontSize: 13, color: INK2, lineSpacingMultiple: 1.15
  });
  s.addNotes('Здесь стоит произнести все четыре слога вслух и попросить группу повторить хором. Мелодию объясняем голосом, а не словами.');
}

/* =======================================================================
   7. Шаг 3 — первые 20 слов
   ======================================================================= */
{
  const s = page(7);
  stephead(s, 3, 'Дни 7–10', 'Первые двадцать слов');

  s.addText('По пять слов в день. Каждое произносим вслух и сразу вставляем в короткую фразу.', {
    x: M, y: 1.6, w: 9, h: 0.35, isTextBox: true, margin: 0,
    fontFace: BODY, fontSize: 15, color: INK2
  });

  const half = (pairs) => [
    [headCell('Слово'), headCell('Читается'), headCell('Перевод')],
    ...pairs.map(r => [
      cell(r[0], { fontSize: 15, color: INK }),
      cell(r[1], { fontFace: HEAD, italic: true, bold: true, fontSize: 13, color: BRICK }),
      cell(r[2])
    ])
  ];
  const left = [['你好', 'nǐ hǎo', 'здравствуйте'], ['谢谢', 'xièxie', 'спасибо'], ['对不起', 'duìbuqǐ', 'извините'],
    ['我', 'wǒ', 'я'], ['你', 'nǐ', 'ты'], ['他', 'tā', 'он'], ['是', 'shì', 'быть'], ['不', 'bù', 'не'],
    ['有', 'yǒu', 'иметь'], ['好', 'hǎo', 'хороший']];
  const right = [['什么', 'shénme', 'что'], ['名字', 'míngzi', 'имя'], ['中国', 'Zhōngguó', 'Китай'],
    ['人', 'rén', 'человек'], ['老师', 'lǎoshī', 'учитель'], ['学生', 'xuésheng', 'ученик'],
    ['喝', 'hē', 'пить'], ['吃', 'chī', 'есть'], ['水', 'shuǐ', 'вода'], ['茶', 'chá', 'чай']];

  s.addTable(half(left), tableOpts({ x: M, y: 2.0, w: 5.6, colW: [1.5, 1.9, 2.2], rowH: 0.38, fontSize: 12 }));
  s.addTable(half(right), tableOpts({ x: M + 6.08, y: 2.0, w: 5.6, colW: [1.5, 1.9, 2.2], rowH: 0.38, fontSize: 12 }));
  s.addNotes('Двадцать слов — не для зубрёжки со слайда, а чтобы показать: набор маленький и посильный. Карточки повторяем трижды: сегодня, через три дня и через неделю. Список раздаём после занятия.');
}

/* =======================================================================
   8. Шаг 4 — иероглиф
   ======================================================================= */
{
  const s = page(8);
  stephead(s, 4, 'Дни 11–15', 'Иероглиф не рисуют, его собирают');

  s.addText('Сначала черты. Из черт складываются кусочки со своим смыслом, их называют ключами. А из кусочков — целый знак.', {
    x: M, y: 1.6, w: 11.5, h: 0.35, isTextBox: true, margin: 0,
    fontFace: BODY, fontSize: 15, color: INK2
  });

  card(s, M, 2.1, 5.75, 2.35);
  eyebrow(s, 'Смысл виден в частях', M + 0.35, 2.32, 4);
  s.addText([
    { text: '木', options: { fontSize: 30, color: INK } },
    { text: '  дерево   →   ', options: { fontSize: 13, color: TAUPE } },
    { text: '林', options: { fontSize: 30, color: INK } },
    { text: '  роща   →   ', options: { fontSize: 13, color: TAUPE } },
    { text: '森', options: { fontSize: 30, color: INK } },
    { text: '  лес', options: { fontSize: 13, color: TAUPE } }
  ], { x: M + 0.35, y: 2.72, w: 5.1, h: 0.6, isTextBox: true, margin: 0, fontFace: BODY, valign: 'middle' });
  s.addText([
    { text: '女', options: { fontSize: 26, color: INK } },
    { text: ' женщина  +  ', options: { fontSize: 13, color: TAUPE } },
    { text: '子', options: { fontSize: 26, color: INK } },
    { text: ' ребёнок  =  ', options: { fontSize: 13, color: TAUPE } },
    { text: '好', options: { fontSize: 26, color: BRICK } },
    { text: ' «хорошо»', options: { fontSize: 13, color: TAUPE } }
  ], { x: M + 0.35, y: 3.5, w: 5.1, h: 0.7, isTextBox: true, margin: 0, fontFace: BODY, valign: 'middle' });

  card(s, M + 6.08, 2.1, 5.75, 2.35);
  eyebrow(s, 'Куда вести руку', M + 6.43, 2.32, 4);
  s.addText([
    { text: 'сверху вниз и слева направо;', options: { bullet: true, breakLine: true } },
    { text: 'сначала горизонтальная черта, потом вертикальная;', options: { bullet: true, breakLine: true } },
    { text: 'сначала откидная влево, потом вправо;', options: { bullet: true, breakLine: true } },
    { text: 'рамка раньше того, что внутри, нижняя сторона — последней.', options: { bullet: true } }
  ], {
    x: M + 6.43, y: 2.72, w: 5.1, h: 1.55, isTextBox: true, margin: 0,
    fontFace: BODY, fontSize: 13, color: INK2, paraSpaceAfter: 4
  });

  card(s, M, 4.7, 5.75, 1.85, HL, 'EFE3C2');
  eyebrow(s, 'Задание на пять дней', M + 0.35, 4.92, 4.5);
  s.addText('Каждый день — два новых знака, по пять строчек в клетке. Пишете и вслух говорите, как читается.', {
    x: M + 0.35, y: 5.25, w: 5.1, h: 1.1, isTextBox: true, margin: 0,
    fontFace: BODY, fontSize: 13.5, color: INK2, lineSpacingMultiple: 1.15
  });

  card(s, M + 6.08, 4.7, 5.75, 1.85, PINK, 'EFD3DB');
  eyebrow(s, 'Частая ошибка', M + 6.43, 4.92, 4);
  s.addText('Срисовывать знак как картинку, начиная с любого места. Внешне получится похоже, но рука знак не запомнит.', {
    x: M + 6.43, y: 5.25, w: 5.1, h: 1.1, isTextBox: true, margin: 0,
    fontFace: BODY, fontSize: 13.5, color: INK2, lineSpacingMultiple: 1.15
  });
  s.addNotes('Хорошо показать порядок черт прямо на доске: 木 в четыре движения. Это запоминается лучше любого списка правил.');
}

/* =======================================================================
   9. Шаг 5 — первые фразы
   ======================================================================= */
{
  const s = page(9);
  stephead(s, 5, 'Дни 16–20', 'Первые фразы');

  s.addText('В китайском нет падежей, родов и спряжений. Слова не меняются — меняется их место во фразе. Порядок такой же, как в русском: кто — что делает — что.', {
    x: M, y: 1.6, w: 11.5, h: 0.35, isTextBox: true, margin: 0,
    fontFace: BODY, fontSize: 15, color: INK2
  });

  const rows = [
    [headCell('Фраза'), headCell('Читается'), headCell('Перевод и что запомнить')],
    ...[
      ['我喝茶', 'wǒ hē chá', 'Я пью чай. Тот самый порядок слов'],
      ['我不喝茶', 'wǒ bù hē chá', 'Я не пью чай. Отрицание 不 — перед действием'],
      ['你好吗？', 'nǐ hǎo ma', 'Как дела? Словечко 吗 в конце делает вопрос'],
      ['这是什么？', 'zhè shì shénme', 'Что это? Вопрос стоит там же, где будет ответ'],
      ['我很好', 'wǒ hěn hǎo', 'У меня всё хорошо. Здесь 是 не нужно']
    ].map(r => [
      cell(r[0], { fontSize: 17, color: INK }),
      cell(r[1], { fontFace: HEAD, italic: true, bold: true, fontSize: 14, color: BRICK }),
      cell(r[2])
    ])
  ];
  s.addTable(rows, tableOpts({ x: M, y: 2.0, w: CW, colW: [2.6, 2.8, 6.43], rowH: 0.45 }));

  card(s, M, 5.25, CW, 1.35);
  eyebrow(s, 'Две вещи, которые сэкономят месяцы', M + 0.4, 5.45, 6);
  s.addText('是 — это «быть кем-то или чем-то»: 我是学生, «я ученик». Перед словом, которое называет качество, она не нужна. А чтобы задать вопрос, ничего переставлять не надо: берём обычную фразу и добавляем в конец 吗.', {
    x: M + 0.4, y: 5.76, w: CW - 0.8, h: 0.75, isTextBox: true, margin: 0,
    fontFace: BODY, fontSize: 13, color: INK2, lineSpacingMultiple: 1.15
  });
  s.addNotes('Две ошибки, которые встречаются у всех: 是 перед прилагательным и перестановка слов в вопросе. Проговариваем их отдельно.');
}

/* =======================================================================
   10. Шаг 6 — слушаем
   ======================================================================= */
{
  const s = page(10);
  watermark(s, '听');
  stephead(s, 6, 'Дни 21–25', 'Слушаем и повторяем вслух');

  s.addText('К третьей неделе многие замечают неприятную вещь: глазами слово узнаёте, а на слух — нет. Лечится это только ежедневным слушанием с повторением вслух. Хватит десяти минут.', {
    x: M, y: 1.6, w: 11.3, h: 0.7, isTextBox: true, margin: 0,
    fontFace: BODY, fontSize: 15, color: INK2, lineSpacingMultiple: 1.15
  });

  const steps = [
    ['Первый раз', 'Просто слушаете полминуты, ничего не читая, и ловите знакомые слова.'],
    ['Второй раз', 'Слушаете и следите глазами по тексту. Сразу видно места, где ухо подвело.'],
    ['Третий раз', 'Говорите вместе с диктором, стараясь попасть в его скорость.']
  ];
  const cw = 3.72, gap = 0.34;
  steps.forEach(([h, t], i) => {
    const x = M + i * (cw + gap);
    card(s, x, 2.5, cw, 2.2);
    s.addText(String(i + 1), {
      x: x + 0.32, y: 2.68, w: 0.8, h: 0.6, isTextBox: true, margin: 0,
      fontFace: HEAD, fontSize: 30, bold: true, italic: true, color: BRICK
    });
    s.addText(h, {
      x: x + 0.32, y: 3.32, w: cw - 0.64, h: 0.35, isTextBox: true, margin: 0,
      fontFace: BODY, fontSize: 14.5, bold: true, color: INK
    });
    s.addText(t, {
      x: x + 0.32, y: 3.68, w: cw - 0.64, h: 0.9, isTextBox: true, margin: 0,
      fontFace: BODY, fontSize: 13, color: INK2, lineSpacingMultiple: 1.15
    });
  });

  card(s, M, 5.0, CW, 1.55, PINK, 'EFD3DB');
  eyebrow(s, 'Частая ошибка', M + 0.4, 5.2, 4);
  s.addText('Включать китайский фоном, между делом. Так ухо не учится: без внимания и без повторения вслух звук проходит мимо. Раз в пару дней записывайте себя и сравнивайте с оригиналом — по-другому ошибки в мелодии не заметить.', {
    x: M + 0.4, y: 5.52, w: CW - 0.8, h: 0.9, isTextBox: true, margin: 0,
    fontFace: BODY, fontSize: 13.5, color: INK2, lineSpacingMultiple: 1.15
  });
  s.addNotes('Полезно включить на занятии короткий диалог и пройти все три прослушивания вместе.');
}

/* =======================================================================
   11. Шаг 7 — собираем вместе
   ======================================================================= */
{
  const s = page(11);
  stephead(s, 7, 'Дни 26–30', 'Собираем всё вместе');

  s.addText('Последние пять дней — ничего нового. Складываем выученное в рассказ о себе и повторяем, пока он не пойдёт без запинки.', {
    x: M, y: 1.6, w: 11.3, h: 0.35, isTextBox: true, margin: 0,
    fontFace: BODY, fontSize: 15, color: INK2
  });

  const rows = [
    [headCell('Заготовка'), headCell('Читается'), headCell('Перевод')],
    ...[
      ['你好！', 'nǐ hǎo', 'Здравствуйте!'],
      ['我叫 ___。', 'wǒ jiào ___', 'Меня зовут ___.'],
      ['我是学生。', 'wǒ shì xuésheng', 'Я ученик.'],
      ['我学习汉语。', 'wǒ xuéxí Hànyǔ', 'Я учу китайский.'],
      ['我喜欢喝茶。', 'wǒ xǐhuan hē chá', 'Я люблю пить чай.'],
      ['认识你很高兴。', 'rènshi nǐ hěn gāoxìng', 'Приятно познакомиться.']
    ].map(r => [
      cell(r[0], { fontSize: 18, color: INK }),
      cell(r[1], { fontFace: HEAD, italic: true, bold: true, fontSize: 14, color: BRICK }),
      cell(r[2])
    ])
  ];
  s.addTable(rows, tableOpts({ x: M, y: 2.05, w: 7.4, colW: [2.7, 2.5, 2.2], rowH: 0.55, fontSize: 13 }));

  card(s, M + 7.75, 2.05, 4.08, 4.3);
  eyebrow(s, 'Проверьте себя', M + 8.1, 2.28, 3);
  s.addText([
    { text: 'читаю вслух незнакомое слово, записанное латиницей;', options: { bullet: true, breakLine: true } },
    { text: 'слышу мелодию слова;', options: { bullet: true, breakLine: true } },
    { text: 'пишу по памяти десять иероглифов;', options: { bullet: true, breakLine: true } },
    { text: 'говорю фразу, отрицание и вопрос;', options: { bullet: true, breakLine: true } },
    { text: 'рассказываю о себе шестью фразами.', options: { bullet: true } }
  ], {
    x: M + 8.1, y: 2.66, w: 3.4, h: 3.4, isTextBox: true, margin: 0,
    fontFace: BODY, fontSize: 13, color: INK2, paraSpaceAfter: 8
  });
  s.addNotes('Финальное задание месяца. Хорошо, если каждый расскажет о себе вслух прямо на занятии.');
}

/* =======================================================================
   12. Чек-лист
   ======================================================================= */
{
  const s = page(12);
  s.addText('Чек-лист на тридцать дней', {
    x: M, y: 0.45, w: 11.5, h: 0.9, isTextBox: true, margin: 0,
    fontFace: HEAD, fontSize: 32, bold: true, color: INK, valign: 'middle'
  });
  s.addText('Закрашивайте по одному. Пропустили день — закрашиваете следующий и продолжаете: один пропуск плана не рушит.', {
    x: M, y: 1.42, w: 10, h: 0.4, isTextBox: true, margin: 0,
    fontFace: BODY, fontSize: 14, color: INK2
  });

  const cols = 10, box = 1.02, gap = 0.16;
  const gridW = cols * box + (cols - 1) * gap;
  const x0 = (W - gridW) / 2;
  for (let i = 0; i < 30; i++) {
    const r = Math.floor(i / cols), c = i % cols;
    const x = x0 + c * (box + gap), y = 2.15 + r * (box + gap);
    s.addShape(pres.ShapeType.roundRect, {
      x, y, w: box, h: box, fill: { color: WHITE }, line: { color: 'DED5C6', width: 0.75 }, rectRadius: 0.1
    });
    s.addText(String(i + 1), {
      x: x + 0.08, y: y + 0.06, w: 0.5, h: 0.3, isTextBox: true, margin: 0,
      fontFace: BODY, fontSize: 11, color: TAUPE
    });
  }

  const marks = ['Дни 1–6 · читаем и слышим', 'Дни 7–15 · слова и знаки', 'Дни 16–25 · фразы и слух', 'Дни 26–30 · рассказ о себе'];
  s.addText(marks.join('     ·     '), {
    x: M, y: 5.75, w: CW, h: 0.4, isTextBox: true, margin: 0,
    fontFace: BODY, fontSize: 12.5, color: TAUPE, align: 'center'
  });

  s.addText('Эта же страница есть в гайде — её удобно распечатать и повесить на видное место.', {
    x: M, y: 6.25, w: CW, h: 0.36, isTextBox: true, margin: 0,
    fontFace: BODY, fontSize: 13, color: INK2, align: 'center'
  });
  s.addNotes('Раздаём распечатку чек-листа. Отмечать дни руками — простой и работающий способ не бросить.');
}

/* =======================================================================
   13. Пять причин, по которым бросают
   ======================================================================= */
{
  const s = page(13);
  s.addText('Пять причин, по которым бросают', {
    x: M, y: 0.45, w: 11.5, h: 0.9, isTextBox: true, margin: 0,
    fontFace: HEAD, fontSize: 32, bold: true, color: INK, valign: 'middle'
  });
  s.addText('За двадцать лет преподавания список почти не меняется. И ни одна причина не про способности.', {
    x: M, y: 1.42, w: 10, h: 0.4, isTextBox: true, margin: 0,
    fontFace: BODY, fontSize: 14, color: INK2
  });

  const items = [
    ['Учить слова без мелодии', '«Потом поставлю» не работает: мелодия — такая же часть слова, как звуки.'],
    ['Заниматься редко и помногу', 'Три часа в воскресенье проигрывают двадцати минутам каждый день.'],
    ['Зубрить списки слов', 'Слово, которое ни разу не стояло во фразе, в речи не всплывёт.'],
    ['Срисовывать иероглифы', 'Без правильного порядка рука не запоминает знак.'],
    ['Молчать', 'Произношение ставится только вслух и только когда кто-то поправляет.']
  ];
  const cw = 3.72, ch = 2.05, gap = 0.34;
  items.forEach(([h, t], i) => {
    const col = i % 3, row = Math.floor(i / 3);
    const x = M + col * (cw + gap), y = 1.95 + row * (ch + 0.3);
    card(s, x, y, cw, ch);
    s.addText(String(i + 1), {
      x: x + 0.3, y: y + 0.18, w: 0.6, h: 0.5, isTextBox: true, margin: 0,
      fontFace: HEAD, fontSize: 26, bold: true, italic: true, color: BRICK
    });
    s.addText(h, {
      x: x + 0.85, y: y + 0.25, w: cw - 1.15, h: 0.55, isTextBox: true, margin: 0,
      fontFace: BODY, fontSize: 14, bold: true, color: INK, valign: 'middle'
    });
    s.addText(t, {
      x: x + 0.3, y: y + 0.92, w: cw - 0.6, h: 0.95, isTextBox: true, margin: 0,
      fontFace: BODY, fontSize: 12.5, color: INK2, lineSpacingMultiple: 1.15
    });
  });
  s.addNotes('Этот слайд хорошо заходит вопросом в зал: кто узнал себя? Дальше показываем, что все пять лечатся режимом.');
}

/* =======================================================================
   14. Что дальше — HSK 1
   ======================================================================= */
{
  const s = page(14);
  s.addText('Следующая цель — первый уровень HSK', {
    x: M, y: 0.45, w: 11.9, h: 0.9, isTextBox: true, margin: 0,
    fontFace: HEAD, fontSize: 32, bold: true, color: INK, valign: 'middle'
  });
  s.addText('HSK — международный экзамен по китайскому. Первый уровень сдают уже после нескольких месяцев спокойных занятий.', {
    x: M, y: 1.42, w: 10.5, h: 0.4, isTextBox: true, margin: 0,
    fontFace: BODY, fontSize: 14, color: INK2
  });

  const stats = [['150', 'слов в программе'], ['2', 'части: слушаем и читаем'], ['120', 'баллов из 200 для зачёта']];
  const cw = 3.72, gap = 0.34;
  stats.forEach(([v, l], i) => {
    const x = M + i * (cw + gap);
    card(s, x, 2.05, cw, 1.95);
    s.addText(v, {
      x, y: 2.28, w: cw, h: 1.0, isTextBox: true, margin: 0,
      fontFace: HEAD, fontSize: 54, bold: true, color: BRICK, align: 'center'
    });
    s.addText(l, {
      x: x + 0.3, y: 3.28, w: cw - 0.6, h: 0.6, isTextBox: true, margin: 0,
      fontFace: BODY, fontSize: 13.5, color: INK2, align: 'center'
    });
  });

  card(s, M, 4.3, CW, 2.25);
  eyebrow(s, 'Что это даёт', M + 0.4, 4.55, 5);
  s.addText([
    { text: 'над иероглифами в заданиях напечатано чтение латиницей, поэтому читать вслепую не придётся;', options: { bullet: true, breakLine: true } },
    { text: 'письменной части на первом уровне нет, все задания с выбором ответа;', options: { bullet: true, breakLine: true } },
    { text: 'сертификат нужен для программ обмена и стипендий, а ещё он хорошо держит мотивацию.', options: { bullet: true } }
  ], {
    x: M + 0.4, y: 4.92, w: CW - 0.8, h: 1.5, isTextBox: true, margin: 0,
    fontFace: BODY, fontSize: 14, color: INK2, paraSpaceAfter: 8
  });
  s.addNotes('Даём слушателю понятную следующую ступень. Цифры по HSK 1 — по действующей редакции экзамена.');
}

/* =======================================================================
   15. Финал
   ======================================================================= */
{
  const s = pres.addSlide();
  s.background = { color: INK };
  s.addText('加油', {
    x: 8.4, y: 0.8, w: 4.8, h: 6.0, isTextBox: true, margin: 0,
    fontFace: BODY, fontSize: 170, color: INK_SOFT, align: 'center', valign: 'middle'
  });
  s.addText('Тридцать дней позади.\nДальше — интереснее', {
    x: M, y: 1.5, w: 8.2, h: 1.8, isTextBox: true, margin: 0,
    fontFace: HEAD, fontSize: 38, bold: true, color: CREAM, lineSpacingMultiple: 1.08
  });
  s.addText('Самое трудное в китайском — первый месяц, когда чужое всё сразу: и звуки, и знаки, и сама логика. Дальше знакомые части узнаются в новых иероглифах, а фразы собираются из того, что вы уже знаете.', {
    x: M, y: 3.4, w: 7.6, h: 1.2, isTextBox: true, margin: 0,
    fontFace: BODY, fontSize: 15, color: SOFT, lineSpacingMultiple: 1.2
  });
  s.addText([
    { text: 'Занятия с преподавателем — русским или китайским, по одному и в маленьких группах, от нуля до подготовки к экзамену.', options: { color: CREAM, breakLine: true } },
    { text: 'kitai-school.ru        Телеграм-канал @kitai_school', options: { color: 'D9BCC4', bold: true } }
  ], {
    x: M, y: 4.9, w: 7.6, h: 1.1, isTextBox: true, margin: 0,
    fontFace: BODY, fontSize: 14, paraSpaceAfter: 10
  });
  s.addImage({ path: path.join(__dirname, 'logo-light.png'), x: M, y: 6.2, w: 1.7, h: 0.68 });
  s.addNotes('Приглашение продолжить с преподавателем и контакты. Здесь же можно ответить на вопросы.');
}

pres.writeFile({ fileName: OUT }).then(() => console.log('готово: ' + OUT));
