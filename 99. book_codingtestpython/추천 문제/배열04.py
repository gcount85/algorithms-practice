# https://school.programmers.co.kr/learn/courses/30/lessons/12910


def solution(arr, divisor):
    arr.sort()
    answer = []

    for a in arr:
        if a % divisor == 0:
            answer.append(a)
    if not answer:
        answer = [-1]
    return answer
