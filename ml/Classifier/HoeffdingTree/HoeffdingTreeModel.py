#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' Definition of HoeffdingTreeModel '

__author__ = 'zwy'

import HoeffdingTree.Node
import HoeffdingTree.Split

class HoeffdingTreeModel(object):
	def __init__(self, root):
		self.__root = root


	def __leafForInstance(self, instance, node):
		if(node.getNodeType() == 'leaf'):
			return node
		elif(node.getNodeType() == 'split'):
			split = node.getSplit()
			splitFeature = split.getFeatureIndex()
			splitPoints = split.getSplitPoints()
			featureType = split.getFeatureType()
			if(featureType == 'continuous'):
				value = instance[splitFeature]
				if(value <= splitPoints):
					return self.__leafForInstance(instance, node.getChildren()[0])
				else:
					return self.__leafForInstance(instance, node.getChildren()[1])
			elif(featureType == 'nominal'):
				for splitPoint in splitPoints:
					if(instance[splitFeature] == splitPoint):
						return self.__leafForInstance(instance, node.getChildren()[splitPoint])



	def singleClassify(self, instance):
		leaf = self.__leafForInstance(instance, self.__root)
		leaf._LearningNode__statistics[0].getStatistics()
		return leaf.getMajorityClass()


	def test(self, dataSet):
		result = [self.singleClassify(data) == data[-1] for data in dataSet]
		cnt = 0
		for re in result:
			if(not re):
				cnt += 1
		print(cnt / len(result))
		return result
