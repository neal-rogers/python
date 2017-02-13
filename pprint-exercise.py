#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""This program demonstrates the function and usage of the argparse module
at https://pymotw.com/2/pprint/"""

data = [ (i, {'a':'A',
              'b':'B',
              'c':'C',
              'd':'D',
              'e':'E',
              'f':'F',
              'g':'G',
              'h':'H',
              })
         for i in xrange(3)
         ]

from pprint import pprint
from pprint_data import data
