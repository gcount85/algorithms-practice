# https://www.acmicpc.net/problem/11279

import sys
import heapq

N = int(sys.stdin.readline())
heap = []

for _ in range(N):
    input = int(sys.stdin.readline())
    heap_size = len(heap)
    if input == 0:
        if heap_size == 0:
            print(0)
        else:
            print(-heapq.heappop(heap))
    else:   # 정수를 삽입할 때 
        heapq.heappush(heap, -input)
