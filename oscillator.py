import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import odeint
from matplotlib.animation import FuncAnimation,FFMpegFileWriter

fig, (ax1,ax2) = plt.subplots(nrows=1,ncols=2,figsize=(20, 6))

x11data,x12data , y11data,y12data , x2data, y21data ,y22data  = [], [],[], [],[],[],[]
ln11, = ax1.plot([], [], 'r', animated=True)
ln12, = ax1.plot([], [], 'b', animated=True)
ln21, = ax2.plot([], [], 'r', animated=True)
ln22, = ax2.plot([], [], 'b', animated=True)


f = np.linspace(-3, 3, 200)

def init():
    ax1.set_xlim(-3, 3)
    ax1.set_ylim(-3, 3)
    ax2.set_xlim(1, 100)
    ax2.set_ylim(-4, 4)
    
#ax1.set_ylabel('common ylabel')
    ln11.set_data(x11data,y11data)
    ln12.set_data(x12data,y12data)
    ln21.set_data(x2data,y21data)
    ln22.set_data(x2data,y22data)
    ax1.set_title( ("r ={} ; w = {} ; ic : (x={},x\'='{})".format(r,omega,st02[0],st02[1])) )
    ax2.set_title( ("r ={} ; w = {} ; ic : (x={},x\'='{})".format(r,omega,st01[0],st01[1])) )
    ax2.set_xlabel('time')
    ax2.set_ylabel('x(t)')
    ax1.set_xlabel('x')
    ax1.set_ylabel('x\'')
    return ln11,ln12,ln21,ln22


r=0
omega=1


def model(state,t):
    x,y =state
    dxdt = y
    dydt = -r*y-omega*omega*x#-0.1*np.sin(0.5*t)
    return dxdt,dydt

N=1000
step=0.15
t = np.arange(0.0, N*step,step)
st01=[0.5,1.0]
st02=[1,0.2]


y1 = odeint(model,st01,t)
y2 = odeint(model,st02,t)


def update(frame):
    x11data.append(y1[frame,0])
    y11data.append(y1[frame,1])

    x12data.append(y2[frame,0])
    y12data.append(y2[frame,1])

    x2data.append(t[frame])
    y21data.append(y1[frame,0])
    y22data.append(y2[frame,0])

    ln11.set_data(x11data,y11data)
    ln12.set_data(x12data,y12data)
    ln21.set_data(x2data,y21data)
    ln22.set_data(x2data,y22data)
    return ln11,ln12,ln21,ln22



    
ani = FuncAnimation(fig, update, frames=range(1,N),
                    init_func=init, blit=True, interval = 0.01,repeat=False)

#print('Writing movie\n')
#ani.save('basic_animation.mp4', fps=30, extra_args=['-vcodec', 'libx264'])
plt.show()


