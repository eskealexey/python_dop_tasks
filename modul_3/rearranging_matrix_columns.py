# Задача 2: Перестановка столбцов матрицы
# Условие: Дана матрица (список списков). Напишите функцию, которая меняет местами первый и последний столбцы матрицы.
# Используйте распаковку позиционных аргументов для передачи строк матрицы во внутреннюю функцию, которая осуществляет
# перестановку элементов.
matrics = [[1, 2, 3, 4], [5, 6, 7, 8], ['a', 'b', 'c', 'd'], ['e', 'f', 'g', 'h']]
print('Первоначальная матрица:')
for matric in matrics:
    print(*matric)

def revers_(lst):
    for row in lst:
        length = len(row)
        a = row[0]
        b = row[length - 1]
        row[0] = b
        row[length - 1] = a
    return lst

list_new = revers_(matrics)
print()
print('Матрица обработанная функцией:')
for matric in list_new:
    print(*matric)

