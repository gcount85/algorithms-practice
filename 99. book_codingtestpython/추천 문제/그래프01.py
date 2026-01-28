# https://school.programmers.co.kr/learn/courses/30/lessons/49189

"""
bfs로 노드 탐색하면서 가장 거리 먼 노드들 개수 출력하며 ㄴ됨
"""
from collections import deque, defaultdict


def solution(n, edge):
    dic = defaultdict(list)
    for s, d in edge:  # O(N)
        dic[s].append(d)
        dic[d].append(s)
    q = deque([(1, 0)])
    max_dist = 0
    dist = [-1] * (n + 1)
    dist[1] = 0
    while q:  # O(n)
        cur, distance = q.popleft()
        max_dist = max(max_dist, distance)
        for node in dic[cur]:
            if dist[node] == -1:
                q.append((node, distance + 1))
                dist[node] = distance + 1
    return dist.count(max_dist)
