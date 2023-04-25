# https://www.acmicpc.net/problem/1012

import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**4)

def dfs_visit(i, j, field, visited, n, m):
    # 재귀적으로 dfs_visit 
    for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        nx = i + dx
        ny = j + dy
        if (nx >= n) or (ny >= m):
            continue
        if (nx < 0) or (ny < 0):
            continue
        # print("좌표 :", (nx, ny), "ny > m ? ", ny == m, "m?", m)
        if field[nx][ny] == 0 or (nx, ny) in visited:
            continue
        visited[(nx, ny)] = 1
        dfs_visit(nx, ny, field, visited, n, m)


def dfs(field, n, m):
    count = 0
    visited = {}
    for i in range(n):
        for j in range(m):
            if field[i][j] == 0 or (i, j) in visited:
                continue
            # 시작 노드를 바꿔서 dfs visit
            dfs_visit(i, j, field, visited, n, m)
            visited[(i, j)] = 1
            count += 1
    return count

for _ in range(int(input())):
    m, n, k = map(int, input().split())
    field = [[0] * m for _ in range(n)]
    for _ in range(k):
        x, y = map(int, input().split())
        field[y][x] = 1
    print(dfs(field, n, m))
        


