# Создайте класс BankAccount, который позволяет создавать объекты с атрибутами для хранения баланса пользователя.
# В классе должны быть методы для депозита (вклада) денег, снятия денег и вывода текущего баланса.
class BankAccount:
    def __init__(self, name, balans):
        self.__name = name
        self.__balans = balans

    def debit(self, deb):
        self.__balans += deb
        print(f'Внесено {deb} рублей')
        return self.__balans


    def kredit(self, cred):
        print(f'Снимаем {cred} рублей')
        if self.__balans < cred:
            print('Столько денег нельзя снять')
        else:
            self.__balans -= cred
            print(f'Снято {cred} рублей')
        return self.__balans


    def __str__(self):
        return f'На балансе {self.__balans} рублей'


cashe = BankAccount('Сберегательный', 10000)

print(cashe)
cashe.debit(5000)
print(cashe)
cashe.kredit(12000)
print(cashe)
