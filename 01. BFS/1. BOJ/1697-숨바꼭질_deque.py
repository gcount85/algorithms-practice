# https://www.acmicpc.net/problem/1697
# 더 느림 

import sys
from collections import deque

input = sys.stdin.readline
n, k = map(int, input().split())


def bfs(n, k):
    if n == k:
        return 0
    visited = {n: 0}
    queue = deque([(n, 0)])
    while queue:
        node, level = queue.popleft()
        for new_node in [node + 1, node - 1, node * 2]:
            if 0 > new_node or new_node > 100000:
                continue
            if new_node == k:
                return level + 1
            if new_node in visited:
                continue
            visited[new_node] = level + 1
            # print(f"visited {i}: ", new_node)
            queue.append((new_node, level + 1))


print(bfs(n, k))
