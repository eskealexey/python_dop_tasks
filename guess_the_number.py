import random

number = random.randint(0, 100)
flag = True
step = 0
while flag:
    step += 1
    num = int(input('Ваше число - '))
    if num  == number:
        print('Вы угадали, это число - ' + str(number) + ' за ' + str(step) + ' ходов' )
        flag = False
    if num < number :
        print('Должно быть больше')
    if num > number :
        print('Должно быть меньше')

