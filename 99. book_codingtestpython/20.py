"""
https://school.programmers.co.kr/learn/courses/30/lessons/42576?language=python3
- N 10만개 -> NlogN 까지 괜찮
- 완주 못한 사람은 1명
- 동명이인 있음
"""


def solution(participant, completion):
    """
    1. completion 배열을 해시화 (k,v = 이름, 횟수)
    2. participant 순회:
        completion 해시테이블에 있음: v -1 처리
        completion 해시테이블에 없음 or v 값이 0이하: return elem
    """
    dic = {}
    for c in completion:  # O(N)
        v = dic.get(c, 0)
        dic[c] = v + 1
    for p in participant:  # O(N)
        v = dic.get(p, 0)
        if v <= 0:
            return p
        dic[p] = v - 1
