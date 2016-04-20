#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' Hoeffding Tree '

__author__ = 'zwy'

import math

class HoeffdingTree(object):
	def __init__(self, 
		gracePeriod, 
		numOfClasses, 
		hoeffdingBoundConfidence, 
		hoeffdingTieThreshold, 
		categoricalFeaturesInfo):
		self.__root = None
		self.__gracePeriod = gracePeriod
		self.__numOfClasses = numOfClasses
		self.__hoeffdingBoundConfidence = hoeffdingBoundConfidence
		self.__hoeffdingTieThreshold = hoeffdingTieThreshold
		self.__featuresInfo = featuresInfo


	def train(self, instance):
		if(self.__root == None):
			self.__root = 