# Пригодится для наполнения списков!
from random import randint
from statistics import mean
from functools import reduce

# 1. Создание списка списков:
harvest = [[randint(5,20) for i in range(3)] for j in range(3)]

# 2. Функция для подсчёта общего урожая:
def total_harvest(list_of_lists):
    return reduce(lambda x,y: x+y, reduce(lambda x,y: x+y, list_of_lists))

# 3. Функция для подсчёта среднего урожая с каждого участка:
def average_harvest_per_plot(list_of_lists):
    return [sum(el)/len(el) for el in list_of_lists]

# Вывод результатов
print('Урожай с каждой грядки на каждом участке:', harvest)
print('Общий урожай со всех участков:', total_harvest(harvest))
print('Средний урожай с каждого участка:', average_harvest_per_plot(harvest))