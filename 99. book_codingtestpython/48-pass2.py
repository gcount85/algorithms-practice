# 스도쿠


def find_empty(board):
    for row, nums in enumerate(board):
        for col, value in enumerate(nums):
            if value == 0:
                return (row, col)
    return None


def is_valid(row, col, board, num):
    for number in board[row]:
        if number == num:
            return False
    for number in range(9):
        n = board[number][col]
        if n == num:
            return False

    start_row = row // 3 * 3
    start_col = col // 3 * 3
    for r in range(start_row, start_row + 3):
        for c in range(start_col, start_col + 3):
            if board[r][c] == num:
                return False
    return True


def find_solution(board):
    """
    1. 빈칸을 찾는다.
        1-1. 빈칸이 없음?: return True
    2. 빈칸에 1부터 9까지 숫자를 넣는다.
        2-1. not isValid?:
            2-1-1. continue
        2-2. 보드에 숫자를 쓴다.
        2-3. if dfs == true: ## 빈칸이 더이상 없다
            2-3-1. return true
        2-4. 보드 숫자 다시 0으로
    3. return False
    """

    empty = find_empty(board)
    if not empty:
        return True

    row, col = empty
    for n in range(1, 10):
        if not is_valid(row, col, board, n):
            continue
        board[row][col] = n
        if find_solution(board):
            return True
        board[row][col] = 0

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
# [5, 3, 4, 6, 7, 8, 9, 1, 2],
# [6, 7, 2, 1, 9, 5, 3, 4, 8],
# [1, 9, 8, 3, 4, 2, 5, 6, 7],
# [8, 5, 9, 7, 6, 1, 4, 2, 3],
# [4, 2, 6, 8, 5, 3, 7, 9, 1],
# [7, 1, 3, 9, 2, 4, 8, 5, 6],
# [9, 6, 1, 5, 3, 7, 2, 8, 4],
# [2, 8, 7, 4, 1, 9, 6, 3, 5],
# [3, 4, 5, 2, 8, 6, 1, 7, 9],

print(
    solution(
        [
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
        ]
    )
)
