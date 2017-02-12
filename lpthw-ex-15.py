#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""This program reads a file and does stuff."""


from sys import argv

#script, filename = argv

print "Enter the filename:"
filename = raw_input("> ")

txt = open(filename)

print "Here's your file %r:" % filename
print txt.read()

txt.close()
open(filename)

print "Type the filename again:"
file_again = raw_input("> ")

txt_again = open(file_again)

print txt_again.read()
txt_again.close()