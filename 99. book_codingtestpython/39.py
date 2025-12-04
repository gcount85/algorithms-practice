from collections import deque, defaultdict


def solution(graph, start):
    """
    1. 큐, visited 초기화. start를 큐, visited에 넣고 시작.
    2. while 큐 빌 때까지 반복:
        2-1. 현재 노드 = 큐 pop
        2-2. 큐의 인접 노드 순회:
            2-2-1. visited에 체크 안 됐으면 큐 append
    """
    graph_dict = defaultdict(list)
    for s, d in graph:
        graph_dict[s].append(d)

    queue = deque([start])
    visited = {start}
    answer = []
    while queue:
        cur = queue.popleft()
        answer.append(cur)
        for node in graph_dict.get(cur, []):
            if node not in visited:
                visited.add(node)
                queue.append(node)

    return answer


print(
    solution(
        [
            (1, 2),
            (1, 3),
            (2, 4),
            (2, 5),
            (3, 6),
            (3, 7),
            (4, 8),
            (5, 8),
            (6, 9),
            (7, 9),
        ],
        1,
    )
)  # [1, 2, 3, 4, 5, 6, 7, 8, 9]


print(
    solution(
        [(0, 1), (1, 2), (2, 3), (3, 4), (4, 5), (5, 0)],
        1,
    )
)  # [1, 2, 3, 4, 5, 0]
