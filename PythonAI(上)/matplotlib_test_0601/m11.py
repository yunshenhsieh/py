import matplotlib.pyplot as plt
from matplotlib import cm
import numpy as np

from mpl_toolkits.mplot3d.axes3d import get_test_data

# 設定視角
fig = plt.figure(figsize=plt.figaspect(0.3))

#第一個子圖
ax = fig.add_subplot(1, 2, 1, projection='3d')

X = np.arange(-6, 6, 0.25)
Y = np.arange(-5, 5, 0.25)
X, Y = np.meshgrid(X, Y)
R = np.sqrt(X**2 + Y**2)
Z = np.sin(R)

surf = ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=cm.rainbow,
                       linewidth=0, antialiased=False)

ax.set_zlim(-1.01, 1.01)

fig.colorbar(surf, shrink=0.5, aspect=10)

#第二個子圖
ax = fig.add_subplot(1, 2, 2, projection='3d')

X, Y, Z = get_test_data(0.1)

# ax.plot_wireframe(X, Y, Z, rstride=5, cstride=5)

surf = ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=cm.rainbow, linewidth=0, antialiased=False)

fig.colorbar(surf, shrink=0.5, aspect=10)

plt.show()

