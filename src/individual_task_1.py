#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Задание 1.

# Парой называется класс с двумя полями, которые обычно имеют имена first и second.
# Требуется реализовать тип данных с помощью такого класса. Во всех заданиях
# обязательно должны присутствовать:
#  * метод инициализации __init__ ;метод должен контролировать значения аргументов на корректность;
#  * ввод с клавиатуры read ;
#  * вывод на экран display .

# Реализовать внешнюю функцию с именем make_тип() , где тип — тип реализуемой структуры.
# Функция должна получать в качестве аргументов значения для полей структуры и
# возвращать структуру требуемого типа. При передаче ошибочных параметров следует выводить сообщение и
# заканчивать работу.

# Номер варианта необходимо уточнить у преподавателя. В раздел программы, начинающийся после
# инструкции if __name__ = '__main__': добавить код, демонстрирующий возможности разработанного класса.

# Поле first — целое число, левая граница диапазона, включается в диапазон; поле second — целое число,
# правая граница диапазона, не включается в диапазон. Пара чисел представляет полуоткрытый
# интервал [first, second). Реализовать метод rangecheck() — проверку заданного целого числа на
# принадлежность диапазону.


class Pair:
    def __init__(self, first: int, second: int):
        # Проверка на корректность диапазона
        if not (isinstance(first, int) and isinstance(second, int)):
            raise ValueError("Оба значения должны быть целыми числами.")
        if first >= second:
            raise ValueError("Значение first должно быть меньше значения second.")

        self.first = first
        self.second = second

    # Ввод данных с клавиатуры
    def read(self):
        try:
            self.first = int(input("Введите значение для first (целое число): "))
            self.second = int(input("Введите значение для second (целое число): "))
            if self.first >= self.second:
                raise ValueError("Значение first должно быть меньше значения second.")
        except ValueError as e:
            print(f"Ошибка ввода: {e}")
            return False
        return True

    # Вывод
    def display(self):
        print(f"Пара чисел: [{self.first}, {self.second})")

    # Проверка, принадлежит ли число заданному интервалу
    def rangecheck(self, number: int):
        return self.first <= number < self.second


# Внешняя функция для создания объекта типа Pair
def make_Pair(first: int, second: int):
    try:
        return Pair(first, second)
    except ValueError as e:
        print(f"Ошибка при создании пары: {e}")
        return None


if __name__ == "__main__":
    pair = make_Pair(10, 20)

    if pair is not None:
        # Вывод диапазона
        pair.display()

        number_to_check = 15
        if pair.rangecheck(number_to_check):
            print(
                f"Число {number_to_check} принадлежит диапазону [{pair.first}, {pair.second})"
            )
        else:
            print(
                f"Число {number_to_check} не принадлежит диапазону [{pair.first}, {pair.second})"
            )

        print("Попробуйте ввести новую пару:")
        if pair.read():
            pair.display()

            if pair.rangecheck(number_to_check):
                print(
                    f"Число {number_to_check} принадлежит новому диапазону [{pair.first}, {pair.second})"
                )
            else:
                print(
                    f"Число {number_to_check} не принадлежит новому диапазону [{pair.first}, {pair.second})"
                )
