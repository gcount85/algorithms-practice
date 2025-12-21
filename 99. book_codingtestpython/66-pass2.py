"""
https://school.programmers.co.kr/learn/courses/30/lessons/132265
각 조각에 동일한 가짓수의 토핑
32분 solved
"""

from collections import Counter


def solution(topping):
    """
    1. 포인터 한개를 두기
    2. 포인터를 기준으로 먼저 좌우에 각각의 토핑이 몇 개씩 있는지 세기. (우: 포인터 포함)
    3. [반복] 포인터가 n-1로 갈 때까지
        2-2. 좌측 딕셔너리 key와 우측 딕셔너리 key 개수가 같으면 ++ answer
        2-3. 포인터를 ++1
        2-4. 우측에서 포인터 자리 토핑을 하나 뺌 -> 0이면 key 삭제 / 좌측에 포인터 자리 토핑 ++1
    """

    n = len(topping)
    pointer = 0
    answer = 0

    # O(N)
    left = set()
    right = Counter(topping)

    # O(N)
    while pointer < n - 1:
        if len(left) == len(right):
            answer += 1
        top = topping[pointer]
        left.add(top)  # 좌측에 추가
        right[top] -= 1  # 우측에서 뺌
        if right[top] == 0:  # 우측에서 토핑 없어지면 종류 제거
            right.pop(top)
        pointer += 1

    return answer
