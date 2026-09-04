#!/usr/bin/env python3
"""Складывает fonts.css и fonts/*.woff2 для guide.html.

Тянет шрифты с Google Fonts один раз, чтобы вёрстка собиралась офлайн.
Иероглифы для поднабора Noto Serif SC берутся прямо из guide.html —
после правок текста скрипт достаточно прогнать заново.

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

# латиница нужна для пиньиня (latin-ext — из-за ā ē ī ō ū), кириллица — для русского текста
KEEP = {'latin', 'latin-ext', 'cyrillic'}

CJK = re.compile(r'[　-〿一-鿿＀-￯]')

LATIN_CSS = ('https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,500;0,600;1,500;1,600'
             '&family=Inter:wght@400;500;600;700&display=swap')
HAN_CSS = 'https://fonts.googleapis.com/css2?family=Noto+Serif+SC:wght@500;700&text='


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


def hanzi_from_guide():
    with open(os.path.join(HERE, 'guide.html'), encoding='utf-8') as f:
        return ''.join(sorted(set(CJK.findall(f.read()))))


def main():
    os.makedirs(os.path.join(HERE, 'fonts'), exist_ok=True)
    hanzi = hanzi_from_guide()
    sources = [
        (LATIN_CSS, True),
        (HAN_CSS + urllib.parse.quote(hanzi), False),
    ]
    out = [
        '/* Шрифты гайда: Cormorant Garamond, Inter, Noto Serif SC (Google Fonts, OFL).',
        '   Лежат рядом в fonts/ — вёрстка печатается офлайн, без запросов в сеть.',
        '   Пересобрать: python3 build-fonts.py (см. README.md). */',
        '',
    ]
    for url, filter_subsets in sources:
        css = get(url)
        for subset, block in re.findall(r'(?:/\*\s*([\w-]+)\s*\*/\s*)?(@font-face\s*\{.*?\})', css, re.S):
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
    print(f'готово: {faces} начертаний, иероглифов в поднаборе — {len(hanzi)}')


if __name__ == '__main__':
    main()
