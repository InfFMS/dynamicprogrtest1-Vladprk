"""
(В. Лашин) Алгоритм вычисления значения функции F(n) и G(n), где n -- целое число, задан следующими соотношениями:
F(n) = G(n - 50000) + G(n + 50000)
G(n) = 5^n, если n <= 6
G(n) = G(n - 3) + 2, если n > 6
Чему равно значение выражения F(100000)?

Формат вывода: программа должна печатать только одно число - ответ на задачу.
"""
import sys
sys.setrecursionlimit(1000000)
mas_1 = []
mas_2 = []
for i in range(1000000):
    mas_1.append('a')
    mas_2.append('a')
def g(n):
    if n <= 6:
        if mas_2[n] == 'a':
            mas_2[n] = 5**n
        return mas_2[n]
    else:
        if mas_2[n] == 'a':
            mas_2[n] = g(n - 3) + 2
        return mas_2[n]
def f(n):
    if mas_1[n] == 'a':
        mas_1[n] = g(n - 50000) + g(n + 50000)
    return mas_1[n]
print(f(100000))
