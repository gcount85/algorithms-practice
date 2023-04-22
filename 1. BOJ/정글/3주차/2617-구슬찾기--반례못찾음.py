# https://www.acmicpc.net/problem/2617

import sys
sys.setrecursionlimit(10**6)


N, M = map(int, sys.stdin.readline().split())
edges1 = [[] for _ in range(N+1)]
edges2 = [[] for _ in range(N+1)]

for _ in range(M):
    src, dst = map(int, sys.stdin.readline().split())
    if dst not in edges1[src]:
        edges1[src].append(dst)  
    if src not in edges2[dst]:
        edges2[dst].append(src)  
# print(edges1, edges2)

count = 0
count_dict = dict.fromkeys(range(1,N+1), 0)

def dfs_visit(s, edges, parent):
    global count
    for v in edges[s]:      # 시작 노드의 목적지 노드들에 대해서
        count += 1
        if v not in parent: # 목적지 노드의 부모노드가 지정되지 않았다면(이전에 방문 안 했으면)
            parent[v] = s   # 시작 노드를 해당 노드의 부모노드로 지정 
            dfs_visit(v, edges, parent) # 해당 목적지 노드를 대상으로 재귀


ans = 0
# dfs 함수는 단절된 그래프, 강하게 연결된 그래프가 아닌 경우에 시작 노드를 바꿔 모든 그래프를 탐색하기 위함
def dfs(N, edges):
    global count, ans
    parent = {}          # 부모 노드를 지정해줌으로써 이미 방문했는지 아닌지 판별
    for s in range(1,N+1):  # 모든 노드들에 대해 
        count = 0
        dfs_visit(s, edges, parent)
        if count >= (N//2)+1:
            ans += 1
    # print(count_dict)


dfs(N, edges1)
dfs(N, edges2)

# for v in count_dict.values():
#     if v >= (N//2)+1:
#         ans += 1
print(ans)