# 다익스트라

from collections import defaultdict
import heapq


def solution(start, num_nodes, edges):
    """
    1. 초기화: 우선순위 큐, 인접리스트
    2. 우선순위큐 빌 때까지:
        2-1. cur = pop
        2-2. stale entry
        2-3. 저장된 거리랑 new 거리 비교:
            2-4. 더 짧으면 갱신 && 힙 push
    """

    graph = defaultdict(list)
    for s, v, w in edges:
        graph[s].append((v, w))

    distances = [999999] * num_nodes
    pq = [(0, start)]  # 거리, 노드
    distances[0] = 0
    while pq:
        dist, cur = heapq.heappop(pq)
        if distances[cur] < dist:
            continue
        for d, w in graph[cur]:
            if distances[d] > dist + w:
                distances[d] = dist + w
                heapq.heappush(pq, (distances[d], d))

    return distances


# TEST 코드 입니다. 주석을 풀고 실행시켜보세요
# 시작노드, 도착노드, 가중치
print(solution(0, 3, [[0, 1, 9], [0, 2, 3], [1, 0, 5], [2, 1, 1]]))  # 반환값 :0, 4, 3
print(solution(0, 4, [[0, 1, 1], [1, 2, 5], [2, 3, 1]]))  # 반환값 : 0, 1, 6, 7
