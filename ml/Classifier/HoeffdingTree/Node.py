#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' Definition of nodes for hoeffding tree '

__author__ = 'zwy'

import HoeffdingTree.Utils

# base node
class Node(object):
	'''
	nodeType: 'split' or 'leaf'
	'''
	def __init__(self, nodeType, depth):
		self.__nodeType = nodeType
		self.__depth = depth


	def getNodeType(self):
		return self.__nodeType


	def getDepth(self):
		return self.__depth


class LearningNode(Node):
	def __init__(self, 
		depth, 
		numOfClasses, 
		numOfFeatures, 
		isActive, 
		fatherBranch, 
		featureInfo, 
		hoeffdingBoundConfidence, 
		hoeffdingTieThreshold):
		Node.__init__(self, 'leaf', depth)
		self.__numOfClasses = numOfClasses
		self.__numOfFeatures = numOfFeatures
		self.__isActive = isActive
		self.__fatherBranch = fatherBranch
		self.__featureInfo = featureInfo
		self.__hoeffdingBoundConfidence = hoeffdingBoundConfidence
		self.__hoeffdingTieThreshold = hoeffdingTieThreshold
		self.__numOfInstancesSinceLastTry = 0
		self.__numOfInstancesFromBeginning = 0
		self.__statistics = {}
		for feat in self.__featureInfo:
			numOfValues = self.__featureInfo[feat]
			if(numOfValue == 0):
				self.__statistics[feat] \
					= HoeffdingTree.Utils.ContinuousFeatureStatistcs(self.__numOfClasses)
			else:
				self.__statistics[feat] \
					= HoeffdingTree.Utils.NominalFeatureStatistics(numOfValues, self.__numOfClasses)


		def getFatherBranch(self):
			return self.__fatherBranch


		def updateNode(self, instance):
			classLabel = instance[-1]
			for feat in self.__numOfFeatures:
				value = instance[feat]
				self.__statistics[feat].update(value, classLabel)


		def getNumOfInstancesFromBeginning(self):
			return self.__numOfInstancesFromBeginning


		def getNumOfInstancesSinceLastTry(self):
			return self.__numOfInstancesSinceLastTry


		def resetNumOfInstancesSinceLastTry(self):
			self.__numOfInstancesSinceLastTry = self.__numOfInstancesFromBeginning


		def trySplit(self):
			pass


class Branch(Oject):
	def __init__(self, fatherPoiner, splitIndex):
		self.__fatherPointer = fatherPointer
		self.__splitIndex = splitIndex

	
	def getFatherPointer(self):
		return self.__fatherPointer


	def getSplitIndex(self):
		return self.__splitIndex
