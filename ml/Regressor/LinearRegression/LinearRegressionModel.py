#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' Definition of LinearRegressionModel '

__author__ = 'zwy'

import Math

class LinearRegressionModel(object):
	def __init__(self, thetaVec):
		self.__thetaVec = thetaVec


	def __dotProduct(self, x, y):
		return Math.dotProduct(x, y)


	def singleRegress(self, data, numFeatures):
		d = [x * 1 for x in data]
		d.insert(0, 1.0)
		featureVec = d[0:numFeatures + 1]
		return __dotProduct(featureVec, self__thetaVec)


	def test(self, dataSet, numFeatures):
		pass

	def printModel(self):
		print(self.__thetaVec)