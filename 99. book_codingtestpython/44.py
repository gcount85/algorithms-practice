# https://school.programmers.co.kr/learn/courses/30/lessons/12978
# 32분 solved

"""
N개의 마을 중 K 시간 이하로 갈 수 있는 마을
음의 가중치 없고, 단일 노드 최단거리 -> 다익스트라
최단 거리가 K 이하인 노드만 리턴
"""

import heapq
from collections import defaultdict


def solution(N, road, K):
    """
    1. 인접 리스트 초기화, 우선순위 큐 초기화, 거리 배열 초기화
    2. 우선순위 큐가 빌 때까지:
        2-1. 현재 노드, 거리 = 큐 pop
        2-2. 저장된 거리보다 pop 된 거리가 길면 pass
        2-3. 현재 노드의 이웃들에 대해서:
            2-3-1. 현재 노드를 거쳐가는 거리가 더 짧으면 갱신
            2-3-2. heap push
    3. 거리 배열에서 k 이하 개수 반환
    """

    INF = float("inf")
    distances = [INF for _ in range(N + 1)]
    graph = defaultdict(list)

    for source, dest, weight in road:
        graph[source].append((dest, weight))
        graph[dest].append((source, weight))

    queue = [(0, 1)]  # 거리, 노드번호
    distances[1] = 0
    while queue:
        cur_dist, cur_node = heapq.heappop(queue)
        if cur_dist > K:
            continue
        if cur_dist != distances[cur_node]:
            continue
        for dest, weight in graph[cur_node]:
            if distances[dest] > cur_dist + weight:
                distances[dest] = cur_dist + weight
                heapq.heappush(queue, (distances[dest], dest))

    answer = sum(1 for v in distances if v <= K)
    return answer
