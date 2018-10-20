#!/usr/bin/env python3

import re

#nobody_file = open('Python_07_nobody.txt','r')

#coordinates = []
#counter = 0

#for line in nobody_file:
#	found = re.search(r'Nobody',line)
#	counter += 1
#	print('Line number :',counter,found)	

philia = open('Philia.txt','w')
nobody_file = open('Python_07_nobody.txt','r')

for line in nobody_file:
	line = line.rstrip()#can not have this and not have \n at the end and it will also work but to be proper should include these
	new_name = re.sub(r'Nobody', 'Philia', line)
	philia.write(new_name+'\n')








