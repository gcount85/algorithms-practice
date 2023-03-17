# https://www.acmicpc.net/problem/9663
# N-Queen 문제는 크기가 N × N인 체스판 위에 퀸 N개를 서로 공격할 수 없게 놓는 문제
# 23-1-17 문제점; promising한지 판단할때 완전히 걸러지지 않음 -> 더 철저하게 컬럼마다 각 조건을 검사하도록..


import sys


def dfs_visit(r: int, edges: list):  # r == 퀸을 두기 위해 탐색하는 행
    global count
    if r == N:
        count += 1
        return
    # 지금까지 두었던 자리들과 비교
    for col in range(N):    # 컬럼 탐색
        edges[r] = col
        for i in range(r):
            positioned = edges[i]
            if col == positioned:
                break
            elif (abs(r-i)) == (abs(col-positioned)):
                break
        dfs_visit(r+1, edges)


def dfs(N):
    global edges
    for c in range(N):    # 시작점 세팅하기 - 각각의 컬럼에 대해; 0, 1, 2
        edges[0] = c      # 0,0부터 시작
        dfs_visit(1, edges)  # 다음 행에 대해서 둘 곳 탐색


N = int(sys.stdin.readline())
edges = [0] * N  # -1로 초기화
count = 0


dfs(N)
print(count)
