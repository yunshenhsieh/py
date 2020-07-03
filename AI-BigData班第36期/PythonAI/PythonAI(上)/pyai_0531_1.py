import numpy as np

a = np.array([1,2,3])
print(a)
print(a.ndim) # 查看維度
print(a.shape) #查看形狀
print(a.size) #查看大小
print(a.dtype) #查看資料型態

b=np.array([[1,2,3],[4,5,6]])
print(b)
print(b.ndim)
print(b.shape)
print(b.size)
print(b.dtype)

c=np.array([[[1,2],[3,4]],[[5,6],[7,8]]])
print(c)
print(c.ndim)
print(c.shape)
print(c.size)
print(c.dtype)

d=np.array([1,2,3,4])
print(d)
print(d.dtype)

d=np.array([1,2,3,4],np.int64)
print(d)
print(d.dtype)

d=np.array([1,2,3,4],dtype=float)
print(d)
print(d.dtype)

d=np.array([1,2,3,4],dtype=complex) # 目前沒用到過
print(d)
print(d.dtype)

e=np.array(d,dtype=float,copy=True)
print(e)
print(e.dtype)

dt = np.dtype('f2')
print(dt)

people = np.dtype([('name','S20'),('height','i4'),('weight','f2')])
a=np.array([('amy',156,50),('bob',175,72)],dtype=people)
print(a)
print(a['name'])