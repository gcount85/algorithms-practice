# 14분 solved
# https://school.programmers.co.kr/learn/courses/30/lessons/1844?language=python3

from collections import deque


def solution(maps):
    """
    1. maps 스팟 초기화: start = (0,0), target = (n-1, m-1)
    2. 큐, visited 초기화: 큐, visited에 start, distance 노드 추가
    3. 큐가 빌 때까지 bfs:
        3-1. cur = 큐 pop
        3-2. 큐가 target이면 distance를 반환
        3-3. cur의 이웃들에 대해서:
            3-4. 방문 가능하면: 큐에 거리 + 1 append, visited에 체크
    4. return -1
    """

    row = len(maps)
    col = len(maps[0])
    start = (0, 0)
    target = (row - 1, col - 1)
    queue = deque([(start, 1)])
    visited = {start}
    while queue:
        cur, dist = queue.popleft()
        if cur == target:
            return dist
        for x, y in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            nx, ny = cur[0] + x, cur[1] + y
            if nx < 0 or ny < 0 or nx >= row or ny >= col:
                continue
            if maps[nx][ny] == 0 or (nx, ny) in visited:
                continue
            queue.append(((nx, ny), dist + 1))
            visited.add((nx, ny))
    return -1
