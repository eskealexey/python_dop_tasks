num = int(input('Введите конечное число - '))

numbers_ = list(range(1, num + 1))
prime_ = []
k = 1
while k < num:
    divisor_ = 0
    c = 0
    while c < numbers_[k]:
        if numbers_[k] % (c + 1) == 0:
            divisor_ += 1
            if divisor_ > 2:
                break
        c += 1
    if divisor_ > 2:
        pass
    else:
        prime_.append(numbers_[k])
    k += 1

print(f'Простые числа в диапазоне от 0 до {num}:')
print(*prime_)
