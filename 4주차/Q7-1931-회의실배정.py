# https://www.acmicpc.net/problem/1931

import sys

N = int(sys.stdin.readline())
schedule = []

for _ in range(N):
    s, e = map(int, sys.stdin.readline().split())
    schedule.append((s,e,e-s))

최대개수 = 0
schedule.sort(key=lambda x: (x[0], x[1], x[2]))
for i in schedule:
    reserved = [i]
    for j in schedule:
        if j[0] >= reserved[-1][1]:
            reserved.append(j)
    현재개수 = len(reserved)
    if 현재개수 > 최대개수:
        최대개수 = 현재개수

# print(schedule)
print(최대개수)
