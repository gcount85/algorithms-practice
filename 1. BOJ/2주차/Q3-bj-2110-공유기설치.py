# https://www.acmicpc.net/problem/2110

import sys

N = 5
C = 3
houses = [1, 2, 4, 8, 9]

# N, C = map(int, sys.stdin.readline().split())
# houses = [int(sys.stdin.readline()) for _ in range(N)]
houses.sort()

dis_range = range(1, houses[-1]-houses[0]+1)  # 거리의 범위는 1부터, 젤 서로 먼 집끼리의 거리

def router_bool(houses, distance):
    global C
    # global 위치     # 좌표를 확인하고 싶으면 위치 변수 주석 해제~ ~
    current = houses[0]
    count = 1
    # 위치 = [houses[0]]
    for i in range(1, len(houses)):
        if houses[i] >= current + distance:
            count += 1
            current = houses[i]
            # 위치.append(current)
            if count == C:
                break
    if count >= C:  # 만약에 공유기 설치를 개수보다 더 많이 할 수 있으면
        return 1
    else:           # 공유기 설치 못함
        return 0


def search(dis_range, low, high):  # low는 젤 작은 거리범위, high는 젤 큰 거리범위
    global C
    global houses
    if (low > high):  # low가 high보다 커지는 상황은 값이 없어서 인덱스가 역전되는 것
        return False
    else:
        mid = (low + high) // 2
        if router_bool(houses, mid) == 1:
            global answer
            answer = mid  # 미드가 정답일 수도 있으니까 일단 넣어둠
            return search(dis_range, mid+1, high)
        else:
            return search(dis_range, low, mid-1)

search(dis_range, dis_range[0], dis_range[-1])
print(answer)  # 거리는 3으로 가야 된다는 거 ..!
