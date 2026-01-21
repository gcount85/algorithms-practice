# https://school.programmers.co.kr/learn/courses/30/lessons/118667

from collections import deque


def solution(queue1, queue2):
    q1_sum = sum(queue1)  # O(N)
    q2_sum = sum(queue2)  # O(N)
    if (total := q1_sum + q2_sum) % 2 == 1:
        return -1

    half = total // 2
    if q1_sum == half:
        return 0

    q1 = deque(queue1)  # O(N)
    q2 = deque(queue2)  # O(N)

    n = len(q1) + len(q2)
    answer = 0
    while answer <= n + 1:  # O(N)
        if q1_sum > q2_sum:
            popped = q1.popleft()
            q2.append(popped)
            q1_sum -= popped
            q2_sum += popped
        elif q2_sum > q1_sum:
            popped = q2.popleft()
            q1.append(popped)
            q2_sum -= popped
            q1_sum += popped
        answer += 1
        if q1_sum == q2_sum:
            return answer
    return -1
