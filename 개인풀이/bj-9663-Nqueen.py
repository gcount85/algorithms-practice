# https://www.acmicpc.net/problem/9663
# N-Queen 문제는 크기가 N × N인 체스판 위에 퀸 N개를 서로 공격할 수 없게 놓는 문제

import sys

N = int(sys.stdin.readline())
count = 0
def dfs_visit(r, c, edges):  # 0,0
    global count
    if r < N:
        for col in range(N):
            if (col in edges[:r]):
                continue
            for i, e in enumerate(edges[:r]):
                if (r-c == i-e):
                    continue
                else:
                    edges[r] = col
                    break
            if edges[r] == -1:
                return
            dfs_visit(r+1, col, edges)
    # if r == N:
        # count += 1
        # return

def dfs(N):
    for r in range(N):  # 모든 노드들에 대해 
        for c in range(N): 
            edges = [-1] * N  # 8*8, (0, 0)부터 시작 
            edges[r] = c
            dfs_visit(r+1, c, edges) # 0,0 // 0,1 // ... 

dfs(N)

print(count)