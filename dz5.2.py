#Найти все простые натуральные числа, не превосходящие n, двоичная запись которых представляет собой палиндром, 
# т. е. читается одинаково слева направо и справа налево.

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

prime = simple_num(int(input('Введите число n: ')))

num_plndrm = list()

for i in range(len(prime)):
    n = prime[i]
    if is_palindrom(n) == True:
        num_plndrm.append(n)


print('ОШИБКА В РЕШЕНИИ')
print('Простые числа палиндромы меньше n: ', num_plndrm)