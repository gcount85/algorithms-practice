import sys
sys.setrecursionlimit(10**9)

# memoization + 재귀함수
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

T = int(sys.stdin.readline())
for i in range(1, T+1):
    n, q = map(int, sys.stdin.readline().split())
    print(f"Case #{i}: {fib(n)%q}")






