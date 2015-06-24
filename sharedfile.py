#!/usr/bin/python3.3
import sys
from collections import Counter

#read in file from sys

#for now hard code the file names
index=open('/Users/Amanda/Documents/Schloss/Fuso/Pangenome/shared/Pangenome/test.index','r')
sam=open('/Users/Amanda/Documents/Schloss/Fuso/Pangenome/shared/Pangenome/test.sam','r')
merged_temp=open('/Users/Amanda/Documents/Schloss/Fuso/Pangenome/shared/Pangenome/test.merged','wt')


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

cluster_seq=open('/Users/Amanda/Documents/Schloss/Fuso/Pangenome/shared/Pangenome/test.merged','r')
shared=open('/Users/Amanda/Documents/Schloss/Fuso/Pangenome/shared/Pangenome/test.shared','wt')


switchline=[]
for line in cluster_seq:
	#cnt = Counter()
	line = line.strip().split('\t')
	print(line[0], '\t', end='', file=shared)
	seqs = line[1].strip().split(',')
	for column in range(0,len(seqs)):
		switchseq = seqs[column] #contig to switch
		if switchseq in d.keys():
			switchpath = d[switchseq]
		#else:
		#	switchpath = ['unknown']  #probably because don't have whole blast yet
		print('\t'.join(switchpath), end="\t", file=shared)  
	print("", end="\n", file=shared)        

cluster_seq.close()
shared.close()