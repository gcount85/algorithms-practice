# https://www.acmicpc.net/problem/2798

import sys

input = sys.stdin.readline

n, m = map(int, input().split())
cards = list(map(int, input().split()))

# refactored
cards.sort(reverse=True)

answer = 0

for high in range(n-2):
    for mid in range(high+1, n-1):
        for low in range(mid+1, n):
            temp_sum = cards[high] + cards[mid] + cards[low]
            if answer < temp_sum and temp_sum <= m:
                answer = temp_sum
                break

print(answer)

# cards.sort()
# high = n - 1
# mid = high - 1
# low = mid - 1

# while (True):
#     if low < 0:
#         mid -= 1
#         low = mid - 1
#     if mid < 1:
#         high -= 1
#         mid = high - 1
#         low = mid - 1
#     if high < 2:
#         break
#     temp_sum = cards[high] + cards[mid] + cards[low]
#     if temp_sum <= m:
#         answer = max(answer, temp_sum)
#     low -= 1

# print(answer)

"""
- 필요한 변수: sum, 포인터 l, m, high 
- 큰 수부터 검색하는 3개의 포인터 만듦 
- l, m, h가 가리키는 숫자들의 합을 구하여 sum에 저장
    1) sum이 m보다 크면: 저장X, l를 한 단계 낮춤
    2) sum이 m보다 같거나 작으면: return
- 만약 l이 0에 도달했는데도 값을 못 찾았으면: m을 한 값 낮춤, l은 m-1로 다시 반복

"""
