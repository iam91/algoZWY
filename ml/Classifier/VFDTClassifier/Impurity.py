#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' Impurity computation '

__author__ = 'zwy'

import math

def gini(classVec, numClasses):
	pass


'''
classVec(list) a list of number of different class labels
numClasses(int) the number of different classes
'''
def entropy(classVec, numClasses):
	cnt = [1 * x for x in classVec]
	tot = sum(cnt)
		
	entropy = []
	for x in cnt:
		if(x == 0):
			entropy.append(0.0)
		else:
			p = x / tot
			entropy.append(- p * math.log(p))

	return sum(entropy)
	