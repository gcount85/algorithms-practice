# https://www.acmicpc.net/problem/2468

"""
어떤 지역의 높이 정보 → 물에 잠기지 않는 안전한 영역은 최대 몇개?
내리는 비의 양에 따라 일정한 높이 이하의 모든 지점은 물에 잠김
어떤 지역의 높이 정보: 2^N * 2^N 배열
배열의 각 원소는 해당 지점의 높이를 표시하는 자연수
안전한 영역이란 물에 잠기지 않는 지점들이 "상하좌우"로 인접하면서 그 크기가 최대인 영역

어떤 지역을 나타내는 2차원 배열의 행과 열의 개수를 나타내는 수 N (2 <= N <= 100)
둘째 줄부터 N개의 줄에 2차원 배열의 첫 번째 행부터 N번째 행까지 순서대로 한 행씩 높이 정보
1 <= 높이 <= 100 정수

"""

import sys


def bfs_visit(s: tuple, parent, height):
    """
    height 보다 큰 값을 갖는 노드만 갈 수 있음 

    """


def bfs(N, max_h, min_h, 최대갯수):
    if (min_h == max_h):
        최대갯수 = max(1, 최대갯수)
        return

    height = min_h
    parent = {}
    count = 0
    for i in range(N):
        for j in range(N):
            if ((i, j) not in parent) and (M[i][j] > height):
                parent[(i, j)] = None
                bfs_visit((i, j), parent, height)
                count += 1
    최대갯수 = max(count, 최대갯수)
    bfs(N, max_h, min_h + 1, 최대갯수)


input = sys.stdin.readline
N = int(input())
M = []
edges = [(-1, 0), (1, 0), (0, -1), (0, 1)]
max_h = 0
min_h = 0
최대갯수 = 0
for _ in range(N):
    temp = list(map(int, input().split()))
    for i in temp:
        max_h = max(max_h, i)
        min_h = min(min_h, i)
    M.append(temp)

bfs(N, max_h, min_h, 최대갯수)

"""
전형적인 bfs 탐색
"""
