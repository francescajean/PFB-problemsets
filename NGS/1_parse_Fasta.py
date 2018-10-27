#!/usr/bin/env python3

from Bio import SeqIO
#from Bio import Seq

fasta_file = 'human_cds.fasta'

id_dict = SeqIO.to_dict(SeqIO.parse(fasta_file, 'fasta'))

for seq in id_dict:
	seqrecord = id_dict[seq]#seqrecord is an object
	seqid = seqrecord.id#tells us that from seqrecord, we want to pull the id (ie. gene name) (is an object but treated as a string)
	sequence = seqrecord.seq#tells us that from seqrecord, we want to pull the sequence (is an object but is treated as a string with SeqIO)
	total_length = len(sequence)#finds the total length of the sequence
	g_count = sequence.count('G')#finds g content
	c_count = sequence.count('C')#finds c content
	gc_content = (g_count+c_count)/total_length#finds gc content
	gc_content_perc = '{:.2%}'.format(gc_content)#converts to pretty
	print(seqid+'\t'+gc_content_perc)#prints each component

print(id_dict)

