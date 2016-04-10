#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' DecisionTreeClassifier '

__author__ = 'zwy'

'''
Continuous features produce binary splits.
Ordinal features with M possible values produce N-way splits with N = 2^(M - 1) - 1 > maxBin ? 2: 2^(M - 1) - 1
Nominal features not implemented yet.
'''

import math
import DecisionTreeClassifier.Node
import DecisionTreeClassifier.Impurity
import DecisionTreeClassifier.DecisionTreeModel
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


def _equal(x, y):
	if(isinstance(x, int) and isinstance(y, int)):
		return x == y
	elif(isinstance(x, float) or isinstance(y, float)):
		return abs(x - y) < 1e-17


def _createBranch(dataSet, numClasses, numFeatures, maxDepth, maxBin, impurityThreshold, currDepth, categoricalFeaturesInfo):
	n = len(dataSet)
	classVec = [x[-1] for x in dataSet]
	currImpurity = DecisionTreeClassifier.Impurity.entropy(classVec, numClasses)
	if(currImpurity < impurityThreshold or currDepth >= maxDepth):
		currNode = DecisionTreeClassifier.Node.LeafNode('leaf', _majorityClass(classVec, numClasses), currDepth)
		return currNode

	splitFeature = 0
	splitPoint = None
	minImpurity = math.log(numClasses)
	bestSubSets = None
	for featureId in range(numFeatures):
		dataSet.sort(key = lambda x: x[featureId])

		if(featureId in categoricalFeaturesInfo):
			numSubSets = categoricalFeaturesInfo[featureId]
		else:
			numSubSets = 2
		
		splitRangesList = []
		if(numSubSets == 2):
			preValue = dataSet[0][featureId]
			triedFlag = False
			for splitPosition in range(n):
				if(_equal(dataSet[splitPosition][featureId], preValue) and triedFlag):
					continue
				triedFlag = True
				splitRangesList.append([[0, splitPosition], [splitPosition, n]])
		elif(numSubSets > 2):
			splitRanges = []
			preValue = dataSet[0][featureId]
			preSplitPoint = 0
			for i in range(n):
				if(_equal(dataSet[i][featureId], preValue)):
					continue
				else:
					splitRanges.append([preSplitPoint, i])
					preSplitPoint = i
			splitRanges.append([preSplitPoint, n])
			splitRangesList.append(splitRanges)

		for splitRanges in splitRangesList:
			subSetsEntropy = []
			subSets = []
			splitPositions = []

			totRanges = len(splitRanges)
			cnt = 0
			for splitRange in splitRanges:
				cnt += 1
				subSet = dataSet[splitRange[0]: splitRange[1]]
				if(cnt < totRanges):
					splitPositions.append(splitRange[1])
				subSets.append(subSet)
				subSetsClassVec = [x[-1] for x in subSet]
				subSetsEntropy.append((len(subSet) / n) * DecisionTreeClassifier.Impurity.entropy(subSetsClassVec, numClasses))
			weightedImpurity = reduce(lambda x, y: x + y, subSetsEntropy)
			if(minImpurity > weightedImpurity):
				splitFeature = featureId
				splitPoints = []
				for position in splitPositions:
					splitPoints.append(dataSet[position][splitFeature])
				splitPoint = splitPoints
				minImpurity = weightedImpurity
				bestSubSets = subSets

	children = [_createBranch(x, numClasses, numFeatures, maxDepth, maxBin, impurityThreshold, currDepth + 1, categoricalFeaturesInfo) for x in bestSubSets]
	currNode = DecisionTreeClassifier.Node.SplitNode('split', (splitFeature, splitPoint), children, currDepth)
	
	return currNode


'''
Parameter format:
dataSet(list) [val1, val2, val3, ..., class]
numClasses(int)
numFeatures(int)
maxDepth(int)
maxBin(int)
impurityThreshold(float)
categoricalFeaturesInfo(dict) {index1: M1, index2: M2, ...}
'''
def train(dataSet, numClasses, numFeatures, maxDepth, maxBin, impurityThreshold, categoricalFeaturesInfo):
	for k in categoricalFeaturesInfo.keys():
		possibleNumOfSplits = int(math.pow(2, categoricalFeaturesInfo[k] - 1) - 1)
		if(maxBin >= possibleNumOfSplits):
			numOfSplits = possibleNumOfSplits
		else:
			numOfSplits = 2
		categoricalFeaturesInfo[k] = numOfSplits

	model = DecisionTreeClassifier.DecisionTreeModel.DecisionTreeModel(_createBranch(dataSet, numClasses, numFeatures, maxDepth, maxBin, impurityThreshold, 1, categoricalFeaturesInfo))
	return model
	