# https://www.acmicpc.net/problem/1707

import sys
sys.setrecursionlimit(10**6)

def dfs_visit(s, edges):
    for v in edges[s]:      # 시작 노드의 목적지 노드들에 대해서
        if v not in parent: # 목적지 노드의 부모노드가 지정되지 않았다면(이전에 방문 안 했으면)
            parent[v] = s   # 시작 노드를 해당 노드의 부모노드로 지정
            if color[s] == 0:
                color[v] = 1
            else:
                color[v] = 0
            dfs_visit(v, edges) # 해당 목적지 노드를 대상으로 재귀
        else:
            if color[s] == color[v]:    # 색이 서로 같으면 result에 1을 추가
                result.append(1)

# dfs 함수는 단절된 그래프, 강하게 연결된 그래프가 아닌 경우에 시작 노드를 바꿔 모든 그래프를 탐색하기 위함
def dfs(N, edges):
    global parent
    for s in range(1,N+1):  # 모든 노드들에 대해 
        if s not in parent: # 이미 방문된 노드가 아니라면
            parent[s] = None   # '부모 없음'을 뜻하는 None으로 저장; dfs_visit을 시작할 노드이기 때문
            color[s] = 0
            dfs_visit(s, edges)
    if 1 in result:
        print("NO")
    else:
        print("YES")
        

K = int(sys.stdin.readline())   #테스트 케이스 개수
for _ in range(K):
    color = {}          # 1, 0으로 색을 표시 
    result = []
    parent = {}          # 부모 노드를 지정해줌으로써 이미 방문했는지 아닌지 판별
    V, E = map(int, sys.stdin.readline().split())
    edges = [[] for _ in range(V+1)]
    for _ in range(E):
        src, dst = map(int, sys.stdin.readline().split())
        edges[src].append(dst)  
        edges[dst].append(src)  # 양방향이기에 이 라인 없이 윗 라인만 있으면 오답
    dfs(V, edges)
