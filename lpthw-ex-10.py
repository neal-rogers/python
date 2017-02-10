#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""This program simply prints output."""


tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."

fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""

lazy_cat = "\v This is a vertical tab."
silly_cat = "This line has a carriage return right \r here."
dumb_cat = "This line has an ASCII bell right \a here."


print tabby_cat
print persian_cat
print backslash_cat
print fat_cat
print lazy_cat
print silly_cat
print dumb_cat

while True:
    for i in ["/","-","|","\\","|"]:
        print "%s\r" % i,
