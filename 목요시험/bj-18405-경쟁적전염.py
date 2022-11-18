# https://www.acmicpc.net/problem/18405


# 번호가 낮은 바이러스부터 bfs로 한 노드씩 탐색하게 하고 (단계를 비교하면서)
# S 단계 이후에 (x,y)에 어떤 parent가 연결되어 있는지 확인하면 될 거같음 


# 제출 못했어요 ㅠㅠ 

import sys

N, K = map(int, sys.stdin.readline().split())  # 시험관 행 , 바이러스 번호 
virus = []
virus_level = {}
virus_index = [[] for _ in range(K+1)]

for i in range(N):
    line = list(sys.stdin.readline().rstrip())
    virus.append(line)
    for j, v in enumerate(line):
        if 0 < v <= K:
            virus_index[K] = (i, j)   # k번까지 바이러스의 시작 위치 저장 

S, X, Y = map(int, sys.stdin.readline().split())  # S초 뒤, (X, Y)

def bfs_first(n: int, src: tuple, virus: list):
    virus_level = {src: (n, 0)}  # {노드 : (바이러스번호, 단계)}
    i = 1                       # 단계를 나타낼 i (다음 단계를 탐색할 때마다 +1)
    frontier = src              # frontier는 각 레벨에서 탐색하게 될 노드(단계마다 바뀜)
    while frontier:             # 탐색할 노드가 존재하지 않을 때까지
        nexts = []              # 다음 단계에서 탐색할 노드를 담을 리스트 
        for u in frontier:          
            edges = [(u[0]+1,u[1]), (u[0]-1,u[1]), (u[0],u[1]+1), (u[0],u[1]-1)]
            for v in edges:      
                if (0 <= v[0] <= N-1) and (0 <= v[1] <= N-1):  # 목적지 노드의 조건
                    if (v not in virus_level):   # 방문한 적 없을 때   
                        if (virus[v[0]][v[1]] == 0) and (v in virus_level.keys()):
                            if (virus_level[v] > i):  
                                virus_level[v] = i    # v의 레벨은 i단계
                                nexts.append(v)       # 탐색할 다음 노드에 v를 추가 
                    else:
                        virus_level[v] = i    # v의 레벨은 i단계
                        nexts.append(v) # 탐색할 다음 노드에 v를 추가 
        frontier = nexts    # 추가 된 다음 노드들을 frontier에 올림
        i += 1
    return virus_level

for n, v in enumerate(virus_index):
    if v != []:
        bfs_first(n, v, virus)  # v는 튜플
        # bfs_next(start, virus)

if (X, Y) in virus_level.keys():
    print(virus_level[(X, Y)])
else:
    print(0)