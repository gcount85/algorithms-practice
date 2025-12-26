# https://school.programmers.co.kr/learn/courses/30/lessons/12900


def solution(n):
    if n == 1:
        return 1
    if n == 2:
        return 2

    a, b = 1, 2
    for i in range(3, n + 1):
        a, b = b, (a + b) % 1000000007
    return b
