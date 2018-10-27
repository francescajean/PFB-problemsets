#!/usr/bin/env python3

import sys

def reverse_comp(dna):
	dna_upper = dna.upper()
	a = dna_upper.replace('A','t')
	c = a.replace('C','g')
	g = c.replace('G','c')
	t = g.replace('T','a')	
	return t[::-1]

sequence1 = sys.argv[1]
sequence2 = sys.argv[2]
count = sys.argv[3]
length = len(sequence1)

score = 0

print('Your options for sequences to reverse complement are: both, seq1, seq2, or neither')
chosen_seq = input("Choose which sequence to reverse complement: ")

if chosen_seq == "both":
	sequence1 = reverse_comp(sequence1)
	sequence2 = reverse_comp(sequence2)
elif chosen_seq == "seq1":
	sequence1 = reverse_comp(sequence1)
elif chosen_seq == "seq2":
	sequence2 = reverse_comp(sequence2)

for index in range(0,length):
	if sequence1[index] == sequence2[index]:
		score += int(count)
	else:
		score -= int(count)
print(score)
		








