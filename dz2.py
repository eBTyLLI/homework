#1
a = int(input())
b = int(input())
if a == 0 or b == 0:
    print("Нельзя делить на ноль!")
else:
    print(a/b, b/a)

#2
s = float(input())
if s > 20:
    print(round(s*0.65, 2), round(s*0.35, 2))
else:
    print(round(s,2), 0)

#3
a = int(input())
if 1 <= a <= 12:
    if a == 1:
        print("Январь. Зима")
    elif a == 2:
        print("Февраль. Зима")
    elif a == 3:
        print("Март. Весна")
    elif a == 4:
        print("Апрель. Весна")
    elif a == 5:
        print("Май. Весна")
    elif a == 6:
        print("Июнь. Лето")
    elif a == 7:
        print("Июль. Лето")
    elif a == 8:
        print("Август. Лето")
    elif a == 9:
        print("Сентябрь. Осень")
    elif a == 10:
        print("Октябрь. Осень")
    elif a == 11:
        print("Ноябрь. Осень")
    elif a == 12:
        print("Декабрь. Зима")
else:
    print('Нужно вводить целое число от 1 до 12')