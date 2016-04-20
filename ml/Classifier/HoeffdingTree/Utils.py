#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' Utility for hoeffding tree '

__author__ = 'zwy'

import math

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


class Statistics(object):
	def __init__(self, statisticsType):
		self.__statisticsType = statisticsType


	def getStatisticsType(self):
		return self.__statisticsType

	@abstractmethod
	def update(self, value, classLabel):
		pass



class NominalFeatureStatistics(Statistics):
	def __init__(self, numOfValues, numOfClasses):
		Statistics.__init__(self, 'nominal')
		self.__numOfValues = numOfValues
		self.__statistics = [[0 for x in range(numOfClasses)] for y in range(numOfValues)]
		self.__classCnt = [0 for x in range(numOfClasses)]
		self.__totCnt = 0


	def update(self, value, classLabel):
		self.__statistics[value][classLabel] += 1
		self.__classCnt[classLabel] += 1
		self.__totCnt += 1


class ContinuousFeatureStatistics(Statistics):
	__VALSUM = 0
	__VALSQSUM = 1
	__MAXVAL = 2
	__MINVAL = 3
	__CNT = 4
	def __init__(self, numOfClasses):
		Statistics.__init__(self, 'continuous')
		self.__numOfClasses = numOfClasses
		self.__statistics = [(0.0, 0.0, 0.0, 0.0, 0) for x in range(self._numOfClasses)]


	def update(self, value, classLabel):
		if(self.statisitcs[classLabel][self.__CNT] == 0):
			self.__statistics[classLabel][self.__MAXVAL] = value
			self.__statistics[classLabel][self.__MinVAL] = value
		else:
			if(self.__statistics[classLabel][self.__MAXVAL] < value):
				self.__statistics[classLabel][self.__MAXVAL] = value
			if(self.__statistics[classLabel][self.__MinVAL] > value):
				self.__statistics[classLabel][self.__MinVAL] = value

		self.__statistics[classLabel][self.__CNT] += 1
		self.__statistics[classLabel][self.__VALSUM] += value
		self.__statistics[classLabel][self.__VALSQSUM] += value * value

		
