# https://www.acmicpc.net/problem/1655

import sys
from queue import PriorityQueue

N = int(sys.stdin.readline())
que = PriorityQueue(maxsize=100001)

for _ in range(N):
    input = int(sys.stdin.readline())
    que.put(input)
    que_size = que.qsize()
    if que_size == 1:
        print(input)
    else:
        if que_size == 2:
            pop_out = que.get()
            print(pop_out)
            que.put(pop_out)
        else:
            temp = []
            while que.qsize() != (que_size//2)+1:
                pop_out = que.get()
                temp.append(pop_out)
            pop_out = que.get()
            print(pop_out)
            temp.append(pop_out)
            for i in temp:
                que.put(i)
