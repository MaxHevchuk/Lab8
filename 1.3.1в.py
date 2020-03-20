import numpy as np


def unionPairs(n, m):  # створюємо генератор та повертаємо його значення при кожному визові функції
    for item in range(n):
        for jtem in range(m):
            yield item, jtem


def matrixMultiplication(m1, m2, r1, c1, r2, c2):
    res_m = np.zeros((r1, c2))  # створюємо розмірність кінечної матриці
    s = 0
    for z in range(0, r1):
        for x in range(0, c2):
            for c in range(0, c1):
                s += m1[z][c] * m2[c][x]  # множимо елементи
            res_m[z, x] = s  # та додаємо в кінчну матрицю
            s = 0
    return res_m


while True:  # матриці можна множити, якщо к-сть столбів А матр. = к-сті рядків В матр.
    colA, rowB = 1, 2  # цикл не прерветься, доки colA не буде = rowB
    rowA, colB = 0, 0
    while colA != rowB:
        print("\nК-сть столбців у першій матриці повинно = к-сті рядків у другій матриці")
        try:
            rowA, colA = int(input('Кількість рядків у матриці А: ')), int(input('Кількість стовпців у матриці А: '))
            rowB, colB = int(input('Кількість рядків у матриці B: ')), int(input('Кількість стовпців у матриці B: '))
        except ValueError:
            print('Тільки числа!')
            continue

    matrix_A, matrix_B = np.zeros((rowA, colA)), np.zeros((rowB, colB))  # створюємо матриці відповідних розмірностей

    print('\nВведіть елементи матриці A:')
    while True:
        for i, j in unionPairs(rowA, colA):
            try:
                matrix_A[i, j] = float(input(f'A[{i + 1}][{j + 1}]: '))  # вводимо елементи матриці А
            except ValueError:
                print('Тільки числа!\n')
                break
        else:
            break

    print('\nВведіть елементи матриці B:')
    while True:
        for q, w in unionPairs(rowB, colB):
            try:
                matrix_B[q, w] = float(input(f'B[{q + 1}][{w + 1}]: '))  # вводимо елементи матриці В
            except ValueError:
                print('Тільки числа!\n')
                break
        else:
            break

    print(matrixMultiplication(matrix_A, matrix_B, rowA, colA, rowB, colB))  # виводимо матрицю-результат множення

    if input('CONTINUE - Enter; BREAK - something'):
        break
