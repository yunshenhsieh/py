import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import numpy as np
import  pandas as pd

x_raw = pd.period_range(pd.datetime.now(),periods=30, freq='d')
print(x_raw)
x = x_raw.to_timestamp().to_pydatetime()
print(x)
y1 = np.random.randint(50,80,30)
y2 = np.random.randint(20,45,30)

g = plt.gca()

for tick in g.xaxis.get_majorticklabels():  # example for xaxis
    tick.set_fontsize(6)

for tick in g.yaxis.get_majorticklabels():  # example for xaxis
    tick.set_fontsize(6)

g.xaxis.set_major_formatter(mdates.DateFormatter('%y-%m-%d'))
plt.gcf().autofmt_xdate()

plt.title('Random Trends')
plt.grid(True)

plt.plot(x,y1)
plt.plot(x,y2)

plt.show()