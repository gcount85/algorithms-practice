# https://school.programmers.co.kr/learn/courses/30/lessons/62050
# bfs?

from collections import deque


def is_valid(n, nx, ny):
    if nx < 0 or ny < 0 or nx >= n or ny >= n:
        return False
    return True


def find_cands(height, land, row, col, now_height):
    direction = [[1, 0], [0, 1], [-1, 0], [0, -1]]
    cands = []
    for x, y in direction:
        nx, ny = row + x, col + y
        if not is_valid(len(land), nx, ny):
            continue
        diff = abs(land[nx][ny] - now_height)
        need_cost = diff if diff > height else 0
        cands.append((nx, ny, need_cost, False))
    return set(cands)


def solution(land, height):
    """
    1. 최솟값 변수, 큐 초기화. 큐에 저장할 상태는 (현재 위치, 현재 비용, 갈 수 있는 곳들(행열, 사다리여부))
    2. ? 아무칸에서 출발하니까 모든 노드에서 다 bfs 돌려야 하나?
    2. 큐가 빌 때까지
        2-1. 현재위치, 현재비용, 갈수있는 곳들(행,열, 사다리여부) = 큐 pop
        2-2. 갈수있는 노드들에 대해서:
            2-2-1. 이미 방문했으면?: pass
            2-2-2. 사다리있으면 비용 0, 사다리 필요하면 비용 추가해서 append
            2-2-3. visited 표기
            2-2-4. 갈수있는 곳들에서 지금 노드 뺀 다음에, 사방 추가해서 또 추가
    3. 탐색 종료 후 현재비용, 최솟값 업뎃
    4. 최솟값 리턴

    """

    n = len(land)
    for row, lst in enumerate(land):
        for col, now_height in enumerate(lst):
            minimum = 99999999
            cands = find_cands(
                height, land, row, col, now_height
            )  # nx, ny, 필요비용, 사다리여부
            queue = deque([(row, col, 0, cands)])
            visited = {(row, col, 0, frozenset(cands))}
            while queue:
                now_x, now_y, cur_cost, now_cands = queue.popleft()
                for nxt_x, nxt_y, need_cost, has_ladder in now_cands:
                    #         # 방문처리
                    if (nxt_x, nxt_y, need_cost, frozenset(now_cands)) in visited:
                        continue
                    nxt_cands = find_cands(
                        height, land, nxt_x, nxt_y, land[nxt_x][nxt_y]
                    )
                    nxt_cands.update(now_cands)
                    nxt_cands.remove((nxt_x, nxt_y, need_cost, has_ladder))
                    queue.append(
                        (
                            nxt_x,
                            nxt_y,
                            cur_cost + (need_cost if not has_ladder else 0),
                            nxt_cands,
                        )
                    )
                    visited.add(
                        (nxt_x, nxt_y, need_cost, has_ladder, frozenset(nxt_cands))
                    )
                # break
            minimum = min(cur_cost, minimum)

    answer = 0
    return answer
