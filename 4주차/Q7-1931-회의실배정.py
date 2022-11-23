# https://www.acmicpc.net/problem/1931

import sys

N = int(sys.stdin.readline())
schedule = []

for _ in range(N):
    s, e = map(int, sys.stdin.readline().split())
    schedule.append((s,e))

schedule.sort(key=lambda x: (x[1], x[0]))

last = schedule[0]
최대개수 = 1
for i in schedule[1:]:   # 이 범위를 그냥 schedule로 설정하면 틀림! 
    if i[0] >= last[1]:
        last = i
        최대개수 += 1

# print(schedule)
print(최대개수)
