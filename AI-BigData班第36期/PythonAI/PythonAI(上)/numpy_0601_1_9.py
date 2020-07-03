import numpy as np
a=np.arange(7)
print(a)
b=a[2:6]
print(b)
c=a[2:6].copy()
print(np.may_share_memory(a,b))
print(np.may_share_memory(a,c))
b[0]=20
print(a)
print(c)