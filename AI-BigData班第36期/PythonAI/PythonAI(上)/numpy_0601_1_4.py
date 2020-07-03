import numpy as np

a=np.arange(6)
print(a)

print(a[2])
print(a[3:5])
print(a[2:-1])
print(a[::1])
print(a[::-1])
print(a[::2])
print(a[::-2])

a[2]=0
print(a)
a[3:5]=0
print(a)
print(a[3:5])
print(a[1:])