#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' Sigmoid Function '

__author__ = 'zwy'

import math

def sigmoid(x):
	return 1 / (1 + math.exp(-x))


def dotProduct(x, y):
	n = len(x)
	ret = 0.0
	for i in range(n):
		ret += x[i] * y[i]
	return ret

