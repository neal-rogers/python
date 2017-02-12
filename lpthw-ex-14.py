#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""This program simply prints output."""


from sys import argv

script, user_name, age = argv
prompt = '> '

print "Hi %s, I'm the %s script." % (user_name, script)
print "I'd like to ask you a few questions."
print "Do you like me %s?" % user_name,
likes = raw_input(prompt)

print "Where do you live, %s?" % user_name,
lives = raw_input(prompt)

print "What kind of computer do you have?",
computer = raw_input(prompt)

print "This last question is about your %s." % age
print "What is your %s?" % age,
age = raw_input(prompt)

print """
Alright, so you said %r about liking me.
You live in %r. Not sure where that is.
You have a %r computer. Nice.
And you are %r years old. Wow.
""" % (likes, lives, computer, age)