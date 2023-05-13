# https://www.acmicpc.net/problem/11866

'''
-  `deque_list = deque()` : deque 선언
-  `deque_list.append(value)` : 밸류 마지막 인덱스에 추가
-  `deque_list.rotate(step)` : 두 칸씩 데이터가 밀림
-  `deque_list.leftappend(value)` : 인덱스 0에 추가
-  `deque_list.extend([1, 2, 3])` : 1, 2, 3 마지막 인덱스부터 연장
-  `deque_list.leftextend([1, 2, 3])` : 1, 2, 3 인덱스 0부터 추가
'''

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

