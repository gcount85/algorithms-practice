"""
https://school.programmers.co.kr/learn/courses/30/lessons/132265
각 조각에 동일한 가짓수의 토핑
32분 solved
"""

from collections import Counter


def solution(topping):
    """
    1. 포인터 한개를 두기
    2. 포인터를 기준으로 먼저 좌우에 각각의 토핑이 몇 개씩 있는지 세기. (좌: 포인터 포함)
       좌측: 1한개 / 우측: 1세개, 2두개, 3한개, 4한개
    3. [반복] 포인터가 n-1로 갈 때까지
        2-2. 좌측 딕셔너리 key와 우측 딕셔너리 key 개수가 같으면 ++ answer
        2-3. 포인터를 ++1
        2-4. 우측에서 포인터 자리 토핑을 하나 뺌 -> 0이면 key 삭제 / 좌측에 포인터 자리 토핑 ++1
    """

    n = len(topping)
    pointer = 0
    answer = 0

    # O(N)
    left = Counter(topping[0:1])
    right = Counter(topping[1:])

    # 최대 O(M)
    left_keys_length = len(left.keys())
    right_keys_length = len(right.keys())

    # O(N)
    while pointer < n - 1:
        if left_keys_length == right_keys_length:
            answer += 1
        pointer += 1
        top = topping[pointer]
        right[top] -= 1
        if right[top] == 0:
            right_keys_length -= 1
        if top in left:
            left[top] += 1
        else:
            left[top] = 1
            left_keys_length += 1
    return answer
