import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d
import numpy as np

fig = plt.figure()
ax = plt.axes(projection='3d')

print()

class Cube:
	def __init__(self,x,y,z,posx,posy,posz,density):
		self.x = x
		self.y = y
		self.z = z
		self.posx = posx
		self.posy = posy
		self.posz = posz
		self.density = density
	def draw(self):
		l = np.linspace(0, self.x, self.density)
		ax.scatter(l+self.posx, self.posy, self.posz, color = 'r')
		ax.scatter(l+self.posx, self.posy + self.y, self.posz, color = 'r')
		ax.scatter(l+self.posx, self.posy, self.posz + self.z, color = 'r')
		ax.scatter(l+self.posx, self.posy + self.y, self.posz + self.z, color = 'r')
		l = np.linspace(0, self.y, self.density)
		ax.scatter(self.posx, l+self.posy, self.posz, color = 'g')
		ax.scatter(self.posx + self.x, l+self.posy, self.posz, color = 'g')
		ax.scatter(self.posx, l+self.posy, self.posz + self.z, color = 'g')
		ax.scatter(self.posx + self.x, l+self.posy, self.posz + self.z, color = 'g')
		l = np.linspace(0, self.z, self.density)
		ax.scatter(self.posx, self.posy, self.posz + l, color = 'b')
		ax.scatter(self.posx + self.x, self.posy, self.posz + l, color = 'b')
		ax.scatter(self.posx, self.posy + self.y, self.posz + l, color = 'b')
		ax.scatter(self.posx + self.x, self.posy + self.y, self.posz + l, color = 'b')

a = Cube(20, 20, 20, 0, 0, 0, 10)
a.draw()

b = Cube(10, 10, 10, 25, 5, 21, 10)
b.draw()

c = Cube(20, 20, 5, 0, 50, 32, 10)
c.draw()

ax.set_xlabel('X Axes')
ax.set_ylabel('Y Axes')
ax.set_zlabel('Z Axes')

plt.show()