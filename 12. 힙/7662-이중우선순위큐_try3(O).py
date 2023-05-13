import sys
import heapq

# 두 개의 힙을 사용하되 해시 테이블을 이용하여 메모하기

def maintain_consistent(check: dict, heap, sign):
    while heap:
        pop_out = heapq.heappop(heap) * sign
        if check.get(pop_out, 0) > 0:
            check[pop_out] -= 1
            return pop_out


t = int(sys.stdin.readline().strip())

for _ in range(t):

    k = int(sys.stdin.readline().strip())  # k <= 1000000
    minheap = []
    maxheap = []
    check = {}
    for _ in range(k):
        cmd, num = sys.stdin.readline().strip().split()
        if cmd == 'D' and (maxheap != [] and minheap != []):
            if num == '-1': # 최솟값 삭제 
                maintain_consistent(check, minheap, 1)
            else: # 최대값 삭제
                maintain_consistent(check, maxheap, -1)
        elif cmd == 'I':
            if int(num) in check:
                check[int(num)] += 1
            else:
                check[int(num)] = 1
            heapq.heappush(minheap, int(num))
            heapq.heappush(maxheap, -int(num))
            
    if sum(check.values()) != 0:
        answer = [maintain_consistent(check, maxheap, -1)]
        heapq.heappush(minheap, answer[0])
        check[answer[0]] += 1
        answer.append(maintain_consistent(check, minheap, 1))
        print(*answer)
    else:
        print('EMPTY')

'''
1. 중복으로 값이 들어올 때 maintain_consistent 로직을 잘 처리해야 함 
2. 마지막에 정답 출력 시, maxheap에서 pop하면 minheap의 최소값이 None이 나올 수 있는 문제

'''