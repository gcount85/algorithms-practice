from collections import deque
import sys
# 노드의 개수와 간선의 개수를 입력 받기
V, E = map(int, sys.stdin.readline().split())

# 모든 노드에 대한 진입차수(indgree)는 0으로 초기화
indegree = [0] * (V + 1)

#각 노드에 연결된 간선 정보를 담기 위한 연결리스트 초기화
edges = [[] for _ in range(V + 1)]

# 방향 그래프의 모든 간선 정보를 입력 받기
for _ in range(E):
    src, dst = map(int, sys.stdin.readline().split())
    edges[src].append(dst)   # 정점 src에서 dst 노드로 이동 가능
    # 진입차수를 1 증가
    indegree[dst] += 1



def topology_sort():
    result = []
    q = deque()
    # 모든 노드를 방문하며 진입차수가 0인 노드를 큐에 삽입
    for v in range(v, V+1): 
        if indegree[v] == 0:
            q.append(v)
    # 큐가 빌 때까지 반복
    while q:
        # 큐에서 원소 꺼내기
        now = q.popleft()
        result.append(now)
        # 해당 원소와 연결된 노드들의 진입차수에서 1 빼기
        for i in edges[now]:
            indegree[i] -= 1
            # 새롭게 진입차수가 0이 되는 노드를 큐에 삽입
            if indegree[i] == 0:
                q.append(i)
    
    # 위상 정렬을 수행한 결과 출력
    for i in result:
        print(i, end=' ')

topology_sort()