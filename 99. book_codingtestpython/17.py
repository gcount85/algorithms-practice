"""
https://school.programmers.co.kr/learn/courses/30/lessons/159994
1. goal을 순회
    1-1. goal[i]가 카드1이나 카드2에 있는지 확인하고 있으면: popleft
        없으면: return "No"
2. 정상적으로 순회 다 끝났으면 "Yes"

"""

from collections import deque


def solution(cards1, cards2, goal):
    c1 = deque(cards1)
    c2 = deque(cards2)
    for e in goal:
        c1_word = c1.popleft() if c1 else 0
        c2_word = c2.popleft() if c2 else 0
        if c1_word == e:
            c2.appendleft(c2_word)
        elif c2_word == e:
            c1.appendleft(c1_word)
        else:
            return "No"

    answer = "Yes"
    return answer
