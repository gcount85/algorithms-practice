# https://www.acmicpc.net/problem/14888


import sys
sys.setrecursionlimit(10**9)

N = int(sys.stdin.readline().strip())
A = list(map(int, sys.stdin.readline().strip().split()))
operator = list(map(int, sys.stdin.readline().strip().split()))  # + - X ％;; 2 1 1 1 
노드의개수 = sum(operator)

edges = [[] for _ in range(노드의개수)]




for _ in range(M):
    src, dst = map(int, sys.stdin.readline().strip().split())
    edges[src].append(dst)  # 간선을 양방향으로 넣어주어야 정확함! 
    edges[dst].append(src)  

count = 0
parent = {}

def dfs_visit(s, edges):
    for v in edges[s]:
        if (v not in parent):     
            parent[v] = s
            dfs_visit(v, edges)

dfs_visit(N, edges)
print(count)