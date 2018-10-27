f#!/usr/bin/env python3

import sys
import re
#import pysam
from Bio import SeqIO

kmer_size = sys.argv[1]
input_file = sys.argv[2]
top_kmer_number = sys.argv[3]

kmer_dict = {}
list_sequences = []

for seq_record in SeqIO.parse(input_file,'fastq'):
	sequences = str(seq_record.seq)
	seq_strip = sequences.rstrip()
	list_sequences.append(seq_strip)
#print(list_sequences)
#print(len(seq_strip))

for sequence in list_sequences:
	sequence = list(sequence)
	for position in range(0,len(sequence)):
		position_end = position+8
		if position_end <= len(sequence):
			kmer_list = sequence[position:position_end]
			kmer_str = ''.join(kmer_list)
			if kmer_str not in kmer_dict.keys():
				kmer_dict[kmer_str] = 1
			else:
				kmer_dict[kmer_str] += 1

#print(kmer_dict)

kmer_sorted = sorted(kmer_dict, key=kmer_dict.get, reverse=True)

top_kmer = kmer_sorted[0:10]

for kmer in top_kmer:
	print(kmer,'\t',kmer_dict[kmer])

#print(kmer_sorted)








