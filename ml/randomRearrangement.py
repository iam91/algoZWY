#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' Randomly rearrange the data '

__author__ = 'zwy'

import sys
import random

args = sys.argv
if(len(args) < 3):
	print("usage: input file and output file")
	exit()

inFile = args[1]
outFile = args[2]

fin = open(inFile, "r")
fout = open(outFile, "w+")

ll = []
lines = fin.readlines()

lines[-1] += '\n'

n = len(lines)


for i in range(n):
	r1 = int(random.uniform(0, n - 1))
	r2 = int(random.uniform(0, n - 1))
	temp = lines[r1]
	lines[r1] = lines[r2]
	lines[r2] = temp

fout.writelines(lines)

fin.close()
fout.close()