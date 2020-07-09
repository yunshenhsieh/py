a=[['a','b','c'],['d','e','f']]
b=['a','b','c']
c=['d','e','f']

def transpose(*matrix):
    return zip(*matrix)
li=transpose(a)
li2=transpose(b,c)
for item in li:
    print(item)
for item in li2:
    print(item)