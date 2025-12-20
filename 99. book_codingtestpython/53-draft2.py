# https://school.programmers.co.kr/learn/courses/30/lessons/92345
"""
1. 시작 위치 초기화
    1-1. 둘이 위치 같으면 이동횟수 1로 종료
2. 게임 시작
    2-1. a가 움직일 차례?:
        2-1-1. a가 valid 한 곳으로 이동, 이동횟수 ++1, 이전 위치 발판 제거
        2-1-2. 갈 곳 없으면 return
        2-2-3. 다음 턴 dfs

    2-2. b가 움직일 차례?:
        2-2-1. b가 valid 한 곳으로 이동, 이동횟수 ++1, 이전 위치 발판제거
        2-2-2. 갈 곳 없으면 return
        2-2-3. 다음 턴 dfs
    2-3. dfs
    2-4. a가 움직였으면 a 위치 복구, b가 움직였음 b위치 복구, 이동횟수 원상복구

"""


def dfs(answer, direction, row, col, board, aloc, bloc, cur_move, who_move):
    print(aloc, bloc, cur_move, who_move)
    # aloc or bloc 둘 중 하나가 == 0이면 갱신하고 돌아감
    if board[aloc[0]][aloc[1]] == 0 or board[bloc[0]][bloc[1]] == 0:
        # print(f"둘 중 하나가 졌음! {aloc, bloc, cur_move, answer[0]}")
        answer[0] = min(answer[0], cur_move)
        return

    if who_move == "a":
        for x, y in direction:
            a_nx, a_ny = aloc[0] + x, aloc[1] + y
            if (
                a_nx < 0
                or a_ny < 0
                or a_nx >= row
                or a_ny >= col
                or board[a_nx][a_ny] == 0
            ):
                continue
            new_aloc = [a_nx, a_ny]
            board[aloc[0]][aloc[1]] = 0
            dfs(answer, direction, row, col, board, new_aloc, bloc, cur_move + 1, "b")
            board[aloc[0]][aloc[1]] = 1

        # 갈 곳 없으면?:
        answer[0] = min(answer[0], cur_move)
        return

    if who_move == "b":
        for x, y in direction:
            b_nx, b_ny = bloc[0] + x, bloc[1] + y
            if (
                b_nx < 0
                or b_ny < 0
                or b_nx >= row
                or b_ny >= col
                or board[b_nx][b_ny] == 0
            ):
                continue
            new_bloc = [b_nx, b_ny]
            board[bloc[0]][bloc[1]] = 0
            dfs(answer, direction, row, col, board, aloc, new_bloc, cur_move + 1, "a")
            board[bloc[0]][bloc[1]] = 1

        answer[0] = min(answer[0], cur_move)
        return


def solution(board, aloc, bloc):
    answer = [99999999]
    direction = [[1, 0], [0, 1], [-1, 0], [0, -1]]
    row = len(board)
    col = len(board[0])
    dfs(answer, direction, row, col, board, aloc, bloc, 0, "a")
    return answer[0]
