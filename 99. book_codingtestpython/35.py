# https://school.programmers.co.kr/learn/courses/30/lessons/12981

"""
- 중복 불가
"""


def solution(n, words):
    """
    1.set를 만든다.
    2. word를 순회한다:
        2-1. set에 없다면?: 넣는다.
        2-2. set에 존재한다면?:
            2-2-1. 이때 인덱스를 가지고 몇 번째 인간인지, 몇 라운드인지 계산한다.
                    몇 번째 인간 => 인덱스 % n
                    몇 라운드 => (인덱스 // n) + 1
    """

    unique = set()
    for i, v in enumerate(words):
        if i > 0 and v[0] != words[i - 1][-1]:
            return [(i % n) + 1, (i // n) + 1]
        if v not in unique:
            unique.add(v)
        else:
            return [(i % n) + 1, (i // n) + 1]
    return [0, 0]
