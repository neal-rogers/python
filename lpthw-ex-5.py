#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""This program simply prints output."""


name = "Zed A. Shaw"
age = 35 # not a lie
height = 74 # inches
weight = 180 # lbs
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'
mheight = height * 2.54
mweight = weight / 2.2

print "Let's talk about %s." % name
print "He's %d inches tall." % height
print "He's %d pounds heavy." % weight
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth

print "If I add %d, %d, and %d I get %d." % (age, height, weight,
                                             age + height + weight)

print "His height is %d centimeters and his weight is %d kilograms." % (mheight, mweight)
