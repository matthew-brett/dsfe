#!/usr/bin/env python
""" Write class template
"""

import sys
from os.path import join as pjoin, dirname
from string import Template

from num2words import num2words

DAYS = pjoin(dirname(__file__), '..', 'days')

template = Template("""\
---
layout: single
title: Class $day_no
permalink: /days/class_$day_no
---

# Day $day_no (the $day_ord day)

## Announcements

* TBA

## Schedule

* TBA

## Assignment

TBA
""")


def main():
    for num in sys.argv[1:]:
        th_day = num2words(int(num) + 1, ordinal=True)
        fname = pjoin(DAYS, f'class_{num}.md')
        print(f"Writing {fname}")
        with open(fname, 'wt') as fobj:
            fobj.write(template.substitute(day_no=num, day_ord=th_day))


if __name__ == '__main__':
    main()
