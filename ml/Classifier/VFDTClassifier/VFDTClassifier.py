#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' VFDTClassifier '

__author__ = 'zwy'

'''
Implement discrete features
'''

import math
import VFDTClassifier.Impurity
import VFDTClassifier.Node

class VFDT(object):
	def __init__(self, 
		gracePeriod, 
		numOfClasses, 
		hoeffdingBoundConfidence,
		hoeffdingTieThreshold, 
		categoricalFeaturesInfo):
		self.__gracePeriod = gracePeriod
		self.__root = None
		self.__numOfClasses = numOfClasses
		self.__hoeffdingBoundConfidence = hoeffdingBoundConfidence
		self.__hoeffdingTieThreshold = hoeffdingTieThreshold
		self.__categoricalFeaturesInfo = categoricalFeaturesInfo


	def returnModel(self):
		return self.__root


	def train(self, instance):
		if(self.__root == None):
			self.__root = VFDTClassifier.Node.LearningNode(1, self.__numOfClasses, True, self.__categoricalFeaturesInfo)
			self.__root.updateNode(instance, self.__categoricalFeaturesInfo)
		else:
			nodeType = self.__root.getNodeType()
			if(nodeType == 'leaf'):
				instanceLeaf = self.__leafForInstance(instance, self.__root)
				if(instanceLeaf.getStatus()):
					instanceLeaf.updateNode(instance, self.__categoricalFeaturesInfo)
					if((instanceLeaf.getNumOfInstancesFromBeginning() - instanceLeaf.getNumOfInstancesSinceLastTry()) 
						> self.__gracePeriod):
						
						# TODO: try split

						instanceLeaf.resetNumOfInstancesSinceLastTry()
				else:
					pass
			elif(nodeType == 'split'):
				pass



	def __leafForInstance(self, instance, node):
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


	def __trySplit(self, node):
		pass
		