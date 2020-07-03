import matplotlib.pyplot as plt
import numpy as np

labels = ['Q1','Q2','Q3','Q4']
sizes = [20,30,40,10]
explode = (0, 0.1, 0, 0)

plt.axis('equal') #圓形

cmap = plt.cm.viridis
colors = cmap(np.linspace(0., 1., len(labels)))

wedges, texts, autotexts = plt.pie(sizes, colors=colors, explode=explode, labels=labels, autopct='%1.2f%%', shadow=False, startangle=90)

plt.setp(autotexts, size=14, weight="bold", color='red' ) #數值
plt.setp(texts, size=18, weight="bold" )  #標籤

plt.title('Pie Chart', weight="bold")

plt.show()
