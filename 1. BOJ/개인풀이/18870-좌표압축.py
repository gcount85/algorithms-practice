# https://www.acmicpc.net/problem/18870

"""
N개의 좌표 X1, X2, ..., XN

"""

n = int(input())
coords = [(i, v) for i, v in enumerate(map(int, input().split()))]
coords.sort(key=lambda x: (x[1]))
# print(coords)

num = float('inf')
answer = []
count = 0
for index, value in coords:
    if value == num:
        answer.append((index, count-1))
    else:
        answer.append((index, count))
        count += 1
    num = value
    # print("count :", count, "num :", num)

answer.sort()
for i in answer:
    print(i[1])
