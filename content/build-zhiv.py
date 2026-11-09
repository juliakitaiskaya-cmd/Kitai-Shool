# -*- coding: utf-8 -*-
import re, os

os.chdir("/home/user/Kitai-Shool/content/blog")
SRC = "schastye-na-kitayskom-yazyke.html"
OUT = "schetnoe-slovo-dlya-zhivotnyh-v-kitayskom.html"
SLUG = "schetnoe-slovo-dlya-zhivotnyh-v-kitayskom"
U = "https://kitai-school.ru/article/"

HERO = "https://static.tildacdn.com/tila6233-3864-4734-b762-383633626332/zhiv-hero.png"
FIG = "https://static.tildacdn.com/tila6164-6434-4366-a337-323065306537/zhiv-info.png"
HERO_ALT = ("Определитель из трёх вопросов: лошадь — 匹, длинное и гибкое — 条, крупный скот — "
            "头, во всех остальных случаях 只")
FIG_ALT = ("Матрица по двум признакам: хозяйственные животные и остальные, обычная форма и "
           "длинное тело; лошадь вынесена отдельно с 匹")

src = open(SRC, encoding="utf-8").read()
css = re.search(r'<link rel="preconnect".*?</style>', src, re.S).group(0)
sticky = re.search(r'<script>\s*/\* Kitai School — sticky.*?</script>', src, re.S).group(0)
assert css.count("#ks-art .han{") == 1

SIDE = re.search(r'<aside id="ks-side">.*?</aside>', src, re.S).group(0)
m = re.search(r'<p class="side-note">.*?</p>', SIDE, re.S)
SIDE = SIDE.replace(m.group(0), '<p class="side-note">只 подходит большинству животных, но '
                                'лошадь считают через 匹, корову через 头, а рыбу через 条</p>')


def L(sl, t):
    return '<a href="%s%s" target="_blank" rel="noopener">%s</a>' % (U, sl, t)


TITLE = "Счётное слово для животных: почему 只 подходит кошке, но не лошади"
DESC = ("Счётное слово для животных в китайском чаще всего 只 (zhī), но не всегда: лошадей "
        "считают через 匹, крупный скот — через 头, а длинных и гибких, вроде рыбы и змеи, — "
        "через 条. Разбираем, по каким признакам закреплена каждая группа, почему 马 стоит "
        "особняком и что делать с собакой, которую называют и 只, и 条.")
OGD = ("只 подходит большинству животных, но лошадь считают через 匹, корову через 头, а рыбу "
       "через 条.")

# ------------------------------------------------- данные: один список на всё
# животное, чтение, перевод, классификатор, хозяйственное ли, длинное ли, пометка
ANIMALS = [
    ("猫", "māo", "кошка", "只", False, False, ""),
    ("鸟", "niǎo", "птица", "只", False, False, ""),
    ("鸡", "jī", "курица", "只", False, False, ""),
    ("老虎", "lǎohǔ", "тигр", "只", False, False, ""),
    ("狗", "gǒu", "собака", "只", False, False, "встречается и 条"),
    ("牛", "niú", "корова", "头", True, False, ""),
    ("猪", "zhū", "свинья", "头", True, False, ""),
    ("大象", "dàxiàng", "слон", "头", True, False, ""),
    ("鱼", "yú", "рыба", "条", False, True, ""),
    ("蛇", "shé", "змея", "条", False, True, ""),
    ("马", "mǎ", "лошадь", "匹", True, False, "исключение"),
]
CLS = [
    ("只", "zhī", "почти все животные: некрупные, птицы, дикие звери"),
    ("头", "tóu", "хозяйственные животные и слон"),
    ("条", "tiáo", "длинное и гибкое тело"),
    ("匹", "pǐ", "только лошади"),
]
CHAIN = [("Это лошадь?", "匹"), ("Длинное и гибкое тело?", "条"), ("Крупный скот?", "头")]
DEFAULT = "只"

known = [c[0] for c in CLS]
assert len(CLS) == 4 and DEFAULT in known, "четыре классификатора, 只 среди них"
assert len(CHAIN) == len(known) - 1, "вопросов на один меньше, чем ответов"
assert all(a in known for q, a in CHAIN), "каждый вопрос ведёт к классификатору"
for zh, py, ru, cl, herd, long_, note in ANIMALS:
    assert cl in known, "у %s неизвестный классификатор" % zh
    assert zh and py and ru, "у %s заполнены не все поля" % zh
assert [a[0] for a in ANIMALS if a[6] == "исключение"] == ["马"], "исключение одно — лошадь"
assert all("峰" != a[3] for a in ANIMALS), "峰 не подтвердилось"
for herd in (False, True):
    for long_ in (False, True):
        box = [a for a in ANIMALS if a[4] == herd and a[5] == long_ and a[6] != "исключение"]
        assert len(set(a[3] for a in box)) <= 1, \
            "в одной группе разные классификаторы: %s" % [a[0] for a in box]

cls_rows = "\n".join(
    '    <tr><td><b class="han">%s</b></td><td>%s</td><td>%s</td><td>%s</td></tr>'
    % (zh, py, about,
       ", ".join('<span class="han">%s</span> %s' % (a[0], a[2])
                 for a in ANIMALS if a[3] == zh))
    for zh, py, about in CLS)

animal_rows = "\n".join(
    '    <tr><td><b class="han">%s</b></td><td>%s</td><td>%s</td>'
    '<td><span class="han">一%s%s</span></td><td>%s</td></tr>'
    % (zh, py, ru, cl, zh, note or "—") for zh, py, ru, cl, herd, long_, note in ANIMALS)

chain_items = "\n".join(
    '  <li><b>%s</b> — тогда <span class="han">%s</span>.</li>' % (q, a) for q, a in CHAIN)

# ------------------------------------------------- ошибки
ERRORS = [
    ("一头狗", "一只狗", "头 закреплено за хозяйственными животными, собака идёт с 只."),
    ("一只马", "一匹马", "У лошади собственный классификатор, и заменить его на 只 нельзя."),
    ("一个猫", "一只猫", "Универсальное 个 с животными звучит небрежно: для них есть свои слова."),
    ("一只鱼", "一条鱼", "Рыба попадает в группу длинных и гибких, а там работает 条."),
    ("两牛", "两头牛", "Между числом и животным классификатор обязателен, пропустить его нельзя."),
]
assert len(ERRORS) == 5, "ошибок должно быть пять"
err_rows = "\n".join(
    '    <tr><td><b class="han">%s</b></td><td><b class="han">%s</b></td><td>%s</td></tr>'
    % e for e in ERRORS)

STORY = """<div class="story">
  <b>Из личного опыта</b>
  <p>Ученица рассказывала о своей собаке и сказала <span class="han">一头狗</span>.</p>
  <p>Логика была понятной: на прошлом занятии мы разбирали <span class="han">一头牛</span>, и она решила, что <span class="han">头</span> годится для всех четвероногих покрупнее кошки.</p>
  <p><b>Разобрали по группам.</b> <span class="han">头</span> закреплено за хозяйственными животными — коровами, свиньями, — а собака идёт с <span class="han">只</span>.</p>
  <p>Дальше был хороший вопрос: а где проходит граница? Собака ведь крупнее курицы, а иногда и свиньи.</p>
  <p>Оказалось, что размер тут ни при чём. Тигр крупнее свиньи, но считается через <span class="han">只</span>, а свинья — через <span class="han">头</span>. Дело не в величине, а в том, к какой группе язык относит животное.</p>
  <p>После этого разбора ошибка не повторялась: достаточно было перестать мерить животных глазами и запомнить три исключения.</p>
</div>"""

FAQ = [
 ("Какое счётное слово для животных в китайском?",
  "По умолчанию 只 (zhī): оно подходит кошкам, птицам, курам и даже тиграм. Исключений три: "
  "лошадей считают через 匹 (pǐ), хозяйственных животных и слона — через 头 (tóu), а длинных "
  "и гибких, вроде рыбы и змеи, — через 条 (tiáo). Если ни одно из трёх не подошло, берите "
  "只 — не ошибётесь."),
 ("Какое счётное слово для собаки?",
  "Основной вариант — 只: 一只狗 «одна собака», 两只狗 «две собаки». Встречается и 条, "
  "особенно в разговорной речи, и это не ошибка: язык здесь допускает оба варианта. Для "
  "начала надёжнее держаться 只, потому что оно уместно всегда."),
 ("Почему лошадь считают через 匹?",
  "Это исключение, которое не выводится ни из размера, ни из формы тела. Лошадь — "
  "хозяйственное животное, и по логике ей подошло бы 头, но закреплено за ней именно 匹: "
  "一匹马. Такие случаи просто запоминают — их в этой теме всего ничего."),
 ("Можно ли везде говорить 个?",
  "В разговоре 个 действительно подставляют почти ко всему, и вас поймут. Но с животными это "
  "звучит небрежно: для них есть свои слова, и носитель их использует. На экзамене или в "
  "письменной речи 一个猫 будет считаться ошибкой."),
 ("Чем 头 отличается от 只?",
  "Группой животных, а не их размером. 头 ставят с хозяйственными животными — коровой, "
  "свиньёй — и со слоном. 只 подходит всем остальным, включая крупных диких: тигр идёт "
  "именно с 只, хотя он больше свиньи. Мерить животных глазами здесь не работает."),
 ("Как сказать «две кошки» и «три рыбы»?",
  "两只猫 (liǎng zhī māo) и 三条鱼 (sān tiáo yú). Обратите внимание на два момента: "
  "классификатор между числом и животным обязателен, пропустить его нельзя, и перед "
  "классификатором ставится 两, а не 二."),
]
assert len(FAQ) == 6, "вопросов должно быть шесть"

faq_vis = "\n".join(
    '  <details class="ksfaq-item">\n'
    '    <summary class="ksfaq-q"><span>%s</span><i class="ksfaq-chev"></i></summary>\n'
    '    <div class="ksfaq-a"><p>%s</p></div>\n'
    '  </details>' % (q, a) for q, a in FAQ)

faq_ld = ",\n".join(
    '        {"@type": "Question", "name": "%s", "acceptedAnswer": {"@type": "Answer", "text": "%s"}}'
    % (q, a) for q, a in FAQ)

HEAD = """<!DOCTYPE html>
<html lang="ru">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>%(title)s</title>
<meta name="description" content="%(desc)s">
<link rel="canonical" href="%(u)s%(slug)s">
<meta property="og:type" content="article">
<meta property="og:title" content="%(title)s">
<meta property="og:description" content="%(ogd)s">
<meta property="og:url" content="%(u)s%(slug)s">
<meta property="og:image" content="%(hero)s">
<meta property="og:image:alt" content="%(heroalt)s">
<meta property="og:site_name" content="Kitai School">
<meta property="og:locale" content="ru_RU">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="%(title)s">
<meta name="twitter:description" content="%(ogd)s">
<meta name="twitter:image" content="%(hero)s">
<meta name="robots" content="index, follow, max-image-preview:large, max-snippet:-1">

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "BlogPosting",
      "@id": "%(u)s%(slug)s#article",
      "headline": "%(title)s",
      "description": "Разбор счётных слов для животных в китайском языке. По умолчанию работает 只 (zhī): оно подходит кошкам, птицам, курам и крупным диким зверям вроде тигра. Три группы выпадают из этого правила: лошадей считают через 匹 (pǐ), хозяйственных животных и слона — через 头 (tóu), длинных и гибких, таких как рыба и змея, — через 条 (tiáo). В статье показано, по каким признакам закреплена каждая группа, почему размер животного не работает как подсказка, что делать с собакой, у которой встречаются оба варианта, и как выбрать нужное слово за три вопроса.",
      "image": "%(hero)s",
      "inLanguage": "ru",
      "datePublished": "2026-11-09",
      "dateModified": "2026-11-09",
      "author": {"@id": "https://kitai-school.ru/#yulia-goryaina"},
      "publisher": {"@id": "https://kitai-school.ru/#org"},
      "mainEntityOfPage": "%(u)s%(slug)s",
      "about": {
        "@type": "Thing",
        "name": "Счётные слова для животных в китайском языке"
      }
    },
    {
      "@type": "Person",
      "@id": "https://kitai-school.ru/#yulia-goryaina",
      "name": "Юлия Горяина",
      "url": "https://kitai-school.ru/about",
      "jobTitle": "Китаист, лингвокоуч, основатель Kitai School",
      "worksFor": {"@id": "https://kitai-school.ru/#org"},
      "alumniOf": {"@type": "CollegeOrUniversity", "name": "Шаньдунский университет (山东大学)"},
      "description": "Китаист и лингвокоуч, докторант Шаньдунского университета (山大), преподаватель МГУ ВШБ, более 20 лет практики. Основатель международной лицензированной онлайн-школы Kitai School.",
      "image": "https://static.tildacdn.com/tild3265-6431-4361-a262-343162663636/DSC01652_1.jpg"
    },
    {
      "@type": "EducationalOrganization",
      "@id": "https://kitai-school.ru/#org",
      "name": "Kitai School",
      "url": "https://kitai-school.ru",
      "description": "Международная лицензированная онлайн-школа китайского языка: групповые и индивидуальные занятия, подготовка к HSK и HSKK.",
      "sameAs": ["https://t.me/kitai_school"]
    },
    {
      "@type": "FAQPage",
      "@id": "%(u)s%(slug)s#faq",
      "mainEntity": [
%(faqld)s
      ]
    },
    {
      "@type": "BreadcrumbList",
      "@id": "%(u)s%(slug)s#breadcrumbs",
      "itemListElement": [
        {"@type": "ListItem", "position": 1, "name": "Главная", "item": "https://kitai-school.ru"},
        {"@type": "ListItem", "position": 2, "name": "Блог", "item": "https://kitai-school.ru/blog"},
        {"@type": "ListItem", "position": 3, "name": "%(title)s", "item": "%(u)s%(slug)s"}
      ]
    }
  ]
}
</script>
""" % dict(title=TITLE, desc=DESC, ogd=OGD, u=U, slug=SLUG, faqld=faq_ld, hero=HERO,
           heroalt=HERO_ALT)

BODY = """<body>
<div id="ks-wrap">
<main id="ks-art">
<article>
<p class="eyebrow">Письменность и грамматика</p>
<h1>Счётное слово для животных: <span class="italic">почему <span class="han">只</span> подходит кошке, но не лошади</span></h1>

<div class="byline">
  <a href="https://kitai-school.ru/about" target="_blank" rel="noopener"><img src="https://static.tildacdn.com/tild3265-6431-4361-a262-343162663636/DSC01652_1.jpg" alt="Юлия Горяина, основатель Kitai School"></a>
  <div>
    <div class="n">Юлия Горяина</div>
    <div class="r">Китаист, докторант Шаньдунского университета (山大), основатель Kitai School</div>
    <time datetime="2026-11-09">9 ноября 2026</time>
  </div>
</div>

<figure class="ks-hero"><img src="HERO_SRC" alt="HERO_ALT" width="1200" height="630"></figure>

<p class="passport">Вы выучили, что животных в китайском считают через <span class="han">只</span>, и спокойно говорите <span class="han">两只猫</span>. Потом доходите до лошади, пробуете <span class="han">一只马</span> — и оказывается, что так не говорят. Исключений тут немного, всего три группы, и каждая закреплена по своему признаку. Разберём их по порядку.</p>

<div class="tldr">
  <b>Коротко</b>
  <p><b>По умолчанию <span class="han">只</span></b> — кошки, птицы, куры, даже тигры. Три исключения: <b><span class="han">匹</span></b> для лошадей, <b><span class="han">头</span></b> для хозяйственных животных и слона, <b><span class="han">条</span></b> для длинных и гибких — рыбы и змеи. Размер животного подсказкой не служит: тигр крупнее свиньи, но идёт с <span class="han">只</span>.</p>
</div>

<h2>Короткий ответ: <span class="italic">по умолчанию 只</span></h2>

<p>Начну с того, что работает в большинстве случаев.</p>

<p><b><span class="han">只</span> (zhī) — основной классификатор для животных.</b> <span class="han">一只猫</span> «одна кошка», <span class="han">两只鸟</span> «две птицы», <span class="han">三只鸡</span> «три курицы». Если вы не знаете, какое слово поставить, и животное не из трёх особых групп, <span class="han">只</span> будет верным выбором.</p>

<p>Важная деталь, которая снимает половину вопросов: <b><span class="han">只</span> годится не только для мелких</b>. Тигр и панда тоже считаются через него.</p>

<p>Дальше посмотрим на три группы, которые из этого правила выпадают. И сразу предупрежу главное заблуждение: угадать их по размеру не получится.</p>

<h2>只: <span class="italic">кошки, птицы и почти все остальные</span></h2>

<p>Эта группа самая большая, и границы у неё простые.</p>

<ul>
  <li><span class="han">一只猫</span> — кошка, <span class="han">一只狗</span> — собака.</li>
  <li><span class="han">一只鸟</span> — птица, <span class="han">一只鸡</span> — курица.</li>
  <li><span class="han">一只老虎</span> — тигр, <span class="han">一只熊猫</span> — панда.</li>
</ul>

<p>Обратите внимание на последнюю строку. <b>Тигр — крупное животное, но классификатор у него тот же, что у кошки.</b> Это первое указание на то, что размер здесь ничего не решает.</p>

<p>У <span class="han">只</span> есть и вторая работа, не связанная с животными: им считают один предмет из пары — <span class="han">一只鞋</span> «один ботинок». Про это и про остальные классификаторы у нас есть отдельный разбор: SCHETN_LINK.</p>

<h2>头: <span class="italic">хозяйственные животные</span></h2>

<p>Первая группа, которая выпадает из общего правила.</p>

<p><b><span class="han">头</span> (tóu) ставят с хозяйственными животными:</b> <span class="han">一头牛</span> «одна корова», <span class="han">一头猪</span> «одна свинья». Сюда же относят слона — <span class="han">一头大象</span>.</p>

<p>Само слово <span class="han">头</span> означает «голова», и счёт скота по головам в русском устроен так же: «десять голов скота». Но на этом сходство заканчивается — в китайском это полноценный классификатор, а не оборот речи.</p>

<p><b>Где проходит граница.</b> Собака крупнее курицы и иногда крупнее поросёнка, но в эту группу не входит: она идёт с <span class="han">只</span>. Дело не в том, насколько животное велико, а в том, относится ли оно к хозяйственным.</p>

<h2>Четыре группы по признакам: <span class="italic">сводка</span></h2>

<p>Соберём все четыре в одну таблицу.</p>

<div class="table-wrap">
<table>
  <caption>Четыре классификатора для животных и то, что в каждую группу входит.</caption>
  <thead><tr><th>Слово</th><th>Чтение</th><th>Признак группы</th><th>Кто входит</th></tr></thead>
  <tbody>
CLS_ROWS
  </tbody>
</table>
</div>

<p>Третий столбец важнее остальных: именно признак, а не список, позволяет разобраться с животным, которого в таблице нет.</p>

<figure class="ks-fig"><img src="FIG_SRC" alt="FIG_ALT" width="1200" height="600"><figcaption>Два признака, которые работают: хозяйственное животное или нет и какой формы тело. Лошадь из этой разметки выпадает.</figcaption></figure>

<p>Посмотрите на нижнюю правую клетку — она пустая. Длинных и гибких хозяйственных животных в обиходе нет, и клетке просто нечего содержать.</p>

<p><b>А теперь главное наблюдение по этой картинке.</b> Строки делят животных не по размеру, а по тому, держат их в хозяйстве или нет. Когда я собирала эту разметку по размеру, тигр оказался в одной клетке с коровой — и сразу стало видно, что признак выбран неверно.</p>

<h2>条: <span class="italic">длинное и гибкое</span></h2>

<p>Вторая группа-исключение, и она определяется формой тела.</p>

<p><b><span class="han">条</span> (tiáo) ставят с длинными и гибкими:</b> <span class="han">一条鱼</span> «одна рыба», <span class="han">一条蛇</span> «одна змея».</p>

<p>Этот же классификатор работает и за пределами животного мира — с дорогами, реками, брюками, то есть со всем вытянутым. Так что группа запоминается легко: если тело длинное и гнётся, берите <span class="han">条</span>.</p>

<p><b>И отдельный случай, про который чаще всего спрашивают, — собака.</b> Основной вариант у неё <span class="han">只</span>, но в речи встречается и <span class="han">一条狗</span>. Это не ошибка: язык здесь допускает оба варианта. Для начала надёжнее держаться <span class="han">只</span> — оно уместно всегда.</p>

STORY_HTML

<p>Случай показательный: ученица выбирала классификатор на глаз, по размеру животного. <b>Именно так эта тема и не работает.</b></p>

<h2>匹: <span class="italic">лошадь, которая стоит особняком</span></h2>

<p>Третье исключение — и единственное, которое ниоткуда не выводится.</p>

<p><b><span class="han">匹</span> (pǐ) закреплено за лошадьми:</b> <span class="han">一匹马</span> «одна лошадь», <span class="han">两匹马</span> «две лошади».</p>

<p>По логике ей подошло бы <span class="han">头</span>: лошадь — животное хозяйственное, держат её рядом с коровами. Но язык распорядился иначе, и своё слово у неё отдельное.</p>

<p><b>Объяснять это происхождением знака я не буду.</b> Версии встречаются разные, подтвердить ни одну мне не удалось, поэтому честнее сказать прямо: это исключение, которое запоминают.</p>

<p>Хорошая новость в том, что оно одно. Запомнить одну пару «лошадь — <span class="han">匹</span>» проще, чем выучить длинный список.</p>

<h2>Как выбрать <span class="italic">за три вопроса</span></h2>

<p>Вот порядок, по которому я советую идти, пока группы не улягутся в голове.</p>

<ul>
CHAIN_ITEMS
  <li><b>Ни одно не подошло</b> — ставьте <span class="han">只</span>.</li>
</ul>

<p>Порядок вопросов важен: лошадь стоит первой именно потому, что она исключение и по другим признакам определилась бы неверно.</p>

<p>Вот как это выглядит на знакомых животных.</p>

<div class="table-wrap">
<table>
  <caption>Одиннадцать животных с их классификаторами и примерами.</caption>
  <thead><tr><th>Знак</th><th>Чтение</th><th>Перевод</th><th>Как считают</th><th>Пометка</th></tr></thead>
  <tbody>
ANIMAL_ROWS
  </tbody>
</table>
</div>

<p>И ещё одно, что к животным относится напрямую: <b>перед классификатором «два» — это <span class="han">两</span>, а не <span class="han">二</span></b>. <span class="han">两只猫</span>, а не <span class="han">二只猫</span>. Про числа у нас есть отдельная статья: CIFRY_LINK.</p>

<h2>Частые ошибки <span class="italic">русскоязычных</span></h2>

<p>Соберём те, что встречаются в тетрадях чаще других.</p>

<div class="table-wrap">
<table>
  <caption>Пять ошибок со счётными словами для животных и причина каждой.</caption>
  <thead><tr><th>Как говорят</th><th>Как надо</th><th>В чём дело</th></tr></thead>
  <tbody>
ERR_ROWS
  </tbody>
</table>
</div>

<p><b>Первые две — попытка вывести слово из размера животного.</b> Третья и четвёртая — подстановка универсального <span class="han">个</span> и выбор по привычному значению.</p>

<p>Пятая стоит особняком: это не выбор не того слова, а пропуск классификатора вообще. Между числом и животным он обязателен, и это правило исключений не знает.</p>

<h2>Чего в статье <span class="italic">нет намеренно</span></h2>

<ul>
  <li><b>Нет <span class="han">峰</span> для верблюдов:</b> подтверждений этому классификатору я не нашла и приводить его не стала.</li>
  <li><b>Нет редких классификаторов</b> для отдельных зверей: источники дают их по-разному, а там, где они есть, <span class="han">只</span> обычно подходит.</li>
  <li><b>Нет этимологии <span class="han">匹</span> и <span class="han">头</span></b> — версии происхождения подтвердить не удалось.</li>
  <li><b>Нет общей теории классификаторов</b> — зачем они нужны, как устроено универсальное <span class="han">个</span>, что такое глагольные счётные слова: это в отдельной статье, на неё стоит ссылка.</li>
  <li><b>Нет данных о том, какой классификатор встречается чаще:</b> корпусных подсчётов найти не удалось.</li>
</ul>

<p>И главный вывод. <b>Классификатор определяется группой, а не размером животного</b>, и групп этих всего четыре.</p>

<p>Польза простая: дальше вы будете выбирать слово за секунду — по трём вопросам, а не по тому, насколько зверь большой на вид.</p>

<div class="cta">
  <p>Такие вещи быстрее всего закрепляются на своих фразах про своих же питомцев: <a href="https://kitai-school.ru/onlayn-kursy-kitayskogo" target="_blank" rel="noopener">онлайн-курсы китайского</a>. <a href="#popup:zayavka">Оставить заявку</a> или написать нам в <a href="https://telegram.me/manager_kitai_school" target="_blank" rel="noopener">Telegram</a>.</p>
</div>

<h2>Частые <span class="italic">вопросы</span> (FAQ)</h2>
<div class="ksfaq__list">
FAQ_VIS
</div>

<p class="sign">Пусть классификатор находится с первого раза! <span class="han">加油</span>！</p>

<div class="sources">
  <h2>Источники</h2>
  <ol>
    <li><b><span class="han">只</span> как основной классификатор для животных</b>, включая птиц и крупных диких зверей вроде тигра и панды, — по разборам китайской грамматики.</li>
    <li><b><span class="han">匹</span> для лошадей</b> — там же, названо как закреплённое за одним видом.</li>
    <li><b><span class="han">头</span> для хозяйственных животных и слона</b> — по тем же источникам, где перечислены коровы, свиньи и слоны.</li>
    <li><b><span class="han">条</span> для длинных и гибких</b> — рыба и змея приводятся как стандартные примеры.</li>
    <li><b>Собака с двумя вариантами, <span class="han">只</span> и <span class="han">条</span></b>, — оба названы в разборах, и ни один не помечен как ошибочный.</li>
    <li><b><span class="han">峰</span> для верблюдов не приводится:</b> подтверждений найти не удалось.</li>
    <li><b>Этимология знаков не приводится:</b> версии происхождения <span class="han">匹</span> и <span class="han">头</span> подтвердить не удалось.</li>
    <li><b>Сопоставления частоты классификаторов нет:</b> подсчётов по корпусу найти не удалось.</li>
    <li>Случай с собакой — из занятий Kitai School; имени и клички не называю.</li>
  </ol>
</div>

</article>
</main>
SIDE_HTML
</div>
"""

REPL = [
    ("HERO_SRC", HERO), ("HERO_ALT", HERO_ALT),
    ("FIG_SRC", FIG), ("FIG_ALT", FIG_ALT),
    ("FAQ_VIS", faq_vis),
    ("CLS_ROWS", cls_rows), ("ANIMAL_ROWS", animal_rows), ("CHAIN_ITEMS", chain_items),
    ("ERR_ROWS", err_rows),
    ("STORY_HTML", STORY), ("SIDE_HTML", SIDE),
    ("SCHETN_LINK", L("schetnye-slova-v-kitayskom-yazyke", "счётные слова в китайском языке")),
    ("CIFRY_LINK", L("cifry-ot-0-do-10-na-kitayskom", "цифры от 0 до 10 на китайском")),
]
for a, b in REPL:
    BODY = BODY.replace(a, b)

out = HEAD + css + "\n</head>\n" + BODY + sticky + "\n</body>\n</html>\n"
open(OUT, "w", encoding="utf-8").write(out)

art = out[out.index('<main id="ks-art">'):out.index('</main>')]


def share(a):
    return 100.0 * art.index(a) / len(art)


vis = re.sub(r"<[^>]+>", " ", art)

print("файл          ", len(out))
print("art           ", len(art))
print("инфографика   %.2f %%" % share('<figure class="ks-fig"'))
print("история       %.2f %%" % share('<div class="story"'))
print("животных      ", len(ANIMALS), "| классификаторов", len(CLS), "| ошибок", len(ERRORS))
print("峰 в тексте   ", vis.count("峰"))
print("div баланс    ", out.count("<div"), out.count("</div>"))
print("p баланс      ", len(re.findall(r"<p[ >]", out)), out.count("</p>"))
print("прямых кавычек", vis.count('"'))
print("h2            ", out.count("<h2>"))
