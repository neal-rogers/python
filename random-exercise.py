#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""This program does stuff."""


import random


for i in xrange(5):
    # this prints a random float 5 times.
    print '%04.3f' % random.random()

for i in xrange(5):
    # this prints a random float 5 times in a range from 1-100.
    print '%04.3f' % random.uniform(1, 100)

print '[1, 100]:'
for i in range(3):
    # this prints integers 3 times in a range from 1-100.
    print random.randint(1, 100)

print '[-5, 5]:'
for i in range(3):
    print random.randint(-5, 5)

random.seed(1)

for i in xrange(5):
    # this prints the same random floats 5 times.
    print '%04.3f' % random.random()