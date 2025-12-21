"""
https://school.programmers.co.kr/learn/courses/30/lessons/42842?language=python3
갈색 = 2x + 2y - 4
노란색 =  (x - 2) * (y - 2) = xy -2y -2x +4
가로*세로 = brown + yellow
가로세로 둘 다 3이상

"""

import math


def solution(brown, yellow):
    size = brown + yellow  # 12
    for a in range(3, math.floor(math.sqrt(size)) + 1):
        if size % a != 0:
            continue
        b = size // a
        if (a - 2) * (b - 2) != yellow:
            continue
        else:
            return [a if a > b else b, a if a < b else b]
