#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' Driver for DecisionTreeClassifier '

__author__ = 'zwy'

import sys
import DecisionTreeClassifier
import DecisionTreeModel

args = sys.argv
if len(args) < 2:
	print('Usage: data file.')
	exit()
else:
	fileDir = args[1]
	dataFile = open(fileDir, 'r')
	rawData = [line.strip('\n').split(',') for line in dataFile.readlines()]
	
	# format the dataset into [feature1, feature2, ..., featuren, class]

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
		data = [float(val) for val in line[1:5]]
		if(classLabel == 'R'):
			data.append(0)
		elif(classLabel == 'B'):
			data.append(1)
		elif(classLabel == 'L'):
			data.append(2)
		dataSet.append(data)
	
	model = DecisionTreeClassifier.train(dataSet, 3, 4, 10, 10, 1e-12, {0: 5, 1: 5, 2: 5, 3: 5})
	print(model.test(dataSet))