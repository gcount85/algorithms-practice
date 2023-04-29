# 메모리 초과

import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**5)

n, m = map(int, input().split())
numbers = list(map(int, input().split()))  # 1 <= num <= 1000
memo = {}


def dp(i, j):
    if (i, j) in memo:
        return memo[(i, j)]
    if i == j:
        return numbers[i]
    if i > j:
        return 0
    memo[(i, j)] = dp(i, j-1) + numbers[j]
    return memo[(i, j)]


for _ in range(m):
    i, j = map(int, input().split())
    print(dp(i-1, j-1))
