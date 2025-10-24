"""
https://school.programmers.co.kr/learn/courses/30/lessons/12973
N = 100만 : NlogN 이하로 빨라야 함
"""


def solution(s):
    """
    - [반복] 문자열을 앞에서부터 순서대로 스택에 넣는다.
    - [분기]
        - 스택 top이랑 a가 같으면 스택 pop
        - 아니면 push
    - 마지막에 스택이 비어있으면 1
    - 아니면 0
    """

    stack = []
    for a in s:
        if stack and a == stack[-1]:
            stack.pop()
            continue
        stack.append(a)
    if stack:
        return 0
    return 1
