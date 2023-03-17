# https://www.acmicpc.net/problem/1158
# 사실상 요세푸스문제0 과 똑같음! 

import sys
from collections import deque

N, K = map(int, sys.stdin.readline().split())
queue = deque()
queue.extend(range(1, N+1))

josephus = []
while len(queue) != 0:
    for i in range(K-1):
        pop_out = queue.popleft()
        queue.append(pop_out)
    pop_out = queue.popleft()
    josephus.append(pop_out)

print("<", end="")
for i in range(len(josephus)-1):
    print(f"{josephus[i]}, ", end="")
print(josephus[-1], end="")
print(">", end="")

