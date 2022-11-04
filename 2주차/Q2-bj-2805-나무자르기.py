# https://www.acmicpc.net/problem/2805

# 상근이는 나무 M미터가 필요하다
# 집 근처의 나무 한 줄에 대한 벌목 허가를 내주었고, 상근이는 새로 구입한 목재절단기를 이용해서 나무를 구할것이다.
# 목재 절단기의 동작
# 절단기에 높이 H를 지정
# 톱날이 땅으로부터 높이 H까지 올라감
# 한 줄에 연속해있는 나무를 모두 절단함 
# -> H 보다 큰 나무는 H 위의 부분이 잘리고, 낮은 나무는 안 잘림
# 적어도 M미터의 나무를 가져가기 위해 설정할 수 있는 높이의 최대값

# 나무높이는 1,000,000,000보다 작거나 같은 양의 정수 또는 0이다.
# 절단기 높이는 0이상 정수


# 높이의 최소값부터 최대값까지 range 뽑아 정렬하고 중간값을 mid로 설정
# mid로 자른 값이 7이랑 같으면  return
# " 7보다 작으면 높이를 내린다(mid가 왼쪽 리스트로 가야한다)
# " 7보다 크면 높이를 올린다(mid가 오른쪽 리스트로 가야한다)
# 이걸 반복

import sys

# 예시
# N = 5 
# M = 1
# height_lst = [0,0,27]

# N = 1 
# M = 500
# height_lst = [1000000000, 1000000000, 1000000000, 1000000000]

N, M = list(map(int, sys.stdin.readline().split()))
height_lst = list(map(int, sys.stdin.readline().split()))
H_range = range(0, max(height_lst))   # H의 범위 (0부터 나무 높이의 최대값)


def find_H(M, H_range, low, high):
    global height_lst
    if (low > high):  # low가 high보다 커지는 상황은 값이 없어서 인덱스가 역전되는 것 
        return False
    else:
        mid = (low + high) // 2
        H = sum([i-H_range[mid] for i in height_lst if i > H_range[mid]])
        # print(H)
        if H == M:
            return H_range[mid]
        elif H < M:
            return find_H(M, H_range, low, mid-1)
        else:
            return find_H(M, H_range, mid+1, high)

print(find_H(M, H_range, 0, len(H_range)-1))

    
    






