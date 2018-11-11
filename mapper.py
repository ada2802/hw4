#!/usr/bin/python

import sys

for line in sys.stdin:
    data = line.strip().split("\t")
    if len(data) == 6:
       date, time, store, item, cost, payment = data
       # mapper code for Quiz: Sales per Category
       print "{0}\t{1}".format(item, cost)
