#!/usr/bin/python2.7

'''
Script to make cluster.list file into a shared-like file that can be read by mothur 
rarefaction.single command
'''

from __future__ import print_function
import sys
import argparse
from collections import Counter
from collections import defaultdict


#read in file from sys
list_file=sys.argv[1]
shared_file=sys.argv[2]

list=open(list_file,'r')
shared=open(shared_file,'wt')