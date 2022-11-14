# https://www.acmicpc.net/problem/21606
import sys
sys.setrecursionlimit(10**9)

N = int(sys.stdin.readline())
A = list(map(int, list(sys.stdin.readline().strip())))
edges = [[] for _ in range(N+1)]
for _ in range(N-1):
    src, dst = map(int, sys.stdin.readline().split())
    edges[src].append(dst)  
    edges[dst].append(src)  # 양방향이기에 이 라인이 없으면 오답

adj_outdoors = 0
path = 0
def dfs_visit_in_to_in(s, edges, visited):
    global path
    for v in edges[s]:      # 시작 노드의 목적지 노드들에 대해서
        if v not in visited: # 목적지 노드의 부모노드가 지정되지 않았다면(이전에 방문 안 했으면)
            visited[v] = s   # 시작 노드를 해당 노드의 부모노드로 지정 
            if A[v-1] == 1:  # 실내다
                path += 1
                

def dfs_visit_out_to_out(s, edges, visited):
    global adj_outdoors
    for v in edges[s]:      # 시작 노드의 목적지 노드들에 대해서
        if v not in visited: # 목적지 노드의 부모노드가 지정되지 않았다면(이전에 방문 안 했으면)
            visited[v] = s   # 시작 노드를 해당 노드의 부모노드로 지정 
            if A[v-1] == 0:  # 실외다
                dfs_visit_out_to_out(v, edges, visited) # 해당 목적지 노드를 대상으로 재귀
            else:
                adj_outdoors += 1

# dfs 함수는 단절된 그래프, 강하게 연결된 그래프가 아닌 경우에 시작 노드를 바꿔 모든 그래프를 탐색하기 위함
def dfs(N, edges):
    global path, adj_outdoors

    for s in range(1,N+1):  # 모든 노드들에 대해 
        visited = {}
        if (s not in visited) and (A[s-1] == 1): # 이미 방문된 노드가 아니고 실내일때 
            visited[s] = None   # '부모 없음'을 뜻하는 None으로 저장; dfs_visit을 시작할 노드이기 때문
            dfs_visit_in_to_in(s, edges, visited)

    visited = {}
    for s in range(1,N+1):  # 모든 노드들에 대해 
        if (s not in visited) and (A[s-1] == 0): # 이미 방문된 노드가 아니고 실외일때
            visited[s] = None   # '부모 없음'을 뜻하는 None으로 저장; dfs_visit을 시작할 노드이기 때문
            dfs_visit_out_to_out(s, edges, visited)
            path += (adj_outdoors * (adj_outdoors - 1))
        adj_outdoors = 0

dfs(N, edges)
print(path)