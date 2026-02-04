"""
https://school.programmers.co.kr/learn/courses/30/lessons/42747?language=python3#
h번 인용된 논문이 h편 이상, 나머지 논문은 h번 이하 인용 -> h의 최댓값 구하기.

1. citations 정렬
2. 가운데 포인터(n//2) 잡고 시작. 이때 h는 n - n//2
3. while 포인터가 0보다 크고 n보다 작을 동안:
    3-1. citations[pointer] >= h:
            포인터를 왼쪽으로 옮겨
            h ++ 1
        else:
            return h - 1
"""


def solution(citations):
    citations.sort()
    n = len(citations)
    pointer = n // 2
    h = n - pointer

    while pointer >= 0 and pointer < n:
        if citations[pointer] == 0:
            return 0
        if citations[pointer] >= h:
            pointer -= 1
            h += 1
        else:
            break
    return h - 1
