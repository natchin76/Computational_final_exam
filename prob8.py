#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun  5 13:39:15 2020
Prob8: BVP
@author: chintan
"""
import numpy as np
from matplotlib import pyplot as plt
from scipy.integrate import solve_bvp
def f(x,y):
    return(np.vstack((y[1],4*(y[0]-x))))
n=10
x1=0
x2=1
y1=0
y2=2
x=np.linspace(x1,x2,n)
y=np.zeros((2,n))
def bc(ya,yb):
    return(ya[0]-y1,yb[0]-y2)
soln=solve_bvp(f,bc,x,y)
xp=np.linspace(x1,x2,50)      
yp=soln.sol(xp)[0]
e=np.exp(1)
y_ext=e**2*(e**4-1)**(-1)*(e**(2*xp)-e**(-2*xp))+xp
plt.scatter(xp,yp,label='using scipy')
plt.plot(xp,y_ext,label='exact soln')
plt.legend()
plt.xlabel('x')
plt.ylabel('y(x)')
plt.grid()
plt.show()

rel_err=abs(y_ext-yp)/y_ext*100
rel_err[0]=0
rel_err[n-1]=0
print('relative error in percentage:',rel_err)
