year = int(input('Введите год: '))
if year % 4 != 0:
    print('Год ' + str(year) + ' НЕвисокосный')
else:
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        print('Год ' + str(year) + ' Високосный')
    else:
        print('Год ' + str(year) + ' НЕвисокосный')