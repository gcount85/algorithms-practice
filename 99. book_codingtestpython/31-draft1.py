# https://school.programmers.co.kr/learn/courses/30/lessons/92343?language=python3

from collections import deque, defaultdict


def build_tree(edges):
    tree = defaultdict(list)
    for s, d in edges:
        tree[s].append(d)
    return tree


def solution(info, edges):
    """
    1. 트리를 만든다.
    2. 양의 최대 갯수 초기화, 큐랑 visited에 현재 노드 담기
    3. 루트부터 bfs
        3-1. 큐에 노드가 없을 때까지:
        3-1. 큐에서 현재 노드 pop
        3-2. maxSheep 업데이트
        3-3. 현재 노드의 인접 노드들 순회:
        3-3-1. 모은 양의 수보다 늑대의 수가 같지 않으면 해당 노드를 큐에 담기 && visited 체크
            큐에 담을 상태: (노드번호, 그때까지의 양 수, 늑대 수)
    4. maxsheep 리턴
    """

    tree = build_tree(edges)
    max_sheep = 1
    start_candidates = frozenset(tree[0])
    visited = {
        (0, max_sheep, 0, start_candidates)
    }  # 노드 번호, 현재 양 수, 현재 늑대 수, candidates
    queue = deque([(0, max_sheep, 0, start_candidates)])

    while queue:
        now, sheep_count, wolf_count, candidates = queue.popleft()
        max_sheep = max(max_sheep, sheep_count)

        for n in candidates:
            is_sheep = info[n] == 0
            ns = sheep_count + 1 if is_sheep else sheep_count
            nw = wolf_count + 1 if not is_sheep else wolf_count
            if ns == nw:
                continue

            next_cands = set(candidates)
            next_cands.remove(n)
            for child in tree[n]:
                next_cands.add(child)
            next_cands = frozenset(next_cands)

            state = (n, ns, nw, next_cands)
            if state in visited:
                continue
            queue.append(state)
            visited.add(state)

    return max_sheep
