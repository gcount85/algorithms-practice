# https://www.acmicpc.net/problem/11025
# 찾아보니 수학적으로 접근해야 한다 함! 

import sys
from collections import deque

N, K = map(int, sys.stdin.readline().split())
queue = deque()
queue.extend(range(1, N+1))
while True:
    for i in range(K-1):
        queue.append(queue.popleft())
    queue.popleft()
    if len(queue) == 1:
        break

print(queue[0])

