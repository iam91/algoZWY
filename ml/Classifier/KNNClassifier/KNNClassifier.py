#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' KNNClassifier '

__author__ = 'zwy'

'''
Work on continuous features using Euclidean distance
'''

import math
from functools import reduce

'''
Parameter format:
dataSet(list) [val1, val2, val3, ..., class]
testData(list) [val1, val2, val3, ..., class]
k(int)
numFeatures(int)
numClasses(int)
normalizeScale(int) normalize the data in [-normalizeScale, normalizeScale]
'''
def test(dataSet, testDataSet, k, numFeatures, numClasses, categoricalFeaturesInfo, normalizeScale):
	result = [singleClassify(dataSet, data, k, numFeatures, numClasses, categoricalFeaturesInfo, normalizeScale) == data[-1] for data in testDataSet]
	cnt = 0
	for re in result:
		if(not re):
			cnt += 1
	print(cnt / len(result))
	return result


'''
Parameter format:
dataSet(list) [val1, val2, val3, ..., class]
testData(list) [val1, val2, val3, ..., class] -1 for unknown class
k(int)
numFeatures(int)
numClasses(int)
normalizeScale(int) normalize the data in [-normalizeScale, normalizeScale]
'''
def singleClassify(dataSet, testData, k, numFeatures, numClasses, categoricalFeaturesInfo, normalizeScale):
	n = len(dataSet)
	if(k > n):
		print('Bad k!')
		return None
	# normalization (ordinal value ignored)
	# normalize continous value to [-1, 1] but resulting in high requirement on float accuracy
	normalizedDataSet = [[] for x in dataSet]
	normalizedTestData = [0.0 for i in range(numFeatures)]
	normalizedTestData.append(testData[-1])
	for i in range(numFeatures):
		if(i in categoricalFeaturesInfo):
			for j in range(n):
				normalizedDataSet[j].append(dataSet[j][i])
				normalizedTestData[i] = testData[i]
		else:
			featureVal = [abs(x[i]) for x in dataSet]
			maxVal = max(featureVal)
			minVal = min(featureVal)
			interval = maxVal - minVal
			if(interval != 0):
				normalized = []
				for x in featureVal:
					if(x != 0):
						sign = abs(x) / x
					else:
						sign = 1.0
				normalized.append(normalizeScale * (x - sign * minVal) / interval)
				x = testData[i]
				if(x != 0):
					sign = abs(x) / x
				else:
					sign = 1.0
				normalizedTestData[i] = normalizeScale * (x - sign * minVal) / interval
			else:
				normalized = []
				for x in featureVal:
					if(x != 0):
						val = abs(x) / x
					else:
						val = 0.0
				normalized.append(normalizeScale * val)
				x = testData[i]
				if(x != 0):
					val = abs(x) / x
				else:
					val = 0.0
				normalizedTestData[i] = normalizeScale * val

			for j in range(n):
				normalizedDataSet[j].append(normalized[j])


	for i in range(n):
		normalizedDataSet[i].append(dataSet[i][-1])

	#classify
	distances = [[_distance(x, normalizedTestData, numFeatures, categoricalFeaturesInfo), x[-1]] for x in normalizedDataSet]
	
	distances.sort(key = lambda x: x[0])

	kneighborsClass = [x[-1] for x in distances[0: k]]
	return _majorityClass(kneighborsClass, numClasses)


'''
Euclidean distance
'''
def _distance(a, b, numFeatures, categoricalFeaturesInfo):
	diff = []
	for i in range(numFeatures):
		if(i in categoricalFeaturesInfo):
			inter = categoricalFeaturesInfo[i] - 1
			diff.append((a[i] - b[i]) / inter)
		else:
			diff.append(a[i] - b[i])
	squaredDiff = [x * x for x in diff]
	dist = math.sqrt(reduce(lambda x, y: x + y, squaredDiff))
	return dist


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