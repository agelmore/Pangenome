#!/usr/bin/python2.7
from __future__ import print_function
import sys
import argparse
from collections import Counter

'''
#Script to count number of reads per pangenome cluster. Reads are mapped 
to sequences using BWA. Sequences are clustered using get_homologues. Final outfile is called summary_file and includes the total number of reads in each cluster from that sample.

'''
'''
parser = argparse.ArgumentParser(description='Count number of reads per pangenome cluster.')
parser.add_argument('sam_file', nargs='+', help='index file with reads in first column and reference sequences they map to in the second')
parser.add_argument('index_file', nargs='+', help='index file with sequences in first column and clusters in the second')
parser.add_argument('outfile', nargs='+', help='file with read counts per cluster')

args = parser.parse_args()
'''

#read in file from sys
index_file=sys.argv[1]
sam_file=sys.argv[2]
merged_temp_file='./temp.merged'
cluster_seq_file='./temp.merged'
shared_file='./temp.shared'
cluster_file='./temp.shared'
summary_file=sys.argv[3]


#temp.merged has the cluster with a list of sequences in that cluster. temp.shared has the #cluster with the reads that mapped to those sequences switched in. 


'''
#for now hard code the file names
index_file='/mnt/EXT/Schloss-data/amanda/Fuso/pangenome/bwa/t0/t0.index'
sam_file='/mnt/EXT/Schloss-data/amanda/Fuso/pangenome/bwa/t0/all.t0.SRS013502.mapped.index'
merged_temp_file='/mnt/EXT/Schloss-data/amanda/Fuso/pangenome/bwa/t0/temp/test.merged'
cluster_seq_file='/mnt/EXT/Schloss-data/amanda/Fuso/pangenome/bwa/t0/temp/test.merged'
shared_file='/mnt/EXT/Schloss-data/amanda/Fuso/pangenome/bwa/t0/temp/test.shared'
cluster_file='/mnt/EXT/Schloss-data/amanda/Fuso/pangenome/bwa/t0/temp/test.shared'
summary_file='/mnt/EXT/Schloss-data/amanda/Fuso/pangenome/bwa/t0/all.t0.SRS013502.mapped.out'
'''

index=open(index_file,'r')
sam=open(sam_file,'r')

merged_temp=open(merged_temp_file,'wt')


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

for f in c.keys():
	print(f, ','.join(c[f]), sep="\t", end="\n", file=merged_temp)

merged_temp.close()

#make dictionary of sequence as key and read as value from sam file

d = {} # dictionary key is sequence and read is value

for row in sam:
	row=row.strip().split('\t')
	sequence = row[1]
	read= row[0]
	if sequence in d.keys():
		d[sequence].append(read)
	else:
		d[sequence] = [read]
sam.close()


cluster_seq=open(cluster_seq_file,'r')
shared=open(shared_file,'wt')


switchline=[]
for line in cluster_seq:
	line = line.strip().split('\t')
	print(line[0], '\t', end='', file=shared)
	seqs = line[1].strip().split(',')
	for column in range(0,len(seqs)):
		switchseq = seqs[column] #contig to switch
		if switchseq in d.keys():
			switchline = d[switchseq]
		print('\t'.join(switchline), end="\t", file=shared)  
	print("", end="\n", file=shared)        

cluster_seq.close()
shared.close()

#Count the reads per cluster to make summary file

cluster_read=open(cluster_file,'r')

summary=open(summary_file,'wt')


for line in cluster_read:
	line = line.strip().split('\t')
	count = len(line) - 1
	print(line[0], count, end='\n', file=summary)
	
summary_file.close()
cluster_read.close()




