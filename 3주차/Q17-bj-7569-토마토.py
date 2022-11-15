# https://www.acmicpc.net/problem/7569


import sys

M, N, H = map(int, sys.stdin.readline().split())  # 가로길이M, 세로길이N, 높이H
tmt_boxes = []
if H == 1:
    tmt_boxes = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
else:
    for _ in range(H):
        box = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
        tmt_boxes.append(box)
print(tmt_boxes)

def bfs(s: tuple, tmt_boxes: list):
    level = {s: 0}      # 단계(level)은 몇 스텝만에 시작노드에서 해당 노드로 갈 수 있는지를 의미
    parent = {s: None}  # 특정 노드의 부모 노드(전 단계에 있던 노드)를 가리킴
    i = 1               # 단계를 나타낼 i (다음 단계를 탐색할 때마다 +1)
    frontier = [s]      # frontier는 각 레벨에서 탐색하게 될 노드(단계마다 바뀜)
    while frontier:     # 탐색할 노드가 존재하지 않을 때까지
        nexts = []      # 다음 단계에서 탐색할 노드를 담을 리스트 
        for u in frontier:          # frontier에 있는 시작노드 s에 대해
            edges = [(u[0]+1,u[1]), (u[0]-1,u[1]), (u[0],u[1]+1), (u[0],u[1]-1)]
            for v in edges:      
                if (0 <= v[0] <= N-1) and (0 <= v[1] <= M-1):  # 목적지 노드의 조건
                    if (v not in level) and (tmt_boxes[v[0]][v[1]] == 1):  
                        level[v] = i    # v의 레벨은 i단계
                        parent[v] = u   # v의 부모 노드는 u
                        nexts.append(v) # 탐색할 다음 노드에 v를 추가 
        frontier = nexts    # 추가 된 다음 노드들을 frontier에 올림
        i += 1
    print(level[(N-1,M-1)]+1)

bfs((0, 0), tmt_boxes)

