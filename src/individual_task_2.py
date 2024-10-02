#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Задание 2.

# Составить программу с использованием классов и объектов для решения задачи. Во всех заданиях,
# помимо указанных в задании операций, обязательно должны быть реализованы следующие методы:
# * метод инициализации __init__ ;
# * ввод с клавиатуры read ;
# * вывод на экран display .

# В раздел программы, начинающийся после инструкции if __name__ = '__main__': добавить код,
# демонстрирующий возможности разработанного класса.

# Создать класс Time для работы со временем в формате «час:минута:секунда».
# Класс должен включать в себя не менее четырех функций инициализации: числами, строкой (например, «23:59:59»),
# секундами и временем. Обязатель ными операциями являются: вычисление разницы между двумя моментами времени в секундах,
# сложение времени и заданного количества секунд, вычитание из времени заданного количества секунд,
# сравнение моментов времени, перевод в секунды, перевод в минуты (с округлением до целой минуты).


class Time:
    def initialize(self, hours=0, minutes=0, seconds=0):
        # Проверкой корректности времени
        if not (0 <= hours < 24 and 0 <= minutes < 60 and 0 <= seconds < 60):
            raise ValueError(
                "Неверный формат времени: допустимые значения 0-23 для часов, 0-59 для минут и секунд."
            )
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    # Инициализация объекта из строки вида "HH:MM:SS"
    def initialize_from_string(self, time_str):
        try:
            hours, minutes, seconds = map(int, time_str.split(":"))
            self.initialize(hours, minutes, seconds)
        except ValueError:
            raise ValueError("Неверный формат строки, ожидается 'HH:MM:SS'.")

    # Инициализация объекта с помощью секунд
    def initialize_from_seconds(self, total_seconds):
        if total_seconds < 0:
            raise ValueError("Количество секунд не может быть отрицательным.")

        hours = (total_seconds // 3600) % 24
        minutes = (total_seconds // 60) % 60
        seconds = total_seconds % 60
        self.initialize(hours, minutes, seconds)

    # Перевод времени в количество секунд
    def to_seconds(self):
        return self.hours * 3600 + self.minutes * 60 + self.seconds

    # Перевод времени в минуты (с округлением)
    def to_minutes(self):
        return round(self.to_seconds() / 60)

    # Добавление секунд к текущему времени
    def add_seconds(self, seconds):
        total_seconds = self.to_seconds() + seconds
        total_seconds %= 86400
        self.initialize_from_seconds(total_seconds)

    # Вычитание секунд из текущего времени
    def subtract_seconds(self, seconds):
        total_seconds = (self.to_seconds() - seconds) % 86400
        if total_seconds < 0:
            total_seconds += 86400
        self.initialize_from_seconds(total_seconds)

    # Вычисление разницы между двумя моментами времени в секундах
    def time_difference(self, other_time):
        return abs(self.to_seconds() - other_time.to_seconds())

    # Сравнение двух моментов времени на равенство
    def is_equal(self, other_time):
        return self.to_seconds() == other_time.to_seconds()

    # Проверка, что текущее время раньше другого
    def is_earlier(self, other_time):
        return self.to_seconds() < other_time.to_seconds()

    # Ввод времени с клавиатуры
    def read(self):
        try:
            time_str = input("Введите время в формате HH:MM:SS: ")
            self.initialize_from_string(time_str)
        except ValueError as e:
            print(f"Ошибка ввода: {e}")

    # Вывод времени в формате HH:MM:SS
    def display(self):
        print(f"{self.hours:02}:{self.minutes:02}:{self.seconds:02}")


if __name__ == "__main__":
    # Инициализация с помощью чисел
    time1 = Time()
    time1.initialize(12, 30, 45)
    time1.display()

    # Инициализация с помощью строки
    time2 = Time()
    time2.initialize_from_string("15:45:30")
    time2.display()

    # Инициализация с помощью секунд
    time3 = Time()
    time3.initialize_from_seconds(55555)
    time3.display()

    # Сложение времени с заданным количеством секунд
    time1.add_seconds(3600)
    time1.display()

    # Вычитание времени
    time2.subtract_seconds(3700)
    time2.display()

    # Разница между двумя моментами времени
    difference = time1.time_difference(time2)
    print(f"Разница между time1 и time2 в секундах: {difference}")

    # Перевод в секунды и минуты
    print(f"Время time1 в секундах: {time1.to_seconds()}")
    print(f"Время time1 в минутах: {time1.to_minutes()}")

    # Сравнение двух моментов времени
    if time1.is_equal(time2):
        print("Моменты времени равны")
    elif time1.is_earlier(time2):
        print("time1 раньше, чем time2")
    else:
        print("time1 позже, чем time2")

    # Ввод времени с клавиатуры
    time1.read()
    time1.display()
