# https://school.programmers.co.kr/learn/courses/30/lessons/62050

import heapq

"""
1. (1,1) 위치에서 시작
2. 주변에 갈 수 있는 곳 중 diff, 위치를 힙에 담아
3. 힙에서 하나 뽑아
4. 방문 안 했으면 거길 가고 2-4를 반복 
"""


def is_valid(n, nx, ny):
    if nx < 0 or ny < 0 or nx >= n or ny >= n:
        return False
    return True


def solution(land, height):
    n = len(land)
    answer = 0
    pq = [(0, 0, 0)]  # 비용, x, y
    visited = set()
    direc = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    while pq:
        diff, cur_x, cur_y = heapq.heappop(pq)
        if (cur_x, cur_y) in visited:
            continue
        visited.add((cur_x, cur_y))
        answer += 0 if diff <= height else diff
        for x, y in direc:
            nx, ny = cur_x + x, cur_y + y
            if is_valid(n, nx, ny):
                height_diff = abs(land[nx][ny] - land[cur_x][cur_y])
                heapq.heappush(pq, (height_diff, nx, ny))
    return answer
