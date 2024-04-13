# Вывод игрового поля на экран
def view_area(p):
    for pole in p:
        print(*pole)

# проверка ввода числа
def inter_num(s):
    while True:
        try:
            num = int(input(f'Введите номер {s} (1, 2, 3): ')) -1
        except ValueError:
            print('Неверный ввод, будьте внимательней')
            continue
        if num >= 0 and num <= 2:
            return num
        else:
            print('Ввод неверный, введите снова')


# проверка по столбцам
def check_col(list_, x):
    list_h = []
    for i in range(3):
        list_h.append(list_[i][x])
    return list_h


# проверка по диагонали (сверху вниз)
def check_d1(list_):
    c = 2
    r = 2
    list_help = []
    while c >= 0 and r >= 0:
        list_help.append(list_[c][r])
        c -= 1
        r -= 1
    return list_help


# проверка по диагонали (снизу вверх)
def check_d2(list_):
    c = 0
    r = 2
    list_help = []
    while c <= 2 and r >= 0:
        list_help.append(list_[c][r])
        c += 1
        r -= 1
    return list_help


# Проверка победителя
def winner_verification():
    if area[0][0:3] == ['X', 'X', 'X'] or area[1][0:3] == ['X', 'X', 'X'] or area[2][0:3] == ['X', 'X', 'X']:
        return 'X'
    if check_col(area, 0) == ['X', 'X', 'X'] or check_col(area, 1) == ['X', 'X',
                                                                       'X'] or check_col(area, 2) == ['X', 'X', 'X']:
        return 'X'
    if check_d1(area) == ['X', 'X', 'X'] or check_d2(area) == ['X', 'X', 'X']:
        return 'X'

    if area[0][0:3] == ['0', '0', '0'] or area[1][0:3] == ['0', '0', '0'] or area[2][0:3] == ['0', '0', '0']:
        return '0'
    if check_col(area, 0) == ['0', '0', '0'] or check_col(area, 1) == ['0', '0',
                                                                       '0'] or check_col(area, 2) == ['0', '0', '0']:
        return '0'
    if check_d1(area) == ['0', '0', '0'] or check_d2(area) == ['0', '0', '0']:
        return '0'


# Подготовка игрового поя
area = [['*', '*', '*'], ['*', '*', '*'], ['*', '*', '*']]
print('-' * 35)
view_area(area)
n = 0

while n < 9:
    if n % 2 == 0:
        print(f'Ход {n + 1}, ходит Крестик')
        char = ('X')
    else:
        print(f'Ход {n + 1}, ходит Нолик')
        char = '0'
    row = inter_num('строки')
    column = inter_num('столбца')

    if area[row][column] == '*':
        area[row][column] = char
    else:
        print('Поле уже ЗАНЯТО!!!')
        print('Повторите ход')
        continue

    view_area(area)
    print('*' * 35)

    win = winner_verification()
    if win == 'X':
        print('Победа Крестиков')
        break
    if win == '0':
        print('Победа Ноликов')
        break
    n += 1

if win != 'X' and win != '0':
    print('Ничья')
