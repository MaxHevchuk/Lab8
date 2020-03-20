import numpy as np  # імпорт бібліотеки numpy

while True:
    try:
        matrix = np.array(list(map(float, input('Введіть лінійний масив: ').split())),
                          dtype=float)  # вводиться лінійний масив
    except ValueError:  # якщо ввели не float, то виводиться помилка
        print('Тільки числа!\n')
        continue
    else:
        print(f'Обернений масив: {list(reversed(matrix))}')  # виведення елементів масиву в оберненому напрямку

    if input('\nCONTINUE - Enter, BREAK - something'):
        break
