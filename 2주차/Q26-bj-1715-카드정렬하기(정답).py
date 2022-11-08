import heapq
import sys

N = int(sys.stdin.readline())
minheap = []

for _ in range(N):
    size = int(sys.stdin.readline())
    heapq.heappush(minheap, size)


count = 0
while len(minheap) != 1:
    pop_out1 = heapq.heappop(minheap)
    pop_out2 = heapq.heappop(minheap)
    count += (pop_out1 + pop_out2)
    heapq.heappush(minheap, pop_out1 + pop_out2)

print(count)
