"""
1
class Car:
    def __init__(self, name="", year=0, maker="", engine_size=0.0, color="", price=0.0):
        self.name = name
        self.year = year
        self.maker = maker
        self.engine_size = engine_size
        self.color = color
        self.price = price

    def data_input(self):
        self.name = input("Введите название модели: ")
        self.year = int(input("Введите год выпуска: "))
        self.maker = input("Введите производителя: ")
        self.engine_size = float(input("Введите объём двигателя: "))
        self.color = input("Введите цвет: ")
        self.price = float(input("Введите цену: "))

    def data_output(self):
        print("Характеристики машины".center(35, "-"))
        print(f"Название модели: {self.name}")
        print(f"Год выпуска: {self.year}")
        print(f"Производитель: {self.maker}")
        print(f"Объём двигателя: {self.engine_size}")
        print(f"Цвет: {self.color}")
        print(f"Цена: {self.price}")

    def output_name(self):
        print(f"Название модели: {self.name}".center(35, "-"))

    def output_year(self):
        print(f"Год выпуска: {self.year}".center(35, "-"))

    def output_maker(self):
        print(f"Производитель: {self.maker}".center(35, "-"))

    def output_engine_size(self):
        print(f"Объём двигателя: {self.engine_size}".center(35, "-"))

    def output_color(self):
        print(f"Цвет: {self.color}".center(35, "-"))

    def output_price(self):
        print(f"Цена: {self.price}".center(35, "-"))

    def __str__(self):
        return f"{self.name} ({self.year}) - {self.maker}, {self.color}, {self.price} у.е."

    def __eq__(self, other):
        return self.name == other.name and self.year == other.year

    def __lt__(self, other):
        return self.price < other.price
"""

"""
2
class Book:
    def __init__(self, name="", year=0, maker="", genre="", author="", price=0.0):
        self.name = name
        self.year = year
        self.maker = maker
        self.genre = genre
        self.author = author
        self.price = price

    def data_input(self):
        self.name = input("Введите название книги: ")
        self.year = int(input("Введите год выпуска: "))
        self.maker = input("Введите издателя: ")
        self.genre = input("Введите жанр: ")
        self.author = input("Введите автора: ")
        self.price = float(input("Введите цену: "))

    def data_output(self):
        print("Описание книги".center(35, "-"))
        print(f"Название книги: {self.name}")
        print(f"Год выпуска: {self.year}")
        print(f"Издатель: {self.maker}")
        print(f"Жанр: {self.genre}")
        print(f"Автор: {self.author}")
        print(f"Цена: {self.price}")

    def output_name(self):
        print(f"Название книги: {self.name}".center(35, "-"))

    def output_year(self):
        print(f"Год выпуска: {self.year}".center(35, "-"))

    def output_maker(self):
        print(f"Издатель: {self.maker}".center(35, "-"))

    def output_genre(self):
        print(f"Жанр: {self.genre}".center(35, "-"))

    def output_author(self):
        print(f"Автор: {self.author}".center(35, "-"))

    def output_price(self):
        print(f"Цена: {self.price}".center(35, "-"))

    def __str__(self):
        return f"{self.name} ({self.year}) - {self.author}, {self.genre}, {self.price} у.е."

    def __eq__(self, other):
        return (self.name, self.author) == (other.name, other.author)

    def __lt__(self, other):
        return self.price < other.price
"""

"""
3
class Stadium:
    def __init__(self, name="", date="", country="", city="", capacity=0):
        self.name = name
        self.date = date
        self.country = country
        self.city = city
        self.capacity = capacity

    def data_input(self):
        self.name = input("Введите название стадиона: ")
        self.date = input("Введите дату открытия: ")
        self.country = input("Введите страну: ")
        self.city = input("Введите город: ")
        self.capacity = int(input("Введите вместимость: "))

    def data_output(self):
        print("Стадион".center(35, "-"))
        print(f"Название стадиона: {self.name}")
        print(f"Дата открытия: {self.date}")
        print(f"Страна: {self.country}")
        print(f"Город: {self.city}")
        print(f"Вместимость: {self.capacity}")

    def output_name(self):
        print(f"Название стадиона: {self.name}".center(35, "-"))

    def output_date(self):
        print(f"Дата открытия: {self.date}".center(35, "-"))

    def output_country(self):
        print(f"Страна: {self.country}".center(35, "-"))

    def output_city(self):
        print(f"Город: {self.city}".center(35, "-"))

    def output_capacity(self):
        print(f"Вместимость: {self.capacity}".center(35, "-"))

    def __str__(self):
        return f"{self.name} ({self.date}) - {self.city}, {self.country}, Вместимость: {self.capacity}"

    def __eq__(self, other):
        return (self.name, self.date) == (other.name, other.date)

    def __lt__(self, other):
        return self.capacity < other.capacity
"""