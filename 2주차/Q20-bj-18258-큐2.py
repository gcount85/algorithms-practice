# https://www.acmicpc.net/problem/18258

import sys


def queue_structure(input: list, queue: list):
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

queue = []
N = int(sys.stdin.readline())
for _ in range(N):
    queue_structure(input := sys.stdin.readline().split(), queue)
