# https://school.programmers.co.kr/learn/courses/30/lessons/92343
# 3회 복습 - BFS
# 25분 solved

from collections import deque, defaultdict


def solution(info, edges):
    graph = defaultdict(list)
    for p, c in edges:
        graph[p].append(c)

    max_sheep = 1
    candidates = set(graph[0])
    # print(candidates)
    queue = deque(
        [(1, 0, candidates)]
    )  # 현재 양 숫자, 현재 늑대 숫자, 갈 수 있는 노드 집합
    while queue:
        cur_sheep, cur_wolf, cands = queue.popleft()
        if cur_sheep > max_sheep:
            # print("현재 노드:", cur, "현재 양수:", cur_sheep)
            max_sheep = max(cur_sheep, max_sheep)
        for nxt in cands:
            nxt_sheep = cur_sheep + (1 if info[nxt] == 0 else 0)
            nxt_wolf = cur_wolf + (1 if info[nxt] == 1 else 0)
            if nxt_wolf >= nxt_sheep:
                continue
            nxt_cands = set(cands)
            nxt_cands.update(graph[nxt])
            nxt_cands.remove(nxt)
            queue.append((nxt_sheep, nxt_wolf, nxt_cands))
    return max_sheep
