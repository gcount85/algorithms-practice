# https://school.programmers.co.kr/learn/courses/30/lessons/86051
# 1:18분 시작


def solution(numbers):
    arr = [i for i in range(10)]
    for i in numbers:
        arr[i] = 0
    return sum(arr)
