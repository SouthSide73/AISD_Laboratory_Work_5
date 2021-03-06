"""
Формируется матрица F следующим образом: скопировать в нее А и  если в Е количество нулей в нечетных столбцах больше,
чем сумма чисел в нечетных строках, то поменять местами В и Е симметрично, иначе С и Е поменять местами несимметрично.
При этом матрица А не меняется. После чего если определитель матрицы А больше суммы диагональных элементов матрицы F,
то вычисляется выражение:A^-1*A^T-K*F^-1, иначе вычисляется выражение (A^-1+G-F^-1)*K, где G-нижняя треугольная матрица,
полученная из А. Выводятся по мере формирования А, F и все матричные операции последовательно.
"""
import time
import numpy as np
try:
    N = int(input("Введите количество строк (столбцов) квадратной матрицы больше 3 и меньше 184:"))
    while (N < 4) and (N > 183):
        N = int(input("Вы ввели неверное число. "
                      "\nВведите количество строк (столбцов) квадратной матрицы больше 3 и меньше 184:"))
    K = int(input("Введите число К:"))
    program = time.time()
    start = time.time()
    A = np.zeros((N, N), dtype=int)
    F = np.zeros((N, N), dtype=int)
    for i in range(N):     # Формируем матрицу А
        for j in range(N):
            A[i][j] = np.random.randint(-10, 10)
    middle = time.time()
    print("Матрица A:\n", A, "\nВремя:", middle - start)
    for i in range(N):      # Формируем матрицу F, копируя из матрицы А
        for j in range(N):
            F[i][j] = A[i][j]
    n = N // 2         # Размерность подматрицы
    start = time.time()
    E = np.zeros((n, n), dtype=int)   # Формируем матрицу Е
    for i in range(n):
        for j in range(n):
            E[i][j] = A[i][j]
    middle = time.time()
    print("Матрица Е:\n", E, "\nВремя:", middle - start)
    amount = 0
    summa = 0
    for i in range(n):
        for j in range(n):
            if j % 2 == 0 and E[i][j] == 0:   # Количество 0 в нечетных столбцах
                amount += 1
            if i % 2 == 0:    # Сумма элементов в нечетных строках
                summa += E[i][j]
    print("Количество нулей в нечётных столбцах:", amount, "\nСумма чисел в нечётных строках:", summa)
    if amount > summa:
        print("Меняем В и Е симметрично")
        for i in range(n):       # В и Е симметрично
            for j in range(n):
                F[i][j] = A[i][N-j-1]
                F[i][N-j-1] = A[i][j]
    else:
        print("Меняем С и E несимметрично")
        for i in range(n):     # С и E несимметрично
            for j in range(n):
                F[i][j] = A[n + i][n + j]
                F[n + i][n + j] = A[i][j]
    print("Матрица A:\n", A, "\nМатрица F:\n", F)
    print("Определитель матрицы А:", round(np.linalg.det(A)), "\nСумма диагональных элементов матрицы F:", np.trace(F))
    if np.linalg.det(A) == 0 or np.linalg.det(F) == 0:
        print("Нельзя вычислить т.к. матрица A или F вырождена")
    elif np.linalg.det(A) > np.trace(F):
        print("Вычисление выражения: A^-1*A^T-K*F^-1")
        A = np.dot(np.linalg.inv(A), np.transpose(A)) - (np.linalg.inv(F) * K)  # A^-1*A^T-K*F^-1
    else:
        print("Вычисление выражения: (A^-1+G-F^-1)*K")
        A = (np.linalg.inv(A) + np.tril(A) - np.linalg.inv(F)) * K   # (A^-1+G-F^-1)*K
    print("Результат:")
    for i in A:         # Вывод результата
        for j in i:
            print("%5d" % round(j), end=' ')
        print()
    finish = time.time()
    result = finish - program
    print("Время программы: " + str(result) + " секунды.")
except ValueError:
    print("\nЭто не число")
