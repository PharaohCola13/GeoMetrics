# A Sphere, brough to you by PharaohCola13

import mpl_toolkits.mplot3d.axes3d as p3
import matplotlib.pyplot as plt

from mpl_toolkits.mplot3d.art3d import *
from matplotlib.animation import *
from matplotlib import *
from numpy import *

option = int(input('Run? (0) Yes, (1) No\n>> '))

while option == 0:
# Definition of x
	def x_(u,v):
    		x = cos(u) * sin(v)
    		return x

# Definition of y
	def y_(u,v):
    		y = sin(u) * sin(v)
    		return y

# Definition of z
	def z_(u,v):
    		z  = cos(v)
    		return z

# Number of edges on the base
	sides = int(input('How many sides?\n>> '))
	s = sides

# Values of the angles
	u = linspace(0, pi, s + 1)
	v = linspace(0, 2 * pi, 10)

	u, v = meshgrid(u, v)

# Symbolic Representation
	x = x_(u,v)
	y = y_(u,v)
	z = z_(u,v)

# Figure Properties
	fig = plt.figure(figsize=(8,8))

	ax = p3.Axes3D(fig)
	ax.set_facecolor('black') # Figure background turns black

# Axis Properties
	plt.axis('off') # Turns off the axis grid
	plt.axis('equal')

# Axis Limits
	ax.set_xlim(-1,1)
	ax.set_ylim(-1,1)
	ax.set_zlim(-1,1)

# Surface Plot
	sphere = ax.plot_surface(x, y, z)

	sphere.set_alpha(1) # Transparency of figure
	sphere.set_edgecolor('w') # Edge color of the lines on the figure
	sphere.set_linewidth(1) # Line width of the edges
	sphere.set_facecolor('deepskyblue') # General color of the figure

# Definitions for animation
	def init():
		return sphere,

	def animate(i):
# azimuth angle : 0 deg to 360 deg
# elev = i * n --> rotates object about the xy-plane with a magnitude of n
# azim = i * n --> rotates object around the z axis with a magnitude of n
# For top view elev = 90
# For side view elev = 0

			ax.view_init(elev=i, azim=i*4)
			return sphere,

# Animate
	ani = FuncAnimation(fig, animate, init_func=init,
	                   frames=100, interval=20, blit=False, repeat=True)

# Saving to Sphere.mp4

	#Writer = writers['ffmpeg']
	#writer = Writer(fps=15, bitrate=1800)
	
	#name = '%s-Sphere' % int(s)
	#ani.save('%s.mp4' % name, writer=writer)

	plt.show()
	option = int(input('Run again? (0) Yes, (1) No\n>> '))