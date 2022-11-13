import sys
sys.setrecursionlimit(10**9)

N, M = map(int, sys.stdin.readline().strip().split())
edges = [[] for _ in range(N+1)]
for _ in range(M):
    src, dst = map(int, sys.stdin.readline().strip().split())
    edges[src].append(dst)  # 간선을 양방향으로 넣어주어야 정확함! 
    edges[dst].append(src)  
# print(edges)

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
    for s in range(1,N+1):
        if s not in parent:
            parent[s] = None
            count += 1
            dfs_visit(s, edges)

dfs(N, edges)
print(count)