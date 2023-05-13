# https://www.acmicpc.net/problem/2748

import sys

n = int(sys.stdin.readline())
memo = {}

def fib(n):
    if n in memo:
        return memo[n]
    if n <= 2:
        f = 1
    else:
        f = fib(n-1) + fib(n-2)
        memo[n] = f
    return f

print(fib(n))