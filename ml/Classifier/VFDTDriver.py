#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' Driver for Classifier '

__author__ = 'zwy'

import sys
import VFDTClassifier.VFDTClassifier

args = sys.argv
if len(args) < 2:
	print('Usage: data file')
	exit()
else:
	fileDir = args[1]
	dataFile = open(fileDir, 'r')
	rawData = [line.strip('\n').split(',') for line in dataFile.readlines()]
	dataFile.close()
	# format the dataset into [feature1, feature2, ..., featuren, classlabel]
	# class labels take the value 0, 1, 2, ... and -1 for known class
	# ordinal features take the value 1, 2, 3, ...

	if(fileDir.endswith("iris.csv")):
		# format iris
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
	elif(fileDir.endswith("balance-scale.csv")):
		# format balance-scale
		dataSet = []
		for line in rawData:
			classLabel = line[0]
			data = [int(val) - 1 for val in line[1:5]]
			if(classLabel == 'R'):
				data.append(0)
			elif(classLabel == 'B'):
				data.append(1)
			elif(classLabel == 'L'):
				data.append(2)
			dataSet.append(data)
	elif(fileDir.endswith("data_banknote_authentication.csv")):
		# format banknote authentication
		dataSet = []
		for line in rawData:
			data = [float(val) for val in line]
			dataSet.append(data)
	elif(fileDir.endswith("nursery.csv")):
		# format nursery
		dataSet = []
		for line in rawData:
			data = [int(val) for val in line]
			dataSet.append(data)
	
	# for discreate features, their values should start from 0
	mm = {0: 3, 1: 5, 2: 4, 3: 4, 4: 3, 5: 2, 6: 3, 7: 3}
	tree = VFDTClassifier.VFDTClassifier.VFDT(200, 5, 0.0001, 0.05, mm)
	for data in dataSet:
		tree.train(data)

	model = tree.getModel() 
	#model.printModel()
	model.test(dataSet)