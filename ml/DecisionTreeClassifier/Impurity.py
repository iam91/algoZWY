#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' Impurity computation '

__author__ = 'zwy'

import math
from functools import reduce


def gini(classVec, numClasses):
	pass

def entropy(classVec, numClasses):
	cnt = [0 for x in range(numClasses)]
	tot = len(classVec)
	for label in classVec:
		cnt[label] += 1
		
	entropy = []
	for x in cnt:
		if(x == 0):
			entropy.append(0.0)
		else:
			p = x / tot
			entropy.append(- p * math.log(p))

	return reduce(lambda x, y: x + y, entropy)