# https://school.programmers.co.kr/learn/courses/30/lessons/43164#

from collections import defaultdict, deque


def solution(tickets):
    dic = defaultdict(list)
    for s, d in tickets:
        dic[s].append(d)
    for k in dic.keys():
        dic[k] = deque(sorted(dic[k]))

    stack = ["ICN"]
    answer = []
    # print(dic)
    while stack:
        cur = stack[-1]
        if dic[cur]:  # 항공권이 있으면
            stack.append(dic[cur].popleft())
        else:
            answer.append(stack.pop())

    return answer[::-1]
