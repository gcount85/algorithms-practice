"""
- 1부터 N까지 번호표
- 1번 기준으로(1번을 포함해서) k 번째 사람 제거
"""

from collections import deque


def solution(N, K):
    q = deque([i + 1 for i in range(N)])

    while len(q) > 1:
        print(q)
        for _ in range(K - 1):
            q.append(q.popleft())
        q.popleft()
    return q[0]


print(solution(5, 2))
