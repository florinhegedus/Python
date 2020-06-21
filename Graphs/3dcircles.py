import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d
import numpy as np

fig = plt.figure()
ax = plt.axes(projection='3d')

print()

#x = np.linspace(min, max, no_of_point)
for t in range(0, 20, 5):
	z = np.linspace(0 ,10, 100)
	x = np.sin(z)
	y = np.cos(z) * np.cos(t)
	z = np.sin(t) * np.cos(z)
	ax.scatter(x,y,z,color='r')

x1 = np.linspace(0, 10, 100)
z1 = np.sin(x1)
y1 = np.cos(x1)

y2 = np.linspace(0, 10, 100)
z2 = np.sin(y2)
x2 = np.cos(y2)


ax.scatter(0,y1,z1,color='b')
ax.scatter(x2,0,z2,color='g')
ax.set_xlabel('X Axes')
ax.set_ylabel('Y Axes')
ax.set_zlabel('Z Axes')

plt.show()