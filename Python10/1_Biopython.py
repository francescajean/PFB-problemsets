#!/usr/bin/env python3

from Bio import SeqIO

filename = './Python_08.fasta'

#for seq_record in SeqIO.parse(filename, 'fasta'):
#	print('ID', seq_record.id)
#	print('Sequence',seq_record.seq)
#	print('Description',seq_record.description)

counts = 0

for seq_record in SeqIO.parse(filename,'fasta'):
	ids = seq_record.id
	if ids:	
		counts += 1
print(counts)







