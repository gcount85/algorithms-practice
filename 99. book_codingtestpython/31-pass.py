# https://school.programmers.co.kr/learn/courses/30/lessons/92343
# 2회 복습 - BFS
# 58분 solved (with 힌트)

from collections import deque, defaultdict


def solution(info, edges):
    """
    1. edges로 인접 리스트 만들기
    2. 최대 양의 수, 큐, visited 초기화
        2-1. root만 세팅
        2-2. 저장할 상태는 (현재 노드 번호, 현재 양의 수, 현재 늑대 수, 갈 수 있는 노드들)
    3. 큐가 빌 때까지:
        3-1. 큐 pop
        3-2. 현재 위치가 루트면 최대 양의 수 update
        3-3. 현재 위치에서 갈 수 있는 모든 노드들에 대해서:
            3-3-1. 방문했으면 pass
            3-3-2. 양의 수 = 늑대 수가 같아지면 pass
            3-3-3. 큐에 저장 && 방문 체크
    """
    graph = defaultdict(list)
    for source, dest in edges:
        graph[source].append(dest)
    start_cand = frozenset(graph[0])  # ⚠️ 시작 상태에서 갈 수 있는 모든 노드들
    queue = deque([(1, 0, start_cand)])  # 양의 수, 늑대 수, 갈 수 있는 모든 노드들
    max_sheep = 1
    visited = {(1, 0, start_cand)}

    while queue:
        cur_sheep, cur_wolf, candidates = queue.popleft()
        max_sheep = max(cur_sheep, max_sheep)

        for nxt in candidates:  # ⚠️ 일반 BFS와 달리 상태에 저장 된 candidates를 순회
            nxt_sheep = cur_sheep + (1 if info[nxt] == 0 else 0)
            nxt_wolf = cur_wolf + (0 if info[nxt] == 0 else 1)
            if nxt_sheep == nxt_wolf:
                continue

            # ⚠️ 다음 후보에서 nxt 를 제거한다.
            nxt_cand = set(candidates)
            nxt_cand.update(graph[nxt])
            nxt_cand.remove(nxt)
            nxt_cand = frozenset(nxt_cand)
            if (nxt_sheep, nxt_wolf, nxt_cand) in visited:
                continue
            queue.append((nxt_sheep, nxt_wolf, nxt_cand))
            visited.add((nxt_sheep, nxt_wolf, nxt_cand))

    return max_sheep
