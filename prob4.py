#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun  5 10:57:26 2020
Prob4: Power spectrum
@author: chintan
"""

import numpy as np
from matplotlib import pyplot as plt

#a)
n=1024
x=np.random.rand(n)
i=range(1,n+1)
plt.scatter(i,x)
plt.title('Uniform random nos.')
plt.show()

#b) Power spectrum
dft=np.fft.fft(x,norm='ortho')
k=np.fft.fftfreq(n)
k=np.fft.fftshift(2*np.pi*k)
p_k=np.abs(np.fft.fftshift(dft))**2
plt.plot(k,p_k)
plt.xlabel('k')
plt.ylabel('P(k)')
plt.title('Power spectrum')
plt.show()

#c)
print('kmin=',k[0])
print('kmax=',k[len(k)-1])

#d)
nbins=5
plt.hist(p_k,bins=np.linspace(k[0],k[n-1],6))  #histogram of power spectrum
plt.xlabel('k')
plt.ylabel('P(k)')
plt.title('Histogram of power spectrum')
plt.show()

#Bartlett method by binning into 5 bins
m=int(n/nbins)
ndata=x[0:1020].reshape([m,nbins])
Pk1=np.zeros([m,nbins])
knew=np.fft.fftfreq(m)
knew=np.fft.fftshift(knew)
for i in range(nbins):
    dft_temp=np.fft.fftshift(np.fft.fft(ndata[:,i],norm='ortho'))
    Pk1[:,i]=(abs(dft_temp))**2
Pk_n=np.zeros(m)
for i in range(m):
    Pk_n[i]=sum(Pk1[i,:])
plt.plot(knew,Pk_n)
plt.xlabel('k')
plt.ylabel('P(k)')
plt.title('Power spectrum by Bartlett method')
plt.show()


