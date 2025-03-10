"""
Задание 1
Есть три кортежа целых чисел необходимо найти
элементы, которые есть во всех кортежах.

tuple1 = (1, 2, 3, 4, 5)
tuple2 = (3, 4, 5, 6, 7)
tuple3 = (4, 5, 8, 9)

common_elements = set(tuple1) & set(tuple2) & set(tuple3)

result = tuple(common_elements)

print(result)
"""

"""
Задание 2
Есть три кортежа целых чисел необходимо найти
элементы, которые уникальны для каждого списка.

tuple1 = (1, 2, 3, 4, 5)
tuple2 = (3, 4, 5, 6, 7)
tuple3 = (4, 5, 8, 9)

set1, set2, set3 = map(set, (tuple1, tuple2, tuple3))

unique_to_tuple1 = set1 - set2 - set3
unique_to_tuple2 = set2 - set1 - set3
unique_to_tuple3 = set3 - set1 - set2

print("Уникальные элементы первого списка:", tuple(unique_to_tuple1))
print("Уникальные элементы второго списка:", tuple(unique_to_tuple2))
print("Уникальные элементы третьего списка:", tuple(unique_to_tuple3))
"""

"""
Задание 3
Есть три кортежа целых чисел необходимо найти элементы, которые есть в каждом из кортежей и находятся
в каждом из кортежей на той же позиции.

tuple1 = (17, 23, 36, 48, 52)
tuple2 = (19, 23, 38, 84, 52)
tuple3 = (16, 23, 92, 46, 52)

common_positions = []

for i in range(min(len(tuple1), len(tuple2), len(tuple3))):
    if tuple1[i] == tuple2[i] == tuple3[i]:
        common_positions.append(tuple1[i])

result = tuple(common_positions)

print("Элементы с одинаковой позицией в списках:", result)
"""