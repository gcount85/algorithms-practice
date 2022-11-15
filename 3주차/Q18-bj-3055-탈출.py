# https://www.acmicpc.net/problem/3055

import sys

R, C = map(int, sys.stdin.readline().split())  # 지도의 행, 열
지도 = []
for i in range(R):
    line = list(sys.stdin.readline().rstrip())
    지도.append(line)
    for j, v in enumerate(line):
        if v == 'S':
            start = (i, j)    # 시작 위치 알아내기
        if v == 'D':
            dst = (i, j)    # 도착 위치 알아내기
        if v == '*':
            water = (i, j)    # 물의 위치 알아내기
print(지도, start, dst, water)

def bfs(s: tuple, water: tuple, 지도: list):
    level = {s: 0, water: 0}      # 단계(level)은 몇 스텝만에 시작노드에서 해당 노드로 갈 수 있는지를 의미
    # parent = {s: None, water: 0}  # 특정 노드의 부모 노드(전 단계에 있던 노드)를 가리킴
    i = 1               # 단계를 나타낼 i (다음 단계를 탐색할 때마다 +1)
    frontier = [s]      # frontier는 각 레벨에서 탐색하게 될 노드(단계마다 바뀜)
    while frontier:     # 탐색할 노드가 존재하지 않을 때까지
        nexts = []      # 다음 단계에서 탐색할 노드를 담을 리스트 
        for u in frontier:          # frontier에 있는 시작노드 s에 대해
            edges = [(u[0]+1,u[1]), (u[0]-1,u[1]), (u[0],u[1]+1), (u[0],u[1]-1)]
            for v in edges:      
                if (0 <= v[0] <= R-1) and (0 <= v[1] <= C-1):  # 목적지 노드의 조건
                    stuff = 지도[v[0]][v[1]]
                    if (v not in level) and ((stuff == '.') or (stuff == 'D')):  
                        level[v] = i    # v의 레벨은 i단계
                        # parent[v] = u   # v의 부모 노드는 u
                        nexts.append(v) # 탐색할 다음 노드에 v를 추가 
        frontier = nexts    # 추가 된 다음 노드들을 frontier에 올림
        i += 1
    print(level)

bfs(start, water, 지도)