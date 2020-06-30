import matplotlib.pyplot as plt
import numpy as np

X = np.arange(20)
Y = np.random.uniform(0.5,1.0, 20)

for x, y in zip(X, Y):
    # ha: horizontal alignment
    # va: vertical alignment
    plt.text(x , y , '%.2f' % y, ha='center', va='bottom', fontsize=6)

plt.bar(X,Y,facecolor='#9999ff', edgecolor='black')

plt.show()
