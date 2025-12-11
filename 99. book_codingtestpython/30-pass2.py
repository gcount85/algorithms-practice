# https://school.programmers.co.kr/learn/courses/30/lessons/159993?language=python3
# 1회 복습 50분 solved

from collections import deque


def bfs(maps, start, exit, lever):
    row = len(maps)
    col = len(maps[0])
    found_lever = False
    visited = {(start, found_lever)}
    queue = deque([(start, 0, found_lever)])

    while queue:
        cur, dist, lever_state = queue.popleft()
        if cur == exit and lever_state:
            return dist
        for x, y in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            nx, ny = cur[0] + x, cur[1] + y
            if nx < 0 or nx >= row or ny < 0 or ny >= col:
                continue
            if ((nx, ny), lever_state) not in visited and maps[nx][ny] != "X":
                visited.add(((nx, ny), lever_state or (nx, ny) == lever))
                queue.append(((nx, ny), dist + 1, lever_state or (nx, ny) == lever))
    return -1


def solution(maps):
    """
    1. maps를 순회하면서 s, e, l를 찾는다.
    2. bfs를 구현한다.
        2-1. s에서 시작하고 l이 켜진 상태에서 e에 도착했을 때의 distance를 반환
        2-2. s 초기화, 큐 초기화, visited(discovered) 초기화
            2-2-1. visited에 s를 먼저 담고, (좌표, distance, lever 상태)
            2-2-2. 큐에는 s의 이웃애들을 담는다.
        2-3. 큐에 빌 때까지 반복:
            2-3-1. 큐에서 노드 하나 뺌
            2-3-2. 현재 노드 == e && 레버가 켜진 상태이면: distance 반환
            2-3-3. 현재 노드의 이웃들에 대해서(이웃은 상하좌우 좌표):
                2-3-3-1. 갈 수 있고 visited에 없으면: (좌표, distance, lever 상태) 확정 && visited 체크
                2-3-3-2. 큐에 추가
        2-4. -1 반환
    """

    row = len(maps)
    col = len(maps[0])

    for i in range(row):
        for j in range(col):
            cur = maps[i][j]
            if cur == "S":
                start = (i, j)
            if cur == "E":
                exit = (i, j)
            if cur == "L":
                lever = (i, j)

    return bfs(maps, start, exit, lever)
