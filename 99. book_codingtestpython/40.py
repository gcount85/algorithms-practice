# 다익스트라

import heapq
from collections import defaultdict


def solution(start, num_nodes, edges):
    """
    1. 인접 행렬/인접 리스트 초기화
    2. 방문 배열 초기화
    3. distances 초기화
    4. 힙에 스타트 노드 추가
    5. 힙이 빌 때까지 반복:
        5-0. cur = heap popped, cur 노드 방문처리
        5-1. start 노드에서 가장 싸게 갈 수 있는 곳으로 먼저 감.
        5-2. 그 노드에서 다른 인접노드 갈때 더 싸게 갈 수 있는지 갱신
        5-3. (인접노드, 가중치)를 힙에 넣음
    6. distance 반환
    """

    graph = defaultdict(list)
    for s, d, w in edges:
        graph[s].append((d, w))

    INF = float("inf")
    visited = set()
    distances = [INF] * num_nodes
    distances[start] = 0

    priority_queue = [(0, start)]  # ⚠️ 정렬 기준은 첫 원소!!
    while priority_queue:
        cur_dist, cur_node = heapq.heappop(priority_queue)
        if cur_dist != distances[cur_node]:  # ⭐ stale entry 제거, 방문 배열 체크랑 택1
            continue
        # if cur_node in visited:
        #     continue
        # visited.add(cur_node)
        for n, w in graph[cur_node]:
            if distances[n] > cur_dist + w:
                distances[n] = cur_dist + w
                heapq.heappush(priority_queue, (distances[n], n))

    return distances


# TEST 코드 입니다. 주석을 풀고 실행시켜보세요
# 시작노드, 도착노드, 가중치
print(solution(0, 3, [[0, 1, 9], [0, 2, 3], [1, 0, 5], [2, 1, 1]]))  # 반환값 :0, 4, 3
print(solution(0, 4, [[0, 1, 1], [1, 2, 5], [2, 3, 1]]))  # 반환값 : 0, 1, 6, 7
