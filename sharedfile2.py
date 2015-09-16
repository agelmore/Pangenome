#!/usr/bin/python2.7

'''
Script to count number of reads per pangenome cluster. Reads are mapped 
to sequences using BWA. Sequences are clustered using get_homologues. Final outfile is called summary_file and includes the total number of reads in each cluster from that sample.

'''

from __future__ import print_function
import sys
import argparse
from collections import Counter
from collections import defaultdict


#read in file from sys
index_file=sys.argv[1]
sam_file=sys.argv[2]
summary_file=sys.argv[3]


#temp.merged has the cluster with a list of sequences in that cluster. temp.shared has the #cluster with the reads that mapped to those sequences switched in. 



index=open(index_file,'r')
sam=open(sam_file,'r')

#make dictionary of sequence as key and read as value from sam file

d = defaultdict(int) # dictionary key is sequence and value is read count

for row in sam:
	row=row.strip().split('\t')
	sequence = row[1]
	d[sequence]+=1
sam.close()

#make dictionary of cluster as key and sequence as value from index file

c = {} # dictionary key is cluster and sequence is value

for row in index:
	row=row.strip().split('\t')
	cluster = row[1]
	seq= row[0]
	if cluster in c.keys():
		c[cluster].append(seq)
	else:
		c[cluster] = [seq]
index.close()

summary=open(summary_file,'wt')

print("clustername","readcount","genecount", end='\n', file=summary) #print the header


for cluster in c.keys():
	genecount=len(c[cluster])
	i=0
	for sequence in c[cluster]:
		i += d[sequence]
	print(cluster, i, genecount, sep='\t', file=summary)






'''


#Generate file with unique reads mapping to each cluster. Insert reads that mapped to genes in place of gene name in the merged temp file. 


for line in cluster_seq:
	line = line.strip().split('\t')
	print(line[0], '\t', end='', file=shared)
	seqs = line[1].strip().split(',')
	for column in range(0,len(seqs)):
		switchline=[]						#will be a list of reads in gene. Has to be reset each loop
		switchseq = seqs[column] 			#gene to switch with reads mapping to gene
		if switchseq in d.keys(): 			#gene must have reads that map to it, else switchline will not have a value and will print no reads for that gene
			switchline = d[switchseq]
			
		print('\t'.join(switchline), end="\t", file=shared)
	print(line[2], end="\n", file=shared)  #print the number of genes at the end of the line (this was already the 3rd column in the file)

cluster_seq.close()
shared.close()

#Count the reads per cluster to make summary file

cluster_read=open(cluster_file,'r')


print("clustername","readcount","genecount", end='\n', file=summary) #print the header
for line in cluster_read:
	line = line.strip().split('\t')
	while '' in line:
		line.remove('') #remove empty items from list. This happens when there are no reads that map to a gene
	length=len(line)
	count = length - 2  #count the number of reads. minus 2 because cluster name and gene count at the end
	genecount=line[-1]
	print(line[0], count, genecount, sep='\t', end='\n', file=summary)
	
#summary_file.close()
#cluster_read.close()
'''