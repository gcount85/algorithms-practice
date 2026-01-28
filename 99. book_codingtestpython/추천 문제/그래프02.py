# https://school.programmers.co.kr/learn/courses/30/lessons/49190
# 이미 방문한 노드를 또 방문하면 그때 카운트 ++1


def solution(arrows):
    answer = 0
    visited = {(0, 0)}
    used_arrows = set()
    x = y = 0

    # 0~7: U, UR, R, DR, D, DL, L, UL
    dx = [0, 1, 1, 1, 0, -1, -1, -1]
    dy = [1, 1, 0, -1, -1, -1, 0, 1]
    for a in arrows:
        for _ in range(2):
            # print(cur_x, cur_y)
            nx, ny = x + dx[a], y + dy[a]
            if (nx, ny) in visited and (x, y, nx, ny) not in used_arrows:
                answer += 1
            visited.add((nx, ny))
            used_arrows.add((x, y, nx, ny))
            used_arrows.add((nx, ny, x, y))
            x, y = nx, ny

    return answer
