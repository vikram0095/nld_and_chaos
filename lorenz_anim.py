import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation,FFMpegFileWriter

fig, (ax1,ax2,ax3) = plt.subplots(nrows=3,ncols=1,figsize=(20, 6),sharex=True)

xdata, y11data,y12data ,y21data ,y22data ,y31data ,y32data = [], [],[], [],[], [],[]
ln11, = ax1.plot([], [], 'r', animated=True)
ln12, = ax1.plot([], [], 'b', animated=True)
ln21, = ax2.plot([], [], 'r', animated=True)
ln22, = ax2.plot([], [], 'b', animated=True)
ln31, = ax3.plot([], [], 'r', animated=True)
ln32, = ax3.plot([], [], 'b', animated=True)


rho=29
sigma=10
beta=8/3
del_t=0.01
N=1500
f = np.linspace(-3, 3, 200)

x2=np.zeros((N,1))
y2=np.zeros((N,1))
z2=np.zeros((N,1))

x1=np.zeros((N,1))
y1=np.zeros((N,1))
z1=np.zeros((N,1))

x1[0]=1
y1[0]=1
z1[0]=1

x2[0]=1
y2[0]=1.0001
z2[0]=1



def init():
    ax1.set_xlim(1, N)
    ax1.set_ylim(-30, 30)
    ax2.set_xlim(1, N)
    ax2.set_ylim(-40, 40)
    ax3.set_xlim(1, N)
    ax3.set_ylim(0, 60)
    plt.xlabel('Iteration')
    ax1.set_title( ("Initital Conditions (x,y,z) for Blue:({},{},{}) and Red:({},{},{})").format(x1[0][0],y1[0][0],z1[0][0],x2[0][0],y2[0][0],z2[0][0]) )
    ln11.set_data(xdata,y11data)
    ln12.set_data(xdata,y12data)
    ln21.set_data(xdata,y21data)
    ln22.set_data(xdata,y22data)
    ln31.set_data(xdata,y31data)
    ln32.set_data(xdata,y32data)
    return ln11,ln12,ln21,ln22,ln31,ln32




for t_iter in range(1,N):
    
    del_x1=sigma*(y1[t_iter-1]-x1[t_iter-1]);
    del_y1=x1[t_iter-1]*(rho-z1[t_iter-1])-y1[t_iter-1]
    del_z1=x1[t_iter-1]*y1[t_iter-1]-beta*z1[t_iter-1]
    
    del_x2=sigma*(y2[t_iter-1]-x2[t_iter-1]);
    del_y2=x2[t_iter-1]*(rho-z2[t_iter-1])-y2[t_iter-1]
    del_z2=x2[t_iter-1]*y2[t_iter-1]-beta*z2[t_iter-1]
    
    x1[t_iter]=x1[t_iter-1]+del_x1*del_t;
    y1[t_iter]=y1[t_iter-1]+del_y1*del_t;
    z1[t_iter]=z1[t_iter-1]+del_z1*del_t;
    
    x2[t_iter]=x2[t_iter-1]+del_x2*del_t;
    y2[t_iter]=y2[t_iter-1]+del_y2*del_t;
    z2[t_iter]=z2[t_iter-1]+del_z2*del_t;
    
def update(frame):
    xdata.append(frame)
    y11data.append(x1[frame])
    y12data.append(x2[frame])
    y21data.append(y1[frame])
    y22data.append(y2[frame])
    y31data.append(z1[frame])
    y32data.append(z2[frame])
    ln11.set_data(xdata, y11data)
    ln12.set_data(xdata, y12data)
    ln21.set_data(xdata, y21data)
    ln22.set_data(xdata, y22data)
    ln31.set_data(xdata, y31data)
    ln32.set_data(xdata, y32data)
    return ln11,ln12,ln21,ln22,ln31,ln32




    
ani = FuncAnimation(fig, update, frames=range(1,N),
                    init_func=init, blit=True, interval = 1,repeat=False)

#print('Writing movie\n')
#ani.save('basic_animation1.mp4', fps=30, extra_args=['-vcodec', 'libx264'])
plt.show()


