import sys
import heapq

# 두 개의 힙을 사용하되 해시 테이블을 이용하여 메모하기
t = int(sys.stdin.readline())

def maintain_consistent(check, heap, flag):
    pop_out = heapq.heappop(heap)
    if flag == 1:
        pop_out *= -1
    while check[pop_out] == 0 and heap != []:
        pop_out = heapq.heappop(heap)
        if flag == 1:
            pop_out *= -1
    check[pop_out] -= 1
    return pop_out

for _ in range(t):

    k = int(sys.stdin.readline())  # k <= 1000000
    minheap = []
    maxheap = []
    check = {}
    for _ in range(k):
        cmd, num = sys.stdin.readline().strip().split()
        if cmd == 'D' and sum(check.values()) > 0:
            if num == '-1': # 최솟값 삭제 
                maintain_consistent(check, minheap, 0)
            else: # 최대값 삭제
                maintain_consistent(check, maxheap, 1)
        elif cmd == 'I':
            if int(num) in check:
                check[int(num)] += 1
            else:
                check[int(num)] = 1
            heapq.heappush(minheap, int(num))
            heapq.heappush(maxheap, -int(num))
            
    if maxheap != [] and minheap != []:
        print(maintain_consistent(check, maxheap, 1), maintain_consistent(check, minheap, 0))
    else:
        print('EMPTY')
