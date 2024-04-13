def convert_c(c):
    forenget = c * 1.8 + 32
    return forenget

gs = u'\N{DEGREE SIGN}'
tem_c = float(input('Введите температуру по Цельсию - '))

tem_f = convert_c(tem_c)
print('{tem_c} {gs}C = {tem_f} {gs}F '.format(tem_c=tem_c, gs=gs, tem_f=tem_f))
