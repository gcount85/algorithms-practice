# https://www.acmicpc.net/problem/7569

import sys

M, N, H = map(int, sys.stdin.readline().split())  # 가로길이M, 세로길이N, 높이H
tmt_boxes = []
ripe_tmt = []
nn = 0
for i in range(H):
    box = []
    for j in range(N):
        tmp = list(map(int, sys.stdin.readline().split()))
        box.append(tmp)
        for idx, rt in enumerate(tmp):
            if rt == 1:
                ripe_tmt.append((i, j, idx))    # 익은 토마토 위치 알아내기
            elif rt == -1:
                nn += 1         # -1의 갯수 알아내기 → 최종적으로 익지 못한 토마토 알아내기 위함
    tmt_boxes.append(box)


def bfs(s: list, tmt_boxes: list):
    level = {}      # 단계(level)은 몇 스텝만에 시작노드에서 해당 노드로 갈 수 있는지를 의미
    for rt in s:
        level[rt] = 0      # 단계(level)은 몇 스텝만에 시작노드에서 해당 노드로 갈 수 있는지를 의미
    i = 1               # 단계를 나타낼 i (다음 단계를 탐색할 때마다 +1)
    frontier = s      # frontier는 각 레벨에서 탐색하게 될 노드(단계마다 바뀜)
    while frontier:     # 탐색할 노드가 존재하지 않을 때까지
        nexts = []      # 다음 단계에서 탐색할 노드를 담을 리스트
        for u in frontier:          # frontier에 있는 시작노드 s에 대해
            edges = [(u[0]+1, u[1], u[2]), (u[0]-1, u[1], u[2]), (u[0], u[1]+1, u[2]),
                     (u[0], u[1]-1, u[2]), (u[0], u[1], u[2]+1), (u[0], u[1], u[2]-1)]
            for v in edges:
                if (0 <= v[0] <= H-1) and (0 <= v[1] <= N-1) and (0 <= v[2] <= M-1):  # 목적지 노드의 조건
                    if (v not in level) and (tmt_boxes[v[0]][v[1]][v[2]] == 0):
                        level[v] = i    # v의 레벨은 i단계
                        nexts.append(v)  # 탐색할 다음 노드에 v를 추가
        frontier = nexts    # 추가 된 다음 노드들을 frontier에 올림
        i += 1
    if (M*N*H) - len(level) - nn != 0:      # 전체칸수 - 익은 토마토수 - (-1갯수) = 익지 못한 토마토수
        print(-1)
    else:
        print(max(level.values()))      # 다 익는데 걸린 시간 = 가장 마지막 단계 수


bfs(ripe_tmt, tmt_boxes)
