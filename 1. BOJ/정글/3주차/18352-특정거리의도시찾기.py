# https://www.acmicpc.net/problem/18352

import sys

N, M, K, X = map(int, sys.stdin.readline().split())
edges = [[] for _ in range(N+1)]
for _ in range(M):
    src, dst = map(int, sys.stdin.readline().split())
    edges[src].append(dst)  

def bfs(s, edges):
    level = {s: 0}      # 단계(level)은 몇 스텝만에 시작노드에서 해당 노드로 갈 수 있는지를 의미
    i = 1               # 단계를 나타낼 i (다음 단계를 탐색할 때마다 +1)
    frontier = [s]      # frontier는 각 레벨에서 탐색하게 될 노드(단계마다 바뀜)
    while frontier:     # 탐색할 노드가 존재하지 않을 때까지
        nexts = []      # 다음 단계에서 탐색할 노드를 담을 리스트 
        for u in frontier:          # frontier에 있는 시작노드 s에 대해
            for v in edges[u]:      
                if (v not in level):  
                    level[v] = i    # v의 레벨은 i단계
                    nexts.append(v) # 탐색할 다음 노드에 v를 추가 
                # if (v in level) and (level[v] > i):   → 이 두 라인 없어도 됨! BFS는 항상 최단 거리를 보장
                #     level[v] = i
        frontier = nexts    # 추가 된 다음 노드들을 frontier에 올림
        i += 1
    # print(level)
    if ans := [k for k, v in level.items() if v == K]:
        ans.sort()
        for i in ans:
            print(i)
    else:
        print(-1)

bfs(X, edges)   # X를 1로 넣어서 계속 틀렸었다...ㅡㅡ 문제좀 잘 읽자
