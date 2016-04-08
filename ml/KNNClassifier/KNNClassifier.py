#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' KNNClassifier '

__author__ = 'zwy'

'''
Work on continuous features using Euclidean distance
'''

import functools

'''
Parameter format:
dataSet(list) [val1, val2, val3, ..., class]
testData(list) [val1, val2, val3, ..., class]
'''
def classify(dataSet, testDataSet):
	for testData in testDataSet:
		pass

def _singleClassify(dataSet, testData, numFeatures):
	n = len(dataSet)
	# normalization
	for i in range(numFeatures):
		dataSet.sort(key = lambda x:x[i])
		maxValue = dataSet[-1][i]
		dataSet = list(map(lambda x: x[-1], dataSet))

	print(dataSet)

