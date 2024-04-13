num = int(input('Введите число от 1 до 10 : '))

for i in range(1, 11):
    print('{num} x {i} = {res}'.format(num=num, i=i, res=num * i))
