# https://www.acmicpc.net/problem/10845
# queue 리스트를 매개변수로 주는 것보다 전역 변수로 지정하는게 메모리랑 속도 면에서 더 나았음 

import sys

queue = []
def queue_structure(input: list):
    global queue
    if input[0] == "push":
        queue.append(input[1])
    elif input[0] == "pop":
        if len(queue) == 0:
            print(-1)
        else:
            print(queue.pop(0))
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
