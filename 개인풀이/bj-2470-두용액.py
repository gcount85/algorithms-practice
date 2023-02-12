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
min_comb = 1000000000*2
ans_용액1 = 0
ans_용액2 = 0
N = int(sys.stdin.readline())
values = list(map(int, sys.stdin.readline().split()))
values.sort()

# todo- i와 동일한 인덱스는 건너뛰기, typeError, 마지막반례해결


def binarysearch(i, l, h):
    """
    i: 용액 1의 인덱스
    l: 탐색 범위 시작 인덱스
    h: 탐색 범위 끝 인덱스 
    """

    if (l < h):
        if (l == i):
            l += 1
        if (h == i):
            h -= 1
    m = (l + h) // 2

    용액1 = values[i]
    mid_comb = abs(values[m] + 용액1)
    high_comb = abs(values[h] + 용액1)
    low_comb = abs(values[l] + 용액1)

    # if (l >= h) or (low_comb == high_comb) or (mid_comb == 0):
    if (l >= h) or (low_comb == high_comb):  # 종료조건 인덱스 잘 지정하기!
        return mid_comb, values[m]
    elif low_comb < high_comb:
        return binarysearch(i, l, m-1)
    elif high_comb < low_comb:
        return binarysearch(i, m+1, h)


for i in range((length := len(values))):
    용액1 = values[i]
    mid_comb, 용액2 = binarysearch(i, 0, length-1)
    if (용액1 == 용액2):
        continue
    # if (mid_comb == 0):
    #     print(min(용액1, 용액2), max(용액1, 용액2))
    #     break
    if (mid_comb < min_comb):
        min_comb = mid_comb
        ans_용액1 = 용액1
        ans_용액2 = 용액2

print(min(ans_용액1, ans_용액2), max(ans_용액1, ans_용액2))


# 1. 용액의 특성값 오름차순 정렬
# 2. 용액 a에 대해서 용액 a를 제외한 나머지 용액에 대해 이분탐색
#     1) 0과의 절대값이 더 작은 쪽으로 탐색 범위 좁힘
#     2) 가장 작은 절대값을 혼합 특성값으로 저장
# 3. 다른 용액들에 대해서도 똑같이 반복 & 가장 작은 혼합 특성값 찾아내기


"""반례
5
-99 -98 1 0 96
0 1

5
-98 -97 1 2 92
1 2

5
-100 -50 20 10 80
-100 80

4
999999995 999999996 999999997 1000000000
999999995 999999996

3
-10 1 2
1 2


6
1 2 3 4 5 6
1 6
"""
