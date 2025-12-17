# 병합만 하는 병헙 정렬


def solution(arr1, arr2):
    """
    1. arr1, arr2 각각 포인터 설정
    2. while 두개의 포인터가 다 끝에 도달할 때까지:
        2-1. 두 개의 포인터가 위치가 모두 n-1 이하이면:
            2-2. 비교해서 더 작은 숫자를 새 배열에 담고, 해당 배열의 포인터를 1 증가
        2-2. 둘 중 하나가 n-1이면:
            2-2-1. n-1보다 작은 포인터를 그 위치부터 끝까지 새배열에 담고 반복문 종료시킴
    """
    n = len(arr1)
    m = len(arr2)
    p1, p2 = 0, 0
    ordered = []
    while True:
        if arr1[p1] < arr2[p2]:
            ordered.append(arr1[p1])
            p1 += 1
        else:
            ordered.append(arr2[p2])
            p2 += 1
        if p1 > n - 1:
            ordered.extend(arr2[p2:])
            break
        elif p2 > m - 1:
            ordered.extend(arr1[p1:])
            break

    return ordered


print(solution([1, 3, 5], [2, 4, 6]))  # [1, 2, 3, 4, 5, 6]
print(solution([1, 2, 3], [4, 5, 6]))  # [1, 2, 3, 4, 5, 6]
