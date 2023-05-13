# https://www.acmicpc.net/problem/16236

import sys
from typing import Tuple    # 시간이 더 소요되지만 가독성을 위해 추가해봄
from collections import deque


def bfs_visit(N, pos_shark, shark_size, aquarium) -> Tuple[tuple, int]:
    '''
    현 상어 위치에서 가장 가까운 먹을 수 있는 물고기의 위치와, 거기까지의 거리 반환
    - 가장 가깝게 먹을 수 있는 물고기: 상어보다 크기가 작음
    '''

    edge_queue = deque([(pos_shark, 0)])
    targets = []
    visited = set()
    visited.add(pos_shark)  # 방문체크

    while edge_queue:
        pos, dist = edge_queue.popleft()  # 시작노드

        candidate = [(pos[0]-1, pos[1]), (pos[0], pos[1]-1),
                     (pos[0], pos[1]+1), (pos[0]+1, pos[1])]

        for x, y in candidate:
            if x < 0 or y < 0:
                continue
            if x > N-1 or y > N-1:
                continue
            if (x, y) in visited:
                continue
            if aquarium[x][y] <= shark_size:
                edge_queue.append(((x, y), dist+1))
                visited.add((x, y))  # 추가하자마자 방문 체크하면 더 효율적
                if 0 < aquarium[x][y] < shark_size:  # 먹을 수 있는 물고기들
                    targets.append(((x, y), dist+1))

    if targets == []:
        return None, 0

    targets.sort(key=lambda x: (x[1], x[0][0], x[0][1]))
    return targets[0]


def solution(N, pos_shark, aquarium):
    '''
    타겟 물고기까지의 거리를 누적 계산하고, 
    상어 사이즈, 상어 위치를 업데이트함
    그 위치에서 다시 다음 bfs를 통해 다음 타겟 위치를 알아냄 
    '''

    shark_size = 2
    distance = 0
    eaten_fish = 0

    while True:
        target_pos, dist = bfs_visit(N, pos_shark, shark_size, aquarium)

        if target_pos == None:
            break

        distance += dist

        eaten_fish += 1
        if eaten_fish == shark_size:
            shark_size += 1
            eaten_fish = 0

        aquarium[target_pos[0]][target_pos[1]] = 0
        pos_shark = target_pos

    print(distance)


def main():
    input = sys.stdin.readline

    N = int(input())

    aquarium = []
    pos_shark = None

    for i in range(N):
        temp = list(map(int, input().split()))
        for j, v in enumerate(temp):
            if v == 9:
                pos_shark = (i, j)
                temp[j] = 0
        aquarium.append(temp)

    # print(aquarium, pos_shark)

    solution(N, pos_shark, aquarium)


if __name__ == "__main__":
    main()

'''
- 요약
    - 크기가 같은 칸은 지나가기만 가능
    - 크기가 작은 칸은 지나가기, 먹기 가능 -> 먹으면 빈칸이 됨
    - 자신의 크기만큼의 개수의 물고기를 먹을 때 마다 크기가 1 증가
    - 가장 가까운 거리의 물고기부터 먹음 (위, 왼쪽부터)
- 리턴
    - 먹을 수 있는 모든 물고기를 먹는데까지 이동한 횟수
- 풀이
    - 위->왼 순으로 순회하도록
    - 상어 크기 변수
    - 후퇴할 때도 거리를 측정해야 함 
    - 누적된 레벨이 거리? 
'''
