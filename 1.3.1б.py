import numpy as np  # імпорт бібліотеки numpy


def unionPairs(n):  # створюємо генератор та повертаємо його значення при кожному визовІ функції
    for item in range(n):
        for jtem in range(n):
            yield item, jtem


while True:
    matrix_A = np.zeros([3, 3], dtype=float)  # створюється матриця А розмірності 3х3 з нулями-елементами
    for i, j in unionPairs(3):
        try:
            matrix_A[i][j] = int(input(f'A[{i + 1}][{j + 1}]: '))  # матриця А наповнюється елементами з клавіатури
        except ValueError:
            print('Тільки числа!')
            break
    else:
        print(f'Матриця А:\n{matrix_A}')  # виведення на екран матриці А

        for a in range(3):
            for b in range(3):
                matrix_A[a][b] = matrix_A[b][a]  # транспортування матриці А
        print(f'Транспонована матриця А:\n{matrix_A}')  # виведення на екран транспонованої матриці А
    if input('CONTINUE - Enter, BREAK - something'):
        break
