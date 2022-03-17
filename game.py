"""Игра угадай число: компьютер загадывает число и отгадывает число"""


import numpy as np


def binary_search(number=1) -> int:
    
    """ Угадываем число с помощью бинарного поиска

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    low = 0     # нижняя граница поиска 
    high = 100  # верхняя граница поиска 

    count = 0 # создаем переменную счетчик, для того чтобы посчитать количество попыток

    while low <= high:
        count += 1
        guess_number = (low + high) / 2 # ищем среднее значение дипазона
        
        if guess_number > number:
            high = guess_number - 1 # если искомое число меньше среднего, то меняем верхнюю границу поиска
        if guess_number < number:
            low = guess_number + 1 # если искомое число больше среднего, то меняем нижнюю границу поиска
        if guess_number == number:
            break # выход из цикла, если число угадано
    
    return count

def guess_game(binary_search) -> int:
    """Какое количество попыток в среднем за 1000 подходов угадывает наш алгоритм

    Args:
        binary_search ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    np.random.seed(1) # инициализируем генератор случайных чисел
    random_array = np.random.randint(1, 101, size=(1000)) # загадываем список чисел
    
    for number in random_array:
        count_ls.append(binary_search(number))
        
    score = int(np.mean(count_ls)) # находим среднее количество попыток
    print(f'Ваш алгоритм угадывает число в среднем за: {score} попыток')
    return(score)

if __name__ == "__main__":
    # RUN
    guess_game(binary_search)



