# Задание: Декораторы в Python
#
# Цель задания:
# Освоить механизмы создания декораторов Python.
# Практически применить знания, создав функцию декоратор и обернув ею другую функцию.
#
# Задание:
# Напишите 2 функции:
# Функция, которая складывает 3 числа (sum_three)
# Функция декоратор (is_prime), которая распечатывает "Простое", если результат 1ой функции будет
# простым числом и "Составное" в противном случае.

# Пример:
# result = sum_three(2, 3, 6)
# print(result)
#
# Результат консоли:
# Простое
# 11
#
# Примечания:
# Не забудьте написать внутреннюю функцию wrapper в is_prime
# Функция is_prime должна возвращать wrapper
# @is_prime - декоратор для функции sum_three

import time


def is_prime(func):
    def wrapper(*args):
        time.sleep(1.0)
        res = func(*args)
        if res <= 1:
            return f'число {res} не определяется'
        for x in range(2, int(res ** 0.5) + 1):
            if res % x == 0:
                print(f'Составное')
                break
        else:
            print(f'Простое')
        return res

    return wrapper


@is_prime
def mul_three(*args):
    x = 1
    for num in args:
        x *= num
    return x


@is_prime
def sum_three(*args):
    x = 0
    for num in args:
        x += num
    return x


result = sum_three(2, 3, 6)
print(result)
result2 = sum_three(2, 3, 6, 13, -23)
print(result2)
result3 = sum_three(2, 3, 6, 22)
print(result3)
result4 = sum_three(2, 3, 6, 13, -24)
print(result4)
result5 = sum_three(2, 3, 6, 13, 198)
print(result5)
result6 = sum_three(2, 3, 6, -9)
print(result6)
result7 = mul_three(2, 2, 2)
print(result7)
result8 = mul_three(5, 5, 5)
print(result8)
