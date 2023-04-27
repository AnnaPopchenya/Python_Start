# Задача 26:  Напишите программу, которая на вход принимает два числа A и B,
# и возводит число А в целую степень B с помощью рекурсии.
# *Пример:*
# A = 3; B = 5 -> 243 (3⁵)
#     A = 2; B = 3 -> 8 

a = int(input('Введите число: '))
b = int(input('Введите число: '))

def stepen(a, b):
    if b == 0:
        return 1
    if b < 0:
        return 1 / stepen(a, -b)
    if b % 2 == 0:
        return stepen(a, b // 2) * stepen(a, b // 2)
    else:
        return stepen(a, b - 1) * a
print(stepen(a, b))