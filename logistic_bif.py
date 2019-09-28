# -*- coding: utf-8 -*-
"""
Created on Fri Sep  6 16:57:27 2019

@author: Vikram
"""

# -*- coding: utf-8 -*-
"""
Created on Sun Sep  1 19:20:32 2019

@author: Vikram
"""

import numpy as np
import matplotlib.pyplot as plt

N=100000
N0=99900

for A in np.arange(1,4,0.00001):
    x=np.zeros(N)
    x[0]=0.5
    for i in range(0,N-1):
        x[i+1]=x[i]*A*(1-x[i])
    
    temp=x[N0:N]
    temp[temp<0]=0
    #np.unique
    mat=((np.round(temp,decimals=6)))
    xx=A*np.ones(np.shape(mat))
    plt.plot(xx,mat,'r,',alpha=0.2)

    #    print(x[i])
    #plt.figure()
