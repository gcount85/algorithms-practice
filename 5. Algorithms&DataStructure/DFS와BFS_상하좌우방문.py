
N = 10
s = (0, 0)  # 시작 위치

visited = [[False] * N for _ in range(N)]
visited[s[0]][s[1]] = True
q = []

while q:
    cur, dist = q.pop(0)
    for dx, dy in [(-1, 0), (0, -1), (0, 1), (1, 0)]:
        nx, ny = cur[0] + dx, cur[1] + dy
        if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
            q.append((nx, ny))
