#!/usr/bin/env python3

all_genes = open('alpaca_allgenes.tsv','r')
stem_cell = open('alpaca_stemcellproliferation_genes.tsv','r')
pig_genes = open('alpaca_pigmentation_genes.tsv','r')

#set_all_genes = set(all_genes)
#print(set_all_genes)

#set_stem_cell = set(stem_cell)
#set_pig_genes = set(pig_genes)

#clean_set_all_genes = set_all_genes.discard('Gene stable ID')
#print(clean_set_all_genes)

#print('The number of genes in alpacas is ',len(set_all_genes))
#print('The number of stem cell proliferation genes in alpacas is ',len(set_stem_cell))

all_genes_set = set()

if line in all_genes:
	line.startswith('ENS')
	all_genes_set.add(line)

prolif_genes_set = set()

if line in stem_cell:
	line.startswith('ENS')
	prolif_genes_set.add(line)

pig_genes_set = set()

if line in pig_genes:
	line.startswith('ENS')
	pig_genes_set.add(line)

non_cell_prolif_genes = all_genes_set - prolif_genes_set
print('The number of genes that are not stem cell proliferation genes is ',len(non_cell_prolif_genes))

cell_and_pig = prolif_genes_set & pig_genes_set
print('The number of genes that are both stem cell proliferative and pigmentation genes is ', len(cell_and_pig))
print(cell_and_pig)





