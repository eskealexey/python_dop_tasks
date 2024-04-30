# Создайте класс Car для автомобиля с атрибутами модели и года выпуска.
# Также нужен класс Garage, который хранит список автомобилей.
# Методы гаража должны позволять добавлять и удалять автомобили.

class Car:
    def __init__(self, model, year):
        self.model = model
        self.year = year

    def __str__(self):
        return f'{self.model} - {self.year}'

class Garage:
    def __init__(self,address, collection=[]):
        self.address = address
        self.collection = collection

    def add_auto(self, auto):
        print(f'Добавляем автомобиль {auto}')
        self.collection.append(auto)

    def del_auto(self, auto):
        print(f'Удаляем автомобиль {auto}')
        self.collection.remove(auto)
        pass

    def __str__(self):
        return f'В {self.address} находятся автомобили - {self.collection}'


garag1 = Garage('гараж1')
print(garag1)

kia = Car('Kia', 1998)
ford = Car('Ford', 2010)
print(kia)
print(ford)
garag1.add_auto(kia.model)
print(garag1)
garag1.add_auto(ford.model)
print(garag1)
garag1.del_auto(ford.model)

print(garag1)