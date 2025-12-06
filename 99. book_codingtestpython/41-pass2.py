from collections import defaultdict


def solution(num_vertices, edges, source):
    """
    1. 인접 리스트 초기화, 시작 노드 거리 초기화
    2. 간선 횟수만큼 반복:
        1-1. 노드 순회:
            1-1-2. 도착 노드 v들에 대해서:
                1-1-2-1. distance[d] 가 distance[s]+ v의 w 둘 중 작은 값으로 d의 거리값 갱신
    3. 음의 싸이클 조사(노드를 한번 더 순회해서 값이 갱신되는지 본다)
        3-1. 노드 순회:
            3-1-1. 도착 노드 v들에 대해서:
                3-1-2. distance[v]가 distance[u] + w 보다 크다?: 음의 싸이클 존재
    """

    INF = float("inf")
    distances = [INF] * num_vertices
    distances[source] = 0
    graph = defaultdict(list)
    for s, d, w in edges:
        graph[s].append((d, w))

    for _ in range(num_vertices - 1):
        for s in range(num_vertices):
            for v, w in graph[s]:
                # distances[v] = min(distances[v], distances[s] + w)
                if distances[s] != INF and distances[v] > distances[s] + w:
                    distances[v] = distances[s] + w

    for s in range(num_vertices):
        for v, w in graph[s]:
            if distances[v] > distances[s] + w:
                return -1

    return distances


print(
    solution(
        5,
        [
            [0, 1, 4],
            [0, 2, 3],
            [0, 4, -6],
            [1, 3, 5],
            [2, 1, 2],
            [3, 0, 7],
            [3, 2, 4],
            [4, 2, 2],
        ],
        0,
    )
)  # [0, -2, -4, 3, -6]

print(
    solution(
        4,
        [[0, 1, 5], [0, 2, -1], [1, 2, 2], [2, 3, -2], [3, 0, 2], [3, 1, 6]],
        0,
    )
)  # -1
