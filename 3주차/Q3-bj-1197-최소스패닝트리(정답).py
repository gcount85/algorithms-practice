import sys
import heapq

V, E = map(int, sys.stdin.readline().split())  # 노드 개수, 엣지 개수
covered = [0] * (V+1)                          # 방문한 노드들 리스트 
edges = [[] for _ in range(V+1)]               # 엣지를 담을 리스트 
sum_min_w = 0                                  # 최소 가중치의 합 

for e in range(E):
    src, dst, weight = map(int, sys.stdin.readline().split())   # 소스노드, 목적지노드, 가중치
    edges[src].append((weight, dst))    # 양방향이기 때문에 둘 다 추가
    edges[dst].append((weight, src))    # 가중치로 최소 힙을 만들어야하므로 가중치를 0 인덱스에 삽입 

min_heap = [(0, 1)]      # (가중치, 목적지노드) 튜플을 담을 우선순위 큐(최소힙)
while min_heap:
    node = heapq.heappop(min_heap)    # min_heap의 최소값을 pop
    if not covered[node[1]]:     # 목적지 노드를 방문한 적 없다면 
        covered[node[1]] = 1     # 방문한 노드에 해당 목적지 노드를 체크
        sum_min_w += node[0]     # 가중치 합에 가중치를 추가 
        for n in edges[node[1]]: # 목적지 노드를 소스 노드로 삼는 모든 (가중치, 목적지노드)를 최소 힙에 추가
            heapq.heappush(min_heap, n)  

print(sum_min_w)
