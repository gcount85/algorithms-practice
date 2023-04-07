# https://www.acmicpc.net/problem/11724

import sys
sys.setrecursionlimit(10**9)

N, M = map(int, sys.stdin.readline().strip().split())
edges = [[] for _ in range(N+1)]
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

# dfs 함수는 단절된 그래프, 강하게 연결된 그래프가 아닌 경우에 시작 노드를 바꿔 모든 그래프를 탐색하기 위함
def dfs(N, edges):
    global count
    for s in range(1,N+1):  # 모든 노드들에 대해 
        if s not in parent: # 이미 방문된 노드가 아니라면
            parent[s] = None # '부모 없음'을 뜻하는 None; dfs_visit을 시작할 노드이기 때문
            count += 1
            dfs_visit(s, edges)

dfs(N, edges)
print(count)