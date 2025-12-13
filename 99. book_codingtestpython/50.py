# https://school.programmers.co.kr/learn/courses/30/lessons/12952


def is_valid(col, cols, d1, d2, diag1, diag2):
    if cols[col] or diag1[d1] or diag2[d2]:
        return False
    return True


def find_solution(n, row, answer, counter, cols, diag1, diag2):
    for col in range(n):
        d1 = row - col + (n - 1)
        d2 = row + col
        if is_valid(col, cols, d1, d2, diag1, diag2):
            cols[col] = diag1[d1] = diag2[d2] = True
            counter[0] += 1
            if counter[0] == n:
                answer[0] += 1
            find_solution(n, row + 1, answer, counter, cols, diag1, diag2)
            cols[col] = diag1[d1] = diag2[d2] = False
            counter[0] -= 1


def solution(n):
    """
    1. i, j = 0,0 부터 시작하며 체스를 둬봄
    2. is valid?
        2-1. yes: keep going
        2-2. no:
            2-2-1. 체스 둔거 원상복구 && backtrack
    3. 종료시점임?
        answer ++1

    """
    answer = [0]
    counter = [0]

    cols = [False] * n
    diag1 = [False] * (2 * n - 1)  # r - c + (n-1)
    diag2 = [False] * (2 * n - 1)  # r + c

    find_solution(n, 0, answer, counter, cols, diag1, diag2)
    return answer[0]
