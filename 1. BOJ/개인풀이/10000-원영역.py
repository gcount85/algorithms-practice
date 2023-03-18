# https://www.acmicpc.net/problem/10000

import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
discs = []

for i in range(N):
    x, r = map(int, input().split())
    discs.append((x - r, 1, r*2))    # position, left edge, diameater
    # position, right edge, diameater (음수로 처리하여 스택처럼 배열되게)
    discs.append((x + r, -1, -r*2))

discs.sort(key=lambda x: (x[0], x[1], -x[2]))
print("디스크", discs)

intersect = 1
stack = deque()
sum_temp = 0
temp = []

for i, v in enumerate(discs):
    edge = v[1]
    this_dia = v[2]
    popped_dia = 0

    if edge == 1:   # 원이 시작할 때
        intersect += 1
        stack.append(this_dia)
        print("스택에 추가:", v, this_dia, stack)
    else:           # 원이 끝날 때
        if (this_dia + stack[-1] == 0):
            if sum_temp + this_dia == -this_dia:
                intersect += 1
            else:
                print("넘어감?")
                continue
        while popped_dia != -this_dia:
            popped_dia = stack.pop()
            print("스택에서 제거:", v, popped_dia, stack)
            temp.append(popped_dia)
        sum_temp = sum(temp)
        if sum_temp + this_dia == -this_dia:
            intersect += 1
            print("더하기두번~! : ", v)
        popped_dia = 0


print(intersect)


"""
5
1 1
3 3
3 1
4 2
5 1
=> 8
"""
