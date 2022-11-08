import heapq
import sys

N = int(sys.stdin.readline())
minheap = []

for _ in range(N):
    size = int(sys.stdin.readline())
    heapq.heappush(minheap, size)

temp = []
for i in range(2):
    pop_out = heapq.heappop(minheap)
    temp.append(pop_out)
count = sum(temp)

while len(minheap) != 0:
    pop_out = heapq.heappop(minheap)
    count += (count + pop_out)

print(count)



