#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' Definition of VFDTTreeModel '

__author__ = 'zwy'

import VFDTClassifier.Node

class VFDTModel(object):
	def __init__(self, root):
		self.__root = root


	def __traverse(self, instance, node):
		if(node.getNodeType() == 'leaf'):
			return node
		elif(node.getNodeType() == 'split'):
			split = node.getSplit()
			splitFeature = split[0]
			splitPoints = split[1]
			numOfSplitPoints = len(splitPoints)

			cnt = 0
			for splitPoint in splitPoints:
				if(data[splitFeature] < splitPoint):
					return self.__leafForInstance(instance, node.getChildren()[cnt])
				elif(cnt >= numOfSplitPoints - 1):
					return self.__leafForInstance(instance, node.getChildren()[cnt + 1])
				cnt += 1


	def test(self, dataSet):
		result = [self.singleClassify(data) == data[-1] for data in dataSet]
		cnt = 0
		for re in result:
			if(not re):
				cnt += 1
		print(cnt / len(result))
		return result


	def singleClassify(self, instance):
		leaf = self.__traverse(instance, self.__root)
		return leaf.getMajorityClass()


	def printModel():
		pass
