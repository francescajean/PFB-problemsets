#!/usr/bin/env python3

#import Bio

class DNARecord(object):	
	
	def __init__(self, sequence, gene_name, species_name):
		self.sequence = sequence
		self.gene_name = gene_name
		self.species_name = species_name

	def seq_length(self):
		length = len(self.sequence)
		return length
	
	def nucleotide_composition(self):
		a_count = self.sequence.count('A')
		t_count = self.sequence.count('T')
		g_count = self.sequence.count('G')
		c_count = self.sequence.count('C')
		counts ='A:'+str(a_count), 'T:'+str(t_count), 'G:'+str(g_count), 'C:'+str(c_count)
		return counts

	def gc_content(self):
		total_length = len(self.sequence)
		g_count = self.sequence.count('G')
		c_count = self.sequence.count('C')
		gc_content = (g_count + c_count)/total_length
		gc_content_perc = '{:.2%}'.format(gc_content)
		return gc_content_perc

	def FASTA(self):
		header = '>{}'.format(self.gene_name)
		dna_seq = '{}'.format(self.sequence)
		fasta_format = header+'\n'+dna_seq
		return fasta_format

fav_gene = DNARecord('ATGCCTAGTCGTACGTA', 'unc119', 'Danio rerio')

for d in [fav_gene]:
	print('name:', d.gene_name, ' ', 'species name:', d.species_name)
	
print('length:',DNARecord.seq_length(fav_gene))

print(DNARecord.FASTA(fav_gene))

print(DNARecord.nucleotide_composition(fav_gene))

print('GC content:',DNARecord.gc_content(fav_gene))










