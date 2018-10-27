#!/usr/bin/env python3

seq = open('Python_06.seq.txt','r')

#contents = seq.read()
#print(contents)

seqdict = {}

for line in seq:	
	line = line.rstrip()
	seqName,sequence = line.split()
	seq_lower = sequence.lower()
	seq_lower.replace('a','T')
	seq_lower_a = seq_lower.replace('a','T')
	seq_lower_a.replace('t','A')
	seq_lower_at = seq_lower_a.replace('t','A')
	seq_lower_at.replace('g','C')
	seq_lower_atg = seq_lower_at.replace('g','C')
	seq_lower_atg.replace('c','G')
	seq_lower_atgc = seq_lower_atg.replace('c','G')
	seq_lower_atgc[::-1]
	rev_comp = seq_lower_atgc[::-1]
	seqdict[seqName]=rev_comp

for item in seqdict:
	print(item + '\t'+ seqdict[item])

#print(seqdict)
seq.close()
