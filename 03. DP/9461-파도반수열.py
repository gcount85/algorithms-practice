from sys import stdin

memo = {1: 1, 2: 1, 3: 1, 4: 2, 5: 2}


def dp(n):
    if n in memo:
        return memo[n]
    memo[n] = dp(n-1) + dp(n-5)
    return memo[n]


t = int(stdin.readline())
for _ in range(t):
    n = int(stdin.readline())
    print(dp(n))
