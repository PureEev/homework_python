import pandas as pd

# Создаем мультииндекс и данные
index = pd.MultiIndex.from_tuples([
    ('city_1', 2010),
    ('city_1', 2020),
    ('city_2', 2010),
    ('city_2', 2020),
    ('city_3', 2010),
    ('city_3', 2020),
], names=['city', 'year'])

population = [
    101,
    201,
    102,
    202,
    103,
    203,
]

# Создаем Series с мультииндексом
pop = pd.Series(population, index=index)

# Создаем DataFrame с мультииндексом
pop_df = pd.DataFrame(
    {
        'total': pop,
        'something': [
            10,
            11,
            12,
            13,
            14,
            15,
        ]
    }
)

# Пример 1: Выбор данных для 'city_1' и столбца 'something'
pop_df_1 = pop_df.xs('city_1', level='city')['something']
print("Задание 1, Пример 1:")
print(pop_df_1)
print()

# Пример 2: Выбор данных для 'city_1' и 'city_3' и столбцов 'total' и 'something'
pop_df_2 = pop_df.loc[(['city_1', 'city_3'], slice(None)), ['total', 'something']]
print("Задание 1, Пример 2:")
print(pop_df_2)
print()

# Пример 3: Выбор данных для 'city_1' и 'city_3' и столбца 'something'
pop_df_3 = pop_df.loc[(['city_1', 'city_3'], slice(None)), 'something']
print("Задание 1, Пример 3:")
print(pop_df_3)
print()

# ==================================================
# Задание 2: Выбор данных по определенным условиям
# ==================================================

# Выбор данных по 2020 году для всех столбцов
pop_df_2020 = pop_df.xs(2020, level='year')
print("Задание 2, Данные за 2020 год:")
print(pop_df_2020)
print()

# ==================================================
# Задание 3: Работа с MultiIndex в DataFrame
# ==================================================

# Создаем мультииндекс для строк и столбцов
index = pd.MultiIndex.from_product(
    [
        ['city_1', 'city_2'],
        [2010, 2020]
    ],
    names=['city', 'year']
)

columns = pd.MultiIndex.from_product(
    [
        ['person_1', 'person_2', 'person_3'],
        ['job_1', 'job_2']
    ],
    names=['worker', 'job']
)

# Создаем данные с правильным количеством столбцов (6 столбцов)
# Каждый внутренний список представляет строку, а количество элементов в списке должно быть равно количеству столбцов
data = [
    [1, 2, 3, 4, 5, 6],  # Данные для city_1, 2010
    [7, 8, 9, 10, 11, 12],  # Данные для city_1, 2020
    [13, 14, 15, 16, 17, 18],  # Данные для city_2, 2010
    [19, 20, 21, 22, 23, 24],  # Данные для city_2, 2020
]

# Создаем DataFrame с мультииндексом
df = pd.DataFrame(data, index=index, columns=columns)

# Пример 1: Все данные по 'person_1' и 'person_3'
df_person1_person3 = df.loc[:, (['person_1', 'person_3'], slice(None))]
print("Задание 3, Пример 1: Данные по person_1 и person_3")
print(df_person1_person3)
print()

# Пример 2: Все данные по первому городу и первым двум person-ам
df_city1_person1_2 = df.loc['city_1', (['person_1', 'person_2'], slice(None))]
print("Задание 3, Пример 2: Данные по city_1 и person_1, person_2")
print(df_city1_person1_2)
print()

# Пример с использованием pd.IndexSlice
idx = pd.IndexSlice
df_slice = df.loc[idx['city_1', :], idx[:, 'job_1']]
print("Задание 3, Пример 3: Использование pd.IndexSlice")
print(df_slice)
print()

# ==================================================
# Задание 4: Пример использования inner и outer джойнов для Series
# ==================================================

# Создаем две Series
ser1 = pd.Series(['a', 'b', 'c'], index=[1, 2, 3])
ser2 = pd.Series(['b', 'c', 'f'], index=[4, 5, 6])

# Outer join (объединение по всем индексам)
outer_join = pd.concat([ser1, ser2], join='outer')
print("Задание 4, Outer Join:")
print(outer_join)
print()

# Inner join (объединение только по общим индексам)
inner_join = pd.concat([ser1, ser2], join='inner')
print("Задание 4, Inner Join:")
print(inner_join)
print()