import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 25*np.pi, 100)
y = np.sin(x)

plt.ion()
fig = plt.figure()
ax = fig.add_subplot(111)
line1, = ax.plot(x, y, 'g-')
line2, = ax.plot(x, y, 'r-')
line3, = ax.plot(x, y, 'r-')
line4, = ax.plot(x, y, 'g-')
line5, = ax.plot(x, y, 'y-')
line6, = ax.plot(x, y, 'm-')
line7, = ax.plot(x, y, 'm-')
line8, = ax.plot(x, y, 'y-')

for phase in np.linspace(0, 10*np.pi, 500):
	line1.set_ydata(np.sin(0.1*x + phase))
	line2.set_ydata(np.sin(-0.1*x - phase))
	line3.set_ydata(0.5*np.sin(0.1*x + phase))
	line4.set_ydata(0.5*np.sin(-0.1*x - phase))
	line5.set_ydata(0.25*np.sin(0.1*x + phase))
	line6.set_ydata(0.25*np.sin(-0.1*x - phase))
	line7.set_ydata(0.75*np.sin(0.1*x + phase))
	line8.set_ydata(0.75*np.sin(-0.1*x - phase))
	fig.canvas.draw()