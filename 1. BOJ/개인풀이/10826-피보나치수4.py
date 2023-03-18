import sys
sys.setrecursionlimit(10**9)

n = int(sys.stdin.readline())
memo = {}

def fib(n):
    if n in memo:
        return memo[n]
    elif n == 0:
        f = 0
    elif 0 < n <= 2:
        f = 1
    else:
        f = fib(n-1) + fib(n-2)
    memo[n] = f
    return f

print(fib(n))