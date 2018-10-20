#!/usr/bin/env python3
 
import re

#rest_enzy_seq = open('Python_07_ApoI.fasta.txt','r')

#number 6
#for site in rest_enzy_seq:
#	site = site.rstrip()
#	sites = re.findall(r'[AG]AATT[CT]',site)
#	if sites:
#		print(sites)

#number 7
'''rest_enzy_seq = open('Python_07_ApoI.fasta.txt','r')
new_string = ''
for line in rest_enzy_seq:
	line = line.rstrip()
	if not re.search(r'^>',line):#if the line doesn't contain the > at the beginning which denotes the sequence identifier, then we are going to do the following	
		replace_sites = re.sub(r'([AG])(AATT[CT])', r'\1^\2',line)#gunna sub the two subpatterns with the identified pattern and include a carrot between the two patterns
		
	split = replace_sites.split('^')
	print(split)#printing the sequence with the new substitution
'''
rest_enzy_seq = open('Python_07_ApoI.fasta.txt','r')

new_string = ''
for line in rest_enzy_seq:
	line = line.rstrip()
	if not re.search(r'^>',line):
		new_string += line	
print(new_string)
replace_sites = re.sub(r'([AG])(AATT[CT])',r'\1^\2',new_string)
cut_replace_sites = replace_sites.split('^')
print(cut_replace_sites)


	
