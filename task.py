# task 1. Сформировать список из N членов последовательности. Для N = 5: 1, -3, 9, -27, 81 и т.д.
number = int(input("Введите число: "))
lst = [(-3)**i for i in range(number)]
print(f"Итоговая последовательность после применения числа: {lst}")

# task 2. Для натурального n создать словарь индекс-значение, состоящий из элементов последовательности 3n + 1. 
# Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}

number = int(input("Введите число: "))
d = {n : 3*n + 1 for n in range(1,number+1)}
print(f"Итоговая последовательность: {d}")

# task 3. Пользователь задаёт две строки. Определить количество вхождений одной строки в другой.

str1 = input("Введите первую строку для проверки:")
str2 = input("Введите вторую строку для поиска в первой строке:")

count = 0
k = 1
for i in range(0,len(str1) - len(str2),k):
    if str2 in str1[i:i+len(str2)]:
        count += 1
        k = len(str2)
    else:
        k = 1
print(f"Вторая строка входит в первую {count} раз(а).")

# task 4. Подсчитать сумму цифр в вещественном числе.

from random import uniform

n = float(input("Введите вещественное число: "))

def sum_digit(n):
    return sum(map(int, list(str(n).replace('.',''))))

print(n)
print(f"сумма цифр вещественного числа равна {sum_digit(n)}")

# task 5. Написать программу получающую набор произведений чисел от 1 до N. 
# Пример: пусть N = 4, тогда [ 1, 2, 6, 24 ]

from itertools import accumulate
import operator

N = int(input('Введите число: '))


def get_prods(N):
    return list(accumulate([x for x in range(1, N + 1)], operator.mul))

print(f"Набор произведений введенного числа:{get_prods(N)}")