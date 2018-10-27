#!/usr/bin/env python3

import re

log_final = open('Log.final.out','r')
log = open('Log.out','r')
#contents_log = log.read()
#contents_log_final = log_final.read()
'''
for line in log:
	if re.search(r'readFilesIn\s+(.+\.fq )\s+(.+\.fq)',line):
		found = re.search(r'readFilesIn\s+(.+\.fq )\s+(.+\.fq)',line) 
		print(found.group(1))
		print(found.group(2))
		break
	#print('File one is named: ',filein1)
	#print('File two is named: ',filein2)
'''
for line in log:
	for (file1,file2) in re.findall(r'readFilesIn\s+(.+\.fq )\s+(.+\.fq)',line):
		break
print('File one is named: ',file1)
print('File two is named: ',file2) 
			

















