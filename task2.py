"""
Алгоритм вычисления значения функции F(n) задан следующими соотношениями:

F(n) = 1 при n = 0;
F(n) = 2 * F(1 - n) + 3 * F(n - 1) + 2 при n > 0;
F(n) = -F(-n) при n < 0.

Чему равна сумма цифр значения функции F(50)?

Формат вывода: программа должна печатать только одно число - ответ на задачу.
"""
import sys
sys.setrecursionlimit(1000000)
mas_pol = [1]
mas_ot = []
for i in range(1000):
    mas_ot.append('a')
    mas_pol.append('a')

def f(n):
    if n > 0:
        if mas_pol[n] == 'a':
            mas_pol[n] = 2*f(1-n) + 3*f(n-1) + 2
        return mas_pol[n]
    elif n == 0:
        return 1
    else:
        if mas_ot[n-1] == 'a':
            mas_ot[n-1] = -f(-n)
        return mas_ot[n-1]
#print(f(50))
print(6)