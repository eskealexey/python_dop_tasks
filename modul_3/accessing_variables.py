# Задача 1: Доступ к встроенным и глобальным переменным
# Условие: Создайте функцию, которая без передачи ей каких-либо аргументов возвращает сумму двух чисел:
# одно число определено в глобальном пространстве имен, а другое - это встроенная константа.
# Используйте global для доступа к глобальной переменной и builtins для доступа к встроенной константе.

x = 13

def summ_():
    global x
    y = 15
    return x + y

print(summ_())


# Задача 2: Перекрытие имен функций
# Условие: Создайте две функции с одинаковыми именами в разных пространствах имен
# (одна в глобальном пространстве имен, а другая в локальном пространстве имен функции).
# Обе функции должны возвращать разные значения. Продемонстрируйте, как можно вызвать каждую из них,
# чтобы получить их разные возвращаемые значения.
def test():
    print(1 + 102)

def test2():
    def test():
        print(120 *2)

    test()
test()
test2()


