# Задача 2: Фибоначчи
# Условие: Создайте рекурсивную функцию, которая принимает число n и возвращает n-ое число Фибоначчи.
# Используйте условия для обработки базовых случаев (первое и второе числа последовательности).

def fibonacci_cikl(n):
    lst_ = [0, 1]
    i = 0
    while i < n :
        lst_.append(lst_[i - 1] + lst_[i -2])
        n -= 1
    return lst_[len(lst_) - 1]

def fibonacci_recurs(n, x = 0, y = 1):
    if n < 2:
        return x + y
    z = x + y
    x = y
    y = z
    return fibonacci_recurs(n - 1, x, y)

print(fibonacci_cikl(8))
print(fibonacci_recurs(8))
