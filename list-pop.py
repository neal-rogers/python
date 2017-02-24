#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""This program does stuff."""


from timeit import Timer


pop_zero = Timer("x.pop(0)", "from __main__ import x")
pop_end = Timer("x.pop()", "from __main__ import x")

print("pop(0) pop()")
for i in range(1000000,1000000,1000000):
    x = list(range(i))
    pt = pop_end.timeit(number=1000)
    x = list(range(i))
    pop_zero.timeit(number=1000)
    pz = pop_zero.timeit(number=1000)
    print("%15.5f, %15.5f" % (pz,pt))