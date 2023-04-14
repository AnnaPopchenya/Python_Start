# Задача 10: На столе лежат n монеток.
# Некоторые из них лежат вверх решкой, а некоторые – гербом.
# Определите минимальное число монеток, которые нужно перевернуть,
# чтобы все монетки были повернуты вверх одной и той же стороной.
# Выведите минимальное количество монет, которые нужно перевернуть

n = int(input('Введите количество монеток: '))
zero = 0
one = 0
for i in range(n):
    x = int(input('Введите 0 или 1: '))
    if x == 0:
        zero += 1
    else:
        one += 1
if one > zero:
    print(zero)
else:
    print(one)
