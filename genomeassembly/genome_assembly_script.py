#!/usr/bin/env python3

from Bio import SeqIO

open_fasta = open('ecoliPB-filtered_0.50.contigs.fasta','r')

list_lengths = []

for seq_record in SeqIO.parse(open_fasta,'fasta'):
#	print('ID', seq_record.id)
#	print('len{}'.format(len(seq_record)))
	list_lengths.append(len(seq_record))

list_lengths.sort()
print('The number of contigs is:', len(list_lengths))
print('The shortest contig is', list_lengths[0], 'nucleotides.')
print('The longest contig is', list_lengths[-1], 'nucleotides.')
list_lengths.reverse()
print(list_lengths)

genome_length = sum(list_lengths)
print('The genome size is:',genome_length)

#contig_length = 0
contig_list = []

for item in list_lengths:
	contig_list.append(item)
	if sum(contig_list) > int(genome_length)/2:
		print(int(genome_length)/2)
		print(sum(contig_list))
		print('The N50 is',contig_list[-1], 'nucleotides.')
		print('The L50 is',len(contig_list),'contigs.')	 
		break






