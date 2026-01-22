# https://school.programmers.co.kr/learn/courses/30/lessons/12909#


def solution(s):
    stack = []
    for b in s:
        if b == "(":
            stack.append(b)
        else:
            if not stack:
                return False
            stack.pop()
    return False if stack else True
