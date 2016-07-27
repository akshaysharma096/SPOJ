"""
Factorial
By: Akshay Sharma
Date: 27/7/16
"""


def Z(n):
    j = 5
    count = 0
    while n // j >= 1:
        count += n // j
        j *= 5
    return count


N = eval(input())
for i in range(N):
    n = eval(input())
    print(Z(n))
