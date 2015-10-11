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



index=open(index_file,'r')
sam=open(sam_file,'r')

#make dictionary of sequence as key and read as value from sam file

d = defaultdict(int) # dictionary key is sequence and value is read count

for row in sam:
	row=row.strip().split('\t')
	sequence = row[1]
	length=row[2]
	d[sequence]+=(1/length)
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




