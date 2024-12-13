#5
n = int(input())
m = int(input())
arr = list()

for i in range(n):
    brr = list()
    for j in range(m):
        brr.append(int(input()))
    arr.append(brr)

for i in range(n):
  for j in range(n):
    print(arr[i][j], end = ' ')
  print()

s = 0
s_max = 0
s_min = 0
i_max = 0
i_min = 0
for j in range(m):
    s_min += arr[0][j]

for i in range(n):
    for j in range(m):
        s += arr[i][j]
    if s > s_max:
        s_max = s
        i_max = i
    s = 0

for i in range(n):
    for j in range(m):
        s += arr[i][j]
    if s < s_min:
        s_min = s
        i_min = i
    s = 0
print()
print('Максимальная строчка: ')
for j in range(m):
    print(arr[i_max][j], end = ' ')
print()
print('Максимальная сумма: ',s_max)
print()
print('Минимальная строчка: ')
for j in range(m):
    print(arr[i_min][j], end = ' ')
print()
print('Минимальная сумма: ', s_min)


#6
from random import *
m = int(input())
n = int(input())
print()
arr = list()
for i in range(m):
  brr = list()
  for i in range(n):
    brr.append(randint(1, n))
  arr.append(brr)
for i in range(n):
  for j in range(n):
    print(arr[i][j], end = ' ')
  print()
for i in range(m):
    for j in range (len(arr)):
        if arr[i][j] % 2 == 0:
            arr[i][j] = 0
        else: arr[i][j] = 1
print()
for i in range(m):
  for j in range(n):
    print(arr[i][j], end = ' ')
  print()