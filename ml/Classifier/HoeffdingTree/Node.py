#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' Definition of nodes for hoeffding tree '

__author__ = 'zwy'

import math
import HoeffdingTree.Utils
import HoeffdingTree.Split

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
		self.__classesCnt = [0 for x in range(self.__numOfClasses)]
		self.__numOfInstancesSinceLastTry = 0
		self.__numOfInstancesFromBeginning = 0
		self.__statistics = {}
		for feat in self.__featureInfo:
			numOfValues = self.__featureInfo[feat]
			if(numOfValues == 0):
				self.__statistics[feat] \
					= HoeffdingTree.Utils.ContinuousFeatureStatistcs(self.__numOfClasses)
			else:
				self.__statistics[feat] \
					= HoeffdingTree.Utils.NominalFeatureStatistics(numOfValues, self.__numOfClasses)


	def getMajorityClass(self):
		maxCnt = self.__classesCnt[0]
		maxInd = 0
		for i in range(self.__numOfClasses):
			if(self.__classesCnt[i] > maxCnt):
				maxCnt = self.__classesCnt[i]
				maxInd = i
		return maxInd


	def getStatus(self):
		return self.__isActive


	def setStatus(self, isActive):
		self.__isActive = isActive


	def getFatherBranch(self):
		return self.__fatherBranch


	def updateNode(self, instance):
		classLabel = instance[-1]
		for feat in range(self.__numOfFeatures):
			value = instance[feat]
			self.__statistics[feat].update(value, classLabel)
		self.__classesCnt[classLabel] += 1


	def getNumOfInstancesFromBeginning(self):
		return self.__numOfInstancesFromBeginning


	def getNumOfInstancesSinceLastTry(self):
		return self.__numOfInstancesSinceLastTry


	def resetNumOfInstancesSinceLastTry(self):
		self.__numOfInstancesSinceLastTry = self.__numOfInstancesFromBeginning


	def trySplit(self):
		preImpurity = HoeffdingTree.Utils.entropy(self.__classesCnt)
		splitCandidates = []
		for feat in self.__featureInfo:
			numOfValues = self.__featureInfo[feat]
			if(numOfValues == 0):
				#continuous feature
				pass
			elif(numOfValues > 0):
				#nominal feature
				stat = self.__statistics[feat].getStatistics()
				postImpurity = 0.0
				totCnt = stat.getTotalCnt()
				for i in range(numOfValues):
					classCntVec = stat[i]
					currCnt = sum(classCntVec)
					currImpurity = HoeffdingTree.Utils.entropy(classCntVec)
					postImpurity += (currCnt / totCnt) * currImpurity
				currInfoGain = preImpurity - postImpurity
				currSplit = HoeffdingTree.Split.Split(feat, 
					list(range(numOfValues)), 
					'nominal', 
					currInfoGain)
				splitCandidates.append(currSplit)

		splitCandidates.sort(key = lambda x: x.getInfoGain(), reverse = True)

		best = splitCandidates[0]
		secondBest = splitCandidates[1]

		infoGainRange = math.log(self.__numOfClasses)
		hoeffdingBound = self.__computeHoeffdingBound(infoGainRange, 
			self.__hoeffdingBoundConfidence, 
			self.__numOfInstancesFromBeginning)

		if((best.getInfoGain - secondBest.getInfoGain) > hoeffdingBound
			or hoeffdingBound < hoeffdingTieThreshold):
			split = best
			numOfChildren = split.getNumOfSplitBins()

			# create a split node waiting for seting children
			splitNode = HoeffdingTree.Node.SplitNode(split, self.getDepth())

			children = [HoeffdingTree.Node.LearningNode(self.getDepth, 
				self.__numOfClasses, 
				self.__numOfFeatures, 
				True, 
				HoeffdingTree.Split.Branch(splitNode, x), 
				self.__featureInfo, 
				self.__hoeffdingBoundConfidence,
				self.__hoeffdingTieThreshold) for x in range(numOfChildren)]

			# attach children to their father(the newly created split node)
			splitNode.setChildren(children)
			return splitNode
		else:
			return self



	def __computeHoeffdingBound(self, r, confidence, weight):
		return math.sqrt((r * r * math.log(1.0 / confidence)) / (2 * weight))


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
