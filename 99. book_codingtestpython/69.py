"""
https://school.programmers.co.kr/learn/courses/30/lessons/120861
[0, 0]은 board의 정 중앙
예를 들어 board의 가로 크기가 9라면 캐릭터는 왼쪽으로 최대 [-4, 0]까지 오른쪽으로 최대 [4, 0]까지 이동할 수 있습니다.
"""


def solution(keyinput, board):
    direction = {"up": [0, 1], "down": [0, -1], "left": [-1, 0], "right": [1, 0]}
    w, h = board
    w_max = (w - 1) // 2
    h_max = (h - 1) // 2
    now_x, now_y = 0, 0
    for k in keyinput:
        x, y = direction[k]
        nx, ny = now_x + x, now_y + y
        if abs(nx) > w_max or abs(ny) > h_max:
            continue
        now_x, now_y = nx, ny

    return [now_x, now_y]
