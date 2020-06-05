#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun  5 13:19:08 2020
Prob6: IVP
@author: chintan
"""
import numpy as np
from matplotlib import pyplot as plt
from scipy.integrate import solve_ivp

def f(x,y):
    f=[32*y[0]+66*y[1]+2*x/3+2/3,-66*y[0]-133*y[1]-x/3-1/3]
    return(f)
y=solve_ivp(f,[0,0.5],[1/3,1/3],t_eval=np.linspace(0,0.5,50))
plt.plot(y.t,y.y[0],label='y1',marker='o')
plt.plot(y.t,y.y[1],label='y2',marker='o')
plt.legend()
plt.xlabel('x')
plt.show()