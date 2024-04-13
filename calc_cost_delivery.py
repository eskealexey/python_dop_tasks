weight = int(input('Вес посылки - '))
cost = 0
if weight <= 2:
    cost = 50.0
elif 2 < weight < 10:
    cost = 50.0 + (weight - 2) * 20.0
else:
    cost = 200.0

print('Посылка весом ' + str(weight) + ' кг стоит ' + str(cost) + ' рублей')