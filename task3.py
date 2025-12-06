"""
Алгоритм вычисления значения функции F(n) и G(n), где n - целое число, задан следующими соотношениями:
F(n) = 2 * (G(n - 3) + 8);
G(n) = 2 * n, если n < 10;
G(n) = G(n - 2) + 1, если n >= 10.
Чему равно значение выражения F(15548)?

Формат вывода: программа должна печатать только одно число - ответ на задачу.
"""
import sys
sys.setrecursionlimit(1000000)
mas_1 = []
mas_2 = []
for i in range(100000):
    mas_1.append('a')
    mas_2.append('a')
def g(n):
    if n >= 10:
        if mas_2[n] == 'a':
            mas_2[n] = g(n-2) + 1
        return mas_2[n]
    else:
        if mas_2[n] == 'a':
            mas_2[n] = 2*n
        return mas_2[n]
def f(n):
    if mas_1[n] == 'a':
        mas_1[n] = 2*(g(n-3) + 8)
    return mas_1[n]
print(f(15548))