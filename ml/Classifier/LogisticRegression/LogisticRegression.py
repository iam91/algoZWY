#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' Logistic regression '

__author__ = 'zwy'

'''
Work on continuous features, applied to binary classification
'''

import LogisticRegression.LogisticRegressionModel
import LogisticRegression.Sigmoid

'''
Parameter format:
dataSet(list) [val1, val2, val3, ..., class]
numFeatures(int)
initTheta(list) [theta0, theta1, ..., thetan]
maxIter(int)
alpha(float)
'''
def train(dataSet, numFeatures, initTheta, maxIter, alpha):
	n = len(dataSet)
	trainingDataSet = [x * 1 for x in dataSet]
	for trainingData in trainingDataSet:
		trainingData.insert(0, 1.0)

	theta = [x * 1 for x in initTheta]
	for i in range(maxIter):
		tempTheta = [x * 1 for x in theta]
		for j in range(numFeatures + 1):
			theta[j] += _gradTheta(trainingDataSet, numFeatures, j, tempTheta, alpha)

	model = LogisticRegression.LogisticRegressionModel.LogisticRegressionModel(theta)
	return model


def _gradTheta(trainingDataSet, numFeatures, featureId, thetaVec, alpha):
	n = len(trainingDataSet)
	ret = 0.0
	for i in range(n):
		featureVec = trainingDataSet[i][0:numFeatures + 1]
		label = trainingDataSet[i][-1]
		ret += featureVec[featureId] * (label - _sigmoid(_dotProduct(featureVec, thetaVec)))
	return alpha * ret


def _sigmoid(x):
	return LogisticRegression.Sigmoid.sigmoid(x)


def _dotProduct(x, y):
	return LogisticRegression.Sigmoid.dotProduct(x, y)

'''
 big number
 learning rate
'''
