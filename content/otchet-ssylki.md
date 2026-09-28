# Отчёт: внутренние ссылки блога приведены к каноническим адресам

Дата: 28 сентября 2026. Ветка `claude/friendly-allen-lc3hz2`, коммит «Ссылки приведены к каноническим адресам».

---

## 1. Что было не так

В репозитории 119 статей. **У 43 из них адрес публикации не совпадает с именем файла.**

Примеры:

| Файл в репозитории | Адрес на сайте |
|---|---|
| `hsk-1.html` | `hsk-1-kak-sdat-pervyy-uroven-s-pervogo-raza` |
| `granty-na-obuchenie-v-kitae.html` | `kak-vyigrat-grant-na-obuchenie-v-kitae` |
| `voda-na-kitajskom-ieroglif.html` | `logika-kitayskih-kluchey-kak-ustroen-ieroglif-voda` |
| `korrektirovka-proiznosheniya-kitajskogo.html` | `korrektirovka-proiznosheniya-v-kitayskom` |
| `za-kakoe-vremya-vyuchit-kitajskij.html` | `za-kakoe-vremya-realno-vyuchit-kitayskiy` |

Внутренние ссылки в статьях строились **по именам файлов**. В результате 130 ссылок вели на несуществующие адреса — читатель попадал на 404.

Из этих 130 **80 поставила я за эту сессию**: я всю дорогу брала слаг из имени файла, не проверив `canonical`. Остальные 50 накопились раньше.

---

## 2. Что сделано

Замена выполнена программно, строго по тегу `<link rel="canonical">` из самой статьи — другого источника правды нет, сайт из этой среды не открывается.

Две технические оговорки, чтобы правка не сломала лишнего:

1. **Граница справа.** Короткий слаг не должен подменять длинный: `hsk-1` не трогает `hsk-1-probnyy-test`. В регулярном выражении стоит запрет на буквы, цифры, дефис и подчёркивание после слага.
2. **Якоря сохранены.** 199 ссылок из 438 заканчивались не кавычкой, а `#faq` и подобным. Замена работает по началу адреса, хвост остаётся на месте.

Проверено после замены: ни одной ссылки на имя файла не осталось; все адреса картинок Tilda на месте, локальных `assets/` ноль; блоки T123 пересобраны, баланс `<div>` сходится, футеров нет.

---

## 3. Что перевставить в Tilda — 22 страницы

| Адрес страницы | Знаков в блоке |
|---|---|
| chem-pisat-kitayskie-ieroglify | 35 767 |
| chto-otvechat-na-nihao | 37 436 |
| drug-na-kitayskom | 44 557 |
| fakty-o-kitayskih-shkolah | 39 894 |
| ieroglif-semya | 42 014 |
| kak-bystro-vyuchit-kitayskiy | 41 505 |
| kak-obshchayutsya-kitaycy | 37 664 |
| kak-pereehat-v-kitay | 39 337 |
| kak-poproshchatsya-na-kitayskom | 39 235 |
| kak-zapominat-ieroglify | 39 273 |
| kitayskiy-internet-sleng | 38 391 |
| kurs-po-etimologii-kitayskogo-yazyka | 44 703 |
| kurs-po-razgovornoy-rechi-kitayskogo-yazyka | 40 983 |
| lager-v-kitae-s-izucheniem-kitayskogo | 40 310 |
| obuchenie-v-kitae-dlya-russkih | 39 193 |
| obuchenie-v-kitae-dlya-russkih-posle-11-klassa | 45 123 |
| postuplenie-v-kitay-bez-ege | 39 247 |
| postuplenie-v-vuz-kitaya | 45 448 |
| shkola-kitayskogo-yazyka-v-moskve | 37 516 |
| stazhirovka-v-kitae | 39 788 |
| yazykovye-kursy-v-kitae | 42 327 |
| yuridicheskiy-kitayskiy-yazyk | 41 966 |

Файлы лежат в `content/blog/<имя файла>.TILDA.html`. Мета-теги не менялись — перевставлять нужно только блок T123.

---

## 4. Вторая находка: ещё 26 страниц, и тут нужно ваше решение

Осталось 89 ссылок, которые ведут на адреса, каких нет **ни у одного** файла в репозитории. Разбор показал, что это не выдумка: за каждой стоит реальная статья блога, но её файл объявляет **другой, более короткий** адрес.

| Адрес в ссылках | Что объявляет файл |
|---|---|
| sertifikat-hsk-chto-to-za-kzamen | sertifikat-hsk |
| hskk-kak-podgotovitsya-k-ustnomu-kzamenu | hskk |
| hskk-1-kak-sdat | hskk-1 |
| hskk-2-kak-sdat-sredniy-uroven | hskk-2 |
| hskk-3-kak-sdat-vysshiy-uroven | hskk-3 |
| yct-kzamen-po-kitayskomu-dlya-detey | yct |
| sdat-yct-v-moskve-kak-zapisatsya | yct-v-moskve |
| eda-na-kitayskom | eda-na-kitayskom-yazyke |
| cveta-na-kitayskom-s-transkripciey | cveta-na-kitajskom |
| cifry-ot-0-do-10-na-kitayskom | cifry-na-kitayskom-ot-0-do-10 |
| kak-govoryat-jivotnye-na-kitayskom | zvuki-zhivotnyh-na-kitayskom |
| idiomy-kitayskogo-yazyka | idiomy-v-kitayskom-yazyke |
| logika-kitayskih-kluchey | znachenie-kluchey-v-kitayskih-ieroglifah |
| ieroglif-drujba | druzhba-na-kitayskom-ieroglif |
| ieroglif-chetyre | ieroglif-4-po-kitayski |
| jeltyy-cvet-v-kitae | znachenie-zheltogo-cveta-v-kitae |
| fioletovyy-cvet-v-kitae | znachenie-fioletovogo-cveta-v-kitae |
| stipendii-v-kitae-dlya-inostrancev | stipendiya-v-kitae |
| magistratura-v-kitae-leksicheskiy-navigator | magistratura-v-kitae |
| distancionnoe-obuchenie-v-kitae-chto-realno-dostupno | distancionnoe-obuchenie-v-kitae |
| kitayskiy-yazyk-dlya-biznesa-kakaya-leksika-nujna | kitayskiy-yazyk-dlya-biznesa |
| tapy-izucheniya-kitayskogo | etapy-izucheniya-kitayskogo-yazyka |
| gruppovye-zanyatiya-po-kitayskomu-yazyku-kak-ustroen-urok | gruppovye-zanyatiya-po-kitayskomu-yazyku |
| kitayskiy-dlya-malyshey-kak-nachat | kitayskiy-dlya-malyshey |
| kursy-po-ieroglifike-kak-vybrat-programmu | kursy-po-ieroglifike |
| kursy-dlya-prepodavateley-kitayskogo-yazyka-chek-list | kursy-dlya-prepodavateley-kitayskogo-yazyka |

**Почему я думаю, что права левая колонка, а не правая.**

Все эти адреса стоят в каталоге статей. В том же каталоге 57 ссылок ведут на адреса, которые статьи объявляют сами, — и среди них все длинные и неочевидные: `hsk-1-kak-sdat-pervyy-uroven-s-pervogo-raza`, `hsk-3-kak-sdat-bez-pininya-vyuchit-600-slov-i-ne-soyti-s-uma`, `hsk-5-kak-sdat-universitetskiy-kzamen`. Десять из десяти совпадений по HSK. Значит, каталог собирали по реальным адресам сайта.

Второй довод — как записаны слова. В левой колонке ровно те особенности транслитерации Tilda, что и в подтверждённых адресах: «экзамен» превращается в `kzamen`, «нужна» в `nujna`, «дружба» в `drujba`, «жёлтый» в `jeltyy`. Так пишет Tilda, а не человек и не я.

**Чего я сделать не могу.** Проверить напрямую: `kitai-school.ru` из этой среды не открывается, прокси отдаёт 403. А правка тут дорогая — менять `canonical` у 26 опубликованных страниц. Ошибусь — уроню их выдачу.

Поэтому решение за вами. Проверяется одной ссылкой: откройте
`https://kitai-school.ru/article/sertifikat-hsk-chto-to-za-kzamen`
и скажите, открылась статья про сертификат HSK или 404.

---

## 5. Что ещё осталось в каталоге

Каталог статей (`_katalog-statej.html`) сам по себе неполон: в нём 83 карточки на 119 статей. Не представлены 62 статьи, включая всё, что написано за последние недели. Разбирать его имеет смысл после того, как решится вопрос из раздела 4, — иначе придётся править дважды.
