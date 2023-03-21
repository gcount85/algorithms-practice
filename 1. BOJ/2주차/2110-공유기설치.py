# https://www.acmicpc.net/problem/2110

import sys


N = 5
C = 3
houses = [1, 2, 4, 8, 9]

# N, C = map(int, sys.stdin.readline().split())
# houses = [int(sys.stdin.readline()) for _ in range(N)]
houses.sort()

dis_range = range(1, houses[-1]-houses[0]+1)  # 거리의 범위는 1부터, 젤 서로 먼 집끼리의 거리


def is_router_installed(distance):
    global C
    current = houses[0]
    count = 1
    for i in range(1, len(houses)):
        if houses[i] >= current + distance:
            count += 1
            current = houses[i]
            if count == C:   # 공유기 설치 완료
                return 1
    return 0                 # 공유기 설치 못함


def search(dis_range, low, high):  # low는 젤 작은 거리범위, high는 젤 큰 거리범위
    global C
    global answer

    if (low > high):  # low가 high보다 커지는 상황은 값이 없어서 인덱스가 역전되는 것
        return False
    else:
        mid = (low + high) // 2
        if is_router_installed(mid) == 1: # 해당 거리 범위로 공유기를 설치할 수 있음
            answer = mid        # 미드가 정답일 수도 있으니까 일단 넣어둠
            return search(dis_range, mid+1, high)
        else: # 해당 거리 범위로 공유기를 설치할 수 없음
            return search(dis_range, low, mid-1)


search(dis_range, dis_range[0], dis_range[-1])
print(answer)


"""
- 이분탐색 함수 
1. 탐색 범위 지정: 공유기 설치 거리 범위(1 ~ 가장 서로 멀리 떨어진 집 끼리의 거리)
2. 탐색 범위 이분탐색
    1) mid 값으로 공유기 설치 가능: 
        (1) mid 값을 답으로 추가
        (2) mid 값 기준 오른쪽 배열 탐색
    2) mid 값으로 공유기 설치 불가: mid 값 기준 왼쪽 배열 탐색

- 공유기 설치 함수
1. 제일 왼쪽 집을 기준으로 설정한 후 공유기 설치 시작
2. 나머지 모든 집들에 대해
    1) 현재 집으로부터 주어진 거리 이상 떨어져 있음:
        (1) 공유기 설치
        (2) 설치한 집을 기준 집으로 재설정
        (3) 모든 공유기 설치 완료: 1 반환
    2) 공유기 설치 불가: 0 반환 

"""
