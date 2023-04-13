N = 10
parent = {}
frontier = []
M = [list(map(int, input().split())) for _ in range(N)]
height = 5
dir = [(-1, 0), (1, 0), (0, -1), (0, 1)]

# 조금 더 빠른 방법 (100ms 정도)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
while frontier:
    (x, y) = frontier.pop()
    for i in range(4):
        next_x = x + dx[i]
        next_y = y + dy[i]
        if (next_x < 0) or (next_x >= N) or (next_y < 0) or (next_y >= N):
            continue
        if ((next_x, next_y) in parent):
            continue
        if (M[next_x][next_y] <= height):
            continue
        parent[(next_x, next_y)] = True
        frontier.append((next_x, next_y))

# 가독성이 조금 더 나은 듯한 방법
while frontier:
    nexts = []
    for u in frontier:
        # 가능한 인덱스
        edges = [(u[0]+i[0], u[1]+i[1]) for i in dir
                 if (0 <= u[0]+i[0] and u[0]+i[0] < N)
                 and (0 <= u[1]+i[1] and u[1]+i[1] < N)]
        for v in edges:
            if (v not in parent) and (M[v[0]][v[1]] > height):
                parent[v] = u
                nexts.append(v)
    frontier = nexts
