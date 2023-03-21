# https://www.acmicpc.net/problem/3055

import sys

R, C = map(int, sys.stdin.readline().split())  # 지도의 행, 열
지도 = []
water = []
water_level = {}

for i in range(R):
    line = list(sys.stdin.readline().rstrip())
    지도.append(line)
    for j, v in enumerate(line):
        if v == 'S':
            start = (i, j)    # 시작 위치 알아내기
        if v == 'D':
            dst = (i, j)    # 도착 위치 알아내기
        if v == '*':
            water.append((i, j))    # 물의 위치 알아내기
# print("시작점:", start, "종착지:", dst, "물의위치:", water)

def bfs_for_고슴도치(s: tuple, 지도: list):
    level = {s: 0}      # 단계(level)은 몇 스텝만에 시작노드에서 해당 노드로 갈 수 있는지를 의미
    i = 1               # 단계를 나타낼 i (다음 단계를 탐색할 때마다 +1)
    frontier = [s]      # frontier는 각 레벨에서 탐색하게 될 노드(단계마다 바뀜)
    while frontier:     # 탐색할 노드가 존재하지 않을 때까지
        nexts = []      # 다음 단계에서 탐색할 노드를 담을 리스트 
        for u in frontier:           
            edges = [(u[0]+1,u[1]), (u[0]-1,u[1]), (u[0],u[1]+1), (u[0],u[1]-1)]
            for v in edges:      
                if (v not in level) and (0 <= v[0] <= R-1) and (0 <= v[1] <= C-1):  # 목적지 노드의 조건
                    stuff = 지도[v[0]][v[1]]
                    possible = ['.', 'D']
                    if (stuff in possible):
                        if (v in water_level.keys()):
                            if (water_level[v] > i):  
                                level[v] = i    # v의 레벨은 i단계
                                nexts.append(v) # 탐색할 다음 노드에 v를 추가 
                        else:
                            level[v] = i    # v의 레벨은 i단계
                            nexts.append(v) # 탐색할 다음 노드에 v를 추가 
        frontier = nexts    # 추가 된 다음 노드들을 frontier에 올림
        i += 1
    if dst in level.keys():
        print(level[dst])
    else:
        print("KAKTUS")

def bfs_for_water(water, 지도: list):
    water_level = {dst: 251}      # 단계(level)은 몇 스텝만에 시작노드에서 해당 노드로 갈 수 있는지를 의미
    for k in water:
        water_level[k] = 0
    i = 1               # 단계를 나타낼 i (다음 단계를 탐색할 때마다 +1)
    frontier = water      # frontier는 각 레벨에서 탐색하게 될 노드(단계마다 바뀜)
    while frontier:     # 탐색할 노드가 존재하지 않을 때까지
        nexts = []      # 다음 단계에서 탐색할 노드를 담을 리스트 
        for u in frontier:          
            edges = [(u[0]+1,u[1]), (u[0]-1,u[1]), (u[0],u[1]+1), (u[0],u[1]-1)]
            for v in edges:      
                if (0 <= v[0] <= R-1) and (0 <= v[1] <= C-1):  # 목적지 노드의 조건
                    stuff = 지도[v[0]][v[1]]
                    if (v not in water_level) and ((stuff == '.') or (stuff == 'S')):  
                        water_level[v] = i    # v의 레벨은 i단계
                        nexts.append(v) # 탐색할 다음 노드에 v를 추가 
        frontier = nexts    # 추가 된 다음 노드들을 frontier에 올림
        i += 1
    return water_level

if water != []:
    water_level = bfs_for_water(water, 지도)
bfs_for_고슴도치(start, 지도)