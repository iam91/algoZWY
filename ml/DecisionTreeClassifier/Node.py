#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' Definition of nodes for DecisionTreeClassifier '

__author__ = 'zwy'

# base node
class Node(object):
	def __init__(self, nodeType, depth):
		self.__nodeType = nodeType
		self.__depth = depth
		#print(nodeType)

	def getNodeType(self):
		return self.__nodeType

	def getDepth(self):
		return self.__depth

# split node
class SplitNode(Node):
	def __init__(self, nodeType, split, children, depth):
		Node.__init__(self, nodeType, depth)
		self.__split = split
		self.__children = children
		#print(nodeType)

	def getSplit(self):
		return self.__split

	def getChildren(self):
		return self.__children

# leaf node
class LeafNode(Node): 
	def __init__(self, nodeType, classLabel, depth):
		Node.__init__(self, nodeType, depth)
		self.__classLabel = classLabel

	def getClassLabel(self):
		return self.__classLabel
		