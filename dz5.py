#1
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


#2

def simple_num(n):
    prime = list()
    for i in range(2, n+1):
        for j in prime:
            if i % j == 0:
                break
        else:
            prime.append(i)

    return prime

def is_palindrom(nu):
    st = str(nu) 
    rev = reversed(st) 
    if list(st) == list(rev):
        return True

def binar(prime):
    for i in range(len(prime)):
        k = int(prime[i])
        prime.append(bin(k)[2:])
        prime.remove(prime[i])

prime = simple_num(int(input('Введите число n: ')))

num_plndrm = list()

binar(prime)

for i in range(len(prime)):
    n = prime[i]
    if is_palindrom(n) == True:
        num_plndrm.append(n)


print('Простые числа палиндромы меньше n: ', num_plndrm)