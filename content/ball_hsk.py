# -*- coding: utf-8 -*-
"""Данные к статье «Баллы HSK».

EXAMS — уровень, вопросов в аудировании, чтении, письме (0 — раздела нет),
максимум и порог. Цена одного вопроса считается, а не вписывается.
"""

SECTION_MAX = 100
PASS_SHARE = 0.6

EXAMS = [
    (1, 20, 20, 0),
    (2, 35, 25, 0),
    (3, 40, 30, 10),
    (4, 45, 40, 15),
    (5, 45, 45, 10),
    (6, 50, 50, 1),
]

SECTIONS = ("аудирование", "чтение", "письмо")

# ----------------------------------------------------------------- расчёты
def sections_of(lvl):
    """Сколько разделов на уровне."""
    row = dict((e[0], e) for e in EXAMS)[lvl]
    return sum(1 for n in row[1:] if n)


MAXI = {lvl: SECTION_MAX * sections_of(lvl) for lvl, a, r, w in EXAMS}
PASS = {lvl: int(round(MAXI[lvl] * PASS_SHARE)) for lvl in MAXI}
TOTAL_Q = {lvl: a + r + w for lvl, a, r, w in EXAMS}

# цена одного вопроса в каждом разделе — именно считается
PRICE = {}
for lvl, a, r, w in EXAMS:
    PRICE[lvl] = {}
    for name, n in zip(SECTIONS, (a, r, w)):
        PRICE[lvl][name] = round(SECTION_MAX / n, 1) if n else None

# пример расчёта: уровень, верных в каждом разделе
EXAMPLE = (4, 31, 28, None)

# расчёт примера — считается, а не вписывается
_lvl, _ok_a, _ok_r, _ok_w = EXAMPLE
_row = dict((e[0], e) for e in EXAMS)[_lvl]
EX_LEVEL = _lvl
EX_STEPS = [
    ("аудирование", _ok_a, _row[1], round(_ok_a * SECTION_MAX / _row[1])),
    ("чтение", _ok_r, _row[2], round(_ok_r * SECTION_MAX / _row[2])),
]
EX_TWO = sum(s[3] for s in EX_STEPS)          # сумма двух разделов
EX_PASS = PASS[_lvl]                          # порог уровня
EX_NEED = EX_PASS - EX_TWO                    # сколько добрать письмом
EX_WRITE_MAX = SECTION_MAX

# ----------------------------------------------------------------- проверки
assert len(EXAMS) == 6, "уровней шесть"
assert [e[0] for e in EXAMS] == list(range(1, 7)), "уровни идут подряд"

NO_WRITING = [lvl for lvl, a, r, w in EXAMS if not w]
WITH_WRITING = [lvl for lvl, a, r, w in EXAMS if w]
assert NO_WRITING == [1, 2], "письма нет только на первых двух уровнях"
assert WITH_WRITING == [3, 4, 5, 6], "с третьего уровня письмо есть"

assert all(MAXI[lvl] == 200 for lvl in NO_WRITING), "без письма сумма 200"
assert all(MAXI[lvl] == 300 for lvl in WITH_WRITING), "с письмом сумма 300"
assert all(PASS[lvl] == 120 for lvl in NO_WRITING), "порог 120"
assert all(PASS[lvl] == 180 for lvl in WITH_WRITING), "порог 180"

assert TOTAL_Q[1] == 40 and TOTAL_Q[2] == 60 and TOTAL_Q[3] == 80, "суммы заданий сходятся"
assert TOTAL_Q[4] == 100 and TOTAL_Q[5] == 100 and TOTAL_Q[6] == 101

# главная находка: вопрос дешевеет от уровня к уровню
LISTEN_PRICE = [PRICE[lvl]["аудирование"] for lvl, a, r, w in EXAMS]
assert LISTEN_PRICE[0] > LISTEN_PRICE[-1], "на первом уровне вопрос дороже, чем на шестом"
assert LISTEN_PRICE == sorted(LISTEN_PRICE, reverse=True), \
    "цена вопроса в аудировании падает от уровня к уровню"

# и вторая: на шестом всё письмо — одно задание
assert dict((e[0], e) for e in EXAMS)[6][3] == 1, "на шестом уровне письменное задание одно"
assert PRICE[6]["письмо"] == 100.0, "это задание весит весь раздел целиком"

assert all(PRICE[lvl]["письмо"] is None for lvl in NO_WRITING), "без письма цены нет"
assert EXAMPLE[0] in WITH_WRITING and EXAMPLE[3] is None, \
    "в примере письмо считается отдельно, а не угадывается"

assert len(EX_STEPS) == 2, "в примере считаются два раздела из трёх"
assert all(0 < ok < total for name, ok, total, ball in EX_STEPS), \
    "верных меньше, чем вопросов, и больше нуля"
assert all(0 < ball < SECTION_MAX for name, ok, total, ball in EX_STEPS), \
    "балл раздела внутри ста"
assert EX_TWO < EX_PASS, "двух разделов на порог не хватает — в этом смысл примера"
assert 0 < EX_NEED < EX_WRITE_MAX, "добрать письмом нужно, и это выполнимо"
