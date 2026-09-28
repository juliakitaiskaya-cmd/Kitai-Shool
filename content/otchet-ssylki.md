# Отчёт: адреса блога сверены с выгрузкой сайта

Дата: 28 сентября 2026. Ветка `claude/friendly-allen-lc3hz2`.

**Отменяет предыдущую версию этого отчёта.** Ваша выгрузка показала, что расхождение вдвое больше, чем я оценила по репозиторию, и что часть моей первой правки увела ссылки не туда. Всё пересчитано заново по выгрузке.

---

## 1. Что показала выгрузка

В файле 118 адресов. В репозитории 119 статей. Сверила построчно: 117 статей сошлись однозначно, дальше — три остатка, о них в разделе 5.

**У 58 статей из 117 тег `canonical` не совпадал с адресом публикации.** То есть больше чем у половины блога страница объявляла поисковику один адрес, а жила по другому.

Примеры:

| Файл объявлял | На сайте живёт |
|---|---|
| `sertifikat-hsk` | `sertifikat-hsk-chto-to-za-kzamen` |
| `hskk` | `hskk-kak-podgotovitsya-k-ustnomu-kzamenu` |
| `znachenie-kluchey-v-kitayskih-ieroglifah` | `logika-kitayskih-kluchey` |
| `etapy-izucheniya-kitayskogo-yazyka` | `tapy-izucheniya-kitayskogo` |
| `drug-na-kitayskom` | `drug-na-kitajskom` |
| `ieroglif-semya` | `ieroglif-semya-na-kitajskom` |

Следствие: **714 внутренних ссылок в 67 статьях вели на несуществующие страницы.**

Сюда попала и часть моей первой правки. Вчера я чинила ссылки по `canonical` из самих статей — другого источника правды у меня не было, сайт из этой среды не открывается (403 через прокси). Теперь видно, что сам `canonical` был неверен у половины блога, так что часть вчерашних 130 правок увела ссылки с одного несуществующего адреса на другой. Сегодня всё пересчитано от выгрузки.

---

## 2. Что исправлено

В каждом из 67 файлов:

- **собственный адрес страницы** — `canonical`, `og:url`, `url` и `@id` в JSON-LD, последний пункт хлебных крошек;
- **все ссылки на другие статьи** блога.

Замена шла по таблице из 101 псевдонима, с границей справа, чтобы короткий адрес не подменил длинный. Конфликтов между псевдонимами и реальными адресами не нашлось — проверено программно до записи файлов.

После правки:

| Проверка | Результат |
|---|---|
| Файлов, где `canonical` ≠ адрес из выгрузки | **0** |
| Ссылок на адреса вне выгрузки | 33 — все на две страницы из раздела 5 |
| Объём блоков T123 | максимум 46 048 знаков (лимит 50 000) |
| Баланс `<div>` | сходится во всех 67 |
| Футер «Для записи» | 0 |
| Локальные `assets/` в картинках | 0, адреса Tilda не тронуты |

---

## 3. Каталог статей

Каталог оказался единственным местом, где адреса были верны с самого начала: все 83 ссылки вели на существующие страницы. Не хватало статей — 34 штуки, включая всё написанное за последние недели.

Добавлены. **Теперь в каталоге 117 карточек** — весь блог. Обновлены счётчики разделов и число в лиде. Проверено: дублей нет, ни одна статья не пропущена, все адреса из выгрузки.

Новые разделы по объёму: О языке и обучении — 19, Лексика и произношение — 17, Учёба и поступление — 16, Экзамены HSK — 15, Иероглифы — 10, Бизнес — 9, Жизнь в Китае — 8, Грамматика — 7, Культура и HSKK/YCT — по 6, CSCA — 4.

Блок — 43 713 знаков, на 390 px без горизонтальной прокрутки.

---

## 4. Что перевставить в Tilda — 67 страниц

**Файлы, которые я отдала раньше сегодня, устарели все до одного.** Берите из этого списка.

Файлы лежат в `content/blog/<имя файла>.TILDA.html`. Мета-теги статей не менялись — перевставляется только блок T123.

| Статья | Адрес | Знаков |
|---|---|---|
| HSK 5 пробный тест | hsk-5-probnyy-test | 40 236 |
| HSKK 1 | hskk-1-kak-sdat | 40 456 |
| HSKK 2 | hskk-2-kak-sdat-sredniy-uroven | 41 357 |
| HSKK 3 | hskk-3-kak-sdat-vysshiy-uroven | 42 010 |
| HSKK: устный экзамен | hskk-kak-podgotovitsya-k-ustnomu-kzamenu | 40 583 |
| YCT для детей | yct-kzamen-po-kitayskomu-dlya-detey | 42 108 |
| Бакалавриат в Китае | bakalavriat-v-kitae | 42 553 |
| Бесплатное образование | besplatnoe-obrazovanie-v-kitae | 40 219 |
| Групповые занятия | gruppovye-zanyatiya-po-kitayskomu-yazyku-kak-ustroen-urok | 42 160 |
| Даты сдачи HSK | daty-sdachi-hsk-raspisanie-sessiy | 40 951 |
| Дистанционное обучение | distancionnoe-obuchenie-v-kitae-chto-realno-dostupno | 44 952 |
| Друг на китайском | drug-na-kitajskom | 44 501 |
| Дружба по-китайски 友 | ieroglif-drujba | 43 004 |
| Еда на китайском | eda-na-kitayskom | 43 850 |
| Жёлтый цвет в Китае | jeltyy-cvet-v-kitae | 39 507 |
| Значение ключей в иероглифах | logika-kitayskih-kluchey | 43 976 |
| Значение цветов в Китае | znachenie-cvetov-v-kitae | 45 087 |
| Идиомы 成语 | idiomy-kitayskogo-yazyka | 41 353 |
| Иероглиф «рыба» 鱼 | ieroglif-ryba | 37 750 |
| Иероглиф «четыре» 四 | ieroglif-chetyre | 35 471 |
| Иероглиф «семья» 家 | ieroglif-semya-na-kitajskom | 42 075 |
| Изучение с нуля | izuchenie-kitajskogo-yazyka-s-nulya-s-chego-nachat | 39 711 |
| Интересные факты о языке | interesnye-fakty-o-kitayskom-yazyke | 40 497 |
| Как «говорят» животные | kak-govoryat-jivotnye-na-kitayskom | 38 279 |
| Как быстро выучить китайский | kak-bystro-vyuchit-kitajskij | 41 547 |
| Как запоминать иероглифы | kak-zapominat-ieroglify | 39 343 |
| Как общаются китайцы | kak-obshchayutsya-kitajcy | 37 738 |
| Как переехать в Китай | kak-pereekhat-v-kitaj-chetyre-osnovaniya | 39 621 |
| Как попрощаться | kak-poproshchatsya-na-kitajskom | 39 271 |
| Китайский для малышей | kitayskiy-dlya-malyshey-kak-nachat | 41 943 |
| Интернет-сленг | kitajskij-internet-sleng | 38 417 |
| Китайский для бизнеса | kitayskiy-yazyk-dlya-biznesa-kakaya-leksika-nujna | 41 432 |
| Деловое общение: 50 фраз | kitayskiy-yazyk-dlya-delovogo-obscheniya | 46 048 |
| Китайский для детей | kitayskiy-yazyk-dlya-detey-marshrut-po-vozrastam | 40 452 |
| 50 фраз для поездки | kitajskij-yazyk-dlya-puteshestvij-50-fraz | 43 652 |
| Курс по грамматике | kurs-po-grammatike-kitajskogo-yazyka-kak-ustroen | 38 356 |
| Курс по логистике | kurs-po-logistike-na-kitajskom-yazyke | 38 949 |
| Курс по маркетингу | kurs-po-marketingu-na-kitajskom-yazyke-ploshchadki-terminy | 42 550 |
| Курс по пунктуации | kurs-po-punktuacii-kitajskogo-yazyka-vse-znaki-glavnye-pravila | 38 145 |
| Курс по разговорной речи | kurs-po-razgovornoj-rechi-kitajskogo-yazyka | 41 053 |
| Курс по союзам | kurs-po-soyuzam-kitajskogo-yazyka | 37 931 |
| Курс по этимологии | kurs-po-ehtimologii-kitajskogo-yazyka-chto-v-istoriyakh | 44 808 |
| Курсы для преподавателей | kursy-dlya-prepodavateley-kitayskogo-yazyka-chek-list | 39 765 |
| Курсы по иероглифике | kursy-po-ieroglifike-kak-vybrat-programmu | 42 517 |
| Лагерь в Китае | lager-v-kitae-s-izucheniem-kitajskogo-chem-on-otlichaetsya | 40 569 |
| Ключи на примере «воды» | logika-kitayskih-kluchey-kak-ustroen-ieroglif-voda | 37 215 |
| Магистратура: язык вуза | magistratura-v-kitae-leksicheskiy-navigator | 45 522 |
| После 11 класса | obuchenie-v-kitae-dlya-russkikh-posle-11-klassa | 45 309 |
| Обучение для русских | obuchenie-v-kitae-dlya-russkikh | 39 344 |
| Онлайн-репетитор | onlajn-repetitor-po-kitajskomu-yazyku-chem-on-otlichaetsya | 45 602 |
| Поступление без ЕГЭ | postuplenie-v-kitaj-bez-egeh-chto-trebuet-vuz | 39 413 |
| Как выбрать вуз | postuplenie-v-vuz-kitaya | 45 640 |
| Сдать YCT в Москве | sdat-yct-v-moskve-kak-zapisatsya | 39 593 |
| Сертификат HSK | sertifikat-hsk-chto-to-za-kzamen | 39 648 |
| Стажировка в Китае | stazhirovka-v-kitae-chto-vam-predlagayut | 40 037 |
| Стипендии для иностранцев | stipendii-v-kitae-dlya-inostrancev | 40 405 |
| Технический китайский | tekhnicheskij-kitajskij-yazyk | 40 060 |
| Факты о китайских школах | fakty-o-kitajskikh-shkolakh | 40 019 |
| Фиолетовый цвет | fioletovyy-cvet-v-kitae | 37 903 |
| Цвета с транскрипцией | cveta-na-kitayskom-s-transkripciey | 34 786 |
| Цифры от 0 до 10 | cifry-ot-0-do-10-na-kitayskom | 37 875 |
| Чем писать иероглифы | chem-pisat-kitajskie-ieroglify | 35 933 |
| Что отвечать на «нихао» | chto-otvechat-na-nikhao | 37 424 |
| Школа в Москве | shkola-kitajskogo-yazyka-v-moskve-chto-schitat | 37 850 |
| Этапы изучения | tapy-izucheniya-kitayskogo | 39 088 |
| Юридический китайский | yuridicheskij-kitajskij-yazyk-chto-chitat | 42 141 |
| Языковые курсы в Китае | yazykovye-kursy-v-kitae-kakie-byvayut | 42 518 |

Плюс каталог: `_katalog-statej.TILDA.html`, 43 713 знаков.

---

## 5. Три вопроса к вам

**1. «Курсы китайского для взрослых».** В репозитории есть файл `kursy-kitajskogo-dlya-vzroslyh.html`, и на него ведут **22 ссылки** из статей — по адресу `kitai-school.ru/article/kursy-kitajskogo-dlya-vzroslyh`. В выгрузке такого адреса нет. Похоже, это не статья, а страница курса, и живёт она не в `/article/`. Скажите правильный адрес — заменю во всех статьях. Пока эти 22 ссылки битые.

**2. «До свидания по-китайски: 再见 и ещё пять способов попрощаться».** Файл `do-svidaniya-po-kitajski-sposoby.html` в репозитории есть, на него ведут **11 ссылок**, а в выгрузке такой страницы нет. При этом есть близкая — «До свидания по-китайски: как на самом деле читается 再见». Варианта два: либо статья не опубликована и её нужно выложить, либо она лишняя и 11 ссылок надо перевести на вторую. Что из этого?

**3. Дубль HSK 1.** В выгрузке две строки с одним и тем же названием «HSK 1: как сдать первый уровень с первого раза»:

- `hsk-1-kak-sdat-pervyy-uroven-s-pervogo-raza` (через «y»)
- `hsk-1-kak-sdat-pervyj-uroven-s-pervogo-raza` (через «j»)

Все ссылки блога и карточка каталога ведут на первый. Второй, судя по всему, — остаток от пересоздания страницы. Его стоит удалить или поставить на него редирект, иначе две одинаковые страницы конкурируют в выдаче.

---

## 6. Прежние долги

1. Две страницы про сроки конкурируют между собой — «За какое время реально выучить китайский» и «За сколько можно выучить с нуля». Какая главная?
2. **Предложение:** называть файлы картинок `oblozhka-<слаг>` и `infografika-<слаг>` — Tilda дважды обрезала два разных файла до одинакового имени.
3. 132 файла `.TILDA-BLOCK.html` и `.TILDA-HEAD.html` — остатки старого формата, предложено удалить.
