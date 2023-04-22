# https://www.acmicpc.net/problem/1764

import sys
from collections import Counter

input = sys.stdin.readline

# Counter 이용
N, M = map(int, input().split())
not_heard = [input().strip() for _ in range(N)]
not_seen = [input().strip() for _ in range(M)]

lst = Counter(not_heard+not_seen)

answer = sorted(k for k, v in lst.items() if v == 2)

print(len(answer), *answer)


# dict 이용
N, M = map(int, input().split())
lst = {}
answer = []
count = 0
for _ in range(N):
    lst[input().strip()] = 1

for _ in range(M):
    if (who := input().strip()) in lst:
        answer.append(who)
        count += 1
answer.sort()

print(count, *answer)
