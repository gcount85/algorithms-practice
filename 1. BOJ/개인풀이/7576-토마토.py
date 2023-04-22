# https://www.acmicpc.net/problem/7576

import sys
from collections import deque


def main():
    """
    정수 1은 익은 토마토,
    정수 0은 익지 않은 토마토,
    정수 -1은 토마토가 들어있지 않은 칸

    - 출력
        - 토마토가 모두 익을 때까지의 최소 날짜
        - 저장될 때부터 모든 토마토가 익어있는 상태이면 0을 출력
        - 토마토가 모두 익지는 못하는 상황이면 -1을 출력
    """

    input = sys.stdin.readline

    M, N = map(int, input().split())
    tomato_box = [list(map(int, input().split())) for _ in range(N)]
    ripen_tomato = deque()

    unripe_tomato = 0
    for i in range(N):
        for j in range(M):
            if tomato_box[i][j] == 1:
                ripen_tomato.append((i, j, 0))
            elif tomato_box[i][j] == 0:
                unripe_tomato += 1

    if (unripe_tomato == 0):
        print(0)
    else:
        level = 0

        while ripen_tomato:
            x, y, level = ripen_tomato.popleft()

            for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                nx, ny = x + dx, y + dy
                if not (0 <= nx < N and 0 <= ny < M):
                    continue
                if tomato_box[nx][ny] == -1 or tomato_box[nx][ny] == 1:
                    continue
                ripen_tomato.append((nx, ny, level+1))
                tomato_box[nx][ny] = 1
                unripe_tomato -= 1

        # print(ripen_tomato)

        print(level if unripe_tomato == 0 else -1)


if __name__ == '__main__':
    main()
