# 배열 회전하기: arr를 시계방향 90도로 n번 회전


def solution(n, arr):
    m = len(arr)
    answer = arr
    for _ in range(n):
        new_arr = [[0] * m for _ in range(m)]
        for i in range(m):
            for j in range(m):
                new_arr[j][(m - 1) - i] = answer[i][j]
        answer = new_arr[:]
    return answer


print(solution(1, [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]))
print(solution(2, [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]))
