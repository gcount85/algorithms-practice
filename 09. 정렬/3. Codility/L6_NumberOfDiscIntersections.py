def solution(A):  # Detected time complexity: O(N**2)
    '''
슈도코드:
    1. A 완전 탐색
    2. 겹치는 경우인지 판별 후 count 
    => O(N**2)라서 비효율적 

리턴:
    - 겹치는 원 쌍의 개수
    - 겹치는 원의 개수가 10000000 이상이면 -1

안 겹치는 경우: 
    - i끼리의 거리 > 두 원의 반지름 합
    '''

    count = 0

    for i, v in enumerate(A):
        e = len(A) - 1
        while e != i:
            if e-i <= (A[e] + v):
                count += 1
                if count > 10000000:
                    return -1
            e -= 1

    return count


def better_solution(A):  # Detected time complexity: O(N*log(N)) or O(N)
    '''
슈도코드:
    1. left edge, right edge 구분 
    2. 좌표상 위치, left edge를 기준으로 정렬(중요) 
    3. 정렬한 것들에 대해서
        1) left edge를 만나면 액티브 디스크 += 1
        2) right edge를 만나면 액티브 디스크 -= 1
    '''

    discs = []
    active_discs = 0
    intersect = 0

    for i, radius in enumerate(A):
        discs.append((i - radius, 1))
        discs.append((i + radius, -1))
    discs.sort(key=lambda x: (x[0], -x[1]))

    for _, edge in discs:
        if (edge == 1):
            intersect += active_discs
            if (intersect > 10000000):
                return -1
            active_discs += 1
        else:
            active_discs -= 1
    return intersect


A = [1, 5, 2, 1, 4, 0]
print(solution(A))
print(better_solution(A))
