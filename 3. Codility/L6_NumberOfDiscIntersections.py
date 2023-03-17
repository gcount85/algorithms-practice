def solution(A):  # Detected time complexity: O(N**2)
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


A = [1, 5, 2, 1, 4, 0]
print(solution(A))

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
