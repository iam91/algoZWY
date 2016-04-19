#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' Definition of nodes for VFDT '

__author__ = 'zwy'

import math
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
	def __init__(self, split, depth):
		Node.__init__(self, 'split', depth)
		self.__split = split
		self.__children = None


	def getSplit(self):
		return self.__split


	def getChildren(self):
		return self.__children


	def setChild(self, index, child):
		self.__children[index] = child


	def setChildren(self, children):
		self.__children = children


# learning node
class LearningNode(Node):
	'''
	isActive is a boolean variable indicates whether the leaf is active or inactive
	'''
	def __init__(self, depth, numOfClasses, isActive, fatherBranch, categoricalFeaturesInfo):
		Node.__init__(self, 'leaf', depth)
		# for discrete features
		# self.__statistics[featureIndex][featureVal][classLabel]
		self.__statistics = {}
		self.__isActive = isActive
		# for discrete features
		# self.__fatherBranch is a tuple that takes the form: (fatherNode, branchIndex)
		self.__fatherBranch = fatherBranch
		self.__numOfClasses = numOfClasses
		self.__numOfInstancesSinceLastTry = 0
		self.__numOfInstancesFromBeginning = 0
		self.__classesCnt = [0 for x in range(numOfClasses)]
		for feat in categoricalFeaturesInfo:
			self.__statistics[feat] = [[0 for x in range(numOfClasses)] for x in range(categoricalFeaturesInfo[feat])]


	def getMajorityClass(self):
		maxCnt = self.__classesCnt[0]
		maxInd = 0
		for i in range(self.__numOfClasses):
			if(self.__classesCnt[i] > maxCnt):
				maxCnt = self.__classesCnt[i]
				maxInd = i
		return maxInd


	def getFatherBranch(self):
		return self.__fatherBranch


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
		self.__classesCnt[classLabel] += 1


	def getNumOfInstancesSinceLastTry(self):
		return self.__numOfInstancesSinceLastTry


	def resetNumOfInstancesSinceLastTry(self):
		self.__numOfInstancesSinceLastTry = self.__numOfInstancesFromBeginning


	def getNumOfInstancesFromBeginning(self):
		return self.__numOfInstancesFromBeginning


	def inheritStatistics(self, oldStatistics, featIndex):
		valIndex = 0
		for val in oldStatistics:
			labelIndex = 0
			for label in val:
				self.__statistics[featIndex][valIndex][labelIndex] = oldStatistics[valIndex][labelIndex]
				self.__numOfInstancesSinceLastTry += oldStatistics[valIndex][labelIndex]
				self.__numOfInstancesFromBeginning += oldStatistics[valIndex][labelIndex]
				self.__classesCnt[labelIndex] += oldStatistics[valIndex][labelIndex]
			labelIndex += 1
		valIndex += 1


	def trySplit(self, 
		categoricalFeaturesInfo, 
		hoeffdingBoundConfidence, 
		hoeffdingTieThreshold):
		splitCandidates = []
		numOfDiscreteFeatures = len(categoricalFeaturesInfo)

		for feat in categoricalFeaturesInfo:
			numOfFeatureValue = categoricalFeaturesInfo[feat]
			postImpurity = 0.0
			for i in range(numOfFeatureValue):
				classVec = self.__statistics[feat][i]

				featureValueWeight = sum(classVec)
				postImpurity += (featureValueWeight 
					/ self.__numOfInstancesFromBeginning) * VFDTClassifier.Impurity.entropy(classVec, self.__numOfClasses)

			splitCandidates.append((feat, postImpurity))

		preImpurity = VFDTClassifier.Impurity.entropy(self.__classesCnt, self.__numOfClasses)
		splitCandidatesInfoGains = [(x[0], preImpurity - x[1]) for x in splitCandidates]
		splitCandidatesInfoGains.sort(key = lambda x: x[1], reverse = True)
		#print(0, splitCandidatesInfoGains)
		best = splitCandidatesInfoGains[0]
		secondBest = splitCandidatesInfoGains[1]

		infoGainRange = math.log(self.__numOfClasses)
		hoeffdingBound = self.__computeHoeffdingBound(infoGainRange, 
			hoeffdingBoundConfidence, self.__numOfInstancesFromBeginning)
		#print(2, best[1] - secondBest[1], hoeffdingBound)
		if((best[1] - secondBest[1]) > hoeffdingBound or hoeffdingBound < hoeffdingTieThreshold):
			splitFeature = best[0]
			splitPoints = [x for x in range(categoricalFeaturesInfo[splitFeature])]

			split = (splitFeature, splitPoints)

			# create a split node waiting for seting children
			splitNode = VFDTClassifier.Node.SplitNode(split, self.getDepth())

			# create children
			children = [VFDTClassifier.Node.LearningNode(self.getDepth() + 1, 
				self.__numOfClasses, 
				True, 
				(splitNode, x),
				categoricalFeaturesInfo) for x in splitPoints]

			# update the statistics of children
			featIndex = 0
			for child in children:
				child.inheritStatistics(self.__statistics[featIndex], featIndex)
				featIndex += 1

			# attach children to their father(the newly created split node)
			splitNode.setChildren(children)
			return splitNode
		else:
			return self


	def __computeHoeffdingBound(self, r, confidence, weight):
		#print(1, r, confidence, weight, math.sqrt((r * r * math.log(1.0 / confidence)) / (2 * weight)))
		return math.sqrt((r * r * math.log(1.0 / confidence)) / (2 * weight))


'''
# update the statistics of children

featIndex = 0
for child in children:
child.inheritStatistics(self.__statistics[featIndex], featIndex)
featIndex += 1
'''
				
'''
def inheritStatistics(self, oldStatistics, featIndex):
valIndex = 0
for val in oldStatistics:
labelIndex = 0
for label in val:
self.__statistics[featIndex][valIndex][labelIndex] = oldStatistics[valIndex][labelIndex]
self.__numOfInstancesSinceLastTry += oldStatistics[valIndex][labelIndex]
self.__numOfInstancesFromBeginning += oldStatistics[valIndex][labelIndex]
self.__classesCnt[labelIndex] += oldStatistics[valIndex][labelIndex]
labelIndex += 1
valIndex += 1
'''
		
