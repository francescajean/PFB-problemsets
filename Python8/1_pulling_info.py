#!/usr/bin/env python3

import sys
import re

'''
class NotFastaError (Exception):
	pass

fasta_file = ''

try:
	fasta_file = sys.argv[1]
	print('User submitted file name: ', fasta_file)
	if not fasta_file.endswith('.fasta'):
		raise NotFastaError('Not a fasta file.')
	FASTA = open(fasta_file, 'r')
	for line in FASTA:
		line = line.rstrip()
		print(line)
except NotFastaError:
	print('File needs to be a FASTA file and end with .fa')
except IOError as ex:
	print('Can\'t find file: ', fasta_file,':', ex.strerror)
'''

fasta_file = ''
fasta_file = sys.argv[1]

FASTA = open(fasta_file,'r')

big_dictionary = {}
not_nuc = []

for line in FASTA:
	line = line.rstrip()
	found = re.search(r'^>(\S+)',line)
	if found:
		gene_name = found.group(1)
		big_dictionary[gene_name] = {'A' : 0 , 'T': 0,'G': 0,'C': 0}
	else:
		for nt in line:
			if nt in big_dictionary[gene_name]:
				big_dictionary[gene_name][nt] += 1	
			else:	
				not_nuc.append(nt)
print(big_dictionary)
print(not_nuc)


fasta_file = ''
fasta_file = sys.argv[1]

FASTA = open(fasta_file, 'r')

for line in FASTA:
	line = line.rstrip()
	found = re.search(r'^>(/S+)',line)
	if found:	
		gene_reference = found.group(1)
		replacement_gene_ref = re.sub(r'gene_reference','gene_reference' '-frame_1-codons', line)
		header_change = []
		












