# Определите класс Animal с атрибутами для вида и имени. Создайте метод, который выводит звуки,
# которые издает животное (например, "ррр" для кошки).

class Animal:
    def __init__(self, vid, name, soud=''):
        self.vid = vid
        self.name = name
        self.sound = soud

    def animal_sound(self, sound):
        return (f'{self.vid} {self.name} говорит {sound}')


cat = Animal('кот', 'Васька')
print(cat.animal_sound('Мяу-мяу'))


dog = Animal('собака', 'Жучка')
print(dog.animal_sound('Гав-гав'))
