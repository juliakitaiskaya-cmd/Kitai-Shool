# -*- coding: utf-8 -*-
"""Данные к статье «Скачать учебник HSK 2».

Издания новой серии проверены по двум независимым каталогам магазинов.
Страницу издательства я не открывала, поэтому всё, что касается изданий,
идёт со статусом «по каталогам», а не «подтверждено издателем».
"""

CONF = "подтверждено"
CATAL = "по каталогам магазинов"
DESCR = "по описаниям"
NOCONF = "подтвердить не удалось"

NEW_SERIES = "New HSK Course"
NEW_SERIES_CN = "新HSK教程"
OLD_SERIES = "HSK Standard Course"

# издания второго уровня новой серии: что, номер, когда вышло
EDITIONS = [
    ("Учебник", "9787521368048", "март 2026 года"),
    ("Рабочая тетрадь", "9787521371789", "апрель 2026 года"),
]

# что из этого бывает в электронном виде
DIGITAL = [
    ("Учебник и тетрадь целиком", False, "электронных изданий у серий нет", CONF),
    ("Цифровые материалы новой серии", True,
     "доступ к ним заявлен в описаниях изданий", DESCR),
    ("Звук к урокам", True, "открывается по коду из книги", CONF),
]

# как отличить книгу новой серии от прежней
TELL = [
    ("Название на обложке", NEW_SERIES + " против " + OLD_SERIES),
    ("Год издания", "у новой серии тома выходят в 2026 году"),
    ("Состав комплекта", "у новой серии учебник и тетрадь, пособия для учителя в наборе нет"),
]

# ----------------------------------------------------------------- расчёты
BOOK_MONTH, WB_MONTH = 3, 4          # месяцы выхода учебника и тетради
GAP_MONTHS = WB_MONTH - BOOK_MONTH
YES_DIGITAL = [d for d in DIGITAL if d[1]]
NO_DIGITAL = [d for d in DIGITAL if not d[1]]

# ----------------------------------------------------------------- проверки
assert len(EDITIONS) == 2, "у второго уровня новой серии две книги для ученика"
assert all(len(num) == 13 and num.startswith("978") for n, num, w in EDITIONS), \
    "номера изданий записаны полностью"
assert len(set(num for n, num, w in EDITIONS)) == 2, "номера у книг разные"
assert GAP_MONTHS == 1, "тетрадь вышла на месяц позже учебника"
assert EDITIONS[0][0] == "Учебник" and EDITIONS[1][0] == "Рабочая тетрадь", \
    "порядок: сначала учебник, потом тетрадь"

assert len(DIGITAL) == 3 and len(YES_DIGITAL) == 2 and len(NO_DIGITAL) == 1
assert NO_DIGITAL[0][0].startswith("Учебник и тетрадь"), \
    "целиком книг в цифре нет — это главный ответ"
assert YES_DIGITAL[0][3] == DESCR, "про цифровые материалы стоит оговорка"
assert any(d[3] == CONF for d in YES_DIGITAL), "звук подтверждён"

assert len(TELL) == 3 and all(a and b for a, b in TELL), "три признака различения"
assert NEW_SERIES in TELL[0][1] and OLD_SERIES in TELL[0][1], "названия обеих серий названы"

import re as _re
_TXT = [x for row in DIGITAL for x in row if isinstance(x, str)]
_TXT += [b for a, b in TELL] + [w for n, num, w in EDITIONS]
assert not _re.search(r"\bруб|\bцена|\bкупить за", " ".join(_TXT)), "цен в данных нет"
assert not _re.search(r"\.ru|\.com|торрент", " ".join(_TXT)), "адресов и площадок в данных нет"
