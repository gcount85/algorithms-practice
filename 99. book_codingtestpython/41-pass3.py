def solution(num_vertices, edges, source):
    """
    1. distances 초기화
    2. 간선 개수만큼 반복:
        2-1. 노드 1번부터 n번까지 반복:
            2-2. i번 노드에서 갈 수 있는 이웃들에 대해 거리가 더 짧아졌으면 갱신
    3. 2-1, 2-2를 한 번 더 반복해서 거리가 짧아진 게 있으면 return -1
    """

    INF = float("inf")
    distances = [INF for _ in range(num_vertices)]
    distances[source] = 0
    length = len(edges)

    for _ in range(length):
        updated = False
        for s, d, w in edges:
            if distances[d] > distances[s] + w:
                distances[d] = distances[s] + w
                updated = True
        if not updated:
            break

    for _ in range(num_vertices):
        for s, d, w in edges:
            if distances[d] > distances[s] + w:
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
