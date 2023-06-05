"""
- BFS
- 동일한 사이즈의 정답 행렬 미리 생성
- 최단 거리를 확인한 후, 정답 행렬의 동일 인덱스에 담기 
- 입력
    - 목표지점이 항상 바뀔 가능성이 있음

- 출력 
    - 원래 갈 수 없는 땅인 위치는 0을 출력 (출발 지점, 0으로 막혀있는 지점)
    - 원래 갈 수 있는 땅인 부분 중에서 도달할 수 없는 위치는 -1을 출력 (0은 아니지만 갈 수 없는 지점)

"""

from sys import stdin
from collections import deque

DIRECTIONS = [(0, 1), (0, -1), (1, 0), (-1, 0)]

def bfs(input_map, sx, sy):
    queue = deque([(sx, sy, 0)])
    output_map[sx][sy] = 0

    while queue:
        x, y, dist = queue.popleft()
        for xdir, ydir in DIRECTIONS:
            nx = x + xdir
            ny = y + ydir 
            if (nx < 0 or ny < 0 or nx > n-1 or ny > m-1):
                continue 
            if (output_map[nx][ny] != -1):
                continue
            if (input_map[nx][ny] == 0):
                output_map[nx][ny] = 0
                continue
            output_map[nx][ny] = dist + 1
            queue.append((nx, ny, dist + 1))
    return output_map

n, m = map(int, stdin.readline().split())
input_map = [list(map(int, stdin.readline().split())) for _ in range(n)]
output_map = [[-1] * m for _ in range(n)] # false로 초기화하면 원래 갈수 없는 벽(0)을 확인할 때 에러


for i, row in enumerate(input_map):
    for j, value in enumerate(row):
        if value == 2:
            sx, sy = i, j
        if value == 0:
            output_map[i][j] = 0

for i in bfs(input_map, sx, sy):
    print(*i)




