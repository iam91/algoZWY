#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' Math Utility '

__author__ = 'zwy'

def dotProduct(x, y):
	n = len(x)
	ret = 0.0
	for i in range(n):
		ret += x[i] * y[i]
	return ret