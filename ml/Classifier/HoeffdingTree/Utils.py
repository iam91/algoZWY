#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' Utility for hoeffding tree '

__author__ = 'zwy'

import math

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

	@abstractmethod
	def update(self, value, classLabel):
		pass


	@abstractmethod
	def getStatistics(self):
		pass



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
	__VALSUM = 0
	__VALSQSUM = 1
	__MAXVAL = 2
	__MINVAL = 3
	__CNT = 4
	def __init__(self, numOfClasses):
		Statistics.__init__(self, 'continuous')
		self.__numOfClasses = numOfClasses
		self.__baseStatistics = [(0.0, 0.0, 0.0, 0.0, 0) for x in range(self._numOfClasses)]


	def update(self, value, classLabel):
		if(self.__baseStatistics[classLabel][self.__CNT] == 0):
			self.__baseStatistics[classLabel][self.__MAXVAL] = value
			self.__baseStatistics[classLabel][self.__MinVAL] = value
		else:
			if(self.__baseStatistics[classLabel][self.__MAXVAL] < value):
				self.__baseStatistics[classLabel][self.__MAXVAL] = value
			if(self.__baseStatistics[classLabel][self.__MinVAL] > value):
				self.__baseStatistics[classLabel][self.__MinVAL] = value

		self.__baseStatistics[classLabel][self.__CNT] += 1
		self.__baseStatistics[classLabel][self.__VALSUM] += value
		self.__baseStatistics[classLabel][self.__VALSQSUM] += value * value


	def getStatistics(self):
		return self.__statistics

		
