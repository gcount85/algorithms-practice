# https://school.programmers.co.kr/learn/courses/30/lessons/12906?language=python3


def solution(arr):
    stack = []
    for a in arr:
        if stack and stack[-1] == a:
            continue
        stack.append(a)
    return stack
