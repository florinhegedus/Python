import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d
import numpy as np

fig = plt.figure()
ax = plt.axes(projection='3d')

print()

#x = np.linspace(min, max, no_of_point)
z = np.linspace(0, 10, 100)
x = np.sin(z)*1.1
y = np.cos(z)*1.1

z1 = np.linspace(0, 10, 100)
x1 = np.sin(z1)
y1 = np.cos(z1)

z2 = np.linspace(0, 10, 100)
x2 = np.sin(z2)*0.9
y2 = np.cos(z2)*0.9

ax.scatter(x,y,z,color='r')
ax.scatter(x1,y1,z1,color='b')
ax.scatter(x2,y2,z2,color='g')
ax.set_xlabel('X Axes')
ax.set_ylabel('Y Axes')
ax.set_zlabel('Z Axes')

plt.show()