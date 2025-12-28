# https://school.programmers.co.kr/learn/courses/30/lessons/12913


def solution(land):
    n = len(land)
    dp = [[0] * 4 for _ in range(n)]
    for i in range(4):
        dp[0][i] = land[0][i]
    # print(dp)
    for i in range(1, n):
        for j in range(4):
            dp[i][j] = land[i][j] + max(v for k, v in enumerate(dp[i - 1]) if k != j)
    return max(dp[n - 1])
