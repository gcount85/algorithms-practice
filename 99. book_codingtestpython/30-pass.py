from collections import deque


def bfs(ways, lever, start, target):
    q = deque()
    q.append((start, False, 0))
    visited = set([(start, False)])

    while q:
        now, found_lever, dist = q.popleft()

        if now == target and found_lever is True:
            return dist

        for node in ways[now]:
            if (node, found_lever) not in visited:
                state = found_lever or (node == lever)  # discovering 과정에서 상태 감지
                visited.add((node, state))  # 큐에 넣는 순간 방문처리(중복 방지)
                q.append((node, state, dist + 1))  # 한 칸 이동했으니 +1

    return -1


def solution(maps):
    row = len(maps)
    col = len(maps[0])

    ways = {}
    for i in range(row):
        for j in range(col):
            # 주요 스팟을 검색하여 좌표를 찾는다.
            now = maps[i][j]
            if now == "S":
                start = (i, j)
            elif now == "E":
                exit_ = (i, j)
            elif now == "L":
                lever = (i, j)

            if now == "X":
                ways[(i, j)] = []
                continue

            # 각각의 좌표에서 갈 수 있는 이웃 노드를 추가한다.
            way = []
            up, down, right, left = (i - 1, j), (i + 1, j), (i, j + 1), (i, j - 1)

            if up[0] >= 0 and maps[up[0]][up[1]] != "X":
                way.append(up)
            if down[0] < row and maps[down[0]][down[1]] != "X":
                way.append(down)
            if right[1] < col and maps[right[0]][right[1]] != "X":
                way.append(right)
            if left[1] >= 0 and maps[left[0]][left[1]] != "X":
                way.append(left)

            ways[(i, j)] = way

    return bfs(ways, lever, start, exit_)
