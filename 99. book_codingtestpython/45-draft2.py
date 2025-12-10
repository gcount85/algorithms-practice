# https://school.programmers.co.kr/learn/courses/30/lessons/67259
# 다익스트라 - exit 까지의 최단 거리. 88점


import heapq


def solution(board):
    """
     1. start, exit 초기화
     2. 우선순위 큐, cost 배열 초기화: (비용, start 위치) 저장, start 위치의 cost는 0
     3. 우선순위 큐가 빌 때까지:
         3-1. 현재 cost, 위치, dir = 큐 pop
         3-2. cost 배열이랑 현재 cost 비교: 현재 cost가 더 크면 continue
         3-3. 현재위치에서 갈 수 있는 위치에 대해서:
             3-3-1. dir에 따라 추가되는 비용 결정
             3-3-2. cost 배열이랑 현재 cost + 추가 비용을 비교:
                 3-3-2-1. 갱신
                 3-3-2-2. heappush
    4. return cost[exit위치]
    """

    n = len(board)
    start = (0, 0)
    pq = [(0, start, None)]  # 현재 cost, 위치, 방향
    INF = float("inf")
    cost = [[INF] * n for _ in range(n)]
    cost[0][0] = 0
    dir = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    while pq:
        cur_cost, (cur_x, cur_y), prev_dir = heapq.heappop(pq)
        if cur_cost > cost[cur_x][cur_y]:
            continue

        for x, y in dir:
            nx, ny = cur_x + x, cur_y + y
            if nx < 0 or ny < 0 or nx >= n or ny >= n or board[nx][ny] == 1:
                continue

            new_cost = 100
            if prev_dir is not None and prev_dir != (x, y):  # 꺾이는 도로
                new_cost += 500

            if cost[nx][ny] >= cur_cost + new_cost:
                cost[nx][ny] = cur_cost + new_cost
                heapq.heappush(pq, (cur_cost + new_cost, (nx, ny), (x, y)))

    # print(cost)
    return cost[n - 1][n - 1]
