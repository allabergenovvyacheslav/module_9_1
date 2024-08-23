""" Форенгейт -> Цельсий
"""
def convert_to_celsius(temp):
    result = (5 / 9) * (temp - 32)
    return result


z = convert_to_celsius(85)
print(z)

""" Фибоначи
"""
def fibonacci(n):
    a = 0
    b = 1
    for _ in range(n):
        yield a
        a = b
        b = a + b


x = fibonacci(n=10)
for elem in x:
    print(elem)


"""Фибоначи_2
"""
def fibonacci_2():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


for elem in fibonacci_2():
    print(elem)
    if elem > 10 ** 5:
        break
