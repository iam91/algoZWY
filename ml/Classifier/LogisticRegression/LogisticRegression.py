#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' Logistic regression '

__author__ = 'zwy'

'''
Work on continuous features 
'''

import math

def _sigmoid(x):
	return 1 / (1 + exp(-x))