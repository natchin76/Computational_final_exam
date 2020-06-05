#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun  5 13:56:04 2020
Prob 9: Singular values
@author: chintan
"""
import numpy as np
A=np.matrix([[2,1],[1,0],[0,1]])
B=np.array([[1,1,0],[1,0,1],[0,1,1]])
eig1=np.linalg.svd(A)[1]
eig2=np.linalg.svd(B)[1]
print('Singular values of A:',eig1)
print('Singular values of B:',eig2)