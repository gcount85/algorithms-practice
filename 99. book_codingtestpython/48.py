# 스도쿠


def find_empty(board):
    for i, row in enumerate(board):
        for j, value in enumerate(row):
            if value == 0:
                return (i, j)
    return None


def is_valid(row, col, board, num):
    # row 에 같은 숫자 없어야 함
    if num in board[row]:
        return False

    # col 에 같은 숫자 없어야 함
    if num in (board[i][col] for i in range(9)):
        return False

    start_row = row // 3 * 3
    start_col = col // 3 * 3

    for cur_row in range(start_row, start_row + 3):
        for cur_col in range(start_col, start_col + 3):
            if board[cur_row][cur_col] == num:
                return False
    return True


def find_solution(board):
    """
    1. 빈칸을 찾는다.
    2. 빈칸이 없으면: return True
    3. 1부터 9까지 숫자에 대해서:
        3-1. 그 자리에 빈칸을 넣는게 유효하면?:
            3-1-1. 빈칸을 채운다
            3-1-2. find_solution 재호출해서 false 나오면: 다시 0으로 바꿈
                    true 나오면 return True
    4. 1~9까지 다 넣었는데도 답을 못찾았으면 return False
    """

    empty = find_empty(board)
    if not empty:
        return True
    i, j = empty
    for n in range(1, 10):
        if not is_valid(i, j, board, n):
            continue
        board[i][j] = n
        if find_solution(board):
            return True
        else:
            board[i][j] = 0
    return False


def solution(board):
    find_solution(board)
    return board


print(
    solution(
        [
            [5, 3, 0, 0, 7, 0, 0, 0, 0],
            [6, 0, 0, 1, 9, 5, 0, 0, 0],
            [0, 9, 8, 0, 0, 0, 0, 6, 0],
            [8, 0, 0, 0, 6, 0, 0, 0, 3],
            [4, 0, 0, 8, 0, 3, 0, 0, 1],
            [7, 0, 0, 0, 2, 0, 0, 0, 6],
            [0, 6, 0, 0, 0, 0, 2, 8, 0],
            [0, 0, 0, 4, 1, 9, 0, 0, 5],
            [0, 0, 0, 0, 8, 0, 0, 7, 9],
        ]
    )
)
