import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 1, 20)

y = np.sqrt(x) +  0.3 * np.random.rand(20)

f = np.poly1d([1, 0.2, 0.1]) #numpy.poly1d 自訂一個一元二次多項式 x^2 + 0 x + 0.1
print(f)

f2 = np.poly1d(np.polyfit(x, y, 2)) # numpy.polyfit 產生擬合的一元二次多項式係數
print(f2)

f3 = np.poly1d(np.polyfit(x, y, 3)) # numpy.polyfit 產生擬合的一元三次多項式係數
print(f3)

plt.scatter(x ,y , s=50, c=y, cmap ='cool', alpha=.6)  #畫漸層點

#plt.plot(x ,y ,'ro')  #畫紅點

plt.plot(x, f(x), color='b', label='f(x)' , linestyle='--')

plt.plot(x, f2(x) ,color='m', label='f2(x)' , linestyle='-.' )

plt.plot(x, f3(x) ,color='m', label='f3(x)' , linestyle=':' )

plt.legend(loc='best')

plt.show()