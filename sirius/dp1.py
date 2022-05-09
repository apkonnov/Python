"""
Числа Фибоначчи
Числа Фибоначчи определяются следующими формулами: F0=0, F1=1, Fn=Fn−1+Fn–2 при n≥2.

Входные данные
На вход программе подаётся целое неотрицательное n≤45.

Выходные данные
Выведите n-е число Фибоначчи.
"""

num = int(input('Введите число n = '))
dp = [-1] * (num + 1)


def fibonacci(n):
    if dp[n] != -1:
        return dp[n]
    if n < 2:
        return n
    dp[n] = fibonacci(n - 1) + fibonacci(n - 2)
    return dp[n]


print(f'{num} число Фибоначчи равно {fibonacci(num)}')
