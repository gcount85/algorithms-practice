# https://school.programmers.co.kr/learn/courses/30/lessons/159993

"""
출발 지점에서 먼저 레버가 있는 칸으로 이동하여 레버를 당긴 후 미로를 빠져나가는 문이 있는 칸으로 이동하면 됩니다.
칸 수 10만
"""
from collections import deque


def solution(maps):
    """
    1. maps로 각 노드마다 갈 수 있는 길 저장
    2. S, L, E 위치 저장
    3. s->l 카운트, 최소 카운트 초기화
    4. [반복] S에서 시작해서 L에 도착할 때까지
        4-1. 이동할 때마다 count ++1
    5. [반복] L에서 E에 도착할 때까지
        5-1. 이동할 때마다 count ++1
    6. 4 , 5번에서 계산된 최소 카운트 반환
    """

    row = len(maps)
    col = len(maps[0])
    ways = {}
    for i in range(row):
        for j in range(col):
            now = maps[i][j]
            if now == "S":
                start = (i, j)
            if now == "E":
                exit = (i, j)
            if now == "L":
                lever = (i, j)

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

    lever_count = 0

    # s에서 l까지 도착하는 최소 횟수 구하기
    now = start
    to_visited = deque(ways[now])
    count = 0
    while len(to_visited) > 0:
        if maps[now[0]][now[1]] == "L":
            break
        for n in ways[now]:
            to_visited.extend(ways[n])
        now = to_visited.popleft()
        count += 1

    # l에서 e까지 도착하는 최소 횟수 구하기
    while len(to_visited) > 0:
        if maps[now[0]][now[1]] == "E":
            break
        for n in ways[now]:
            to_visited.extend(ways[n])
        now = to_visited.popleft()
        count += 1

    print(count)
    return count
