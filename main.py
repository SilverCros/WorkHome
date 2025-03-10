"""def print_square(size):
    for _ in range(size):
        print('*' * size)

def print_triangle(size):
    for i in range(1, size + 1):
        print('*' * i)

def print_isosceles_triangle(size):
    for i in range(size):
        print(' ' * (size - i - 1) + '*' * (2 * i + 1))

def print_rectangle(width, height):
    for _ in range(height):
        print('*' * width)

def print_diamond(size):
    for i in range(size):
        print(' ' * (size - i - 1) + '*' * (2 * i + 1))
    for i in range(size - 2, -1, -1):
        print(' ' * (size - i - 1) + '*' * (2 * i + 1))

def print_hourglass(size):
    for i in range(size, 0, -1):
        print('*' * i)
    for i in range(2, size + 1):
        print('*' * i)

def main():
    while True:
        print("\n1. Квадрат\n2. Треугольник\n3. Равнобедренный треугольник\n4. Прямоугольник\n5. Ромб\n6. Песочные часы\n7. Выход")
        choice = input("Выберите фигуру: ")

        if choice == '1':
            size = int(input("Размер квадрата: "))
            print_square(size)
        elif choice == '2':
            size = int(input("Размер треугольника: "))
            print_triangle(size)
        elif choice == '3':
            size = int(input("Размер равнобедренного треугольника: "))
            print_isosceles_triangle(size)
        elif choice == '4':
            width = int(input("Ширина: "))
            height = int(input("Высота: "))
            print_rectangle(width, height)
        elif choice == '5':
            size = int(input("Размер ромба: "))
            print_diamond(size)
        elif choice == '6':
            size = int(input("Размер песочных часов: "))
            print_hourglass(size)
        elif choice == '7':
            break
        else:
            print("Некорректный выбор.")

if __name__ == "__main__":
    main()"""

line = input("Введите строку:")

clean_str =''.join(line.split()).lower()
palin = clean_str == clean_str[::-1]
if palin:
    print("Палиндром")
else:
    print("Не палиндром")