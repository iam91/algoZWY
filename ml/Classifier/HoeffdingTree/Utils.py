#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' Utility for hoeffding tree '

__author__ = 'zwy'

import math
from scipy.stats import norm

'''
classVec(list) a list of number of different class labels
numClasses(int) the number of different classes
'''
def entropy(classCntVec):
	cnt = [1 * x for x in classCntVec]
	tot = sum(cnt)
	entropy = []
	for x in cnt:
		if(x == 0):
			entropy.append(0.0)
		else:
			p = x / tot
			entropy.append(- p * math.log(p))
	return sum(entropy)


class Statistics(object):
	def __init__(self, statisticsType):
		self.__statisticsType = statisticsType


	def getStatisticsType(self):
		return self.__statisticsType


class NominalFeatureStatistics(Statistics):
	def __init__(self, numOfValues, numOfClasses):
		Statistics.__init__(self, 'nominal')
		self.__numOfValues = numOfValues
		# self.__statistics[featureVal][classLabel]
		self.__statistics = [[0 for x in range(numOfClasses)] for y in range(numOfValues)]
		self.__classCnt = [0 for x in range(numOfClasses)]
		self.__totCnt = 0


	def update(self, value, classLabel):
		self.__statistics[value][classLabel] += 1
		self.__classCnt[classLabel] += 1
		self.__totCnt += 1


	def getStatistics(self):
		return self.__statistics


	def getTotalCnt(self):
		return self.__totCnt


class ContinuousFeatureStatistics(Statistics):
	VALSUM = 0
	VALSQSUM = 1
	MAXVAL = 2
	MINVAL = 3
	CNT = 4
	def __init__(self, numOfClasses):
		Statistics.__init__(self, 'continuous')
		self.__numOfClasses = numOfClasses
		self.__baseStatistics = [[0.0, 0.0, 0.0, 0.0, 0] for x in range(self.__numOfClasses)]
		self.__numOfBins = 10


	def update(self, value, classLabel):
		if(self.__baseStatistics[classLabel][self.CNT] == 0):
			self.__baseStatistics[classLabel][self.MAXVAL] = value
			self.__baseStatistics[classLabel][self.MINVAL] = value
		else:
			if(self.__baseStatistics[classLabel][self.MAXVAL] < value):
				self.__baseStatistics[classLabel][self.MAXVAL] = value
			if(self.__baseStatistics[classLabel][self.MINVAL] > value):
				self.__baseStatistics[classLabel][self.MINVAL] = value

		self.__baseStatistics[classLabel][self.CNT] += 1
		self.__baseStatistics[classLabel][self.VALSUM] += value
		self.__baseStatistics[classLabel][self.VALSQSUM] += value * value


	def getStatistics(self):
		minValue = self.__baseStatistics[0][self.MINVAL]
		maxValue = self.__baseStatistics[0][self.MAXVAL]
		for i in range(self.__numOfClasses):
			if(self.__baseStatistics[i][self.MINVAL] < minValue):
				minValue = self.__baseStatistics[i][self.MINVAL]
			if(self.__baseStatistics[i][self.MAXVAL] > maxValue):
				maxValue = self.__baseStatistics[i][self.MAXVAL]
		binWidth = (maxValue - minValue) / self.__numOfBins
		
		splitPointCandidates = []
		for i in range(self.__numOfBins + 1):
			splitPointCandidates.append(minValue + i * binWidth)
		
		retStatistics = []
		

		meanList = []
		varianceList = []
		for i in range(self.__numOfClasses):
			mean = self.__baseStatistics[i][self.VALSUM] / self.__baseStatistics[i][self.CNT]
			variance = (self.__baseStatistics[i][self.VALSQSUM] 
				- mean * self.__baseStatistics[i][self.VALSUM]) / (self.__baseStatistics[i][self.CNT] - 1)
			meanList.append(mean)
			varianceList.append(variance)


		statisticsForEachSplitPoint = []
		for splitPoint in splitPointCandidates:
			statisticsForEachClass = []
			for i in range(self.__numOfClasses):
				stddev = math.sqrt(varianceList[i])
				normalizedSplitPoint = (splitPoint - meanList[i]) / stddev
				
				lessAndEqual = norm.cdf(normalizedSplitPoint)
				larger = 1 - lessAndEqual

				lCnt = int(lessAndEqual * self.__baseStatistics[i][self.CNT])
				rCnt = int(larger * self.__baseStatistics[i][self.CNT])
				statisticsForEachClass.append((lCnt, rCnt))
			statisticsForEachSplitPoint.append((splitPoint, statisticsForEachClass))

		return statisticsForEachSplitPoint
