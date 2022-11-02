# https://itcrowd2016.tistory.com/76

import sys

dir = [[-1, 0], [0, 1], [1, 0], [0, -1]]


def bfs(start):
    que = []
    que.append(start)
    map_b[start[0]][start[1]] = 0
    while que:
        cur = que.pop(0)
        for k in range(4):
            nr = cur[0] + dir[k][0]
            nc = cur[1] + dir[k][1]
            if nr < 0 or nr >= N or nc < 0 or nc >= N:
                continue
            if map_b[nr][nc] == 0:
                continue
            que.append([nr, nc])
            map_b[nr][nc] = 0


N = int(sys.stdin.readline())
map = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
maxT = 0
ans = 0

# 가장 높은 지대 찾기
for i in range(N):
    for j in range(N):
        maxT = max(maxT, map[i][j])
if maxT == 1:  # 최대 영역이 1이라면 전체가 한덩이이므로 답은 1
    ans = 1
else:
    for day in range(maxT+1):
        map_b = [[0]*N for _ in range(N)]
        for i in range(N):
            for j in range(N):
                # 잠긴부분 :0 /잠기지 않은 부분 :1 로 나눔
                map_b[i][j] = 1 if map[i][j] >= day else 0
        # for row in map_b:
        #     print(row)

        cnt = 0  # 안전영역 갯수
        for i in range(N):
            for j in range(N):
                if map_b[i][j] == 1:
                    bfs([i, j])  # bfs로 탐색한 횟수를 알아내서 영역 개수 탐색
                    cnt += 1
        ans = max(ans, cnt)
print(ans)
