#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' Definition of nodes for hoeffding tree '

__author__ = 'zwy'

class Split(object):
	def __init__(self, featureIndex, splitPoints, featureType, infoGain):
		self.__featureIndex = featureIndex
		self.__splitPoints = splitPoints
		self.__featureType = featureType
		self.__infoGain = infoGain


	def getFeatureIndex(self):
		return self.__featureIndex


	def getSplitPoints(self):
		return self.__splitPoints


	def getFeatureType(self):
		return self.__featureType


	def getInfoGain(self):
		return self.__infoGain


	def getNumOfSplitBins(self):
		if(self.__featureType == 'continuous'):
			return 2
		elif(self.__featureType == 'nominal'):
			return len(self.__splitPoints)


class Branch(object):
	def __init__(self, fatherPointer, childIndex):
		self.__fatherPointer = fatherPointer
		self.__childIndex = childIndex

	
	def getFatherPointer(self):
		return self.__fatherPointer


	def getChildIndex(self):
		return self.__childIndex
