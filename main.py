n = int(input('Введите число: '))
d = 2
list = []

while d < n:
    flag = True
    for i in range(2, int(d ** 0.5) + 1):
        if d % i == 0:
            flag = False
            break
    if flag:
        list.append(d)
    d += 1

print(list)