#!/usr/bin/env python3

fasta = open('Python_06.fastq.txt','r')

linedict = {}

total_char = 0
total_lines = 0

for char in fasta:
	char = char.rstrip()
	char_count = len(char)
	total_char  += char_count

fasta = open('Python_06.fastq.txt','r')
for line in fasta:
	line = line.rstrip()	
	total_lines += 1

average = total_char/total_lines

print('The total number of characters is ',total_char, 'characters.')
print('The total number of lines is ',total_lines,'lines.')
print('The average number of characters per line is ',average,'charcters.')

#total_lines = 0
#for 
