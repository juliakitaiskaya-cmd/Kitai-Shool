# -*- coding: utf-8 -*-
"""Данные к статье «Учебники HSK: какой том брать на своём уровне».

VOLUMES — том серии HSK Standard Course: уровень, метка тома, уроков, слов.
None означает, что цифру подтвердить не удалось: в тексте и на картинке
она так и остаётся непроставленной, а не додумывается.
"""

SERIES_NAME = "HSK Standard Course"
SERIES_CN = "HSK标准教程"
EDITOR = "Цзян Липин"
EDITOR_CN = "姜丽萍"
LEVELS_IN_SERIES = 6

# уровень, метка тома, уроков, слов в томе
VOLUMES = [
    (1, "1", 15, 150),
    (2, "2", None, None),
    (3, "3", 20, None),
    (4, "4A", 10, 300),
    (4, "4B", None, None),
    (5, "5A", 18, 1200),
    (5, "5B", None, None),
    (6, "6A", 20, 1300),
    (6, "6B", None, None),
]

# из чего состоит комплект одного тома
KIT = [
    ("учебник", "основная книга: тексты, лексика, грамматика", True),
    ("рабочая тетрадь", "упражнения к каждому уроку", True),
    ("книга для преподавателя", "ход урока, ключи и тексты аудирования", False),
]

# как устроено аудио
AUDIO = [
    ("код на задней обложке", "в изданиях последних лет запись берут по нему"),
    ("диск в комплекте", "в более ранних изданиях запись шла отдельным диском"),
]

# ----------------------------------------------------------------- расчёты
LEVELS = sorted(set(lvl for lvl, tag, les, w in VOLUMES))
VOLS_PER_LEVEL = {lvl: sum(1 for v in VOLUMES if v[0] == lvl) for lvl in LEVELS}
ONE_VOLUME = [lvl for lvl in LEVELS if VOLS_PER_LEVEL[lvl] == 1]
TWO_VOLUMES = [lvl for lvl in LEVELS if VOLS_PER_LEVEL[lvl] == 2]

TOTAL_VOLUMES = len(VOLUMES)
BOOKS_PER_VOLUME = len(KIT)
TOTAL_BOOKS = TOTAL_VOLUMES * BOOKS_PER_VOLUME

KNOWN = [v for v in VOLUMES if v[3] is not None]
UNKNOWN = [v for v in VOLUMES if v[3] is None]
NEEDED = [name for name, what, need in KIT if need]

# ----------------------------------------------------------------- проверки
assert LEVELS == list(range(1, LEVELS_IN_SERIES + 1)), "уровни серии идут подряд с первого"
assert ONE_VOLUME == [1, 2, 3], "на младших уровнях том один"
assert TWO_VOLUMES == [4, 5, 6], "с четвёртого уровня томов два"
assert TOTAL_VOLUMES == 9, "томов в серии девять"
assert BOOKS_PER_VOLUME == 3 and TOTAL_BOOKS == 27, "три книги на том, двадцать семь всего"

assert all(tag[-1] in "AB" for lvl, tag, les, w in VOLUMES if lvl in TWO_VOLUMES), \
    "тома уровней с двумя книгами помечены буквами"
assert all(tag.isdigit() for lvl, tag, les, w in VOLUMES if lvl in ONE_VOLUME), \
    "тома младших уровней помечены только цифрой"
assert len(set(tag for lvl, tag, les, w in VOLUMES)) == TOTAL_VOLUMES, "метки томов не повторяются"

assert len(KNOWN) == 4, "словарь подтверждён ровно по четырём томам"
assert len(UNKNOWN) == 5, "по остальным пяти цифру не подтвердили"
assert [v[1] for v in KNOWN] == ["1", "4A", "5A", "6A"], "подтверждены первый том и первые половины"
assert all(v[3] is None for v in VOLUMES if v[1].endswith("B")), \
    "ни по одному второму тому цифры нет"

WORDS = [v[3] for v in KNOWN]
assert WORDS == sorted(WORDS), "по подтверждённым томам словарь растёт с уровнем"
assert WORDS[-1] // WORDS[0] >= 8, "между первым томом и шестым разрыв в разы"

assert len(NEEDED) == 2, "ученику нужны две книги из трёх"
assert "книга для преподавателя" not in NEEDED, "третья книга — не для ученика"
assert len(AUDIO) == 2, "два способа получить запись"
