# 행렬 곱 앤드 전치


def multiply(a, b):
    array = [[0] * 3 for _ in range(3)]
    for i in range(3):
        for j in range(3):
            for k in range(3):
                array[i][j] += a[i][k] * b[k][j]
    return array


def transpose(a):
    array = [[0] * 3 for _ in range(3)]
    for i in range(3):
        for j in range(3):
            array[i][j] = a[j][i]
    return array


def solution(mtx1, mtx2):
    return transpose(multiply(mtx1, mtx2))


print(solution([[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[9, 8, 7], [6, 5, 4], [3, 2, 1]]))
print(solution([[2, 4, 6], [1, 3, 5], [7, 8, 9]], [[9, 1, 2], [4, 5, 6], [7, 3, 8]]))
