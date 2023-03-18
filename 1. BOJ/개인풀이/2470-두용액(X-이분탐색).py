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
aux = 0  # values가 양수들의 리스트인지 확인 
N = int(sys.stdin.readline())
values = list(map(int, sys.stdin.readline().split()))
values.sort()


# todo- i와 동일한 인덱스는 건너뛰기, typeError, 마지막반례해결
# -1 곱한 값을 이분탐색으로 찾기

def binarysearch(용액1, l, h, aux):
    """
    i: 용액 1의 인덱스
    l: 탐색 범위 시작 인덱스
    h: 탐색 범위 끝 인덱스 
    """
    탐색값 = 용액1 * -1
    m = (l + h) // 2

    if (values[m] == 탐색값) or (l >= h):
        return m
    elif (values[m] > 탐색값):
        return binarysearch(i, l, m-1, aux)
    elif (values[m] < 탐색값):
        return binarysearch(i, m+1, h, aux)


if (values[0] >= 0):
    aux = 1

for i in range((length := len(values))):
    m = binarysearch(values[i], 0, length-1, aux)
    if i == m:
        continue
    sumvalue = values[i] + values[m]
    if (sumvalue < min_comb):
        min_comb = sumvalue
        ans_용액1 = values[i]
        ans_용액2 = values[m]

print(min(ans_용액1, ans_용액2), max(ans_용액1, ans_용액2))


# 1. 용액의 특성값 오름차순 정렬
# 2. 용액 a에 대해서 용액 a를 제외한 나머지 용액에 대해 이분탐색
#     1) 0과의 절대값이 더 작은 쪽으로 탐색 범위 좁힘
#     2) 가장 작은 절대값을 혼합 특성값으로 저장
# 3. 다른 용액들에 대해서도 똑같이 반복 & 가장 작은 혼합 특성값 찾아내기


"""반례
5
-98 -97 1 2 92
1 2

5
-100 -50 20 10 80
-100 80

5
-100 -50 20 40 80
-50 40

4
999999995 999999996 999999997 1000000000
999999995 999999996

3
-10 1 2
1 2


6
1 2 3 4 5 6
1 2

6
-6 -5 -4 -3 -2 -1
-2 -1

4
-3 -1 1 10
정답: -1 1

"""
