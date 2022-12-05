# https://www.acmicpc.net/problem/9663
# N-Queen 문제는 크기가 N × N인 체스판 위에 퀸 N개를 서로 공격할 수 없게 놓는 문제

import sys

N = int(sys.stdin.readline())

# 8*8, (1,1)부터 시작 
edges = [[0] * N for _ in range(N)] 
count = 0
parent = {}          # 부모 노드를 지정해줌으로써 이미 방문했는지 아닌지 판별
def dfs_visit(tup: tuple):
    r = tup[0] # 행
    c = tup[1] # 열
    for i, v in enumerate(edges):
        for j, k in enumerate(v):
            if (i == r):
                continue
            if (j == c):
                continue
            if (i-r == j-c):
                continue
            else:
                edges[i][k] = 1
    for v in edges:      
        if (v == 1): # 목적지 노드의 부모노드가 지정되지 않았다면(이전에 방문 안 했으면)
            dfs_visit(v, edges) # 해당 목적지 노드를 대상으로 재귀


# dfs 함수는 단절된 그래프, 강하게 연결된 그래프가 아닌 경우에 시작 노드를 바꿔 모든 그래프를 탐색하기 위함
def dfs(N, edges):
    for r in range(N):  # 모든 노드들에 대해 
        for c in range(N): 
            dfs_visit((r,c))
            # if n번째 줄까지 도달했으면 count += 1


