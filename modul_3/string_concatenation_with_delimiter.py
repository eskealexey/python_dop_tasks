# Задача 2: Конкатенация строк с разделителем
# Условие: Создайте функцию, которая принимает произвольное количество строк и строку-разделитель,
# конкатенирует все строки, вставляя между ними разделитель, и возвращает результат. Убедитесь,
# что разделитель не добавляется после последней строки.


def get_string():
    stroka = input('Введите строку (для окончания ввода введите "stop"): ')
    return stroka


def konkaten(list_, split):
    length = len(list_)
    str_ = ''
    for i in range(length):
        if i != length - 1:
            str_ = str_ + list_[i] + split
        else:
            str_ = str_ + list_[i]
    return str_


list_string = []
flag = True


while flag:
    str_ = get_string()
    if str_.lower() == 'stop'.lower():
        flag = False
    else:
        list_string.append(str_)


split_ = input('Введите строку разделитель: ')

print(konkaten(list_string, split_))
