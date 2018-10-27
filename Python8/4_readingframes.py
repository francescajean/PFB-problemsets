#!/usr/bin/env python3

import sys
import re
from Bio import SeqIO

fasta_file = ''
fasta_file = sys.argv[1]
FASTA = open(fasta_file,'r')
open_FASTA = SeqIO.parse(FASTA,'fasta')

reading_frame = sys.argv[2]

for seq_record in open_FASTA:
	print(seq_record.id,'frame-',(int(reading_frame)+1),'-codons')
	int_reading_frame = int(reading_frame)
	sequence = seq_record.seq
	sequence_frame = sequence[int_reading_frame:]
	str_sequence_frame = str(sequence_frame)
	find_all_codons = re.findall(r'(.{1,3})',str_sequence_frame)
	joined_codons = ' '.join(find_all_codons)
	print(joined_codons)

#for position in range(0,len(seq_record.seq)):
#	position_end = position+3

#print(___.id,'frame-'reading_frame'codons')	


