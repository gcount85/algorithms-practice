"""
https://school.programmers.co.kr/learn/courses/30/lessons/12980
1. 도착지의 1/2 거리가 정수가 아니다 -> floor 취하고 건전지 사용량 +1
"""

import math


def solution(n):
    ans = 0
    while n != 1:
        n /= 2
        if n % 1 != 0:
            n = math.floor(n)
            ans += 1

    return ans + 1
