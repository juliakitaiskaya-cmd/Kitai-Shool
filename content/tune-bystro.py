# -*- coding: utf-8 -*-
# Точечное усиление опубликованной статьи «Как быстро выучить китайский».
# Новая страница по брифу не создаётся: бриф повторяет её тайтл и все три обещания.
# 1) чиним битую ссылку на несуществующую kursy-kitajskogo-dlya-vzroslyh
# 2) вписываем свободную вариацию ключа «быстро научиться китайскому языку» в FAQ
#    — в видимый блок и в JSON-LD одновременно, чтобы они остались слово в слово
import os

os.chdir("/home/user/Kitai-Shool/content/blog")
F = "kak-bystro-vyuchit-kitayskiy.html"
s = open(F, encoding="utf-8").read()
before = len(s)

# 1. битая ссылка
OLD_LINK = ('<a href="https://kitai-school.ru/article/kursy-kitajskogo-dlya-vzroslyh" target="_blank" '
            'rel="noopener">курсы китайского для взрослых</a>')
NEW_LINK = ('<a href="https://kitai-school.ru/onlayn-kursy-kitayskogo" target="_blank" '
            'rel="noopener">онлайн-курсы китайского</a>')
if OLD_LINK in s:
    s = s.replace(OLD_LINK, NEW_LINK)
    print("ссылка починена")

# 2. вариация ключа в FAQ (видимый блок и JSON-LD)
OLD_Q = "Как быстро выучить китайский с нуля?"
NEW_Q = "Как быстро научиться китайскому языку с нуля?"
assert s.count(OLD_Q) == 2, s.count(OLD_Q)
s = s.replace(OLD_Q, NEW_Q)
print("вопрос FAQ переформулирован, вхождений заменено: 2")

open(F, "w", encoding="utf-8").write(s)
print("файл %d (было %d)" % (len(s), before))
