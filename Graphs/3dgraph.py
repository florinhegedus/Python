import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d

fig = plt.figure()
ax = plt.axes(projection='3d')

x = [1,2,3,4,5,6,7,8,9]
y = [1,2,3,4,5,6,7,8,9]
z = [1,2,3,4,5,6,7,8,9]

ax.scatter(x,y,z,color='r')
ax.set_xlabel('X Axes')
ax.set_ylabel('Y Axes')
ax.set_zlabel('Z Axes')

plt.show()