#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' Hoeffding Tree '

__author__ = 'zwy'

import math
import HoeffdingTree.Node
import HoeffdingTree.Split
import HoeffdingTree.HoeffdingTreeModel

class HoeffdingTreeClassifier(object):
	def __init__(self, 
		gracePeriod, 
		numOfClasses, 
		hoeffdingBoundConfidence, 
		hoeffdingTieThreshold, 
		featuresInfo):
		self.__root = None
		self.__gracePeriod = gracePeriod
		self.__numOfClasses = numOfClasses
		self.__hoeffdingBoundConfidence = hoeffdingBoundConfidence
		self.__hoeffdingTieThreshold = hoeffdingTieThreshold
		self.__featuresInfo = featuresInfo


	def getModel(self):
		return HoeffdingTree.HoeffdingTreeModel.HoeffdingTreeModel(self.__root)


	def train(self, instance):
		if(self.__root == None):
			self.__root = HoeffdingTree.Node.LearningNode(1, 
				self.__numOfClasses, 
				len(self.__featuresInfo), 
				True, 
				None, 
				self.__featuresInfo, 
				self.__hoeffdingBoundConfidence, 
				self.__hoeffdingTieThreshold)
			self.__root.updateNode(instance)
		else:
			instanceLeaf = self.__leafForInstance(instance, self.__root)
			if(instanceLeaf.getStatus()):
				instanceLeaf.updateNode(instance)
				if((instanceLeaf.getNumOfInstancesFromBeginning() - instanceLeaf.getNumOfInstancesSinceLastTry()) 
					>= self.__gracePeriod):
					tryResultNode = self.__trySplit(instanceLeaf)
					fatherBranch = instanceLeaf.getFatherBranch()
					if(fatherBranch == None):
						self.__root = tryResultNode
					else:
						fatherBranch.getFatherPointer().setChild(fatherBranch.getChildIndex(), tryResultNode)
					instanceLeaf.resetNumOfInstancesSinceLastTry()
			else:
				pass


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
				else:
					return self.__leafForInstance(instance, node.getChildren()[1])
			elif(featureType == 'nominal'):
				for splitPoint in splitPoints:
					return self.__leafForInstance(instance, node.getChildren()[splitPoint])


	def __trySplit(self, node):
		return node.trySplit()