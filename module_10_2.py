            # Домашнее задание по теме "Потоки на классах"


from time import sleep
from threading import Thread, Lock


class Knight(Thread):
    total_enemies = 100
    lock = Lock()

    def __init__(self, name, power):
        super().__init__()
        self.name = name
        self.power = power
        self.days = 0

    def run(self):
        print(f'{self.name}, на нас напали!')
        while True:
            sleep(1)
            with Knight.lock:
                if Knight.total_enemies <= 0:
                    break
                Knight.total_enemies -= self.power
                Knight.total_enemies = max(Knight.total_enemies, 0)
                self.days += 1


            day_word = "день" if self.days == 1 else "дня"
            print(f'{self.name} сражается {self.days} {day_word}, осталось {Knight.total_enemies} воинов.')


        day_word = "день" if self.days == 1 else "дня"
        print(f'{self.name} одержал победу спустя {self.days} {day_word}!')


first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight('Sir Galahad', 20)

first_knight.start()
second_knight.start()

first_knight.join()
second_knight.join()

print('Все битвы закончились!')






