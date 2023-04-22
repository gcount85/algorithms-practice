# https://www.acmicpc.net/problem/1916


import sys

N = int(sys.stdin.readline())  # 도시의 개수
M = int(sys.stdin.readline())  # 버스의 개수
edges = [{} for _ in range(N+1)]    
for _ in range(M):
    src, dst, weight = map(int, sys.stdin.readline().split())
    if dst in edges[src].keys():  
        if edges[src][dst] > weight:
            edges[src][dst] = weight  
    else:
        edges[src][dst] = weight  
A, B = map(int, sys.stdin.readline().split())  # 출발지점, 도착지점

def bfs(s, edges):
    level = {s[0]: 0}      # 단계(level)은 몇 스텝만에 시작노드에서 해당 노드로 갈 수 있는지를 의미
    weight = {s[0]: 0}     # 각 노드까지 도달하는데 드는 최소 비용 
    i = 1               # 단계를 나타낼 i (다음 단계를 탐색할 때마다 +1)
    frontier = [s]      # frontier는 각 레벨에서 탐색하게 될 노드(단계마다 바뀜)
    while frontier:     # 탐색할 노드가 존재하지 않을 때까지
        nexts = []      # 다음 단계에서 탐색할 노드를 담을 리스트 
        for u in frontier:          # frontier에 있는 시작노드들에 대해
            for v in edges[u[0]].items():  #v: (2, 5)     
                if (v[0] not in level):  
                    level[v[0]] = i    # v의 레벨은 i단계
                    weight[v[0]] = weight[u[0]] + v[1]
                    nexts.append(v) # 탐색할 다음 노드에 v를 추가 
                if (v[0] in level) and (weight[v[0]] > weight[u[0]] + v[1]):
                    weight[v[0]] = weight[u[0]] + v[1]
                    nexts.append(v) # 탐색할 다음 노드에 v를 추가 ## 이 라인 추가 안해서 계속 틀림 ㅠㅠㅠㅠㅠ
        frontier = nexts    # 추가 된 다음 노드들을 frontier에 올림
        i += 1
    print(weight[B])

bfs((A,0), edges)  
