#!/usr/bin/env python3
"""Складывает fonts.css и fonts/*.woff2 для video.html.

Иероглифы для поднабора Noto Serif SC берутся прямо из video.html.
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
KEEP = {'latin', 'latin-ext', 'cyrillic'}
CJK = re.compile(r'[　-〿一-鿿＀-￯]')

LATIN_CSS = ('https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@600;700'
             '&family=Inter:wght@500;600;700;800;900&display=swap')
HAN_CSS = 'https://fonts.googleapis.com/css2?family=Noto+Serif+SC:wght@500;700&text='


def get(url, binary=False):
    req = urllib.request.Request(url, headers={'User-Agent': UA})
    err = None
    for _ in range(4):
        try:
            data = urllib.request.urlopen(req, timeout=60).read()
            return data if binary else data.decode()
        except Exception as e:
            err = e
    raise err


def main():
    os.makedirs(os.path.join(HERE, 'fonts'), exist_ok=True)
    with open(os.path.join(HERE, 'video.html'), encoding='utf-8') as f:
        hanzi = ''.join(sorted(set(CJK.findall(f.read()))))
    out = ['/* Шрифты ролика: Inter, Cormorant Garamond, Noto Serif SC (Google Fonts, OFL).',
           '   Пересобрать: python3 build-fonts.py */', '']
    for url, filt in ((LATIN_CSS, True), (HAN_CSS + urllib.parse.quote(hanzi), False)):
        for subset, block in re.findall(r'(?:/\*\s*([\w-]+)\s*\*/\s*)?(@font-face\s*\{.*?\})', get(url), re.S):
            if filt and subset not in KEEP:
                continue
            src = re.search(r'url\((https://[^)]+)\)', block).group(1)
            family = re.search(r"font-family: '([^']+)'", block).group(1).replace(' ', '-').lower()
            weight = re.search(r'font-weight: (\d+)', block).group(1)
            name = f'{family}-{weight}-{subset or "sc"}.woff2'
            with open(os.path.join(HERE, 'fonts', name), 'wb') as f:
                f.write(get(src, binary=True))
            out.append(re.sub(r'url\(https://[^)]+\)', f'url(fonts/{name})', block))
    faces = sum(1 for line in out if line.startswith('@font-face'))
    if faces < 15:
        raise SystemExit(f'Google отдал только {faces} начертаний — ответ пришёл не в том формате')
    with open(os.path.join(HERE, 'fonts.css'), 'w') as f:
        f.write('\n'.join(out) + '\n')
    print(f'готово: {faces} начертаний, иероглифов — {len(hanzi)}')


if __name__ == '__main__':
    main()
