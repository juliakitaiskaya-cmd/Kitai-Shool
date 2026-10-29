# -*- coding: utf-8 -*-
"""Добавляет в каталог статьи, у которых появился адрес в выгрузке."""
import re, os

os.chdir("/home/user/Kitai-Shool/content/blog")
SRC = "_katalog-statej.html"
U = "https://kitai-school.ru/article/"

# раздел: (слаг, заголовок карточки, описание)
NEW = {
 "hsk": [
  ("sdat-hsk-kak-prohodit-den-kzamena", "Как проходит день экзамена",
   "Что взять с собой, как устроен зал и где теряют баллы на формате, а не на языке."),
 ],
 "hskk": [
  ("sdat-yct-kzamenacionnaya-leksika", "YCT: экзаменационная лексика",
   "Слова-подсказки в заданиях и знаки, которые дети путают чаще всего."),
 ],
 "grammar": [
  ("kak-sostavlyat-predlozheniya-na-kitajskom", "Как составлять предложения",
   "Базовая схема и шесть позиций: почему порядок слов здесь работает за падежи."),
  ("konstrukciya--v-kitajskom", "Конструкция 把",
   "Зачем она нужна и четыре условия, без которых предложение не соберётся."),
  ("passivnyy-zalog-v-kitayskom", "Пассивный залог с 被",
   "Схема конструкции, оттенок неприятного и три замены, из-за которых 被 звучит реже."),
  ("poryadok-opredeleniy-v-kitayskom", "Порядок определений",
   "Пять мест перед существительным и правила частицы 的, которая меняет смысл."),
  ("narechiya-v-kitayskom", "Наречия: 很, 也, 都",
   "Почему их место в предложении строго фиксировано и что идёт раньше отрицания."),
  ("mestoimeniya-v-kitayskom-yazyke", "Местоимения",
   "我, 你, 他 без падежей, множественное число через 们 и вежливое 您."),
  ("schetnye-slova-v-kitayskom-yazyke", "Счётные слова 量词",
   "Зачем нужны классификаторы, как они закреплены за предметами и пятнадцать частых."),
  ("poryadkovye-chislitelnye-v-kitayskom-yazyke", "Порядковые числительные",
   "第一, 第二 и случаи, где 第 не ставят вовсе."),
 ],
 "lexika": [
  ("kurs-po-fonetike-kitajskogo-yazyka-tony-pinin", "Курс по фонетике",
   "Тоны, пиньинь и как перестать говорить по-русски китайскими словами."),
  ("iniciali-v-kitajskom-yazyke", "Инициали и финали",
   "21 инициаль, 35 финалей и правила, по которым собирается слог."),
  ("kitayskie-slova-dlya-nachinauschih", "70 слов первого месяца",
   "Вежливые формы, служебный костяк и десять глаголов — с иероглифом и пиньинем."),
  ("kitayskie-slova-na-russkom-proiznoshenii", "Китайские слова русскими буквами",
   "Где кириллица искажает звучание и как пользоваться такой записью без вреда."),
  ("privet-po-kitajski", "«Привет» по-китайски",
   "Как пишется 你好 и почему отдельного иероглифа «здравствуйте» нет."),
  ("sdobroe-utro-po-kitajski", "«Доброе утро»",
   "早上好, короткое 早 и чем от них отличается 早安."),
  ("ya-tebya-lublu-po-kitayski", "«Я тебя люблю»",
   "我爱你, его тоны и более сдержанные способы сказать то же самое."),
  ("udacha-po-kitajski", "«Удача» по-китайски",
   "好运, 运气 и почему 福 на двери не переворачивают."),
  ("krasivye-slova-na-kitajskom", "Красивые слова",
   "Выражения, в которых виден образ, а не только значение."),
  ("napitki-na-kitayskom", "Напитки",
   "Вода, чай, кофе и молочный чай: как называются и как их заказать."),
  ("siniy-na-kitayskom", "Синий цвет",
   "蓝 и его оттенки, а ещё 蓝图 и 蓝领 — слова, где цвет уже не про цвет."),
  ("chernyy-na-kitayskom", "Чёрный цвет",
   "Иероглиф 黑, слова от 黑板 до 黑马 и значение «незаконный», которого нет в русском."),
  ("seryj-po-kitajski", "Серый цвет",
   "灰色 huīsè: чтение, написание и случаи, где это слово не подходит."),
  ("mesyacy-na-kitayskom", "Месяцы",
   "Почему их не нужно запоминать по отдельности и где прячется исключение."),
  ("nol-po-kitayski", "Ноль по-китайски",
   "Иероглиф 零, кружок 〇 и почему этот знак значит «мелочь»."),
  ("kitayskaya-sistema-schisleniya", "Система счисления",
   "Разряды 百, 千, 万 и 亿, группы по четыре нуля и запись больших чисел."),
  ("drobi-v-kitayskom-yazyke", "Дроби и проценты",
   "Формула 分之, где знаменатель идёт первым, и скидки, которые считают наоборот."),
 ],
 "ieroglify": [
  ("poryadok-chert-v-kitayskih-ieroglifah", "Порядок черт",
   "Восемь базовых черт и правила, по которым собирается любой знак."),
  ("chto-oznachaut-kitayskie-ieroglify", "Что означают иероглифы",
   "Как узнать значение знака и почему у одного иероглифа их несколько."),
  ("kto-pridumal-kitayskie-ieroglify", "Кто придумал иероглифы",
   "Легенда о Цан Цзе и то, что на самом деле говорит наука."),
  ("ogon-na-kitayskom-ieroglif", "Иероглиф «огонь» 火",
   "Четыре точки внизу и слова, которые из этого знака выросли."),
  ("kakoj-kitajskij-uchit", "Упрощённые или традиционные",
   "Какой китайский учить и когда выбор действительно есть."),
  ("istoriya-kitajskoj-kalligrafii", "История каллиграфии",
   "Как письмо стало искусством наравне с живописью."),
 ],
 "kultura": [
  ("kitayskie-tradicionnye-prazdniki", "Традиционные праздники",
   "Календарь главных дат, легенды и обычаи — от Нового года до середины осени."),
  ("prazdnik-fonarey", "Праздник фонарей",
   "Чем завершается новогодний цикл, как устроены загадки на фонарях и чем 汤圆 отличается от 元宵."),
  ("krasnyy-cvet-v-kitayskoy-kulture", "Красный цвет",
   "От свадебных конвертов до слов с корнем 红 и случаев, где красный неуместен."),
  ("kitayskaya-numerologiya", "Числовая символика",
   "Почему 8 приносит богатство, а 4 пугает: значения цифр держатся на созвучии."),
  ("neschastlivoe-chislo-v-kitae", "Несчастливое число",
   "Четвёрка, её двузначные усиления и числа, о которых говорят реже."),
  ("kitajskie-primety-i-sueveriya-tri-mekhanizma", "Приметы и суеверия",
   "Три механизма, новогодние запреты и год своего знака."),
  ("pochemu-kitay-nazyvaut-podnebesnoy", "Почему Китай — Поднебесная",
   "中国 — название страны, 天下 — картина мира, а «Поднебесная» — слово русское."),
  ("kakaya-religiya-v-kitae", "Какая религия в Китае",
   "Конфуцианство, буддизм, даосизм и понятие «трёх учений»."),
  ("kitajskie-poslovicy-i-pogovorki", "Пословицы и поговорки",
   "Народная мудрость в нескольких иероглифах и чем она отличается от чэнъюй."),
  ("luchshie-kitajskie-knigi", "Китайские книги",
   "От классических романов до современной прозы: с чего начинать читать."),
  ("kak-nazyvaetsya-tradicionnoe-kitajskoe-plate", "Традиционное платье",
   "Ципао, ханьфу и чем они различаются."),
  ("kak-zdorovayutsya-kitajcy-zhesty-poklony", "Как здороваются китайцы",
   "Жесты, поклоны и почему рукопожатие здесь молодое."),
  ("kak-obrashchatsya-k-kitajcam-po-imeni-ili-familii", "Имя или фамилия",
   "Как обратиться к китайцу, чтобы не показаться невежливым."),
  ("rechevoj-ehtiket-v-kitae", "Речевой этикет",
   "Формулы вежливости и слова, которыми лучше не злоупотреблять."),
  ("kak-obshchatsya-v-kitae", "Как общаться в Китае",
   "Почему здесь слушают ситуацию, а не слова."),
 ],
 "postuplenie": [
  ("dokumenty-dlya-postupleniya-v-kitaj", "Документы для поступления",
   "Полный список и логика подготовки: что заказывать первым из-за сроков."),
  ("skolko-stoit-uchyoba-v-kitae", "Сколько стоит учёба",
   "Цены на обучение и проживание и расходы, о которых не пишут в брошюре."),
  ("stipendiya-pravitelstva-knr-dlya-rossiyan", "Стипендия правительства КНР",
   "Отдельный канал для россиян: двойная подача и две ступени отбора."),
  ("kitajskie-vuzy-dlya-russkikh-studentov-bez-znaniya-yazyka", "Вузы без знания языка",
   "Какие программы идут на английском и чем за это приходится платить."),
  ("medicinskoe-obrazovanie-v-kitae", "Медицинское образование",
   "Сколько учиться на врача и признают ли диплом дома."),
  ("obuchenie-v-kitae-posle-9-klassa-chto-realno-vozmozhno", "После 9 класса",
   "Что реально возможно в 15–16 лет и чем занять два года до поступления."),
  ("kak-postupit-na-yazykovye-kursy-v-kitaj-kalendar-podachi", "Языковые курсы: подача",
   "Календарь подачи, деньги на входе и что приходит в ответ."),
  ("yazykovoy-god-v-kitae-leksika-kampusa", "Языковой год: лексика кампуса",
   "Беглая речь и что делать, когда учебник перестаёт помогать."),
 ],
 "zhizn": [
  ("kak-uchatsya-kitajskie-shkolniki", "Как учатся школьники",
   "Предметы, языки, учебный год и нагрузка по неделям."),
  ("pravila-v-kitayskih-shkolah", "Правила в школах",
   "Три слоя правил: государственный свод, указания и распорядок самой школы."),
  ("kak-stavyat-ocenki-v-kitae", "Как ставят оценки",
   "Стобалльная система, запрет на рейтинги и культ результата."),
  ("mozhno-li-studentam-rabotat-v-kitae", "Работа для студентов",
   "Что разрешает виза и где проходят границы."),
 ],
 "business": [
  ("kursy-delovogo-kitajskogo-yazyka-kak-vybrat-programmu", "Курсы делового китайского",
   "Как выбрать программу под свою задачу и не бросить на полпути."),
  ("kurs-po-ehkonomicheskomu-kitajskomu-chek-list", "Экономический китайский",
   "Чек-лист по выбору программы и чем он отличается от делового."),
  ("kak-pisat-pismo-na-kitajskom", "Письмо на китайском",
   "Шесть частей, формулы вежливости и отличия от русской традиции."),
 ],
 "oyazyke": [
  ("stoit-li-uchit-kitajskij-yazyk", "Стоит ли учить китайский",
   "Как принять решение до оплаты курса и когда честный ответ — нет."),
  ("kak-izuchit-kitajskij-yazyk-samostoyatelno-iz-chego-sostoit-zanyatie",
   "Самостоятельно: из чего состоит занятие",
   "Как устроить неделю, чтобы заниматься без преподавателя и не встать."),
  ("kak-kitaycy-uchat-svoy-yazyk", "Как китайцы учат свой язык",
   "Пиньинь в первом классе, прописи в клетку и шесть языков на выбор в гаокао."),
  ("razgovornyy-klub-s-nositelem-yazyka-kak-ustroeny", "Разговорный клуб",
   "Как устроены встречи, кому подходит и что говорить, чтобы не молчать."),
  ("samoe-dlinnoe-slovo-v-kitajskom-yazyke", "Самое длинное слово",
   "Существует ли оно и как вообще считать длину там, где нет пробелов."),
 ],
}

DUP = {
    "hsk-1-kak-sdat-pervyj-uroven-s-pervogo-raza":
        "дубль hsk-1-kak-sdat-pervyy-uroven-s-pervogo-raza",
    "kak-zdorovayutsya-kitajcy":
        "дубль kak-zdorovayutsya-kitajcy-zhesty-poklony",
}

src = open(SRC, encoding="utf-8").read()
было = len(re.findall(r'class="card"', src))

# адреса, которые уже стоят в каталоге
in_cat = set(re.findall(r'href="https://kitai-school\.ru/article/([^"]+)"', src))
for sec, items in NEW.items():
    for slug, _, _ in items:
        assert slug not in in_cat, "уже в каталоге: %s" % slug

# все новые адреса есть в выгрузке
have = {l.split("\t")[1] for l in open("../adresa-sayta.tsv", encoding="utf-8")
        if l.startswith("article\t")}
for sec, items in NEW.items():
    for slug, _, _ in items:
        assert slug in have, "нет в выгрузке: %s" % slug


def card(slug, title, desc):
    return ('    <a class="card" href="%s%s" target="_blank" rel="noopener">'
            '<span class="t">%s</span><span class="d">%s</span>'
            '<span class="go">Читать</span></a>\n' % (U, slug, title, desc))


out = src
for sec, items in NEW.items():
    m = re.search(r'(<section class="cat-sec" id="%s">.*?</div>\s*\n)(\s*</section>)'
                  % sec, out, re.S)
    assert m, "раздел не найден: %s" % sec
    block = m.group(0)
    add = "".join(card(*i) for i in items)
    # вставляем перед закрытием .cat-grid
    tail = re.search(r'\n(\s*)</div>\s*\n\s*</section>', block)
    assert tail, "конец сетки не найден: %s" % sec
    new_block = block[:tail.start()] + "\n" + add.rstrip("\n") + block[tail.start():]
    out = out.replace(block, new_block)

# пересчитываем подписи
TOTAL = 0
for sec in re.findall(r'<section class="cat-sec" id="([^"]+)">', out):
    blk = re.search(r'<section class="cat-sec" id="%s">.*?</section>' % sec, out, re.S).group(0)
    n = len(re.findall(r'class="card"', blk))
    TOTAL += n
    word = "статья" if n % 10 == 1 and n % 100 != 11 else \
           "статьи" if n % 10 in (2, 3, 4) and n % 100 not in (12, 13, 14) else "статей"
    new_blk = re.sub(r'(<span class="cnt">)[^<]*(</span>)',
                     r'\g<1>%d %s\g<2>' % (n, word), blk, count=1)
    out = out.replace(blk, new_blk)

out = out.replace("119 статей в одном месте", "%d статей в одном месте" % TOTAL)

open(SRC, "w", encoding="utf-8").write(out)

# блок для Tilda — от <style> до конца #ks-cat
i = out.index("<style>")
j = out.index("</body>")
block = out[i:j].rstrip()
assert block.endswith("</div>"), "блок обрывается не на закрытии #ks-cat"
open("_katalog-statej.TILDA.html", "w", encoding="utf-8").write(block + "\n")

стало = len(re.findall(r'class="card"', out))
print("карточек было", было, "стало", стало, "| добавлено", стало - было)
print("в подписи разделов и в лиде:", TOTAL)
print("пропущены как дубли:", len(DUP))
for s, why in DUP.items():
    print("   ", s, "—", why)
print("размер блока T123:", len(block))

# ---- блок T123 не влезает в лимит ~50 000, режем на два ----------------------
LIMIT = 50000
PART1 = ("hsk", "hskk", "csca", "grammar", "lexika", "ieroglify")

secs = {m.group(1): m.group(0) for m in
        re.finditer(r'<section class="cat-sec" id="([^"]+)">.*?</section>', block, re.S)}
style = block[:block.index("</style>") + 8]
head = block[block.index('<div id="ks-cat">'):block.index("<section")]
foot = block[block.rindex('<div class="cat-foot">'):block.rindex("</div>")]

p1 = style + "\n" + head + "\n".join(secs[s] for s in PART1) + "\n\n</div>\n"
p2 = ('<div id="ks-cat" style="padding-top:0">\n\n'
      + "\n".join(secs[s] for s in secs if s not in PART1)
      + "\n\n" + foot + "\n</div>\n")

assert len(p1) < LIMIT and len(p2) < LIMIT, "часть не влезла в лимит"
assert len(re.findall(r'class="card"', p1 + p2)) == стало, "карточки потерялись при делении"
open("_katalog-statej.TILDA-1.html", "w", encoding="utf-8").write(p1)
open("_katalog-statej.TILDA-2.html", "w", encoding="utf-8").write(p2)
print("часть 1:", len(p1), "| часть 2:", len(p2), "| лимит", LIMIT)
