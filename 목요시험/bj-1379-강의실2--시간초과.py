# https://www.acmicpc.net/problem/1379 강의실2
# 최대한 적은 수의 강의실을 사용하여 모든 강의가 이루어지게 하고 싶다.


import sys
import heapq

N = int(sys.stdin.readline())

schedule1 = []
schedule2 = []

for _ in range(N):
    n, s, e = map(int, sys.stdin.readline().split())
    heapq.heappush(schedule1, (e, s, n)) # 끝나는시간, 시작시간, 강의번호

ans = []
강의실번호 = 0
while schedule1:
    강의실번호 += 1
    last = heapq.heappop(schedule1)  # 8,3,1
    ans.append((강의실번호, last[2]))  # 강의실번호랑, 강의번호 추가      
    while schedule1:
        comp = heapq.heappop(schedule1)
        if comp[1] >= last[0]:
            last = comp
            ans.append((강의실번호, last[2]))  # 강의실번호, 강의번호 추가      
        else:
            heapq.heappush(schedule2, comp)
    for j in schedule2:
        heapq.heappush(schedule1, j)
    schedule2.clear()


print(ans[-1][0]) # 강의실 개수 -> 이건 맞게 나오는데 
for k in ans:
    print(k[0])


