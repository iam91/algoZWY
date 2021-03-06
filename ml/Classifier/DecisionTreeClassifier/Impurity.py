#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' Impurity computation '

__author__ = 'zwy'

import math


def gini(classVec, numClasses):
	pass


'''
classVec(list) a list of class labels of the dataset
numClasses(int) the number of different classes
'''
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

	return sum(entropy)
	