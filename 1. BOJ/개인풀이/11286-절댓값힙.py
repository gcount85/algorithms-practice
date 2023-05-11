import heapq
import sys

input = sys.stdin.readline
heap = []  # creates an empty heap
answer = []
for _ in range(int(input())):
    if (x := int(input())) == 0:
        answer.append(heapq.heappop(heap)[1] if heap != [] else 0)
    else:
        heapq.heappush(heap, (abs(x), x))

print(*answer)
