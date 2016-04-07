#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' Definition of DecisionTreeModel '

__author__ = 'zwy'

import Node

class DecisionTreeModel(object):
	def __init__(self, root):
		self.__root = root

	def test(self, dataSet):
		result = [self.__singleTest(data) == data[-1] for data in dataSet]
		return result

	def __singleTest(self, data):
		return self.__traverse(data, self.__root)

	def __traverse(self, data, node):
		type = node.getNodeType()
		if(type == 'leaf'):
			return node.getClassLabel()
		elif(type == 'split'):
			split = node.getSplit()
			splitFeature = split[0]
			splitPoint = split[1]
			if(data[splitFeature] < splitPoint):
				return self.__traverse(data, node.getChildren()[0])
			else:
				return self.__traverse(data, node.getChildren()[1])