#!/usr/bin/env python3

from Bio import SeqIO
import sys
import re

fasta_file = ''

class SequenceError(Exception):
	pass

try:
	fasta_file = sys.argv[1]#input the file name on the command line
	print('User provided file name:', fasta_file)#confirm the file name inputted
	if not fasta_file.endswith('.fasta'):#if it's not a fasta file, an error will be raised
		raise ValueError('Not a FASTA file')
	FASTA = open(fasta_file, 'r')#if it's not an error, then it will open/parse the file
	open_FASTA = SeqIO.parse(FASTA, 'fasta')
	for seq_record in open_FASTA:
		if re.findall(r'[^ATCGN]',str(seq_record.seq)):
			raise SequenceError('Sequence contains characters other than ACTGN')
	else:
		print(seq_record.id,'frame-1-codons')
		print(' '.join(re.findall(r'(.{1,3})',str(seq_record.seq))))
except ValueError:#raisint the value error that we created
	print('File needs to be a FASTA file.') 
except SequenceError:
	print('Sequences can only contain ACTGN characters')
except IndexError:#if a file was not inputted on the command line
	print('Please provide a file name.')
except IOError:#if the fasta file is not in that directory or the path is not given
	print("Can\'t find file:", fasta_file)
'''
for seq_record in open_FASTA:#printing the sequence name and the codons for frame 1
	print(seq_record.id,'frame-1-codons')
	print(' '.join(re.findall(r'(.{1,3})',str(seq_record.seq))))#first have to string the sequence record so that findall recognizes it, specifying in the findall to look for 1-3 nucleotides (to form a codon); findall puts everything it finds into a list, so using join to join the components of the list into a string separated only by a whitespace
'''



'''

line = line.rstrip()
	found = re.search(r'^>(/S+)',line)
	if found:	
		gene_reference = found.group(1)
		replacement_gene_ref = re.sub(r'gene_reference','gene_reference' '-frame_1-codons', line)
		header_change = []
'''
