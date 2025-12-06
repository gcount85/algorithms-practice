def solution(num_vertices, edges, source):
    """
    1. 시작 노드 거리 초기화
    2. 간선 횟수만큼 반복:
        2-1. 모든 간선들에 대해서:
            2-1-1. distance[d] 가 distance[s]+ v의 w 둘 중 작은 값으로 d의 거리값 갱신
    3. 음의 싸이클 조사(노드를 한번 더 순회해서 값이 갱신되는지 본다)
        3-1. 모든 간선들에 대해서:
            3-1-1. distance[v]가 distance[u] + w 보다 크다?: 음의 싸이클 존재
    """

    INF = float("inf")
    distances = [INF] * num_vertices
    distances[source] = 0
    # ⚠️ 간선만 조사하면 되는 거라 굳이 인접 리스트 만들 필요 X

    for _ in range(num_vertices - 1):  # O(N) * O(E)
        updated = False  # ⚠️ 조기 종료를 위한 업데이트 플래그
        for s, v, w in edges:
            if (
                distances[s] != INF and distances[v] > distances[s] + w
            ):  # distance[s] 가 INF라는 건 start -> s까지 아직 경로가 존재하지 않음.
                # 따라서 start -> s -> v를 계산하는 게 의미 없음
                distances[v] = distances[s] + w
                updated = True
        if not updated:
            break

    for s, v, w in edges:  # O(E)
        if distances[s] != INF and distances[v] > distances[s] + w:
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
