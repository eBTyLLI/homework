#1
import math

r = int(input("Введите радиус в сантиметрах: "))
print(round(2*math.pi*r,2))
print(round(math.pi*r**2,2))

#2
x, y = 10, 55
print(f"ДО x, y = {x}, {y}")
x, y = y, x
print(f"ПОСЛЕ x, y = {x}, {y}")

#3
import math

L = int(input("Введите длину маятника: "))
print(str(round(2*math.pi*math.sqrt(L/9.81), 2)))