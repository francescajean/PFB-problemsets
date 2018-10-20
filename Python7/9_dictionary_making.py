#!/usr/bin/env python3

import re

re_file = open('bionet.txt','r')

enzy_dict = {}

for line in re_file:	
	line = line.rstrip()
	for (enzyme,cutsite) in re.findall(r'^(\w.*?)\s{4,}(.*[A-Z^])$',line):
		enzy_dict[enzyme] = cutsite
#print(enzy_dict)

for (e,c) in enzy_dict.items():
	print(e,'\t',c)







			#cutsite = found.group(3)
			#enzy_dict[enzyme] = cutsite
#print(enzy_dict)
#file.close()








