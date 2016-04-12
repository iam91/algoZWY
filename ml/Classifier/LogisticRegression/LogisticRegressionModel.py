#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' Definition of LogisticRegressionModel '

__author__ = 'zwy'

import LogisticRegression.Sigmoid

class LogisticRegressionModel(object):
	def __init__(self, thetaVec):
		self.__thetaVec = thetaVec


	def __sigmoid(self, x):
		return LogisticRegression.Sigmoid.sigmoid(x)


	def __dotProduct(self, x, y):
		return LogisticRegression.Sigmoid.dotProduct(x, y)


	def singleClassify(self, data, numFeatures):
		d = [x * 1 for x in data]
		d.insert(0, 1.0)
		featureVec = d[0:numFeatures + 1]
		p =  1 / (1 + self.__sigmoid( - self.__dotProduct(featureVec, self.__thetaVec)))
		if(p > 0.5):
			return 1.0
		else:
			return 0.0


	def test(self, dataSet, numFeatures):
		result = [self.singleClassify(data, numFeatures) == data[-1] for data in dataSet]
		cnt = 0
		for re in result:
			if(not re):
				cnt += 1
		print(cnt / len(result))
		return result