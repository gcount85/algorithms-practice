# https://school.programmers.co.kr/learn/courses/30/lessons/12987
# 16분 solved
# O(NlogN)


def solution(A, B):
    A.sort()  # nlogn
    B.sort()  # nlogn

    answer = 0
    a = 0
    b = 0
    n = len(A)
    while a <= n - 1 and b <= n - 1:  # O(n)
        if A[a] >= B[b]:
            b += 1
        else:
            answer += 1
            a += 1
            b += 1
    return answer
