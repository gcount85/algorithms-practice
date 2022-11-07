# https://www.acmicpc.net/problem/18258
# 큐2는 deque 모듈(연결 리스트 방식)을 사용하여 속도가 더 빠름

import sys
from collections import deque

'''
-  `deque_list = deque()` : deque 선언
-  `deque_list.append(value)` : 밸류 마지막 인덱스에 추가
-  `deque_list.rotate(step)` : 두 칸씩 데이터가 밀림
-  `deque_list.leftappend(value)` : 인덱스 0에 추가
-  `deque_list.extend([1, 2, 3])` : 1, 2, 3 마지막 인덱스부터 연장
-  `deque_list.leftextend([1, 2, 3])` : 1, 2, 3 인덱스 0부터 추가
'''


queue = deque()
def queue_structure(input: list):
    global queue
    if input[0] == "push":
        queue.append(input[1])
    elif input[0] == "pop":
        if len(queue) == 0:
            print(-1)
        else:
            print(queue.popleft())
    elif input[0] == "size":
        print(len(queue))
    elif input[0] == "empty":
        if len(queue) == 0:
            print(1)
        else:
            print(0)
    elif input[0] == "front":
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[0])
    elif input[0] == "back":
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[-1])

N = int(sys.stdin.readline())
for _ in range(N):
    queue_structure(input := sys.stdin.readline().split())
