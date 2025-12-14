# https://school.programmers.co.kr/learn/courses/30/lessons/67259
# 2회 복습 30분 solved


import heapq


def solution(board):
    n = len(board)
    INF = 99999999
    dir = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    # x, y, 4방향 가격을 저장할 cost 배열 구현 [x][y][dir]
    cost = [[[INF, INF, INF, INF] for _ in range(n)] for _ in range(n)]
    pq = [(0, 0, 0, None)]

    while pq:
        cur_cost, cur_x, cur_y, prev_dir = heapq.heappop(pq)
        if prev_dir != None and cur_cost > cost[cur_x][cur_y][prev_dir]:
            continue

        for di, (x, y) in enumerate(dir):
            nx, ny = cur_x + x, cur_y + y
            if nx < 0 or ny < 0 or nx >= n or ny >= n or board[nx][ny] == 1:
                continue

            plus_cost = 500 if prev_dir != None and prev_dir != di else 0
            new_cost = cur_cost + 100 + plus_cost

            if cost[nx][ny][di] > new_cost:
                cost[nx][ny][di] = new_cost
                heapq.heappush(pq, (new_cost, nx, ny, di))

    return min(cost[n - 1][n - 1])
