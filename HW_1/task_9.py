# Задача 18: Требуется найти в массиве A самый близкий по величине элемент к заданному числу X.
# Если таких элементов несколько, вы вывести один любой.
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих  строках записаны N целых чисел Ai (можно использовать псевдогенерацию).
# Последняя строка содержит число X
# *Пример:*

# 5
#     7 -2 3 5 1
#     6
#     -> 7

import random
N = int(input('Введите количество элементов в массиве N: '))
x = int(input('Введите число, к которому надо найти самый близкий по величине элемент: '))
list = [random.randint(-5, 5) for i in range(N)]
print(list)

num = list[0]
for i in list:
    if abs(i - x) < abs(num - x):
        num = i
print(f'Самый близкий  по величине элемент  к {x} -> {num}')