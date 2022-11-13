# 첫째 줄에 정점의 개수 N(1 ≤ N ≤ 1,000),
# 간선의 개수 M(1 ≤ M ≤ 10,000), 
# 탐색을 시작할 정점의 번호 V

import sys
import heapq

N, M, V = map(int, sys.stdin.readline().split())
edges = [[] for _ in range(N+1)]
for _ in range(M):
    src, dst = map(int, sys.stdin.readline().split())
    edges[src].append(dst)
    edges[src].sort()
print(edges)

# 첫째 줄에 DFS를 수행한 결과를, 그 다음 줄에는 BFS를 수행한 결과

def bfs(s, edges):
    level = {s: 0}      # 단계(level)은 몇 스텝만에 시작노드에서 해당 노드로 갈 수 있는지를 의미
    parent = {s: None}  # 특정 노드의 부모 노드(전 단계에 있던 노드)를 가리킴
    i = 1               # 단계를 나타낼 i (다음 단계를 탐색할 때마다 +1)
    frontier = [s]      # frontier는 각 레벨에서 탐색하게 될 노드(단계마다 바뀜)
    print(s, end=' ')
    while frontier:     # 탐색할 노드가 존재하지 않을 때까지
        nexts = []      # 다음 단계에서 탐색할 노드를 담을 리스트 
        for u in frontier:          # frontier에 있는 시작노드 s에 대해
            for v in edges[u]:      # 그 시작노드가 가진 엣지들의 목적지 노드에 대해 
                if v not in level:  # 목적지 노드가 level에 없다면
                    level[v] = i    # v의 레벨은 i단계
                    parent[v] = u   # v의 부모 노드는 u
                    print(v, end=' ')
                    nexts.append(v) # 탐색할 다음 노드에 v를 추가 
        frontier = nexts    # 추가 된 다음 노드들을 frontier에 올림
        i += 1

bfs(V, edges)
