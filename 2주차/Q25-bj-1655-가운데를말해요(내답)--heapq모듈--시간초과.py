# https://www.acmicpc.net/problem/1655

import sys
import heapq

N = int(sys.stdin.readline())
que = []

for _ in range(N):
    input = int(sys.stdin.readline())
    heapq.heappush(que, input)
    que_size = len(que)
    if que_size == 1:
        print(input)
    else:
        if que_size == 2:
            pop_out = heapq.heappop(que)
            print(pop_out)
            heapq.heappush(que, pop_out)
        else:
            temp = []
            while len(que) != (que_size//2)+1:
                pop_out = heapq.heappop(que)
                temp.append(pop_out)
            pop_out = heapq.heappop(que)
            print(pop_out)
            heapq.heappush(que, pop_out)
            for i in temp:
                heapq.heappush(que, i)
