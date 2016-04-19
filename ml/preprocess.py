#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' Data preprocessing: discrete features map'

__author__ = 'zwy'

import sys
args = sys.argv
if(len(args) < 3):
	print("usage: input file and output file")
	exit()

inFile = args[1]
outFile = args[2]

fin = open(inFile, "r")
fout = open(outFile, "w+")

def featureMap(valSet, currVal):
	return str(valSet.index(currVal))

# set value sets for each feature
oVal0 = "usual, pretentious, great_pret".split(", ")
oVal1 = "proper, less_proper, improper, critical, very_crit".split(", ")
oVal2 = "complete, completed, incomplete, foster".split(", ")
oVal3 = "1, 2, 3, more".split(", ")
oVal4 = "convenient, less_conv, critical".split(", ")
oVal5 = "convenient, inconv".split(", ")
oVal6 = "nonprob, slightly_prob, problematic".split(", ")
oVal7 = "recommended, priority, not_recom".split(", ")
oVal8 = "not_recom, recommend, very_recom, priority, spec_prior".split(", ")

# combination of all value sets
valSet = {
	0: oVal0,
	1: oVal1,
	2: oVal2,
	3: oVal3,
	4: oVal4,
	5: oVal5,
	6: oVal6,
	7: oVal7,
	8: oVal8
}

# start mapping
ll = []
cnt = 0
for line in fin.readlines():
	vals = line.strip('\n').split(",")
	vals[0] = featureMap(valSet[0], vals[0])
	vals[1] = featureMap(valSet[1], vals[1])
	vals[2] = featureMap(valSet[2], vals[2])
	vals[3] = featureMap(valSet[3], vals[3])
	vals[4] = featureMap(valSet[4], vals[4])
	vals[5] = featureMap(valSet[5], vals[5])
	vals[6] = featureMap(valSet[6], vals[6])
	vals[7] = featureMap(valSet[7], vals[7])
	vals[8] = featureMap(valSet[8], vals[8])
	l = ""
	cnt = 0
	nn = len(vals)
	for i in vals:
		l += i
		cnt += 1
		if(cnt < nn):
			l += ','
		else:
			l += '\n'
	ll.append(l)
fout.writelines(ll)

fin.close()
fout.close()