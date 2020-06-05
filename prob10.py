#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun  5 14:21:33 2020
Fourier transform of box function
@author: chintan
"""
import numpy as np
from matplotlib import pyplot as plt

def f(x):
    if -1<x<1:
        return(1)
    return(0)

#1 numpoints=64
xmin=-10
xmax=10
n=64
dx=(xmax-xmin)/(n-1)
x=np.linspace(xmin,xmax,n)
y=np.zeros(n)
for i in range(n):
    y[i]=f(x[i])
k=2*np.pi*np.fft.fftfreq(n,d=dx) 
factor=np.exp(-1j*k*xmin)
ft=np.fft.fft(y,norm='ortho')
aft=dx*np.sqrt(n/(2*np.pi))*factor*ft
plt.scatter(k,aft)  
plt.title('n=64')
plt.show()

#2 numpoints=128
xmin=-10
xmax=10
n=128
dx=(xmax-xmin)/(n-1)
x=np.linspace(xmin,xmax,n)
y=np.zeros(n)
for i in range(n):
    y[i]=f(x[i])
k=2*np.pi*np.fft.fftfreq(n,d=dx) 
factor=np.exp(-1j*k*xmin)
ft=np.fft.fft(y,norm='ortho')
aft=dx*np.sqrt(n/(2*np.pi))*factor*ft
plt.scatter(k,aft)  
plt.title('n=128')
plt.show()

#3 numpoints=256
xmin=-10
xmax=10
n=256
dx=(xmax-xmin)/(n-1)
x=np.linspace(xmin,xmax,n)
y=np.zeros(n)
for i in range(n):
    y[i]=f(x[i])
k=2*np.pi*np.fft.fftfreq(n,d=dx) 
factor=np.exp(-1j*k*xmin)
ft=np.fft.fft(y,norm='ortho')
aft=dx*np.sqrt(n/(2*np.pi))*factor*ft
plt.scatter(k,aft)  
plt.title('n=256')
plt.show()

    
