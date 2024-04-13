import random


# создание игрового поля
def create_area(n):
    pole = [[0] * n for i in range(n)]
    for i in range(n):
        for j in range(n):
            pole[i][j] = '*'
    return pole


# вывод игрового поля на экран
def view_area(lst_, n):
    num_ = [n for n in range(n)]
    print(' ', *num_)
    lenth = len(lst_)
    for x in range(0, lenth):
        print(x, *lst_[x])
    print('=' * 30)


# рандомные координаты спрятаного ящика
def random_box(n, num_):
    list_random = []
    for i in range(n):
        list_random.append(i)
        r = random.randrange(0, num_)
        c = random.randrange(0, num_)
        list_random[i] = [r, c]
    return list_random


# проверка ввода числа
def enter_num(s, n=10):
    while True:
        try:
            num_ = int(input(f'Введите номер {s} от 0 до {n - 1}: '))
        except ValueError:
            print('Неверный ввод, будьте внимательней')
            continue
        if (num_ >= 0) and (num_ <= n):
            return num_
        else:
            print('Ввод неверный, введите снова')


# проверка хода
def check_progress(row_, col_, lst):
    for i in lst:
        r, c = i[0], i[1]
        if (row_ == r) and (col_ == c):
            return 1
        if (row_ == r) or (col_ == c):
            return 2
    pass


# ++++++++++++++++++ Первоначальная инициализация игры ++++++++++++++++++++++ #
num = 10  # размер поля (10 на 10 ячеек)
list_area = create_area(num)  # инициализируем игровое поле
view_area(list_area, num)  # вывод поля на экран
list_box = random_box(1, num)  # случайные координаты ящика
# char_1 = u'\u2B24'
char_1 = 'X'
# char_2 = u'\u00B6'
char_2 = 'O'
# char_3 = u'\u4DC0'
char_3 = 'П'
win = 0
count = 1 # счетчик ходов
# ------------------- игровой цикл ------------------------------------
while True:

    print(f'Шаг № {count}')
    row = enter_num('строки', num)
    col = enter_num('столбца', num)

    if list_area[row][col] != '*':
        print('Такой шаг уже был')
        print('повторите ход')
        continue

    win = check_progress(row, col, list_box)
    if win == 1:
        list_area[row][col] = char_3
        view_area(list_area, num)  # вывод поля на экран
        break
    elif win == 2:
        list_area[row][col] = char_2
    else:
        list_area[row][col] = char_1

    view_area(list_area, num)  # вывод поля на экран
    count += 1
print(f'Сундук был найден на шаге № {count}')