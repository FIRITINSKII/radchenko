# Функция для нахождения суммы всех цифр числа
def sum_of_digits(number):
    return sum(int(digit) for digit in str(number))

# Пример использования:
print(sum_of_digits(123))  # Выведет: 6 (1 + 2 + 3)


# Функция для объединения двух строк
def concatenate_strings(str1, str2):
    return str1 + str2

# Пример использования:
print(concatenate_strings("Hello", "World"))  # Выведет: HelloWorld


# Функция для объединения двух списков в один
def merge_lists(list1, list2):
    return list1 + list2

# Пример использования:
print(merge_lists([1, 2, 3], [4, 5, 6]))  # Выведет: [1, 2, 3, 4, 5, 6]


# Функция для объединения двух словарей
def merge_dicts(dict1, dict2):
    return {**dict1, **dict2}

# Пример использования:
print(merge_dicts({'a': 1, 'b': 2}, {'c': 3, 'd': 4}))  # Выведет: {'a': 1, 'b': 2, 'c': 3, 'd': 4}


# Функция для объединения двух сетов
def merge_sets(set1, set2):
    return set1.union(set2)

# Пример использования:
print(merge_sets({1, 2, 3}, {3, 4, 5}))  # Выведет: {1, 2, 3, 4, 5}
