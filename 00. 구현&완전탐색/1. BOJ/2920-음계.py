# https://www.acmicpc.net/problem/2920

import sys


def solution():
    input = sys.stdin.readline
    음계 = list(map(int, input().split()))
    n = len(음계)

    flag = "ascending"
    gap = -1
    if (음계[0] == 8):
        flag = "descending"
        gap = 1

    for i in range(n-1):
        if (음계[i] - 음계[i+1] != gap):
            return "mixed"

    return flag


print(solution())
