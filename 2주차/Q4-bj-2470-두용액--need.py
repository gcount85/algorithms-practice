# https://www.acmicpc.net/problem/2470
# 산성 용액은 1부터 1,000,000,000까지의 양의 정수, 알칼리성 용액은 -1부터 -1,000,000,000까지의 음의 정수
# 같은 양의 두 용액을 혼합한 용액의 특성값은 혼합에 사용된 각 용액의 특성값의 합
# 특성값이 0에 가장 가까운 용액을 만들어라

# N은 2 이상 100,000 이하
# 용액의 특성값을 나타내는 N개의 정수
import sys

N = 5
values = [-97, 10, 1, -2, -1, 4]
values.sort()

# N = int(sys.stdin.readline())
# values = sorted(list(map(int, sys.stdin.readline().split())))
answer = -1

mid_index = (N-1) // 2
# 음 = [i for i in values if i < 0]

def search(원소, rest_lst, low_index, high_index):
    if low_index >= high_index:  # low_index가 high_index보다 같은 상황이 제일 절대값 작은 경우 
        return rest_lst[low_index]
    else:
        mid_index = (low_index + high_index) // 2
        mid_abs = abs(0-(rest_lst[mid_index] + 원소))
        low_abs = abs(0-(rest_lst[low_index] + 원소))
        high_abs = abs(0-(rest_lst[high_index] + 원소))
        if min(mid_abs, low_abs, high_abs) == mid_abs: # 오른쪽으로 
            return rest_lst[mid_index]        
        elif max(mid_abs, low_abs, high_abs) == low_abs: # 오른쪽으로 
            return search(원소, rest_lst, mid_index+1, high_index)
        elif max(mid_abs, low_abs, high_abs) == high_abs: # 왼쪽으로 
            return search(원소, rest_lst, low_index, mid_index-1)

# print(search(음[0], 양, 0, len(양)-1))

for i, v in enumerate(values):
    if i <= N-1:
        est = (v, search(v, values[i+1:], 0, (N)-(i+1))) 
        # print(est)
        if answer == -1:
            answer = est
        else:
            if abs(0-sum(answer)) > abs(0-sum(est)):
                answer = est

print(answer[0], answer[1])



    

# 용액의 특성값을 0보다 작은 쪽, 0보다 큰 쪽 이렇게 두개로 나눔
# 리스트의 한 원소에 대해서 나머지 리스트를 이분탐색함 
# 0과의 절대값이 작은쪽으로 리스트를 이동 
# 결과값을 comb에 저장(0과의 절대값이 기존의 comb값보다 작은 경우에만 )


