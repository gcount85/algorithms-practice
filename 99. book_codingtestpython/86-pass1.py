# https://school.programmers.co.kr/learn/courses/30/lessons/150365
# 그리디

import sys

sys.setrecursionlimit(10**6)


def is_in_map(n, m, x, y):
    if x < 1 or y < 1 or x > n or y > m:
        return False
    return True


def is_possible_path(remain, dist):
    if dist > remain:
        return False
    if (remain - dist) % 2 != 0:
        return False
    return True


def solution(n, m, x, y, r, c, k):
    path = []
    direction = [(1, 0, "d"), (0, -1, "l"), (0, 1, "r"), (-1, 0, "u")]

    # 거리만큼 움직이면서 유망여부 판단
    for step in range(1, k + 1):
        remain = k - step
        moved = False

        for i, j, ch in direction:
            nx, ny = x + i, y + j
            if not is_in_map(n, m, nx, ny):
                continue
            if is_possible_path(remain, abs(nx - r) + abs(ny - c)):
                moved = True
                x, y = nx, ny
                path.append(ch)
                break

        if not moved:
            return "impossible"

    return "".join(path)
