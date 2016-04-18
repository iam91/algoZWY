#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' Definition of nodes for VFDT '

__author__ = 'zwy'

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
		for feat in categoricalFeaturesInfo:
			self.__statistics[feat] = [[0 for x in range(numOfClasses)] for x in range(categoricalFeaturesInfo[feat])]


	def getStatus(self):
		return self.__isActive


	def setStatus(self, isActive):
		self.__isActive = isActive


	def updateNode(self, instance, categoricalFeaturesInfo):
		classLabel = instance[-1]
		featureVec = [x for x in categoricalFeaturesInfo]
		for feat in featureVec:
			self.__statistics[feat][instance[feat]][classLabel] += 1

		self.__numOfInstancesSinceLastTry += 1


	def getNumOfInstancesSinceLastTry(self):
		return self.__numOfInstancesSinceLastTry

	def resetNumOfInstancesSinceLastTry(self):
		self.__numOfInstancesSinceLastTry = 0