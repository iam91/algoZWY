#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' Definition of LogisticRegressionModel '

__author__ = 'zwy'

import LogisticRegression.Sigmoid

class LogisticRegressionModel(thetaVec):
	def __init__(self, thetaVec):
		self.__thetaVec = thetaVec


	def __sigmoid(x):
		return LogisticRegression.Sigmoid.sigmoid(x)


	def __dotProduct(x, y):
		return LogisticRegression.Sigmoid.dotProduct(x, y)


	def singleClassify(data, numFeatures):
		d = [x for x in data]
		d.insert(0, 1.0)
		featureVec = d[0:numFeatures + 1]
		return 1 / (1 + __sigmoid( -featureVec, self.__thetaVec))


	def test(dataSet):
		pass