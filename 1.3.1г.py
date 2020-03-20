import numpy as np


def unique_pairs(n):  # створюємо генератор та повертаємо його значення при кожному визовІ функції
    for item in range(n):
        for jtem in range(n):
            yield item, jtem


while True:
    matrix_A = np.zeros([4, 4], dtype=float)  # створюємо матрицю 4х4 з нулів
    matrix_B = np.zeros([4, 4], dtype=float)  # ствоюємо таку ж матрицю
    print('Введіть елементи матриці А:')
    for i, j in unique_pairs(4):
        try:
            input_element = float(input(f'A[{i + 1}][{j + 1}]: '))  # вводимо елементи матриці
        except ValueError:  # якщо вводиться не float виводиться помилка
            print('Тільки числа!\n')
            break
        else:
            matrix_A[i][j], matrix_B[i][j] = \
                input_element, input_element  # якщо помилки немає - додаємо елементи до обох матриць
            if input_element < 0:  # якщо ввелися від'ємні значення, то у 2-ій матриці вони замінюються на 0
                matrix_B[i][j] = 0
    else:
        print(f'Матриця А:\n{matrix_A}\n'  # виведення на екран початкову матрицю
              f'Матриця B:\n{matrix_B}')  # та зі зміненими значеннями
        if input('CONTINUE - enter, EXIT - something: '):
            break
    continue
