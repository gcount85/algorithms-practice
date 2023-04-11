# https://www.acmicpc.net/problem/7576

import sys
from collections import deque

"""

정수 1은 익은 토마토, 
정수 0은 익지 않은 토마토, 
정수 -1은 토마토가 들어있지 않은 칸

- 출력
    - 토마토가 모두 익을 때까지의 최소 날짜
    - 저장될 때부터 모든 토마토가 익어있는 상태이면 0을 출력
    - 토마토가 모두 익지는 못하는 상황이면 -1을 출력
"""

input = sys.stdin.readline

M, N = map(int, input().split())
rotten_tomato = deque([])
tomato_box = []
empty_grid = 0

for i in range(N):
    temp = list(map(int, input().split()))
    for j in range(M):
        if temp[j] == 1:
            rotten_tomato.append(((i, j), 0))
        if temp[j] == -1:
            empty_grid += 1
    tomato_box.append(temp)

# print(rotten_tomato)

all_tomato_count = M*N - empty_grid

if (len(rotten_tomato) == all_tomato_count):
    print(0)
else:

    visited = {}
    level = 0

    while rotten_tomato:
        cur_grid, level = rotten_tomato.popleft()
        visited[cur_grid] = level
        for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            nx, ny = cur_grid[0]+dx, cur_grid[1]+dy
            if not (0 <= nx < N and 0 <= ny < M):
                continue
            if (nx, ny) in visited or tomato_box[nx][ny] == -1:
                continue
            rotten_tomato.append(((nx, ny), level+1))
            visited[(nx, ny)] = level+1

    # print(rotten_tomato)
    # print(all_tomato_count)
    # print(visited)

    if len(visited.keys()) != all_tomato_count:
        print(-1)
    else:
        print(level)
