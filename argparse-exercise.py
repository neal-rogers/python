#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""This program demonstrates the function and usage of the argparse module
at https://docs.python.org/2.7/howto/argparse.html"""


import argparse

parser = argparse.ArgumentParser()
#parser.add_argument("echo", help="echo the string you use here")
#args = parser.parse_args()
#print args.echo

#parser.add_argument("square", help="display a square of a given number",
#                    type=int)
#args = parser.parse_args()
#print args.square**2

parser.add_argument("--verbosity", help="increase output verbosity",
                    action="store_true")
parser.add_argument("square", help="display a square of a given number",
                    type=int)
args = parser.parse_args()
answer = args.square**2
if args.verbosity == 2:
    print "the square of {} equals {}".format(args.square, answer)
elif args.verbosity == 1:
    print "()^2 == {}".format(args.square, answer)
else:
    print answer