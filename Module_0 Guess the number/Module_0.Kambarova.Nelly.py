#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


def game_core(number):
    '''Сначала устанавливаем любое random число, используем бинарный поиск числа.
       Функция принимает загаданное число и возвращает число попыток'''

    count = 0 # счетчик попыток
    perdict = np.random.randint(1,101) # предполагаемое число
    lower_bound = 1   # создаем переменную нижней границы
    upper_bound = 100 # создаем переменную верхней границы
    
    while lower_bound < upper_bound:
        center = (lower_bound + upper_bound) // 2  # создаем переменную центр 
        count += 1 
        if number == perdict:
            return count
        elif number > perdict:
            upper_bound = center - 1
        elif number < perdict:
            lower_bound = center + 1       
    return(count)   


def score_game(game_core):
    count_ls = []
    np.random.seed(1) 
    random_array = np.random.randint(1,101, size=(1000))
    for number in random_array:
        count_ls.append(game_core(number))
    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")
    return(score)


score_game(game_core)

