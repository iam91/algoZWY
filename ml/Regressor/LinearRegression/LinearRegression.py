#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' Linear Regression '

__author__ = 'zwy'

import Math

def _dotProduct(x, y):
	return Math.dotProduct(x, y)


def _gradThetaBatch(traningDataSet, numFeatures, featureId, thetaVec, alpha)


'''
Parameter format:
dataSet(list) [val1, val2, val3, ..., class]
numFeatures(int)
initTheta(list) [theta0, theta1, ..., thetan]
maxIter(int)
alpha(float)
iterMethod(str) 'btch' for batch gradient ascent, 'stoc' for stochastic gradient ascent
'''
def train(dataSet, numFeatures, initTheta, maxIter, alpha, iterMethod):
	n = len(dataSet)
	trainingDataSet = [x * 1 for x in dataSet]
	for trainingData in trainingDataSet:
		trainingData.insert(0, 1.0)

	theta = [x * 1 for x in initTheta]
	