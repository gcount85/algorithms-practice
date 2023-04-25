import heapq
import sys

input = sys.stdin.readline
heap = []  # creates an empty heap 
answer = []
for _ in range(int(input())):
    if (x:=int(input())) == 0: # 자연수면 추가, 0이면 pop
        answer.append(heapq.heappop(heap) if heap != [] else 0)
    else:
        heapq.heappush(heap, x)

print(*answer)    
