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
