# https://www.acmicpc.net/problem/11725

import sys

N = int(sys.stdin.readline())
edges = [[] for _ in range(N+1)]
for _ in range(N-1):
    src, dst = map(int, sys.stdin.readline().split())
    edges[src].append(dst)  
    edges[dst].append(src)  # 양방향이기에 이 라인 없이 윗 라인만 있으면 오답

parent = {1: None}          # 부모 노드를 지정해줌으로써 이미 방문했는지 아닌지 판별
def dfs_visit(s, edges):
    for v in edges[s]:      # 시작 노드의 목적지 노드들에 대해서
        if v not in parent: # 목적지 노드의 부모노드가 지정되지 않았다면(이전에 방문 안 했으면)
            parent[v] = s   # 시작 노드를 해당 노드의 부모노드로 지정 
            dfs_visit(v, edges) # 해당 목적지 노드를 대상으로 재귀

dfs_visit(1, edges)
sort_parent = sorted(list(parent.items()))
for i in sort_parent:
    if i[0] > 1:
        print(i[1])
