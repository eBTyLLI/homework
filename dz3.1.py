n = int(input("Введите число от 1 до 100 "))
i = 1
if n > 100 or n < 1:
    print('Вы ввели неправильное число')
else:
    while i != n+1:
        print(i**2, ' ')
        i += 1