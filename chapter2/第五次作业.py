from matplotlib.pylab import *
import numpy as np
V = []
t = []
dt = 1
V.append(0.)
t.append(0)
g=9.8
end_time = 100
for i in range(int(end_time / dt)):
    tmp = V[i] - g * dt
    V.append(tmp)
    t.append(dt * (i+1))
    print t[-1],V[-1]
x = t
y = V
plt.plot(x, y)
plt.xlabel('time/s')
plt.ylabel('velocity/(m/s)')
plt.title('SPEED/(m/s)')
plt.legend()
plt.show()
