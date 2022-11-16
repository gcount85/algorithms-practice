# https://www.acmicpc.net/problem/2617

import sys
sys.setrecursionlimit(10**6)


N, M = map(int, sys.stdin.readline().split())
edges1 = [[] for _ in range(N+1)]
edges2 = [[] for _ in range(N+1)]

for _ in range(M):
    src, dst = map(int, sys.stdin.readline().split())
    edges1[src].append(dst)  
    edges2[dst].append(src)  

count = 0
count_dict = dict.fromkeys(range(1,N+1), 0)

def dfs_visit(s, edges):
    global count
    for v in edges[s]:      # 시작 노드의 목적지 노드들에 대해서
        count += 1
        # if v not in parent: # 목적지 노드의 부모노드가 지정되지 않았다면(이전에 방문 안 했으면)
        # parent[v] = s   # 시작 노드를 해당 노드의 부모노드로 지정 
        dfs_visit(v, edges) # 해당 목적지 노드를 대상으로 재귀

# dfs 함수는 단절된 그래프, 강하게 연결된 그래프가 아닌 경우에 시작 노드를 바꿔 모든 그래프를 탐색하기 위함
def dfs(N, edges):
    global count
    # parent = {}          # 부모 노드를 지정해줌으로써 이미 방문했는지 아닌지 판별
    for s in range(1,N+1):  # 모든 노드들에 대해 
        # if s not in parent: # 이미 방문된 노드가 아니라면
        count = 0
        # parent[s] = None   # '부모 없음'을 뜻하는 None으로 저장; dfs_visit을 시작할 노드이기 때문
        dfs_visit(s, edges)
        if count_dict[s] < count:
            count_dict[s] = count
    # print(count_dict)


dfs(N, edges1)
dfs(N, edges2)

ans = 0
for v in count_dict.values():
    if v >= (N//2+1):
        ans += 1
print(ans)