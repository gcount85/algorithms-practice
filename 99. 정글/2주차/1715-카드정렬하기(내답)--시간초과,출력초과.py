import heapq
import sys

N = int(sys.stdin.readline())
minheap = []

for _ in range(N):
    size = int(sys.stdin.readline())
    heapq.heappush(minheap, size)

count = 0
for i in range(2):
    pop_out = heapq.heappop(minheap)
    count += pop_out

while len(minheap) != 0:
    pop_out = heapq.heappop(minheap)
    count += (count + pop_out)

print(count)



