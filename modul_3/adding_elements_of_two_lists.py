# Задача 1: Сложение элементов двух списков
# Условие: Напишите функцию, которая принимает два списка чисел равной длины и возвращает список их попарных сумм.
# Используйте распаковку позиционных аргументов для передачи элементов списков в функцию сложения.

lst1 = [51, 2, 83, 46, 5]
lst2 = [5, 14, 32, 12, 1]

def summa_lists(list1, list2):
    lst_sum = []
    for x, y in zip(list1, list2):
        lst_sum.append(x + y)
    return lst_sum
sum_list = summa_lists(lst1, lst2)
print(sum_list)
print(*sum_list)