# https://www.acmicpc.net/problem/12865

import sys
sys.setrecursionlimit(10**6)

N, K = map(int, sys.stdin.readline().split())
W = []   # 아이템의 무게 리스트
P = []   # 아이템의 가치

for _ in range(N):
	w, v = map(int, sys.stdin.readline().split())
	W.append(w)
	P.append(v)



# 재귀버전 → 메모리, 시간 초과 나는 듯..

def knapsack2(i, K, W, P):		# 인덱스, 무게, 무게 리스트, 가치 리스트 
    if (i < 0 or K <= 0):		# 아이템이 0개이거나 무게가 0일 때
        return 0
    if (W[i] > K):	# 아이템의 무게가 무게 제한보다 클 때 
        return knapsack2(i-1, K, W, P)	# 아이템을 한 개 뺀 상태로 돌아감(배낭에 담지 않음)
    else:			# 아이템의 무게가 무게 제한과 같거나 작을 때
        left = knapsack2(i-1, K, W, P)		  # left = 배낭에 담지 않았을 경우의 가치
        right = knapsack2(i-1, K-W[i], W, P)  # right = 배낭에 담았을 경우의 가치
        return max(left, P[i] + right)


profit = knapsack2(len(W)-1, K, W, P)
print(profit)


# 반복문 버전
# 참고: https://www.acmicpc.net/board/view/93599

sum_value = [0]*(K+1)
items = []

for _ in range(N):
    w, v = map(int, sys.stdin.readline().split())
    items.append((w, v))

for item in items:
    w, v = item 

    for i in range(K, w-1, -1):   # 무게제한부터 해당 무게까지 -1씩 감소시키면서
        # 배낭에 담기 전의 최대 가치 + 담은 후의 최대 가치 중 최댓값
        sum_value[i] = max(sum_value[i], sum_value[i-w]+v)  

print(sum_value[-1])


'''
반례
5 10
3 8
4 7
1 9
5 6
2 1
답: 25
'''