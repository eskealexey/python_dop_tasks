# Создайте класс Customer с информацией о клиенте и класс ShoppingCart с списком товаров.
# Включите методы в корзину для добавления и удаления товаров,
# а также для расчета общей стоимости покупки.

class Customer:
    def __init__(self, name):
        self.name = name

class ShoppingCart(Customer):
    total_cost = 0
    def __init__(self,name, product={}):
        super().__init__(name)
        name =  name
        self.product = product

    def add_product(self, name, cost):
        print(f'Добавлен продукт - {name}')
        self.product[name] = cost
        self.counting(cost)

    def del_product(self,name):
        print(f'убран продукт - {name}')
        self.counting(-self.product[name])
        self.product.pop(name)


    def counting(self, cost):
        self.total_cost = self.total_cost + cost
        return self.total_cost


    def view(self):
        return f'В корзине находятся {self.product} общей стоимостью {self.total_cost} р'


alex = ShoppingCart(Customer('Alexey'))
alex.add_product('bred', 35)
print(alex.view())
alex.add_product('milk', 65)
print(alex.view())
alex.add_product('ananas', 150)
print(alex.view())
alex.del_product('ananas')
print(alex.view())