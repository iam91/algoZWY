#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' Driver for Classifier '

__author__ = 'zwy'

import sys
#DecisionTreeClassifier
import DecisionTreeClassifier.DecisionTreeClassifier
import DecisionTreeClassifier.DecisionTreeModel
#KNNClassifier
import KNNClassifier.KNNClassifier

args = sys.argv
if len(args) < 3:
	print('Usage: data file and classifier')
	exit()
else:
	fileDir = args[1]
	classifier = args[2]
	dataFile = open(fileDir, 'r')
	rawData = [line.strip('\n').split(',') for line in dataFile.readlines()]
	dataFile.close()
	# format the dataset into [feature1, feature2, ..., featuren, classlabel]
	# class labels take the value 0, 1, 2, ... and -1 for known class
	# ordinal features take the value 1, 2, 3, ...

	# format iris
	'''
	dataSet = []
	for line in rawData:
		classLabel = line[-1]
		data = [float(val) for val in line[0:4]]

		if(classLabel == 'Iris-setosa'):
			data.append(0)
		elif(classLabel == 'Iris-versicolor'):
			data.append(1)
		elif(classLabel == 'Iris-virginica'):
			data.append(2)

		dataSet.append(data)
	'''
	
	# format balance-scale
	
	dataSet = []
	for line in rawData:
		classLabel = line[0]
		data = [int(val) for val in line[1:5]]
		if(classLabel == 'R'):
			data.append(0)
		elif(classLabel == 'B'):
			data.append(1)
		elif(classLabel == 'L'):
			data.append(2)
		dataSet.append(data)
	
	
	if(classifier == 'DecisionTreeClassifier'):
		model = DecisionTreeClassifier.DecisionTreeClassifier.train(dataSet, 3, 4, 10, 10, 1e-17, {0: 5, 1: 5, 2: 5, 3: 5})
		print(model.test(dataSet))
	elif(classifier == 'KNNClassifier'):
		print(KNNClassifier.KNNClassifier.test(dataSet, dataSet, 10, 4, 3, {0: 5, 1: 5, 2: 5, 3: 5}))
	elif(classifier == 'LogisticRegression'):
		
	