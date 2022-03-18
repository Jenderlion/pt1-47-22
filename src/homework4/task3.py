"""
Двоичная пирамида.
На вход функции передаются два целых числа m и n, такие что 0 ≤ m ≤ n.
Функция выполняет следующие действия:
Перевести числа от m до n (включительно) в двоичные числа.
Сложить полученные двоичные числа по основанию 10.
Перевести результат сложения в двоичную число.
Вернуть строку с результатом.
"""


def binary_pyramid(m=1, n=4):
    pyramid_sum = 0

    for num in range(m, n + 1):
        pyramid_sum += int(str(bin(num))[2:])

    return str(bin(pyramid_sum))[2:]


print(binary_pyramid())
