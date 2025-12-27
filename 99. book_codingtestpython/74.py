# https://school.programmers.co.kr/learn/courses/30/lessons/12900


def solution(n):
    if n == 1:
        return 1
    if n == 2:
        return 2

    a, b = 1, 2
    for _ in range(3, n + 1):
        a, b = b, (a + b) % 1000000007
    return b


# 반복 횟수를 다르게 정의할 수도 있음
def solution2(n):
    if n == 1:
        return 1
    if n == 2:
        return 2

    a, b = 1, 2  # dp[1], dp[2]
    for _ in range(n - 2):  # n-2번 반복하면 a는 dp[n-1], b는 dp[n]
        a, b = b, (a + b) % 1000000007
    return b
