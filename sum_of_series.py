num = int(input('Веедите целое число: '))

series_ = list(range(1, num + 1))
sum = 0
for i in series_:
    sum += i

print('Сумма чисел от 1 до {num} равна {sum}'.format(num=num, sum=sum))