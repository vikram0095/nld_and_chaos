# -*- coding: utf-8 -*-
"""
Created on Mon Aug 19 15:00:48 2019

@author: Vikram
"""

import numpy as np
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d.axes3d as p3
import matplotlib.animation as animation
from mpl_toolkits.mplot3d import Axes3D
from scipy.integrate import odeint

rho=29
sigma=10
beta=8/3

def model(state,t):
    x,y,z=state
    dxdt=sigma*(y-x)
    dydt=x*(rho-z)-y
    dzdt=x*y-beta*z
    return dxdt,dydt,dzdt


N=10000
step=0.01
t = np.arange(0.0, N*step,step)
st01=[20,20,20]
st02=[20,20.5,20]

speed=1
no_of_points_visible=500
y1 = odeint(model,st01,t)
y2 = odeint(model,st02,t)


fig = plt.figure()
ax = Axes3D(fig)
ax.view_init(elev=20, azim=106)

def update_lines(num, dataLines, lines):
    for line, data in zip(lines, dataLines):

        line.set_data(data[0:2, max(num*speed-no_of_points_visible,0):num*speed])
        line.set_3d_properties(data[2,max(num*speed-no_of_points_visible,0):num*speed])
        #ax.view_init(elev=10, azim=((num%3600)/10))
        #fig.canvas.draw()
    return lines

data = np.array([y1.T,y2.T])

lines = [ax.plot(dat[0, 0:1], dat[1, 0:1], dat[2, 0:1])[0] for dat in data]
ax.set_xlim(-40,40)
ax.set_ylim(-40,40)
ax.set_zlim(0,80)

print(np.shape(data))
print(np.shape(lines))


line_ani = animation.FuncAnimation(fig, update_lines, frames=2000, fargs=(data, lines),
                                   interval=10, blit=True, repeat=True)
#line_ani.save('lorentz_attractor.mp4', fps=50, extra_args=['-vcodec', 'libx264'])
plt.show()
