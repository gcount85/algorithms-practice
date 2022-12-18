# https://www.acmicpc.net/problem/9663
# N-Queen 문제는 크기가 N × N인 체스판 위에 퀸 N개를 서로 공격할 수 없게 놓는 문제

import sys


def dfs_visit(r, edges):  # r == 퀸을 두기 위해 탐색하는 행
    global count
    if r == N:
        return 
    for col in range(N):    # 컬럼 탐색
        for i, v in enumerate(edges[:r]):   # 지금까지 두었던 자리들과 비교
            if (v == col):  # 두려고 하는 행 보다 위에, 같은 줄에 위치한 경우
                continue
            if (abs(r-i) == abs(col-v)):  # 대각선에 위치한 경우
                continue
            else:
                edges[r] = col
                # print(edges)
                dfs_visit(r+1, edges)
    if (r == N):
        count += 1


def dfs(N):
    global edges
    for c in range(N):    # 시작점 세팅하기 - 각각의 컬럼에 대해; 0, 1, 2
        edges[0] = c      # 0,0부터 시작
        dfs_visit(1, edges)  # 다음 행에 대해서 둘 곳 탐색


N = int(sys.stdin.readline())
count = 0
edges = [-1] * N  # -1로 초기화

dfs(N)

print(count)
