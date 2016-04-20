#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' Definition of HoeffdingTreeModel '

__author__ = 'zwy'

import HoeffdingTree.Node
import HoeffdingTree.Split

class HoeffdingTreeModal(object):
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
				if(value < splitPoints):
					return self.__leafForInstance(instance, node.getChildren()[0])
				elif:
					return self.__leafForInstance(instance, node.getChildren()[1])
			elif(featureType == 'nominal'):
				for splitPoint in splitPoints:
					return self.__leafForInstance(instance, node.getChildren()[splitPoint])


	def singleClassify(self, instance):
		leaf = self.__traverse(instance, self.__root)
		return leaf.getMajorityClass()
