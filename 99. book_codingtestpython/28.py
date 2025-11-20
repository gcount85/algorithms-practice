# [코딩테스트 연습 - 예상 대진표 | 프로그래머스 스쿨](https://school.programmers.co.kr/learn/courses/30/lessons/12985#)

import math


def solution(n, a, b):
    bigger = a if a > b else b
    smaller = a if a < b else b
    bigger = bigger + 1 if bigger % 2 == 1 else bigger

    answer = 1
    while abs(bigger - smaller) != 1:
        bigger = math.ceil(bigger / 2)
        bigger = bigger + 1 if bigger % 2 == 1 else bigger
        smaller = math.ceil(smaller / 2)
        answer += 1

    return answer
