from matplotlib.pylab import *
import numpy as np
X = []
t = []
dt = 1
X.append(0.)
t.append(0)
V=40
end_time = 100
for i in range(int(end_time / dt)):
    tmp = X[i] + V * dt
    X.append(tmp)
    t.append(dt * (i+1))
    print t[-1],X[-1]
x = t
y = X
plt.plot(x, y)
plt.xlabel('time/s')
plt.ylabel('distance/m')
plt.title('SPEED/(m/s)')
plt.legend()
plt.show()
