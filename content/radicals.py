# -*- coding: utf-8 -*-
"""Список 214 классических ключей.

Знаки и их порядок берутся прямо из блока «Kangxi Radicals» стандарта Юникода
(U+2F00–U+2FD5): в нём ровно 214 символов, расположенных по номерам
классического списка. Русские значения заданы здесь по официальным именам
Юникода вида KANGXI RADICAL HEART.
"""
import unicodedata

START, END = 0x2F00, 0x2FD5
CHARS = [chr(c) for c in range(START, END + 1)]
NAMES = [unicodedata.name(c).replace("KANGXI RADICAL ", "") for c in CHARS]

assert len(CHARS) == 214, "ключей должно быть 214, в блоке %d" % len(CHARS)
assert NAMES[0] == "ONE" and NAMES[-1] == "FLUTE", "блок начинается и кончается не тем"

# русские значения по именам Юникода
RU = {
    "ONE": "один", "LINE": "вертикальная черта", "DOT": "точка",
    "SLASH": "откидная черта", "SECOND": "второй знак цикла", "HOOK": "крюк",
    "TWO": "два", "LID": "крышка", "MAN": "человек", "LEGS": "ноги",
    "ENTER": "входить", "EIGHT": "восемь", "DOWN BOX": "рамка, открытая вниз",
    "COVER": "покров", "ICE": "лёд", "TABLE": "столик",
    "OPEN BOX": "рамка, открытая вверх", "KNIFE": "нож", "POWER": "сила",
    "WRAP": "обёртка", "SPOON": "ложка", "RIGHT OPEN BOX": "короб",
    "HIDING ENCLOSURE": "укрытие", "TEN": "десять", "DIVINATION": "гадание",
    "SEAL": "печать", "CLIFF": "обрыв", "PRIVATE": "своё", "AGAIN": "снова",
    "MOUTH": "рот", "ENCLOSURE": "ограда", "EARTH": "земля", "SCHOLAR": "учёный муж",
    "GO": "идти", "GO SLOWLY": "идти медленно", "EVENING": "вечер", "BIG": "большой",
    "WOMAN": "женщина", "CHILD": "ребёнок", "ROOF": "крыша", "INCH": "вершок",
    "SMALL": "малый", "LAME": "хромой", "CORPSE": "тело", "SPROUT": "росток",
    "MOUNTAIN": "гора", "RIVER": "река", "WORK": "работа", "ONESELF": "сам",
    "TURBAN": "платок", "DRY": "сухой", "SHORT THREAD": "нить",
    "DOTTED CLIFF": "навес", "LONG STRIDE": "длинный шаг", "TWO HANDS": "две руки",
    "SHOOT": "стрелять", "BOW": "лук", "SNOUT": "рыло", "BRISTLE": "щетина",
    "STEP": "шаг", "HEART": "сердце", "HALBERD": "секира", "DOOR": "дверь",
    "HAND": "рука", "BRANCH": "ветвь", "RAP": "стучать", "SCRIPT": "письмена",
    "DIPPER": "ковш", "AXE": "топор", "SQUARE": "сторона", "NOT": "не",
    "SUN": "солнце", "SAY": "говорить", "MOON": "луна", "TREE": "дерево",
    "LACK": "нехватка", "STOP": "остановка", "DEATH": "смерть", "WEAPON": "оружие",
    "DO NOT": "не надо", "COMPARE": "сравнивать", "FUR": "шерсть", "CLAN": "род",
    "STEAM": "пар", "WATER": "вода", "FIRE": "огонь", "CLAW": "коготь",
    "FATHER": "отец", "DOUBLE X": "черты гадания", "HALF TREE TRUNK": "половина ствола",
    "SLICE": "дощечка", "FANG": "клык", "COW": "корова", "DOG": "собака",
    "PROFOUND": "тёмный", "JADE": "яшма", "MELON": "тыква", "TILE": "черепица",
    "SWEET": "сладкий", "LIFE": "жизнь", "USE": "применять", "FIELD": "поле",
    "BOLT OF CLOTH": "отрез ткани", "SICKNESS": "болезнь", "DOTTED TENT": "шаг в стороны",
    "WHITE": "белый", "SKIN": "кожа", "DISH": "блюдо", "EYE": "глаз",
    "SPEAR": "копьё", "ARROW": "стрела", "STONE": "камень", "SPIRIT": "алтарь",
    "TRACK": "след", "GRAIN": "злак", "CAVE": "пещера", "STAND": "стоять",
    "BAMBOO": "бамбук", "RICE": "рис", "SILK": "шёлк", "JAR": "кувшин",
    "NET": "сеть", "SHEEP": "баран", "FEATHER": "перо", "OLD": "старый",
    "AND": "и", "PLOW": "соха", "EAR": "ухо", "BRUSH": "кисть", "MEAT": "мясо",
    "MINISTER": "сановник", "SELF": "сам по себе", "ARRIVE": "достигать",
    "MORTAR": "ступа", "TONGUE": "язык", "OPPOSE": "расходиться", "BOAT": "лодка",
    "STOPPING": "остановиться", "COLOR": "цвет", "GRASS": "трава", "TIGER": "тигр",
    "INSECT": "насекомое", "BLOOD": "кровь", "WALK ENCLOSURE": "шагать",
    "CLOTHES": "одежда", "WEST": "запад", "SEE": "видеть", "HORN": "рог",
    "SPEECH": "речь", "VALLEY": "долина", "BEAN": "боб", "PIG": "свинья",
    "BADGER": "зверь", "SHELL": "раковина", "RED": "красный", "RUN": "бежать",
    "FOOT": "нога", "BODY": "туловище", "CART": "повозка", "BITTER": "горький",
    "MORNING": "утро", "WALK": "идти в пути", "CITY": "город", "WINE": "вино",
    "DISTINGUISH": "различать", "VILLAGE": "селение", "GOLD": "металл",
    "LONG": "длинный", "GATE": "ворота", "MOUND": "холм", "SLAVE": "раб",
    "SHORT TAILED BIRD": "короткохвостая птица", "RAIN": "дождь", "BLUE": "синий",
    "WRONG": "неверный", "FACE": "лицо", "LEATHER": "кожа выделанная",
    "TANNED LEATHER": "кожа дублёная", "LEEK": "лук-порей", "SOUND": "звук",
    "LEAF": "голова", "WIND": "ветер", "FLY": "летать", "EAT": "еда",
    "HEAD": "голова, начало", "FRAGRANT": "аромат", "HORSE": "лошадь",
    "BONE": "кость", "TALL": "высокий", "HAIR": "волосы", "FIGHT": "драться",
    "SACRIFICIAL WINE": "жертвенное вино", "CAULDRON": "котёл", "GHOST": "дух умершего",
    "FISH": "рыба", "BIRD": "птица", "SALT": "солончак", "DEER": "олень",
    "WHEAT": "пшеница", "HEMP": "конопля", "YELLOW": "жёлтый", "MILLET": "просо",
    "BLACK": "чёрный", "EMBROIDERY": "вышивка", "FROG": "лягушка",
    "TRIPOD": "треножник", "DRUM": "барабан", "RAT": "крыса", "NOSE": "нос",
    "EVEN": "ровный", "TOOTH": "зуб", "DRAGON": "дракон", "TURTLE": "черепаха",
    "FLUTE": "флейта",
}

missing = [n for n in NAMES if n not in RU]
assert not missing, "нет русского значения для: %s" % missing[:5]
assert all(RU[n].strip() for n in NAMES), "пустое значение в словаре"

# разбивка по числу черт: (черт, номер первого, номер последнего)
GROUPS = [
    (1, 1, 6), (2, 7, 29), (3, 30, 60), (4, 61, 94), (5, 95, 117),
    (6, 118, 149), (7, 150, 169), (8, 170, 179), (9, 180, 188),
    (10, 189, 191), (11, 192, 194), (12, 195, 196), (13, 197, 200),
    (14, 201, 202), (15, 203, 204), (16, 205, 206), (17, 207, 208),
    (18, 209, 209), (19, 210, 210), (20, 211, 211), (21, 212, 212),
    (22, 213, 213), (23, 214, 214),
]

assert GROUPS[0][1] == 1 and GROUPS[-1][2] == 214, "группы должны покрывать весь список"
total = 0
prev_end = 0
for strokes, a, b in GROUPS:
    assert a == prev_end + 1, "разрыв в номерах перед группой из %d черт" % strokes
    assert b >= a, "группа из %d черт задана наоборот" % strokes
    total += b - a + 1
    prev_end = b
assert total == 214, "сумма по группам даёт %d вместо 214" % total
assert [g[0] for g in GROUPS] == sorted(g[0] for g in GROUPS), "черты должны расти"

# обычные иероглифы вместо символов-ключей: знаки блока ключей есть не во всех
# шрифтах, а у каждого из них в Юникоде прописан обычный эквивалент
PLAIN = []
for c in CHARS:
    d = unicodedata.decomposition(c)
    assert d.startswith("<compat>"), "у ключа %s нет обычного эквивалента" % c
    PLAIN.append(chr(int(d.split()[-1], 16)))
assert len(PLAIN) == 214, "эквивалентов должно быть 214"
assert PLAIN[84] == "水", "ключ 85 — это 水"

# итоговый список: (номер, знак, число черт, русское значение)
RADICALS = []
for strokes, a, b in GROUPS:
    for num in range(a, b + 1):
        RADICALS.append((num, PLAIN[num - 1], strokes, RU[NAMES[num - 1]]))

assert len(RADICALS) == 214, "в итоговом списке %d строк" % len(RADICALS)
assert [r[0] for r in RADICALS] == list(range(1, 215)), "номера идут не подряд"
assert RADICALS[84][1] == "水" and RADICALS[84][2] == 4, "у ключа 85 — 水 и четыре черты"
assert RADICALS[84][3] == "вода", "ключ 85 — вода"

COUNTS = [(strokes, b - a + 1) for strokes, a, b in GROUPS]
MAXG = max(c for _, c in COUNTS)
assert MAXG == 34, "самая большая группа — четыре черты, 34 ключа"

if __name__ == "__main__":
    print("ключей:", len(RADICALS), "| групп:", len(GROUPS), "| самая большая:", MAXG)
    for strokes, n in COUNTS:
        print("  %2d черт: %2d" % (strokes, n))
