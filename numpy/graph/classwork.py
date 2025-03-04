import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt

rng = np.random.default_rng(1)
data = rng.normal(size = 1000)

#plt.hist(data, bins = 30, denisty = True, alpha = 0.5, hisstype = 'step', edgecolor = 'red')
#plt.show()


x1 = rng.normal(0,0.0, 1000)
x2 = rng.normal(-2,1, 1000)
x3 = rng.normal(3,2, 1000)

args = dict(alpha = 0.5, bins = 40)

#plt.hist(x1, **args)
#plt.hist(x2, **args)
#plt.hist(x3, **args)

print(np.histogram(x1, bins =1))


mean = [0,0]
cov = [[1,1], [1,2]]
x,y = rng.multivariate_normal(mean, cov, 10000).T

#plt.hist2d(x, y, bins = 30)
#plt.hexbin(x,y, gridsize = 30)
#cb = plt.colorbar()






x = np.linspace(0,10,1000)

fig, ax = plt.subplots()

y = np.sin(x[:, np.newaxis] + np.pi* np.arange(0.2,0.5))
lines = plt.plot(x,y)

plt.legend(lines, ['1', '2', '3', '4'])
#ax.plot(x, np.sin(x), label = 'Синус')
#ax.plot(x, np.cos(x), label = 'косинус')

#ax.axis('equal')

#ax.legend(
 #   frameon = True,
  #  fancybox = True,
   # shadow = True
#)


fig, ax = plt.subplots()
lines = []
styles = ['-', '--', '-.', ':']
x = np.linspace(0,10,1000)
for i in range(4):
    lines += ax.plot(x, np.sin(x-i+np.pi/2)),styles[i]

ax.axis('equal')

ax.legend(lines[:2], ['l 1', 'l2'], loc = 'upper right')

leg = mpl.legend.Legend(ax, lines[1:], ['line 2', 'line 3', 'line 4'])

ax.add_artist(leg)


fig, axis = plt.subplots(2,3, sharex = 'col')

for i in range(2):
    for j in range(3):
        ax[i,j].text(0.5, 0.5, str((i,j)), fontsize = 16, ha = 'center')



grid = plt.GridSpec(2,3)

plt.subplot(grid[0,0])
plt.subplot(grid[0,1:])
plt.subplot(grid[1,:2])
plt.subplot(grid[1,2])


mean = [0, 0]
cov = [[1,1], [1,2]]

rng = np.random.default_rng(1)
x,y = rng.multivariate_normal(mean, cov, 3000).T

grid = plt.GridSpec(4,4,hspace=0.2, wspace = 0.2)

main_ax = fig.add_subplot(grid[:-1,1:])

main_ax.plot(x, y, 'ok', markersize = 3)


plt.show()
