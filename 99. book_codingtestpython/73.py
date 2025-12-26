# https://school.programmers.co.kr/learn/courses/30/lessons/12945

import sys

sys.setrecursionlimit(10**6)


def solution(n):
    dp = [0] * (n + 1)
    dp[0] = 0
    dp[1] = 1

    def f(n):
        if dp[n]:
            return dp[n]
        else:
            if n == 0:
                return 0
            if n == 1:
                return 1
            dp[n] = (f(n - 1) + f(n - 2)) % 1234567
            return dp[n]

    return f(n)


# 이게 젤 빠름
def solution2(n):
    MOD = 1234567
    a, b = 0, 1
    for _ in range(n):
        a, b = b, (a + b) % MOD
    return a
