# https://school.programmers.co.kr/learn/courses/30/lessons/12905


def solution(board):
    """
    - 숫자가 1이면?: 가로, 세로, 대각선 확인해서 모두 1 이상이면 가/세/대 최솟값 +1
    """

    row, col = len(board), len(board[0])
    for i in range(1, row):
        for j in range(1, col):
            if (
                board[i][j] == 1
                and board[i - 1][j] >= 1
                and board[i][j - 1] >= 1
                and board[i - 1][j - 1] >= 1
            ):
                board[i][j] = (
                    min(board[i - 1][j], board[i][j - 1], board[i - 1][j - 1]) + 1
                )
    return max(max(r) for r in board) ** 2
