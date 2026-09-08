# -*- coding: utf-8 -*-
"""Сборка блока для Tilda: python3 rebuild.py <slug>

Из <slug>.html (полная страница) делает <slug>.TILDA.html — один блок T123:
<style> … </style> + JSON-LD + <div id="ks-wrap"> … </div> + скрипт sticky.
Мета-теги в блок не попадают: они живут в настройках страницы Tilda.
"""
import re, sys, os

D = os.path.join(os.path.dirname(os.path.abspath(__file__)), "blog")


def build(name):
    src = open(os.path.join(D, name + ".html"), encoding="utf-8").read()

    style = re.search(r"<style>.*?</style>", src, re.S).group(0)
    ld = re.search(r'<script type="application/ld\+json">.*?</script>', src, re.S).group(0)
    wrap = re.search(r'<div id="ks-wrap">.*\n</div>', src, re.S).group(0)
    sticky = re.search(r"<script>\s*/\* Kitai School — sticky.*?</script>", src, re.S).group(0)

    tilda = style + "\n" + ld + "\n" + wrap[: wrap.rfind("\n</div>")] + "\n" + sticky + "\n</div>"

    opens, closes = tilda.count("<div"), tilda.count("</div>")
    ok = "OK" if opens == closes else "MISMATCH"
    open(os.path.join(D, name + ".TILDA.html"), "w", encoding="utf-8").write(tilda)
    return "%s: chars=%d div=%d/%d %s footer=%d" % (
        name, len(tilda), opens, closes, ok, tilda.count("site-footer"))


if __name__ == "__main__":
    for n in sys.argv[1:]:
        print(build(n))
