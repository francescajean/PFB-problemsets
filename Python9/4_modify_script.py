#!/usr/bin/env python3

import sys
import re

def split_line(line,line_count):#creating a new definition, should be at top with other methods
	regex = (r'[ATGC]{1,'+str(line_count)+'}')
	line = line.replace('\n','')
	changed_line = re.findall(regex,line)
	sequence = '\n'.join(changed_line)
	return sequence

class NotFastaError (Exception):#establishing an exception error
	pass

dna = ''#making the file called into a string

try:	#trying to pull the file from the command line, gets returned with errors if the file input isn't
	dna = sys.argv[1]#correct or if an input/output error
	print('User submitted file name: ', dna)
	if not dna.endswith('.fasta'):
		raise NotFastaerror('Not a fasta file.')
	FASTA = open(dna,'r')
except NotFastaError:
	print('File needs to be a FASTA file and end with .fasta')
except IOError as ex:
	print('Can\'t find file: ', fasta_file, ':', ex.sterror)

line_count = sys.argv[2]#sets up the second input from command line to be the number the sequence breaks on

big_dictionary = {}#creating an empty dictionary

for line in FASTA:#starts going through the opened file from the command line
	line = line.rstrip()#strips the newline from the end
	found = re.search(r'^>(.+)',line)#regex to find  the header
	if found:#if header found, puts it as the key in big dictionary
		gene_name = found.group(1)
		big_dictionary[gene_name] = ''
	else:#if header not found, adds the line(ie. sequence) and adds each line to the value of the key
		big_dictionary[gene_name] += line
for gene_name in big_dictionary:#for every value in the dictionary, performing the created definition
	function_line = split_line(big_dictionary[gene_name],line_count)#see definition above
	print(gene_name+'\n'+function_line)#printing the gene_name from the dictionary and the changed seq





		






