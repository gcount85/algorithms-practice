# https://school.programmers.co.kr/learn/courses/30/lessons/43105


def solution(triangle):
    n = len(triangle)
    dp = [[0] * n for _ in range(n)]

    for i in range(n):
        dp[n - 1][i] = triangle[n - 1][i]

    # dp 아랫줄부터 채움
    for i in range(n - 2, -1, -1):
        for j in range(i + 1):
            dp[i][j] = max(dp[i + 1][j], dp[i + 1][j + 1]) + triangle[i][j]

    return dp[0][0]
