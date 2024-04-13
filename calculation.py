def calc_imt(weight, height):
    imt = round(weight/height ** 2, 2)
    print('Индекс массы тела (ИМТ) равен {imt}'.format(imt=imt))


weight = float(input('Введите вес в килограммах - '))
height = float(input('Введите рост в метрах - '))

calc_imt(weight, height)