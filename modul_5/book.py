# Реализуйте класс Book с атрибутами title, author и price.
# Добавьте метод discount, который применяет скидку на книгу и изменяет её цену.
class Book:
    def __init__(self, title, autor, price):
        self.title = title
        self.author = autor
        self.price = price

    def discount(self, discount):
        print(f'Скидка - {discount}%')
        sum = self.price * discount // 100
        self.price -= sum
        return self.price

    def __str__(self):
        return (f'Название: "{self.title}"\n'
                f'Автор: {self.author}\n'
                f'Цена: {self.price}\n'
                f'{'*' * 30}\n')


book = Book('Морской волк', 'Джек Лондон', 250)
print(book)

book.discount(25)
print(book)
book1 = Book('80 дней вокруг света', 'Жюль Верн', 500)
print(book1)
book1.discount(10)
print(book1)