# Разработайте класс Television с атрибутами для текущего канала и уровня громкости.
# Включите методы для смены канала, изменения громкости и вывода текущего состояния телевизора.

class Television:
    def __init__(self, canal, volume=25):
        self.canal = canal
        self.volume = volume

    def __str__(self):
        if self.volume < 0:
            self.volume = 0
        return f'Канал: {self.canal}, громкость - {self.volume} %'

    def canal_change(self, new_canal):
        print(f'Меняем канал на {new_canal}')
        self.canal = new_canal
        return self.canal

    def volume_change(self, volume_new):
        if volume_new > 0:
            print(f'Увеличиваем громкость на {volume_new}%')
        elif volume_new < 0:
            print(f'Уменьшаем громкость на {abs(volume_new)}%')
        self.volume = self.volume + volume_new
        return self.volume


tele = Television('NTV')
print(tele)
tele.volume_change(25)
print(tele)
tele.volume_change(-35)
print(tele)
tele.canal_change('RTR')
tele.volume_change(-35)
print(tele)
