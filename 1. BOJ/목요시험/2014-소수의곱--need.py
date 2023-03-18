import heapq
import sys

# K, N = map(int, sys.stdin.readline().split())
# sosu = list(map(int, sys.stdin.readline().split())) 

K, N = 4, 19
sosu = [2, 3, 5, 7] 

minheap0 = []  # 2,3,5,7이 담김 
minheap1 = [] 

for i in sosu:
    heapq.heappush(minheap0, i)
    heapq.heappush(minheap1, i)

count = 0
temp = 0
while count > N:  ## 계속 최소값끼리 곱하게
    for i in sosu:
        for j in sosu:
            heapq.heappush(minheap1, i*j)
            count += 1
    
print(minheap1)
    