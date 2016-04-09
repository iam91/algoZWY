#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' Definition of DecisionTreeModel '

__author__ = 'zwy'

import Node

class DecisionTreeModel(object):
	def __init__(self, root):
		self.__root = root

	def test(self, dataSet):
		result = [self.singleClassify(data) == data[-1] for data in dataSet]
		cnt = 0
		for re in result:
			if(not re):
				cnt += 1
		print(cnt / len(result))
		return result

	def singleClassify(self, data):
		return self.__traverse(data, self.__root)

	def __traverse(self, data, node):
		type = node.getNodeType()
		if(type == 'leaf'):
			return node.getClassLabel()
		elif(type == 'split'):
			split = node.getSplit()
			splitFeature = split[0]
			splitPoints = split[1]
			numOfSplitPoints = len(splitPoints)

			cnt = 0
			for splitPoint in splitPoints:
				if(data[splitFeature] < splitPoint):
					return self.__traverse(data, node.getChildren()[cnt])
				elif(cnt >= numOfSplitPoints - 1):
					return self.__traverse(data, node.getChildren()[cnt + 1])
				cnt += 1
				