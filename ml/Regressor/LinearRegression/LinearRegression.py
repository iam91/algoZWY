#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' Linear Regression '

__author__ = 'zwy'

import Math
import LinearRegression.LinearRegressionModel

'''
Parameter format:
dataSet(list) [val1, val2, val3, ..., class]
numFeatures(int)
initTheta(list) [theta0, theta1, ..., thetan]
maxIter(int)
alpha(float)
iterMethod(str) 'btch' for batch gradient ascent, 'stoc' for stochastic gradient ascent
normalizeScale(int) normalize the data in [-normalizeScale, normalizeScale]
'''
def train(dataSet, numFeatures, initTheta, maxIter, alpha, normalizeScale):
	n = len(dataSet)
	trainingDataSet = [x * 1 for x in dataSet]

	#normalize
	normalizedDataSet = [[] for x in trainingDataSet]
	for k in range(numFeatures):
		featureVal = [abs(x[k]) for x in trainingDataSet]
		maxVal = max(featureVal)
		minVal = min(featureVal)
		interval = maxVal - minVal
		if(interval != 0.0):
			normalized = []
			for x in featureVal:
				if(x != 0):
					sign = abs(x) / x
				else:
					sign = 1.0
				normalized.append(normalizeScale * (x - sign * minVal) / interval)
		else:
			normalized = []
			for x in featureVal:
				if(x != 0):
					val = abs(x) / x
				else:
					val = 0.0
				normalized.append(normalizeScale * val)

		for j in range(n):
			normalizedDataSet[j].append(normalized[j])
	trainingDataSet = [x for x in normalizedDataSet]

	for trainingData in trainingDataSet:
		trainingData.insert(0, 1.0)

	theta = [x * 1 for x in initTheta]
	for i in range(maxIter):
		tempTheta = [x * 1 for x in theta]

		#print the cost function
		print(_costFunc(trainingDataSet, theta, numFeatures))

		for j in range(numFeatures + 1):
			theta[j] -= _gradThetaBatch(trainingDataSet, numFeatures, j, tempTheta, alpha)

	model = LinearRegression.LinearRegressionModel.LinearRegressionModel(theta)
	return model
	

def _dotProduct(x, y):
	return Math.dotProduct(x, y)


def _gradThetaBatch(trainingDataSet, numFeatures, featureId, thetaVec, alpha):
	m = len(trainingDataSet)
	ret = 0.0
	for i in range(m):
		featureVec = trainingDataSet[i][0:numFeatures + 1]
		label = trainingDataSet[i][-1]
		ret += (_dotProduct(featureVec, thetaVec) - label) * featureVec[featureId]

	return alpha * ret / m


def _costFunc(trainingDataSet, thetaVec, numFeatures):
	L = 0.0
	m = len(trainingDataSet)
	for data in trainingDataSet:
		featureVec = data[0:numFeatures + 1]
		pred = _dotProduct(featureVec, thetaVec)
		y = data[-1]
		error = pred - y
		L += error * error
	return L / m