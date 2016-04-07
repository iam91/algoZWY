#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' DecisionTreeClassifier '

__author__ = 'zwy'

import Node
import Impurity
from functools import reduce

def _majorityClass(classVec, numClasses):
	cnt = [0 for x in range(numClasses)]
	for label in classVec:
		cnt[label] += 1

	maxCnt = cnt[0]
	maxLabel = 0
	for index in range(numClasses):
		if(cnt[index] > maxCnt):
			maxCnt = cnt[index]
			maxLabel = index

	return maxLabel

def _createBranch(dataSet, numClasses, numFeatures, maxDepth, impurityThreshold, currDepth):
	n = len(dataSet)
	classVec = [x[-1] for x in dataSet]
	currImpurity = Impurity.entropy(classVec, numClasses)
	if(currImpurity < impurityThreshold or currDepth >= maxDepth):
		currNode = Node.LeafNode('leaf', _majorityClass(classVec, numClasses))
		return currNode


	# continuous feature, numSubSets = 2
	flag = False
	splitFeature = 0
	splitPoint = 0.0
	minImpurity = 0.0
	bestSubSets = None
	for featureId in range(numFeatures):
		dataSet.sort(key = lambda x: x[featureId])
		numSubSets = 2
		for splitPosition in range(n):
			subSetsEntropy = []
			subSets = []
			splitRanges = [[0, splitPosition], [splitPosition, n]]
			for i in range(numSubSets):
				head = splitRanges[i][0]
				tail = splitRanges[i][1]
				subSet = dataSet[head:tail]
				subSets.append(subSet)
				subSetsClassVec = [x[-1] for x in subSet]
				subSetsEntropy.append((len(subSet) / n) * Impurity.entropy(subSetsClassVec, numClasses))
			weightedImpurity = reduce(lambda x, y: x + y, subSetsEntropy)
			if(flag):
				if(minImpurity > weightedImpurity):
					splitFeature = featureId
					splitPoint = dataSet[splitPosition][splitFeature]
					minImpurity = weightedImpurity
					bestSubSets = subSets
			else:
				splitFeature = featureId
				splitPoint = dataSet[splitPosition][splitFeature]
				minImpurity = weightedImpurity
				bestSubSets = subSets
				flag = True

	children = [_createBranch(x, numClasses, numFeatures, maxDepth, impurityThreshold, currDepth + 1) for x in bestSubSets]
	currNode = Node.SplitNode('split', (splitFeature, splitPoint), children)

	return currNode

def train(dataSet, numClasses, numFeatures, maxDepth, impurityThreshold):
	return _createBranch(dataSet, numClasses, numFeatures, maxDepth, impurityThreshold, 1)







