#!/usr/bin/python3.3
import sys
from collections import Counter


'''
#Script to count number of reads per pangenome cluster. Reads are mapped 
to sequences using BWA. Sequences are clustered using get_homologues. Final outfile is called summary_file and includes the total number of reads in each cluster from that sample.

'''

#read in file from sys

#for now hard code the file names, add sys_args later
index_file='/Users/Amanda/Documents/Schloss/Fuso/Pangenome/shared/Pangenome/test.index'
sam_file='/Users/Amanda/Documents/Schloss/Fuso/Pangenome/shared/Pangenome/test.sam'
merged_temp_file='/Users/Amanda/Documents/Schloss/Fuso/Pangenome/shared/Pangenome/test.merged'
cluster_seq_file='/Users/Amanda/Documents/Schloss/Fuso/Pangenome/shared/Pangenome/test.merged'
shared_file='/Users/Amanda/Documents/Schloss/Fuso/Pangenome/shared/Pangenome/test.shared'
cluster_file='/Users/Amanda/Documents/Schloss/Fuso/Pangenome/shared/Pangenome/test.shared'
summary_file='/Users/Amanda/Documents/Schloss/Fuso/Pangenome/shared/Pangenome/test.summary'


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

'''
for f in d.keys():
	print(f, ','.join(d[f]), sep="\t", end="\n", file=shared)
sam.close()
'''

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
			switchpath = d[switchseq]
		print('\t'.join(switchpath), end="\t", file=shared)  
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
	
summary.close()
cluster_read.close()




