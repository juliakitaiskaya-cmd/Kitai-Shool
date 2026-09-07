# -*- coding: utf-8 -*-
import re, io

B = "https://kitai-school.ru/article/"

SECTIONS = [
("hsk", "试", "Экзамены HSK", [
 ("hsk-1-kak-sdat-pervyy-uroven-s-pervogo-raza","HSK 1","Первый уровень: 150 слов, структура, форматы заданий и типичные ловушки экзамена."),
 ("hsk-1-probnyy-test-kak-ispolzovat-onlayn-trenajer","HSK 1 — пробный тест","Как использовать онлайн-тренажёр и честно проверить готовность к первому уровню."),
 ("hsk-2-sdaem-vtoroy-uroven-bez-stressa","HSK 2","Второй уровень: 300 слов, первые связные тексты и главная ловушка иероглифики."),
 ("hsk-2-probnyy-test-kak-ponyat-chto-ty-deystvitelno-gotov","HSK 2 — пробный тест","Готовы ли вы на самом деле: как проходить пробник без пиньиня и разбирать ошибки."),
 ("hsk-3-kak-sdat-bez-pininya-vyuchit-600-slov-i-ne-soyti-s-uma","HSK 3","Уровень, где исчезает пиньинь: 600 слов, три раздела и добавляется письмо."),
 ("hsk-3-probnyy-test-kak-preodolet-barer-i-sdat-na-maksimum","HSK 3 — пробный тест","Прыжок на новый уровень: как готовиться к чтению без пиньиня и к письму."),
 ("hsk-4-v-2026-razbor-kzamena-lovushek-i-novyh-formatov","HSK 4","Уровень «свободно говорю»: 1200 слов, новые форматы и как сдать в 2026 году."),
 ("hsk-4-probnyy-test-kak-ponyat-chto-ty-realno-gotov","HSK 4 — пробный тест","Как понять, что вы действительно готовы: скорость чтения и стратегия по времени."),
 ("podgotovka-k-hsk-4","Подготовка к HSK 4","Структура экзамена и понятный план занятий, чтобы дойти до сдачи."),
 ("sistema-ocenki-hsk-4","Система оценки HSK 4","Как считаются баллы, что такое проходные 180 и почему для вуза нужно больше."),
 ("ot-hsk-1-do-hsk-4-kak-menyautsya-trebovaniya-k-kolichestvu","От HSK 1 до HSK 4: слова и знаки","Почему 1200 слов — это не 1200 иероглифов и как на самом деле растёт объём."),
 ("hsk-5-kak-sdat-universitetskiy-kzamen","HSK 5","«Университетский» уровень: 2500 слов, длинные тексты и ловушки с синонимами."),
 ("hsk-5-probnyy-test","HSK 5 — пробный тест","Как устроить себе настоящую симуляцию экзамена и разобрать результат по темам."),
 ("sertifikat-hsk-chto-to-za-kzamen","Сертификат HSK","Что подтверждает сертификат, кому он нужен и что меняет переход на HSK 3.0."),
]),
("hskk", "说", "Устные экзамены HSKK и YCT", [
 ("hskk-kak-podgotovitsya-k-ustnomu-kzamenu","HSKK: устный экзамен","Как собрать связный ответ за минуту подготовки и что делать, если забыли слово."),
 ("hskk-1-kak-sdat","HSKK 1","Начальный уровень: повтор за диктором, короткие ответы и как перестать бояться."),
 ("hskk-2-kak-sdat-sredniy-uroven","HSKK 2","Средний уровень: рассказ по картинке, схема из четырёх предложений и связки."),
 ("hskk-3-kak-sdat-vysshiy-uroven","HSKK 3","Высший уровень: чтение вслух, пересказ и разговор о сложном простыми словами."),
 ("yct-kzamen-po-kitayskomu-dlya-detey","YCT: экзамен для детей","Четыре уровня детского экзамена, как выбрать свой и что сертификат реально даёт."),
 ("sdat-yct-v-moskve-kak-zapisatsya","Сдать YCT в Москве","Как найти центр, о чём спросить при записи, что взять с собой и как пройдёт день."),
]),
("csca", "考", "Экзамен CSCA", [
 ("csca-glavnyy-kzamen-dlya-postupleniya-v-vuzy-kitaya","CSCA: экзамен для вузов Китая","Что это за экзамен, из каких предметов состоит, структура и даты."),
 ("matematika-na-csca-kak-ponimat-usloviya-zadach","Математика на CSCA","Темы, лексика и как не потерять баллы на «мелочах» вроде 至少 и 至多."),
 ("fizika-na-csca-kak-vyuchit-fizicheskuu-terminologiu-na-kitayskom","Физика на CSCA","Как читать физические термины по составу слова и учить лексику быстрее."),
 ("himiya-na-csca-kak-vyuchit-kitayskuu-himicheskuu-terminologiu","Химия на CSCA","Названия элементов и ключ-подсказка: как устроена химическая лексика."),
]),
("grammar", "语", "Грамматика", [
 ("kak-zadavat-voprosy-na-kitayskom-vse-o-chastice--ma-za-5-minut","Частица 吗","Самый простой способ задать вопрос: как работает 吗 и когда она не нужна."),
 ("konstruktor-voprosov-v-kitayskom-shemy-i-pravila","Конструктор вопросов","Вопросительные местоимения и схемы: как собрать любой вопрос без перестановок."),
 ("razdelno-sochetaemye-glagoly","Раздельно-сочетаемые глаголы 离合词","Почему 见面 нельзя сказать «见面他» и как правильно разрывать такие глаголы."),
 ("minus-na-minus-daet-plus-kak-rabotaet-dvoynoe-otricanie","Двойное отрицание","不得不, 非…不可 и ловушки 差点儿没 и 好不: два минуса дают плюс с оттенком."),
]),
("lexika", "词", "Лексика и произношение", [
 ("top-50-bazovyh-glagolov-kitayskogo-yazyka-s-primerami","50 базовых глаголов","Ядро повседневной речи: глаголы с примерами и сочетаниями, а не списком."),
 ("eda-na-kitayskom","Еда: 60 слов для меню","Продукты, блюда и способы готовки: как из одних знаков складываются десятки названий."),
 ("cveta-na-kitayskom-s-transkripciey","Цвета с транскрипцией","Схема «качество + 色»: основные цвета с пиньинем и прозрачная логика названий."),
 ("cifry-ot-0-do-10-na-kitayskom","Цифры от 0 до 10","Тоны и транскрипция, изменение тона у 一, разница 二 и 两 и счёт на пальцах."),
 ("uchimsya-nazyvat-vremya-chasy-i-minuty-na-kitayskom","Время: часы и минуты","Как называть время по-китайски, от 点 и 分 до 半 и 差."),
 ("dni-nedeli-v-kitae","Дни недели","星期, 周 и 礼拜: три способа назвать день и почему воскресенье не «седьмое»."),
 ("dni-mesyacy-i-gody-na-kitayskom","Даты: дни, месяцы, годы","Порядок год → месяц → число, разница 号 и 日 и как заполнять документы."),
 ("do-svidaniya-po-kitayski-kak-na-samom-dele-chitaetsya","«До свидания» — как читается","再见 по слогам: почему «цзайцзянь» лишь приблизительно и при чём тут тоны."),
 ("korrektirovka-proiznosheniya-v-kitayskom","Корректировка произношения","Как поставить тоны и трудные звуки, чтобы вас понимали носители."),
 ("kak-govoryat-jivotnye-na-kitayskom","Как «говорят» животные","Собака лает 汪汪, кошка мяукает 喵: звукоподражания и что они говорят о фонетике."),
 ("idiomy-kitayskogo-yazyka","Идиомы 成语","Четыре знака, за которыми стоит история: как устроены чэнъюй и почему их не переводят буквально."),
 ("vesna-po-kitayski--ieroglif--i-umenie-chuvstvovat-kontekst","Весна по-китайски","Иероглиф 春 и умение чувствовать контекст: слово шире, чем время года."),
]),
("ieroglify", "字", "Иероглифы и письменность", [
 ("v-kitae-bukvy-ili-ieroglify-iz-chego-sostoit-kitayskaya-pismennost","Буквы или иероглифы","Из чего на самом деле состоит китайская письменность и что такое пиньинь."),
 ("kakie-bukvy-v-kitayskom-yazyke","Какие буквы в китайском","Почему алфавита нет, откуда взялся миф о «буквах хань» и что учить вместо них."),
 ("logika-kitayskih-kluchey","Значение ключей в иероглифах","Ключ-смысл и фонетик-подсказка: как угадывать значение незнакомого знака."),
 ("logika-kitayskih-kluchey-kak-ustroen-ieroglif-voda","Ключи на примере «воды»","Как устроен 水 и как ключ управляет смыслом десятков других знаков."),
 ("ieroglif-drujba","Иероглиф «дружба» 友","Две руки, направленные в одну сторону: разбор знака и как его запомнить."),
 ("ieroglif-ryba","Иероглиф «рыба» 鱼","От древней пиктограммы к современному знаку и почему 鱼 связан с достатком."),
 ("ieroglif-chetyre","Иероглиф «четыре» 四","Простое числительное с непростой репутацией: созвучие с 死 и суеверия вокруг него."),
]),
("kultura", "文", "Культура Китая", [
 ("kitayskiy-tiket-obscheniya-uvajenie-k-starshim-ierarhiya-i-ponyatie-lica","Этикет общения","Уважение к старшим, иерархия и понятие «лица» — то, что считывается сразу."),
 ("znachenie-cvetov-v-kitae","Значение цветов","Красный, белый, зелёный: символика оттенков и почему зелёная шапка — беда."),
 ("jeltyy-cvet-v-kitae","Жёлтый цвет","黄 был цветом императора: как менялась символика от знака власти до наших дней."),
 ("fioletovyy-cvet-v-kitae","Фиолетовый цвет","紫 — цвет благородства и доброго знака: откуда взялось 紫气东来."),
 ("nacionalnoe-jivotnoe-kitaya-bolshaya-panda","Большая панда","Национальное животное Китая: символ, дипломатия и лексика вокруг 熊猫."),
]),
("postuplenie", "学", "Учёба и поступление в Китае", [
 ("kak-postupit-v-kitay-na-budjet","Как поступить на бюджет","Пять путей к оплаченному месту, что покрывает стипендия и что решает при отборе."),
 ("besplatnoe-obrazovanie-v-kitae","Бесплатное образование","Что стоит за словом «бесплатно»: расходы до подачи, до вылета и в первый месяц."),
 ("stipendiya-csc-v-kitae-polnyy-gayd-po-polucheniu-dlya-studentov","Стипендия CSC","Полный гайд: каналы подачи Type A, B и C, учебный план и интервью."),
 ("stipendii-v-kitae-dlya-inostrancev","Стипендии для иностранцев","Правительственные, университетские и провинциальные: что покрывают и кому дают."),
 ("kak-vyigrat-grant-na-obuchenie-v-kitae","Как выиграть грант","Четыре типа грантов, документы, стратегия подачи и нужен ли посредник."),
 ("bakalavriat-v-kitae","Бакалавриат 本科","Сколько длится, чем программы на китайском отличаются от английских и зачем 预科."),
 ("magistratura-v-kitae-leksicheskiy-navigator","Магистратура: язык вуза","Лексика университетской среды — от деканата до защиты проекта."),
 ("est-li-v-kitae-kolledji","Есть ли в Китае колледжи","Среднее профессиональное образование: как устроено и кому подходит."),
 ("kak-postupit-v-kitay-posle-kolledzha","Поступление после колледжа","Засчитывается ли диплом, что такое «3+2» и какие пути реально открыты."),
 ("distancionnoe-obuchenie-v-kitae-chto-realno-dostupno","Дистанционное обучение","Что действительно доступно из России, а что завязано на присутствие в стране."),
]),
("zhizn", "活", "Жизнь в Китае", [
 ("rabota-v-kitae-dlya-inostranca","Работа для иностранца","Виза Z, требования, востребованные сферы и путь от оффера до вида на жительство."),
 ("dorogo-li-v-kitae","Дорого ли в Китае","Реальные цены на жильё, еду и транспорт — с расчётами по разным городам."),
 ("skolko-stoit-metro-v-kitae","Сколько стоит метро","Как устроена оплата проезда, тарифы по городам и способы платить."),
 ("detskie-sady-v-kitae","Детские сады","Возраст и группы, три типа садов с ценами, распорядок дня и обязательный сон."),
 ("chto-vzyat-s-soboy-v-kitay","Что взять с собой","Переходник, наличные, приложения и лекарства: что везти и что лучше оставить дома."),
 ("kakie-lekarstva-vzyat-s-soboy-v-kitay","Аптечка в поездку","Что положить с собой, что купить на месте и как объясниться в аптеке."),
]),
("business", "商", "Китайский для работы и бизнеса", [
 ("kitayskiy-yazyk-dlya-biznesa-kakaya-leksika-nujna","Китайский для бизнеса","Другой регистр: обороты для переговоров, вежливый отказ и ошибка с 万 и 亿."),
 ("biznes-tiket-v-kitae-5-pravil-kotorye-reshaut-vse","Бизнес-этикет","Пять правил, которые решают исход переговоров: от визитки до застолья."),
 ("kak-obrashchatsya-k-kitaycam-v-delovom-pisme","Обращение в деловом письме","Почему обращаются по должности, а не по имени, и как не нарушить иерархию."),
 ("korporativnyy-kitayskiy-zachem-kompanii-vkladyvautsya-v-obuchenie","Корпоративный китайский","Зачем компании учат сотрудников языку и как выстроить такую программу."),
]),
("oyazyke", "汉", "О языке и обучении", [
 ("slojno-li-uchit-kitayskiy-s-nulya","Сложно ли учить с нуля","Что действительно трудно, что проще русского и где бывает плато."),
 ("tapy-izucheniya-kitayskogo","Этапы изучения языка","Маршрут по шагам: пиньинь и тоны, иероглифика, грамматика, чтение и речь."),
 ("za-skolko-mojno-vyuchit-kitayskiy-yazyk-s-nulya","За сколько выучить с нуля","Сроки по уровням HSK, ориентир FSI и реально ли выучить за год."),
 ("za-kakoe-vremya-realno-vyuchit-kitayskiy","За какое время: статистика часов","Что говорят методики и цифры: сколько часов уходит на каждый уровень."),
 ("gruppovye-zanyatiya-po-kitayskomu-yazyku-kak-ustroen-urok","Групповые занятия","Как устроен урок, где успевает высказаться каждый, и о чём спросить школу."),
 ("kitayskiy-dlya-malyshey-kak-nachat","Китайский для малышей","Как знакомить дошкольника с языком через игры, песни и мультфильмы."),
 ("kursy-po-ieroglifike-kak-vybrat-programmu","Курсы по иероглифике","Как разложить сложный знак на графемы и на что смотреть в программе."),
 ("kursy-dlya-prepodavateley-kitayskogo-yazyka-chek-list","Курсы для преподавателей","Чек-лист по выбору программы: произношение, иероглифика и методика."),
 ("kak-razgovarivaut-v-kitae","Как разговаривают в Китае","Путунхуа и семь диалектных групп: почему письменность остаётся общей."),
 ("interesnye-fakty-o-kitayskom-yazyke","Интересные факты о языке","Тоны, десятки тысяч знаков и три тысячи для газеты: проверенные факты."),
 ("zachem-uchit-kitayskiy-yazyk","Зачем учить китайский","Карьера, наука, культура и неожиданные бонусы для мозга."),
]),
]

def plural(n):
    if 11 <= n % 100 <= 14: return "статей"
    d = n % 10
    if d == 1: return "статья"
    if d in (2, 3, 4): return "статьи"
    return "статей"

total = sum(len(s[3]) for s in SECTIONS)

STYLE = """<style>
@import url('https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,500;0,600;0,700&family=Inter:wght@400;500;600;700&family=Noto+Serif+SC:wght@500;700&display=swap');

#ks-cat{
  --brick:#A41E3A;--brick-deep:#841630;--brick-soft:#F7E6EB;
  --ink:#2C2420;--ink-2:#5A4F45;--taupe:#8B7D6B;--taupe-soft:#B8AC9C;
  --cream:#FAF7F2;--cream-2:#F3EDE3;--surface:#FFFFFF;
  --hairline:#EAE3D8;--hairline-2:#DED5C6;--shadow-card:0 2px 14px rgba(44,36,32,.06);
  --r-md:16px;--r-lg:22px;--r-pill:999px;
  --fd:'Cormorant Garamond',Georgia,'Times New Roman',serif;
  --fs:'Inter',-apple-system,'Helvetica Neue',Arial,sans-serif;
  --fh:'Noto Serif SC','Songti SC','SimSun',serif;
  max-width:1120px;margin:0 auto;padding:32px 22px 56px;background:var(--cream);
  font-family:var(--fs)!important;color:var(--ink-2);font-size:17px;line-height:1.6;-webkit-font-smoothing:antialiased;overflow-wrap:break-word;
}
#ks-cat *{box-sizing:border-box}
#ks-cat .cat-head{margin:0 0 30px}
#ks-cat .cat-eyebrow{font-family:var(--fs)!important;font-size:12.5px;font-weight:600;letter-spacing:.15em;text-transform:uppercase;color:var(--brick)!important;margin:0 0 10px}
#ks-cat h1{font-family:var(--fd)!important;font-weight:600;font-size:44px;line-height:1.08;letter-spacing:-.01em;color:var(--ink)!important;margin:0 0 12px}
#ks-cat .cat-lead{font-size:18px;color:var(--ink-2);max-width:60ch;margin:0}

#ks-cat .cat-nav{display:flex;flex-wrap:wrap;gap:8px;margin:24px 0 8px;padding:18px 0 0;border-top:1px solid var(--hairline)}
#ks-cat .cat-nav a{font-family:var(--fs)!important;font-size:13.5px;font-weight:500;color:var(--ink)!important;text-decoration:none;background:var(--surface);border:1px solid var(--hairline-2);border-radius:var(--r-pill);padding:7px 15px;transition:.15s}
#ks-cat .cat-nav a:hover{background:var(--brick)!important;color:#fff!important;border-color:var(--brick)}

#ks-cat .cat-sec{margin-top:46px;scroll-margin-top:90px}
#ks-cat .cat-sec-h{display:flex;align-items:center;gap:14px;margin:0 0 20px;padding-bottom:14px;border-bottom:2px solid var(--brick-soft)}
#ks-cat .cat-sec-h .ic{flex:0 0 auto;width:48px;height:48px;border-radius:14px;background:var(--brick);color:#fff;font-family:var(--fh)!important;font-weight:700;font-size:26px;display:flex;align-items:center;justify-content:center}
#ks-cat .cat-sec-h h2{font-family:var(--fd)!important;font-weight:600;font-size:29px;line-height:1.1;color:var(--ink)!important;margin:0}
#ks-cat .cat-sec-h .cnt{font-family:var(--fs)!important;font-size:13px;font-weight:600;color:var(--taupe)!important;margin-left:auto;white-space:nowrap}

#ks-cat .cat-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(320px,1fr));gap:16px}
#ks-cat a.card{display:flex;flex-direction:column;background:var(--surface);border:1px solid var(--hairline);border-radius:var(--r-md);padding:20px 22px;text-decoration:none;box-shadow:var(--shadow-card);transition:.16s;position:relative}
#ks-cat a.card:hover{border-color:var(--brick);box-shadow:0 8px 26px rgba(164,30,58,.13);transform:translateY(-2px)}
#ks-cat a.card .t{font-family:var(--fd)!important;font-weight:600;font-size:20px;line-height:1.2;color:var(--ink)!important;margin:0 0 8px}
#ks-cat a.card:hover .t{color:var(--brick)!important}
#ks-cat a.card .d{font-family:var(--fs)!important;font-size:14px;line-height:1.5;color:var(--ink-2)!important;margin:0 0 14px;flex:1 1 auto}
#ks-cat a.card .go{font-family:var(--fs)!important;font-size:13.5px;font-weight:600;color:var(--brick)!important;display:inline-flex;align-items:center;gap:6px}
#ks-cat a.card .go:after{content:"\\2192";display:inline-block;font-size:15px;line-height:1;transition:transform .16s}
#ks-cat a.card:hover .go:after{transform:translateX(3px)}

#ks-cat .cat-foot{margin-top:50px;padding:26px 30px;background:var(--surface);border:1px solid var(--hairline);border-radius:var(--r-lg);box-shadow:var(--shadow-card);text-align:center}
#ks-cat .cat-foot p{margin:0 0 14px;color:var(--ink-2)!important;font-family:var(--fs)!important}
#ks-cat .cat-foot .btn{display:inline-block!important;background:var(--brick)!important;color:#fff!important;font-family:var(--fs)!important;font-weight:600!important;font-size:15.5px!important;text-decoration:none!important;border-radius:14px!important;padding:13px 28px!important}
#ks-cat .cat-foot .btn:hover{background:var(--brick-deep)!important}

@media(max-width:600px){
  #ks-cat{padding:24px 14px 44px}
  #ks-cat h1{font-size:32px}
  #ks-cat .cat-grid{grid-template-columns:1fr}
  #ks-cat .cat-sec-h h2{font-size:24px}
}
</style>"""

o = io.StringIO()
w = o.write

w('\n<div id="ks-cat">\n\n')
w('<div class="cat-head">\n')
w('  <p class="cat-eyebrow">Блог Kitai School</p>\n')
w('  <h1>Все статьи по темам</h1>\n')
w('  <p class="cat-lead">Экзамены HSK, HSKK, YCT и CSCA, грамматика и лексика, иероглифы, культура Китая, '
  'учёба, работа и жизнь в стране — %d %s в одном месте. Выбирайте тему и читайте.</p>\n' % (total, plural(total)))
w('</div>\n\n')

w('<nav class="cat-nav">\n')
for sid, ic, name, items in SECTIONS:
    w('  <a href="#%s">%s</a>\n' % (sid, name))
w('</nav>\n')

for sid, ic, name, items in SECTIONS:
    w('\n<!-- %s -->\n' % name.upper())
    w('<section class="cat-sec" id="%s">\n' % sid)
    w('  <div class="cat-sec-h"><span class="ic">%s</span><h2>%s</h2><span class="cnt">%d %s</span></div>\n'
      % (ic, name, len(items), plural(len(items))))
    w('  <div class="cat-grid">\n')
    for slug, t, d in items:
        w('    <a class="card" href="%s%s" target="_blank" rel="noopener">'
          '<span class="t">%s</span><span class="d">%s</span>'
          '<span class="go">Читать</span></a>\n' % (B, slug, t, d))
    w('  </div>\n')
    w('</section>\n')

w('\n<div class="cat-foot">\n')
w('  <p>Не нашли нужную тему или хотите разобрать её с преподавателем? Приходите на бесплатный пробный урок — подберём программу под вашу цель.</p>\n')
w('  <a class="btn" href="#popup:zayavka">Записаться на пробный урок →</a>\n')
w('</div>\n\n')
w('</div>\n')

body = o.getvalue()
tilda = STYLE + body

D = "/home/user/Kitai-Shool/content/blog/"
open(D + "_katalog-statej.TILDA.html", "w", encoding="utf-8").write(tilda)

page = ('<!DOCTYPE html>\n<html lang="ru">\n<head>\n<meta charset="utf-8">\n'
        '<meta name="viewport" content="width=device-width, initial-scale=1">\n'
        '<title>Все статьи Kitai School — каталог по темам</title>\n'
        '<link rel="preconnect" href="https://fonts.googleapis.com">\n'
        '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>\n'
        + STYLE + '\n</head>\n<body>\n' + body + '\n</body>\n</html>\n')
open(D + "_katalog-statej.html", "w", encoding="utf-8").write(page)

# --- проверки ---
slugs = [s for _, _, _, its in SECTIONS for s, _, _ in its]
print("всего статей:", total, "| уникальных ссылок:", len(set(slugs)))
print("разделов:", len(SECTIONS))
print("TILDA chars:", len(tilda))
print("div:", tilda.count("<div"), "/", tilda.count("</div>"))
print("section:", tilda.count("<section"), "/", tilda.count("</section>"))
print("прямых кавычек в тексте:", len(re.findall(r'>[^<]*"[^<]*<', body)))
ids = re.findall(r'<section class="cat-sec" id="([^"]+)"', body)
navs = re.findall(r'<a href="#([^"]+)">', body)
print("якоря совпадают:", ids == navs)
