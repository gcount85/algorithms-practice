"""
다익스트라 : 단일 노드에서 모든 노드까지 최단 거리 구하기

1. 인접리스트, 힙큐, distance 배열 초기화
2. 힙큐가 빌 때까지 반복:
    2-1. curdist, node = heappop
    2-2. 현 노드에서 갈 수 있는 노드들에 대하여:
        2-2-1. curdist + 인접리스트[next node] <= distance[next node]: distance 업데이트 + 힙에 담음

"""

import heapq
from collections import defaultdict


def solutions(start, numNodes, edges):
    # 인접리스트, 힙큐, distance 초기화
    graph = defaultdict(list)
    for s, d, w in edges:
        graph[s].append((d, w))
    distance = [99999] * numNodes
    distance[start] = 0
    heap = [(0, start)]

    # 힙이 빌 때까지 반복
    while heap:
        cur_dist, cur_node = heapq.heappop(heap)
        for nxt, nxt_dist in graph[cur_node]:
            if cur_dist + nxt_dist <= distance[nxt]:
                distance[nxt] = cur_dist + nxt_dist
                heapq.heappush(heap, (cur_dist + nxt_dist, nxt))

    return distance


print(solutions(0, 3, [[0, 1, 9], [0, 2, 3], [1, 0, 5], [2, 1, 1]]))  # [0, 4, 3]
print(solutions(0, 4, [[0, 1, 1], [1, 2, 5], [2, 3, 1]]))  # [0, 1,6,7]
