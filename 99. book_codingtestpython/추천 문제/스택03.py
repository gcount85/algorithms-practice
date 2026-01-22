# https://school.programmers.co.kr/learn/courses/30/lessons/120853


def solution(s):
    string = s.split(" ")
    # print(string)

    stack = []
    for s in string:
        if s == "Z":
            stack.pop()
        else:
            stack.append(int(s))
    return sum(stack)
