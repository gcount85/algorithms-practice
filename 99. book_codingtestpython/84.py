# https://school.programmers.co.kr/learn/courses/30/lessons/138476

from collections import Counter


def solution(k, tangerine):  # 귤 개수 K, 귤 배열
    """
    1. 귤 종류별로 카운팅
    2. 가장 종류가 많은 귤부터 채움
    """

    # 가장 종류가 많은 귤부터 내림차순 정렬
    counter = sorted(Counter(tangerine).values(), reverse=True)
    answer = 0
    for count in counter:
        diff = k - count
        answer += 1
        if diff <= 0:
            break
        k = diff

    return answer
