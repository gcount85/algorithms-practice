# https://school.programmers.co.kr/learn/courses/30/lessons/150365
# 백트래킹. 추가 가지치기가 핵심.

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

    def dfs(cur_x, cur_y):
        # ✅ 가지치기: 남은 이동으로 도착 불가면 컷
        if not is_possible_path(k - len(path), abs(r - cur_x) + abs(c - cur_y)):
            return None

        if len(path) == k:
            if (cur_x, cur_y) == (r, c):
                return True
            else:
                return False

        # 사방으로 가본다
        for x1, y1, d in direction:
            nx, ny = cur_x + x1, cur_y + y1
            if not is_in_map(n, m, nx, ny):
                continue
            path.append(d)
            if dfs(nx, ny):
                return "".join(path)
            path.pop()
        return False

    start_dist = abs(r - x) + abs(c - y)
    if start_dist > k or (k - start_dist) % 2 != 0:
        return "impossible"
    answer = dfs(x, y)

    return answer if answer else "impossible"
