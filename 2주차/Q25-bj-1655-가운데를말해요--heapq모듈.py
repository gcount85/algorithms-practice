# https://www.acmicpc.net/problem/1655

import heapq
import sys

'''
1. leftheap과 rightheap의 길이가 같다면(즉 두 heap에 들어있는 리스트 요소의 수가 같으면) 
중간값의 기준이 되는 leftheap에 수를 넣는다. 
반면, 길이가 같지 않다면 길이를 맞춰주기 위해 rightheap에 수를 넣는다.

2. 만약에 leftheap의 루트가 rightheap의 루트보다 크면 
leftheap의 루트와 rightheap의 루트를 바꿔준다.
why? leftheap은 중간값을 기준으로 작은 수가 들어가는 곳이다.
 그런데 leftheap의 루트가 rightheap보다 크다면, 중간값보다 큰 수가 leftheap에 들어가있는 상황이기에 
 leftheap의 루트와 rightheap의 루트를 바꿔준다.
'''

N = int(sys.stdin.readline())
smallerheap = []  # 최대힙
biggerheap = []   # 최소힙 

for _ in range(N):
    input = int(sys.stdin.readline())
    if len(smallerheap) == len(biggerheap):    # len() 변수로 지정 안 하는게 나음(계속 변하니)
        heapq.heappush(smallerheap, -input)
    else:
        heapq.heappush(biggerheap, input)
    if (len(biggerheap) != 0) and (-smallerheap[0] > biggerheap[0]):
        # biggerheap[0], smallerheap[0] = -smallerheap[0], -biggerheap[0]  # 이렇게 하면 틀림
        min = heapq.heappop(biggerheap)
        max = -heapq.heappop(smallerheap)
        heapq.heappush(smallerheap, -min)
        heapq.heappush(biggerheap, max)
    print(-smallerheap[0])






