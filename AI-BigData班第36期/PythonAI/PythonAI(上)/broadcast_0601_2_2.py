import numpy as np
a = np.arange(6).reshape(2,3)
print(a)
print('')
print(a+5)
print('')
b=np.ones(6,dtype=int).reshape(2,3)
print(b)
print(a+ 2*b)