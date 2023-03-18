# https://www.acmicpc.net/problem/9663
# N-Queen 문제는 크기가 N × N인 체스판 위에 퀸 N개를 서로 공격할 수 없게 놓는 문제

import sys


def promising(r):
    for i in range(r):
        if edges[r] == edges[i]:
            return False
        elif (abs(r-i)) == (abs(edges[r]-edges[i])):
            return False
    return True


def dfs_visit(r: int):  # r == 퀸을 두기 위해 탐색하는 행
    global count
    if r == N:
        count += 1
        return
    # 지금까지 두었던 자리들과 비교
    for col in range(N):    # 컬럼 탐색
        edges[r] = col
        if promising(r) == True:
            dfs_visit(r+1)


N = int(sys.stdin.readline())
count = 0
edges = [-1] * N  # -1로 초기화

dfs_visit(0)

print(count)
