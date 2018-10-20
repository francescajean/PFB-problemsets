 #!/usr/bin/env python3

import re

fasta = open('Python_07.fasta.txt','r')

for line in fasta:
	line = line.strip()#
	for (sequencename,description) in re.findall('([A-Z]\d{5}\.\d)\|(.+)', line):
		print('id: ', sequencename)
		print('description: ', description)	
	
#for line in fasta:	
#	line = line.strip()
#	if re.findall('([A-Z]\d{5}\.\d)\|(.+)',line):	
			


#	else:
#		print('sequence: ',line)


