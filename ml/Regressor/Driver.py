#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' Driver for Regressor'

__author__ = 'zwy'

import sys

import LinearRegression.LinearRegression

args = sys.argv
if len(args) < 3:
	print('Usage: data file and regressor')
	exit()
else:
	fileDir = args[1]
	regressor = args[2]
	dataFile = open(fileDir, 'r')
	rawData = [line.strip('\n').split(',') for line in dataFile.readlines()]
	dataFile.close()

	if(fileDir.endswith("airfoil.csv")):
		dataSet = []
		for data in rawData:
			d = [float(x) for x in data]
			dataSet.append(d)
	for data in dataSet:
		print(data)
	if(regressor == 'LinearRegression'):
		print(LinearRegression.LinearRegression.train([1, 0], [0, 1]))
		