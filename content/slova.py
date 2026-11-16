# -*- coding: utf-8 -*-
"""Данные к статье «Список слов HSK по уровням».

Числа накопительные: сколько слов нужно знать к концу уровня, а не
сколько добавляется на нём. Прибавка считается, а не вписывается.
"""

# уровень → словарь по прежнему стандарту (накопительно)
OLD = [(1, 150), (2, 300), (3, 600), (4, 1200), (5, 2500), (6, 5000)]

# уровень → словарь по действующему стандарту (накопительно)
NEW = [(1, 300), (2, 500), (3, 1000), (4, 2000), (5, 3600), (6, 5400)]
NEW_TOP = ("7–9", 11000)          # верхняя ступень считается одной полосой

# черновик 2021 года: цифры, которые до сих пор ходят по сети
DRAFT = [(1, 500), (2, 1272), (3, 2245)]
DRAFT_YEAR = 2021
FINAL_MONTH = "ноябрь 2025"
FINAL_WHEN = "ноябре 2025 года"   # предложный падеж для текста

# признаки списка, собранного по устаревшему черновику
STALE_SIGNS = [
    ("первый уровень на 500 слов", "в действующем словнике их 300"),
    ("второй уровень за тысячу", "действующая цифра — 500"),
    ("третий уровень за две тысячи", "действующая цифра — 1000"),
]

# ----------------------------------------------------------------- расчёты
LEVELS = [lvl for lvl, w in OLD]
OLD_D = dict(OLD)
NEW_D = dict(NEW)

# во сколько раз действующий словник тяжелее прежнего на каждом уровне
RATIO = {lvl: round(NEW_D[lvl] / OLD_D[lvl], 2) for lvl in LEVELS}

# прибавка на уровне: разница с предыдущим
def steps(table):
    out, prev = [], 0
    for lvl, total in table:
        out.append((lvl, total, total - prev))
        prev = total
    return out


OLD_STEPS = steps(OLD)
NEW_STEPS = steps(NEW)

# недельная норма: прибавка уровня, разложенная на полгода занятий
import math
WEEKS = 26
PER_WEEK = {lvl: math.ceil(add / WEEKS) for lvl, total, add in NEW_STEPS}

DRAFT_D = dict(DRAFT)
DRAFT_GAP = {lvl: DRAFT_D[lvl] - NEW_D[lvl] for lvl, w in DRAFT}

# ----------------------------------------------------------------- проверки
assert LEVELS == list(range(1, 7)), "уровни идут подряд с первого по шестой"
assert [lvl for lvl, w in NEW] == LEVELS, "в обеих шкалах одни и те же уровни"

assert all(w > 0 for lvl, w in OLD + NEW + DRAFT), "все объёмы положительные"
assert [w for lvl, w in OLD] == sorted(w for lvl, w in OLD), "прежняя шкала растёт"
assert [w for lvl, w in NEW] == sorted(w for lvl, w in NEW), "действующая шкала растёт"
assert NEW_TOP[1] > NEW_D[6], "верхняя ступень выше шестого уровня"

assert all(NEW_D[lvl] > OLD_D[lvl] for lvl in LEVELS), \
    "действующий словник тяжелее прежнего на каждом уровне"
assert RATIO[1] == 2.0, "на первом уровне слов ровно вдвое больше"
assert RATIO[6] < 1.1, "на шестом уровне разница почти исчезает"
assert [RATIO[lvl] for lvl in LEVELS] == sorted((RATIO[lvl] for lvl in LEVELS), reverse=True), \
    "разрыв между шкалами сокращается от уровня к уровню"

assert all(add > 0 for lvl, total, add in OLD_STEPS + NEW_STEPS), "прибавка всегда больше нуля"
assert OLD_STEPS[0][2] == 150 and NEW_STEPS[0][2] == 300, "первый уровень набирают с нуля"

assert [lvl for lvl, w in DRAFT] == [1, 2, 3], "черновик сравниваем на первых трёх уровнях"
assert all(DRAFT_D[lvl] > NEW_D[lvl] for lvl, w in DRAFT), \
    "черновик требовал больше, чем действующий словник"
assert DRAFT_GAP[2] > DRAFT_GAP[1], "расхождение с черновиком растёт ко второму уровню"
assert len(STALE_SIGNS) == 3 and all(a and b for a, b in STALE_SIGNS), \
    "у каждого признака устаревшего списка названа действующая цифра"
assert FINAL_WHEN.startswith("ноябре"), "в тексте дата стоит в предложном падеже"

assert WEEKS == 26, "норма считается на полгода занятий"
assert all(v > 0 for v in PER_WEEK.values()), "недельная норма везде положительная"
assert PER_WEEK[2] < PER_WEEK[1], "на втором уровне норма ниже, чем на первом"
assert PER_WEEK[6] == max(PER_WEEK.values()), "самая тяжёлая неделя — на шестом уровне"
assert PER_WEEK[6] > 3 * PER_WEEK[1], "к шестому уровню норма вырастает в разы"
