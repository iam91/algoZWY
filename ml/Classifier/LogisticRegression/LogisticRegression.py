#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' Logistic regression '

__author__ = 'zwy'

'''
Work on continuous features, applied to binary classification
'''

import LogisticRegression.LogisticRegressionModel
import LogisticRegression.Sigmoid
import math
import random

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
	for i in range(maxIter):
		tempTheta = [x * 1 for x in theta]

		#print the cost function
		#print(_costFunc(trainingDataSet, theta, numFeatures))

		if(iterMethod == "btch"):
			for j in range(numFeatures + 1):
				theta[j] += _gradThetaBatch(trainingDataSet, numFeatures, j, tempTheta, alpha)
		elif(iterMethod == "stoc"):
			'''
			for j in range(numFeatures + 1):
				t = random.randint(0, n - 1)
				print(t)
				trainingData = trainingDataSet[t]
				theta[j] += _gradThetaStoc(trainingData, numFeatures, j, tempTheta, alpha)
			'''
			for traningData in trainingDataSet:
				for j in range(numFeatures + 1):
					theta[j] += _gradThetaStoc(trainingData, numFeatures, j, tempTheta, alpha)

	model = LogisticRegression.LogisticRegressionModel.LogisticRegressionModel(theta)
	return model


def _gradThetaBatch(trainingDataSet, numFeatures, featureId, thetaVec, alpha):
	n = len(trainingDataSet)
	ret = 0.0
	for i in range(n):
		featureVec = trainingDataSet[i][0:numFeatures + 1]
		label = trainingDataSet[i][-1]
		ret += featureVec[featureId] * (label - _sigmoid(_dotProduct(featureVec, thetaVec)))

	return alpha * ret

def _gradThetaStoc(trainingData, numFeatures, featureId, thetaVec, alpha):
	ret = 0.0
	featureVec = trainingData[0:numFeatures + 1]
	label = trainingData[-1]
	ret = featureVec[featureId] * (label - _sigmoid(_dotProduct(featureVec, thetaVec)))
	return alpha * ret

def _sigmoid(x):
	return LogisticRegression.Sigmoid.sigmoid(x)


def _dotProduct(x, y):
	return LogisticRegression.Sigmoid.dotProduct(x, y)

def _costFunc(trainingDataSet, thetaVec, numFeatures):
	L = 0.0
	for data in trainingDataSet:
		featureVec = data[0:numFeatures + 1]
		multi = _dotProduct(featureVec, thetaVec)
		y = data[-1]
		L += y * multi - math.log(1 + math.exp(multi))

	return L


'''
 big number
 learning rate
'''
