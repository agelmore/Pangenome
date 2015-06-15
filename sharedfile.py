#!/usr/bin/python3.3
import sys
from collections import Counter

#read in file from sys

#for now hard code the file names
index=open('/Users/Amanda/Documents/Schloss/Fuso/Pangenome/shared/test.index','r')
sam=open('/Users/Amanda/Documents/Schloss/Fuso/Pangenome/shared/test.sam','r')
merged=open('/Users/Amanda/Documents/Schloss/Fuso/Pangenome/shared/test.merged','wt')
shared=open('/Users/Amanda/Documents/Schloss/Fuso/Pangenome/shared/test.shared','wt')


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
	print(f, c[f], end="\n", file=merged)
	

sam.close()

#switchline=[]
#for line in opf:
	#cnt = Counter()
#	line = line.strip().split('\t')
#	print(line[0], '\t', end='', file=temp)
#	contigs = line[1].strip().split(',')
#	for column in range(0,len(contigs)):
#		switchcontig = contigs[column] #contig to switch
#		if switchcontig in c.keys():
#			switchpath = c[switchcontig]
#		else:
#			switchpath = ['unknown']  #probably because don't have whole blast yet
#		print('\t'.join(switchpath), end="\t", file=temp)  
#	print("", end="\n", file=temp)        

merged.close()
shared.close()