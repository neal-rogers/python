#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""This program simply prints output."""


print "How old are you?",
age = raw_input()
print "How tall are you?",
height = raw_input()
print "How much do you weigh?",
weight = raw_input()
print "What is your favorite color?",
fcolor = raw_input()


print "So, you're %r old, %r tall, %r heavy, and your favorite color is %r." % (
    age, height, weight, fcolor
)
