import numpy as np
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d.axes3d as p3
import matplotlib.animation as animation
from mpl_toolkits.mplot3d import Axes3D
rho=29
sigma=10
beta=8/3
del_t=0.01
N=4000



x2=np.zeros((N,))
y2=np.zeros((N,))
z2=np.zeros((N,))

x1=np.zeros((N,))
y1=np.zeros((N,))
z1=np.zeros((N,))

x1[0]=1
y1[0]=1
z1[0]=1

x2[0]=1
y2[0]=15
z2[0]=1


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

fig = plt.figure()
ax = Axes3D(fig)
def update_lines(num, dataLines, lines):
    for line, data in zip(lines, dataLines):
        # NOTE: there is no .set_data() for 3 dim data...
        line.set_data(data[0:2, :num])
        line.set_3d_properties(data[2, :num])
        ax.view_init(elev=10, azim=((num%3600)/10))
        fig.canvas.draw()
    return lines


data = np.array([[x1,y1,z1],[x2,y2,z2]])

lines = [ax.plot(dat[0, 0:1], dat[1, 0:1], dat[2, 0:1])[0] for dat in data]

ax.set_xlim(-40,40)
ax.set_ylim(-40,40)
ax.set_zlim(0,80)

print(np.shape(data))
#print(np.shape(lines))


line_ani = animation.FuncAnimation(fig, update_lines, frames=2000, fargs=(data, lines),
                                   interval=1, blit=True, repeat=True)
#line_ani.save('lorentz_attractor.mp4', fps=50, extra_args=['-vcodec', 'libx264'])
plt.show()
