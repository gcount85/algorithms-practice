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
N = int(sys.stdin.readline())
values = list(map(int, sys.stdin.readline().split()))
values.sort()

def solution(values, min_comb):
    ans1 = 0
    ans2 = 0
    s = 0
    e = len(values) - 1

    if (values[0] > 0):
        ans1 = values[0]
        ans2 = values[1]
        print(ans1, ans2)
        return

    elif (values[-1] < 0):
        ans1 = values[-2]
        ans2 = values[-1]
        print(ans1, ans2)
        return

    while (s < e):
        sumvalue = abs(values[s] + values[e])
        if (sumvalue < min_comb):
            min_comb = sumvalue
            ans1 = values[s]
            ans2 = values[e]
        if min_comb == 0:
            break
        if values[s] + values[e] < 0:
            s += 1
        elif values[s] + values[e] > 0:
            e -= 1

    print(ans1, ans2)

solution(values, min_comb)


# 1. 용액의 특성값 오름차순 정렬
# 2. 투 포인터 검색 
#   1) start, end에서 검색 시작
#   2) 0과 제일 가까운 수 찾기!
#   3) 0보다 작으면 start += 1
#   4) 0보다 크면 end -= 1  


"""반례
5
-99 -98 0 1 96
0 1

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
