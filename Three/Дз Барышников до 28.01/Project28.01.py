"""Задание 1:
Пользователь вводит с клавиатуры арифметическое
выражение. Например, 23+12.
Необходимо вывести на экран результат выражения.
В нашем примере это 35. Арифметическое выражение
может состоять только из трёх частей: число, операция,
число. Возможные операции: +, -,*,/."""

"""example = input("Введите арифметическое выражение: ")

try:
    if '+' in example:
        num1, num2 = example.split('+')
        result = float(num1) + float(num2)
    elif '-' in example:
        num1, num2 = example.split('-')
        result = float(num1) - float(num2)
    elif '*' in example:
        num1, num2 = example.split('*')
        result = float(num1) * float(num2)
    elif '/' in example:
        num1, num2 = example.split('/')
        result = float(num1) / float(num2)
    else:
        raise ValueError("Недопустимая операция.")

    print("Результат выражения:", result)

except Exception as i:
    print("Ошибка выражения:", i)"""

"""Задание 2:
В списке целых, заполненном случайными числами,
определить минимальный и максимальный элементы,
посчитать количество отрицательных элементов, посчитать количество положительных элементов, посчитать
количество нулей. Результаты вывести на экран."""

"""import random

size = 30
number = [random.randint(-15, 15) for _ in range(size)]

min_value = min(number)
max_value = max(number)
negative_value = sum(1 for num in number if num < 0)
positive_value = sum(1 for num in number if num > 0)
zero_value = number.count(0)

print("Сгенерированный список:", number)
print("Минимальный элемент:", min_value)
print("Максимальный элемент:", max_value)
print("Количество отрицательных элементов:", negative_value)
print("Количество положительных элементов:", positive_value)
print("Количество нулей:", zero_value)"""