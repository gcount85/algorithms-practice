# https://school.programmers.co.kr/learn/courses/30/lessons/159993
# 2회 복습 38분 solved

from collections import deque


def solution(maps):
    """
    1. maps 순회하면서 S, L, E 찾음
    2. 큐, visited 초기화: 큐에 저장할 상태 (현재 노드, 레버 상태, 거리)
    3. 큐가 빌 때까지:
        3-1. cur, 레버상태, 거리 = 큐 pop
        3-2. cur가 exit고 레버상태 true 면: 거리 반환
        3-3. cur가 갈 수 있고 방문 가능한 노드들에 대해서:
            3-3-1. lever면 레버상태 true, 거리 + 1, 넥스트 노드 위치를 큐에 저장 && 방문 체크
    """

    row = len(maps)
    col = len(maps[0])
    for i in range(row):
        for j in range(col):
            if maps[i][j] == "S":
                start = (i, j)
            elif maps[i][j] == "L":
                lever = (i, j)
            elif maps[i][j] == "E":
                end = (i, j)

    visited = [
        [[-1, -1] for _ in range(col)] for _ in range(row)
    ]  # x, y, 레버상태 true/false
    q = deque([(start, False, 0)])
    visited[start[0]][start[1]][1] = 1  # 시작 지점 레버상태 false로 체크
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    # print(visited)
    # visited = {(start, False)}

    while q:
        cur_node, lever_on, cur_dist = q.popleft()
        if cur_node == end and lever_on:
            return cur_dist

        for x, y in directions:
            nx, ny = cur_node[0] + x, cur_node[1] + y
            if nx < 0 or ny < 0 or nx >= row or ny >= col or maps[nx][ny] == "X":
                continue
            if visited[nx][ny][0 if lever_on else 1] == 1:
                continue
            # if ((nx, ny), lever_on) in visited:
            #     continue
            next_node = (nx, ny)
            found_lever = lever_on or next_node == lever
            q.append((next_node, found_lever, cur_dist + 1))
            visited[nx][ny][0 if found_lever else 1] = 1
            # visited.add(((nx, ny), found_lever))
    return -1
