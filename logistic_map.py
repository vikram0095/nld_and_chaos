# -*- coding: utf-8 -*-
"""
Created on Sun Sep  1 19:20:32 2019

@author: Vikram
"""

import numpy as np
import matplotlib.pyplot as plt

A=3.74
N=500
N0=450
#x=np.zeros(N)
#x1=np.zeros(N)
#
#x[0]=0.5
#x1[0]=0.5
#for i in range(0,N-1):
#    x[i+1]=x[i]*A*(1-x[i])
#    x1[i+1]=x1[i]*A*(1-x1[i])
#plt.plot(x[N0:N])
#
#plt.plot(x1[N0:N])
#
#plt.figure()
#plt.scatter(x[N0-1:N-1],x[N0:N])

x=np.zeros(N)
cx=np.zeros(N)
cy=np.zeros(N)

x1=np.zeros(N)
cx1=np.zeros(N)
cy1=np.zeros(N)

x[0]=0.30000001
cx[0]=x[0]
cy[0]=0
cx[1]=x[0]
cy[1]=x[0]*A*(1-x[0])

x1[0]=0.3
cx1[0]=x1[0]
cy1[0]=0
cx1[1]=x1[0]
cy1[1]=x1[0]*A*(1-x1[0])

for i in range(1,N-2,2):
    cx[i+1]=cy[i]
    cy[i+1]=cy[i]
    cx[i+2]=cx[i+1]
    cy[i+2]=cy[i+1]*A*(1-cy[i+1]);
    
    cx1[i+1]=cy1[i]
    cy1[i+1]=cy1[i]
    cx1[i+2]=cx1[i+1]
    cy1[i+2]=cy1[i+1]*A*(1-cy1[i+1]);
#    print(x[i])
#plt.figure()
x_all=np.arange(0,1.01,0.01);
plt.plot(x_all,A*np.multiply(x_all,(1-x_all)))
plt.plot(cx[N0:N],cy[N0:N])
plt.plot(cx1[N0:N],cy1[N0:N])
plt.plot([0,1],[0,1],'k')
del x
del x1
x=np.zeros(N)
x1=np.zeros(N)
x[0]=0.3
x1[0]=0.300000001
for i in range(0,N-1):
    x[i+1]=x[i]*A*(1-x[i])
    x1[i+1]=x1[i]*A*(1-x1[i])
plt.figure()
plt.plot(x[N0:N])
plt.plot(x1[N0:N])
