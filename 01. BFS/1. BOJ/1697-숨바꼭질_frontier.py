# https://www.acmicpc.net/problem/1697

import sys

n, k = map(int, sys.stdin.readline().split())


def bfs(n, k):
    if n >= k: # -1로만 갈 수 있으므로
        return n - k
    visited = {n: 0}
    i = 0
    queue = [n]
    while queue:
        i += 1
        frontier = []
        for node in queue:
            for new_node in [node + 1, node - 1, node * 2]:
                if 0 > new_node or new_node > 100000:
                    continue
                if new_node == k:
                    return i
                if new_node in visited:
                    continue
                visited[new_node] = i
                # print(f"visited {i}: ", new_node)
                frontier.append(new_node)
        queue = frontier


print(bfs(n, k))
