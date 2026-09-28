#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Проверка внутренних ссылок против adresa-sayta.tsv.

    python3 check-links.py               # весь блог
    python3 check-links.py <slug> ...    # только эти статьи

Печатает каждую ссылку, которой нет в списке реальных адресов сайта,
и возвращает код 1. Ссылку, которой нет в списке, ставить нельзя.
"""
import os, re, sys, glob

HERE = os.path.dirname(os.path.abspath(__file__))
BLOG = os.path.join(HERE, "blog")
LIST = os.path.join(HERE, "adresa-sayta.tsv")
HOST = "https://kitai-school.ru"


def load():
    articles, pages = set(), set()
    with open(LIST, encoding="utf-8") as f:
        for line in f:
            if line.startswith("#") or not line.strip():
                continue
            kind, addr = line.rstrip("\n").split("\t")[:2]
            (articles if kind == "article" else pages).add(addr)
    return articles, pages


def targets(argv):
    if argv:
        return [os.path.join(BLOG, a.removesuffix(".html") + ".html") for a in argv]
    return [f for f in sorted(glob.glob(os.path.join(BLOG, "*.html")))
            if ".TILDA" not in os.path.basename(f)]


def main():
    articles, pages = load()
    bad = 0
    for path in targets(sys.argv[1:]):
        name = os.path.basename(path)
        own = None
        text = open(path, encoding="utf-8").read()
        m = re.search(r'rel="canonical" href="%s/article/([^"]+)"' % HOST, text)
        if m:
            own = m.group(1)
            if own not in articles:
                print("%s: собственный адрес %s не найден в списке" % (name, own))
                bad += 1
        for href in re.findall(r'href="([^"]+)"', text):
            if not href.startswith(HOST):
                continue
            tail = href[len(HOST):].split("#")[0].split("?")[0]
            if tail.startswith("/article/") and tail != "/article/":
                slug = tail[len("/article/"):].rstrip("/")
                if slug not in articles:
                    print("%s: ссылка на несуществующую статью %s" % (name, slug))
                    bad += 1
            elif tail not in pages:
                print("%s: ссылка на неизвестную страницу %s" % (name, tail))
                bad += 1
    print("нарушений: %d" % bad)
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
