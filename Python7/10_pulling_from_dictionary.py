#!/usr/bin/env python3

#this is almost doing the thing (test before committing)
import sys
import re

dictionary = open('new_reference.txt','r')

enzyme = sys.argv[1]
#cutsite = sys.argv[2]

for line in dictionary:
	if enzyme in line:
		split_line = line.split('\t')
		print('This enzyme cuts at: ', split_line[1])
	else:
		print('This enzyme is not in the dictionary.')
#print('This enzyme cuts at: ', split_line[1])
