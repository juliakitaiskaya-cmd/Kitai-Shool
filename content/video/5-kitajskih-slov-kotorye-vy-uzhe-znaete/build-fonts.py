#!/usr/bin/env python3
"""Складывает fonts.css и fonts/*.woff2 для video.html.

Тянет шрифты с Google Fonts один раз, чтобы рендер потом шёл офлайн.
Запуск: python3 build-fonts.py
"""
import os
import re
import urllib.parse
import urllib.request

# полная строка UA обязательна: по короткой Google отдаёт ttf без разбивки на поднаборы
UA = ('Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
      '(KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36')
HERE = os.path.dirname(os.path.abspath(__file__))

# латиница нужна для пиньиня (латиница-ext — из-за ā ē ī ō ū), кириллица — для русского текста
KEEP = {'latin', 'latin-ext', 'cyrillic'}

# у Noto Serif SC берём только те иероглифы, что встречаются в видео
HANZI = '茶台风关系功夫麻将加油！'

SOURCES = [
    ('https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,500;0,600;1,500;1,600'
     '&family=Inter:wght@400;500;600;700&display=swap', True),
    ('https://fonts.googleapis.com/css2?family=Noto+Serif+SC:wght@500;700&text='
     + urllib.parse.quote(HANZI), False),
]


def get(url, binary=False):
    req = urllib.request.Request(url, headers={'User-Agent': UA})
    err = None
    for _ in range(4):
        try:
            data = urllib.request.urlopen(req, timeout=60).read()
            return data if binary else data.decode()
        except Exception as e:      # сеть бывает капризной — пробуем ещё раз
            err = e
    raise err


def main():
    os.makedirs(os.path.join(HERE, 'fonts'), exist_ok=True)
    out = [
        '/* Шрифты для рендера видео: Cormorant Garamond, Inter, Noto Serif SC (Google Fonts, OFL).',
        '   Лежат рядом в fonts/ — страница рисуется офлайн, без запросов в сеть.',
        '   Пересобрать: python3 build-fonts.py (см. README.md). */',
        '',
    ]
    for url, filter_subsets in SOURCES:
        css = get(url)
        blocks = re.findall(r'(?:/\*\s*([\w-]+)\s*\*/\s*)?(@font-face\s*\{.*?\})', css, re.S)
        for subset, block in blocks:
            if filter_subsets and subset not in KEEP:
                continue
            src = re.search(r'url\((https://[^)]+)\)', block).group(1)
            family = re.search(r"font-family: '([^']+)'", block).group(1).replace(' ', '-').lower()
            weight = re.search(r'font-weight: (\d+)', block).group(1)
            italic = 'i' if 'italic' in block else ''
            name = f'{family}-{weight}{italic}-{subset or "sc"}.woff2'
            with open(os.path.join(HERE, 'fonts', name), 'wb') as f:
                f.write(get(src, binary=True))
            out.append(re.sub(r'url\(https://[^)]+\)', f'url(fonts/{name})', block))
    faces = sum(1 for line in out if line.startswith('@font-face'))
    if faces < 20:
        raise SystemExit(f'Google отдал только {faces} начертаний — похоже, ответ пришёл не в том формате')
    with open(os.path.join(HERE, 'fonts.css'), 'w') as f:
        f.write('\n'.join(out) + '\n')
    print('готово:', faces, 'начертаний')


if __name__ == '__main__':
    main()
