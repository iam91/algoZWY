#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' Definition of nodes for VFDT '

__author__ = 'zwy'

import VFDTClassifier.Impurity

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


# split node
class SplitNode(Node):
	def __init__(self, split, children, depth):
		Node.__init__(self, 'split', depth)
		self.__split = split
		self.__children = children


	def getSplit(self):
		return self.__split


	def getChildren(self):
		return self.__Children


# learning node
class LearningNode(Node):
	'''
	isActive is a boolean variable indicates whether the leaf is active or inactive
	'''
	def __init__(self, depth, numOfClasses, isActive, categoricalFeaturesInfo):
		Node.__init__(self, 'leaf', depth)
		# for discrete features
		# __statistics[featureIndex][featureVal][classLabel]
		self.__statistics = {}
		self.__isActive = isActive
		self.__numOfInstancesSinceLastTry = 0
		self.__numOfInstancesFromBeginning = 0
		for feat in categoricalFeaturesInfo:
			self.__statistics[feat] = [[0 for x in range(numOfClasses)] for x in range(categoricalFeaturesInfo[feat])]


	def getStatus(self):
		return self.__isActive


	def setStatus(self, isActive):
		self.__isActive = isActive


	def updateNode(self, instance, categoricalFeaturesInfo):
		classLabel = instance[-1]
		featureIndexVec = [x for x in categoricalFeaturesInfo]
		for feat in featureIndexVec:
			self.__statistics[feat][instance[feat]][classLabel] += 1

		self.__numOfInstancesFromBeginning += 1


	def getNumOfInstancesSinceLastTry(self):
		return self.__numOfInstancesSinceLastTry


	def resetNumOfInstancesSinceLastTry(self):
		self.__numOfInstancesSinceLastTry = self.__numOfInstancesFromBeginning


	def getNumOfInstancesFromBeginning(self):
		return self.__numOfInstancesFromBeginning


	def trySplit(self, 
		categoricalFeaturesInfo, 
		numOfClasses, 
		hoeffdingBountConfidence, 
		hoeffdingTieThreshold):
		splitCandidates = []
		numOfDiscreteFeatures = len(categoricalFeaturesInfo)
		totClassCnt = [0 for x in range(numOfDiscreteClass)]
		for feat in categoricalFeaturesInfo:
			numOfFeatureValue = categoricalFeaturesInfo[feat]
			postImpurity = 0.0
			for i in range(numOfFeatureValue):
				classVec = self.__statistics[feat][i]

				for j in range(numOfDiscreteClass):
					totClassCnt[j] += classVec[j]

				featureValueWeight = sum(classVec)
				postImpurity += (featureValueWeight 
					/ self.__numOfInstancesFromBeginning) * Impurity.entropy(classVec, numOfClasses)

			splitCandidates.append((feat, postImpurity))

		preImpurity = Impurity.entropy(totClassCnt, numOfClasses)
		splitCandidatesInfoGains = [(x[0], preImpurity - x[1]) for x in splitCandidates]
		splitCandidatesInfoGains.sort(key = lambda x: x[1], reverse = True)

		best = splitCandidatesInfoGains[0]
		secondBest = splitCandidatesInfoGains[1]

		infoGainRange = math.log(numOfClasses)
		hoeffdingBound = self.__computeHoeffdingBound(infoGainRange, 
			hoeffdingBountConfidence, self.__numOfInstancesFromBeginning)

		if((best[1] - secondBest[1]) > hoeffdingBound 
			|| hoeffdingBound < hoeffdingTieThreshold):
			


	def __computeHoeffdingBound(self, r, confidence, weight):
		return math.sqrt((r * r * math.log(1.0 / confidence)) / (2 * weight))



				

		
