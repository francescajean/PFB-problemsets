#!/usr/bin/env python3

import re

header = open('Python_07.fasta.txt','r')

for line in header:
	line = line.strip()
	headers = re.findall(r'>.+',line)
	if headers:  
		print(headers)





