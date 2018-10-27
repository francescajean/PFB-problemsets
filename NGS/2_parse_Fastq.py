#!/usr/bin/env python3

from Bio import SeqIO

fastq_file = SeqIO.parse('four_reads.fastq','fastq')
'''
for entry in fastq_file:
	trimmed = entry[5:]#somehow the sequence and quality are joined (if you trim one, you trim both)
	print(trimmed.format('fastq'))#formats things somehow (some sort of python magic going on here)
'''
#haven't figured this one out fully yet, later problem
greater = 0
under = 0

for entry in fastq_file:
	for quality in entry.letter_annotations:
		for qual in :
			if qual > 30:
				greater += 1
			else:
				under += 1
			fraction = greater/under
			fraction_perc = '{:.2%}'.format(fraction)
		print(entry.id+'\t'+fraction_perc)
				




