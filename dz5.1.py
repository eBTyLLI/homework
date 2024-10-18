# Три точки заданы своими координатами X(x1, x2), Y(y1, y2) и Z(z1, z2). 
# Найти и напечатать координаты точки, для которой угол между осью абсцисс и лучом, соединяющим начало координат с точкой, минимальный. 
# Вычисления оформить в виде процедуры.

import numpy as np
import math 

def min_corner(x, y, z):
    xc = np.acos(abs(x[0])/math.sqrt(x[0]**2+x[1]**2))
    yc = np.acos(abs(y[0])/math.sqrt(y[0]**2+y[1]**2))
    zc = np.acos(abs(z[0])/math.sqrt(z[0]**2+z[1]**2))
    if xc < yc and xc < zc:
        print(x)
    elif yc < xc and yc < zc:
        print(y)
    elif zc < xc and zc < yc:
        print(z)
    else: 'Какие-то из углов равны ツ'

x = list()
y = list()
z = list()
d = list()
d.append(x)
d.append(y)
d.append(z)

for i in range (1, 4):
  print('Введите координаты ', i, '-ой точки: ')
  cord1 = int(input('x: '))
  cord2 = int(input('y: '))
  d[i-1].append(cord1)
  d[i-1].append(cord2)

min_corner(x, y, z)