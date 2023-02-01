# https://www.acmicpc.net/problem/2470

"""
산성 용액 특성값: 1부터 1,000,000,000까지의 양의 정수, 
알칼리성 용액 특성값: -1부터 -1,000,000,000까지의 음의 정수
같은 양의 두 용액을 혼합한 용액의 특성값: 두 용액의 특성값 합

특성값이 0에 가장 가까운 용액을 만들어라

입력
첫째 줄 N (2 <= N <= 100,000)
둘째 줄부터 용액의 특성값을 나타내는 N개의 정수 (-1,000,000,000이상 1,000,000,000 이하)
(특성값은 모두 다름. 산성 용액만으로나 알칼리성 용액만 있는 경우도 있음)

출력
첫째 줄에 특성값이 0에 가장 가까운 용액을 만들어내는 두 용액의 특성값 오름차순 출력
0에 가깝게 만드는 경우가 두 개 이상일 경우에는 그 중 아무것이나 하나를 출력

"""

import sys


def binarysearch(i, values, l, h):
    m = (l + h) // 2
    용액1 = values[i]
    middle = abs(values[m] + 용액1)
    high = abs(values[h] + 용액1)
    low = abs(values[l] + 용액1)

    if (middle == 0):
        return middle, 용액2
    if low < high:
        binarysearch(i, values, l, m)
    if low > high:
        binarysearch(i, values, m, h)


input = sys.stdin.readline
N = int(input())
values = list(map(int, input().split()))
min_comb = 1000000000*2
ans_용액2 = 0


for i in range((length := len(values))):
    용액1 = values[i]
    comb, 용액2 = binarysearch(i, values, 0, length-1)
    if (comb == 0):
        print(용액1, 용액2)
        break
    if (comb < min_comb):
        min_comb = comb
        ans_용액2 = 용액2


# 1. 용액의 특성값 오름차순 정렬
# 2. 용액 a에 대해서 용액 a를 제외한 나머지 용액에 대해 이분탐색
#     1) 0과의 절대값이 더 작은 쪽으로 탐색 범위 좁힘
#     2) 가장 작은 절대값을 혼합 특성값으로 저장
# 3. 다른 용액들에 대해서도 똑같이 반복 & 가장 작은 혼합 특성값 찾아내기

# If no items
# 	Return false
# If middle item is 50 // 중간 인덱스부터 시작
# 	Return true
# Else if 50 < middle item
# 	Search left half
# Else if 50 > middle item
# 	Search right half
