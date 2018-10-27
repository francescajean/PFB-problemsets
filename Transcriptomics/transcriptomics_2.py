#!/usr/bin/env python3

import sys

file_name = sys.argv[1]
open_file = open(file_name,'r')

gene_dict = {}#initializing an empty dictionary

for line in open_file:
	strip_line = line.rstrip()#for every line, remove the end white space
	split_line = strip_line.split('\t')#split the line on tabs (creates a list of each component)
	gene_name = split_line[2].split('^')#the gene name is the second index of the list but we wanna split it on the ^ to remove it
	gene = gene_name[0]#the new list of the split gene name has the gene name at the 0 index
	set_of_reads = set()#initializing the set
	transcript_read = split_line[0]#transcript read is the 0 index from the original split
	if gene not in gene_dict.keys():#now testing whether the gene (from second split) is a key in the dictionary and if it's not, we are adding it to the dictionary and creating a set
		gene_dict[gene] = set_of_reads
	else:#if it is in the dictionary, we are adding the transcript read to the set (which won't have duplicates because it is a set)
		gene_dict[gene].add(transcript_read)
#print(gene_dict)
for entry in gene_dict.keys():#to iterate over all of the entrys in the dictionary, gotta do a for loop
	print(entry, '\t\t', len(gene_dict[entry]))#print entry (which is now the key) and the length of the set (ie. how many transcript reads are in the key)	

#to make this look pretty, pipe the output to column -t
