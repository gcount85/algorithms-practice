# https://school.programmers.co.kr/learn/courses/30/lessons/92345
"""
1. 시작 위치 초기화
    1-1. 둘이 위치 같으면 이동횟수 1로 종료
2. 게임 시작
    2-1. a가 valid 한 곳으로 이동, 이동횟수 ++1, 이전 위치 발판 제거
        2-1-1. 갈 곳 없으면 return
    2-2. b가 valid 한 곳으로 이동, 이동횟수 ++1, 이전 위치 발판제거
        2-2-1. 갈 곳 없으면 return
    2-3. dfs
    2-4. a, b 위치, 이동횟수 원상복구

"""


def dfs(answer, direction, row, col, board, aloc, bloc, cur_move):
    if board[aloc[0]][aloc[1]] == 0:
        answer[0] = min(cur_move, answer[0])
        return
    if board[bloc[0]][bloc[1]] == 0:
        answer[0] = min(cur_move, answer[0])
        return

    # A 위치 정함
    a_cands = []
    for x, y in direction:
        a_nx, a_ny = aloc[0] + x, aloc[1] + y
        if a_nx < 0 or a_ny < 0 or a_nx >= row or a_ny >= col or board[a_nx][a_ny] == 0:
            continue
        a_cands.append((a_nx, a_ny))
    if not a_cands:
        answer[0] = min(cur_move, answer[0])
        return

    # B 위치 정함
    b_cands = []
    for x, y in direction:
        b_nx, b_ny = bloc[0] + x, bloc[1] + y
        if b_nx < 0 or b_ny < 0 or b_nx >= row or b_ny >= col or board[b_nx][b_ny] == 0:
            continue
        b_cands.append((b_nx, b_ny))
    if not b_cands:
        answer[0] = min(cur_move, answer[0])
        return

    for new_a in a_cands:
        for new_b in b_cands:
            prev_ax, prev_ay = aloc
            prev_bx, prev_by = bloc
            board[prev_ax][prev_ay] = 0
            if board[prev_bx][prev_by] == 0:
                answer[0] = min(cur_move + 1, answer[0])
                return
            board[prev_bx][prev_by] = 0
            dfs(answer, direction, row, col, board, new_a, new_b, cur_move + 2)
            board[prev_ax][prev_ay] = 1
            board[prev_bx][prev_by] = 1


def solution(board, aloc, bloc):
    if aloc == bloc:
        return 1
    answer = [99999999]
    direction = [[1, 0], [0, 1], [-1, 0], [0, -1]]
    row = len(board)
    col = len(board[0])
    dfs(answer, direction, row, col, board, aloc, bloc, 0)
    return answer[0]
