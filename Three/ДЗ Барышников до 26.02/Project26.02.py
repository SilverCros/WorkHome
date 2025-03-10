"""
Задание 1
К уже реализованному классу «Дробь» добавьте статический метод,
который при вызове возвращает количество созданных объектов класса «Дробь».

class SimpleFraction:
    def __init__(self, num, denom):
        self.num = num
        self.denom = denom

    def set_num(self, num):
        self.num = num

    def set_denom(self, denom):
        self.denom = denom

    def get_num(self):
        return self.num

    def get_denom(self):
        return self.denom

    def input_data(self):
        self.num = int(input("Введите числитель: "))
        self.denom = int(input("Введите знаменатель: "))

    def output_data(self):
        print(f"{self.num}/{self.denom}")

    def add(self, other):
        result_num = (self.num * other.denom) + (other.num * self.denom)
        result_denom = self.denom * other.denom
        return SimpleFraction(result_num, result_denom)

    def subtract(self, other):
        result_num = (self.num * other.denom) - (other.num * self.denom)
        result_denom = self.denom * other.denom
        return SimpleFraction(result_num, result_denom)

    def multiply(self, other):
        result_num = self.num * other.num
        result_denom = self.denom * other.denom
        return SimpleFraction(result_num, result_denom)

    def divide(self, other):
        result_num = self.num * other.denom
        result_denom = self.denom * other.num
        return SimpleFraction(result_num, result_denom)
"""

"""
Задание 2
Создайте класс для конвертирования температуры из
Цельсия в Фаренгейт и наоборот. У класса должно быть
два статических метода: для перевода из Цельсия в 
Фаренгейт и для перевода из Фаренгейта в Цельсий. Также
класс должен считать количество подсчетов температуры и
возвращать это значение с помощью статического метода.

class TempConverter:
    conversion_count = 0

    @staticmethod
    def convert_celsius_to_fahrenheit(celsius):
        TempConverter.conversion_count += 1
        fahrenheit = (celsius * 9/5) + 32
        return fahrenheit

    @staticmethod
    def convert_fahrenheit_to_celsius(fahrenheit):
        TempConverter.conversion_count += 1
        celsius = (fahrenheit - 32) * 5/9
        return celsius

    @staticmethod
    def get_total_conversions():
        return TempConverter.conversion_count

temp_c = 30
temp_f = TempConverter.convert_celsius_to_fahrenheit(temp_c)
print(f"{temp_c}°C = {temp_f}°F")

temp_f = 86
temp_c = TempConverter.convert_fahrenheit_to_celsius(temp_f)
print(f"{temp_f}°F = {temp_c}°C")

print(f"Количество конвертаций: {TempConverter.get_total_conversions()}")
"""

"""
Задание 3
Создайте класс для перевода из метрической системы
в английскую и наоборот. Функциональность необходимо
реализовать в виде статических методов. Обязательно
реализуйте перевод мер длины.

class DistanceConverter:
    METERS_TO_YARDS = 1.09361
    YARDS_TO_METERS = 0.9144

    @staticmethod
    def convert_meters_to_yards(meters):
        yards = meters * DistanceConverter.METERS_TO_YARDS
        return yards

    @staticmethod
    def convert_yards_to_meters(yards):
        meters = yards * DistanceConverter.YARDS_TO_METERS
        return meters

length_m = 15
length_yd = DistanceConverter.convert_meters_to_yards(length_m)
print(f"{length_m} м = {length_yd} ярдов")

length_yd = 16.4
length_m = DistanceConverter.convert_yards_to_meters(length_yd)
print(f"{length_yd} ярдов = {length_m} м")
"""
