for y in range(1,10):
    for x in range(2,10):
        print('{:<2}{:<2}{:<2}{:}{:<2}  '.format( x ,'×', y ,'= ', x*y ), end='')
    else:
        print('')


print('')
for y in range(1,10):
    for x in range(2,6):
        print('{:<2}{:<2}{:<2}{:}{:<2}  '.format( x ,'×', y ,'= ', x*y ), end='')
    else:
        print('')

print('')

for y in range(1, 10):
    for x in range(6,10):
        print('{:<2}{:<2}{:<2}{:}{:<2}  '.format( x ,'×', y ,'= ', x*y ), end='')
    else:
        print('')

print('')

#3
for y in range(1,19):

    for x in range(2,6):
        if y < 10:
            print('{:<2}{:<2}{:<2}{:}{:<2}  '.format( x ,'×', y ,'= ', x*y ), end='')
        else:
            x1 = x + 4
            y1 = y - 9
            print('{:<2}{:<2}{:<2}{:}{:<2}  '.format(x1, '×', y1, '= ', x1 * y1), end='')
    else:
        print('')
