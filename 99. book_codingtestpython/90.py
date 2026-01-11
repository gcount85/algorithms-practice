# https://school.programmers.co.kr/learn/courses/30/lessons/68936

import sys

sys.setrecursionlimit(10**6)


def solution(arr):
    """
    1. 0 개수, 1개수 세는 전역변수 두기
    2. 1, 2, 3, 4분면 각각 0, 1 개수 세기 ->  만약 범위 내의 모든 숫자가 0이거나 1이면:
        2-1. 전역변수 업뎃하고 return
    3. else: 다시 1,2,3,4분면 개수 세기 재귀 반복
    """

    answer = [0, 0]
    n = len(arr)  # 4

    def count(start_row, start_col, size):
        # 해당 분면 숫자 검사
        num = arr[start_row][start_col]
        stop = False
        for i in range(start_row, start_row + size):
            for j in range(start_col, start_col + size):
                if arr[i][j] != num:
                    stop = True
                    break
            if stop:
                break
        else:  # break 없이 모두 숫자가 통일이면?
            answer[num] += 1
            return

        # 다시 1,2,3,4 분면 개수 세기 : 0, 3, 0, 3..
        size = size // 2
        count(start_row, start_col, size)  # 0-1, 0-1
        count(start_row, start_col + size, size)  # 0-1, 2-3
        count(start_row + size, start_col, size)  # 2-3, 0-1
        count(start_row + size, start_col + size, size)  # 2-3, 2-3

    count(0, 0, n)

    return answer
